# Changelog

Newest entries at top. Updated every session per CLAUDE.md requirement.

---

## [2026-06-26] — Audit and update extraction-pipeline.md; fix executor bugs

### Fixed
- `docs/extraction-pipeline.md` — Bug audit pass: documented all 10 reported issues with verified status (fixed / not-a-bug / known gap). Updated Step 3b to clarify `page` is `str` not `int`. Updated Step 5b to document `Semaphore(4)` rate-limit guard. Updated Step 8 to explain row offset correctness and that classification tokens are included in totals. Updated fallback section to document duplication risk when classifier misses summary. Updated Key Design Decisions table with semaphore, model names (gpt-4.1 + gpt-4.1-mini), page type, token accounting rows.

Files touched: `docs/extraction-pipeline.md`, `CHANGELOG.md`

---

## [2026-06-26] — Fix extraction bugs: semaphore, classification token accounting

### Fixed
- `backend/app/ai/agents/extraction/executor.py` — Added `asyncio.Semaphore(4)` around all chunk API calls. Without this, large documents fire all chunks simultaneously, triggering 429 rate-limit errors.
- `backend/app/ai/agents/extraction/executor.py` — Classification tokens (Phase 1 classifier call) now included in `total_input`/`total_output`. Previously the classifier's API cost was invisible in `token_usage` and `cost_usd` was understated.
- `backend/app/ai/agents/extraction/executor.py` — `_classify_pages()` return type changed to `tuple[list[Page], int, int]` to return token counts alongside selected pages.

Files touched: `backend/app/ai/agents/extraction/executor.py`, `CHANGELOG.md`

---

## [2026-06-26] — Add extraction pipeline documentation

### Added
- `docs/extraction-pipeline.md` — end-to-end walkthrough of extraction pipeline: upload → worker claim → PDF parse → page classification → parallel chunked extraction → post-processing → DB write → client poll. Covers each step's purpose and design rationale. Includes Step 3b: cross-page record handling — documents the chunk boundary split risk, current mitigation (240k char budget keeps most docs in one chunk), and the future 1-page overlap + dedup fix.

Files touched: `docs/extraction-pipeline.md`, `CHANGELOG.md`

---

## [2026-06-26] — Fix treatment_date range + deterministic payments/balance correction

### Fixed
- `backend/app/ai/prompts/templates/extraction/system.j2` — `treatment_date`: medical billing ledgers now extract start date only (not full range). Imaging/pharmacy records still use full range format.
- `backend/app/ai/agents/extraction/executor.py` — Added `_fix_payments_balance()` post-processor applied after chunk merge. Computes `expected = total_charges - ins_paid - adjustment`; if `payments ≈ expected` and `balance ≈ 0.0`, swaps them (`balance = payments`, `payments = null`). Also normalises explicit `payments = 0.0` to `null` when expected balance is ~0.0 (empty column artefact). Deterministic — no model involvement.

Files touched: `backend/app/ai/prompts/templates/extraction/system.j2`, `CHANGELOG.md`

---

## [2026-06-25] — Fix payments/balance swap, duplicate CPT codes, classifier accuracy

### Fixed
- `backend/app/ai/prompts/templates/extraction/system.j2` — `payments`/`balance` column disambiguation: added explicit rule that "PT Paid" columns showing `total_charges - ins_paid - adjustment` are `balance` (patient still owes), not `payments` (already received). `payments` = null unless a separate payment transaction is explicitly recorded.
- `backend/app/ai/prompts/templates/extraction/system.j2` — CPT code deduplication bug: added rule to preserve duplicate codes when same code billed twice as separate line items.
- `backend/app/ai/agents/factory.py` — Classifier prompt tuned to prefer compact high-density pages (10+ rows). Detail pages (1–3 records/page with narrative) now correctly ranked lower than summary pages.
- `backend/app/ai/agents/extraction/executor.py` — Classifier preview increased from 500 → 800 chars so enough rows are visible to judge page density.

Files touched: `backend/app/ai/prompts/templates/extraction/system.j2`, `backend/app/ai/agents/factory.py`, `backend/app/ai/agents/extraction/executor.py`, `CHANGELOG.md`

---

## [2026-06-25] — Two-phase extraction: dynamic summary page detection + parallel chunking

### Fixed
### Changed
- `backend/app/models/extraction.py` — Added `PageClassification` pydantic model (`has_summary: bool`, `summary_pages: list[int]`).
- `backend/app/ai/agents/factory.py` — Added `build_page_classifier_agent()` using `gpt-4.1-mini` + `PageClassification` output type. Classifier receives 500-char page previews and identifies summary/ledger pages by document structure, not position.
- `backend/app/ai/agents/extraction/executor.py` — Two-phase extraction: Phase 1 classifies pages (cheap, fast), Phase 2 extracts only summary pages in parallel chunks. Fallback to all pages if no summary detected. Summary page can be anywhere in the document.
- `backend/app/ai/prompts/templates/extraction/user.j2` — Renders pages inline (`=== PAGE N ===` blocks); no tool calls.
- `backend/app/ai/agents/factory.py` — Removed `read_page`/`get_document_info` tools; upgraded model to `gpt-4.1`.
- `backend/app/ai/prompts/templates/extraction/system.j2` — Removed tool-calling workflow; reflects prompt-embedded page strategy.

Files touched: `backend/app/ai/agents/extraction/executor.py`, `backend/app/ai/prompts/templates/extraction/user.j2`, `backend/app/ai/agents/factory.py`, `backend/app/ai/prompts/templates/extraction/system.j2`, `CHANGELOG.md`

---

## [2026-06-25] — Fix Job.id NULL identity key on INSERT

### Fixed
- `backend/app/dao/models/job.py` — `id: Mapped[str] = mapped_column(String, primary_key=True)` had no `server_default`, so SQLAlchemy didn't know the DB generates the UUID. After INSERT, `id` stayed `None` → `FlushError: Instance has a NULL identity key`. Fixed by adding `server_default=text("gen_random_uuid()::text")`, which tells SQLAlchemy to emit `RETURNING id` and populate the ORM object post-INSERT.

Files touched: `backend/app/dao/models/job.py`, `CHANGELOG.md`

---

## [2026-06-25] — Fix SET LOCAL bind-parameter syntax error + Alembic async migration never committing DDL

### Fixed
- `backend/app/service/job_service.py` + `backend/app/service/extraction_service.py` — `SET LOCAL app.current_user_id = $1` fails with PostgresSyntaxError because PostgreSQL `SET` commands do not accept bind parameters. Replaced with `SELECT set_config('app.current_user_id', :uid, true)` — `set_config` is a function and accepts parameterized values; the `true` third argument makes it transaction-local (equivalent to `SET LOCAL`).

Files touched: `backend/app/service/job_service.py`, `backend/app/service/extraction_service.py`, `CHANGELOG.md`

---

## [2026-06-25] — Fix Alembic async migration never committing DDL

### Fixed
- `backend/alembic/env.py` — `run_migrations_online()` called `context.configure()` and `context.run_migrations()` in two separate `run_sync` callbacks without `context.begin_transaction()`. SQLAlchemy 2.0 `async with engine.connect()` does NOT auto-commit; the implicit transaction was rolled back on `AsyncConnection.close()`, so all DDL executed but nothing persisted. Fixed by: (1) combining configure + run_migrations in a single `_do_run_migrations(connection)` callback, (2) wrapping with `context.begin_transaction()` so Alembic commits the transaction, (3) using `NullPool` on the migration engine (recommended for one-shot migration scripts).

Files touched: `backend/alembic/env.py`, `CHANGELOG.md`

---

## [2026-06-24] — Backend auth (register/login, session validation, dual-CM lifespan)

### Added
- `backend/alembic/versions/c3d5e7f9a1b2_add_auth_tables_and_default_privileges.py` — migration chaining off b9c4f2a1e835: creates `user`, `account`, `session` tables (Better Auth-compatible, camelCase columns); grants billing_app access; sets ALTER DEFAULT PRIVILEGES so future tables automatically grant to billing_app; downgrade reverses in correct order
- `backend/app/api/routes/auth.py` — `POST /auth/register` (email uniqueness check, bcrypt hash, user+account+session rows, returns token + user); `POST /auth/login` (lookup user by email, bcrypt verify, new session, returns token + user); both use `request.app.state.admin_cm` for raw SQL
- `backend/app/api/dependencies/auth.py` — `get_current_user_id(request)`: reads `Authorization: Bearer <token>`, queries `session` table via admin_cm, raises 401 on missing/expired token, returns userId

### Changed
- `backend/pyproject.toml` — added `bcrypt>=4.0.0`
- `backend/app/api/main.py` — lifespan now creates two ContextManagers: `admin_cm` (billing role, stored on `app.state.admin_cm`) and `app_cm` (billing_app, RLS-subject, used for ServiceContainer); added CORS middleware for `http://localhost:3000`; added auth router at `/auth`; closes both CMs on shutdown
- `backend/app/api/routes/jobs.py` — removed placeholder `get_current_user_id`; now imports real `get_current_user_id` from `app.api.dependencies.auth`; no other logic changes
- `backend/app/api/routes/health.py` — uses `request.app.state.admin_cm` instead of removed `context_manager`

Files touched: `backend/alembic/versions/c3d5e7f9a1b2_add_auth_tables_and_default_privileges.py`, `backend/app/api/routes/auth.py`, `backend/app/api/dependencies/auth.py`, `backend/pyproject.toml`, `backend/app/api/main.py`, `backend/app/api/routes/jobs.py`, `backend/app/api/routes/health.py`, `CHANGELOG.md`

---

## [2026-06-24] — Implement extraction pipeline (PDF parsing, agent, tools, service)

### Added
- `backend/pyproject.toml` — added `pdfplumber>=0.11.0`
- `backend/app/ai/prompts/templates/extraction/system.j2` — detailed system prompt: document types (ledger, imaging, pharmacy), extraction rules (CPT/HCPCS codes, provider vs custodian, insurers vs third_parties, TP Paid / PT Paid columns, null vs 0.0), flagging rules (severity tiers, over-flagging note), workflow instructions
- `backend/app/ai/prompts/templates/extraction/user.j2` — user prompt template; renders doc_id, page count, per-page 300-char previews; instructs agent to call get_document_info() then read_page() on relevant pages
- `backend/app/ai/agents/extraction/executor.py` — `ExtractionAgentExecutor`: renders user.j2, calls `Runner.run` with max_turns=25, returns `(ExtractionOutput, usage)`

### Changed
- `backend/app/ai/tools.py` — added `read_page(ctx, page_num)` (1-indexed, validates range, returns page text or error string) and `get_document_info(ctx)` (page count + 150-char previews of all pages)
- `backend/app/models/extraction.py` — added `ExtractionOutput(records: list[BillingRecord], flagged: list[FlaggedRecord])`
- `backend/app/ai/agents/factory.py` — added `build_extraction_agent()`: model=gpt-4o-mini, output_type=ExtractionOutput, tools=[read_page, get_document_info], instructions from extraction/system.j2
- `backend/app/service/extraction_service.py` — full `process_job(job_id, user_id)` implementation: fetches job with SET LOCAL identity, parses PDF with pdfplumber, builds RunContext, runs ExtractionAgentExecutor, computes token_usage + cost_usd (gpt-4o-mini pricing) + processing_duration_seconds, writes completed/failed status; never raises — inner except writes failure to job row

Files touched: `backend/pyproject.toml`, `backend/app/ai/prompts/templates/extraction/system.j2`, `backend/app/ai/prompts/templates/extraction/user.j2`, `backend/app/ai/tools.py`, `backend/app/models/extraction.py`, `backend/app/ai/agents/factory.py`, `backend/app/ai/agents/extraction/executor.py`, `backend/app/service/extraction_service.py`, `CHANGELOG.md`

---

## [2026-06-24] — Implement worker loop with dual-connection RLS architecture

### Added / Changed
- `backend/app/config/settings.py` — added `APP_DB_CONNECTION_STRING: str = ""` (billing_app role, RLS-subject; falls back to admin conn if empty)
- `backend/app/core/context_manager.py` — added optional `connection_string` param to `__init__`; `initialize()` now uses `self._connection_string` instead of hardcoded `settings.POSTGRES_CONNECTION_STRING`; defaults to admin conn if param is None or empty
- `backend/app/worker/loop.py` — full implementation replacing stubbed sleep loop:
  - Two `ContextManager` instances: `admin_cm` (billing role, bypasses RLS) and `app_cm` (billing_app role, subject to RLS)
  - `JobDAO(admin_cm)` for `claim_next_job` and `recover_stalled` — these must see all users' jobs
  - `ExtractionService(app_cm)` for result writes — uses SET LOCAL identity per job owner
  - Stall recovery on startup (`iteration == 0`) and every 12 iterations (~60s at 5s poll); logs count when > 0
  - Claim loop: admin session → `claim_next_job` → if claimed, `extraction_service.process_job(job_id, user_id)`; if empty, sleep
  - Outer `except Exception` catches all errors, logs `worker_loop_error`, sleeps before retrying
- `backend/app/service/extraction_service.py` — updated `process_job` signature to `(self, job_id: str, user_id: str) -> None`; added docstring explaining SET LOCAL requirement for RLS isolation

Files touched: `backend/app/config/settings.py`, `backend/app/core/context_manager.py`, `backend/app/worker/loop.py`, `backend/app/service/extraction_service.py`, `CHANGELOG.md`

---

## [2026-06-24] — Implement /jobs API routes (all stubs → real endpoints)

### Changed
- `backend/app/api/routes/jobs.py` — replaced all `NotImplementedError` stubs:
  - `get_current_user_id(request)` — placeholder auth dependency; reads `X-User-Id` header, raises 401 if missing; TODO comment marks M1 replacement point
  - `POST /jobs` (201): reads `UploadFile` bytes, computes SHA-256; passes `content_hash=None` when `bypass_cache=True`; delegates to `job_service.create_job`
  - `GET /jobs`: optional `?status=` query param; validates against `_VALID_STATUSES` frozenset, raises 422 on invalid; delegates to `job_service.list_jobs`
  - `GET /jobs/active`: defined before `/{job_id}` so FastAPI matches literal path first; delegates to `job_service.get_active_jobs`
  - `GET /jobs/{job_id}`: delegates to `job_service.get_job`; `JobNotFoundException` propagates to main.py handler → 404
  - `DELETE /jobs/{job_id}`: delegates to `job_service.cancel_job`; `JobNotFoundException` → 404, `JobNotCancellableException` → 409 via main.py handler

Files touched: `backend/app/api/routes/jobs.py`, `CHANGELOG.md`

---

## [2026-06-24] — Implement JobService (all stubs → real async code)

### Changed
- `backend/app/service/job_service.py` — replaced all `NotImplementedError` stubs:
  - `__init__`: added `get_settings()` call to access `PDF_MOUNT_PATH`
  - `_set_user_identity(session, user_id)`: new helper; runs `SET LOCAL app.current_user_id = :uid` before every DAO call so RLS policies fire correctly
  - `create_job(user_id, pdf_filename, pdf_bytes, content_hash)`: generates uuid4 filename, writes PDF to `PDF_MOUNT_PATH` via `asyncio.to_thread` (outside DB transaction), then inserts job row; TODO comment marks M3 cache-check location
  - `get_job(user_id, job_id)`: sets identity, calls DAO get, raises `JobNotFoundException` if None (RLS makes another user's job indistinguishable from not-found)
  - `list_jobs(user_id, status)`: sets identity, delegates to DAO list; RLS scopes result automatically
  - `get_active_jobs(user_id)`: sets identity, delegates to DAO get_active
  - `cancel_job(user_id, job_id)`: sets identity, calls DAO cancel; if None, re-fetches within same session to distinguish 404 (not found) vs 409 (wrong status); raises `JobNotFoundException` or `JobNotCancellableException` accordingly

Files touched: `backend/app/service/job_service.py`, `CHANGELOG.md`

---

## [2026-06-24] — Implement JobDAO (all stubs → real SQLAlchemy 2.0 async code)

### Changed
- `backend/app/dao/pg/job_dao.py` — replaced all `NotImplementedError` stubs:
  - `_to_orm`: builds `Job` ORM instance from dict
  - `_to_dto`: maps all `Job.__mapper__.column_attrs` → plain dict; converts `uuid.UUID→str`, `Decimal→float`, `datetime→isoformat`
  - `_row_to_dto`: same conversion for raw `text()` RETURNING result mappings
  - `_apply_filters`: applies optional `status` filter to a select query
  - `create(session, user_id, pdf_filename, pdf_path, content_hash)`: `session.add` + `flush` + `refresh`; id populated by server default
  - `get(session, job_id)`: `select(Job).where(id==)`, returns dict or None
  - `list(session, status)`: `select(Job)` ordered by `created_at DESC`, optional status filter
  - `get_active(session)`: `WHERE status='processing'` ordered by `started_at DESC`
  - `update_status(session, job_id, status, ...)`: ORM `update().returning(Job)`; sets `started_at` when status→processing, `completed_at` when →completed/failed/cancelled
  - `cancel(session, job_id)`: `UPDATE WHERE id=? AND status='pending'`; returns dict or None (None = not found or wrong status)
  - `claim_next_job(session)`: CTE `SELECT … FOR UPDATE SKIP LOCKED` + `UPDATE … RETURNING jobs.*` in one atomic statement; TODO comment: caller must pass admin session (billing role) to bypass RLS
  - `recover_stalled(session, timeout_minutes)`: `UPDATE WHERE status='processing' AND started_at < now() - interval`; returns rowcount

Files touched: `backend/app/dao/pg/job_dao.py`, `CHANGELOG.md`

---

## [2026-06-24] — Fix migration: remove FORCE RLS, add sequence grants

### Changed
- `backend/alembic/versions/b9c4f2a1e835_add_user_id_rls_and_metrics.py`:
  - Removed `ALTER TABLE jobs FORCE ROW LEVEL SECURITY` from `upgrade()` — FORCE subjects the owner role (`billing`) to RLS too, which breaks Alembic migrations that run without `app.current_user_id` set; `billing_app` (non-owner) remains fully subject to RLS without it
  - Removed `ALTER TABLE jobs NO FORCE ROW LEVEL SECURITY` from `downgrade()` accordingly
  - Added `GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO billing_app` in `upgrade()` — needed for any future serial/sequence columns
  - Added `REVOKE USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public FROM billing_app` in `downgrade()` before role drop

Files touched: `backend/alembic/versions/b9c4f2a1e835_add_user_id_rls_and_metrics.py`, `CHANGELOG.md`

---

## [2026-06-24] — Add user_id/RLS/metrics migration and update Job ORM model

### Added
- `backend/alembic/versions/b9c4f2a1e835_add_user_id_rls_and_metrics.py` — new migration (chains off `0de1443cd0f2`):
  - Columns: `user_id UUID NOT NULL`, `content_hash VARCHAR(64)`, `token_usage JSONB`, `cost_usd NUMERIC(10,6)`, `processing_duration_seconds NUMERIC(10,3)`
  - Indexes: `idx_jobs_user_id`, `idx_jobs_user_content_hash` (partial `WHERE status='completed'`)
  - Role: `billing_app` with LOGIN, CONNECT + USAGE + SELECT/INSERT/UPDATE/DELETE grants
  - RLS: `ENABLE ROW LEVEL SECURITY` + `FORCE ROW LEVEL SECURITY` on `jobs`
  - Policies: `jobs_select_policy`, `jobs_insert_policy`, `jobs_update_policy`, `jobs_delete_policy` — all keyed on `current_setting('app.current_user_id', true)::uuid`
  - `downgrade()` reverses in correct order: drop policies → disable RLS → revoke/drop role → drop indexes → drop columns

### Changed
- `backend/app/dao/models/job.py` — added ORM columns for all 5 new fields: `user_id` (`UUID(as_uuid=True)`), `content_hash` (`String(64)`), `token_usage` (`JSONB`), `cost_usd` (`Numeric(10,6)`), `processing_duration_seconds` (`Numeric(10,3)`); added two new indexes to `__table_args__`; added imports for `uuid`, `Decimal`, `Numeric`, `UUID`

Files touched: `backend/alembic/versions/b9c4f2a1e835_add_user_id_rls_and_metrics.py`, `backend/app/dao/models/job.py`, `CHANGELOG.md`

---

## [2026-06-24] — Add frontend + backend implementation instructions to CLAUDE.md

### Changed
- `CLAUDE.md` — added "Implementation Instructions" section: smoke tests, frontend screen list, auth topology flow, Docker wiring, backend stub-fill guide (JobDAO, JobService, routes, ExtractionService, worker loop, extraction agent, caching), Alembic migration workflow, key file reading order

Files touched: `CLAUDE.md`, `CHANGELOG.md`

---

## [2026-06-24] — Expand CLAUDE.md with full assignment constraints

### Changed
- `CLAUDE.md` — added missing constraints from ASSIGNMENT.md: job metrics (`token_usage`, `cost_usd`, `processing_duration_seconds`), content-based caching spec, cache bypass flag, `GET /jobs/{job_id}` isolation rule, `DELETE` 409 behavior, connection pooling hazard for `SET LOCAL`, worker identity pattern, retry/stall-recovery requirements, `AGENTS.md` deliverable, design doc required sections, extraction field weights, evaluation priority order, deliverables checklist, flagging rubric

Files touched: `CLAUDE.md`, `CHANGELOG.md`

---

## [2026-06-24] — Add CLAUDE.md and initialize CHANGELOG

### Added
- `CLAUDE.md` — full project reference: purpose, tech stack, file structure, patterns, API contract, data models, milestones, constraints, run instructions
- `CHANGELOG.md` — this file; tracks all code/file changes going forward

Files touched: `CLAUDE.md`, `CHANGELOG.md`
