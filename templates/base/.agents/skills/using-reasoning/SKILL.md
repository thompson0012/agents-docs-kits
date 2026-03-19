---
name: using-reasoning
description: Use when a request is analytical and could plausibly fit more than one reasoning child such as state calibration, problem framing, scenario planning, advisory analysis, or multi-lens problem solving.
---

# Using Reasoning

Use this router when the task is analytical, strategic, or diagnostic and more than one reasoning skill could fit.

Do not analyze the problem fully here. Select the narrowest correct reasoning skill, then hand off.

## Core Contract

- Choose exactly one primary reasoning skill or decide that no reasoning skill is needed.
- Prefer the earliest boundary violation in the chain: distorted state before vague problem, vague problem before analysis, concrete signal before generic advisory, advisory before general multi-lens analysis.
- Allow only explicit handoffs listed below.
- If the request does not benefit from a reasoning skill, say so and answer directly.
- Use `references/children.json` as the source of truth for child boundaries, nested targets, install hints, and companion recommendations.

## Decision Tree

Apply these checks in order.

### 1. Is the reasoning state distorted?
Route to `using-reasoning/thinking-ground` when one or more of these are present:
- validation seeking or obvious attachment to a preferred answer
- urgency inflated beyond the evidence or deadline
- looping without real update
- analysis that sounds polished but hollow
- identity defense mixed into the reasoning

### 2. Is the problem still unclear?
If the user cannot state the problem clearly and solution-neutrally in one or two sentences, route to `using-reasoning/problem-definition`.

Typical signs:
- symptom descriptions without a clean problem statement
- multiple candidate problems competing for attention
- proposed solutions appearing before the real problem is stable

### 3. Is there a concrete external signal with uncertainty about implications?
Route to `using-reasoning/strategic-foresight` when both are true:
- a concrete signal, threshold, launch, policy move, pricing shift, hardware curve, or scientific result is present
- the user wants implications, scenarios, winners/losers, second-order effects, or indicators to watch

### 4. Does the user want a structured advisory deliverable?
Route to `using-reasoning/domain-expert-consultation` when the user wants:
- expert consultation
- strategic recommendation
- decision memo
- tradeoff evaluation
- structured advisory brief

Use this only when the problem is already clear enough to advise on honestly.

### 5. Is the problem clear and complicated enough for lens analysis?
Route to `using-reasoning/dynamic-problem-solving` when the problem is already defined and the user wants rigorous analysis, challenge, diagnosis, or decision support.

### 6. No reasoning skill
If none of the above fits cleanly, do not force a reasoning skill.

## Allowed Handoffs

- `using-reasoning/thinking-ground -> using-reasoning/problem-definition`
- `using-reasoning/thinking-ground -> using-reasoning/dynamic-problem-solving`
- `using-reasoning/thinking-ground -> using-reasoning/domain-expert-consultation`
- `using-reasoning/thinking-ground -> using-reasoning/strategic-foresight`
- `using-reasoning/problem-definition -> using-reasoning/dynamic-problem-solving`
- `using-reasoning/problem-definition -> using-reasoning/domain-expert-consultation`
- `using-reasoning/problem-definition -> using-reasoning/strategic-foresight`
- `any reasoning skill -> self-cognitive` after completion or before a risky commitment when verification is now the main need

## Forbidden Defaults

- Do not route to `using-reasoning/dynamic-problem-solving` before a vague problem is framed.
- Do not route to `using-reasoning/domain-expert-consultation` when the real issue is still problem definition.
- Do not route to `using-reasoning/strategic-foresight` without a concrete external signal.
- Do not run multiple primary reasoning skills in parallel for the same request.

## References

- `references/children.json`


## Router Output

Return one of these forms and then invoke the selected skill if needed:

- `Route to using-reasoning/thinking-ground.`
- `Route to using-reasoning/problem-definition.`
- `Route to using-reasoning/strategic-foresight.`
- `Route to using-reasoning/domain-expert-consultation.`
- `Route to using-reasoning/dynamic-problem-solving.`
- `Install <child-path>, then route to <child-path>.`
- `No reasoning skill needed; answer directly.`

Add one sentence explaining why the selected route is the narrowest correct fit.

## Failure Modes to Avoid

- mistaking stress or urgency for a clearly framed problem
- treating a proposed solution as evidence that the problem is already defined
- choosing advisory output when scenario planning is the actual need
- choosing multi-lens analysis when the user really needs a single problem statement first
