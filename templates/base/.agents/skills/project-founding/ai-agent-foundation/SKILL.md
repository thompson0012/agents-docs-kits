---
name: ai-agent-foundation
description: Use when founding an AI-native or agentic product where model behavior, human override, latency, observability, unit economics, policy control, data sensitivity, or agent responsibility materially changes the blueprint.
---

# AI Agent Foundation

Use this skill to found AI-native or agentic products honestly: what the system should do, what the human must still own, what failure modes are acceptable, and what controls make the product commercially repeatable instead of merely impressive in a demo.

The goal is the same founding arc as `project-foundation`, but with explicit treatment of model uncertainty, automation boundaries, and operating economics.

## Core Contract

- Preserve the full founding arc: clarify the problem, justify why AI belongs, define product 1.0, expose covered and uncovered situations, rank features by business value, and build a staged roadmap.
- Every blueprint must state whether non-AI automation is sufficient, whether one controlled assistant is sufficient, and what specifically justifies any multi-agent design.
- Do not describe autonomy without naming responsibility, approval boundaries, retry rules, budget enforcement, and failure logging.
- Treat hallucination, latency, unit economics, observability, human override, policy control, data sensitivity, model portability, feedback loops, and memory value as first-class design inputs.
- Keep the system governable: the user should know what the model may do, what it may never do, and how mistakes surface.
- Do not replace `startup-pressure-test`. This skill designs the blueprint; it does not perform the harsh market teardown.

## When This Skill Fits

Use it for:

- AI copilots where the product promise depends on model output quality or tool use
- agent workflows where the system plans, acts, or coordinates work with bounded autonomy
- products that need approval loops, policy enforcement, auditability, or model portability from day one
- requests that explicitly need guidance on latency, cost control, memory, or feedback loops as part of the founding design

Route away when:

- AI is only a replaceable implementation detail and the real job is ordinary product blueprinting
- the user wants a general startup viability teardown rather than a staged AI product design

## Workflow

### Phase 1 — Prove AI is actually required

Answer in order:

- what the user job is
- what non-AI software or workflow alternative exists
- why that alternative is insufficient
- whether retrieval, ranking, classification, generation, or action is the real AI contribution

If ordinary software solves the problem adequately, say so. Do not force AI into the wedge.

### Phase 2 — Choose the minimum responsible operating model

Start from the least autonomous design that works.

Evaluate in this order:

1. deterministic software or workflow support
2. single AI assistant with bounded tools and human review
3. multiple specialized agents only when responsibilities truly differ and coordination adds value

For the chosen level, define:

- who plans
- who executes
- who evaluates
- who approves
- what remains under human control

### Phase 3 — Define AI product 1.0 and control architecture

Specify:

- target user and primary workflow
- must-have capabilities and explicit non-goals
- acceptable failure boundary
- stable core, variable prompt or policy layer, and interface boundaries
- model layer, tool layer, memory layer, policy layer, and observability layer

The architecture must say how actions are gated, not only how outputs are generated.

### Phase 4 — Surface failure modes and uncovered situations

Explicitly separate:

- situations covered now
- partially covered situations
- uncovered situations
- intentionally deferred autonomy

Then define what happens under failure:

- hallucination or factual error
- tool failure or partial completion
- latency spike or timeout
- budget breach
- policy violation attempt
- sensitive-data exposure risk
- bad memory or stale feedback contamination

### Phase 5 — Re-rank by business value and control burden

For each capability, evaluate both upside and operating burden:

- revenue or retention effect
- trust impact
- latency cost
- model or tooling cost
- observability and review burden
- policy or security complexity

Then decide whether to build now, reserve, experiment, or avoid.

### Phase 6 — Design the learning and portability loop

Define:

- what feedback is captured
- what qualifies as a failure worth logging
- how prompts, policies, or models change safely
- whether memory creates durable user value or only hidden complexity
- what portability boundary prevents lock-in to one model vendor

### Phase 7 — Build the staged roadmap

Produce at least these versions:

- v1.0 assisted and reviewable
- v2.0 controlled autonomy
- v3.0 scaled governance and economics
- long-term leverage

Each version should state the objective, user value, technical milestone, commercial milestone, and the control milestone that must be true before advancing.

## Decision Rules

- Prefer non-AI or simpler AI when it achieves the job with less failure surface.
- Prefer one agent over many unless there is a clear responsibility split with measurable benefit.
- If a human override path is required for trust or policy, it is not optional.
- If retries, latency, or cost can blow through budget silently, the design is incomplete.
- If memory does not create durable value, keep it out of version 1.
- If failure cannot be observed and logged, autonomy claims are not credible.

## Anti-Patterns

- agentic theatre without a clear responsibility map
- autonomy before wedge
- hidden human labor disguised as automation
- memory accumulation without measurable product value
- model lock-in with no portability boundary
- demo-quality output with no override, policy, or logging design

## Output Template

Use this template literally.

```md
# Project Name

## Executive Framing
- What it is:
- Who it serves:
- Core job:
- Why now:

## Why AI Belongs Here
- Non-AI alternative:
- Why that is insufficient:
- Minimum AI contribution:
- Why AI is part of the wedge rather than a later enhancement:

## Operating Model Choice
- Deterministic or non-AI option considered:
- Single-assistant option considered:
- Multi-agent option considered:
- Chosen model and why:
- Human responsibilities that remain:

## World Context and Constraints
- Capability limits that matter:
- Latency constraints:
- Unit-economics constraints:
- Trust, policy, or compliance constraints:
- Data-sensitivity constraints:

## AI Product 1.0 Definition
- Target user:
- Primary workflow:
- Must-have capabilities:
- Explicit non-goals:
- Acceptable failure boundary:
- Why someone would adopt it now:

## Control Architecture
- Core layer:
- Model layer:
- Tool layer:
- Memory layer:
- Policy and approval layer:
- Observability and logging layer:
- Portability boundary:

## Covered vs Uncovered Situations
### Covered now
- ...

### Partially covered
- ...

### Not yet covered
- ...

### Intentionally deferred autonomy
- ...

## Failure, Override, and Logging Plan
- Hallucination or factual error handling:
- Tool failure handling:
- Latency or timeout handling:
- Retry and budget enforcement:
- Policy violation handling:
- Sensitive-data handling:
- Failure logging and review loop:

## Feature Prioritization by Business Value
| Capability | Value or trust reason | Cost / control burden | Decision |
| --- | --- | --- | --- |
| ... | ... | ... | Build now / Reserve / Experiment / Avoid |

## Roadmap
### v1.0 — Assisted and reviewable
- Objective:
- User value:
- Technical milestone:
- Commercial milestone:
- Control milestone:

### v2.0 — Controlled autonomy
- Objective:
- User value:
- Technical milestone:
- Commercial milestone:
- Control milestone:

### v3.0 — Scaled governance and economics
- Objective:
- User value:
- Technical milestone:
- Commercial milestone:
- Control milestone:

### Long-term leverage
- Strategic destination:
- What becomes possible later:

## Risks and Assumptions
- Hallucination risk:
- Latency risk:
- Unit-economics risk:
- Observability risk:
- Human-override risk:
- Policy-control risk:
- Data-sensitivity risk:
- Model-portability risk:
- Feedback-loop or memory risk:
- Responsibility or approval risk:

## Next Recommendation
- Most logical next artifact or action:
```

## What Good Looks Like

A strong result makes the reader say:

- I know why AI is necessary here instead of merely fashionable.
- I know whether one assistant is enough or why more coordination is justified.
- I know what the system handles, what still needs humans, and what remains uncovered.
- I understand how cost, latency, and governance shape the roadmap.
- I can explain how failures are observed, overridden, and used to improve the product.
