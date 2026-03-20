# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

Task 34 and the vendor-agnostic cleanup remain complete, and `templates/base/AGENTS.md` now tells future agents both to check the project-local `.agents/skills/` directory when a needed skill was not loaded from `~/.agents/skills` and to use `.agents/skills/using-agent-practices/SKILL.md` as the router index when the right local skill is unclear. The next likely step is still a capability-based methodology refinement pass across the finance, research, and webapp docs that were already flagged as promising follow-up targets.

## Latest Completed Work

Enhanced `templates/base/AGENTS.md` with a `Project-Local Skills` section that explicitly points agents at `.agents/skills/` as the fallback skill surface when the needed skill was not loaded from `~/.agents/skills`, and now also requires `.agents/skills/using-agent-practices/SKILL.md` as the router index when the correct local skill or family router is not obvious.

## In Progress

None.

## Blockers

None.

## Next Recommended Action

Review the identified methodology-heavy docs in finance, research, and website-building/webapp, then tighten their capability-based guidance without reintroducing stale or vendor-specific surface assumptions.

## Touched Files

- `scripts/audit_base_template_skills.py`
- `scripts/tests/test_audit_base_template_skills.py`
- `scripts/tests/test_vendor_agnostic_naming.py`
- `.github/workflows/base-template-skill-audit.yml`
- `templates/base/.agents/skills/{coding-and-data,design-foundations,feature-spec,generating-design-tokens,media,meta-prompting,self-cognitive,startup-pressure-test,visualization}/SKILL.md`
- `templates/base/.agents/skills/startup-pressure-test/evals/{evals.json,trigger-evals.json}`
- `templates/base/.agents/skills/using-agent-practices/{SKILL.md,evals/**,references/category-map.md}`
- `templates/base/.agents/skills/using-{documents,finance,research,reasoning,legal,marketing,sales}/**`
- `templates/base/.agents/skills/website-building/{SKILL.md,game/**,informational/**,shared/**,webapp/**}`
- `templates/base/AGENTS.md`
- `docs/live/current-focus.md`
- `docs/live/progress.md`
- `docs/live/todo.md`
- deleted `.DS_Store` artifacts under repo root, `.git/`, and `templates/base/.agents/**`

## Verification Status

Observed success for:

- `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-agent-practices --strict`
- `python3 templates/base/.agents/skills/using-documents/scripts/validate_router.py templates/base/.agents/skills/using-documents`
- `python3 templates/base/.agents/skills/using-reasoning/scripts/validate_router.py templates/base/.agents/skills/using-reasoning`
- `python3 -m unittest scripts.tests.test_audit_base_template_skills scripts.tests.test_vendor_agnostic_naming -v`
- `python3 -m py_compile scripts/audit_base_template_skills.py scripts/tests/test_audit_base_template_skills.py scripts/tests/test_vendor_agnostic_naming.py templates/base/.agents/skills/using-documents/docx/scripts/comment.py templates/base/.agents/skills/website-building/shared/llm-api/media_client.py templates/base/.agents/skills/website-building/shared/llm-api/generate_image.py templates/base/.agents/skills/website-building/shared/llm-api/generate_video.py templates/base/.agents/skills/website-building/shared/llm-api/generate_audio.py templates/base/.agents/skills/website-building/shared/llm-api/transcribe_audio.py`
- `python3 scripts/audit_base_template_skills.py`
- repo-wide grep for the removed vendor-name patterns returned no matches
- `git diff --check` returned no output
- readback review of `templates/base/AGENTS.md` confirmed the new `Project-Local Skills` section and the explicit `~/.agents/skills` → `.agents/skills/` fallback wording
- readback review of `templates/base/AGENTS.md` confirmed the new router-index rule for `.agents/skills/using-agent-practices/SKILL.md`

## Hand-off Note

`templates/base/AGENTS.md` now covers both the generated doc surface and the project-local skill surface. Generated projects will explicitly tell agents to fall back to `.agents/skills/` when a needed skill was not already loaded from `~/.agents/skills`, and to read `.agents/skills/using-agent-practices/SKILL.md` as the router index when local skill routing is unclear.