# AGENTS.md — AI Agent Working Guide

## Project
Full-stack medical billing extraction platform. FastAPI backend + Next.js frontend +
2-replica background worker + PostgreSQL 16 with Row-Level Security.

## Repo Layout
```
medical-billing-records-assignment-package/
  backend/          Python 3.12, FastAPI, SQLAlchemy async, OpenAI Agents SDK
  frontend/         Next.js 14 App Router, TypeScript, Tailwind CSS
  data/             12 sample PDFs + ground truth JSON (doc_001–doc_012)
  docs/             domain.md, schema.md, design.md
  alembic/          migrations (never edit existing — always create new)
  docker-compose.yml
  .env.example
```

## Run Commands

### Full stack (Docker)
```bash
cp .env.example .env          # fill OPENAI_API_KEY and BETTER_AUTH_SECRET
docker compose up --build
```

### Backend only (local)
```bash
cd backend
uv sync
uv run uvicorn app.api.main:app --reload --port 8000
```

### Worker only (local)
```bash
cd backend
uv run python worker.py
```

### Migrations
```bash
cd backend
uv run alembic upgrade head
# Generate new: uv run alembic revision --autogenerate -m "description"
```

### Tests
```bash
cd backend
uv run pytest tests/ -v
# Unit tests only (no server needed):
uv run pytest tests/test_extraction_models.py -v
```

### Eval extraction accuracy
```bash
cd backend
uv run python scripts/eval_extraction.py
```

### Frontend (local dev)
```bash
cd frontend
npm install
npm run dev    # http://localhost:3000
```

## Key Conventions

### Two DB roles — never mix them
- `billing` (admin/owner): used only for Alembic migrations
- `billing_app` (RLS-subject): used by API and worker at runtime
- `POSTGRES_CONNECTION_STRING` → billing role (migrations only)
- `APP_DB_CONNECTION_STRING` → billing_app role (all runtime access)

### Identity propagation — required before every DML
Every DB session must run before touching user-owned tables:
```sql
SET LOCAL app.current_user_id = '<uuid>'
```
Wired in `ContextManager.session()` via SQLAlchemy event listener on `after_begin`.

### Worker identity
Worker has no HTTP session. After `claim_next_job()`, reads `job.user_id` from claimed
row, calls `SET LOCAL app.current_user_id = job.user_id` before writing result. Code
lives in `backend/app/worker/loop.py`.

### Alembic rule
Never edit existing migrations. Always create new revision for schema changes:
```bash
uv run alembic revision --autogenerate -m "add_content_hash_to_jobs"
```

### AI pipeline pattern (study echo/executor.py first)
```
AgentFactory.build_*() → Agent[RunContext]
ExtractionOrchestrator.run(agent, context) → RunMetrics
PromptLoader.render("template_name", vars) → rendered string
```

### Extraction pipeline (backend/app/ai/agents/extraction/executor.py)
```
pdfplumber → chunk pages (~40k chars / ~10k tokens)
  → gpt-5.4-mini classifies billing-relevant pages
  → gpt-5.4 extracts per chunk in parallel (Semaphore(4))
  → merge results
  → _merge_patient_records() cross-chunk dedup
  → _fix_payments_balance() post-processing
  → over-extraction / periodic billing detection
```

### Job status machine
```
pending → processing → completed
pending → processing → failed
pending → cancelled
```

### API response envelope
All `/jobs` responses are wrapped:
```json
{ "success": true, "message": "...", "data": <payload> }
```
Frontend `apiFetch` auto-unwraps this in `src/lib/api.ts`.

### Smoke tests after changes
```bash
# Health
curl http://localhost:8000/health

# Register
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name":"test","email":"test@test.com","password":"password123"}'

# Login
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"password123"}'
```

## Critical Files to Read Before Editing

| Area | File |
|---|---|
| Extraction agent | `backend/app/ai/agents/extraction/executor.py` |
| Agent pattern reference | `backend/app/ai/agents/echo/executor.py` |
| Job lifecycle | `backend/app/service/job_service.py` |
| Atomic claiming | `backend/app/dao/pg/job_dao.py` |
| Worker loop | `backend/app/worker/loop.py` |
| DB session + identity | `backend/app/core/context_manager.py` |
| Output models | `backend/app/models/extraction.py` |
| API routes | `backend/app/api/routes/jobs.py` |
| Frontend API client | `frontend/src/lib/api.ts` |

## Do Not
- Edit `alembic/versions/0de1443cd0f2_initial.py` or any existing migration
- Connect at runtime using the `billing` (admin) role — use `billing_app` only
- Import LangChain, CrewAI, LlamaIndex, or AutoGen
- Commit `.env` (it contains secrets)
- Add `BYPASSRLS` to the `billing_app` role
