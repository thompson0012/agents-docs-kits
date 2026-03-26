# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

User-directed reasoning-family work is now landed: `using-reasoning` has a nested `reality-check` leaf for hidden-rule and survivability analysis, with router metadata and discoverability updated. Task 39 remains complete and no validation blocker is open, so the default next move still returns to Task 35.

## Latest Completed Work

- added `templates/base/.agents/skills/using-reasoning/reality-check/SKILL.md` with evidence guardrails (`Observed pattern` / `Supported hypothesis` / `Uncertain`) and a blunt but non-theatrical output contract
- updated `templates/base/.agents/skills/using-reasoning/{SKILL.md,references/children.json,evals/*}` so `reality-check` routes after `strategic-foresight` and before generic advisory and lens-analysis leaves
- updated `templates/base/.agents/skills/using-agent-practices/references/category-map.md` and `templates/base/docs/reference/codemap.md` for reasoning-family discoverability
- reviewed reference writeback: no `docs/reference/{architecture,memory,lessons}.md` update was needed because this change adds a leaf inside an existing family without changing repo-wide ownership, policy, or invariants

## In Progress

None.

## Blockers

None recorded.

## Next Recommended Action

Resume Task 35: refine the capability-based methodology overlays in the finance, research, and webapp docs. Treat `using-reasoning/reality-check` as landed unless a concrete regression appears.

## Touched Files

- `templates/base/.agents/skills/using-reasoning/`
- `templates/base/.agents/skills/using-agent-practices/references/category-map.md`
- `templates/base/docs/reference/codemap.md`
- `docs/live/progress.md`

## Verification Status

- Check: `python3 templates/base/.agents/skills/using-reasoning/scripts/validate_router.py --strict templates/base/.agents/skills/using-reasoning`
- Result: passed
- Check: `python3 templates/base/.agents/skills/create-skill/scripts/validate.py --strict templates/base/.agents/skills/using-reasoning/reality-check`
- Result: passed
- Check: targeted Python assertions for child order, evidence labels, and eval coverage
- Result: passed

## Hand-off Note

`using-reasoning/reality-check` now owns blunt hidden-rule and survivability requests; `startup-pressure-test` still owns startup viability math, and research skills still own source-heavy evidence gathering. Unless a concrete blocker appears, resume from Task 35.