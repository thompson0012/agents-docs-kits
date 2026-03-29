# Financial Analysis Guide

Use supported public-data research tools as a three-step pipeline:
1. `web_search` locates the best public source
2. `fetch` reads the source URL, PDF, HTML page, or JSON endpoint
3. `calc` or local arithmetic turns reported figures into ratios, growth rates, and valuation outputs

Search snippets are discovery aids, not evidence.

## Fetching Financial Statements

### Statement Types

| Type | Contains |
| --- | --- |
| `income` | Revenue, expenses, net income, EPS |
| `balance_sheet` | Assets, liabilities, equity |
| `cash_flow` | Operating, investing, financing cash flows |

### Public-source workflow

1. Resolve the exact company and ticker with `web_search` if needed.
2. Fetch SEC submissions JSON to locate the latest 10-K, 10-Q, or 8-K filing page.
3. Fetch SEC company facts JSON for standardized reported metrics.
4. Fetch the matching investor-relations earnings release or presentation when you need quarter framing, guidance, or KPIs not cleanly exposed in XBRL.
5. Keep the fiscal period end, filing date, and source URL with every number.

### Useful public URLs

- SEC submissions: `https://data.sec.gov/submissions/CIK##########.json`
- SEC company facts: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`
- Filing page or primary filing document from the submissions result
- Official investor-relations earnings release or quarterly-results PDF

### Period discipline

- Annual analysis: anchor every figure to the fiscal year end and filing date
- Quarterly analysis: anchor to the fiscal quarter end plus release or filing date
- TTM analysis: state exactly which four quarters are included

## Ratio Analysis

### Profitability Ratios

Calculate from reported income statement and balance sheet data:

```
Gross Margin = Gross Profit / Revenue
Operating Margin = Operating Income / Revenue
Net Margin = Net Income / Revenue
ROE = Net Income / Shareholders Equity
ROA = Net Income / Total Assets
ROIC = NOPAT / Invested Capital
```

### Liquidity Ratios

```
Current Ratio = Current Assets / Current Liabilities
Quick Ratio = (Current Assets - Inventory) / Current Liabilities
Cash Ratio = Cash / Current Liabilities
```

### Leverage Ratios

```
Debt-to-Equity = Total Debt / Shareholders Equity
Debt-to-EBITDA = Total Debt / EBITDA
Interest Coverage = EBIT / Interest Expense
```

### Calculating ratios

1. Fetch the reported numerator and denominator from the filing, SEC company facts JSON, or the official earnings release.
2. Confirm both figures use the same reporting period and accounting basis.
3. Calculate the ratio locally.
4. Report the ratio with the underlying figures, period end, and source URLs.

Example source routing:
- ROE: net income from the income statement, total stockholders' equity from the balance sheet
- Current ratio: current assets and current liabilities from the balance sheet
- Debt-to-EBITDA: total debt from the balance sheet, EBITDA reconstructed from reported operating data when not shown directly

## Comparable Company Analysis

### Step 1: Identify Peer Group

Identify peers using business model, geography, customer base, size, and capital intensity.

Use `web_search` to confirm:
- official company descriptions and investor-relations pages
- sector and industry classification
- whether the candidate peers report on a comparable basis

Do not build a comp set from ticker familiarity alone.

### Step 2: Build valuation inputs

For each company:
1. Fetch the current quote from the issuer IR stock page or the primary exchange quote page.
2. Record the displayed timestamp, currency, and delay status.
3. Fetch the latest filing or SEC company facts for shares, cash, debt, revenue, book value, and earnings inputs.
4. Calculate equity value, enterprise value, and valuation multiples locally.

For past reference dates, only use a public historical price source if the fetched page exposes the exact date and pricing basis. If you cannot fetch a reliable point-in-time source, say the historical price is unavailable from current supported sources.

### Step 3: Fetch growth metrics

1. Pull at least two comparable reported periods from filings, SEC company facts, or official earnings materials.
2. Standardize period labels across peers before calculating growth.
3. Calculate YoY or CAGR locally.
4. Flag when one peer is using a different fiscal calendar or incomplete period coverage.

### Common Multiples

| Multiple | Formula | Best For |
| --- | --- | --- |
| P/E | Price / EPS | Profitable companies |
| EV/EBITDA | Enterprise Value / EBITDA | Capital-intensive businesses |
| P/S | Price / Revenue per Share | High-growth, unprofitable companies |
| P/B | Price / Book Value | Asset-heavy sectors such as banks or REITs |
| PEG | P/E / EPS Growth Rate | Growth-adjusted valuation |

## DCF Valuation

### Required Inputs

1. **Historical free cash flow** — from reported cash flow statements
2. **Discount rate (WACC)** — calculated from public assumptions or clearly labeled as an estimate
3. **Terminal growth rate** — usually a conservative long-run growth assumption
4. **Projection period** — typically 5-10 years depending on business maturity

### Workflow

1. Fetch 5+ years of reported revenue, operating cash flow, capex, and net income from filings or SEC company facts.
2. Fetch the latest IR earnings release, presentation, or shareholder letter for management guidance and business drivers.
3. Calculate historical free cash flow locally:

```
FCF = Operating Cash Flow - CapEx
```

4. Project future free cash flow from explicit operating assumptions.
5. Discount projected cash flows and terminal value locally.
6. Reconcile enterprise value to equity value using reported cash, debt, and share count from the same reporting date.

### Terminal Value

Gordon Growth Model:

```
Terminal Value = FCF_final * (1 + g) / (r - g)
```

Where:
- `g` = perpetual growth rate
- `r` = discount rate (WACC)

### DCF discipline

- Keep operating assumptions separate from management guidance and separate both from your own scenario inputs.
- Do not mix current market inputs with stale balance-sheet data without saying so.
- If the company does not have stable positive cash flow, say the DCF is highly assumption-sensitive.

## Statistical Analysis

For returns, volatility, correlation, or beta, use a public historical price source only when the fetched source exposes the exact series period and price field you are using.

### Workflow

1. Fix the start date, end date, frequency, and price basis first.
2. Fetch the historical series from a public source that can be cited directly.
3. Calculate locally:

```
Daily Return = (close[i] - close[i-1]) / close[i-1]
Correlation = corr(asset_a_returns, asset_b_returns)
Annualized Volatility = std(daily_returns) * sqrt(252)
Beta = covariance(stock, benchmark) / variance(benchmark)
```

4. Report the exact series source, date range, and whether prices are adjusted or unadjusted.

### Common analyses

- Correlation between assets
- Beta calculation versus a benchmark
- Sharpe ratio
- Portfolio variance
- Moving averages and other technical indicators

## What Not To Claim

Do not claim any of the following unless you fetched a real public source or the user provided the data:
- live brokerage holdings
- private portfolio or watchlist access
- proprietary consensus databases
- private transcript access
- precise historical prices without a fetched point-in-time source
