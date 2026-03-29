# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The next work item is harness goal-lineage hardening: keep template live docs inert, add a roadmap artifact that preserves source/plan/phase goals, and make phased execution rehydrate from stored truth after compaction instead of drifting from the original objective.

## Latest Completed Work

- captured the user requirement that `template/` must be a true template with no prefilled content
- identified the recurring failure mode where roadmap execution loses the source goal after phase 1 and compaction
- drafted `docs/superpowers/plans/2026-03-27-harness-goal-lineage-hardening.md` to harden template inertness, goal lineage, and resume behavior
- added a new `project-founding` skill family under `templates/base/.agents/skills/` with general and AI/agentic founding leaves plus router metadata and evals
- renamed the top-level template router to `using-labs21-suite`, added explicit child metadata, and cut stale routes to moved non-suite families so the shipped Labs21 suite tells the truth about what it owns

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
- `templates/base/.agents/skills/using-labs21-suite/{SKILL.md,references/children.json,references/category-map.md,evals/*}`
- `templates/base/AGENTS.md`
- `AGENTS.md`
- `README.md`
- `docs/reference/{architecture.md,codemap.md,memory.md}`

## Verification Status

- `python3 templates/base/.agents/skills/create-router-skill/scripts/validate_router.py templates/base/.agents/skills/using-labs21-suite --strict`
- `python3 templates/base/.agents/skills/project-founding/scripts/validate_router.py templates/base/.agents/skills/project-founding --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/project-founding/project-foundation`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/project-founding/ai-agent-foundation`

## Hand-off Note

The next session should implement the harness goal-lineage hardening plan and keep the roadmap as the authoritative source for phased work. The `project-founding` family and the renamed `using-labs21-suite` router are complete unless later prompt-eval tuning exposes routing drift.
