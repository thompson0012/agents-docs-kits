# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

Pressure-test the nested router families (`using-sales`, `using-marketing`, `using-reasoning`, `using-research`, and `using-finance`) and decide whether the router model is mature enough before adding any more family routers.

## Scope

- Keep the work inside the nested router packages, the touched root router docs, and the router-authoring guidance only if eval results expose generic model gaps.
- Compare router behavior against direct leaf selection and check whether nested paths, install hints, and selection order hold up under realistic prompts.
- Do not start new router families until the eval evidence is reviewed.

## Constraints

- Do not encode vendor-specific runtime rules as the canonical router workflow.
- Treat the current nested families as the canonical structure unless evaluation reveals a concrete problem.
- If an eval exposes a flaw, patch the smallest honest rule or metadata field rather than widening the routers speculatively.
- Do not commit from this task.

## Success Criteria

- Prompt-pressure evals exist for the nested router families and compare router behavior against a believable baseline.
- Any routing failures are documented with concrete prompts and fixed at the correct boundary.
- A clear decision is recorded on whether the nested-router convention is ready for more families or needs another refinement pass first.