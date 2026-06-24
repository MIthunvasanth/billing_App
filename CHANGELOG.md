# Changelog

Newest entries at top. Updated every session per CLAUDE.md requirement.

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
