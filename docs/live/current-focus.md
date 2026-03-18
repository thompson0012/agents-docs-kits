# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

Apply the router-package model to real families with nested leaf placement, starting with `using-sales` and `using-marketing`, so family entrypoints become the canonical discoverable paths and leaf skills live under their routers.

## Scope

- Keep the work inside `templates/base/.agents/skills/using-sales/`, `templates/base/.agents/skills/using-marketing/`, the touched router-authoring guidance, the root suite router files, and the live docs updated for continuity.
- Preserve the portable router approach: explicit child metadata, truthful install behavior, and lazy nested leaf loading.
- Remove the old top-level sales and marketing leaf placement as the canonical representation for those families.

## Constraints

- Do not encode Anthropic-, OpenAI-, or other vendor-specific runtime rules as the canonical router workflow.
- Keep routers narrow: they select among their child leaves and do not absorb the leaves' full workflows.
- The router path should tell the truth about family membership: sales leaves under `using-sales/`, marketing leaves under `using-marketing/`.
- Do not commit from this task.

## Success Criteria

- `using-sales` routes to nested child paths and its former top-level leaf skills now live under the router package.
- `using-marketing` exists as a router package with nested marketing leaves and explicit child metadata.
- `using-agent-practices` and its category map route ambiguous sales and marketing requests to the correct family routers.
- `create-router-skill` and `create-skill` guidance both reflect the nested-family convention.
- Focused validation proves the new nested router packages are structurally valid and the local validators reject malformed router metadata.