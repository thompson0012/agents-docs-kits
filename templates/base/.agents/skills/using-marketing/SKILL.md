---
name: using-marketing
description: Use when a marketing request could plausibly need performance analytics, competitive positioning analysis, or content creation and the agent must choose the narrowest child skill first.
---

# Using Marketing

Use this router when the request is marketing-related and more than one marketing child skill could fit.

Do not perform the full child workflow here. Select the narrowest correct marketing skill, then hand off.

## Core Contract

- Choose exactly one primary child skill or decide that no marketing skill is needed.
- Prefer the most concrete business question first: measurement and diagnosis before market comparison before content production.
- Use `references/children.json` as the source of truth for child boundaries, nested targets, install hints, and companion recommendations.
- If the best child is missing, say to install it rather than quietly doing weaker work under the wrong skill.
- Do not route to multiple sibling marketing skills in parallel for one request.

## Decision Order

Apply these checks in order.

### 1. Is the main need measurement, KPI selection, reporting, or diagnosis?
Route to `using-marketing/marketing-performance-analytics` when the request is about channel performance, funnel metrics, recurring reports, attribution, forecasting, or diagnosing what changed.

Typical signs:
- reporting cadence, KPI, dashboard, forecast, attribution, or funnel language
- request to explain performance changes or optimization priorities
- need to tie marketing activity to pipeline or revenue outcomes

### 2. Is the main need competitor or positioning analysis?
Route to `using-marketing/marketing-competitive-analysis` when the request is about competitor landscapes, messaging comparisons, positioning maps, battlecards, or content-gap reviews.

Typical signs:
- competitor, battlecard, positioning, messaging, or market-map language
- request to compare how peers frame value or where they are winning
- need for source-backed market context before changing strategy or enablement

### 3. Is the main need to draft or structure marketing content?
Route to `using-marketing/content-creation` when the primary deliverable is the actual copy or structure for a blog post, social post, email, landing page, press release, or case study.

Typical signs:
- write, draft, outline, headline, CTA, or content brief language
- need for channel-specific content structure or copy best practices
- request for the artifact itself rather than the analysis behind it

### 4. No marketing skill
If none of the above fits cleanly, do not force a marketing skill.

## Router Output

Return one of these forms and then invoke the selected child if needed:

- `Route to using-marketing/marketing-performance-analytics.`
- `Route to using-marketing/marketing-competitive-analysis.`
- `Route to using-marketing/content-creation.`
- `Install <child-path>, then route to <child-path>.`
- `No marketing skill needed; answer directly.`

Add one sentence explaining why the selected child is the narrowest correct fit.

## References

- `references/children.json`

## Failure Modes to Avoid

- routing every marketing question to content creation because it sounds more concrete
- creating content before enough measurement or market context exists to justify it
- doing competitor analysis when the actual problem is KPI definition or reporting
- silently downgrading to another child when the best one is missing
