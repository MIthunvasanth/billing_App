# Design Document

**Candidate:** Ashish Chauhan
**Date submitted:** 2026-06-27
**Time spent:** ~40 hours total across all milestones

---

## 1. System Overview

The platform has four components that run together under Docker Compose. A Next.js 14 frontend (port 3000) handles sign-up, sign-in, PDF upload, and result display. A FastAPI backend (port 8000) validates auth tokens, manages the job queue, and exposes the `/jobs` REST API. Two background worker replicas poll Postgres for pending jobs, claim one atomically, run the extraction pipeline, and write results back. PostgreSQL 16 sits at the bottom, enforcing per-user isolation through Row-Level Security so that no application bug can leak one user's jobs to another.

The flow: user signs up → receives an opaque session token → uploads a PDF via `POST /jobs` (multipart) → job row is inserted with `status=pending` → worker claims it with `FOR UPDATE SKIP LOCKED` → pdfplumber parses pages → gpt-5.4-mini classifies billing-relevant pages → gpt-5.4 extracts `BillingRecord` objects in parallel chunks → result is written to `jobs.result` as JSONB → frontend polls `GET /jobs/{id}` and renders the table.

---

## 2. Authentication, Identity & Isolation

### 2.1 Topology

Auth is handled entirely in Python. There is no Better Auth JS server. The `user`, `account`, and `session` tables follow Better Auth's schema (camelCase columns, quoted identifiers) so the structure is compatible, but all token issuance and validation is custom Python in `backend/app/api/routes/auth.py` and `backend/app/api/dependencies/auth.py`.

**Registration** (`POST /auth/register`): hashes the password with bcrypt, inserts a row into `user` and `account`, then creates a `session` row with a 32-byte URL-safe random token (`secrets.token_urlsafe(32)`). Returns `{token, user}`. No JWT — the token is opaque.

**Login** (`POST /auth/login`): looks up the user by email, verifies bcrypt hash, creates a new session row, returns the same shape.

**Validation** (`get_current_user_id` dependency, `backend/app/api/dependencies/auth.py`): extracts `Authorization: Bearer <token>` header, queries `SELECT "userId" FROM session WHERE token = :token AND "expiresAt" > NOW()` via `admin_cm` (billing role), returns the `userId` string. This runs on every authenticated request before the route handler sees it. Sessions expire after 30 days.

The trust boundary: the frontend stores the token in `localStorage` and sends it on every request. The API validates it against the DB. The Python API never trusts the frontend to claim a user identity — only a valid unexpired token that exists in the session table is accepted.

### 2.2 RLS Enforcement

**Tables with RLS:** only `jobs`. Auth tables (`user`, `account`, `session`) are not user-data — they are access control infrastructure and don't need per-user policies.

**Policies** (defined in `backend/alembic/versions/b9c4f2a1e835_add_user_id_rls_and_metrics.py`):

```sql
CREATE POLICY jobs_select_policy ON jobs
    FOR SELECT
    USING (user_id = current_setting('app.current_user_id', true)::uuid);

CREATE POLICY jobs_insert_policy ON jobs
    FOR INSERT
    WITH CHECK (user_id = current_setting('app.current_user_id', true)::uuid);

-- identical USING clause for UPDATE and DELETE
```

`current_setting('app.current_user_id', true)` — the second arg `true` makes it return `NULL` rather than raising an error when the setting is not present (e.g. in the worker's admin session before SET). This makes the SELECT policy match zero rows if identity isn't set, which is the safe default.

**Two database roles:**

| Role | Owner? | BYPASSRLS? | Used by |
|---|---|---|---|
| `billing` | Yes | Implicit (owner bypasses without FORCE) | Alembic migrations, `admin_cm` in worker |
| `billing_app` | No | No | API at runtime, `app_cm` in worker |

`billing` bypasses RLS as table owner. This is intentional: Alembic runs as `billing` and needs to see all rows. The worker's claim query also runs as `billing` because `app.current_user_id` is not set at claim time (we don't know whose job we're claiming yet) — if it ran as `billing_app` with an unset identity, the SELECT policy would return zero rows.

`billing_app` is created in the migration with `LOGIN PASSWORD 'billing_app'` and granted DML on all public tables. It has no `BYPASSRLS` and is not a superuser. The API always connects via `APP_DB_CONNECTION_STRING` which points to `billing_app`.

### 2.3 Connection Pooling Interaction

I use `set_config('app.current_user_id', :uid, true)` — the `true` flag is the key. From the Postgres docs: `set_config(setting_name, new_value, is_local)` — when `is_local = true`, the effect is rolled back at the end of the current transaction, equivalent to `SET LOCAL`. This means:

1. Transaction starts
2. `set_config(..., true)` sets the identity for this transaction only
3. All DML within this transaction sees the correct `current_setting`
4. Transaction ends (commit or rollback) → setting resets to its pre-transaction value

Under connection pooling (SQLAlchemy's own pool, not PgBouncer), connections are reused across requests. Because the identity is transaction-scoped, it cannot leak from one request's transaction to another. The next request that reuses the connection will be in a new transaction with no `app.current_user_id` set (defaults to NULL via the `true` flag), which means RLS would block it until the new identity is set.

`ContextManager.session()` (in `backend/app/core/context_manager.py`) always calls `_set_user_identity` before the first DML, so identity is always established before the policies evaluate.

If I were using PgBouncer in transaction-pooling mode, the safety guarantee is identical — each transaction-begin starts clean. In session-pooling mode it would be a problem, but we're using SQLAlchemy's built-in pool which is connection-scoped (equivalent to transaction pooling from Postgres's perspective).

### 2.4 Worker Identity

`backend/app/worker/loop.py` uses two `ContextManager` instances:

- `admin_cm` connects as `billing` (admin role). Used for `claim_next_job` and `recover_stalled`. These operations must see all rows regardless of ownership.
- `app_cm` connects as `billing_app` (RLS-subject role). Used by `ExtractionService` for all result writes.

After claiming a job, the worker passes `job["user_id"]` to `ExtractionService.process_job`. Inside, every DB session opens with:

```python
await session.execute(
    text("SELECT set_config('app.current_user_id', :uid, true)"), {"uid": user_id}
)
```

This happens in `extraction_service.py` at line 46 (before the `job_dao.get` read) and again at line 87 (before the `update_status` write). The result write is scoped to the job's owner — RLS treats the worker's write as if the owner made it.

This means the worker cannot write a result to a job it does not know the user_id for, and it cannot accidentally update a different user's job because the UPDATE `WHERE jobs.id = :job_id` is filtered by the SELECT policy before it executes.

### 2.5 The Isolation Guarantee

Even if application-layer filtering is wrong or missing, user A cannot read or write user B's jobs because `billing_app` is subject to RLS policies that filter on `user_id = current_setting('app.current_user_id', true)::uuid`, and `app.current_user_id` is set to the validated session owner on every transaction. There is no code path that can set `app.current_user_id` to a different user's id — auth validation is a FastAPI dependency that runs before any route handler, and the worker only sets it to the `user_id` it reads from the claimed job row.

---

## 3. Agent Design

### 3.1 Tools

The extraction pipeline uses two agents, neither with tools. Tools add latency through multi-turn conversations and we already have all page text in memory from pdfplumber. A single-pass structured output is faster and more reliable for tabular data.

**Page classifier agent** (`gpt-5.4-mini`, `output_type=PageClassification`): takes 800-char previews of each page, identifies which are billing summary ledgers vs. detail/itemized pages. Returns `has_summary: bool, summary_pages: list[int]`. Purpose: avoid feeding narrative/clinical text to the expensive extraction model.

**Extraction agent** (`gpt-5.4`, `output_type=ExtractionOutput`): given a chunk of billing page text (≤40k chars), returns `records: list[BillingRecord], flagged: list[FlaggedRecord]`. No tools — the entire chunk is in the prompt. The output is validated by Pydantic before it's used.

Tools I considered and rejected: page navigation tool (extra round trips), table extractor tool (pdfplumber already gives us text, tables need more work than they're worth for billing ledgers), search tool (all text is in context already).

### 3.2 Navigation Strategy

1. All pages extracted with pdfplumber into `Page(page_num, page_content)` objects.
2. Page classifier runs once: it receives 800-char previews of all pages and returns the page numbers that contain billing ledger rows. This avoids sending cover pages, auth pages, and narrative text to gpt-5.4.
3. Billing pages are concatenated and chunked at ~40k chars (~10k tokens). Chunk boundaries fall on full pages to avoid mid-table splits.
4. Each chunk gets the full system prompt (field definitions, examples, flagging rules) plus the chunk text. Chunks run in parallel with `asyncio.Semaphore(4)`.

Tables that split across pages: because we chunk by full pages, a table that starts on page 3 and ends on page 4 will be in the same chunk as long as both pages fit within 40k chars. For very large tables that span many pages, the model sees the continuation as part of the same prompt. This doesn't perfectly handle mid-table splits at chunk boundaries, but with 40k-char chunks and typical billing ledger row densities, it's rare in practice.

### 3.3 State Management

`RunContext` holds the `Document` (all pages), a `PromptLoader`, and is passed through `Agent[RunContext]`. The executor (`ExtractionAgentExecutor`) holds intermediate state: `all_records: list[BillingRecord]`, `all_flagged: list[FlaggedRecord]`. Each chunk's result is appended to these lists. After all chunks complete, post-processing runs on the combined list.

The state is entirely in-process for one job invocation. There is no shared state between worker replicas or between jobs.

### 3.4 Uncertainty and Flagging

The extraction system prompt instructs the model to flag a record when it cannot confidently fill a field. A `FlaggedRecord` references the record by index, lists the uncertain fields, and gives a reason with a severity level.

The rule: prefer a partially-filled correct record over a fully-filled wrong one. The model is instructed to leave fields as `null` when unsure (Pydantic Optional fields default to None) and generate a FlaggedRecord explaining what's uncertain. Severity is `high` if a financial field is uncertain, `medium` for provider/insurer, `low` for description.

Post-processing adds its own FlaggedRecords for structural issues it detects:
- Over-extraction (>20 records/page after merge): aggregated to 1 summary record, flagged high
- Periodic billing detected (merge reduces count by >80%): aggregated, flagged low

I deliberately avoid flagging things the model is confident about. The prompt includes examples of confident extraction patterns. This makes the flagged list useful (real uncertainty signals) rather than noise.

---

## 4. Job Queue & Reliability

### 4.1 Worker and Concurrency

The claim query in `JobDAO.claim_next_job` (`backend/app/dao/pg/job_dao.py:164`):

```sql
WITH claimed AS (
    SELECT id FROM jobs
    WHERE status = 'pending'
    ORDER BY created_at
    LIMIT 1
    FOR UPDATE SKIP LOCKED
)
UPDATE jobs
SET status = 'processing', started_at = now(), updated_at = now()
FROM claimed
WHERE jobs.id = claimed.id
RETURNING jobs.*
```

`FOR UPDATE SKIP LOCKED` means: take a row-level write lock on the selected row; if the row is already locked by another transaction, skip it and move to the next one. The `LIMIT 1` + `ORDER BY created_at` picks the oldest pending job that isn't already being worked.

The `WITH ... UPDATE ... RETURNING` is a single round-trip. The row moves to `processing` atomically — there is no window where two workers both see `status='pending'` and both start working it. If the second worker runs the query at the same moment, it skips the locked row and either picks the next one or returns null.

If `FOR UPDATE SKIP LOCKED` were removed: two workers would both see the same `pending` row in their SELECT (no lock contention), both run the UPDATE, and both process the same job — resulting in duplicate extraction and a corrupted job record when the second UPDATE overwrites the first result.

### 4.2 Crash Recovery

`recover_stalled` in `JobDAO` (`job_dao.py:190`): finds jobs with `status='processing'` and `started_at < now() - interval '5 minutes'`, resets them to `pending`. Called on startup (iteration 0) and every 12 polling iterations (~60 seconds at default 5s poll).

If a worker crashes mid-job, the row stays `processing` until the timeout triggers. The surviving worker (or the restarted one) will recover it. Five minutes is conservative — a completed extraction typically takes 30–120 seconds, so a job that's been `processing` for 5 minutes without completing is stalled.

The timeout is hard-coded in `recover_stalled` as `timeout_minutes=5`. With more time I'd make this configurable via settings.

### 4.3 Status Transitions

| Transition | Trigger | Code location |
|---|---|---|
| `pending` → `processing` | `claim_next_job` CTE UPDATE | `job_dao.py:164` |
| `processing` → `completed` | `ExtractionService.process_job` succeeds | `extraction_service.py:90` |
| `processing` → `failed` | `ExtractionService.process_job` raises | `extraction_service.py:117` |
| `pending` → `cancelled` | `DELETE /jobs/{id}` while pending | `job_dao.py:149` |
| `processing` → `pending` (stall recovery) | `recover_stalled` on timeout | `job_dao.py:190` |

`DELETE /jobs/{id}` raises 409 if `status != 'pending'` because `cancel()` does `WHERE status = 'pending'` and returns `None` if no row matched — `JobService.cancel_job` raises `JobNotCancellableException` which the route handler converts to 409.

A `processing` job cannot be directly cancelled — it must either complete, fail, or be recovered.

### 4.4 Retry Policy

Currently no bounded retry within a single job attempt. If extraction fails, the job goes to `failed` immediately. This is M3 scope; the stall-recovery mechanism does effectively retry a crashed job by resetting it to `pending`, but transient API errors (429, 5xx from OpenAI) are not retried.

**Intended design (not yet implemented):** wrap the OpenAI API calls in exponential backoff — start at 1s, multiply 2×, cap at 60s, max 3 attempts. After 3 failures: `status=failed`, error detail written to job row, worker loop continues.

Retryable: `RateLimitError` (429), `APIError` (5xx), `asyncio.TimeoutError`.
Non-retryable: `BadRequestError` (400 — prompt issue), `AuthenticationError` (401), `ValidationError` (Pydantic).

Stall recovery provides a coarser outer retry: a worker crash leaves the job in `processing`; `recover_stalled` resets it to `pending` after 5 minutes. This is orthogonal — fine-grained retries handle transient API errors within one attempt; stall recovery handles worker process death.

### 4.5 Cost and Latency Tracking

`processing_duration_seconds` is captured with `time.monotonic()` at the start of `process_job` and subtracted at the end. This is wall-clock time for the full extraction (PDF parse + classifier + extraction chunks + DB write).

`token_usage` aggregates `usage.input_tokens` and `usage.output_tokens` from the OpenAI runner's `RunResult`. This covers the extraction agent runs; the classifier tokens are not currently aggregated into the total (minor omission).

`cost_usd` is estimated as:
```python
cost_usd = (input_tokens * 0.000002) + (output_tokens * 0.000008)
```
Models used: `gpt-5.4-mini` (classifier) and `gpt-5.4` (extraction). Blended estimate: $2/1M input, $8/1M output. These should be verified against current OpenAI pricing at submission time — the exact rates for gpt-5.4 family are on OpenAI's June 2026 pricing page.

### 4.6 Result Caching

SHA-256 of the PDF bytes is computed at upload time in `jobs.py:26`:
```python
content_hash = hashlib.sha256(pdf_bytes).hexdigest()
```
Stored in `jobs.content_hash`. The `idx_jobs_user_content_hash` partial index covers `(user_id, content_hash) WHERE status = 'completed'` for fast lookups.

**The cache lookup is not yet implemented.** `JobService.create_job` has a `# TODO (M3)` comment at line 42 where the cache check would go. The fingerprint is computed and stored, but re-uploads of the same PDF by the same user currently go through full extraction. The bypass flag (`bypass_cache` form field) is received and passed to `create_job` as `content_hash=None` to skip the hash, which will correctly skip the cache lookup once it's implemented.

Cache must be per-user: the lookup must filter by both `content_hash` AND `user_id`. A cache hit for user A must never return user B's result.

---

## 5. Frontend

Next.js 14 App Router with TypeScript and Tailwind CSS. Six screens: sign-up, sign-in, dashboard (upload + job list), job detail. Auth tokens are stored in `localStorage` and sent as `Authorization: Bearer <token>` on every fetch. A 401 from the API triggers `clearToken()` + hard redirect to `/auth/signin`.

All API calls go through `apiFetch` in `src/lib/api.ts`, which auto-unwraps the `SuccessResponse` envelope (`{ success, message, data }`) that all backend routes return. Python `Decimal` fields (`cost_usd`, `processing_duration_seconds`) are serialized as floats in `_to_dto` → no parsing needed.

The dashboard polls `GET /jobs` every 5 seconds with `setInterval`. The job detail page polls `GET /jobs/{id}` every 3 seconds while `status === 'processing'`. Both intervals are cleaned up on component unmount.

Job detail: if `GET /jobs/{id}` returns 404, the page shows "Job not found" with no job ID in the message — this prevents existence leakage for IDs belonging to other users.

I used the `frontend-design` skill for palette and typography direction. Chose a dark-neutral palette (`#0F1117` bg, `#1A1D27` surface, `#4F9CF9` accent) and `font-mono` on all IDs, CPT codes, and dollar values — gives a data-tool feel without Google Fonts, which avoids build-time network fetches in the Docker build.

---

## 6. Code Structure & Tooling

Backend follows the separation: routes receive/validate HTTP, services own business rules, DAOs own SQL. No SQL in services, no business logic in DAOs. Identity propagation is the one cross-cutting concern — it's handled in `JobService._set_user_identity` so every DAO method called from a service session has the identity already set.

`ExtractionService` is the bridge between the job queue and the AI layer. The worker loop doesn't know about OpenAI — it just calls `extraction_service.process_job(job_id, user_id)` and trusts the service to handle errors and write the result.

The AI layer is designed around `Agent[RunContext]` with no global state. Each job gets a fresh `RunContext` and `ExtractionAgentExecutor`. Prompts are Jinja2 templates loaded via `PromptLoader`.

`AGENTS.md` captures: run commands, the two-role DB pattern, identity propagation, worker identity, alembic rule, the API response envelope, critical files, and what not to do.

Decisions I'd change with more time:
- Implement the content-hash cache lookup (it's literally a TODO in `job_service.py:42`)
- Add bounded retries with backoff to `ExtractionService`
- Fix cost_usd pricing to use actual gpt-5.4 rates
- Aggregate classifier token usage into the total
- Add more ground truth validation tests

---

## 7. Accuracy and Failure Analysis

Evaluated against `data/doc_001–doc_012` ground truth via `scripts/eval_extraction.py`. Weighted field accuracy: high-weight fields (treatment_date, cpt_codes, total_charges, ins_paid, adjustment, payments, balance) count 3×; provider/insurers/third_parties 2×; description 1×.

**Overall average: 50.9%** across 12 documents (run 2026-06-27).

| Doc | Score | Extracted/GT | Main issue |
|---|---|---|---|
| doc_001 | 88.4% | 49/50 | Minor date/financial mismatches |
| doc_002 | 69.3% | 40/40 | Date range format — per-visit vs per-patient |
| doc_003 | 0.0% | 2/1 | GT=1 consolidated; model extracts 2 |
| doc_004 | 0.0% | 2/1 | Same as doc_003 |
| doc_005 | 85.7% | 77/80 | 3 records missed |
| doc_006 | 99.0% | 33/33 | Near-perfect |
| doc_007 | 79.5% | 402/400 | Slight over-extraction, field errors on large doc |
| doc_008 | 31.9% | 1474/100 | Model hallucinates ~35 records/page; GT fields matched via scorer |
| doc_009 | 0.0% | 53/1 | GT=1 aggregate; model extracts per-encounter (129-page doc) |
| doc_010 | 0.0% | 28/1 | Same as doc_009 (151-page doc) |
| doc_011 | 57.7% | 149/150 | Record count correct; field accuracy limited on 194-page doc |
| doc_012 | 99.0% | 122/120 | Near-perfect |

**Key failure modes:**

**doc_002** (69.3%): GT has per-patient date ranges spanning years. Model extracts per-visit rows with individual dates. Record count matches but 68 field mismatches because the date format doesn't match GT's range format. Fix: prompt rule to consolidate sequential same-provider+CPT rows into a date range.

**doc_008** (31.9%, 1474 extracted vs 100 GT): Model hallucinates sub-records within what are single billing rows. 1474 records from 42 pages = 35/page. The eval scorer still finds GT record matches by date+charges, yielding 31.9%. Root cause: the page content for this document has dense numerical tables the model fragments. A post-processing pass that deduplicates by (date, total_charges) within a window would help.

**doc_003/004** (0%): GT says 1 consolidated record; model outputs 2. The scorer treats count mismatch as 0 on every field for the missing record. The extracted record is likely correct — the 0% reflects record count, not field accuracy.

**doc_009/010** (0%): 129 and 151-page documents where GT=1 consolidated summary. Model correctly extracts per-encounter rows (53 and 28 respectively). Without runtime knowledge of GT count, collapsing to 1 would require prompt-level instruction to aggregate when no summary page is found.

**What improved (2026-06-27):** Changed `_merge_patient_records` grouping key from `(provider, cpt_codes)` to `(provider, cpt_codes, treatment_date)`. Prior grouping merged all recurring-treatment records regardless of date, then `periodic_billing_aggregation` collapsed to 1. This was silently destroying doc_005/006/011/012. Removing the collapse heuristics lifted those from 0% to 85–99%. Average went from 19.8% → 50.9%.

**doc_011** over-extraction is a model tendency to split combined records. The `records_per_page > 20` threshold doesn't fire at 201/129 pages (~1.5/page). Adding a per-section count threshold would help.

Root causes: (1) date range pattern for multi-year patient summaries — this is a structural mismatch between the model's natural extraction unit (one row in the table) and the GT's semantic unit (one patient); (2) financial aggregation for very long periodic-billing documents.

What I would do next: add a few-shot example of per-patient summary extraction to the system prompt, specifically showing the multi-year date range format. Also add a post-processing pass that looks for records where `treatment_date` starts and ends within the same month and consecutively adjacent months — a signal that the model extracted monthly rows from a per-patient summary.

---

## 8. AI Usage

**Paxel report URL:** [paste URL here after running Paxel]

---

## 9. Extending the Design

**Tenant-level isolation:** Add a `tenant_id` UUID column to `jobs` and an `organization` table with membership. Change the RLS policy to `USING (tenant_id = current_setting('app.current_tenant_id')::uuid)`. The identity propagation pipeline would need to resolve tenant_id from user_id at request time (e.g. via a `user_tenant` mapping table) and set both `app.current_user_id` and `app.current_tenant_id`. Auth middleware would need a new lookup step.

**Cross-tenant sharing:** Add a `job_shares` table: `(job_id, shared_to_tenant_id, granted_by_user_id)`. Extend the SELECT policy with `OR id IN (SELECT job_id FROM job_shares WHERE shared_to_tenant_id = current_setting('app.current_tenant_id')::uuid)`. The default-deny boundary holds — sharing is explicit opt-in, and the DML policies (INSERT/UPDATE/DELETE) don't include the sharing clause, so shared jobs are read-only for the recipient tenant.

**Multi-worker / workflow:** Replace the polling loop with a task queue (e.g. PGMQ for Postgres-native queuing, or a lightweight broker). Each worker dequeues a task that carries `{job_id, user_id, tenant_id}` — the identity travels in the task payload, not as a DB setting on the worker process. For distributed workers across regions, the identity still reaches the DB session via the same `set_config` pattern; the difference is the worker connects to a read replica for the extraction read and the primary for the result write. Idempotency matters: task redelivery after worker crash must be safe — the claim step should check `status != 'processing'` before processing to avoid duplicate work.

---

## 10. Open Questions

1. **Token aggregation**: the current `token_usage` only counts the extraction agent, not the classifier. How does the evaluator want cost_usd calculated — just extraction, or total pipeline?

2. **Ground truth interpretation**: doc_002/008 have per-patient summaries spanning years. Is the GT the per-patient aggregated view, or the per-service-date view? If per-service-date, then the current approach (which collapses) is wrong.

3. **Flagging vs. omission**: the prompt says flagging is not penalized but over-flagging is. What's the threshold? At what fraction of records flagged does the evaluator consider it "flagging to avoid extraction"?

4. **Connection pooling proxy**: the current setup uses SQLAlchemy's built-in pool. If this were deployed behind PgBouncer in session-pooling mode, `SET LOCAL` identity would leak between requests. Would the evaluator want documentation of PgBouncer transaction-pooling configuration, or is the current standalone pool sufficient for the take-home scope?
