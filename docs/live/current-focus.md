# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

Pilot the new router-package model on a real family by adding `using-sales` as the first concrete sales router and wiring the top-level suite router to delegate ambiguous sales requests into it.

## Scope

- Keep the work inside `templates/base/.agents/skills/using-sales/`, the touched `using-agent-practices/` files, and the live docs updated for continuity.
- Preserve the portable router approach: explicit child metadata, truthful install behavior, and lazy leaf loading.
- Use the pilot to validate whether the router-package model works on a real family before applying it to more families.

## Constraints

- Do not encode Anthropic-, OpenAI-, or other vendor-specific runtime rules as the canonical sales-router workflow.
- Keep the router narrow: select among `account-research`, `sales-call-prep`, and `sales-draft-outreach` without absorbing their full workflows.
- Keep the root suite router honest: route sales ambiguity to `using-sales` without forcing unrelated requests into the sales family.
- Do not commit from this task.

## Success Criteria

- `using-sales/SKILL.md` cleanly routes among the three sales leaves and exposes explicit router outputs.
- `using-sales/references/children.json` captures selection order, child boundaries, and install hints honestly.
- `using-agent-practices` and its category map delegate ambiguous sales requests to `using-sales`.
- Focused validation proves the new sales router package is structurally valid and the local validator rejects malformed router metadata.