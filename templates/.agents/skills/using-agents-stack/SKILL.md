---
name: using-agents-stack
description: Use when a repository follows the agents-stack harness and the agent must route work to one workflow phase child explicitly.
---

# Using Agents Stack

Use this router when the hard problem is choosing the next harness phase in a repository that uses the agents-stack starter layout. If the repository does not use this harness family, or the request is ordinary implementation outside the harness workflow, no family child fits.

Do not perform the child workflow here. Choose the narrowest correct phase skill, then hand off.

## Core Contract

- Route to exactly one child or say no family child fits.
- Use `references/children.json` as the source of truth for child selection, prerequisites, install hints, and fallbacks.
- Use `references/state-machine.md` and `references/file-system-layout.md` for family-specific state and path rules.
- Prefer the strongest durable evidence on disk over chat memory or optimistic status text.
- Do not implement, review, or rewrite state inside the router.
- If the best child is missing, say to install it rather than quietly doing weaker work under the wrong child.

## Decision Order

1. Check whether the repository belongs to this family at all: `AGENTS.md`, `docs/live/*`, `.harness/<FEAT-ID>/`, and the agents-stack role/lifecycle model.
2. Read `docs/live/features.json` to determine whether the repo is uninitialized, has one active sprint, or needs a new proposal.
3. Apply the ordered selection logic from `references/children.json`.
4. Pick the narrowest child that matches the strongest durable evidence.
5. If the selected child is missing, install it when possible or disclose the fallback.
6. Hand off to the selected child.

## Family Workflow Boundary

This router owns only the agents-stack workflow family:

- project initialization of durable state
- sprint proposal
- adversarial contract review
- contract-bound execution
- independent live review
- state synchronization and archive closeout

This router does not replace ordinary feature implementation, generic project planning, or non-harness repository work. If the repository is not using the agents-stack state model, no family child fits.

## Router Output

Return one of these forms and then invoke the selected child if needed:

- `Route to using-agents-stack/project-initializer.`
- `Route to using-agents-stack/generator-proposal.`
- `Route to using-agents-stack/evaluator-contract-review.`
- `Route to using-agents-stack/generator-execution.`
- `Route to using-agents-stack/adversarial-live-review.`
- `Route to using-agents-stack/state-update.`
- `Install using-agents-stack/<child>, then route to using-agents-stack/<child>.`
- `No family child fits; answer directly.`

Add one sentence explaining why the selected child is the narrowest correct fit.

## References

- `references/children.json`
- `references/state-machine.md`
- `references/file-system-layout.md`

## Final Checklist

- [ ] Router stays focused on selection and handoff
- [ ] Child inventory is current in `references/children.json`
- [ ] Missing/install/fallback behavior is explicit
- [ ] Validation completed
