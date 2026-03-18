# Agent Practices Category Map

This repository's first-party suite currently contains these live skills under `templates/base/.agents/skills/`.

## Orchestration and Continuity

- `context-compaction` — compact session state for handoff or continuation
- `self-cognitive` — verify reasoning, run retros, and extract repeatable workflows

## Reasoning and Strategy

Route through `using-reasoning` when the request could plausibly fit more than one of these:

- `thinking-ground` — calibrate reasoning state before analysis
- `problem-definition` — turn a messy situation into one clean problem statement
- `dynamic-problem-solving` — analyze a clearly defined complicated problem through multiple lenses
- `domain-expert-consultation` — produce a structured advisory memo or expert recommendation
- `strategic-foresight` — run scenarios around a concrete external signal or threshold

## Prompt Artifact Creation

- `meta-prompting` — design or optimize a production-grade prompt artifact

## Commercial Reality Testing

- `startup-pressure-test` — pressure-test a startup idea with market, funnel, and runway realism

## Sales Workflow Routing

Route through `using-sales` when the request could plausibly fit more than one of these:

- `account-research` — gather company, contact, and qualification intelligence before sales action
- `sales-call-prep` — build a prep brief for an upcoming sales conversation
- `sales-draft-outreach` — draft personalized outbound email or LinkedIn outreach


## Design Systems and Visual Prototyping

- `generating-design-tokens` — turn brand inputs into a design token spec or brand system
- `liquid-glass-design` — implement or evaluate experimental liquid-glass UI effects in the browser

## Routing Rule of Thumb

Ask first: what is the primary artifact needed?

- compacted state -> `context-compaction`
- audit or retro -> `self-cognitive`
- prompt -> `meta-prompting`
- startup simulation -> `startup-pressure-test`
- design token spec -> `generating-design-tokens`
- liquid-glass implementation note -> `liquid-glass-design`
- analytical framing, calibration, advisory judgment, or scenario reasoning -> `using-reasoning`
- ambiguous sales help across research, meeting prep, or outreach -> `using-sales`
