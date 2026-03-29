---
name: project-founding
description: Use when a request is about founding or blueprinting a new project, product, or internal system and you must choose between general project founding and AI-native or agentic founding.
---

# Project Founding

Use this router when the job is to turn an idea into a staged project blueprint and more than one founding child could fit.

Do not perform the leaf workflow here. Choose the narrowest correct founding skill, then hand off.

## Core Contract

- Choose exactly one primary child or decide that no `project-founding` child fits.
- Default to `project-founding/project-foundation` unless AI behavior, model economics, autonomy, or governance materially changes the blueprint.
- Route to `project-founding/ai-agent-foundation` only when model output quality, tool use, memory, human override, policy control, latency, cost, or failure observability is part of the founding problem itself.
- Use `references/children.json` as the source of truth for child boundaries, install hints, and companion recommendations.
- If the best child is missing, say to install it rather than quietly doing weaker work under the wrong child.
- Do not let this family absorb startup viability teardowns, implementation plans, or generic execution work.

## Decision Tree

| Founding Need | Route | Examples |
|---|---|---|
| General product, service, workflow, or internal-tool blueprinting | `load_skill("project-founding/project-foundation")` | define the wedge, scope v1, map covered vs uncovered situations, set roadmap versions, preserve extensibility |
| AI-native or agentic product blueprinting where model behavior and control surfaces are first-class | `load_skill("project-founding/ai-agent-foundation")` | AI copilot, agent workflow, human approval loop, memory strategy, policy enforcement, latency and unit-economics constraints |

Use the AI child when the product promise depends on uncertain model behavior or delegated machine action. If AI is optional seasoning on an otherwise ordinary product, stay with `project-founding/project-foundation`.

## Allowed Handoffs

- `project-founding/project-foundation -> project-founding/ai-agent-foundation` when AI or agent governance becomes central after the initial blueprint is framed.
- `project-founding/ai-agent-foundation -> project-founding/project-foundation` when the real problem is still ordinary product founding and AI is only an implementation option.
- `any project-founding child -> startup-pressure-test` after the blueprint exists and the next question is whether the business survives harsh commercial scrutiny.

## Forbidden Defaults

- Do not route to `project-founding/ai-agent-foundation` just because the prompt mentions AI once.
- Do not route to `project-founding/project-foundation` when hallucination handling, tool permissions, model portability, human override, or retry-budget control will decide whether the product is viable.
- Do not use this family when the user really wants a brutal viability teardown, investor-style skepticism, or CAC/churn/runway pressure testing.
- Do not turn the router into a mini leaf skill by writing the full blueprint here.

## References

- `references/children.json`

## Router Output

Return one of these forms and then invoke the selected child if needed:

- `Route to project-founding/project-foundation.`
- `Route to project-founding/ai-agent-foundation.`
- `Install <child-path>, then route to <child-path>.`
- `No project-founding child fits; answer directly.`

Add one sentence explaining why the selected child is the narrowest correct fit.

## Failure Modes to Avoid

- treating any mention of AI as proof that agent-specific founding is required
- treating an AI-native product as ordinary software planning and ignoring controllability, budget, and override design
- competing with `startup-pressure-test` by turning blueprinting into a harsh viability teardown
- treating multi-agent structure as the default rather than a justified design choice
- hiding uncovered situations, deferred work, or fragile assumptions behind polished roadmap language
