---
name: using-finance
description: Use when a finance request could plausibly need finance-data tool patterns or audit-control support and the agent must choose the narrowest child skill first.
---

# Using Finance

Use this router when the request is finance-related and more than one finance child skill could fit.

Do not perform the full child workflow here. Select the narrowest correct finance skill, then hand off.

## Core Contract

- Choose exactly one primary child skill or decide that no finance skill is needed.
- Prefer the most specialized finance workflow first: audit-control support before finance-data tooling.
- Use `references/children.json` as the source of truth for child boundaries, nested targets, install hints, and companion recommendations.
- If the best child is missing, say to install it rather than quietly doing weaker work under the wrong skill.
- Do not route to multiple sibling finance skills in parallel for one request.

## Decision Order

Apply these checks in order.

### 1. Is the work about audit controls, SOX, sampling, testing evidence, or workpapers?
Route to `using-finance/finance-audit-support` when the request is about internal controls over financial reporting, control testing, deficiency evaluation, sample selection, workpapers, or remediation support.

Typical signs:
- SOX 404, controls, walkthroughs, operating effectiveness, deficiency, remediation, or workpaper language
- request for audit support around financial controls rather than market-data tooling
- need for reviewer-ready audit documentation or testing logic

### 2. Is the work about finance data tools, public-company metrics, or market-data retrieval patterns?
Route to `using-finance/finance-markets` when the request is about finance connectors, quotes, financials, earnings, segments, or how to gather structured finance data.

Typical signs:
- prices, financials, earnings, segments, holdings, estimates, analyst research, or connector/tool usage language
- request for finance data sourcing patterns or reference-date handling
- need to support another finance or investment skill with market-data mechanics

### 3. No finance skill
If none of the above fits cleanly, do not force a finance skill.

## Router Output

Return one of these forms and then invoke the selected child if needed:

- `Route to using-finance/finance-audit-support.`
- `Route to using-finance/finance-markets.`
- `Install <child-path>, then route to <child-path>.`
- `No finance skill needed; answer directly.`

Add one sentence explaining why the selected child is the narrowest correct fit.

## References

- `references/children.json`

## Failure Modes to Avoid

- routing public-company or connector-tooling questions into audit support
- routing SOX or controls work into finance-markets just because both mention financial data
- silently downgrading to another child when the best one is missing
