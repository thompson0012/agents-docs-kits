---
name: labs21-product-suite
description: Use when a user starts a new Labs21 product-definition workflow or needs to move between strategy, PRD, and system-design stages that produce the durable reference docs for downstream delivery.
---

# Labs21 Product Suite — Router

This router owns the stage-gated Labs21 product-development family. It chooses exactly one child skill, hands off cleanly, and does not perform the child workflow inline.

Read [child inventory](references/children.json) for the authoritative stage order, per-child route conditions, prerequisites, and install hints.

## Stage Order

1. **Strategy** — `labs21-chief-architect` (raw ideas, MVP framing, blueprint -> `docs/reference/design.md`)
2. **Product definition** — `labs21-prd-writer` (requirements, user stories, acceptance criteria -> `docs/reference/requirements.md`)
3. **System design** — `labs21-system-architect` (schemas, APIs, state flows, infrastructure -> `docs/reference/implementation.md`)

If the request would skip a prerequisite stage, route to the prerequisite child first and surface the gap.

## Boundary

- This router does not answer the product question itself; it selects the narrowest child that can.
- This family stops at durable product-definition outputs. Once `docs/reference/design.md`, `docs/reference/requirements.md`, and `docs/reference/implementation.md` exist, defined-feature delivery hands off to `harness-engineering` or `delivery-control`.
- If the best child is missing at runtime, say to install it. Do not silently substitute.
- If no child fits, say so and answer directly.

## References

- [child inventory](references/children.json)
- [router metadata](references/router-metadata.md)
- [relationship types](references/relationship-types.md)
