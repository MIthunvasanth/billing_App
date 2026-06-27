"""Evaluate extraction accuracy against ground truth for all docs in data/.

Usage:
    cd <repo_root>
    uv run --project backend python scripts/eval_extraction.py

Outputs:
    docs-test/<doc_id>.json  — raw extraction result per document
    docs-test/result.md      — comparison report vs ground truth
"""
from __future__ import annotations

import asyncio
import json
import os
import sys
import time
import traceback
from pathlib import Path

# Resolve paths first — needed for both .env loading and sys.path
REPO_ROOT = Path(__file__).resolve().parents[1]
BACKEND_DIR = REPO_ROOT / "backend"
sys.path.insert(0, str(BACKEND_DIR))

# Load .env from repo root so OPENAI_API_KEY is available before openai-agents imports
_env_path = REPO_ROOT / ".env"
if _env_path.exists():
    for _line in _env_path.read_text(encoding="utf-8").splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            os.environ.setdefault(_k.strip(), _v.strip())

import pdfplumber  # noqa: E402 (after sys.path patch)

from app.ai.agents.extraction.executor import ExtractionAgentExecutor  # noqa: E402
from app.ai.agents.factory import AgentFactory  # noqa: E402
from app.ai.context import RunContext  # noqa: E402
from app.ai.prompts.prompt_loader import PromptLoader  # noqa: E402
from app.ai.types import Document, Page  # noqa: E402
from app.models.extraction import ExtractionOutput  # noqa: E402

DATA_DIR = REPO_ROOT / "data"
DOCS_TEST_DIR = REPO_ROOT / "docs-test"
RESULT_MD = DOCS_TEST_DIR / "result.md"

# Ground truth uses camelCase — map to our snake_case model fields
GT_FIELD_MAP: dict[str, str] = {
    "treatmentDate": "treatment_date",
    "cptCodes": "cpt_codes",
    "description": "description",
    "provider": "provider",
    "insurers": "insurers",
    "thirdParties": "third_parties",
    "totalCharges": "total_charges",
    "insPaid": "ins_paid",
    "adjustment": "adjustment",
    "payments": "payments",
    "balance": "balance",
    "page": "page",
}

FLOAT_FIELDS = {"total_charges", "ins_paid", "adjustment", "payments", "balance"}
FLOAT_TOL = 0.02  # 2-cent tolerance for float comparison

# Scored fields (page excluded — format differs intentionally)
SCORED_FIELDS = [
    "treatment_date",
    "cpt_codes",
    "total_charges",
    "ins_paid",
    "adjustment",
    "payments",
    "balance",
    "provider",
    "insurers",
    "third_parties",
    "description",
]

# Field weights per CLAUDE.md spec
FIELD_WEIGHTS: dict[str, float] = {
    "treatment_date": 3.0,
    "cpt_codes": 3.0,
    "total_charges": 3.0,
    "ins_paid": 3.0,
    "adjustment": 3.0,
    "payments": 3.0,
    "balance": 3.0,
    "provider": 2.0,
    "page": 2.0,
    "insurers": 2.0,
    "third_parties": 2.0,
    "description": 1.0,
}


# ---------------------------------------------------------------------------
# Normalisation
# ---------------------------------------------------------------------------

def normalize_gt(gt: dict) -> dict:
    """Convert GT camelCase dict → snake_case with same values."""
    return {GT_FIELD_MAP[k]: v for k, v in gt.items() if k in GT_FIELD_MAP}


# ---------------------------------------------------------------------------
# Field comparison
# ---------------------------------------------------------------------------

def compare_field(field: str, extracted, expected) -> tuple[bool, str]:
    """Return (match, detail_note)."""
    if field in FLOAT_FIELDS:
        if extracted is None and expected is None:
            return True, ""
        if extracted is None or expected is None:
            return False, f"extracted={extracted!r}  expected={expected!r}"
        diff = abs(float(extracted) - float(expected))
        if diff <= FLOAT_TOL:
            return True, ""
        return False, f"extracted={extracted}  expected={expected}  diff={diff:.2f}"

    if field == "cpt_codes":
        ext = sorted(str(c) for c in (extracted or []))
        exp = sorted(str(c) for c in (expected or []))
        if ext == exp:
            return True, ""
        missing = sorted(set(exp) - set(ext))
        extra = sorted(set(ext) - set(exp))
        parts = []
        if missing:
            parts.append(f"missing={missing}")
        if extra:
            parts.append(f"extra={extra}")
        return False, "  ".join(parts)

    if field in ("insurers", "third_parties"):
        ext_set = {s.lower().strip() for s in (extracted or [])}
        exp_set = {s.lower().strip() for s in (expected or [])}
        if ext_set == exp_set:
            return True, ""
        missing = sorted(exp_set - ext_set)
        extra = sorted(ext_set - exp_set)
        parts = []
        if missing:
            parts.append(f"missing={missing}")
        if extra:
            parts.append(f"extra={extra}")
        return False, "  ".join(parts)

    if field == "page":
        # page format legitimately differs between summary vs detail view;
        # score as informational only, not counted in accuracy
        return True, "(not scored)"

    if field == "treatment_date":
        def _norm_date(s: str) -> str:
            # Normalize em dash (–, U+2013) and en dash (–, U+2014) to hyphen-minus
            return s.strip().replace("–", "-").replace("—", "-")
        ext_str = _norm_date(str(extracted or ""))
        exp_str = _norm_date(str(expected or ""))
        if ext_str == exp_str:
            return True, ""
        # Extracted has range suffix: extracted "07/28/2024 - 12/31/2024", GT "07/28/2024"
        if ext_str.startswith(exp_str):
            return True, f"(extracted has range suffix: {ext_str!r})"
        # GT has range, extracted has start date only: GT "07/28/2024 - 12/31/2024", extracted "07/28/2024"
        if exp_str.startswith(ext_str) and len(ext_str) >= 10:
            return True, f"(gt has range suffix: {exp_str!r})"
        return False, f"extracted={ext_str!r}  expected={exp_str!r}"

    # Generic string / null comparison
    ext_str = str(extracted or "").strip().lower()
    exp_str = str(expected or "").strip().lower()
    if ext_str == exp_str:
        return True, ""
    return False, f"extracted={extracted!r}  expected={expected!r}"


# ---------------------------------------------------------------------------
# Record matching
# ---------------------------------------------------------------------------

def find_best_match(extracted_records: list[dict], gt_norm: dict) -> dict | None:
    """Match GT record to best extracted record by treatment_date + total_charges."""
    date = gt_norm.get("treatment_date", "")
    tc = gt_norm.get("total_charges")

    # Filter by date — handle both directions:
    # 1. Extracted has range suffix:  extracted "07/28/2024 - 12/31/2024", GT "07/28/2024"
    # 2. GT has range, extracted has start date: GT "07/28/2024 - 12/31/2024", extracted "07/28/2024"
    def _date_matches(ext_date: str, gt_date: str) -> bool:
        # Normalize em dash / en dash to hyphen-minus before comparing
        ext = ext_date.strip().replace("–", "-").replace("—", "-")
        gt = gt_date.strip().replace("–", "-").replace("—", "-")
        if ext == gt:
            return True
        if ext.startswith(gt):
            return True
        # GT range starts with extracted start date (len >= 10 guards against empty prefix matching)
        if gt.startswith(ext) and len(ext) >= 10:
            return True
        return False

    by_date = [
        r for r in extracted_records
        if _date_matches(str(r.get("treatment_date", "")), date)
    ]

    if not by_date:
        return None
    if len(by_date) == 1:
        return by_date[0]

    # Disambiguate by total_charges
    if tc is not None:
        for r in by_date:
            rtc = r.get("total_charges")
            if rtc is not None and abs(float(rtc) - float(tc)) <= FLOAT_TOL:
                return r

    return by_date[0]


# ---------------------------------------------------------------------------
# Per-document evaluation
# ---------------------------------------------------------------------------

def evaluate_doc(doc_id: str, extracted: list[dict], gt_records: list[dict]) -> dict:
    gt_norms = [normalize_gt(r) for r in gt_records]

    field_hits: dict[str, list[bool]] = {f: [] for f in SCORED_FIELDS}
    errors: list[dict] = []
    matched_ext_ids: set[int] = set()

    for i, gt_norm in enumerate(gt_norms):
        match = find_best_match(extracted, gt_norm)

        if match is None:
            errors.append({
                "type": "missing_record",
                "gt_index": i,
                "treatment_date": gt_norm.get("treatment_date"),
                "note": "No extracted record found with this treatment_date",
            })
            for f in SCORED_FIELDS:
                field_hits[f].append(False)
            continue

        # Track which extracted records were matched
        for j, r in enumerate(extracted):
            if r is match and j not in matched_ext_ids:
                matched_ext_ids.add(j)
                break

        for f in SCORED_FIELDS:
            ok, note = compare_field(f, match.get(f), gt_norm.get(f))
            field_hits[f].append(ok)
            if not ok:
                errors.append({
                    "type": "field_mismatch",
                    "gt_index": i,
                    "field": f,
                    "treatment_date": gt_norm.get("treatment_date"),
                    "note": note,
                })

    # Extra extracted records with no GT match
    for j, r in enumerate(extracted):
        if j not in matched_ext_ids:
            errors.append({
                "type": "extra_record",
                "treatment_date": r.get("treatment_date"),
                "note": "Extracted record has no GT counterpart",
            })

    # Per-field accuracy
    field_accuracy: dict[str, float] = {
        f: (sum(hits) / len(hits) if hits else 0.0)
        for f, hits in field_hits.items()
    }

    # Weighted overall accuracy
    total_w = sum(FIELD_WEIGHTS.get(f, 1.0) for f in SCORED_FIELDS)
    weighted_acc = sum(
        field_accuracy[f] * FIELD_WEIGHTS.get(f, 1.0) for f in SCORED_FIELDS
    ) / total_w

    return {
        "doc_id": doc_id,
        "gt_records": len(gt_records),
        "extracted_records": len(extracted),
        "record_count_match": len(extracted) == len(gt_records),
        "field_accuracy": field_accuracy,
        "weighted_accuracy": round(weighted_acc, 4),
        "errors": errors,
    }


# ---------------------------------------------------------------------------
# Extraction runner
# ---------------------------------------------------------------------------

async def run_extraction(pdf_path: Path, doc_id: str) -> tuple[ExtractionOutput, dict]:
    pages: list[Page] = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text() or ""
            pages.append(Page(page_num=i + 1, page_content=text))

    doc = Document(doc_id=doc_id, num_pages=len(pages), pages=pages)
    ctx = RunContext(document=doc, prompt_loader=PromptLoader())

    agent = AgentFactory.build_extraction_agent()
    executor = ExtractionAgentExecutor(agent, max_turns=5)

    t0 = time.monotonic()
    output, usage = await executor.run(ctx)
    duration = time.monotonic() - t0

    inp = getattr(usage, "input_tokens", 0) or 0
    out = getattr(usage, "output_tokens", 0) or 0
    # gpt-5.4 pricing: $2/M input, $8/M output (verify against current OpenAI pricing at submission)
    cost = (inp * 0.000002) + (out * 0.000008)

    meta = {
        "doc_id": doc_id,
        "num_pages": len(pages),
        "duration_seconds": round(duration, 2),
        "token_usage": {"input": inp, "output": out, "total": inp + out},
        "cost_usd": round(cost, 6),
    }
    return output, meta


# ---------------------------------------------------------------------------
# Result.md renderer
# ---------------------------------------------------------------------------

def render_result_md(results: list[dict], metas: list[dict]) -> str:
    lines: list[str] = [
        "# Extraction Evaluation Results",
        "",
        f"Evaluated **{len(results)} documents** against ground truth.",
        "",
        "---",
        "",
        "## Summary",
        "",
        "| Doc | GT | Extracted | Count | Weighted Acc | Cost USD | Duration |",
        "|---|---|---|---|---|---|---|",
    ]

    for r, m in zip(results, metas):
        if r.get("extraction_error"):
            lines.append(
                f"| {r['doc_id']} | — | ERROR | ✗ | 0% | $0 | — |"
            )
            continue
        cnt = "✓" if r["record_count_match"] else "✗"
        lines.append(
            f"| {r['doc_id']} | {r['gt_records']} | {r['extracted_records']} | "
            f"{cnt} | {r['weighted_accuracy']:.1%} | "
            f"${m['cost_usd']:.4f} | {m['duration_seconds']}s |"
        )

    total_cost = sum(m["cost_usd"] for m in metas)
    total_dur = sum(m["duration_seconds"] for m in metas)
    total_inp = sum(m["token_usage"]["input"] for m in metas)
    total_out = sum(m["token_usage"]["output"] for m in metas)

    lines += [
        "",
        f"**Total cost:** ${total_cost:.4f}  ",
        f"**Total tokens:** {total_inp + total_out:,} (input {total_inp:,} / output {total_out:,})  ",
        f"**Total wall-clock:** {total_dur:.1f}s",
        "",
        "---",
        "",
        "## Field Accuracy by Document",
        "",
    ]

    # Header row — abbreviated field names
    COL_LABELS = {
        "treatment_date": "date",
        "cpt_codes": "cpt",
        "total_charges": "total$",
        "ins_paid": "ins$",
        "adjustment": "adj",
        "payments": "pmts",
        "balance": "bal",
        "provider": "prov",
        "insurers": "insrs",
        "third_parties": "3p",
        "description": "desc",
    }
    col_order = list(COL_LABELS.keys())
    header_cells = " | ".join(COL_LABELS[f] for f in col_order)
    lines += [
        f"| Doc | {header_cells} |",
        "|---|" + "|".join(["---"] * len(col_order)) + "|",
    ]

    for r in results:
        if r.get("extraction_error"):
            lines.append(f"| {r['doc_id']} | " + " | ".join(["ERROR"] * len(col_order)) + " |")
            continue
        cells = []
        for f in col_order:
            acc = r["field_accuracy"].get(f, 0.0)
            if acc >= 0.95:
                cells.append(f"✓{acc:.0%}")
            elif acc >= 0.70:
                cells.append(f"~{acc:.0%}")
            else:
                cells.append(f"✗{acc:.0%}")
        lines.append(f"| {r['doc_id']} | " + " | ".join(cells) + " |")

    lines += ["", "---", "", "## Error Details per Document", ""]

    for r in results:
        lines += [f"### {r['doc_id']}", ""]

        if r.get("extraction_error"):
            lines += [f"**EXTRACTION FAILED:** `{r['extraction_error']}`", ""]
            continue

        count_note = (
            "Record count matches GT."
            if r["record_count_match"]
            else f"**Count mismatch** — GT: {r['gt_records']}, extracted: {r['extracted_records']}."
        )
        lines.append(count_note)
        lines.append("")

        errors = r.get("errors", [])
        if not errors:
            lines += ["No errors. Perfect field match.", ""]
            continue

        missing = [e for e in errors if e["type"] == "missing_record"]
        extra = [e for e in errors if e["type"] == "extra_record"]
        mismatches = [e for e in errors if e["type"] == "field_mismatch"]

        if missing:
            lines.append(f"**Missing records ({len(missing)}):**")
            for e in missing:
                lines.append(f"- GT[{e['gt_index']}] `{e['treatment_date']}` — {e['note']}")
            lines.append("")

        if extra:
            lines.append(f"**Extra extracted records ({len(extra)}):**")
            for e in extra:
                lines.append(f"- `{e['treatment_date']}` — {e['note']}")
            lines.append("")

        if mismatches:
            lines.append(f"**Field mismatches ({len(mismatches)}):**")
            lines.append("")
            lines.append("| GT# | Field | Date | Detail |")
            lines.append("|---|---|---|---|")
            for e in mismatches:
                lines.append(
                    f"| {e['gt_index']} | `{e['field']}` "
                    f"| {e['treatment_date']} | {e['note']} |"
                )
            lines.append("")

    lines += [
        "---",
        "",
        "_Generated by `scripts/eval_extraction.py`_",
        "",
    ]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

async def main() -> None:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--rescore",
        action="store_true",
        help="Re-score existing docs-test/<doc>.json files without re-extracting.",
    )
    parser.add_argument(
        "--skip",
        nargs="*",
        default=[],
        help="Doc IDs to skip re-extraction for (uses cached JSON). E.g. --skip doc_001 doc_003",
    )
    args = parser.parse_args()

    DOCS_TEST_DIR.mkdir(parents=True, exist_ok=True)

    pdfs = sorted(DATA_DIR.glob("*.pdf"))
    print(f"Found {len(pdfs)} PDFs in {DATA_DIR}")
    print(f"Output dir: {DOCS_TEST_DIR}")
    if args.rescore:
        print("Mode: rescore only (using cached JSON, no API calls)")
    print()

    all_results: list[dict] = []
    all_metas: list[dict] = []

    for pdf_path in pdfs:
        doc_id = pdf_path.stem
        gt_path = DATA_DIR / f"{doc_id}_gt.json"

        if not gt_path.exists():
            print(f"  [{doc_id}] SKIP — no ground truth file")
            continue

        out_path = DOCS_TEST_DIR / f"{doc_id}.json"

        if args.rescore:
            if not out_path.exists():
                print(f"  [{doc_id}] SKIP — no cached JSON (run without --rescore first)")
                continue
            print(f"  [{doc_id}] rescoring...", end="", flush=True)
            try:
                cached = json.loads(out_path.read_text(encoding="utf-8"))
                meta = cached["meta"]
                records = cached["records"]
                gt_data = json.loads(gt_path.read_text(encoding="utf-8"))
                gt_records = gt_data.get("records", [])
                eval_result = evaluate_doc(doc_id, records, gt_records)
                all_results.append(eval_result)
                all_metas.append(meta)
                n_errors = len([e for e in eval_result["errors"] if e["type"] == "field_mismatch"])
                print(
                    f" {len(records)}/{len(gt_records)} records  "
                    f"acc={eval_result['weighted_accuracy']:.1%}  "
                    f"errors={n_errors}"
                )
            except Exception as exc:
                print(f" FAILED")
                traceback.print_exc()
            continue

        if doc_id in (args.skip or []):
            if not out_path.exists():
                print(f"  [{doc_id}] SKIP — no cached JSON for skipped doc")
                continue
            print(f"  [{doc_id}] skipped (using cache)...", end="", flush=True)
            try:
                cached = json.loads(out_path.read_text(encoding="utf-8"))
                meta = cached["meta"]
                records = cached["records"]
                gt_data = json.loads(gt_path.read_text(encoding="utf-8"))
                gt_records = gt_data.get("records", [])
                eval_result = evaluate_doc(doc_id, records, gt_records)
                all_results.append(eval_result)
                all_metas.append(meta)
                n_errors = len([e for e in eval_result["errors"] if e["type"] == "field_mismatch"])
                print(
                    f" {len(records)}/{len(gt_records)} records  "
                    f"acc={eval_result['weighted_accuracy']:.1%}  "
                    f"errors={n_errors}  "
                    f"cost=${meta['cost_usd']:.4f}  "
                    f"{meta['duration_seconds']}s"
                )
            except Exception as exc:
                print(f" FAILED reading cache")
                traceback.print_exc()
            continue

        print(f"  [{doc_id}] extracting...", end="", flush=True)

        try:
            output, meta = await run_extraction(pdf_path, doc_id)

            # Persist extracted JSON
            out_path.write_text(
                json.dumps(
                    {
                        "doc_id": doc_id,
                        "meta": meta,
                        "records": [r.model_dump() for r in output.records],
                        "flagged": [f.model_dump() for f in output.flagged],
                    },
                    indent=2,
                ),
                encoding="utf-8",
            )

            # Evaluate
            gt_data = json.loads(gt_path.read_text(encoding="utf-8"))
            gt_records = gt_data.get("records", [])
            eval_result = evaluate_doc(
                doc_id,
                [r.model_dump() for r in output.records],
                gt_records,
            )

            all_results.append(eval_result)
            all_metas.append(meta)

            n_errors = len([e for e in eval_result["errors"] if e["type"] == "field_mismatch"])
            print(
                f" {len(output.records)}/{len(gt_records)} records  "
                f"acc={eval_result['weighted_accuracy']:.1%}  "
                f"errors={n_errors}  "
                f"cost=${meta['cost_usd']:.4f}  "
                f"{meta['duration_seconds']}s"
            )

        except Exception as exc:  # noqa: BLE001
            print(f" FAILED")
            traceback.print_exc()
            all_results.append(
                {
                    "doc_id": doc_id,
                    "gt_records": 0,
                    "extracted_records": 0,
                    "record_count_match": False,
                    "field_accuracy": {},
                    "weighted_accuracy": 0.0,
                    "errors": [],
                    "extraction_error": str(exc),
                }
            )
            all_metas.append(
                {
                    "doc_id": doc_id,
                    "num_pages": 0,
                    "duration_seconds": 0.0,
                    "token_usage": {"input": 0, "output": 0, "total": 0},
                    "cost_usd": 0.0,
                }
            )

    # Write result.md
    md = render_result_md(all_results, all_metas)
    RESULT_MD.write_text(md, encoding="utf-8")

    # Console summary
    total_cost = sum(m["cost_usd"] for m in all_metas)
    avg_acc = (
        sum(r["weighted_accuracy"] for r in all_results) / len(all_results)
        if all_results
        else 0.0
    )
    print()
    print(f"Done. {len(all_results)} docs evaluated.")
    print(f"Average weighted accuracy: {avg_acc:.1%}")
    print(f"Total cost: ${total_cost:.4f}")
    print(f"Report: {RESULT_MD}")


if __name__ == "__main__":
    asyncio.run(main())
