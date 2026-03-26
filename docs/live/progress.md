# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The user-directed skill audit is now landed: the template's top-level skill router and category inventory cover every live top-level skill under `templates/base/.agents/skills/`, including standalone specialist leaves that were previously undiscoverable from the canonical top-level surface. No router family move or package-layout cutover was needed, and no validation blocker is open, so the default next move still returns to Task 35.

## Latest Completed Work

- completed a full scan of `templates/base/.agents/skills/` and found six live top-level skills missing from `using-agent-practices` discoverability: `create-skill`, `create-router-skill`, `cx-ticket-triage`, `data-exploration`, `visualization`, and `media`
- updated `templates/base/.agents/skills/using-agent-practices/{SKILL.md,references/category-map.md,evals/*}` so those skills are explicit direct routes with near-miss coverage against `coding-and-data`, `using-design/design-foundations`, and `using-documents`
- updated `templates/base/docs/reference/{codemap.md,memory.md}` and `templates/base/docs/live/progress.md` to preserve the top-level discoverability rule and continuity state
- reviewed reference writeback: no `docs/reference/{architecture,codemap,memory,lessons}.md` update was needed at the repo root because the durable routing rule is template-local rather than repo-wide

## In Progress

None.

## Blockers

None recorded.

## Next Recommended Action

Resume Task 35: refine the capability-based methodology overlays in the finance, research, and webapp docs. Treat the top-level skill audit as landed unless a concrete discoverability regression appears.

## Touched Files

- `templates/base/.agents/skills/using-agent-practices/`
- `templates/base/docs/reference/{codemap.md,memory.md}`
- `templates/base/docs/live/progress.md`
- `docs/live/progress.md`

## Verification Status

- Check: `python3 templates/base/.agents/skills/create-skill/scripts/validate.py --strict templates/base/.agents/skills/using-agent-practices`
- Result: passed
- Check: targeted Python assertions for top-level skill coverage, router outputs, category-map inventory completeness, and eval IDs
- Result: passed

## Hand-off Note

`using-agent-practices` is now the honest top-level inventory for both family routers and standalone specialist skills. If a new top-level skill lands later, update the router body, category map, and trigger/task evals together; otherwise resume from Task 35.