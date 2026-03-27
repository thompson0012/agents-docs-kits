# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The template skill surface now has a complete top-level discoverability pass: `using-agent-practices` and its category map cover every live top-level skill, including standalone specialist leaves that were previously omitted. No package moves or new router families were needed, so the default next move still returns to Task 35 unless a concrete routing regression appears.

## Latest Completed Work

- completed a full scan of `templates/base/.agents/skills/` and found six live top-level skills missing from the canonical top-level router surface: `create-skill`, `create-router-skill`, `cx-ticket-triage`, `data-exploration`, `visualization`, and `media`
- updated `templates/base/.agents/skills/using-agent-practices/{SKILL.md,references/category-map.md,evals/*}` so those skills are first-class direct routes with explicit boundary language against nearby skills
- updated `templates/base/docs/reference/{codemap.md,memory.md}` to preserve the top-level discoverability rule and the category-map role
- reviewed reference writeback: no `templates/base/docs/reference/{architecture.md,lessons.md}` update was needed because the change tightened top-level discoverability rules without moving package boundaries or adding a new failure-pattern worth preserving

## In Progress

None.

## Blockers

None.

## Next Recommended Action

- Next step: Resume Task 35: refine the capability-based methodology overlays in the finance, research, and webapp docs. Treat the top-level skill audit as landed unless a concrete discoverability regression appears.

## Touched Files

- `templates/base/.agents/skills/using-agent-practices/`
- `templates/base/docs/reference/{codemap.md,memory.md}`
- `templates/base/docs/live/progress.md`

## Verification Status

- Check: `python3 templates/base/.agents/skills/create-skill/scripts/validate.py --strict templates/base/.agents/skills/using-agent-practices`
- Result: passed
- Check: targeted Python assertions for top-level skill coverage, router outputs, category-map inventory completeness, and eval IDs
- Result: passed

## Hand-off Note

- Resume from: `templates/base/.agents/skills/using-agent-practices/` if any top-level routing ambiguity resurfaces; otherwise return to Task 35 work.
- Watch for: future standalone skills added under `templates/base/.agents/skills/` without matching updates to `using-agent-practices/SKILL.md`, `references/category-map.md`, and trigger/task eval coverage.
