# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

Run prompt-pressure evaluations against the expanded router suite now that the base template portability cleanup and audit gate are in place.

## Scope

- Keep `scripts/audit_base_template_skills.py` and `.github/workflows/base-template-skill-audit.yml` green while evaluating router behavior.
- Use the newly standardized portable skill corpus as the baseline; do not add more router families unless prompt-pressure evidence justifies it.
- Limit follow-up changes to eval-driven fixes and continuity docs; the portability cleanup itself is complete.

## Constraints

- Keep shipped skill names and directory layout stable; rely on portable YAML frontmatter and current-tool-surface guidance only.
- Do not reintroduce stale `skills/` paths, vendor branding, or unsupported tool names in skill docs.
- Do not commit from this task.

## Success Criteria

- Prompt-pressure evidence exists for the expanded router suite.
- Any resulting fixes preserve a passing `python3 scripts/audit_base_template_skills.py`.
- A clear decision is recorded on whether additional router families are still justified.