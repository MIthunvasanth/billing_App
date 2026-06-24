import time

import pdfplumber
from sqlalchemy import text

from app.ai.agents.extraction.executor import ExtractionAgentExecutor
from app.ai.agents.factory import AgentFactory
from app.ai.context import RunContext
from app.ai.prompts.prompt_loader import PromptLoader
from app.ai.types import Document, Page
from app.core.context_manager import ContextManager
from app.dao.pg.job_dao import JobDAO
from app.service.base_service import BaseService


class ExtractionService(BaseService):
    """Owns the extraction pipeline for a single job.

    Called by the worker loop with a job_id and user_id. Responsible for:
    - Loading the PDF from the mounted volume
    - Building RunContext and running ExtractionAgentExecutor
    - Writing the extraction result or error back to the job record

    This service is the bridge between the job queue and the AI layer.
    Never raises — all exceptions must be caught and written to the job
    error field so the worker loop stays alive.
    """

    def __init__(self, context_manager: ContextManager) -> None:
        super().__init__(context_manager)
        self.job_dao = JobDAO(context_manager)

    async def process_job(self, job_id: str, user_id: str) -> None:
        """Run the full extraction pipeline for a job.

        user_id is the job owner. Every DB session opened here calls
        SET LOCAL app.current_user_id = user_id before any DML so RLS
        policies enforce per-owner isolation on the result write.

        Must never raise — catch all exceptions and write to job.error.
        """
        start = time.monotonic()

        # Fetch job to get pdf_path — set identity so RLS allows the read
        async with self.context_manager.session() as session:
            await session.execute(
                text("SET LOCAL app.current_user_id = :uid"), {"uid": user_id}
            )
            job = await self.job_dao.get(session, job_id)

        if not job:
            self.logger.error("job_not_found_in_extraction", job_id=job_id)
            return

        try:
            # Parse PDF pages with pdfplumber
            pages: list[Page] = []
            with pdfplumber.open(job["pdf_path"]) as pdf:
                for i, pdf_page in enumerate(pdf.pages):
                    page_text = pdf_page.extract_text() or ""
                    pages.append(Page(page_num=i + 1, page_content=page_text))

            doc = Document(doc_id=job_id, num_pages=len(pages), pages=pages)
            ctx = RunContext(document=doc, prompt_loader=PromptLoader())

            agent = AgentFactory.build_extraction_agent()
            executor = ExtractionAgentExecutor(agent, max_turns=25)
            extraction_output, usage = await executor.run(ctx)

            duration = time.monotonic() - start
            input_tokens = getattr(usage, "input_tokens", 0) or 0
            output_tokens = getattr(usage, "output_tokens", 0) or 0
            token_usage = {
                "input": input_tokens,
                "output": output_tokens,
                "total": input_tokens + output_tokens,
            }
            # gpt-4o-mini pricing: $0.15/1M input tokens, $0.60/1M output tokens
            cost_usd = (input_tokens * 0.00000015) + (output_tokens * 0.0000006)

            result_data = {
                "records": [r.model_dump() for r in extraction_output.records],
                "flagged": [f.model_dump() for f in extraction_output.flagged],
            }

            async with self.context_manager.session() as session:
                await session.execute(
                    text("SET LOCAL app.current_user_id = :uid"), {"uid": user_id}
                )
                await self.job_dao.update_status(
                    session,
                    job_id,
                    status="completed",
                    result=result_data,
                    token_usage=token_usage,
                    cost_usd=cost_usd,
                    processing_duration_seconds=duration,
                )

            self.logger.info(
                "job_completed",
                job_id=job_id,
                records=len(extraction_output.records),
                flagged=len(extraction_output.flagged),
                cost_usd=round(cost_usd, 6),
                duration_seconds=round(duration, 2),
            )

        except Exception as exc:
            duration = time.monotonic() - start
            self.logger.error("extraction_failed", job_id=job_id, error=str(exc))
            try:
                async with self.context_manager.session() as session:
                    await session.execute(
                        text("SET LOCAL app.current_user_id = :uid"), {"uid": user_id}
                    )
                    await self.job_dao.update_status(
                        session,
                        job_id,
                        status="failed",
                        error=str(exc),
                        processing_duration_seconds=duration,
                    )
            except Exception as write_exc:
                self.logger.error(
                    "failed_to_write_failure",
                    job_id=job_id,
                    error=str(write_exc),
                )
