# Labs21 Suite Category Map

> Human-readable summary derived from [children.json](children.json). For authoritative route conditions and selection order, read `children.json` directly.

## Suite Router

- `using-labs21-suite` — top-level router for the shipped Labs21 template skill surface

## Orchestration and Reflection

- `context-compaction` — compact session state for handoff or continuation
- `self-cognitive` — confidence checks, retrospectives, and repeatable-workflow extraction

## Prompt Work

- `meta-prompting` — design or evaluate prompt artifacts (system prompts, templates, rubrics, architectures)
- `prompt-augmentation` — enrich a sparse generation prompt without redesigning the prompt architecture

## Skill Package Authoring

- `create-skill` — create or upgrade a reusable leaf skill package
- `create-router-skill` — create or upgrade a router package with child metadata and honest fallbacks

## Design Workflow Routing

- `using-design` — family router for design-specific work (foundations, tokens, generative UI, liquid-glass)

## Software Delivery Routing

- `delivery-control` — family router for non-trivial feature lifecycle (discovery, harness design, plan review, evaluator selection)

## Commercial Reality Testing

- `startup-pressure-test` — harsh startup viability teardown with realistic acquisition, retention, and runway pressure

## Reasoning Workflow Routing

- `using-reasoning` — family router for analytical, strategic, or diagnostic reasoning

## Outside the Shipped Suite

The template no longer ships a set of moved or external families that sit outside `using-labs21-suite`. Do not route to them from `using-labs21-suite`.
