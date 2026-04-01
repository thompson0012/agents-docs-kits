---
name: using-labs21-suite
description: Use when the user may need a shipped Labs21 template skill from `.agents/skills` and the right top-level skill or family router is not obvious yet.
---

# Using Labs21 Suite

Route to the narrowest shipped Labs21 template skill. Do not solve the user's substantive task here.

Read [child inventory](references/children.json) for the authoritative route table: selection order, per-child route conditions, avoid conditions, and install hints. Apply the selection order top-to-bottom and pick the first child whose `route_when` matches.

For a human-readable category overview, see [category map](references/category-map.md).

## Boundary

- Route only among children listed in [children.json](references/children.json). That is the shipped boundary.
- Do not route to moved or external families. They are outside this router.
- If the best child is missing at runtime, say to install it. Do not silently substitute.
- If no shipped child fits, say so and continue with a non-suite workflow.

## Failure Modes

- Forcing a Labs21 suite route onto work that left this boundary (repo coding, websites, documents, legal, sales, marketing, research, finance, media, data-profiling).
- Routing prompt-architecture work to `prompt-augmentation` when the user needs `meta-prompting`.
- Routing router-package work to `create-skill` when the package's job is family routing.
- Routing delivery lifecycle work to `delivery-control` when the need is orchestration, independent QA, or structured knowledge extraction inside `delivery-control`.
- Routing startup viability into `using-reasoning` because it sounds analytical.
- Routing ordinary implementation into `using-design` when the hard problem is not the design boundary.
