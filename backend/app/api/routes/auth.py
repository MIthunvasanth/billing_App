import secrets
import uuid
from datetime import datetime, timedelta, timezone

import bcrypt
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from sqlalchemy import text

router = APIRouter()


class RegisterRequest(BaseModel):
    email: str
    password: str
    name: str


class LoginRequest(BaseModel):
    email: str
    password: str


def _session_expiry() -> datetime:
    return datetime.now(timezone.utc) + timedelta(days=30)


@router.post("/register", status_code=201)
async def register(body: RegisterRequest, request: Request) -> dict:
    """Create a new user account and return a session token."""
    admin_cm = request.app.state.admin_cm

    async with admin_cm.session() as session:
        # Check email uniqueness
        existing = await session.execute(
            text('SELECT id FROM "user" WHERE email = :email'),
            {"email": body.email},
        )
        if existing.one_or_none() is not None:
            raise HTTPException(status_code=409, detail="Email already registered")

        user_id = str(uuid.uuid4())
        now = datetime.now(timezone.utc)
        hashed = bcrypt.hashpw(body.password.encode(), bcrypt.gensalt()).decode()
        token = secrets.token_urlsafe(32)
        expires_at = _session_expiry()

        await session.execute(
            text(
                'INSERT INTO "user" (id, name, email, "emailVerified", "createdAt", "updatedAt")'
                " VALUES (:id, :name, :email, FALSE, :now, :now)"
            ),
            {"id": user_id, "name": body.name, "email": body.email, "now": now},
        )
        await session.execute(
            text(
                'INSERT INTO account (id, "accountId", "providerId", "userId", password, "createdAt", "updatedAt")'
                " VALUES (:id, :account_id, 'credential', :user_id, :password, :now, :now)"
            ),
            {
                "id": str(uuid.uuid4()),
                "account_id": user_id,
                "user_id": user_id,
                "password": hashed,
                "now": now,
            },
        )
        await session.execute(
            text(
                'INSERT INTO session (id, token, "expiresAt", "userId", "createdAt", "updatedAt")'
                " VALUES (:id, :token, :expires_at, :user_id, :now, :now)"
            ),
            {
                "id": str(uuid.uuid4()),
                "token": token,
                "expires_at": expires_at,
                "user_id": user_id,
                "now": now,
            },
        )

    return {
        "token": token,
        "user": {"id": user_id, "email": body.email, "name": body.name},
    }


@router.post("/login")
async def login(body: LoginRequest, request: Request) -> dict:
    """Authenticate with email/password and return a new session token."""
    admin_cm = request.app.state.admin_cm

    async with admin_cm.session() as session:
        user_row = await session.execute(
            text('SELECT id, name FROM "user" WHERE email = :email'),
            {"email": body.email},
        )
        user = user_row.one_or_none()
        if user is None:
            raise HTTPException(status_code=401, detail="Invalid credentials")

        user_id, user_name = user[0], user[1]

        account_row = await session.execute(
            text(
                "SELECT password FROM account"
                ' WHERE "userId" = :user_id AND "providerId" = \'credential\''
            ),
            {"user_id": user_id},
        )
        account = account_row.one_or_none()
        if account is None or not bcrypt.checkpw(
            body.password.encode(), account[0].encode()
        ):
            raise HTTPException(status_code=401, detail="Invalid credentials")

        now = datetime.now(timezone.utc)
        token = secrets.token_urlsafe(32)
        expires_at = _session_expiry()

        await session.execute(
            text(
                'INSERT INTO session (id, token, "expiresAt", "userId", "createdAt", "updatedAt")'
                " VALUES (:id, :token, :expires_at, :user_id, :now, :now)"
            ),
            {
                "id": str(uuid.uuid4()),
                "token": token,
                "expires_at": expires_at,
                "user_id": user_id,
                "now": now,
            },
        )

    return {
        "token": token,
        "user": {"id": user_id, "email": body.email, "name": user_name},
    }
