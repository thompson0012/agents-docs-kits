---
name: using-agents-stack
description: Use when a repository follows the agents-stack harness and the orchestrator must route work to one workflow phase child via a fresh worker.
---

# Using Agents Stack

Use this router when the hard problem is choosing the next harness phase in a repository that uses the agents-stack starter layout. If the repository does not use this harness family, or the request is ordinary implementation outside the harness workflow, no family child fits.

Do not perform the child workflow here. Choose the narrowest correct phase skill, then dispatch a fresh worker, sub-agent, Task agent, or equivalent delegation primitive for that child. Do not load the child phase into the orchestrator's own context and continue inline.

## Core Contract

- Route to exactly one child or say no family child fits.
- Use `references/children.json` as the source of truth for child selection, prerequisites, install hints, and fallbacks.
- Use `references/state-machine.md`, `references/file-system-layout.md`, and `references/orchestrator-worker.md` for family-specific state, path, and delegation rules.
- Prefer the strongest durable evidence on disk over chat memory or optimistic status text.
- Treat `build_failed`, `review_failed`, `awaiting_human`, and `escalated_to_human` as distinct routing states. Do not collapse them into generic "blocked" or route them all back into execution.
- Retries after `build_failed` or reconciled `review_failed` require a recorded clean restore boundary such as a disposable worktree, VCS snapshot, or equivalent `clean_restore_ref`. Automatic destructive reset is valid only in disposable workspaces and is not the default expectation.
- Respect attempt budgets. When `attempt_count` reaches `max_attempts`, or no safe clean restore boundary exists, automatic retry stops and the sprint must park for human action or escalation.
- Parked sprints in `.harness/` with `awaiting_human` or `escalated_to_human` remain visible durable state, but they do not count as the single runnable active sprint.
- When no runnable active sprint exists, choose the highest-priority pending backlog item whose dependencies are satisfied before proposing new work.
- Protect the orchestrator context: it selects, dispatches, and waits for structured worker outputs; it does not implement, review, or rewrite state inline.
- If the best child is missing, say to install it rather than quietly doing weaker work under the wrong child.

## Decision Order

1. Check whether the repository belongs to this family at all: `AGENTS.md`, `docs/live/*`, `.harness/<FEAT-ID>/`, and the agents-stack role/lifecycle model.
2. Read `docs/live/features.json` to determine whether the repo is uninitialized, has one runnable active sprint, has only parked sprints, or needs a new proposal.
3. If a runnable active sprint exists, route from the strongest local durable artifact for that sprint.
4. If `review.md` exists but live and local state have not yet reconciled the verdict, route to `state-update` before any new execution or proposal work.
5. If the sprint is in `build_failed` or reconciled `review_failed`, route to `generator-execution` only when attempts remain and `clean_restore_ref` defines a safe restore boundary.
6. If the sprint is in `awaiting_human` or `escalated_to_human` and that parked state is already reflected durably, do not auto-dispatch execution. Surface the parked state unless new human edits have changed the checkpoint.
7. If no runnable active sprint exists, ignore parked `awaiting_human` and `escalated_to_human` sprints for scheduling and select the highest-priority dependency-satisfied pending backlog item for proposal.
8. Pick the narrowest child that matches the strongest durable evidence.
9. If the selected child is missing, install it when possible or disclose the fallback.
10. Dispatch a fresh worker for the selected child with a stable worker ID, phase-appropriate tools, and explicit artifact return targets.

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

Return one of these forms, then dispatch the selected child as a fresh worker if needed:

- `Route to using-agents-stack/project-initializer.`
- `Route to using-agents-stack/generator-proposal.`
- `Route to using-agents-stack/evaluator-contract-review.`
- `Route to using-agents-stack/generator-execution.`
- `Route to using-agents-stack/adversarial-live-review.`
- `Route to using-agents-stack/state-update.`
- `Install using-agents-stack/<child>, then route to using-agents-stack/<child>.`
- `No family child fits; answer directly.`

Add one sentence explaining why the selected child is the narrowest correct fit. If a child is selected, continue by spawning a fresh worker with that child prompt rather than swapping personas inside the orchestrator.

When the durable truth is a fully reconciled `awaiting_human` or `escalated_to_human` sprint with no new human edits, the correct result is usually `No family child fits; answer directly.` plus an explanation that automation must wait on the file-based human handoff boundary.

## References

- `references/children.json`
- `references/state-machine.md`
- `references/file-system-layout.md`
- `references/orchestrator-worker.md`

## Final Checklist

- [ ] Router stays focused on selection and fresh-worker dispatch
- [ ] Child inventory is current in `references/children.json`
- [ ] Missing/install/fallback behavior is explicit
- [ ] Retry routing respects clean restore boundaries and attempt budgets
- [ ] Parked `awaiting_human` and `escalated_to_human` sprints do not auto-dispatch into execution
- [ ] No child work is performed inline in the orchestrator
- [ ] Validation completed
