---
name: using-research
description: Use when a research request could plausibly need broad deep-dive research, market-framework analysis, or investment-oriented research and the agent must choose the narrowest child skill first.
---

# Using Research

Use this router when the request is research-heavy and more than one research child skill could fit.

Do not perform the full child workflow here. Select the narrowest correct research skill, then hand off.

## Core Contract

- Choose exactly one primary child skill or decide that no research skill is needed.
- Prefer the most domain-specific research artifact first: investment research before market-framework research before broad general research.
- Use `references/children.json` as the source of truth for child boundaries, nested targets, install hints, and companion recommendations.
- If the best child is missing, say to install it rather than quietly doing weaker work under the wrong skill.
- Do not route to multiple sibling research skills in parallel for one request.

## Decision Order

Apply these checks in order.

### 1. Is the main need investment-oriented research?
Route to `using-research/investment-research` when the request is about a stock, portfolio, investment thesis, investor lens, or public-company analysis.

Typical signs:
- ticker, company valuation, thesis, buy/sell, portfolio, holdings, or investor-style language
- request for screening, thesis pressure-testing, or portfolio analysis
- need for research grounded in finance data and market tools

### 2. Is the main need market-framework or market-sizing research?
Route to `using-research/market-research` when the request is about market sizing, frameworks such as PESTEL or Porter's Five Forces, competitive benchmarking, JTBD, business model canvas, or structured market analysis.

Typical signs:
- TAM, SAM, SOM, market size, five forces, SWOT, PESTEL, JTBD, perceptual map, value chain, or benchmarking language
- request for a market report or framework-driven strategic research artifact
- need for premium connector-first market evidence and structured report output

### 3. Is the main need a broad deep-dive research brief?
Route to `using-research/research-assistant` when the user needs general, institutional-grade research and synthesis that is not specifically market-framework work or investment research.

Typical signs:
- deep research, comprehensive briefing, evidence gathering, or decision support without a narrower family fit
- request spans domain knowledge, source gathering, synthesis, and executive communication
- the artifact is a broad research deliverable rather than a framework-specific analysis

### 4. No research skill
If none of the above fits cleanly, do not force a research skill.

## Router Output

Return one of these forms and then invoke the selected child if needed:

- `Route to using-research/investment-research.`
- `Route to using-research/market-research.`
- `Route to using-research/research-assistant.`
- `Install <child-path>, then route to <child-path>.`
- `No research skill needed; answer directly.`

Add one sentence explaining why the selected child is the narrowest correct fit.

## References

- `references/children.json`

## Failure Modes to Avoid

- routing every research request to the broadest generalist child
- doing broad research when the user clearly needs a market framework or investment thesis workflow
- forcing market-framework research onto an investment question because both mention analysis
- silently downgrading to another child when the best one is missing
