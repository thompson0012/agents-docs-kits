# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

Task 39 remains complete, the base template's design family now uses an honest nested router layout under `using-design`, and both the repo guide and the template guide now include a mandatory reference-writeback gate. Future meaningful changes must explicitly triage whether `docs/reference/*` needs updates instead of waiting for user prompting. No unresolved validation blocker is currently recorded, so the default next move still returns to Task 35 once this guide change is noted.

## Latest Completed Work

Completed the bundled design-family cutover and tightened the writeback mechanism:
- moved `design-foundations`, `generating-design-tokens`, `generative-ui`, and `liquid-glass-design` into `templates/base/.agents/skills/using-design/` as nested leaf skills
- updated `templates/base/.agents/skills/using-design/{SKILL.md,references/children.json,evals/*}` and dependent references so direct and ambiguous routes use `using-design/<leaf>` consistently
- added a `Reference Writeback Gate` to both `AGENTS.md` and `templates/base/AGENTS.md` so agents must explicitly decide whether `docs/reference/{memory.md,lessons.md,architecture.md,codemap.md}` need updates after meaningful work
- preserved the new policy in `docs/reference/memory.md` and kept router-validator abstraction unchanged to avoid unrelated repo-wide churn

## In Progress

None.

## Blockers

None recorded.

## Next Recommended Action

Resume Task 35: refine the capability-based methodology overlays in the finance, research, and webapp docs. Treat the nested `using-design/<leaf>` layout and the new reference-writeback gate as landed unless a concrete regression appears.

## Touched Files

- `AGENTS.md`
- `templates/base/AGENTS.md`
- `templates/base/.agents/skills/using-design/`
- `templates/base/.agents/skills/using-agent-practices/`
- `templates/base/.agents/skills/using-documents/`
- `templates/base/.agents/skills/software-delivery/plan-design-review/`
- `templates/base/.agents/skills/visualization/`
- `templates/base/.agents/skills/website-building/`
- `docs/reference/{memory.md,lessons.md}`
- `templates/base/docs/live/{runtime.md,qa.md}`
- `templates/base/docs/reference/{architecture.md,codemap.md}`

## Verification Status

Validated `templates/base/.agents/skills/using-design/` with `python3 templates/base/.agents/skills/using-design/scripts/validate_router.py --strict templates/base/.agents/skills/using-design`, JSON-parsed the updated router/eval metadata, grep-checked that stale top-level design-leaf route/path references were removed from edited skill surfaces, and manually reviewed the new `Reference Writeback Gate` text in both agent guides.

## Hand-off Note

`using-design` is now both the family router and the physical package boundary for the bundled design leaves, and the repo now has an explicit guide-level gate requiring `docs/reference/*` writeback triage after meaningful work. Keep direct leaf routing on the nested `using-design/<leaf>` identifiers, keep normal site/app/game builds under `website-building`, and expect future sessions to justify or perform reference-doc updates explicitly. Unless a concrete regression appears, resume from Task 35.