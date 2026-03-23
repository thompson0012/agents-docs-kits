---
name: feature-discovery
description: Use when a feature idea, change request, or product direction is still fuzzy and the next job is to define the real problem, smallest wedge, and open decisions before writing a spec or starting implementation.
---

# Feature Discovery

Use this skill to turn a fuzzy feature request into a compact discovery artifact that another skill can act on.

The output is not a PRD, requirements doc, or implementation plan. It is the smallest truthful description of what problem might be worth solving, for whom, why now, and where the boundary likely belongs.

## Core Contract

- Stop before full requirements writing. If the user wants acceptance criteria, detailed requirements, or a PRD, hand off to `feature-spec`.
- Stay solution-light. You may name candidate approaches only to compare wedges or expose tradeoffs, not to lock implementation.
- Challenge the request, not just the wording. A stated feature may hide the real problem, the wrong user, or an oversized scope.
- Produce one discovery artifact that makes the next decision easier: proceed to spec, gather evidence, or stop.
- If the request is already a concrete plan, do not redo discovery. Review the plan or route to the right review skill instead.

## When to Use

Use this skill when:
- the user has an idea, complaint, opportunity, or requested change but not a stable problem statement
- a request starts with proposed solution language such as "build", "add", or "we need" without clear user value
- multiple possible user problems or wedges are competing
- the team needs a pre-PRD artifact to align on what is actually being considered
- you need to decide whether the idea deserves specification work at all

Do not use this skill when:
- the main ask is to write a PRD, requirements doc, or acceptance criteria set
- the plan already exists and needs review rather than discovery
- the work is already repo-backed and ready for implementation

## Workflow

### Phase 1 — Capture the request without inheriting its assumptions

Write down only the raw claim:
- what change is being requested
- who seems to want it
- what pain, opportunity, or trigger prompted it
- what evidence exists so far

Then separate:
- **observed signal** — support tickets, usage drop, repeated complaint, missed deal, manual pain, policy need
- **assumed cause** — the story about why this is happening
- **proposed solution** — the feature or change someone jumped to

If the request has no evidence, say so plainly. Lack of evidence does not kill the idea, but it lowers confidence.

### Phase 2 — Reframe the problem before narrowing scope

Create 2-4 candidate framings. Vary at least one of these each time:
- primary user or buyer
- job to be done
- moment in the workflow
- severity or frequency of the pain
- what counts as success

For each framing, ask:
- what user behavior or business outcome would change if this were solved
- what would remain painful even after this shipped
- whether the request is really a feature, a workflow gap, a positioning issue, or an operational problem

Discard any framing that depends on a specific UI, architecture choice, or internal implementation before the problem is clear.

### Phase 3 — Find the smallest credible wedge

Define the narrowest version worth evaluating:
- **target user** — exactly who this is for first
- **trigger moment** — when the need appears
- **core promise** — what gets meaningfully easier, safer, faster, or more likely to succeed
- **success signal** — the earliest observable sign that the wedge matters
- **non-goals** — what this first pass will explicitly not solve

A good wedge is small enough to reject easily and strong enough to matter if it works.

### Phase 4 — Surface constraints and open decisions

Capture only the unknowns that change the next decision:
- missing evidence
- policy or business constraints
- dependency on another team, workflow, or system
- unresolved choice that affects scope or target user
- reason the idea might not deserve a spec yet

Do not expand this into engineering design, delivery sequencing, or acceptance criteria.

### Phase 5 — Produce the discovery artifact

Return a compact artifact with these sections:

### Request in plain language
- 1-2 sentences

### Candidate problem frames
- 2-4 bullets

### Chosen discovery statement
Use this format:

```text
[USER] struggles to [JOB] during [MOMENT], which causes [COST OR RISK].
The smallest wedge worth exploring is [BOUNDARY].
```

### Why this wedge
- 3-5 bullets

### Evidence and confidence
- what evidence exists
- what is inferred
- confidence: low / medium / high

### Non-goals
- 3-5 bullets

### Open decisions
- only decisions that block a spec or invalidate the wedge

### Recommended next step
Use one of these exactly:
- `Proceed to feature-spec.`
- `Gather more evidence before writing a spec.`
- `Stop here. The request is not yet worth specification.`

## Failure Modes to Avoid

- Turning discovery into a full PRD or requirements list.
- Accepting the proposed feature as the problem without challenge.
- Naming a wedge so broad that it is just the roadmap in miniature.
- Skipping non-goals, which guarantees later scope creep.
- Smuggling in engineering decisions under the label of "constraints."
- Claiming confidence without any evidence source.

## Exit Checklist

Before you stop, confirm that the artifact contains:
- one clear problem statement
- one smallest credible wedge
- explicit non-goals
- evidence vs inference called out separately
- a next step that honestly says spec, more discovery, or stop
