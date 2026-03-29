# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The next work item is harness goal-lineage hardening: keep template live docs inert, add a roadmap artifact that preserves source/plan/phase goals, and make phased execution rehydrate from stored truth after compaction instead of drifting from the original objective.

## Latest Completed Work

- captured the user requirement that `template/` must be a true template with no prefilled content
- identified the recurring failure mode where roadmap execution loses the source goal after phase 1 and compaction
- drafted `docs/superpowers/plans/2026-03-27-harness-goal-lineage-hardening.md` to harden template inertness, goal lineage, and resume behavior
- added a new `project-founding` skill family under `templates/base/.agents/skills/` with general and AI/agentic founding leaves plus router metadata and evals
- updated `using-agent-practices` discovery routes and category map so staged project blueprinting routes to `project-founding` instead of falling through to generic reasoning

## In Progress

Harness goal-lineage hardening plan drafted; implementation pending.
- goal-lineage hardening remains the main pending implementation track; the new `project-founding` skill family is complete and validated

## Blockers

None recorded.

## Next Recommended Action

Review and execute `docs/superpowers/plans/2026-03-27-harness-goal-lineage-hardening.md`.

## Touched Files

- `docs/superpowers/plans/2026-03-27-harness-goal-lineage-hardening.md`
- `docs/live/current-focus.md`
- `docs/live/progress.md`
- `templates/base/.agents/skills/project-founding/`
- `templates/base/.agents/skills/using-agent-practices/SKILL.md`
- `templates/base/.agents/skills/using-agent-practices/references/category-map.md`
- `docs/reference/architecture.md`
- `docs/reference/codemap.md`
- `docs/reference/memory.md`

## Verification Status

- Not run yet for this plan.
- `python3 templates/base/.agents/skills/project-founding/scripts/validate_router.py templates/base/.agents/skills/project-founding --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/project-founding/project-foundation`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/project-founding/ai-agent-foundation`

## Hand-off Note

The next session should implement the harness goal-lineage hardening plan and keep the roadmap as the authoritative source for phased work. The `project-founding` skill family work is complete unless prompt-eval tuning exposes routing drift.
