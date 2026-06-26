from __future__ import annotations

import asyncio
from types import SimpleNamespace

from agents import Agent, Runner

from app.ai.agents.factory import AgentFactory
from app.ai.context import RunContext
from app.ai.types import Page
from app.core.common.logger import get_logger
from app.models.extraction import BillingRecord, ExtractionOutput, FlaggedRecord, PageClassification

_CHARS_PER_TOKEN = 4
_TARGET_TOKENS_PER_CHUNK = 60_000
_TARGET_CHARS_PER_CHUNK = _TARGET_TOKENS_PER_CHUNK * _CHARS_PER_TOKEN

# Characters of each page sent to the classifier (enough to judge row density)
_CLASSIFIER_PREVIEW_CHARS = 800

# Max concurrent OpenAI API calls — prevents 429s on large documents
_MAX_CONCURRENT_CHUNKS = 4


def _fix_payments_balance(record: BillingRecord) -> BillingRecord:
    """Deterministically correct the payments/balance column swap.

    Three cases handled in order:

    1. payments=None, balance=X where X ≈ expected:
       Model put the patient payment in balance instead of payments.
       Move balance → payments, set balance = 0.0.

    2. payments=X where X ≈ expected, balance ≈ 0:
       Model put the remaining balance amount in payments instead of balance.
       Move payments → balance, null payments.

    3. payments=0.0, expected ≈ 0:
       Empty column artefact. Null the 0.0 payment.
    """
    tc = record.total_charges
    ip = record.ins_paid
    adj = record.adjustment

    if tc is None or ip is None:
        return record

    # adj=None treated as 0.0 — common in pharmacy records where no adjustment column exists
    expected = round(tc - ip - (adj or 0.0), 2)

    # Case 1: payments missing but balance holds the patient payment amount
    if (
        record.payments is None
        and record.balance is not None
        and abs(record.balance - expected) < 0.02
        and expected > 0.02
    ):
        return record.model_copy(update={"payments": record.balance, "balance": 0.0})

    # Case 2: payments holds the balance value → swap
    if (
        record.payments is not None
        and record.balance is not None
        and abs(record.payments - expected) < 0.02
        and abs(record.balance) < 0.02
    ):
        return record.model_copy(update={"balance": record.payments, "payments": None})

    # Case 3: payments is explicit 0.0 but expected balance is also ~0.0 → null
    if record.payments == 0.0 and abs(expected) < 0.02:
        return record.model_copy(update={"payments": None})

    return record


def _build_chunks(pages: list[Page]) -> list[list[Page]]:
    """Token-aware chunking. Single oversized page gets its own chunk."""
    chunks: list[list[Page]] = []
    current: list[Page] = []
    current_chars = 0

    for page in pages:
        page_chars = len(page.page_content)
        if current and current_chars + page_chars > _TARGET_CHARS_PER_CHUNK:
            chunks.append(current)
            current = [page]
            current_chars = page_chars
        else:
            current.append(page)
            current_chars += page_chars

    if current:
        chunks.append(current)

    return chunks


class ExtractionAgentExecutor:
    """Two-phase extraction: classify summary pages, then extract in parallel chunks.

    Phase 1: Send short previews of all pages to a classifier agent.
             Classifier identifies which pages are summary/ledger pages.
    Phase 2: Extract only from summary pages (chunked + parallel).
             Fallback to all pages if no summary detected.

    This handles any document structure — summary page can be anywhere.
    """

    def __init__(
        self,
        agent: Agent[RunContext] | None = None,
        max_turns: int = 5,
        max_concurrent_chunks: int = _MAX_CONCURRENT_CHUNKS,
    ) -> None:
        self.agent = agent if agent is not None else AgentFactory.build_extraction_agent()
        self.classifier = AgentFactory.build_page_classifier_agent()
        self.max_turns = max(1, max_turns)
        self._semaphore = asyncio.Semaphore(max_concurrent_chunks)
        self.logger = get_logger(__name__)

    async def _classify_pages(self, ctx: RunContext) -> tuple[list[Page], int, int]:
        """Phase 1: identify summary pages. Returns (pages, input_tokens, output_tokens)."""
        previews = "\n\n".join(
            f"=== Page {p.page_num} ===\n{p.page_content[:_CLASSIFIER_PREVIEW_CHARS]}"
            for p in ctx.document.pages
        )
        prompt = (
            f"Document has {ctx.document.num_pages} pages. "
            f"Identify which pages are summary billing ledgers.\n\n{previews}"
        )

        result = await Runner.run(
            self.classifier,
            prompt,
            context=ctx,
            max_turns=3,
        )

        u = result.context_wrapper.usage
        inp = getattr(u, "input_tokens", 0) or 0
        out = getattr(u, "output_tokens", 0) or 0

        classification: PageClassification = result.final_output

        self.logger.info(
            "page_classification_done",
            doc_id=ctx.document.doc_id,
            has_summary=classification.has_summary,
            summary_pages=classification.summary_pages,
            classifier_input_tokens=inp,
            classifier_output_tokens=out,
        )

        if classification.has_summary and classification.summary_pages:
            summary_set = set(classification.summary_pages)
            selected = [p for p in ctx.document.pages if p.page_num in summary_set]
            if selected:
                return selected, inp, out

        # Fallback: extract from all pages
        self.logger.info(
            "no_summary_found_using_all_pages",
            doc_id=ctx.document.doc_id,
        )
        return ctx.document.pages, inp, out

    async def _run_chunk(
        self,
        ctx: RunContext,
        chunk_pages: list[Page],
        chunk_idx: int,
        total_chunks: int,
    ) -> tuple[ExtractionOutput, int, int]:
        """Phase 2: extract one chunk, return (output, input_tokens, output_tokens)."""
        user_text = ctx.prompt_loader.render(
            "extraction/user.j2",
            {
                "doc_id": ctx.document.doc_id,
                "total_pages": ctx.document.num_pages,
                "pages": [
                    {"page_num": p.page_num, "page_content": p.page_content}
                    for p in chunk_pages
                ],
            },
        )

        async with self._semaphore:
            result = await Runner.run(
                self.agent,
                user_text,
                context=ctx,
                max_turns=self.max_turns,
            )

        u = result.context_wrapper.usage
        inp = getattr(u, "input_tokens", 0) or 0
        out = getattr(u, "output_tokens", 0) or 0

        self.logger.info(
            "chunk_completed",
            doc_id=ctx.document.doc_id,
            chunk=chunk_idx + 1,
            total_chunks=total_chunks,
            pages=[p.page_num for p in chunk_pages],
            records=len(result.final_output.records),
        )

        return result.final_output, inp, out

    async def run(self, ctx: RunContext) -> tuple[ExtractionOutput, object]:
        """Run two-phase extraction and return (ExtractionOutput, combined_usage)."""
        self.logger.info(
            "extraction_agent_started",
            doc_id=ctx.document.doc_id,
            num_pages=ctx.document.num_pages,
        )

        # Phase 1: classify (tokens counted toward totals below)
        pages_to_extract, cls_inp, cls_out = await self._classify_pages(ctx)

        # Safety: if classifier selected < 30% of pages on a 3+ page doc, it
        # was too selective (found one summary page and missed everything else).
        # Fall back to all pages so large multi-record docs get full coverage.
        all_pages = ctx.document.pages
        min_threshold = max(1, len(all_pages) * 0.3)
        if len(all_pages) >= 3 and len(pages_to_extract) < min_threshold:
            self.logger.info(
                "classifier_fallback_to_all_pages",
                doc_id=ctx.document.doc_id,
                selected=len(pages_to_extract),
                total=len(all_pages),
                threshold=min_threshold,
            )
            pages_to_extract = all_pages

        chunks = _build_chunks(pages_to_extract)

        self.logger.info(
            "extraction_phase2_start",
            doc_id=ctx.document.doc_id,
            pages_selected=len(pages_to_extract),
            num_chunks=len(chunks),
        )

        # Phase 2: parallel extraction
        chunk_results = await asyncio.gather(
            *[
                self._run_chunk(ctx, chunk_pages, i, len(chunks))
                for i, chunk_pages in enumerate(chunks)
            ]
        )

        all_records = []
        all_flagged: list[FlaggedRecord] = []
        total_input = cls_inp
        total_output = cls_out

        for chunk_output, inp, out in chunk_results:
            record_offset = len(all_records)
            for flag in chunk_output.flagged:
                if flag.row is not None:
                    flag = flag.model_copy(update={"row": flag.row + record_offset})
                all_flagged.append(flag)
            all_records.extend(_fix_payments_balance(r) for r in chunk_output.records)
            total_input += inp
            total_output += out

        total_pages = len(ctx.document.pages)
        records_per_page = len(all_records) / max(1, total_pages)
        if records_per_page > 20:
            all_flagged.append(
                FlaggedRecord(
                    row=None,
                    fields=["treatment_date"],
                    reason=(
                        f"Possible over-extraction: {len(all_records)} records from {total_pages} pages "
                        f"({records_per_page:.0f}/page). Document may have been extracted at line-item "
                        f"level instead of summary level."
                    ),
                    page="1",
                    severity="high",
                )
            )
            self.logger.warning(
                "over_extraction_detected",
                doc_id=ctx.document.doc_id,
                records=len(all_records),
                total_pages=total_pages,
                records_per_page=records_per_page,
            )

        self.logger.info(
            "extraction_agent_completed",
            doc_id=ctx.document.doc_id,
            records=len(all_records),
            flagged=len(all_flagged),
            total_input_tokens=total_input,
            total_output_tokens=total_output,
        )

        combined_usage = SimpleNamespace(
            input_tokens=total_input,
            output_tokens=total_output,
        )
        return ExtractionOutput(records=all_records, flagged=all_flagged), combined_usage
