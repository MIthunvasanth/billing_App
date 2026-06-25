from fastapi import HTTPException, Request
from sqlalchemy import text


async def get_current_user_id(request: Request) -> str:
    """FastAPI dependency — validates Bearer token and returns the authenticated user_id.

    Reads Authorization: Bearer <token> header, looks up the session in the
    database via admin_cm (billing role, full access to session table),
    and returns the userId string.

    Raises:
        HTTPException(401): if the header is missing, malformed, or the token
            is not found / has expired.
    """
    auth_header = request.headers.get("Authorization", "")
    if not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or malformed auth token")
    token = auth_header[len("Bearer "):].strip()
    if not token:
        raise HTTPException(status_code=401, detail="Missing auth token")

    admin_cm = request.app.state.admin_cm
    async with admin_cm.session() as session:
        result = await session.execute(
            text(
                'SELECT "userId" FROM session'
                ' WHERE token = :token AND "expiresAt" > NOW()'
            ),
            {"token": token},
        )
        row = result.one_or_none()

    if row is None:
        raise HTTPException(status_code=401, detail="Invalid or expired session")
    return str(row[0])
