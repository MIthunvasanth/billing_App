# Medical Billing Extraction Platform

Full-stack AI platform: upload medical PDFs → extract structured `BillingRecord` data
using OpenAI Agents SDK. Per-user isolation enforced by PostgreSQL Row-Level Security.

## Prerequisites

- Docker Desktop (with Compose v2)
- OpenAI API key (`sk-...`)

## Quick Start

```bash
git clone <repo>
cd medical-billing-records-assignment-package

cp .env.example .env
```

Open `.env` and set the two required values:

```env
OPENAI_API_KEY=sk-...
BETTER_AUTH_SECRET=<any 32+ char random string, e.g. openssl rand -hex 32>
```

Then start the full stack:

```bash
docker compose up --build
```

Services:
| Service | URL | Notes |
|---|---|---|
| Frontend (Next.js) | http://localhost:3000 | Sign up / sign in / upload |
| API (FastAPI) | http://localhost:8000 | REST API + Swagger at `/docs` |
| Worker | — | 2 replicas, polls for jobs |
| Postgres | localhost:5432 | Migrations run automatically on API start |

## End-to-End Flow

1. Open http://localhost:3000/auth/signup
2. Create an account (email + password)
3. You land on the dashboard — click **Choose File**, select any PDF from `data/`
4. Click **Upload** — a new job appears with `status: pending`
5. The worker claims it within a few seconds → `status: processing`
6. Extraction completes (typically 30–120s) → `status: completed`
7. Click the job row to see the full result:
   - `BillingRecord` table with CPT codes, charges, insurance payments, balance
   - `FlaggedRecord` list with severity highlights (yellow/orange/red)

## Smoke Tests

```bash
# 1. Health check (DB connectivity)
curl -s http://localhost:8000/health | python -m json.tool
# Expected: {"status": "ok", "db": "ok"}

# 2. Swagger UI
open http://localhost:8000/docs

# 3. Worker logs
docker compose logs worker --tail 30

# 4. Isolation check
# Sign in as user A, grab a job_id, then sign in as user B and try to fetch it.
# Must return 404 — existence must not leak across user boundaries.
```

## Tear Down

```bash
docker compose down -v
```

`-v` removes the Postgres volume for a clean slate.

## Local Development (no Docker)

### Backend

```bash
cd backend
uv sync
cp ../.env.example ../.env   # edit as above
uv run uvicorn app.api.main:app --reload --port 8000
# In a second terminal:
uv run python worker.py
```

### Frontend

```bash
cd frontend
npm install
# frontend/.env.local already points to http://localhost:8000
npm run dev    # http://localhost:3000
```

### Migrations

```bash
cd backend
uv run alembic upgrade head
# New migration after schema change:
uv run alembic revision --autogenerate -m "description"
```

### Tests

```bash
cd backend
uv run pytest tests/ -v
# Unit tests only (no server needed):
uv run pytest tests/test_extraction_models.py -v
# E2E tests (requires running API):
uv run pytest tests/test_job_lifecycle.py -v
```

## Environment Variables

| Variable | Required | Purpose |
|---|---|---|
| `OPENAI_API_KEY` | **Yes** | Extraction agents |
| `BETTER_AUTH_SECRET` | **Yes** | JWT signing secret (32+ chars) |
| `POSTGRES_CONNECTION_STRING` | Yes | Admin/migration role (`billing`) |
| `APP_DB_CONNECTION_STRING` | Yes | App role (`billing_app`, RLS-enforced) |
| `PDF_MOUNT_PATH` | Yes | Shared upload directory (`/app/pdfs`) |
| `WORKER_POLL_INTERVAL_SECONDS` | Yes | Worker polling cadence (default 5) |
| `NEXT_PUBLIC_API_BASE_URL` | Frontend | Backend URL for browser API calls |

See `.env.example` for all defaults.

## Project Structure

```
backend/
  app/
    api/          FastAPI app, routes (/jobs, /auth, /health), dependencies
    ai/           OpenAI Agents SDK pipeline (extraction agent, orchestrator)
    dao/          SQLAlchemy models + DAOs (job_dao.py — atomic claiming)
    service/      Business logic (job_service.py, extraction_service.py)
    worker/       Polling loop (loop.py)
    models/       Pydantic output types (extraction.py)
    core/         DB lifecycle, context manager, identity propagation
  alembic/        Schema migrations (never edit existing ones)
  tests/          pytest — unit + E2E lifecycle tests

frontend/
  src/
    app/          Next.js App Router pages (auth, dashboard, jobs/[id])
    lib/          api.ts (fetch + SuccessResponse unwrap), auth.ts (token store)

data/             12 sample PDFs + ground truth JSON (doc_001–doc_012)
docs/             domain.md, schema.md, design.md
```

## Architecture Notes

- **RLS enforcement**: `billing_app` role is subject to RLS; app never connects as owner.
  Every transaction runs `SET LOCAL app.current_user_id = '<uuid>'` before any DML.
- **Atomic job claiming**: `SELECT ... FOR UPDATE SKIP LOCKED` — two workers cannot claim
  the same job.
- **Worker identity**: worker reads `job.user_id` from the claimed row and sets
  `SET LOCAL` before writing results — no HTTP session required.
- **Content caching**: SHA-256 of PDF bytes stored on job row; duplicate upload by same
  user returns cached result without re-running extraction.

For the full specification see [ASSIGNMENT.md](ASSIGNMENT.md).
For design decisions and accuracy analysis see [docs/design.md](docs/design.md).
