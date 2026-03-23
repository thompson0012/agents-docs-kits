---
name: plan-engineering-review
description: Use when a feature plan exists and needs pre-implementation engineering challenge for architecture, data flow, edge cases, testability, reversibility, and observability before coding starts.
---

# Plan Engineering Review

Use this skill to pressure-test an implementation plan before any repo-backed build work begins.

The job is to strengthen the plan, not to write code, review an existing diff, or improvise architecture during implementation.

## Boundary

Use this skill when:
- the feature direction is mostly chosen but the engineering shape still needs challenge
- the plan mentions architecture, integrations, migrations, background jobs, state changes, or operational risk
- the team needs a sharper view of failure modes, rollout safety, and test coverage before coding

Do not use this skill for:
- fuzzy feature framing with no stable plan yet — use `software-delivery/feature-discovery`
- PRD or scope definition work — use `feature-spec`
- live code review, branch review, or bug triage
- repo-backed implementation — use `coding-and-data` after this review stabilizes the plan
- browser QA or visual verification of a built product

## Core Contract

- Review the plan as a system design artifact, not as prose.
- Prefer the simplest architecture that tells the truth about constraints and ownership.
- Make data flow, control flow, and failure behavior explicit.
- Treat testability, rollback, and observability as first-class design requirements.
- Stop hidden coupling, hand-wavy migrations, and "we'll handle that later" placeholders before build starts.

## What Good Output Looks Like

Return a tightened plan with these sections:
1. **System boundary** — what changes, what stays external, and who owns each moving part
2. **Request and data flow** — the main happy path and the key alternate or failure paths
3. **Engineering risks** — the concrete failure modes or design gaps that would hurt correctness, reliability, or delivery
4. **Required plan edits** — specific decisions the plan must add or change before coding
5. **Verification gates** — the tests, metrics, logs, alerts, and rollback hooks that must exist for the plan to be honest
6. **Handoff** — either `Ready for coding-and-data.` or `Not ready for implementation.` with the blocking reasons

## Review Workflow

### Phase 1 — Reconstruct the Real Change

Extract the smallest accurate statement of:
- the user-visible behavior being added or changed
- the system boundary touched
- the data created, read, updated, deleted, or derived
- external dependencies, operators, and downstream consumers

If the plan hides the real change behind generic language, rewrite it plainly before reviewing further.

### Phase 2 — Trace the Flows

Map the flows the next implementer will actually need:
- entrypoints and callers
- state transitions
- persistence and cache interactions
- async work, retries, queues, and backfills
- integration boundaries and failure return paths

If a diagram would remove ambiguity, add a compact ASCII diagram.

### Phase 3 — Challenge the Architecture

For every major responsibility, ask:
- why does this logic live here instead of upstream, downstream, or behind an existing abstraction?
- does the plan introduce duplicate representations or conversion layers?
- is any new infrastructure spending complexity without enough payoff?
- what assumption would a tired maintainer get wrong?
- what part is hardest to reverse if it fails in production?

Bias toward boring, reversible designs unless the plan proves a more novel choice is necessary.

### Phase 4 — Cover Edge Cases and Failure Modes

Review at minimum:
- empty, invalid, duplicate, partial, stale, and out-of-order input
- permission and tenancy boundaries
- race conditions, retries, idempotency, and double-submit paths
- schema evolution, migrations, backfills, and rollback behavior
- degraded dependency behavior: timeout, partial outage, bad payloads, and rate limits
- user-visible truthfulness when work is delayed, queued, or failed

If the plan cannot explain what the caller sees when the system fails, it is not ready.

### Phase 5 — Make Verification Concrete

The plan must name:
- the unit, integration, and end-to-end checks that prove the design
- what must be asserted for error paths, not just the happy path
- what telemetry will exist at launch: logs, metrics, traces, alerts, dashboards, or audit events
- what rollout or reversal mechanism exists: feature flag, kill switch, migration guard, staged rollout, or manual recovery
- what evidence would show the feature is safe to expand, pause, or revert

Reject vague promises like "add tests" or "monitor it". The plan must say what gets tested and what gets observed.

### Phase 6 — Tighten the Plan

Convert the review into a smaller, more truthful plan:
- remove speculative complexity
- add missing invariants and contracts
- split unsafe big-bang steps into reversible stages
- name unresolved decisions explicitly
- mark blockers that must be answered before coding

End with a clear implementation recommendation: ready now, ready after plan edits, or not ready.

## Quick Checklist

- Is the system boundary explicit?
- Is the source of truth for each important piece of data clear?
- Are failure paths described as concretely as success paths?
- Can the change be rolled out and rolled back safely?
- Would a new engineer know what to test and why?
- Would on-call know what signal proves the feature is healthy or broken?
- Did the plan earn every new abstraction, queue, table, cache, and service?

## Failure Modes to Avoid

- Reviewing implementation style instead of plan correctness
- Accepting diagrams with no ownership, invariants, or rollback story
- Allowing "TBD" around migrations, retries, or error handling
- Treating testability as a follow-up task instead of a design property
- Adding platform complexity before proving simpler designs fail
- Confusing observability with a single log line or dashboard screenshot
- Declaring the plan ready when callers still cannot distinguish success from failure
