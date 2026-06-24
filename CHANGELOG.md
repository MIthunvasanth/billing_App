# Changelog

Newest entries at top. Updated every session per CLAUDE.md requirement.

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
