# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

`create-router-skill` is now being exercised on a real family: `templates/base/.agents/skills/using-sales/` exists as the first concrete family router, and `using-agent-practices` now delegates ambiguous sales requests into it.

## Latest Completed Work

Created `using-sales/` with a router-focused `SKILL.md`, `references/children.json`, eval prompts, and a local `scripts/validate_router.py`. The router selects among `account-research`, `sales-call-prep`, and `sales-draft-outreach` using a concrete priority order. Updated `using-agent-practices/SKILL.md` plus `references/category-map.md` so the suite router now sends ambiguous sales requests to `using-sales` rather than forcing a premature leaf choice.

## In Progress

None.

## Blockers

None.

## Next Recommended Action

Run prompt-pressure evaluations against `using-sales`, then decide whether the next pilot should be `using-marketing` or whether the sales pilot exposed model changes that should be folded back into `create-router-skill` first.

## Touched Files

- `templates/base/.agents/skills/using-sales/SKILL.md`
- `templates/base/.agents/skills/using-sales/references/children.json`
- `templates/base/.agents/skills/using-sales/evals/evals.json`
- `templates/base/.agents/skills/using-sales/evals/trigger-evals.json`
- `templates/base/.agents/skills/using-sales/scripts/validate_router.py`
- `templates/base/.agents/skills/using-agent-practices/SKILL.md`
- `templates/base/.agents/skills/using-agent-practices/references/category-map.md`
- `docs/live/current-focus.md`
- `docs/live/progress.md`
- `docs/live/todo.md`

## Verification Status

Read back the new sales router and root-routing changes. Ran and observed success for:

- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-sales --strict`
- `python3 templates/base/.agents/skills/using-sales/scripts/validate_router.py templates/base/.agents/skills/using-sales --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-agent-practices --strict`
- `python3 -m py_compile templates/base/.agents/skills/using-sales/scripts/validate_router.py`
- `python3 templates/base/.agents/skills/using-sales/scripts/validate_router.py tmp/using-sales-invalid --strict` failing on an unknown fallback target
- reviewer pass on `using-sales` and root-router integration; fixed one contract inconsistency in `using-agent-practices` and revalidated

## Hand-off Note

The first real router pilot is in place. `using-sales` demonstrates that the router-package model can mediate between research, meeting prep, and outreach without flattening the leaf skills. The next useful decision is whether this pattern transfers cleanly to `using-marketing` or whether the sales pilot surfaced enough edge cases to refine the generic router-authoring package first.