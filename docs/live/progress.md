# Progress

Read after `docs/live/current-focus.md` to recover the latest state, continuity, and hand-off details. Keep each section concise so the next session can resume quickly.

## Current State

The root repository now has a lean AGENTS router, machine-readable routing metadata, executable router validation, and boundary-contract local guides for both the root repo and the template package hierarchy.

## Latest Completed Work

- rewrote root `AGENTS.md` into a lean router/index with startup minimums for repo work vs template work, scope fences, ordered decision flow, escalation rules, failure-mode fencing, and explicit router verification commands
- created root local guides at `.agents/AGENTS.md`, `.agents/skills/AGENTS.md`, `docs/AGENTS.md`, `docs/live/AGENTS.md`, and `docs/reference/AGENTS.md` so the repo now has real leaf boundary contracts instead of only a root guide
- added `.agents/router-manifest.json` as the machine-readable source of truth for root governance-surface routing and startup paths
- sharpened `.agents/skills/using-agents-md/SKILL.md` into a concrete governance-change triage skill with expected-output format, common scenarios, manifest lookup, and stronger negative controls
- standardized the template local guides under `templates/base/.agents/` and `templates/base/docs/` to the same boundary-contract shape: Local Scope, Owns, Does Not Own, Required Reads, Local Update Rules, and Failure Modes to Avoid
- added `scripts/tests/test_agents_router.py` first and watched it fail red before implementation
- implemented `scripts/validate_agents_router.py` to validate the root router sections, root and template leaf-guide contract headings, manifest schema, manifest paths, and repo-local skill inventory
- updated `docs/reference/{architecture,codemap,memory,lessons,implementation}.md` so the new root router, manifest, validator, and repo-vs-template scope fence are preserved as durable truth

## In Progress

None.

## Blockers

None.

## Next Recommended Action

Use the new root router and validator as the default governance path. A later follow-up can add negative eval fixtures and interrupted-work recovery checks, but no further action is required for this fix itself.

## Touched Files

- `AGENTS.md`
- `.agents/AGENTS.md`
- `.agents/skills/AGENTS.md`
- `.agents/skills/using-agents-md/SKILL.md`
- `.agents/router-manifest.json`
- `docs/AGENTS.md`
- `docs/live/AGENTS.md`
- `docs/reference/AGENTS.md`
- `templates/base/.agents/AGENTS.md`
- `templates/base/.agents/skills/AGENTS.md`
- `templates/base/.agents/skills-optional/AGENTS.md`
- `templates/base/docs/AGENTS.md`
- `templates/base/docs/live/AGENTS.md`
- `templates/base/docs/reference/AGENTS.md`
- `scripts/tests/test_agents_router.py`
- `scripts/validate_agents_router.py`
- `docs/reference/architecture.md`
- `docs/reference/codemap.md`
- `docs/reference/memory.md`
- `docs/reference/lessons.md`
- `docs/reference/implementation.md`
- `docs/live/progress.md`

## Verification Status

- RED first: `python3 -m unittest scripts.tests.test_agents_router` failed before implementation with four failures covering missing root local guides, missing validator, missing router sections, and non-standardized template leaf guides
- GREEN: `python3 -m unittest scripts.tests.test_agents_router`
- GREEN: `python3 scripts/validate_agents_router.py`
- GREEN: `python3 -m unittest scripts.tests.test_template_agents_hierarchy`
- GREEN: `git diff --check`

## Hand-off Note

The repo and template now both expose explicit boundary contracts, but only the root repo guide acts as the active router. No `docs/live/current-focus.md` update was needed because the active objective and scope did not change. Reference docs were updated because this change introduced durable router structure, entrypoints, validator behavior, and reusable lessons.
