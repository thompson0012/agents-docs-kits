# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The base template skill suite now has a repo-level audit gate and a broad portability cleanup: shipped skills align with the portable frontmatter contract, stale `skills/` path references are removed, and website-building/finance/research guidance no longer points at dead tool surfaces. Prompt-pressure evaluation of the expanded router suite is still pending.

## Latest Completed Work

Standardized the remaining legacy skill corpus onto the current portable contract, rewrote website-building around the current browser/local-run tool surface, removed stale vendor/tool/path references across document, finance, research, reasoning, marketing, legal, and sales skills, added `scripts/audit_base_template_skills.py` plus `.github/workflows/base-template-skill-audit.yml`, and deleted committed `.DS_Store` artifacts.

## In Progress

None.

## Blockers

None.

## Next Recommended Action

Resume Task 28: run prompt-pressure evaluations against the expanded router suite with `python3 scripts/audit_base_template_skills.py` kept green after each follow-up change.

## Touched Files

- `scripts/audit_base_template_skills.py`
- `.github/workflows/base-template-skill-audit.yml`
- `templates/base/.agents/skills/{coding-and-data,design-foundations,feature-spec,generating-design-tokens,media,meta-prompting,self-cognitive,startup-pressure-test,visualization}/SKILL.md`
- `templates/base/.agents/skills/using-{documents,finance,research,reasoning,legal,marketing,sales}/**`
- `templates/base/.agents/skills/website-building/{SKILL.md,game/**,informational/**,shared/**,webapp/**}`
- `docs/live/current-focus.md`
- `docs/live/progress.md`
- `docs/live/todo.md`
- deleted `.DS_Store` artifacts under repo root, `.git/`, and `templates/base/.agents/**`

## Verification Status

Observed success for:

- `python3 scripts/audit_base_template_skills.py`

## Hand-off Note

The new audit script is now the truth source for portability drift: it runs strict leaf/router validation and scans for stale `skills/` paths, unsupported tool names, vendor strings, and `.DS_Store` artifacts. Run it before claiming future skill-suite edits are complete.