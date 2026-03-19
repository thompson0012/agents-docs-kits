---
name: using-legal
description: Use when a legal request could plausibly need commercial contract review or operational privacy-compliance support and the agent must choose the narrowest child skill first.
---

# Using Legal

Use this router when the request is legal in nature and more than one legal child skill could fit.

Do not perform the full child workflow here. Select the narrowest correct legal skill, then hand off.

## Core Contract

- Choose exactly one primary child skill or decide that no legal skill is needed.
- Prefer operational privacy-compliance support before general contract review when the real problem is regulatory obligations, privacy operations, or DPA compliance mechanics.
- Use `references/children.json` as the source of truth for child boundaries, nested targets, install hints, and companion recommendations.
- If the best child is missing, say to install it rather than quietly doing weaker work under the wrong skill.
- Do not route to multiple sibling legal skills in parallel for one request.

## Decision Order

Apply these checks in order.

### 1. Is the work about privacy obligations, DPA compliance mechanics, DSARs, breach timelines, transfers, or regulatory monitoring?
Route to `using-legal/legal-compliance` when the request is about operational privacy compliance or privacy-law issue spotting rather than broad commercial agreement redlining.

Typical signs:
- GDPR, UK GDPR, CCPA/CPRA, cross-border transfers, DPIAs, DSARs, breach-notification timing, or regulator updates
- DPA review focused on privacy obligations, transfer terms, or compliance operations
- need for privacy-by-design, records of processing, or recurring regulatory workflow support

### 2. Is the main work commercial agreement review, playbook deviation analysis, or clause-by-clause redlining?
Route to `using-legal/contract-review` when the request is about reviewing or negotiating a contract against a negotiation playbook, even if privacy and DPA clauses are one part of the broader agreement.

Typical signs:
- contract review, redlines, negotiation fallback positions, risk allocation, or clause severity language
- limitation of liability, indemnity, IP, term and termination, dispute resolution, or broader commercial agreement structure
- DPA/privacy terms are one clause set inside a larger contract review

### 3. No legal skill
If none of the above fits cleanly, do not force a legal skill.

## Router Output

Return one of these forms and then invoke the selected child if needed:

- `Route to using-legal/legal-compliance.`
- `Route to using-legal/contract-review.`
- `Install <child-path>, then route to <child-path>.`
- `No legal skill needed; answer directly.`

Add one sentence explaining why the selected child is the narrowest correct fit.

## References

- `references/children.json`

## Failure Modes to Avoid

- routing broad commercial contract review into legal-compliance just because one clause mentions privacy
- routing privacy operations, DSARs, or breach-response work into contract-review because a DPA is involved
- silently downgrading to another child when the best one is missing
