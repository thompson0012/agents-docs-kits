# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The suite now has eight real family routers with nested child placement: `website-building`, `using-documents`, `using-legal`, `using-sales`, `using-marketing`, `using-reasoning`, `using-research`, and `using-finance`. `using-agent-practices` now surfaces the document family alongside the web, legal, commercial, research, finance, and reasoning families.

## Latest Completed Work

Implemented the deferred document-format family as `using-documents/` and moved `docx`, `pdf`, `pptx`, and `xlsx` under that router package as canonical nested children. Added `references/children.json`, eval scaffolding, and a local `validate_router.py`, then updated the moved skill docs so script-path examples now point at `skills/using-documents/...`. Updated `using-agent-practices` plus `references/category-map.md` so document-format requests route through the new family router instead of treating the four formats as unrelated top-level entrypoints.

## In Progress

None.

## Blockers

None.

## Next Recommended Action

Run prompt-pressure evaluations against the expanded router suite (`website-building`, `using-documents`, `using-legal`, `using-sales`, `using-marketing`, `using-reasoning`, `using-research`, `using-finance`) and then decide whether any additional router families are still justified.

## Touched Files

- `templates/base/.agents/skills/using-documents/SKILL.md`
- `templates/base/.agents/skills/using-documents/references/children.json`
- `templates/base/.agents/skills/using-documents/evals/evals.json`
- `templates/base/.agents/skills/using-documents/evals/trigger-evals.json`
- `templates/base/.agents/skills/using-documents/scripts/validate_router.py`
- `templates/base/.agents/skills/using-documents/docx/SKILL.md`
- `templates/base/.agents/skills/using-documents/docx/CREATION.md`
- `templates/base/.agents/skills/using-documents/docx/EDITING.md`
- `templates/base/.agents/skills/using-documents/docx/scripts/accept_changes.py`
- `templates/base/.agents/skills/using-documents/docx/scripts/comment.py`
- `templates/base/.agents/skills/using-documents/docx/scripts/pack.py`
- `templates/base/.agents/skills/using-documents/docx/scripts/unpack.py`
- `templates/base/.agents/skills/using-documents/pdf/SKILL.md`
- `templates/base/.agents/skills/using-documents/pdf/form-filling.md`
- `templates/base/.agents/skills/using-documents/pdf/formfill.py`
- `templates/base/.agents/skills/using-documents/pdf/layout.py`
- `templates/base/.agents/skills/using-documents/pdf/render.py`
- `templates/base/.agents/skills/using-documents/pdf/libraries/cli-tools.md`
- `templates/base/.agents/skills/using-documents/pdf/libraries/pdfplumber.md`
- `templates/base/.agents/skills/using-documents/pdf/libraries/pypdfium2.md`
- `templates/base/.agents/skills/using-documents/pdf/libraries/reportlab.md`
- `templates/base/.agents/skills/using-documents/pptx/SKILL.md`
- `templates/base/.agents/skills/using-documents/pptx/CREATING.md`
- `templates/base/.agents/skills/using-documents/pptx/EDITING.md`
- `templates/base/.agents/skills/using-documents/pptx/scripts/pack.py`
- `templates/base/.agents/skills/using-documents/pptx/scripts/repair.py`
- `templates/base/.agents/skills/using-documents/pptx/scripts/slides.py`
- `templates/base/.agents/skills/using-documents/pptx/scripts/unpack.py`
- `templates/base/.agents/skills/using-documents/xlsx/SKILL.md`
- `templates/base/.agents/skills/using-documents/xlsx/scripts/_soffice.py`
- `templates/base/.agents/skills/using-documents/xlsx/scripts/pivot_table.py`
- `templates/base/.agents/skills/using-documents/xlsx/scripts/recalc.py`
- `templates/base/.agents/skills/using-agent-practices/SKILL.md`
- `templates/base/.agents/skills/using-agent-practices/references/category-map.md`
- `docs/live/current-focus.md`
- `docs/live/progress.md`
- `docs/live/todo.md`

## Verification Status

Read back the new `using-documents` router package, the moved child skills, and the root-router updates. Ran and observed success for:

- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-documents --strict`
- `python3 templates/base/.agents/skills/using-documents/scripts/validate_router.py templates/base/.agents/skills/using-documents --strict`
- `python3 -m py_compile templates/base/.agents/skills/using-documents/scripts/validate_router.py`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-agent-practices --strict`
- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-agent-practices --strict` after the final category-map spacing cleanup
- reviewer re-check confirming no material issues remain in the final `using-documents` rollout or its root-router integration
- `python3 templates/base/.agents/skills/using-documents/scripts/validate_router.py tmp/using-documents-invalid --strict` failing on an unknown fallback target
- reviewer pass confirming the `using-documents` rollout is coherent, the moved child references are aligned, and the root router/category map expose the family honestly after the trailing-newline cleanup

## Hand-off Note

The document-format family is now a real router rather than a deferred idea. The next decision should be evidence-driven across the whole suite: pressure-test the expanded router set before creating any more families.