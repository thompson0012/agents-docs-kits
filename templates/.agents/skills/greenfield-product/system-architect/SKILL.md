---
name: system-architect
description: Use when a validated PRD exists and engineering is about to begin, and you need schemas, APIs, state flows, and infrastructure decisions that become docs/reference/implementation.md.
---

# System Architect

Use this skill to translate approved requirements into concrete implementation design.

## Core contract

- Start only after the PRD is validated.
- Do not reopen product scope.
- Design the structural foundation: data model, APIs, state flow, and deployment shape.
- Produce `docs/reference/implementation.md`.

## Focus

Cover the minimum that makes the architecture buildable:

- domain entities and schemas
- API contracts and boundaries
- state transitions and invariants
- infrastructure and integration assumptions
- implementation risks and ADR-worthy decisions

## Output

Return an implementation design that an engineer can build without renegotiating the PRD.
