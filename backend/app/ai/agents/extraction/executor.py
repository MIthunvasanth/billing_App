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
_TARGET_TOKENS_PER_CHUNK = 10_000
_TARGET_CHARS_PER_CHUNK = _TARGET_TOKENS_PER_CHUNK * _CHARS_PER_TOKEN  # 40_000

# Characters of each page sent to the classifier (enough to judge row density)
_CLASSIFIER_PREVIEW_CHARS = 800

# Max concurrent OpenAI API calls — prevents 429s on large documents
_MAX_CONCURRENT_CHUNKS = 4


def _fix_payments_balance(record: BillingRecord) -> BillingRecord:
    """Deterministically correct the payments/balance column swap."""
    tc = record.total_charges
    ip = record.ins_paid
    adj = record.adjustment

    if tc is None or ip is None:
        return record

    expected = round((tc or 0) - (ip or 0) - (adj or 0), 2)

    # Case 1: payments missing, balance holds the patient payment amount
    if (
        record.payments is None
        and record.balance is not None
        and abs(record.balance - expected) < 0.02
        and expected > 0.02
    ):
        record.payments = record.balance
        record.balance = 0.0
        return record

    # Case 2: payments holds the outstanding balance (amount still owed, not paid)
    if record.payments is not None and record.balance == 0.0 and expected > 0.02:
        if abs(record.payments - expected) < 0.02:
            record.balance = record.payments
            record.payments = None
            return record

    # Case 3: payments is explicit 0.0 but expected balance is also ~0.0 → null
    if record.payments == 0.0 and abs(expected) < 0.02:
        record.payments = None
        return record

    return record


def _parse_dates_from_record(record: BillingRecord) -> list:
    from datetime import datetime
    dates = []
    d = record.treatment_date.strip().replace("–", "-").replace("—", "-")
    for part in d.split(" - "):
        part = part.strip()
        try:
            dates.append(datetime.strptime(part, "%m/%d/%Y"))
        except ValueError:
            pass
    return dates


def _merge_patient_records(records: list[BillingRecord]) -> list[BillingRecord]:
    """After parallel chunk extraction, merge records for the same encounter split across chunk boundaries.

    Groups by (provider, sorted_cpt_codes, normalized_treatment_date). Only merges records
    with the same date — this covers the case where one encounter spans a chunk boundary
    and both chunks emit a partial record for the same visit. Records with different dates
    are distinct visits and must NOT be merged.
    """
    from collections import defaultdict
    from datetime import datetime

    def _norm_date(d: str) -> str:
        return d.strip().replace("–", "-").replace("—", "-")

    groups: dict[tuple, list[BillingRecord]] = defaultdict(list)
    for r in records:
        key = (r.provider.strip().lower(), tuple(sorted(set(r.cpt_codes))), _norm_date(r.treatment_date))
        groups[key].append(r)

    merged: list[BillingRecord] = []
    for group in groups.values():
        if len(group) == 1:
            merged.append(group[0])
            continue

        all_dates: list[datetime] = []
        for r in group:
            all_dates.extend(_parse_dates_from_record(r))

        if all_dates:
            d0 = min(all_dates).strftime("%m/%d/%Y")
            d1 = max(all_dates).strftime("%m/%d/%Y")
            merged_date = f"{d0} - {d1}" if d0 != d1 else d0
        else:
            merged_date = group[0].treatment_date

        def _sum(field: str) -> float | None:
            vals = [getattr(r, field) for r in group if getattr(r, field) is not None]
            return round(sum(vals), 2) if vals else None

        all_cpts: list[str] = []
        all_ins: list[str] = []
        all_thirds: list[str] = []
        for r in group:
            all_cpts.extend(r.cpt_codes)
            all_ins.extend(r.insurers)
            all_thirds.extend(r.third_parties)

        merged.append(BillingRecord(
            treatment_date=merged_date,
            cpt_codes=list(dict.fromkeys(all_cpts)),
            description=next((r.description for r in group if r.description), None),
            provider=group[0].provider,
            insurers=list(dict.fromkeys(all_ins)),
            third_parties=list(dict.fromkeys(all_thirds)),
            total_charges=_sum("total_charges"),
            ins_paid=_sum("ins_paid"),
            adjustment=_sum("adjustment"),
            payments=_sum("payments"),
            balance=_sum("balance"),
            page=group[0].page,
        ))

    return merged



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

        # Cross-chunk dedup: merge records for the same patient split across chunk boundaries
        # Groups by (provider, cpt_codes) — same procedure set at same provider = same patient
        pre_merge_count = len(all_records)
        all_records = _merge_patient_records(all_records)
        post_merge_count = len(all_records)
        if post_merge_count != pre_merge_count:
            self.logger.info(
                "cross_chunk_merge",
                doc_id=ctx.document.doc_id,
                before=pre_merge_count,
                after=post_merge_count,
            )

        total_pages = len(ctx.document.pages)
        records_per_page = len(all_records) / max(1, total_pages)
        if records_per_page > 20:
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
