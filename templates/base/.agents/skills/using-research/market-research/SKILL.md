---
name: market-research
description: Use when analyzing a market, industry, company, or technology with strategy frameworks and source-backed web research.
---

# Market Research

Use `web_search` for breadth, `fetch` for the source itself, and `task` for independent research branches. Search result snippets are discovery aids; the report should cite fetched sources.

**Critical:** Always deliver a complete report with explicit limitations. Missing data should narrow the claims, not stop the analysis.

## Supported Tools

- `web_search` — locate relevant sources, recent developments, and candidate primary materials
- `fetch` — read the actual article, filing, PDF, transcript, or JSON endpoint
- `task` — parallelize independent framework dimensions
- `write` — save the final markdown report when the task calls for a file deliverable

## Phase 1: Framework Detection

Parse the user's message to identify the subject and the best-fit framework. Check for explicit framework names first, then keyword matches, then infer from intent.

| Framework | Keywords | Example Intents |
| --- | --- | --- |
| PESTEL Analysis | pestel, macro-environmental, political, economic, social, technological | "Biggest external forces affecting [industry]?" |
| Technology Adoption / S-Curve | s-curve, adoption curve, diffusion, hype cycle | "Where is [technology] on the adoption curve?" |
| Porter's Five Forces | porter, five forces, buyer power, barriers to entry, substitutes | "Competitive dynamics in [industry]?" |
| Competitive Benchmarking | competitive landscape, benchmarking, compare the top | "Compare top players in [category]" |
| Perceptual Mapping | perceptual map, positioning map, brand positioning | "How do consumers perceive [brands] on [dimensions]?" |
| BCG Matrix | bcg matrix, stars, cash cows, question marks | "Classify [company]'s business units" |
| SWOT Analysis | swot, strengths, weaknesses, opportunities, threats | "[Company]'s strengths and weaknesses?" |
| Business Model Canvas | business model canvas, value proposition, revenue streams | "How does [company] make money?" |
| Value Chain Analysis | value chain, primary activities, support activities | "Map [company]'s value chain" |
| Ansoff Matrix | ansoff, market penetration, product development, diversification | "Where is [company]'s growth coming from?" |
| TAM / SAM / SOM | tam, sam, som, market sizing | "How big is the market for [product]?" |
| Jobs to Be Done (JTBD) | jobs to be done, jtbd, switching triggers | "Why do customers buy [product]?" |

If the request is too vague, ask directly for the missing subject, geography, company, or timeframe.

## Phase 2: Clarification

Only ask for missing required inputs.

| Framework | Required | Optional |
| --- | --- | --- |
| PESTEL | industry/sector, geography | timeframe, focal company |
| S-Curve | technology or product category | segment, geography |
| Porter's Five Forces | industry, geography | sub-segment |
| Competitive Benchmarking | market or product category | specific companies, dimensions |
| Perceptual Mapping | category, two axes | brands, geography |
| BCG Matrix | company, business units | time period |
| SWOT | company or product | timeframe |
| Business Model Canvas | company | emphasis areas |
| Value Chain | company | comparison company |
| Ansoff Matrix | company | time period, initiative |
| TAM / SAM / SOM | product/service, target market | methodology, segment |
| JTBD | buyer persona or product category | industry context |

## Phase 3: Research Orchestration

### Core Rules

1. Start broad with `web_search`, then fetch the best sources.
2. Prefer primary sources whenever they exist.
3. Treat search snippets as leads, not citations.
4. Record the publication date, geography, and source URL for every material claim.
5. If the best available evidence is secondary, say that clearly.

### Source Priority

Use the strongest available source for each claim:

1. Government data and regulatory filings
2. Company filings, investor-relations pages, earnings materials, and official product pages
3. Industry associations, standards bodies, and public survey owners
4. Reputable press or analyst commentary

### Parallelization Strategy

Use `task` for frameworks whose dimensions are independent:

| Framework | Parallel Strategy |
| --- | --- |
| PESTEL | One task per dimension |
| Porter's Five Forces | One task per force |
| Competitive Benchmarking | One task per competitor |
| Perceptual Mapping | One task per brand |
| BCG Matrix | One task per business unit |
| SWOT | One task per quadrant |
| Value Chain | One task for primary activities, one for support activities |
| Ansoff Matrix | One task per quadrant |
| JTBD | One task each for functional jobs, emotional/social jobs, and switching triggers |

Keep these sequential because later sections depend on earlier ones:
- TAM / SAM / SOM
- Business Model Canvas
- S-Curve when the adoption stage depends on the evidence gathered in order

### Primary-Source Tracing

For important figures, trace the number back to the source that produced it:
- market size -> data owner, filing, or government release
- company revenue or segment data -> filing or earnings material
- product positioning claim -> official product page, pricing page, or sourced survey
- adoption data -> survey owner, regulator, or standards body

If the trail breaks, say the claim is secondary rather than presenting it as settled fact.

## Phase 4: Report

The markdown report is the primary deliverable.

### Report Structure

1. `# [Framework]: [Subject]`
2. **Executive summary** — 2-3 paragraphs, lead with the most important conclusion
3. **Framework body** — substantive sourced sections, not just bullets
4. **Conclusion** — restate the main finding, key uncertainties, and what to watch next

### Citation Rules

- Cite the fetched URL directly in the report
- Put the citation next to the claim it supports
- Include the publication date or reporting period when it matters
- Distinguish clearly between reported facts, management claims, survey evidence, and interpretation

### Visualization Guidance

Generate a chart only when it makes the finding easier to understand:
- market share or ranked comparisons
- time-series trends
- framework-required visuals like perceptual maps or BCG-style matrices

Skip charts when the evidence is sparse, purely qualitative, or better expressed as a table.

## Framework-Specific Notes

- **PESTEL:** cite the actual law, policy, or data release rather than a commentary article when possible.
- **Five Forces:** name actual buyers, suppliers, substitutes, and entrants instead of describing forces generically.
- **Competitive Benchmarking:** keep metrics comparable across companies and time periods.
- **Perceptual Mapping:** ground axes in measured perception or clearly defined criteria, not vibe.
- **BCG Matrix:** use relative market share and market growth consistently.
- **TAM / SAM / SOM:** show the narrowing logic explicitly and separate assumptions from sourced inputs.
- **JTBD:** distinguish what customers say from what you infer.

## Common Failure Modes

- citing a search snippet instead of the fetched source
- mixing geographies or time periods in one comparison without disclosure
- inflating weak secondary evidence into a firm conclusion
- using a framework label without actually answering the framework's core question
- stopping early because one dimension has thin evidence instead of reporting the gap honestly
