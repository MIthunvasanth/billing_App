import asyncio
import uuid
from pathlib import Path

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.config.settings import get_settings
from app.core.context_manager import ContextManager
from app.dao.pg.job_dao import JobDAO
from app.service.base_service import BaseService
from app.service.exceptions import JobNotFoundException, JobNotCancellableException


class JobService(BaseService):
    """Owns the job lifecycle: creation, status queries, and cancellation.

    All database access goes through JobDAO. This service does not interact
    with the AI layer — that is ExtractionService's responsibility.
    """

    def __init__(self, context_manager: ContextManager) -> None:
        super().__init__(context_manager)
        self.job_dao = JobDAO(context_manager)
        self._settings = get_settings()

    async def _set_user_identity(self, session: AsyncSession, user_id: str) -> None:
        """Propagate caller identity into the DB session so RLS policies can act on it."""
        await session.execute(
            text("SELECT set_config('app.current_user_id', :uid, true)"),
            {"uid": str(user_id)},
        )

    async def create_job(
        self,
        user_id: str,
        pdf_filename: str,
        pdf_bytes: bytes,
        content_hash: str | None = None,
    ) -> dict:
        # TODO (M3): content-hash cache check goes here.
        # Query job_dao for a completed job with same user_id + content_hash.
        # If found, return a new job row in completed status reusing cached result.
        # Skip if content_hash is None or if cache-bypass flag was passed by caller.

        file_uuid = str(uuid.uuid4())
        pdf_dir = Path(self._settings.PDF_MOUNT_PATH)
        saved_path = pdf_dir / f"{file_uuid}.pdf"

        # Write PDF to disk before opening a DB transaction — no reason to hold
        # a connection open during filesystem I/O.
        await asyncio.to_thread(pdf_dir.mkdir, parents=True, exist_ok=True)
        await asyncio.to_thread(saved_path.write_bytes, pdf_bytes)

        async with self.context_manager.session() as session:
            await self._set_user_identity(session, user_id)
            return await self.job_dao.create(
                session,
                user_id=uuid.UUID(user_id),
                pdf_filename=pdf_filename,
                pdf_path=str(saved_path),
                content_hash=content_hash,
            )

    async def get_job(self, user_id: str, job_id: str) -> dict:
        async with self.context_manager.session() as session:
            await self._set_user_identity(session, user_id)
            job = await self.job_dao.get(session, job_id)
            if job is None:
                raise JobNotFoundException(job_id)
            return job

    async def list_jobs(self, user_id: str, status: str | None = None) -> list[dict]:
        async with self.context_manager.session() as session:
            await self._set_user_identity(session, user_id)
            return await self.job_dao.list(session, status=status)

    async def get_active_jobs(self, user_id: str) -> list[dict]:
        async with self.context_manager.session() as session:
            await self._set_user_identity(session, user_id)
            return await self.job_dao.get_active(session)

    async def cancel_job(self, user_id: str, job_id: str) -> dict:
        async with self.context_manager.session() as session:
            await self._set_user_identity(session, user_id)
            cancelled = await self.job_dao.cancel(session, job_id)
            if cancelled is not None:
                return cancelled
            # cancel() returns None when no pending row matched — distinguish
            # "not found" from "wrong status" so the API can return 404 vs 409.
            existing = await self.job_dao.get(session, job_id)
            if existing is None:
                raise JobNotFoundException(job_id)
            raise JobNotCancellableException(job_id, existing["status"])
