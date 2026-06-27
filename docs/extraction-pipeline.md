# Extraction Pipeline — Upload to Result

End-to-end walkthrough of how a medical billing PDF becomes structured `BillingRecord` JSON.

---

## Overview

```
User uploads PDF
      │
      ▼
POST /jobs  →  save PDF  →  insert job row (status=pending)
                                    │
                            Worker polls DB
                                    │
                            claim_next_job()   ← atomic SELECT FOR UPDATE SKIP LOCKED
                                    │
                            ExtractionService.process_job()
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
               Parse PDF     Phase 1:          Phase 2:
               (pdfplumber)  Classify pages    Extract chunks (parallel)
                                    │               │
                                    └───────────────┘
                                            │
                                  Post-process records
                                            │
                                  Write result to DB (status=completed)
```

---

## Step 1 — User Uploads PDF (`POST /jobs`)

**File:** `backend/app/api/routes/jobs.py`

**What happens:**
1. API receives `multipart/form-data` with the PDF file
2. Auth middleware validates the caller's session → extracts `user_id`
3. File content is hashed (SHA-256) for cache lookup
4. **Cache check**: if a prior completed job with the same hash exists for this user → return cached result immediately (no re-extraction)
5. PDF saved to `PDF_MOUNT_PATH` (Docker volume shared with worker)
6. Job row inserted: `status=pending`, `user_id`, `pdf_path`, `content_hash`
7. Response returns the new job ID immediately (async — extraction happens in background)

**Why async:** Extraction takes 30–90 seconds. HTTP request must return fast; worker picks it up.

**Why content hash:** Same PDF uploaded twice → same result. Saves API cost and time. Hash is per-user — another user's identical PDF does NOT share cache (RLS boundary).

---

## Step 2 — Worker Claims the Job

**File:** `backend/app/worker/loop.py`

**What happens:**
```
loop:
  job = claim_next_job()   # atomic claim
  if job:
    ExtractionService.process_job(job.id, job.user_id)
  else:
    sleep(WORKER_POLL_INTERVAL_SECONDS)
```

**Why atomic claim (`SELECT FOR UPDATE SKIP LOCKED`):**
Two worker replicas run simultaneously. Without atomicity, both could claim the same job. `SKIP LOCKED` means a row being processed by worker A is invisible to worker B — no coordination needed, no duplicate processing.

**Why store `user_id` on the job row:**
The worker has no HTTP session. It reads `user_id` from the claimed job, then calls `SET LOCAL app.current_user_id = job.user_id` before any DB write. This satisfies PostgreSQL Row-Level Security so the worker writes the result under the correct user identity.

---

## Step 3 — PDF Parsing (`pdfplumber`)

**File:** `backend/app/service/extraction_service.py`

**What happens:**
```python
with pdfplumber.open(job.pdf_path) as pdf:
    for i, page in enumerate(pdf.pages):
        text = page.extract_text() or ""
        pages.append(Page(page_num=i+1, page_content=text))
```

**Why pdfplumber:**
Extracts text layout-aware — preserves column alignment in billing tables. Raw `PyPDF2` loses column structure; `pdfplumber` keeps whitespace relationships so the model can parse tabular rows correctly.

**Output:** `Document` object with a `Page` list (1-indexed page numbers, raw text per page).

---

## Step 3b — Cross-Page Record Handling (Page Boundary Overlap)

**`BillingRecord.page` is typed `str`** — accepts both `"6"` (single page) and `"6-7"` (cross-page range). The Pydantic schema enforces this; structured-output validation passes for either form.

**The problem:** A single billing record can span two PDF pages — e.g. a row starts at the bottom of page 6 (date, codes, charges) and the financial columns (ins_paid, adjustment, balance) overflow to the top of page 7. If those two pages end up in different extraction chunks, the record gets split:

- Chunk A (page 6 only) → sees an incomplete row, may extract a partial record or skip it
- Chunk B (page 7 only) → sees orphaned numbers with no context, may misattribute them

### How we mitigate this today

**Large token budget per chunk (240k chars ≈ 60k tokens):** Most medical billing PDF pages are 5,000–20,000 characters. At 240k chars/chunk, a typical document fits entirely in **one or two chunks**. When all pages are in the same chunk, the model sees every cross-page record as a single contiguous block — no split risk.

For doc_001 (21 pages, each ~10k chars = ~210k chars total) → all pages fit in one chunk. All cross-page records (`"page": "6-7"`, `"page": "8-9"`, etc.) were extracted correctly because the model saw pages 6 and 7 together.

### When the mitigation is insufficient

If a single page exceeds the char budget (e.g. a 300k-char page), it gets its own chunk — but that's a self-contained oversized page, not a boundary split. The real risk is when a document has **many dense pages** and the chunk boundary happens to land between two pages that share a record.

Example: 500-page document, chunk boundary between page 250 and 251, record spanning those pages → that record is lost.

### Current gap and future fix

| Scenario | Current behaviour |
|---|---|
| Record spans pages within same chunk | ✓ Extracted correctly |
| Record spans chunk boundary | ✗ May be missed or partially extracted |

**Future fix (not yet implemented):** 1-page overlap between adjacent chunks — the last page of chunk N is repeated as the first page of chunk N+1. After merge, dedup records by `(treatment_date, total_charges)` to remove duplicates introduced by the overlap. This guarantees every cross-page record appears in at least one chunk's full context.

```
Without overlap:  [p1 p2 p3] [p4 p5 p6]   ← record at p3/p4 split
With 1-page overlap: [p1 p2 p3] [p3 p4 p5 p6]  ← p3 in both chunks
                                 └── dedup on merge
```

Until implemented, the large char budget is the primary safeguard. Flag documents that produced fewer records than expected — it may indicate a boundary split.

---

## Step 4 — Phase 1: Page Classification

**File:** `backend/app/ai/agents/extraction/executor.py` → `_classify_pages()`

**What happens:**
1. Take first 800 characters of each page (preview)
2. Send all previews to a lightweight classifier agent (`gpt-5.4-mini`)
3. Classifier identifies which pages are **summary/ledger pages** (compact table with many rows) vs **detail/itemized pages** (1–3 records with expanded line items)
4. Return only the summary pages for extraction

**Why classify first:**
Medical billing PDFs typically have two layers:
- **Summary page**: all records in a compact table (one row per billing episode, 10–50+ rows/page)
- **Detail pages**: each row expanded with line-item breakdowns

Extracting from the summary gives cleaner, single-date records matching the billing statement format. Extracting from detail pages gives date ranges and redundant data.

**Fallback:** If no summary is detected, extract from all pages. This handles documents with no summary layer (e.g. imaging records, pharmacy records).

**Known gap — fallback duplication risk:** If a document actually has a summary page but the classifier misses it (`has_summary=false`), the fallback extracts from all pages. Both the summary row and its detail expansion are visible — the same billing episode can appear twice (once as a compact summary row, once as an expanded detail block). The merged `records[]` would then contain duplicates. Mitigation: tune the classifier to avoid false negatives; if duplication is observed in practice, add a dedup pass by `(treatment_date, total_charges)` after merge.

---

## Step 5 — Phase 2: Chunked Parallel Extraction

**File:** `backend/app/ai/agents/extraction/executor.py` → `_build_chunks()` + `asyncio.gather()`

### 5a. Token-Aware Chunking

```python
_TARGET_CHARS_PER_CHUNK = 240_000  # ~60k tokens

def _build_chunks(pages):
    # group pages until char budget exceeded
    # single oversized page → its own chunk
```

**Why chunk by characters, not page count:**
Medical billing pages vary wildly in density — a summary page with 50 rows might be 50,000 chars; a single pharmacy record page might be 2,000 chars. Fixed page-count chunks (e.g. "3 pages") fail on dense documents. Character budget ensures each API call stays under the model's context window regardless of page density.

**Token budget:** 60k tokens of page content leaves ~68k tokens for system prompt, user prompt overhead, and structured output — well within `gpt-5.4`'s context.

### 5b. Parallel Execution

```python
chunk_results = await asyncio.gather(
    *[self._run_chunk(ctx, chunk, i, total) for i, chunk in enumerate(chunks)]
)
```

**Why parallel:** All chunks are independent — no inter-chunk dependencies. Running N chunks in parallel gives the same wall-clock time as running 1 chunk. A 100-page document with 10 chunks completes in the same time as a 10-page document.

**Rate-limit guard:** Each chunk fires a separate OpenAI API call. Without throttling, a 10-chunk document would issue 10 simultaneous requests, triggering 429 errors on any non-enterprise quota. `asyncio.Semaphore(4)` in `_run_chunk` caps concurrent API calls at 4. Wall-clock impact is minimal — the 5th chunk starts as soon as the fastest of the first 4 finishes.

### 5c. Agent Prompt Structure

Each chunk is sent to `gpt-5.4` with:
- **System prompt** (`extraction/system.j2`): extraction rules (field definitions, column disambiguation, CPT code handling, flagging rules)
- **User prompt** (`extraction/user.j2`): full page text embedded inline

```
=== PAGE 6 ===
[full text of page 6]

=== PAGE 7 ===
[full text of page 7]
...
Extract all billing records. Return records[] and flagged[].
```

**Why embed pages in prompt vs tool calls:**
Tool calls (agent reads pages one by one) burn one "turn" per page call. A 21-page document needs 23+ turns minimum — hits `max_turns` limits. Embedding text directly means the agent sees all content at once and produces output in 1–2 turns. No turn-counting issue regardless of document size.

---

## Step 6 — Structured Output

**File:** `backend/app/models/extraction.py`

The extraction agent uses `output_type=ExtractionOutput` — the OpenAI Agents SDK forces the model to call a `StructuredOutput` tool matching the Pydantic schema. Invalid output causes automatic retry.

```python
class ExtractionOutput(BaseModel):
    records: list[BillingRecord]
    flagged: list[FlaggedRecord]
```

Each `BillingRecord` has 12 fields: `treatment_date`, `cpt_codes`, `description`, `provider`, `insurers`, `third_parties`, `total_charges`, `ins_paid`, `adjustment`, `payments`, `balance`, `page`.

`FlaggedRecord` captures ambiguity without dropping the record — a flagged record still appears in `records[]`.

---

## Step 7 — Post-Processing: Payments/Balance Correction

**File:** `backend/app/ai/agents/extraction/executor.py` → `_fix_payments_balance()`

**Problem:** Medical billing ledgers have one patient-amount column. Models sometimes map it to `payments` (amount already paid) when it's actually `balance` (amount still owed).

**Deterministic fix (no model involvement):**
```python
expected = round(total_charges - ins_paid - adjustment, 2)

if payments ≈ expected AND balance ≈ 0.0:
    # column is the balance, not a received payment
    balance = payments
    payments = null

if payments == 0.0 AND expected ≈ 0.0:
    # empty column artefact, not an actual zero payment
    payments = null
```

**Why in code, not prompt:** Prompt instructions for this disambiguation were ignored by the model in practice. A deterministic rule is reliable across all documents.

---

## Step 8 — Merge Chunks + Fix FlaggedRecord Indices

**File:** `backend/app/ai/agents/extraction/executor.py`

After parallel extraction:
1. Records from all chunks are concatenated in page order
2. `FlaggedRecord.row` is a zero-based index into the merged `records[]`. Each chunk's flags are offset by the record count of prior chunks:
   ```python
   for flag in chunk_output.flagged:
       if flag.row is not None:
           flag = flag.model_copy(update={"row": flag.row + record_offset})
   ```
   **Why offset is correct:** Each extraction agent only sees its own chunk's pages — it has no knowledge of prior chunks. So the model's `row` values start at 0 for the first record in that chunk, not from the document start. Adding `record_offset` (= total records in all prior chunks) maps chunk-local indices to document-wide indices.

3. Token usage (`input_tokens`, `output_tokens`) is summed across **all** API calls — Phase 1 classifier tokens and Phase 2 chunk tokens. Phase 1 classification runs first and seeds the totals; each chunk adds on top. `cost_usd` is therefore a true full-pipeline cost, not just extraction cost.

---

## Step 9 — Write Result to DB

**File:** `backend/app/service/extraction_service.py`

On success:
```python
await job_dao.update_status(
    session, job_id,
    status="completed",
    result={"records": [...], "flagged": [...]},
    token_usage={"input": N, "output": M, "total": N+M},
    cost_usd=...,
    processing_duration_seconds=...,
)
```

On failure (after retries exhausted):
```python
await job_dao.update_status(session, job_id, status="failed", error=str(exc))
```

**Cost calculation** (gpt-5.4 pricing):
```
cost = (input_tokens × $0.002/1k) + (output_tokens × $0.008/1k)
```

**Why never raise from `process_job`:** Worker loop must stay alive even if one job fails. All exceptions are caught, written to `job.error`, and the loop continues to the next job.

---

## Step 10 — Client Polls for Result

```
GET /jobs/{job_id}
```

Returns full job including:
- `status`: `pending` → `processing` → `completed` / `failed`
- `result.records[]`: structured billing records
- `result.flagged[]`: records needing manual review
- `token_usage`, `cost_usd`, `processing_duration_seconds`

RLS enforces isolation — another user's `job_id` returns the same 404 as a non-existent ID.

---

## Key Design Decisions Summary

| Decision | Alternative | Why chosen |
|---|---|---|
| Embed pages in prompt | Tool calls per page | No turn limit; simpler; same latency |
| Token-aware chunking | Fixed page-count chunks | Handles dense/sparse pages uniformly |
| Parallel chunk execution with `Semaphore(4)` | Unbounded parallel or sequential | Wall-clock ≈ max(chunks); semaphore prevents 429 rate-limit errors |
| Deterministic payments/balance fix | Prompt instruction | Model ignored prompt; code is reliable |
| Two-phase classify → extract | Extract all pages always | Avoids detail-page noise; finds summary anywhere |
| `gpt-5.4` (extract) + `gpt-5.4-mini` (classify) | `gpt-4o-mini` | 1M context window; better instruction following; `gpt-4o-mini` (128k) would overflow on 60k-token chunks |
| `page` field typed `str` | `int` | Accepts both `"6"` and `"6-7"` without structured-output validation failure |
| pdfplumber | PyPDF2 | Preserves column alignment in billing tables |
| Classification tokens counted in totals | Extraction-only token count | `cost_usd` reflects true full-pipeline spend |
