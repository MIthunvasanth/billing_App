import asyncio

from app.config.settings import get_settings
from app.core.common.logger import get_logger
from app.core.context_manager import ContextManager
from app.dao.pg.job_dao import JobDAO
from app.service.extraction_service import ExtractionService

logger = get_logger(__name__)

# Recover stalled jobs on startup and every RECOVER_EVERY iterations.
# At the default 5-second poll interval this is approximately every 60 seconds.
_RECOVER_EVERY = 12


async def run() -> None:
    """Main worker loop. Runs indefinitely, polling for pending jobs.

    Uses two separate DB connections:
    - admin_cm (billing role, bypasses RLS) — for claim_next_job and recover_stalled,
      which must see all jobs across all users.
    - app_cm (billing_app role, subject to RLS) — for ExtractionService, which writes
      results under the job owner's identity via SET LOCAL app.current_user_id.
    """
    settings = get_settings()

    # billing role — owner, bypasses RLS; used for cross-user queue operations
    admin_cm = ContextManager(settings)
    await admin_cm.initialize()

    # billing_app role — subject to RLS; used for result writes with owner identity
    app_cm = ContextManager(
        settings,
        connection_string=settings.APP_DB_CONNECTION_STRING or settings.POSTGRES_CONNECTION_STRING,
    )
    await app_cm.initialize()

    admin_dao = JobDAO(admin_cm)
    extraction_service = ExtractionService(app_cm)

    logger.info("worker_started", poll_interval=settings.WORKER_POLL_INTERVAL_SECONDS)

    iteration = 0
    while True:
        try:
            # Recover stalled jobs on startup (iteration 0) and periodically.
            if iteration % _RECOVER_EVERY == 0:
                async with admin_cm.session() as session:
                    recovered = await admin_dao.recover_stalled(session)
                if recovered > 0:
                    logger.info("stalled_jobs_recovered", count=recovered)

            # Atomically claim the next pending job using the admin session so
            # RLS does not filter it out (app.current_user_id is not set here).
            async with admin_cm.session() as session:
                job = await admin_dao.claim_next_job(session)

            if job:
                logger.info("job_claimed", job_id=job["id"], user_id=job["user_id"])
                # ExtractionService uses app_cm and sets SET LOCAL app.current_user_id
                # = job["user_id"] before writing, so RLS enforces per-owner isolation.
                await extraction_service.process_job(
                    job_id=job["id"],
                    user_id=job["user_id"],
                )
            else:
                await asyncio.sleep(settings.WORKER_POLL_INTERVAL_SECONDS)

            iteration += 1

        except Exception:
            logger.exception("worker_loop_error")
            await asyncio.sleep(settings.WORKER_POLL_INTERVAL_SECONDS)
