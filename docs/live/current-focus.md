# Current Focus

Read after `AGENTS.md` when starting or resuming work. Keep this file limited to the current objective and the bounds for active work.

## Objective

Pressure-test the expanded router suite (`website-building`, `using-documents`, `using-legal`, `using-sales`, `using-marketing`, `using-reasoning`, `using-research`, and `using-finance`) and decide whether the router model is mature enough before creating any additional family routers.

## Scope

- Keep the work inside the existing router packages, the touched root-router docs, and the router-authoring guidance only if eval results expose a generic model gap.
- Compare router behavior against believable direct-leaf baselines and check whether nested paths, install hints, and selection order hold up under realistic prompts.
- Treat `using-documents/` as the canonical home for `docx`, `pdf`, `pptx`, and `xlsx`; do not create more router families until the expanded suite has been pressure-tested.

## Constraints

- Do not encode vendor-specific runtime rules as the canonical router workflow.
- Treat the current router families as the canonical structure unless evaluation reveals a concrete problem.
- If an eval exposes a flaw, patch the smallest honest rule or metadata field rather than widening the routers speculatively.
- Do not commit from this task.

## Success Criteria

- Prompt-pressure evals exist for the expanded router suite and compare router behavior against a believable baseline.
- Any routing failures are documented with concrete prompts and fixed at the correct boundary.
- A clear decision is recorded on whether the expanded router convention is ready for more families or needs another refinement pass first.