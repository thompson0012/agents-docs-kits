---
name: using-sales
description: Use when a sales request could plausibly need account research, call preparation, or personalized outbound drafting and the agent must choose the narrowest child skill first.
---

# Using Sales

Use this router when the request is sales-related and more than one sales child skill could fit.

Do not perform the full child workflow here. Select the narrowest correct sales skill, then hand off.

## Core Contract

- Choose exactly one primary child skill or decide that no sales skill is needed.
- Prefer the most concrete deliverable first: meeting prep before outbound draft before general research.
- Use `references/children.json` as the source of truth for child boundaries, install hints, and companion recommendations.
- If the best child is missing, say to install it rather than quietly doing weaker work under the wrong skill.
- Do not route to multiple sibling sales skills in parallel for one request.

## Decision Order

Apply these checks in order.

### 1. Is the user preparing for a specific meeting or call?
Route to `sales-call-prep` when the request is about a scheduled or imminent discovery call, demo, negotiation, proposal review, check-in, or QBR.

Typical signs:
- known meeting type, attendees, or calendar context
- need for agenda, discovery questions, objections, or next-step planning
- request to prepare before a call or meeting

### 2. Is the user asking for a personalized outbound message?
Route to `sales-draft-outreach` when the main deliverable is a cold email, warm email, LinkedIn note, re-engagement note, or follow-up message.

Typical signs:
- drafting, writing, or revising outreach copy
- choosing a hook, CTA, or follow-up sequence
- explicit outbound channel request

### 3. Is the user primarily gathering account or contact intelligence?
Route to `account-research` when the main need is to understand a company, person, or domain before a sales action.

Typical signs:
- research, intel, or lookup request
- missing enough context to prep a call or draft credible outreach
- request for company profile, recent news, key people, or qualification signals

### 4. No sales skill
If none of the above fits cleanly, do not force a sales skill.

## Router Output

Return one of these forms and then invoke the selected child if needed:

- `Route to sales-call-prep.`
- `Route to sales-draft-outreach.`
- `Route to account-research.`
- `Install <child-name>, then route to <child-name>.`
- `No sales skill needed; answer directly.`

Add one sentence explaining why the selected child is the narrowest correct fit.

## References

- `references/children.json`

## Failure Modes to Avoid

- treating every sales request as outbound drafting
- doing broad account research when the user already needs a meeting brief now
- drafting outreach before enough research exists to support a credible hook
- silently downgrading to another child when the best one is missing
