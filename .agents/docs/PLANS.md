# PLANS.md — Durable Plan & Task Records

> **STATUS**: TEMPLATE
> **OWNER**: Human (final authority) / AI (maintenance)
> **LAST REVIEWED**: 2026-02-12

**Purpose**: Provide a lightweight, version-controlled way to keep **approved plans**, their **task breakdowns**, and key outputs **traceable across sessions**.

*Note: This is a supporting guide. Canonical rules reside in `AGENTS.md`.*

## Recommended Structure

Use a dated folder per plan:

- `/.agents/docs/plans/YYYY-MM-DD_short-title/`
- `plan.md` — the approved plan (use the Plan Template in `/.agents/docs/GUIDELINES.md`)
  - `tasks.md` — atomic task checklist for the plan
  - `decisions.md` (optional) — decisions + rationale + links
  - `outputs/` (optional) — screenshots, logs, diagrams, exported reports

Example:
- `/.agents/docs/plans/2026-02-09_traceable-plan-records/plan.md`
- `/.agents/docs/plans/2026-02-09_traceable-plan-records/tasks.md`

## How It Connects to Existing Docs

- `PROGRESS.md` remains the **session timeline** and can link to the active plan folder.
- `TASKS.md` can remain a **session scratchpad**, but when a plan folder exists, prefer linking to the plan’s `tasks.md` to avoid duplication.
- `LESSONS.md` remains the place to record “what we learned” and process improvements.

## Minimal Templates

### plan.md (reference)

Use the “Plan Template (RECOMMENDED)” from `/.agents/docs/GUIDELINES.md`.

### tasks.md (recommended)

```text
# Tasks — <short title>

Plan: ../<same-folder>/plan.md

## Status
- Last updated: YYYY-MM-DD
- Owner: <optional>

## Tasks (atomic)
- [ ] Task 1 — success criteria: ...
- [ ] Task 2 — success criteria: ...
```

## Conventions (Recommended)

- Keep plan folders small and scoped to one approved goal.
- Prefer links over duplicated text (one source of truth).
- If the plan changes materially, add a short “Plan change note” section in `plan.md` with date + reason.
