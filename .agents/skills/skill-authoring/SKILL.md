---
name: skill-authoring
description: Use when creating, upgrading, or packaging reusable skills and you need to choose between a leaf skill and a router family.
---

# Skill Authoring

Use this family when you are building or revising reusable skill packages for the template or another shared repo. It is maintainer-facing, not part of runtime delivery.

## Core contract

- Route to exactly one child.
- Use `create-skill` for leaf skills and single-job packages.
- Use `create-router-skill` for family routers that need discoverable children and install-or-fallback behavior.
- Keep the portable core first; add runtime-specific packaging only after the core works without vendor assumptions.
- Keep leaf and router responsibilities separate.

## Output

Return one of these forms:

- `Route to skill-authoring/create-skill.`
- `Route to skill-authoring/create-router-skill.`
- `No family child fits; answer directly.`

Add one sentence explaining why the selected child is the narrowest correct fit.

## References

- [children inventory](references/children.json)
