---
name: meta-prompting
description: Use when the requested deliverable is a prompt artifact, system prompt, prompt template, or prompt architecture that must be reliable, testable, and shaped for a specific workflow or runtime.
---

# Meta-Prompting

Use this skill when the job is to design, repair, or evaluate the prompt itself. The output is a copyable prompt artifact, not the task answer.

## Boundary

Use `prompt-augmentation` instead when the real need is to enrich a sparse prompt, generate prompt variants, build positive or negative prompts, or expand text, image, or video generation prompts without redesigning the surrounding prompt architecture.

## Discovery

Infer or collect only what changes the design:

- objective and success criteria
- target workflow or runtime constraints that materially affect structure
- hard boundaries, non-goals, and likely failure modes
- required output shape, if the caller already knows it

Ask follow-up questions only when the missing detail changes the prompt architecture.

## Workflow

### 1. Choose the lightest structure

Use the smallest prompt shape that can survive the task:

- direct instruction for clear, low-risk work
- role plus rubric when style, policy, or decision quality matters
- examples or counter-examples when behavior is easy to misread
- branching or comparison structure when the model must weigh options
- explicit output contract when downstream consumers depend on the format

Do not add scaffolding that the use case does not earn.

### 2. Draft the prompt

Include only the sections that help:

- role or operating stance, if needed
- task and scope
- context the model genuinely needs
- constraints and non-goals
- process checks or evaluation rubric when reliability matters
- output contract
- examples only when they reduce ambiguity

Reasoning scaffolding is a design tool, not a disclosure requirement. Keep internal rigor and visible output separate unless the user explicitly wants the reasoning exposed.

### 3. Stress-test the draft

Before delivering, silently check:

- what the target system is most likely to misunderstand
- where scope drift or over-answering will happen
- which assumptions are still implicit
- whether any section can be removed without reducing reliability
- whether the output contract matches the caller's real need

Patch the prompt until the structure matches the risk.

## Delivery

Return:

1. a brief prompt strategy note explaining the chosen structure
2. the final copyable prompt artifact with clearly marked variables
3. any critical usage notes or known failure edges that the caller should watch

Match the artifact format to the user or runtime. Do not force one syntax as universal truth.

## Quality Bar

A good prompt artifact:

- solves the real task rather than the surface phrasing
- makes success and failure legible
- states boundaries explicitly
- stays as simple as the job allows
- is ready to copy without hidden assumptions
