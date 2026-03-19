# Market Data Guide

Use supported research tools as a two-step pipeline:
- `web_search` finds the source
- `fetch` reads the source URL, PDF, HTML page, or JSON endpoint

Search snippets are leads, not evidence.

## Reference Date Discipline

Every finance answer needs a reference date.

| Question Type | Anchor |
| --- | --- |
| Current quote or market move | Quote timestamp and whether data is delayed |
| Reported fundamentals | Fiscal period end plus filing or release date |
| Guidance / management commentary | Date of the earnings release, transcript, or presentation |
| Holdings | Filing date or sponsor holdings "as of" date |
| Macro data | Release date and measured period |

Do not mix dates across companies without saying so.

## Source Routing

| Need | Best Source | Notes |
| --- | --- | --- |
| Reported income statement / balance sheet / cash flow | SEC filings or SEC XBRL company facts | Best for reported numbers and point-in-time reproducibility |
| Filing history / accession numbers | SEC submissions JSON or filing index pages | Use to locate the right 10-K, 10-Q, 8-K, DEF 14A, 13F, Form 4, N-PORT, etc. |
| Earnings release, presentation, shareholder letter | Company investor-relations site | Best source for guidance, KPIs, and quarter framing |
| Earnings transcript | Public issuer transcript or openly accessible transcript page | If unavailable publicly, say so rather than inventing access |
| Current stock quote | Issuer IR stock page or primary exchange quote page | State timestamp and delay status |
| ETF or fund holdings | Sponsor holdings page / downloadable CSV / fact sheet / SEC fund filing | Prefer sponsor holdings page when current composition matters |
| Institutional ownership | SEC 13F filings or issuer disclosure pages | Distinguish filer date from report period |
| Insider trading | SEC Forms 3, 4, and 5 | Use filing date and transaction date separately |
| Rates, inflation, labor, GDP | Treasury, Federal Reserve, BLS, BEA | Prefer the official release or series page |

## Public URLs That Work Well With `fetch`

### SEC company facts
Use for standardized reported fundamentals.

- Pattern: `https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json`
- Example: `https://data.sec.gov/api/xbrl/companyfacts/CIK0000320193.json`

Useful for:
- revenue, net income, EPS, shares outstanding
- cash, debt, equity
- capex, operating cash flow, free cash flow inputs

### SEC submissions
Use to find the filing history and accession numbers for a company.

- Pattern: `https://data.sec.gov/submissions/CIK##########.json`
- Example: `https://data.sec.gov/submissions/CIK0000320193.json`

Useful for:
- latest 10-K / 10-Q / 8-K
- proxy statements
- insider and ownership filings

### Filing pages
Once you have the filing accession number or filing page from submissions, fetch the filing page or linked primary document. Prefer the filing itself over summaries.

### Investor-relations pages
Search for the issuer's official IR site when you need:
- earnings releases
- presentations and shareholder letters
- KPI callouts not cleanly exposed in XBRL
- official stock quote pages hosted by the issuer

Good search patterns:
- `[company] investor relations earnings release`
- `[company] investor relations quarterly results pdf`
- `[company] investor relations stock information`

### ETF and fund holdings
Search the sponsor site first.

Good search patterns:
- `[fund name] holdings csv`
- `[ticker] fund holdings pdf site:[sponsor-domain]`
- `[fund name] portfolio holdings site:[sponsor-domain]`

Prefer the sponsor page or download over third-party holdings summaries.

### Macro sources
Use official pages and releases:
- U.S. Treasury for yields and debt issuance
- Federal Reserve for policy statements and series pages
- BLS for CPI, PPI, payrolls, unemployment
- BEA for GDP, PCE, personal income

## Workflows by Question Type

### 1. Public-company fundamentals
1. Resolve company name and ticker with `web_search` if needed.
2. Fetch SEC submissions to locate the latest relevant filing.
3. Fetch SEC company facts for standardized metrics.
4. Fetch the matching IR earnings release or presentation for management commentary and guidance.
5. Report the number with period end, filing date, and source URL.

### 2. Earnings deep-dive
1. Search the official IR page for the quarter's earnings release, deck, and webcast materials.
2. Fetch the release and presentation first.
3. If a public transcript exists, fetch it; otherwise say the transcript is not publicly accessible from current sources.
4. Separate **reported results**, **guidance**, and **management commentary** so they do not blur together.

### 3. Quote or trading context
1. Search the issuer IR stock page or primary exchange page.
2. Fetch the quote page.
3. Record the exact timestamp, currency, and delay status shown on the page.
4. If the page lacks a clear timestamp, label the quote as unverified and avoid overstating precision.

### 4. Portfolio, fund, or ownership analysis
1. If the user gives holdings, use them.
2. If the user names a fund, manager, or politician, fetch the public holdings source that actually exists.
3. If no holdings are provided and no public source is named, ask for tickers and weights instead of implying private access.
4. Distinguish clearly between:
   - user-provided holdings
   - fund holdings
   - 13F institutional positions
   - insider transactions

### 5. Macro and rates context
1. Search the official release or series page.
2. Fetch the release itself.
3. Cite both the measurement period and the publication date.
4. When a later revision exists, prefer the latest official revision and say that the series was revised.

## Cross-Checks

Cross-check when:
- the figure is material to the conclusion
- the source is secondary rather than primary
- peers show different period coverage
- the value appears to conflict with prior reported numbers

Common cross-check pairs:
- SEC filing vs IR earnings release
- sponsor holdings page vs fund fact sheet
- issuer quote page vs exchange quote page
- macro release vs series page

## What Not To Claim

Do not claim any of the following unless the user provides the data or you fetch a real public source:
- live brokerage holdings
- a saved portfolio or watchlist
- proprietary analyst consensus databases
- private transcript access
- point-in-time historical prices you cannot source directly
