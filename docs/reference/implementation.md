# Implementation Reference

Read when implementing or changing technical behavior. Keep entries short and current.

## Technical Decisions

- Decision:
- Reason:
- Consequence:

## Interfaces

- Surface:
- Contract:
- Notes:

## Dependencies

- Dependency:
- Why it exists:
- Constraints:

## Caveats

- Caveat:
- Impact:
- Mitigation:


## Technical Decisions

- Decision: Root router-governance changes are verified with `python3 -m unittest scripts.tests.test_agents_router`, `python3 scripts/validate_agents_router.py`, and `git diff --check`.
- Reason: the root router now depends on both prose entrypoints and a machine-readable manifest; all three checks are needed to catch contract drift.
- Consequence: AGENTS/router edits are not complete until the unit test, validator, and whitespace check all pass.

## Dependencies

- Dependency: `.agents/router-manifest.json`
- Why it exists: machine-readable routing source for root governance surfaces and startup paths.
- Constraints: must stay aligned with root `AGENTS.md`, root local guides, and real filesystem paths.

- Dependency: `scripts/validate_agents_router.py`
- Why it exists: executable contract check for root router sections, local-guide headings, and manifest integrity.
- Constraints: warnings may be promoted to failures with `--strict`; keep schema changes synchronized with the tests.