---
name: meta-prompting
description: Use when the user wants a prompt, system instruction set, or prompt architecture that must be reliable, testable, and tailored to a specific runtime or workflow.
---

# Meta-Prompting

Use this skill for non-trivial prompt work where structure matters more than a quick rewrite.

## Required Inputs

Collect the minimum information needed before finalizing:
- **Use case** — what the target system must accomplish
- **Target runtime** — model, agent, or platform constraints that materially affect prompt shape
- **Success metric** — what good output looks like
- **Constraints** — policy boundaries, tone, output format, refusal rules, latency limits, or token limits

If a missing input changes the design, ask focused follow-up questions before drafting.

## Workflow

### 1. Discovery
- Remove ambiguity from the task.
- Identify edge cases, likely failure modes, and refusal boundaries.
- Decide whether the user needs reliability, creativity, or a deliberate balance.

### 2. Prompt Architecture
Choose the lightest structure that will survive real use:
- **Direct instruction** — straightforward tasks with low ambiguity
- **Reasoning scaffolding** — reasoning-heavy work where internal rigor matters
- **Branching plans** — exploration, option comparison, or planning
- **Role and rubric structure** — style-critical or policy-sensitive outputs
- **Examples and counter-examples** — when behavior needs anchoring

Do not add scaffolding that the use case does not earn.

### 3. Draft
Build the prompt with explicit sections for:
- role or persona, if needed
- task definition
- constraints and non-goals
- required process or checks
- output format
- examples only when they materially reduce ambiguity

### 4. Stress Test
Before delivering, silently pressure-test the draft:
- What will the target system misunderstand?
- Where will it over-answer, hedge, or ignore a boundary?
- What assumptions are still implicit?
- Can any section be removed without reducing reliability?

Patch the draft until the structure matches the risk.

## Delivery Format

Return two parts:

### Prompt strategy
Briefly explain the chosen structure and why it fits the use case.

### Final prompt
Provide a copyable prompt artifact with clearly marked variables for the user to fill in.

## Quality Bar

A good prompt:
- matches the user's real objective rather than the surface wording,
- makes success and failure legible,
- states constraints explicitly,
- avoids unnecessary verbosity,
- and is ready to use without hidden assumptions.

## When Not to Use

Skip this skill for:
- a simple factual answer,
- a minor copy edit,
- or a one-line rewrite that does not need architectural thinking.