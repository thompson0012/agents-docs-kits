# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The suite now has two real family routers using nested leaf placement: `using-sales/` and `using-marketing/`. Their child skills live inside the router packages, and `using-agent-practices` delegates ambiguous sales and marketing requests into those family entrypoints.

## Latest Completed Work

Moved the sales leaves under `using-sales/` (`account-research`, `sales-call-prep`, `sales-draft-outreach`), updated the sales router to use nested child paths, and added `using-marketing/` with nested `marketing-performance-analytics`, `marketing-competitive-analysis`, and `content-creation` leaves. Updated `using-agent-practices` plus `references/category-map.md` to route both sales and marketing ambiguity through family routers. Updated `create-router-skill` and `create-skill` guidance so nested router families are now the documented convention rather than an optional variant.

## In Progress

None.

## Blockers

None.

## Next Recommended Action

Run prompt-pressure evaluations against both `using-sales` and `using-marketing`, then decide whether the nested-family convention is mature enough to roll into the next router candidate or whether the generic router-authoring package still needs one more refinement pass.

## Touched Files

- `templates/base/.agents/skills/using-sales/SKILL.md`
- `templates/base/.agents/skills/using-sales/references/children.json`
- `templates/base/.agents/skills/using-sales/evals/evals.json`
- `templates/base/.agents/skills/using-sales/evals/trigger-evals.json`
- `templates/base/.agents/skills/using-sales/scripts/validate_router.py`
- `templates/base/.agents/skills/using-sales/account-research/SKILL.md`
- `templates/base/.agents/skills/using-sales/sales-call-prep/SKILL.md`
- `templates/base/.agents/skills/using-sales/sales-call-prep/reference/src.md`
- `templates/base/.agents/skills/using-sales/sales-draft-outreach/SKILL.md`
- `templates/base/.agents/skills/using-sales/sales-draft-outreach/reference/src.md`
- `templates/base/.agents/skills/using-marketing/SKILL.md`
- `templates/base/.agents/skills/using-marketing/references/children.json`
- `templates/base/.agents/skills/using-marketing/evals/evals.json`
- `templates/base/.agents/skills/using-marketing/evals/trigger-evals.json`
- `templates/base/.agents/skills/using-marketing/scripts/validate_router.py`
- `templates/base/.agents/skills/using-marketing/marketing-performance-analytics/SKILL.md`
- `templates/base/.agents/skills/using-marketing/marketing-performance-analytics/reference/src.md`
- `templates/base/.agents/skills/using-marketing/marketing-competitive-analysis/SKILL.md`
- `templates/base/.agents/skills/using-marketing/marketing-competitive-analysis/reference/src.md`
- `templates/base/.agents/skills/using-marketing/content-creation/SKILL.md`
- `templates/base/.agents/skills/using-agent-practices/SKILL.md`
- `templates/base/.agents/skills/using-agent-practices/references/category-map.md`
- `templates/base/.agents/skills/create-router-skill/SKILL.md`
- `templates/base/.agents/skills/create-router-skill/assets/router-skill-template.md`
- `templates/base/.agents/skills/create-router-skill/assets/children-template.json`
- `templates/base/.agents/skills/create-router-skill/references/router-metadata.md`
- `templates/base/.agents/skills/create-skill/SKILL.md`
- `docs/live/current-focus.md`
- `docs/live/progress.md`
- `docs/live/todo.md`

## Verification Status

Read back the nested sales and marketing routers, root-router updates, and router-authoring guidance. Ran and observed success for:

- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-sales --strict`
- `python3 templates/base/.agents/skills/using-sales/scripts/validate_router.py templates/base/.agents/skills/using-sales --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-marketing --strict`
- `python3 templates/base/.agents/skills/using-marketing/scripts/validate_router.py templates/base/.agents/skills/using-marketing --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-agent-practices --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/create-router-skill --strict`
- `python3 -m py_compile templates/base/.agents/skills/using-sales/scripts/validate_router.py`
- `python3 -m py_compile templates/base/.agents/skills/using-marketing/scripts/validate_router.py`
- `python3 templates/base/.agents/skills/using-marketing/scripts/validate_router.py tmp/using-marketing-invalid --strict` failing on an unknown fallback target
- reviewer re-check on the final nested-router rollout confirming the sales/marketing conventions, templates, and root routing are aligned and no material issues remain

## Hand-off Note

The suite now treats family routers as the canonical discoverable entrypoints for the Sales and Marketing families, with their leaf skills nested underneath. The next high-value question is whether to repeat this pattern for the next router candidate immediately or first pressure-test the nested convention under more realistic routing prompts.