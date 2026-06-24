# CLAUDE.md — Medical Billing Records Assignment

## Project Purpose

Full-stack AI-native take-home assignment. Multi-user SaaS platform that extracts structured billing data from medical PDFs using OpenAI Agents SDK. Users upload PDFs, a background worker claims jobs atomically, and an AI pipeline extracts `BillingRecord` / `FlaggedRecord` output. Per-user isolation enforced by Postgres Row-Level Security.

## CHANGELOG REQUIREMENT (MANDATORY)

**Every time you modify files or write code, update `CHANGELOG.md` in the root folder.**

- File must exist at `CHANGELOG.md` (root level). Create it if missing.
- Use this format:

```markdown
## [YYYY-MM-DD] — <short description>

### Added
- ...

### Changed
- ...

### Fixed
- ...

Files touched: `path/to/file1`, `path/to/file2`
```

- One entry per working session/task. Append to top (newest first).
- Never skip this step. It is required after every code change.

---

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Next.js + Better Auth, port 3000 |
| Backend API | FastAPI (async) + Uvicorn, port 8000 |
| Worker | Python asyncio polling loop, 2 replicas |
| Database | PostgreSQL 16, RLS enforced |
| ORM | SQLAlchemy 2.0 async + asyncpg |
| Migrations | Alembic |
| AI | OpenAI Agents SDK (`openai-agents>=0.15.1`) |
| Prompt templates | Jinja2 |
| Logging | structlog (JSON) |
| Config | Pydantic Settings (.env) |
| Containers | Docker + Docker Compose |

---

## File Structure

```
medical-billing-records-assignment-package/
├── CLAUDE.md                        ← this file
├── AGENTS.md                        ← YOU CREATE: AI agent working guide for repo
├── CHANGELOG.md                     ← update every session
├── ASSIGNMENT.md                    ← full spec (milestones M1–M4)
├── README.md                        ← ops guide (docker compose up, smoke tests)
├── docker-compose.yml               ← full stack: postgres, api, worker, web
├── .env.example                     ← all required env vars
├── .gitignore
│
├── data/                            ← 12 sample PDFs + ground truth JSON
│   ├── doc_001.pdf
│   ├── doc_001_gt.json              ← ground truth: {doc_id, records[]}
│   └── ... (doc_002–doc_012)
│
├── docs/
│   ├── domain.md                    ← medical billing domain reference — READ BEFORE CODING EXTRACTION
│   ├── schema.md                    ← BillingRecord + FlaggedRecord spec
│   └── design.md                    ← YOUR hand-written design doc (fill this in; must include Paxel URL)
│
├── frontend/                        ← YOU BUILD THIS (Next.js + Better Auth)
│   └── README.md                    ← build instructions
│
└── backend/
    ├── Dockerfile                   ← Python 3.12, uv-based
    ├── main.py                      ← uvicorn entry: app.api.main:app
    ├── worker.py                    ← worker entry: app.worker.loop
    ├── pyproject.toml               ← Python deps
    ├── uv.lock
    ├── .python-version              ← 3.12
    ├── alembic.ini
    ├── scripts/
    │   └── migrate.sh               ← runs alembic upgrade head, then exec
    ├── pdfs/                        ← shared upload volume (Docker mount)
    ├── alembic/
    │   ├── env.py
    │   └── versions/
    │       └── 0de1443cd0f2_initial.py
    └── app/
        ├── api/
        │   ├── main.py              ← FastAPI app + lifespan (ContextManager + ServiceContainer)
        │   ├── routes/
        │   │   ├── health.py        ← GET /health (public)
        │   │   └── jobs.py          ← POST/GET/DELETE /jobs — ALL STUBS
        │   ├── schema/
        │   │   └── __init__.py      ← SuccessResponse, ErrorResponse
        │   └── dependencies/
        │       └── container.py     ← FastAPI DI helpers
        ├── config/
        │   └── settings.py          ← pydantic-settings, .env-backed
        ├── core/
        │   ├── context_manager.py   ← DB lifecycle (initialize, get_session, close)
        │   ├── database/
        │   │   ├── base_database.py
        │   │   └── postgres.py      ← AsyncEngine + sessionmaker factory
        │   └── common/
        │       ├── logger.py        ← structlog JSON
        │       ├── time.py
        │       └── id/
        │           ├── short_id.py
        │           └── snowflake.py
        ├── dao/
        │   ├── base_pg_dao.py       ← base class for SQL access
        │   ├── models/
        │   │   ├── base.py          ← TimestampBase ORM base
        │   │   └── job.py           ← Job model (id, status, pdf_path, result JSONB, ...)
        │   └── pg/
        │       └── job_dao.py       ← JobDAO — ALL STUBS (incl. atomic claim_next_job)
        ├── service/
        │   ├── base_service.py
        │   ├── container.py         ← ServiceContainer (DI root)
        │   ├── exceptions.py        ← BaseServiceException, JobNotFoundException, etc.
        │   ├── job_service.py       ← JobService — ALL STUBS
        │   └── extraction_service.py ← ExtractionService.process_job — STUB
        ├── models/
        │   └── extraction.py        ← Pydantic: BillingRecord, FlaggedRecord
        ├── ai/
        │   ├── config.py            ← AgentConfig, ECHO_AGENT_CONFIG
        │   ├── context.py           ← RunContext (shared pipeline state)
        │   ├── types.py             ← Document, Page, RunMetrics
        │   ├── orchestrator.py      ← ExtractionOrchestrator (pipeline runner)
        │   ├── tools.py             ← echo_tool (demo tool)
        │   ├── agents/
        │   │   ├── factory.py       ← AgentFactory.build_echo_agent()
        │   │   └── echo/
        │   │       └── executor.py  ← EchoAgentExecutor (working demo — study this)
        │   ├── prompts/
        │   │   ├── prompt_loader.py ← Jinja2 template loader
        │   │   └── templates/
        │   │       └── echo/
        │   │           ├── system.j2
        │   │           └── user.j2
        │   └── utils/
        │       └── concurrency.py
        └── worker/
            └── loop.py              ← polling loop (claim → process → write) — MOSTLY STUBBED
```

---

## Key Patterns

### DI / Startup Flow
`docker compose up` → `scripts/migrate.sh` runs Alembic → API starts → `ContextManager` inits Postgres → `ServiceContainer` wires DAOs + Services.

### Job Lifecycle
```
pending → processing → completed
                    ↘ failed
pending → cancelled
```
`POST /jobs` (upload PDF) → Job row inserted (status=`pending`) → Worker polls, claims atomically → `ExtractionService.process_job()` → status=`completed` with JSONB result **or** `failed` with error.

A job that transitions to `processing` must **never** silently revert to `pending`.

### AI Pipeline Pattern (study `echo/executor.py`)
```
AgentFactory.build_*() → Agent[RunContext]
ExtractionOrchestrator.run(agent, context) → aggregates RunMetrics
PromptLoader.render("template_name", vars) → rendered string
```

### RLS Pattern (you implement)
- Two DB roles: `billing` (owner/migration) and `billing_app` (RLS-subject)
- Every API/worker session: `SET LOCAL app.current_user_id = '<uuid>'`
- RLS policy: `USING (user_id = current_setting('app.current_user_id')::uuid)`
- **Connection pooling hazard**: `SET LOCAL` is transaction-scoped. Under a transaction-pooling proxy (e.g. PgBouncer), the setting leaks to the next user unless you re-set it at the start of every transaction. Document how you handle this.

### Worker Identity Pattern
The background worker has no HTTP session. You must decide how it establishes DB identity when writing a job result (e.g. using the `user_id` stored on the job row itself). Document this in `docs/design.md`.

---

## Environment Variables

| Variable | Purpose |
|---|---|
| `OPENAI_API_KEY` | Required for extraction agents |
| `POSTGRES_CONNECTION_STRING` | Admin role (Alembic migrations) |
| `APP_DB_CONNECTION_STRING` | App role (RLS-enforced, runtime) |
| `PDF_MOUNT_PATH` | Where PDFs are stored (`/app/pdfs`) |
| `WORKER_POLL_INTERVAL_SECONDS` | Worker polling cadence |
| `BETTER_AUTH_SECRET` | Next.js auth secret (long random string) |
| `BETTER_AUTH_URL` | Frontend URL for auth redirects |
| `NEXT_PUBLIC_API_BASE_URL` | Backend URL for frontend API calls |
| `DATABASE_URL` | Postgres URL for Better Auth tables |

Copy `.env.example` → `.env` and fill in `OPENAI_API_KEY` and `BETTER_AUTH_SECRET`.

---

## API Contract

Do not rename or remove any endpoint. All `/jobs` routes return only the authenticated caller's data.

| Method | Path | Auth | Key Behavior |
|---|---|---|---|
| GET | `/health` | public | Returns `{"status":"ok","db":"ok"}`; checks live DB connectivity every call |
| POST | `/jobs` | required | Upload PDF; create job owned by caller; supports cache bypass flag (header or query param, your choice) |
| GET | `/jobs` | required | List own jobs; optional `?status=pending\|processing\|completed\|failed` |
| GET | `/jobs/active` | required | List processing jobs; must reflect live state — never cached |
| GET | `/jobs/{job_id}` | required | Full job detail; another user's job ID must be **indistinguishable from non-existent** |
| DELETE | `/jobs/{job_id}` | required | Cancel pending job; return **409** if already processing or completed |

### Content-Based Caching (M3, but flag required from M2)
- `POST /jobs`: if uploaded file content matches a prior completed job **owned by the same user**, return a new job record in `completed` state reusing cached result
- Fingerprint by **file content** (not filename)
- Cache is **per-user** — a cache hit must never cross user boundaries
- Bypass flag (header or query param) skips cache, always runs full extraction

### Job Metrics (required M2+)
Every job response must include these three fields (JSON `null` until known):

| Field | What to capture |
|---|---|
| `token_usage` | LLM token counts: at least `input`, `output`, `total` |
| `cost_usd` | Estimated USD spend; document pricing assumptions |
| `processing_duration_seconds` | Wall-clock time from worker start to terminal state |

---

## Data Models

### BillingRecord
`treatment_date`, `cpt_codes[]`, `description`, `provider`, `insurers[]`, `third_parties[]`, `total_charges`, `ins_paid`, `adjustment`, `payments`, `balance`, `page`

### FlaggedRecord
`row` (index into records[] or null), `fields[]` (BillingRecord field names), `reason`, `page`, `severity` (low/medium/high)

### Ground Truth Format
`data/doc_*_gt.json` uses camelCase (`treatmentDate`, `cptCodes`, `insPaid`). Your models use snake_case — handle conversion in evaluation/testing.

### Extraction Field Weights
| Weight | Fields |
|---|---|
| High | `treatment_date`, `cpt_codes`, `total_charges`, `ins_paid`, `adjustment`, `payments`, `balance` |
| Medium | `provider`, `page`, `insurers`, `third_parties` |
| Low | `description` |

---

## Milestones

| # | Name | Status |
|---|---|---|
| M1 | Auth + RLS | TODO |
| M2 | Extraction behind auth | TODO |
| M3 | Reliability (retry, stall recovery, caching) | TODO |
| M4 | Frontend UX | TODO |

A smaller system fully working through M2 beats a sprawling one working nowhere.

---

## Critical Constraints

### Hard Requirements (breaking = automatic fail on affected milestone)
- **Docker Compose required** — `docker compose up` must start frontend + API + worker + Postgres cleanly; milestone scores zero if it doesn't
- **No LangChain / CrewAI / LlamaIndex / AutoGen** — OpenAI Agents SDK or direct API calls only
- **RLS must be DB-enforced** — app-layer `WHERE user_id = ...` does not satisfy the isolation guarantee; the `billing_app` role must be subject to RLS policies; app must not connect as owner/superuser at runtime
- **Atomic job claiming** — two workers must never claim the same job; use `SELECT ... FOR UPDATE SKIP LOCKED`; document what breaks if removed
- **Git history** — incremental commits required; single squashed commit or re-init is an automatic fail
- **API contract intact** — do not rename or remove any endpoint
- **New DB schema → new Alembic migration** — never edit existing migrations

### Strong Requirements (evaluated hard in debrief)
- **Worker identity** — background worker must establish correct DB identity before writing results; this must be in code, not just prose
- **`GET /jobs/{job_id}` isolation** — another user's job ID must return same response as a non-existent job (no 403 that leaks existence)
- **`DELETE /jobs/{job_id}`** — must return 409 if job is already processing or completed
- **Connection pooling safety** — `SET LOCAL` is transaction-scoped; document how you handle identity under a pooled connection
- **Retries (M3)** — transient failures (timeouts, rate limits) must not flip job straight to `failed`; use bounded retries with backoff; document what counts as retryable
- **Stall recovery (M3)** — jobs stuck in `processing` after a worker crash must be recoverable; document when recovery triggers
- **Flagging correctness** — flagged uncertain records are NOT penalized; confident wrong values are the failure mode; do not over-flag (flagging almost everything = avoiding extraction)

### Deliverables Checklist
- [ ] `AGENTS.md` at repo root — how AI coding agents should work in this repo; project layout, run/test commands, conventions, workflow you used
- [ ] `docs/design.md` — hand-written, precise; include auth topology, RLS implementation, worker identity, accuracy/failure analysis, Paxel report URL
- [ ] Tests — core extraction logic + at least one E2E lifecycle test with an unhappy path
- [ ] `README.md` — gets reviewer from clone → `docker compose up` → sign-up → upload → result, no guesswork
- [ ] `.env.example` — all required vars documented
- [ ] Alembic migrations for any schema additions (RLS policies, auth tables, new columns)

### Design Doc Requirements (`docs/design.md`) — must include:
1. Auth topology: where session is created/validated, how Python API learns caller identity
2. How user identity reaches DB session so RLS policies can act on it
3. How `SET LOCAL` interacts with connection pooling
4. How background worker establishes correct DB identity (no HTTP session)
5. Concurrency mechanism for atomic job claiming
6. Caching fingerprinting approach + failure modes
7. Retry strategy: what counts as retryable, bounds, backoff
8. Stall recovery: when it triggers, how
9. Honest extraction accuracy / failure analysis
10. Paxel report URL

### Do Before Writing Extraction Code
Read `docs/domain.md` and `docs/schema.md`. Do a manual pass over every sample PDF + its ground truth. If you can't label samples correctly with the schema in front of you, the model won't do it reliably either.

---

## Evaluation Priority Order

1. **Backend depth** — isolation truly DB-enforced; topology coherent; worker handles identity correctly
2. **AI agent design** — tools chosen and why; navigation strategy; uncertainty handling; field-level accuracy on held-out docs
3. **Code quality** — clean API/service/DAO separation; no global mutable state; meaningful errors; tests
4. **Full-stack runnability** — clone → `docker compose up` → sign up → upload → result, no guesswork
5. **Frontend** — working knowledge bar; functional beats elaborate
6. **Design document** — hand-written, precise, defensible

---

## Running Locally

```bash
cp .env.example .env
# fill in OPENAI_API_KEY and BETTER_AUTH_SECRET
docker compose up --build
# API: http://localhost:8000
# Frontend: http://localhost:3000 (after you build it)
```

---

## Implementation Instructions

### Smoke Tests (run after each milestone)

```bash
# 1. Health check
curl -s http://localhost:8000/health | python -m json.tool
# Expected: {"status": "ok", "db": "ok"}

# 2. Swagger UI
open http://localhost:8000/docs

# 3. Worker logs
docker compose logs worker --tail 30

# 4. Isolation check (the one that matters)
# Signed in as user A, fetch user B's job ID via API → must get nothing
# Connect as billing_app role directly to DB → same result
```

Tear down + fresh DB:
```bash
docker compose down -v
```

---

## Frontend Instructions (`frontend/`)

### What to Build

| Screen | Required |
|---|---|
| Sign Up | Yes — email/password minimum |
| Sign In | Yes |
| Protected dashboard | Yes — redirects unauthenticated users |
| Upload PDF | Yes — calls `POST /jobs` with auth token |
| Job list | Yes — polls or refreshes, shows status |
| Job detail / result | Yes — shows BillingRecord table + FlaggedRecord highlights |

### Tech Choices
- **Framework**: Next.js — App Router or Pages Router (your choice; justify in `docs/design.md`)
- **Auth**: Better Auth — wire it in, migrate auth tables into Postgres
- **Port**: `3000`
- **API communication**: fetch against `NEXT_PUBLIC_API_BASE_URL` (env var)

### Environment Variables Needed
```
BETTER_AUTH_SECRET=<long random string>
BETTER_AUTH_URL=http://localhost:3000
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
DATABASE_URL=postgresql://billing:billing@postgres:5432/billing
```

### Docker Requirements
- Add `Dockerfile` inside `frontend/`
- Uncomment and fill the `web` service skeleton in root `docker-compose.yml`
- Serve on port `3000`
- `docker compose up` must start the web service alongside API + worker + Postgres

### Auth → API Identity Flow (you design, document in `docs/design.md`)
- Better Auth issues session token/JWT in Next.js app
- Frontend passes token to Python API (Authorization header or cookie)
- Python API validates token, extracts `user_id`
- API sets `SET LOCAL app.current_user_id = '<uuid>'` on every DB transaction so RLS policies fire

### Frontend Bars
- Functional + isolation-correct > elaborate
- Another user's data leaking through the UI = fail, regardless of design quality
- AI design tooling (Claude `design`, `impeccable.style`) is encouraged for polish

---

## Backend Instructions (`backend/`)

### What to Implement (all stubs → real code)

#### 1. Database / RLS (M1)
- Create `billing_app` Postgres role (non-owner, no `BYPASSRLS`)
- Enable RLS on every user-owned table: `ALTER TABLE jobs ENABLE ROW LEVEL SECURITY`
- Write RLS policies using `current_setting('app.current_user_id')::uuid`
- Add `user_id` column to `jobs` table
- New Alembic migration for every schema change — never edit existing ones
- API + worker must connect via `APP_DB_CONNECTION_STRING` (the RLS-subject role), not the admin role

#### 2. Identity Propagation (M1/M2)
Every DB session at runtime must run:
```sql
SET LOCAL app.current_user_id = '<uuid>';
```
Inside a transaction, before any DML or SELECT on user-owned tables. Wire this into `ContextManager.get_session()` or a SQLAlchemy event listener.

**Connection pooling**: `SET LOCAL` is transaction-scoped. If using a transaction-pooled proxy, the setting resets between transactions — re-set it at the start of every transaction. Document your approach.

#### 3. Worker Identity (M2)
Worker has no HTTP session. Strategy: read `user_id` from the claimed job row, then `SET LOCAL app.current_user_id` before writing the result. This must be in code.

#### 4. JobDAO (`app/dao/pg/job_dao.py`) — fill stubs
```python
create_job(user_id, pdf_filename, pdf_path, content_hash) → Job
get_job(job_id) → Job | None
list_jobs(user_id, status=None) → list[Job]
claim_next_job() → Job | None          # SELECT FOR UPDATE SKIP LOCKED
update_job_status(job_id, status, ...) → Job
cancel_job(job_id) → Job
```

Atomic claim pattern:
```sql
SELECT * FROM jobs
WHERE status = 'pending'
ORDER BY created_at
LIMIT 1
FOR UPDATE SKIP LOCKED
```

#### 5. JobService (`app/service/job_service.py`) — fill stubs
- `create_job`: save PDF to `PDF_MOUNT_PATH`, insert job row, check content-hash cache
- `get_job`: RLS enforces ownership; return `None` for not-found and wrong-owner alike
- `list_jobs`: pass status filter to DAO
- `cancel_job`: check status, return 409 if processing/completed
- `claim_next_job`: delegate to DAO atomic claim
- `recover_stalled`: find jobs stuck in `processing` past timeout, reset to `pending` (M3)

#### 6. API Routes (`app/api/routes/jobs.py`) — fill stubs
- Validate auth on every `/jobs` route (middleware or dependency)
- Inject `user_id` from validated session into service calls
- `POST /jobs`: accept `multipart/form-data`, call `JobService.create_job`
- `DELETE /jobs/{job_id}`: call `JobService.cancel_job`; raise 409 on wrong status
- `GET /jobs/active`: never cache; always live DB query

#### 7. ExtractionService (`app/service/extraction_service.py`) — fill stub
```
load PDF → parse pages → build RunContext → run ExtractionOrchestrator → write result
```
- Record `token_usage`, `cost_usd`, `processing_duration_seconds` on every job
- On success: `status=completed`, write JSONB result
- On failure after retries: `status=failed`, write error detail

#### 8. Worker Loop (`app/worker/loop.py`) — fill stubs
```
loop:
  job = claim_next_job()
  if job:
    SET LOCAL user_id = job.user_id
    ExtractionService.process_job(job)
  else:
    sleep(WORKER_POLL_INTERVAL_SECONDS)
```
- 2 replicas by default (docker-compose scale)
- Bounded retries with backoff for transient failures (M3)
- Stall recovery: on startup and periodically, reset jobs stuck in `processing` past timeout (M3)

#### 9. Extraction Agent (M2) — build in `app/ai/`
Study `app/ai/agents/echo/executor.py` as the pattern. Build your own:
- `AgentFactory.build_extraction_agent()` → `Agent[RunContext]`
- Tools: page reader, table extractor, navigation (jump to page), uncertainty flagging
- Prompts in `app/ai/prompts/templates/extraction/` (system.j2, user.j2)
- Must produce `BillingRecord[]` + `FlaggedRecord[]` matching `app/models/extraction.py`
- Read `docs/domain.md` and `docs/schema.md` before writing any prompt

#### 10. Content-Based Caching (M3)
- Hash PDF content (e.g. SHA-256) at upload time; store hash on job row
- On `POST /jobs`: query for prior completed job with same hash + same user_id → return cached result as new completed job
- Bypass: if `X-Bypass-Cache: true` header (or `?bypass_cache=1` query param) present, skip cache
- Cache must never cross user boundaries (hash lookup scoped by `user_id`)

### Alembic Migration Workflow
```bash
# Generate new migration (from inside backend container or with venv active)
alembic revision --autogenerate -m "description"

# Apply
alembic upgrade head

# In Docker: migrations run automatically via scripts/migrate.sh at container start
```
Never edit `alembic/versions/0de1443cd0f2_initial.py` or any existing migration.

### Key File Reading Order
1. `docs/domain.md` — billing domain rules
2. `docs/schema.md` — output schema
3. `app/ai/agents/echo/executor.py` — agent pattern to follow
4. `app/dao/pg/job_dao.py` — stubs to implement
5. `app/service/job_service.py` — stubs to implement
6. `app/worker/loop.py` — stubs to implement
