# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The suite now treats Sales, Marketing, Reasoning, Research, and Finance as real family routers with nested leaf placement. Their child skills live under the router packages, and `using-agent-practices` delegates ambiguous requests into those family entrypoints instead of forcing premature leaf selection.

## Latest Completed Work

Moved the remaining reasoning, research, and finance leaves under their family routers: `using-reasoning/`, `using-research/`, and `using-finance/`. Added `references/children.json`, eval prompts, and local `validate_router.py` scripts where those router packages needed them. Updated `using-agent-practices` plus `references/category-map.md` so ambiguous research and finance requests now route through family routers and reasoning entries now point at nested child paths. Generalized `create-router-skill` so its examples and templates are router-generic rather than bound to reasoning-specific content, and kept `create-skill` aligned with the nested-router convention.

## In Progress

None.

## Blockers

None.

## Next Recommended Action

Run prompt-pressure evaluations against the nested router families (`using-sales`, `using-marketing`, `using-reasoning`, `using-research`, and `using-finance`) and then decide which remaining top-level areas truly deserve routers rather than staying as standalone leaves.

## Touched Files

- `templates/base/.agents/skills/using-reasoning/SKILL.md`
- `templates/base/.agents/skills/using-reasoning/references/children.json`
- `templates/base/.agents/skills/using-reasoning/evals/evals.json`
- `templates/base/.agents/skills/using-reasoning/evals/trigger-evals.json`
- `templates/base/.agents/skills/using-reasoning/scripts/validate_router.py`
- `templates/base/.agents/skills/using-reasoning/thinking-ground/SKILL.md`
- `templates/base/.agents/skills/using-reasoning/thinking-ground/assets/system-pocket-card.md`
- `templates/base/.agents/skills/using-reasoning/problem-definition/SKILL.md`
- `templates/base/.agents/skills/using-reasoning/dynamic-problem-solving/SKILL.md`
- `templates/base/.agents/skills/using-reasoning/dynamic-problem-solving/assets/quick-invoke-template.md`
- `templates/base/.agents/skills/using-reasoning/dynamic-problem-solving/references/lens-library.md`
- `templates/base/.agents/skills/using-reasoning/dynamic-problem-solving/references/bias-inventory.md`
- `templates/base/.agents/skills/using-reasoning/domain-expert-consultation/SKILL.md`
- `templates/base/.agents/skills/using-reasoning/strategic-foresight/SKILL.md`
- `templates/base/.agents/skills/using-research/SKILL.md`
- `templates/base/.agents/skills/using-research/references/children.json`
- `templates/base/.agents/skills/using-research/evals/evals.json`
- `templates/base/.agents/skills/using-research/evals/trigger-evals.json`
- `templates/base/.agents/skills/using-research/scripts/validate_router.py`
- `templates/base/.agents/skills/using-research/research-assistant/SKILL.md`
- `templates/base/.agents/skills/using-research/market-research/SKILL.md`
- `templates/base/.agents/skills/using-research/investment-research/SKILL.md`
- `templates/base/.agents/skills/using-research/investment-research/investor-profiles.md`
- `templates/base/.agents/skills/using-finance/SKILL.md`
- `templates/base/.agents/skills/using-finance/references/children.json`
- `templates/base/.agents/skills/using-finance/evals/evals.json`
- `templates/base/.agents/skills/using-finance/evals/trigger-evals.json`
- `templates/base/.agents/skills/using-finance/scripts/validate_router.py`
- `templates/base/.agents/skills/using-finance/finance-audit-support/SKILL.md`
- `templates/base/.agents/skills/using-finance/finance-audit-support/reference/src.md`
- `templates/base/.agents/skills/using-finance/finance-markets/SKILL.md`
- `templates/base/.agents/skills/using-finance/finance-markets/analysis.md`
- `templates/base/.agents/skills/using-finance/finance-markets/market-data.md`
- `templates/base/.agents/skills/using-finance/finance-markets/reporting.md`
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

Read back the nested reasoning, research, and finance routers, root-router updates, and generalized router-authoring guidance. Ran and observed success for:

- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-reasoning --strict`
- `python3 templates/base/.agents/skills/using-reasoning/scripts/validate_router.py templates/base/.agents/skills/using-reasoning --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-research --strict`
- `python3 templates/base/.agents/skills/using-research/scripts/validate_router.py templates/base/.agents/skills/using-research --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-finance --strict`
- `python3 templates/base/.agents/skills/using-finance/scripts/validate_router.py templates/base/.agents/skills/using-finance --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-agent-practices --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/create-router-skill --strict`
- `python3 -m py_compile templates/base/.agents/skills/using-reasoning/scripts/validate_router.py`
- `python3 -m py_compile templates/base/.agents/skills/using-research/scripts/validate_router.py`
- `python3 -m py_compile templates/base/.agents/skills/using-finance/scripts/validate_router.py`
- `python3 templates/base/.agents/skills/using-reasoning/scripts/validate_router.py tmp/using-reasoning-invalid --strict` failing on an unknown fallback target
- `python3 templates/base/.agents/skills/using-research/scripts/validate_router.py tmp/using-research-invalid --strict` failing on an unknown fallback target
- `python3 templates/base/.agents/skills/using-finance/scripts/validate_router.py tmp/using-finance-invalid --strict` failing on an unknown fallback target
- reviewer re-check on the final remaining-router rollout confirming the nested router conventions, generic templates, and cross-family references are aligned and no material issues remain

## Hand-off Note

The nested-router convention is now applied across the main multi-leaf families, and the router-authoring package is generic enough to create future routers without smuggling in a specific family model. The next decision should be evidence-driven: run prompt-pressure evals before creating any more routers.