---
name: research-assistant
description: Use when the user needs broad, high-quality research, evidence gathering, or an executive briefing and no narrower market or investment research workflow is a better fit.
---

# Research Assistant

Use this skill for broad deep-dive research that must be evidence-led, well structured, and decision-useful.

## Core Standard

Do the full research job, not a shallow skim.
- Prioritize primary and authoritative sources.
- Use search results to find leads; use `fetch` to inspect the actual source before treating a claim as evidence.
- Cross-check material claims across multiple sources when accuracy matters.
- Call out gaps, stale evidence, and unresolved uncertainty instead of papering them over.
- Prefer tables, concise comparisons, and simple visuals only when they reduce cognitive load.

## Workflow

### 1. Frame the question
- Restate the real decision or deliverable.
- Identify what must be known, what is nice to know, and what would change the conclusion.
- Ask focused clarifying questions only when missing information would materially change the research plan.

### 2. Build a research plan
Break the work into concrete lines of inquiry such as:
- background and definitions,
- current state and recent developments,
- quantitative evidence,
- competing viewpoints,
- risks, edge cases, and open questions.

For topics with an active timeline, include at least one recency-focused query with the current year.

### 3. Gather evidence
- Start with `web_search` to discover likely sources.
- Use `fetch` to read the highest-value sources directly.
- Use `read` for local files the user provides.
- Use `task` to parallelize independent subtopics when the research naturally splits by region, theme, entity, or source type.

Each subtopic should capture the fact, why it matters, and the source URL or file path.

### 4. Analyze, do not just collect
When handling data or lists:
- normalize units and categories before comparing them,
- compute ranges, distributions, deltas, or rankings when they matter,
- verify intermediate results before promoting them into conclusions,
- and separate observed facts from interpretation.

### 5. Synthesize for the user
The final output should usually include:
- a direct answer or executive summary,
- the key findings in priority order,
- supporting evidence with citations or source links,
- important caveats and unknowns,
- and recommended next questions or decisions when useful.

## Evidence Rules

### Primary-source tracing
For rankings, official statistics, filings, regulations, or published datasets:
- do not treat search snippets as authoritative,
- trace important claims back to the original publisher when possible,
- and prefer the publisher's own page or document over aggregators.

### Recency
If the topic can change over time, explicitly check for current-year developments that could invalidate older material.

### Honesty
If the evidence is thin, say so. A bounded answer with visible uncertainty is better than a confident synthesis built on weak sources.

## Research for Build Tasks

If the task mixes research with building a report, slide deck, website, or another artifact, separate the phases:
1. research and source gathering,
2. asset or dataset collection if needed,
3. build only after the facts are sufficiently pinned down.

Do not skip from a thin evidence base straight into production work.

## Parallelization Guidance

Parallelize with subagents when the lines of inquiry are independent, for example:
- one subagent per geography,
- one per named company or entity,
- one for quantitative evidence and one for qualitative context.

Have each subagent return structured findings that the parent can combine without re-researching the same ground.