# Agent Practices Category Map

This repository's first-party suite currently contains these live skills under `templates/base/.agents/skills/`.

## Orchestration and Continuity

- `context-compaction` — compact session state for handoff or continuation
- `self-cognitive` — verify reasoning, run retros, and extract repeatable workflows

## Reasoning and Strategy

Route through `using-reasoning` when the request could plausibly fit more than one of these:

- `using-reasoning/thinking-ground` — calibrate reasoning state before analysis
- `using-reasoning/problem-definition` — turn a messy situation into one clean problem statement
- `using-reasoning/dynamic-problem-solving` — analyze a clearly defined complicated problem through multiple lenses
- `using-reasoning/domain-expert-consultation` — produce a structured advisory memo or expert recommendation
- `using-reasoning/strategic-foresight` — run scenarios around a concrete external signal or threshold

## Prompt Artifact Creation

- `meta-prompting` — design or optimize a production-grade prompt artifact

## Commercial Reality Testing

- `startup-pressure-test` — pressure-test a startup idea with market, funnel, and runway realism

## Sales Workflow Routing

Route through `using-sales` when the request could plausibly fit more than one of these:

- `using-sales/account-research` — gather company, contact, and qualification intelligence before sales action
- `using-sales/sales-call-prep` — build a prep brief for an upcoming sales conversation
- `using-sales/sales-draft-outreach` — draft personalized outbound email or LinkedIn outreach


## Marketing Workflow Routing

Route through `using-marketing` when the request could plausibly fit more than one of these:

- `using-marketing/marketing-performance-analytics` — measure performance, choose KPIs, and diagnose funnel or attribution issues
- `using-marketing/marketing-competitive-analysis` — compare competitors, messaging, positioning, and battlecards
- `using-marketing/content-creation` — draft or structure marketing content artifacts across channels


## Research Workflow Routing

Route through `using-research` when the request could plausibly fit more than one of these:

- `using-research/investment-research` — research stocks, theses, investor styles, and portfolios
- `using-research/market-research` — run framework-based market sizing, competitive, or strategic market research
- `using-research/research-assistant` — deliver broad deep-dive research and synthesis when no narrower child fits

## Finance Workflow Routing

Route through `using-finance` when the request could plausibly fit more than one of these:

- `using-finance/finance-audit-support` — support SOX, internal-control, workpaper, and deficiency-evaluation work
- `using-finance/finance-markets` — handle finance data tools, connector patterns, and structured market-data retrieval


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
- ambiguous marketing help across analytics, competitor analysis, or content creation -> `using-marketing`
- ambiguous research help across broad research, market frameworks, or investment analysis -> `using-research`
- ambiguous finance help across audit support or finance-data tooling -> `using-finance`
