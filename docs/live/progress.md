# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

Task 39 is complete. The repo now has a first-class `software-delivery` harness lane plus an independent `frontend-evaluator` lane, and the base template now ships `docs/live/runtime.md` and `docs/live/qa.md` for baton and evidence handoff. No unresolved validation blocker is currently recorded, so the default next move is back to Task 35.

## Latest Completed Work

Updated the main delivery-control surfaces:
- `templates/base/.agents/skills/software-delivery/{SKILL.md,references/children.json,evals/*}` plus new `harness-design/` and `frontend-evaluator/` leaves
- `templates/base/.agents/skills/website-building/{SKILL.md,references/children.json,shared/12-playwright-interactive.md}` so builder QA stays separate from independent evaluator signoff
- `templates/base/.agents/skills/using-agent-practices/{SKILL.md,references/category-map.md,evals/*}` and `templates/base/AGENTS.md` so harness-control and strict frontend-acceptance requests discover `software-delivery` honestly
- `templates/base/docs/live/{runtime.md,qa.md}` and `templates/base/docs/reference/{architecture.md,codemap.md}` so multi-session baton state and evaluator evidence have durable template homes

## In Progress

None.

## Blockers

None recorded.

## Next Recommended Action

Resume Task 35: refine the capability-based methodology overlays in the finance, research, and webapp docs. Only detour if a concrete validator failure or regression from Task 39 is observed.

## Touched Files

- `templates/base/.agents/skills/software-delivery/`
- `templates/base/.agents/skills/website-building/`
- `templates/base/.agents/skills/using-agent-practices/`
- `templates/base/AGENTS.md`
- `templates/base/docs/live/{runtime.md,qa.md}`
- `templates/base/docs/reference/{architecture.md,codemap.md}`

## Verification Status

This continuity pass did not re-run validators. If verification details are needed, read the Task 39 implementation handoff and the touched template surfaces above.

## Hand-off Note

Task 39 closed the harness-control, frontend-evaluator, and live-doc additions. Use `software-delivery/harness-design` for cross-session orchestration, `software-delivery/frontend-evaluator` for independent browser signoff, and `website-building` for builder-side implementation plus QA. Unless a concrete blocker appears, resume from Task 35.