---
name: finance-markets
description: Use when researching public-market securities, company fundamentals, filings, earnings materials, fund holdings, or macro market data with supported web and fetch tools.
---

# Finance Research Tools

Public-market work needs source discipline. Use `web_search` to find the right source, then use `fetch` to read the source itself before citing numbers.

## Source Hierarchy

Use sources in this order and stop when the highest available source answers the question:

1. **Primary sources** — SEC filings and SEC JSON endpoints, company investor-relations pages, exchange pages, ETF sponsor holdings pages, Treasury/Federal Reserve/BLS/BEA releases
2. **Primary-source mirrors** — issuer-hosted PDFs, earnings releases, shareholder letters, posted presentations, official transcript pages
3. **Secondary sources** — reputable market-data sites or financial press only when the primary source is unavailable or clearly incomplete
4. **Search snippets** — discovery only; never cite the snippet itself as evidence

## Core Workflow

1. **Resolve the entity first.** Confirm the legal name, ticker, exchange, and instrument type before pulling data.
2. **Fix the reference date.** Every answer should be anchored to a date or reporting period.
3. **Route to the right source.** Use [market-data.md](market-data.md) to choose filings, IR pages, sponsor holdings, or macro releases.
4. **Fetch the source itself.** Do not rely on the search result summary when a source URL can be opened directly.
5. **Preserve provenance.** Keep the exact source URL, publication date, and as-of date with each number.
6. **Cross-check when needed.** If a number is surprising, stale, or comes from a secondary source, verify it against a filing, IR page, or another authoritative source.
7. **Report with limits.** Use [reporting.md](reporting.md) and state when data is delayed, estimated, or unavailable.

## Practical Routing Rules

### Company fundamentals
- Prefer SEC filings and SEC XBRL data for revenue, margins, EPS, cash, debt, capex, SBC, buybacks, shares, and segment disclosures.
- Use company IR earnings releases and presentations for management guidance, KPIs, and quarter-specific commentary.
- Use earnings-call transcripts only when the transcript is publicly available from the issuer or another openly accessible source.

### Price and trading context
- For current price or intraday context, prefer the issuer's IR quote page or the primary exchange quote page.
- State the timestamp and whether the quote is delayed.
- For historical performance, use a public historical data source only if the page exposes the exact period and pricing basis; otherwise say the historical series is unavailable from current supported sources.

### Holdings and ownership
- Only analyze holdings when the user provides positions or names a public source that can be fetched.
- For ETFs and mutual funds, use sponsor holdings pages, CSV downloads, fact sheets, or SEC fund filings.
- For institutional ownership, use 13F filings or issuer disclosures.
- For insider trading, use Forms 3, 4, and 5.
- Do **not** imply brokerage access, private watchlist access, or saved portfolio memory.

### Macro and rates
- Prefer official releases: Treasury for yields, Federal Reserve for policy and series pages, BLS for labor and inflation, BEA for GDP and income.
- Quote the release date and the period measured, not just the publication date.

## When Search Is Not Enough

Search is for locating sources. It is not the evidence layer.

Use `web_search` to find:
- the correct SEC filing or filing index page
- the investor-relations page for a company or fund sponsor
- the official macro release or data series page
- public transcript, presentation, or factsheet URLs

Then use `fetch` to read the source content directly.

## Multi-Company Research

When the question covers several companies or multiple independent evidence buckets, split work with `task` so each branch reads its own source set. Standardize the fields first so comparisons stay honest.

Good split:
- one task per company for peer comps
- one task for financial statements, one for price context, one for industry context

Bad split:
- several tasks using different definitions of revenue, margin, or reporting periods

## Common Failure Modes

- Using a search snippet instead of the filing or IR page behind it
- Mixing reporting periods across peers
- Treating delayed quotes as real-time prices without saying so
- Presenting estimated or consensus figures as reported results
- Claiming portfolio analysis without user-provided holdings or a public holdings source
- Relying on a transcript or news article when the filing already answers the question

## Quick Start

- Need source routing or example URLs: [market-data.md](market-data.md)
- Need output structure, tables, and citation rules: [reporting.md](reporting.md)
