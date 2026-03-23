---
name: plan-product-review
description: Use when a feature plan already exists and needs a product-value review focused on user benefit, smallest wedge, scope honesty, non-goals, and whether the plan deserves to move forward.
---

# Plan Product Review

Use this skill to challenge a feature plan from the product side before implementation starts.

This is a review skill, not a planning or delivery skill. Its job is to test whether the plan solves a real problem for the right user with an honest scope and clear non-goals.

## Core Contract

- Review an existing plan. Do not start implementation here.
- Stay on product questions: user value, wedge, sequencing, scope, adoption risk, and success definition.
- Do not drift into architecture, test design, observability, or implementation detail. That belongs in engineering review.
- If the "plan" is only a vague idea, stop and route back to discovery or spec work instead of pretending the review can proceed.
- The output must make a decision easier: approve, tighten, cut, defer, or stop.

## When to Use

Use this skill when:
- a feature plan, proposal, or spec draft exists and needs product challenge before build
- the team wants to pressure-test whether the scope matches the stated value
- you need to identify what should be cut, deferred, or named as a non-goal
- there is concern that the plan solves too much, too little, or the wrong user problem
- stakeholders are aligned on the feature name but not on the product wedge

Do not use this skill when:
- there is no actual plan to review yet
- the main need is a full requirements document or acceptance criteria authoring
- the main concern is architecture, failure modes, testability, rollout mechanics, or technical reversibility

## Review Standard

A plan is product-ready only if it can answer all of these:
- Who is the first user or buyer?
- What painful or valuable moment is changing?
- Why is this wedge worth shipping before adjacent ideas?
- What is explicitly out of scope?
- How will we know the plan worked soon after launch?

If the plan cannot answer these clearly, the review should not mask that weakness with polished language.

## Workflow

### Phase 1 — Normalize the plan into product terms

Extract the plan as five short bullets:
- target user
- problem or opportunity
- proposed wedge
- expected user or business outcome
- stated scope limits

If any of these are missing, mark them missing before continuing.

### Phase 2 — Challenge value before scope

Ask:
- what user pain or business opportunity justifies doing this now
- whether the plan improves a repeated, high-friction, high-value moment or only adds surface area
- whether the first user actually has enough urgency to change behavior
- whether success depends on adjacent work the plan quietly assumes

If value is weak or indirect, say so plainly.

### Phase 3 — Pressure-test the wedge

Review whether the wedge is the smallest version that still matters.

Check for:
- a narrow first user rather than "everyone"
- a single moment or workflow rather than an end-to-end platform ambition
- one primary success outcome
- a believable first release that can teach something decisive

Then ask:
- what can be cut without breaking the core promise
- what is bundled only because it feels related
- what fast-follow items are pretending to be v1 requirements

### Phase 4 — Review scope honesty and non-goals

A strong plan names what it will not do.

Look for:
- missing non-goals
- non-goals that are too soft to constrain scope
- hidden expansion paths such as admin tools, settings, migrations, reporting, edge personas, or cross-platform support
- timeline pressure being used to justify ambiguity rather than deliberate cuts

If the plan adds scope without a corresponding cut, call that out as a product risk.

### Phase 5 — Check measurement and decision quality

Review whether the plan includes:
- a short-term success signal
- a likely adoption or activation metric
- a clear failure condition or reason to revisit the wedge
- open questions that genuinely matter before build

Do not demand a full analytics plan here. The bar is whether the team can tell if the wedge mattered.

### Phase 6 — Deliver the review

Return exactly these sections:

### Plan summary
- 3-5 bullets

### What the plan gets right
- 2-5 bullets

### Product risks and weak assumptions
- 3-7 bullets

### Scope cuts or non-goals to add
- 3-7 bullets

### Questions that must be answered before build
- only blocking or scope-changing questions

### Verdict
Use one of these exactly:
- `Proceed with minor tightening.`
- `Tighten the wedge before build.`
- `Reduce scope and rewrite the non-goals.`
- `Stop and return to feature discovery.`

## Failure Modes to Avoid

- Reviewing implementation quality instead of product value.
- Rewriting the whole plan instead of critiquing the one provided.
- Accepting "all users" or "full workflow" as a serious first wedge.
- Praising breadth when the plan really needs cuts.
- Treating unstated non-goals as harmless.
- Giving a positive verdict without naming what would prove the plan wrong.

## Fast Checklist

Use this before finalizing the verdict:
- Is the first user specific?
- Is the moment of value specific?
- Is the wedge smaller than the surrounding vision?
- Are non-goals explicit and constraining?
- Can the team tell soon whether this mattered?
- Did the review stay out of engineering design?
