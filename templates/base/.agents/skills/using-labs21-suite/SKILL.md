---
name: using-labs21-suite
description: Use when the user may need a shipped Labs21 template skill from `.agents/skills` and the right top-level skill or family router is not obvious yet.
---

# Using Labs21 Suite

Use this router to choose the narrowest shipped Labs21 template skill when a request could fit more than one top-level suite entrypoint.

Do not solve the user's substantive task here. Pick exactly one shipped top-level skill or say that no Labs21 suite skill fits.

For the current shipped inventory and install hints, read [child inventory](references/children.json). For the human-readable suite map, read [category map](references/category-map.md).

## Core Contract

- Route only among the currently shipped top-level skills in this template suite.
- Do not route to moved or external families such as `website-building`, `using-documents`, `using-design`, `coding-and-data`, `using-research`, or similar non-suite skills. They are outside this router's owned boundary.
- Prefer a family router only when the ambiguity lives inside that family. In this suite, that means `project-founding` or `software-delivery`.
- If the best shipped child is missing, say to install it before routing. Do not silently substitute a different child.
- If no shipped Labs21 suite skill fits, say so and answer directly or continue with a non-suite workflow.

## Decision Order

Apply these checks in order.

1. Need session compaction, handoff state, or continuation summary -> `context-compaction`
2. Need a confidence check, retrospective, or repeatable workflow extraction -> `self-cognitive`
3. Need a prompt artifact, system prompt, prompt template, rubric, or prompt architecture -> `meta-prompting`
4. Need a sparse text, image, or video generation prompt enriched without redesigning the prompt architecture -> `prompt-augmentation`
5. Need a reusable leaf skill package created or upgraded -> `create-skill`
6. Need a router package created or upgraded with child metadata and honest install-or-fallback behavior -> `create-router-skill`
7. Need staged project or product blueprinting, and the right founding lane is not obvious yet -> `project-founding`
8. Need lifecycle guidance for non-trivial software delivery and the next stage inside that family is not obvious yet -> `software-delivery`
9. Need a harsh startup viability teardown, launch stress test, or CAC/churn/runway pressure pass -> `startup-pressure-test`
10. Otherwise -> no Labs21 suite skill

## Router Output

Return one of these forms and then invoke the selected skill if needed:

- `Route to context-compaction.`
- `Route to self-cognitive.`
- `Route to meta-prompting.`
- `Route to prompt-augmentation.`
- `Route to create-skill.`
- `Route to create-router-skill.`
- `Route to project-founding.`
- `Route to software-delivery.`
- `Route to startup-pressure-test.`
- `No Labs21 suite skill fits; answer directly.`

Add one sentence explaining why the selected route is the narrowest correct fit.

## Failure Modes to Avoid

- routing to removed families that are no longer shipped in this template suite
- treating this router as a generic umbrella for every skill available in the runtime
- routing plain repo coding or debugging into this suite after `coding-and-data` moved out
- routing website, document, legal, sales, marketing, research, finance, design, media, or data-profiling work into this suite just because older versions used to own those paths
- routing prompt-architecture work to `prompt-augmentation` when the user really needs `meta-prompting`
- routing router-package work to `create-skill` when the package's job is family routing
- routing early project blueprinting to `startup-pressure-test` when the user still needs a staged plan before a teardown is honest
- routing non-trivial software delivery straight to `self-cognitive` when the main need is still discovery, delivery-control design, plan review, or evaluator selection inside `software-delivery`
- forcing a Labs21 suite route onto a request that is now outside this router's owned boundary
