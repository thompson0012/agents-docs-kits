# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

Replace the legacy `create-skill` guidance with a production-ready, universal `skills-creator` package that matches the provided structure, scripts, and references for scaffolding, authoring, validating, and evaluating SKILL.md packages.

## Scope

- Work inside `templates/base/.agents/skills/skills-creator/` plus the live docs that track progress.
- Include SKILL.md, `scripts/scaffold.py`, `scripts/validate.py`, `assets/skill_template.md`, `assets/eval_template.md`, and references for patterns, platforms, security, and antipatterns.
- Retire the old `create-skill` folder; do not alter other skills or routers.

## Constraints

- Keep the skill universal across surfaces (no platform-bound instructions).
- Follow the naming and validation rules from the specification (gerund form preferred, forbidden words, ≤64 chars, ≤500 body lines, ≤1-level references).
- Preserve unrelated skills and existing router work.

## Success Criteria

- `skills-creator/SKILL.md` reflects the seven-phase lifecycle and progressive disclosure rules, with clear references to supporting files.
- Scripts scaffold and validate skill packages per the naming/frontmatter/line-count rules.
- Assets and references match the required templates and checklists.
- Live docs reflect the updated objective and completed work.
