# Labs21 Suite Category Map

This template's shipped Labs21 suite under `templates/base/.agents/skills/` currently contains only these top-level skills and family routers.

## Suite Router

- `using-labs21-suite` — top-level discoverability router for the shipped Labs21 template skill surface when the right top-level entrypoint is not obvious yet

## Orchestration and Reflection

- `context-compaction` — compact session state for handoff or continuation
- `self-cognitive` — run confidence checks, retrospectives, and repeatable-workflow extraction

## Prompt Work

- `meta-prompting` — design or evaluate a prompt artifact such as a system prompt, prompt template, prompt architecture, rubric, or eval plan
- `prompt-augmentation` — enrich a sparse prompt or generate prompt variants for text, image, or video generation while preserving the user's core subject

## Skill Package Authoring

- `create-skill` — create or upgrade a reusable leaf skill package, scaffold a portable skill directory, or rewrite skill guidance into a reusable package
- `create-router-skill` — create or upgrade a discoverable router skill whose main job is selecting among child skills, carrying explicit child metadata, and handling install-or-fallback behavior honestly

Use `create-skill` when the package's job is one repeatable workflow. Use `create-router-skill` only when the package's job is family routing.

## Project and Product Founding

Route through `project-founding` when the request is about staged blueprinting and the right founding lane is not obvious yet.

- `project-founding/project-foundation` — turn a product or project idea into a staged blueprint with covered-now versus later scope, business-value priorities, roadmap versions, robustness questions, and extensibility checks
- `project-founding/ai-agent-foundation` — do the same for AI-native or agentic projects, adding governance, controllability, cost, observability, and human-override guidance

Keep harsh commercial teardowns in `startup-pressure-test`.

## Software Delivery Routing

Route through `software-delivery` when the request is non-trivial software feature work and the user needs help choosing the next delivery stage.

- `software-delivery/feature-discovery` — turn a fuzzy feature idea or change request into a clear problem statement and next-step recommendation
- `software-delivery/harness-design` — choose the honest delivery-control mode across single-session work, compacted continuation, or planner/generator/evaluator execution with explicit handoffs
- `software-delivery/plan-product-review` — challenge a plan on user value, scope, sequencing, and MVP shape before implementation
- `software-delivery/plan-engineering-review` — challenge a plan on architecture, failure modes, rollback, tests, and observability before implementation
- `software-delivery/plan-design-review` — challenge a plan on UX flows, states, accessibility, and interface clarity before implementation
- `software-delivery/frontend-evaluator` — provide strict independent browser-facing acceptance with evidence, defects, and retry guidance after implementation exists

## Commercial Reality Testing

- `startup-pressure-test` — pressure-test a startup, launch thesis, or business model with realistic acquisition, retention, monetization, burn, and runway pressure

## Outside the Shipped Labs21 Suite

The template no longer ships older router targets such as `website-building`, `using-documents`, `using-design`, `using-legal`, `using-sales`, `using-marketing`, `using-research`, `using-finance`, `media`, `coding-and-data`, `data-exploration`, `visualization`, or `cx-ticket-triage`.

Do not route to those from `using-labs21-suite`. If the user needs one of those moved or external workflows, say that no Labs21 suite skill fits and continue with the appropriate non-suite workflow instead of pretending the template still owns that path.
