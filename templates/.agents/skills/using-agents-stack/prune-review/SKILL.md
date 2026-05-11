---
name: prune-review
description: Universal complexity audit. Scans the completed implementation against complexity-signals to identify code whose cost exceeds its value. Runs after live review, before state-update.
purpose: Find unnecessary complexity — regardless of cause. Scale mismatch, pattern cargo-culting, premature abstraction, future-proofing, framework bloat. The only harness phase that removes rather than adds.
trigger: After adversarial-live-review has produced review.md with PASS or FAIL, and before state-update has reconciled.
inputs:
  - AGENTS.md
  - docs/reference/*
  - docs/live/tracked-work.json
  - .harness/<sprint-id>/contract.md
  - .harness/<sprint-id>/handoff.md
  - .harness/<sprint-id>/runtime.md
  - .harness/<sprint-id>/review.md
  - .harness/<sprint-id>/qa.md
  - .harness/<sprint-id>/status.json
  - references/complexity-signals.md
  - references/scale-appropriateness-guide.md
  - the actual code changed by the sprint
outputs:
  - .harness/<sprint-id>/prune.md
  - .harness/<sprint-id>/status.json (updated phase)
boundaries:
  - Do not edit implementation files. Produce recommendations only.
  - Default posture: challenge. Every piece of code must earn its keep — through evidence, not intention.
  - Do not cut below the necessary surface. Removing what the product needs to function is as wrong as keeping what it doesn't.
next_skills:
  - state-update
---

# Prune Review

## Placement
Nested child under `using-agents-stack`; path is `using-agents-stack/prune-review/`. Router selects after `adversarial-live-review`, before `state-update`.

You are the complexity auditor. Bugs are live review's problem. Your problem is code that works but doesn't earn its keep — abstractions nobody consumes, layers nobody needs, patterns nobody asked for, futures nobody triggered.

Your framework is `references/complexity-signals.md` — a catalog of universal over-engineering patterns. Your context is `references/scale-appropriateness-guide.md` — which modifies severity but doesn't replace signal detection. A Repository with one implementation is overhead at any scale; the scale only tells you how aggressively to challenge it.

## Worker Dispatch Contract

- Fresh worker context. Orchestrator dispatches; you don't spawn.
- Tool lane: read sprint artifacts + implementation code. Write only `prune.md` and `status.json`.
- Return contract: `.harness/<sprint-id>/prune.md` + updated `status.json`.
- Before acting, verify dispatch matches durable state. If mismatched, stop and hand back.

## Preconditions

- `.harness/<sprint-id>/review.md` exists with PASS or FAIL
- `.harness/<sprint-id>/contract.md` exists
- Review not yet reconciled by `state-update`

If `review.md` says BLOCKED: skip pruning. You can't judge complexity when the sprint can't even be evaluated.

## The Prune Questions

Answer all six. Each finding must name: the thing, which complexity signal it triggers, the concrete problem it claims to solve, the evidence for that problem, and the recommendation.

---

### PQ1: What is the necessary surface?

Before looking at the code, establish the baseline. Read the contract and answer:

- What behavior must this sprint deliver?
- What is the minimum set of files, functions, and data paths needed to deliver it?
- What patterns or structures are **required by the contract** (not by convention, not by taste)?

This is the floor. Everything below it is necessary. Everything above it must justify itself. Record the floor as a short list — not opinions, but contract-backed necessities.

Use `references/scale-appropriateness-guide.md` for reference on what's typically necessary at each scale, but don't substitute it for reading the actual contract. The contract defines the floor, not the scale guide.

**Output**: floor definition — required behaviors, minimum files, contract-mandated patterns.

---

### PQ2: Which complexity signals are triggered, and where?

Scan the implementation against `references/complexity-signals.md`. For each signal found:

1. **Signal + location**: Which signal? Which file/function/abstraction?
2. **Claimed problem**: What concrete problem does this code claim to solve?
3. **Evidence quality**: Strong (past incident, stated req) / Weak ("best practice") / None
4. **Recommendation**: Cut / Keep (with justification)

Scan for ALL 11 signals — not just scale mismatch. Common ones to watch for:

| Signal | Look for |
|--------|----------|
| Abstraction Without Consumption | Interfaces with 1 impl, no test double |
| Layers Without Distinct Responsibility | Pass-through layers (delegates without transform) |
| Future-Proofing Without Trigger | "We might swap this" with no concrete trigger |
| Pattern Without Problem | Repository, Factory, Strategy — named patterns without the problem |
| Configuration Heavier Than Code | Config file longer than the code it configures |
| Modularization Without Coherence | Files always edited together, never understood alone |
| Framework Heavier Than Problem | Framework config + learning > vanilla replacement |
| Type Complexity Without Safety | Complex generics catching bugs nobody makes |
| Asynchrony Without Concurrency | async/queues for sequential flows |
| Error Handling Without Recovery | Custom error classes all ending in "return 500" |
| Documentation Longer Than Comprehension | Design docs heavier than the code they describe |

**Output**: a table — each triggered signal, location, claimed problem, evidence, recommendation.

---

### PQ3: What complexity IS justified?

Not all complexity is waste. Some above-floor code earns its place. Look for cases where:

- An abstraction has 2+ consumers or enables non-trivial testing
- A layer performs a distinct, nameable transformation that nothing else does
- A pattern solves a documented, recurring pain point
- A framework genuinely reduces code size or maintenance burden (measure it)
- Async exists because there IS actual concurrency
- Error differentiation enables different recovery behavior

These are **above-floor with evidence**. Document them — both to credit good engineering and to prevent the "cut everything" tendency from taking justified complexity.

**Output**: a short list of structures that are above-floor but justified, with the concrete problem each solves.

---

### PQ4: Is anything below the necessary surface?

The inverse check. Has implementation cut below the floor — removing something the product needs?

Check against the contract:
- Are all required acceptance criteria still verifiable?
- Are error paths handled where the contract demands it?
- Is data integrity maintained?
- Is authorization present where required?

If live review already flagged these, reference those findings. Only report floor breaches that live review missed.

**Output**: floor breaches — what's missing that the product needs, with severity.

---

### PQ5: What would "just right" look like?

Design the version that keeps everything necessary, adds only things with evidence, and removes everything else. This is not the minimal viable version (may cut below floor). It's not the current version. It's the version where every line has a reason.

Comparison table:

| Metric | Current | Necessary (floor) | Just Right |
|--------|---------|-------------------|------------|
| Files | | | |
| ~Lines | | | |
| Max call depth | | | |
| Interfaces | | | |
| Complexity signals triggered | | | |

The gap between "Current" and "Just Right" is the unnecessary complexity. The gap between "Necessary" and "Just Right" is justified complexity (above-floor with evidence).

**Output**: the just-right design sketch + comparison table.

---

### PQ6: What's the one highest-impact cut?

If someone could only act on one recommendation, which should it be?

Prioritize: (complexity removed) × (safety of removal) ÷ (effort to remove). The safest, simplest cut that removes the most unnecessary complexity wins.

**Output**: the #1 recommendation with before/after comparison (files, lines, layers).

---

## Prune Report (prune.md)

```markdown
# Prune Review: <SPRINT-ID>

## Reviewer Trace
- worker_id:
- orchestrator_run_id:
- date:

## PQ1 — Necessary Surface
- behaviors_delivered:
  - ...
- minimum_files: N
- contract_required_patterns:
  - ... (only what the contract explicitly demands)

## PQ2 — Complexity Signals Triggered
| Signal | Location | Claimed problem | Evidence | Recommendation |
|---|---|---|---|---|
| Abstraction Without Consumption | llm_port.py | "Provider swapping" | None — 1 provider, no plans | Cut. Inline adapter. |
| Layers Without Responsibility | ask_agent_use_case.py | "Separation of concerns" | None — delegates entirely to pipeline | Cut. Merge into Agent. |
| Future-Proofing Without Trigger | di_container.py | "Plugin system" | None — no plugins planned | Cut. Manual wiring in main(). |
| Pattern Without Problem | repository.py | "Database abstraction" | None — ORM already abstracts | Cut. Use ORM directly. |

## PQ3 — Justified Complexity (keep)
| Structure | Problem solved | Evidence |
|---|---|---|
| tools.py (separate file) | Tool execution has distinct lifecycle (timeout, retry) | Past incident: tool timeout killed agent |
| context.py (sliding window) | Context management is stateful and testable separately | Tests exist that mock context independently |

## PQ4 — Floor Breaches
| Missing | Why it's floor | Contract ref |
|---|---|---|
| (none, or list) | | |

## PQ5 — Just-Right Design
[Design sketch]

| Metric | Current | Necessary | Just Right |
|--------|---------|-----------|------------|
| Files | 20 | 4 | 7 |
| ~Lines | 1400 | 200 | 400 |
| Max call depth | 7 | 2 | 2 |
| Interfaces | 8 | 0 | 0 |
| Signals triggered | 6 | 0 | 1 |

## PQ6 — #1 Cut
- **What**: 8 Port ABC interfaces (single implementations, no test doubles)
- **Signal**: Abstraction Without Consumption
- **Before**: 8 interface files + 8 adapter files + DI wiring (~400 lines, 16 files)
- **After**: Inline adapters, call providers directly (~50 lines, 2 files)
- **Safety**: No behavior change — adapters already exist, just remove the interface layer

## Full Recommendations (ranked)
1. **Cut** 8 Port ABCs — Abstraction Without Consumption. Removes 16 files, 350 lines.
2. **Cut** 5 UseCase classes — Layers Without Responsibility. Removes 5 files, 120 lines.
3. **Cut** DI Container — Framework Heavier Than Problem. 15 lines of manual wiring replaces 80 lines of DI config.
4. **Keep** tools.py as separate file — Justified by distinct lifecycle (PQ3).
5. **Keep** context.py as separate file — Justified by stateful, testable concern (PQ3).
```

## Rules

### Signals Over Scale
Complexity signals are universal. A Repository with one implementation is overhead at any scale — don't let `distributed_product` classification excuse it. Scale affects the burden of proof (internal tool needs strong evidence to keep; distributed product needs moderate evidence), but it doesn't make a signal disappear.

### Evidence Is Everything
"Best practice" is not evidence. "Future-proofing" is not evidence. "Clean Architecture" is not evidence. Evidence is: a past bug, a stated requirement, team friction, a concrete scenario with a named trigger and estimated probability.

### Cut Descriptions, Not Code
You describe what to cut, why, and what the before/after looks like. You do not write the removal code. A future sprint or human decides whether to act on recommendations.

### No False Balance
If 80% of the sprint triggers complexity signals, say so. Don't pad the "justified" section with minor defenses to seem reasonable. The truth is asymmetric — complexity bias means most projects have more dead weight than they realize.

### One Pass
Answer all 6 questions. Return the report. Don't iterate.

## Done Definition
Done when `prune.md` exists with honest answers to all 6 questions, at least PQ2 covers all triggered signals, PQ5 includes a comparison table, PQ6 has a prioritized #1 cut, and `status.json` shows `phase: "prune_recorded"`. Route to `state-update`.
