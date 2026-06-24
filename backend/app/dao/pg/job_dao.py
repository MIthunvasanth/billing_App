import uuid
from decimal import Decimal
from typing import Any

import sqlalchemy as sa
from sqlalchemy import select, text, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.context_manager import ContextManager
from app.dao.base_pg_dao import BasePgDAO
from app.dao.models.job import Job


class JobDAO(BasePgDAO[Job]):
    """Data access for the jobs table.

    All SQL lives here. No business logic — status transition rules
    belong in JobService, not here.
    """

    def __init__(self, context_manager: ContextManager) -> None:
        super().__init__(context_manager, Job)

    # ------------------------------------------------------------------ helpers

    def _to_orm(self, data: dict) -> Job:
        return Job(
            user_id=data["user_id"],
            pdf_filename=data["pdf_filename"],
            pdf_path=data["pdf_path"],
            status=data.get("status", "pending"),
            content_hash=data.get("content_hash"),
        )

    def _to_dto(self, orm: Job) -> dict:
        def _conv(v: Any) -> Any:
            if isinstance(v, uuid.UUID):
                return str(v)
            if isinstance(v, Decimal):
                return float(v)
            if hasattr(v, "isoformat"):
                return v.isoformat()
            return v

        return {
            attr.key: _conv(getattr(orm, attr.key))
            for attr in Job.__mapper__.column_attrs
        }

    def _apply_filters(self, query: Any, filters: dict) -> Any:
        if filters.get("status") is not None:
            query = query.where(Job.status == filters["status"])
        return query

    def _row_to_dto(self, row: dict) -> dict:
        """Serialize a raw DB row mapping (from text() RETURNING) to a plain dict."""
        def _conv(v: Any) -> Any:
            if isinstance(v, uuid.UUID):
                return str(v)
            if isinstance(v, Decimal):
                return float(v)
            if hasattr(v, "isoformat"):
                return v.isoformat()
            return v

        return {k: _conv(v) for k, v in row.items()}

    # ------------------------------------------------------------------ public

    async def create(
        self,
        session: AsyncSession,
        user_id: uuid.UUID,
        pdf_filename: str,
        pdf_path: str,
        content_hash: str | None = None,
    ) -> dict:
        job = Job(
            user_id=user_id,
            pdf_filename=pdf_filename,
            pdf_path=pdf_path,
            status="pending",
            content_hash=content_hash,
        )
        session.add(job)
        await session.flush()
        await session.refresh(job)
        return self._to_dto(job)

    async def get(self, session: AsyncSession, job_id: str) -> dict | None:
        result = await session.execute(select(Job).where(Job.id == job_id))
        job = result.scalar_one_or_none()
        return self._to_dto(job) if job else None

    async def list(self, session: AsyncSession, status: str | None = None) -> list[dict]:
        query = select(Job).order_by(Job.created_at.desc())
        if status is not None:
            query = query.where(Job.status == status)
        result = await session.execute(query)
        return [self._to_dto(j) for j in result.scalars().all()]

    async def get_active(self, session: AsyncSession) -> list[dict]:
        result = await session.execute(
            select(Job)
            .where(Job.status == "processing")
            .order_by(Job.started_at.desc())
        )
        return [self._to_dto(j) for j in result.scalars().all()]

    async def update_status(
        self,
        session: AsyncSession,
        job_id: str,
        status: str,
        result: dict | None = None,
        error: str | None = None,
        token_usage: dict | None = None,
        cost_usd: float | None = None,
        processing_duration_seconds: float | None = None,
    ) -> dict | None:
        values: dict[str, Any] = {"status": status, "updated_at": sa.func.now()}
        if result is not None:
            values["result"] = result
        if error is not None:
            values["error"] = error
        if token_usage is not None:
            values["token_usage"] = token_usage
        if cost_usd is not None:
            values["cost_usd"] = cost_usd
        if processing_duration_seconds is not None:
            values["processing_duration_seconds"] = processing_duration_seconds
        if status == "processing":
            values["started_at"] = sa.func.now()
        if status in ("completed", "failed", "cancelled"):
            values["completed_at"] = sa.func.now()

        stmt = (
            update(Job)
            .where(Job.id == job_id)
            .values(**values)
            .returning(Job)
        )
        row = await session.execute(stmt)
        job = row.scalars().one_or_none()
        return self._to_dto(job) if job else None

    async def cancel(self, session: AsyncSession, job_id: str) -> dict | None:
        stmt = (
            update(Job)
            .where(Job.id == job_id, Job.status == "pending")
            .values(
                status="cancelled",
                completed_at=sa.func.now(),
                updated_at=sa.func.now(),
            )
            .returning(Job)
        )
        row = await session.execute(stmt)
        job = row.scalars().one_or_none()
        return self._to_dto(job) if job else None

    async def claim_next_job(self, session: AsyncSession) -> dict | None:
        # TODO: caller MUST pass an admin session (POSTGRES_CONNECTION_STRING / billing role).
        # billing_app is subject to RLS; with app.current_user_id unset at claim time,
        # current_setting('app.current_user_id', true) returns NULL and the SELECT policy
        # matches 0 rows. billing (table owner) bypasses RLS without FORCE.
        # Wired in worker/loop.py — see worker implementation step.
        stmt = text("""
            WITH claimed AS (
                SELECT id FROM jobs
                WHERE status = 'pending'
                ORDER BY created_at
                LIMIT 1
                FOR UPDATE SKIP LOCKED
            )
            UPDATE jobs
            SET status     = 'processing',
                started_at = now(),
                updated_at = now()
            FROM claimed
            WHERE jobs.id = claimed.id
            RETURNING jobs.*
        """)
        result = await session.execute(stmt)
        row = result.mappings().one_or_none()
        return self._row_to_dto(dict(row)) if row else None

    async def recover_stalled(self, session: AsyncSession, timeout_minutes: int = 5) -> int:
        # timeout_minutes is an internal integer — not user input, no injection risk.
        stmt = (
            update(Job)
            .where(
                Job.status == "processing",
                Job.started_at
                < sa.func.now()
                - sa.literal_column(f"interval '{timeout_minutes} minutes'"),
            )
            .values(status="pending", started_at=None, updated_at=sa.func.now())
        )
        result = await session.execute(stmt)
        return result.rowcount
