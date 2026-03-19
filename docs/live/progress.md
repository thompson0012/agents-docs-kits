# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The suite now has seven real family routers with nested child placement: `website-building`, `using-legal`, `using-sales`, `using-marketing`, `using-reasoning`, `using-research`, and `using-finance`. `using-agent-practices` now surfaces the web-project and legal families alongside the earlier commercial, research, finance, and reasoning families.

## Latest Completed Work

Scanned the remaining top-level skills and identified three credible grouping moves: formalize `website-building`, create a document-format family (`docx` / `pdf` / `pptx` / `xlsx`), and optionally add a smaller legal family. Implemented the first two low-ambiguity moves needed right now: formalized `website-building/` as a real router with `game`, `webapp`, and `informational` children plus explicit child metadata, eval scaffolding, and a local validator; and created `using-legal/` with nested `contract-review` and `legal-compliance` leaves, explicit DPA-boundary routing logic, eval scaffolding, and a local validator. Updated `using-agent-practices` plus `references/category-map.md` so the new families are discoverable. Removed the obsolete top-level `webapp/`, `contract-review/`, and `legal-compliance/` entrypoints so each concept has one canonical path.

## In Progress

None.

## Blockers

None.

## Next Recommended Action

Run prompt-pressure evaluations against the expanded router suite (`website-building`, `using-legal`, `using-sales`, `using-marketing`, `using-reasoning`, `using-research`, `using-finance`) and then decide whether the deferred document-format family is still worth building as the next router.

## Touched Files

- `templates/base/.agents/skills/website-building/SKILL.md`
- `templates/base/.agents/skills/website-building/references/children.json`
- `templates/base/.agents/skills/website-building/evals/evals.json`
- `templates/base/.agents/skills/website-building/evals/trigger-evals.json`
- `templates/base/.agents/skills/website-building/scripts/validate_router.py`
- `templates/base/.agents/skills/website-building/informational/SKILL.md`
- `templates/base/.agents/skills/website-building/game/SKILL.md`
- `templates/base/.agents/skills/website-building/webapp/SKILL.md`
- `templates/base/.agents/skills/website-building/shared/08-standards.md`
- `templates/base/.agents/skills/website-building/shared/09-technical.md`
- `templates/base/.agents/skills/using-legal/SKILL.md`
- `templates/base/.agents/skills/using-legal/references/children.json`
- `templates/base/.agents/skills/using-legal/evals/evals.json`
- `templates/base/.agents/skills/using-legal/evals/trigger-evals.json`
- `templates/base/.agents/skills/using-legal/scripts/validate_router.py`
- `templates/base/.agents/skills/using-legal/contract-review/SKILL.md`
- `templates/base/.agents/skills/using-legal/legal-compliance/SKILL.md`
- `templates/base/.agents/skills/using-legal/legal-compliance/reference/src.md`
- `templates/base/.agents/skills/using-agent-practices/SKILL.md`
- `templates/base/.agents/skills/using-agent-practices/references/category-map.md`
- `docs/live/current-focus.md`
- `docs/live/progress.md`
- `docs/live/todo.md`

## Verification Status

Read back the new website and legal router packages, the root-router updates, and the nested-path cutover. Ran and observed success for:

- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/website-building --strict`
- `python3 templates/base/.agents/skills/website-building/scripts/validate_router.py templates/base/.agents/skills/website-building --strict`
- `python3 -m py_compile templates/base/.agents/skills/website-building/scripts/validate_router.py`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-legal --strict`
- `python3 templates/base/.agents/skills/using-legal/scripts/validate_router.py templates/base/.agents/skills/using-legal --strict`
- `python3 -m py_compile templates/base/.agents/skills/using-legal/scripts/validate_router.py`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-agent-practices --strict`
- `python3 templates/base/.agents/skills/website-building/scripts/validate_router.py tmp/website-building-invalid --strict` failing on an unknown fallback target
- `python3 templates/base/.agents/skills/using-legal/scripts/validate_router.py tmp/using-legal-invalid --strict` failing on an unknown fallback target
- reviewer pass confirming the `website-building` and `using-legal` rollouts are coherent, discoverable, and free of material issues after the trailing-newline cleanup

## Hand-off Note

The remaining credible router candidate is still the document-format family (`docx`, `pdf`, `pptx`, `xlsx`), but it has a larger internal path-rewrite surface than the two families added here. The suite is now in a good state to pressure-test before making that next move.