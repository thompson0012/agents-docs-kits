---
name: investment-research
description: Use when evaluating a stock, ETF, thesis, investor style, or portfolio question that needs source-backed public-market research from primary materials.
---

# Investment Research Workflows

Ground every conclusion in fetched source material. Search results help locate evidence; they are not the evidence.

Apply the same source-routing, reference-date discipline, and reporting conventions used by the companion `finance-markets` skill under `.agents/skills/using-finance/finance-markets/`.

End investment responses with a brief disclaimer: *This is research and analysis only, not personalized financial advice.*

## Classification

Classify the user's query into one of four research modes:

| Signal | Mode |
| --- | --- |
| Screening criteria, filtering, ranking, or "find stocks that..." | **Find** |
| Specific belief or thesis: "should I buy X?", "is X overvalued?" | **Think** |
| Named investor or investing style | **Imitate** |
| Holdings, diversification, concentration, correlation, or rebalancing | **Analyze** |

If the query is ambiguous, ask one clarifying question.

## Find

**Goal:** Filter a public-market universe by explicit criteria and surface the strongest candidates.

### Steps

1. **Clarify criteria** — Capture hard filters (market cap, geography, sector, profitability) and ranking metrics (FCF yield, growth, margins, leverage).
2. **Build the universe honestly** — Use a universe the user provides, a named ETF's sponsor holdings page, a public index constituent page, or another explicit public list. Do not pretend you can scan the entire market from private databases you do not have.
3. **Collect comparable fields** — For the candidate list, fetch the same reporting period and source type for every name: filings for fundamentals, IR pages for guidance, quote pages for current market context.
4. **Rank on stated metrics** — Apply the user's filters, then rank on the primary metric. If the dataset is partial, say so.
5. **Deep-dive the top names** — For the top 5-10 names, fetch a second layer of evidence: filing details, earnings materials, and any source-backed bear cases.
6. **Present** — Use a ranked table plus 2-3 bullets per top name explaining why it screened well and what could invalidate the result.

Use `task` when evaluating several independent tickers so each branch reads its own filings and IR materials.

## Think

**Goal:** Pressure-test a specific investment thesis with explicit evidence for and against.

### Phase A: Frame

1. Restate the thesis in one sentence: asset, belief, time horizon, and expected outcome.
2. Ask 1-2 clarifying questions only if the time horizon, catalyst, or disconfirming evidence threshold is unclear.
3. Define the evidence buckets you need before searching: fundamentals, guidance, price context, and competitive or macro context.

### Phase B: Research

4. **Financials** — Pull reported numbers from filings or SEC company facts across a consistent period.
5. **Management commentary** — Pull earnings releases, shareholder letters, decks, and public transcripts if available.
6. **Price context** — Pull current quote context from issuer or exchange pages and historical context only from a source that exposes the relevant period clearly.
7. **Industry context** — Use `web_search` to locate primary or near-primary sources on competitors, regulation, demand signals, and macro drivers, then `fetch` those sources.

### Phase C: Pressure Test

8. List the thesis assumptions explicitly.
9. For each assumption, gather confirming evidence and counter-evidence.
10. Separate **reported fact**, **management claim**, and **analyst or press interpretation** so the user can see which layer supports the thesis.
11. If valuation is involved, show the assumption bridge from operating inputs to the implied outcome.

### Phase D: Conclude

12. Deliver a structured verdict:
   - **Thesis strength:** Strong / Moderate / Weak
   - **Key supporting evidence** (3-5 bullets)
   - **Key risks** (3-5 bullets)
   - **What would change the view**
13. Offer a follow-up checklist the user can revisit after the next earnings release, filing, or macro catalyst. Do not promise automated monitoring unless the harness actually provides it.

## Imitate

**Goal:** Evaluate a security or generate ideas through the lens of a named investor's philosophy.

### Steps

1. **Identify investor** — Match the user's request to [investor-profiles.md](investor-profiles.md). If none is named, ask which investor or style to use.
2. **Read the profile** — Load the investor's quantitative preferences and qualitative principles.
3. **Pick a path:**
   - **Evaluate a specific name** — Score the company against the investor's criteria using filings, IR materials, and market context.
   - **Generate ideas** — Run a bounded Find workflow using that investor's criteria as filters.
4. **Present** as a scorecard:

   | Criterion | Threshold | Actual | Verdict |
   | --- | --- | --- | --- |
   | ROE | >15% | 22% | Pass |
   | Debt/Equity | <0.5 | 0.3 | Pass |

5. Add a short qualitative section explaining where the fit depends on judgment rather than clean reported data.

## Analyze

**Goal:** Analyze a portfolio's composition, risk concentrations, and possible improvements.

### Steps

1. **Collect holdings truthfully** — Use tickers and weights the user provides, or fetch a real public holdings source the user names (for example a fund sponsor page or 13F filing). Do not imply brokerage connectivity, saved memory, or private watchlist access.
2. **Fetch supporting data** — Pull company profiles, reported fundamentals, and current quote context for each holding from public sources.
3. **Run the analysis that the data supports**:
   - **Always possible:** concentration, sector mix, geography mix, valuation mix, overlap against a public benchmark list
   - **Only when historical prices are actually sourced:** correlation, beta, volatility, drawdown, Sharpe-style metrics
4. **Flag issues** — over-concentration, sector skew, duplicated exposures, valuation extremes, or data gaps that block a stronger conclusion.
5. **Suggest adjustments** — rebalancing ideas, diversification gaps, and questions the user should answer before trading.

## Cross-Cutting Patterns

### Backtesting

When evaluating a strategy historically, temporal integrity is a hard constraint.

1. Insert a censor gap between the decision date and the evaluation window.
2. Use only data that would have been available on that decision date.
3. If you cannot prove point-in-time availability, say so and stop rather than leaking future information.

### Source Discipline

- Primary source first
- Use `fetch` on the actual page, filing, PDF, or JSON endpoint
- Label delayed or estimated data
- Keep reporting periods aligned across comparisons
- State what you could not verify directly

### Disclaimer

End every investment research response with:

*This is research and analysis only, not personalized financial advice. Consult a qualified financial advisor before making investment decisions.*
