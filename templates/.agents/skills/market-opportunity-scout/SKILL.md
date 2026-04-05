---
name: market-opportunity-scout
description: Use when public posts, threads, newsletters, interviews, transcripts, or creator/company notes should be turned into evidence-backed business opportunities by extracting recurring pains, DIY workarounds, and unmet jobs-to-be-done.
---

# Market Opportunity Scout

## Overview

Use this skill to analyze public sharing from a person, creator, company, or niche and turn it into concrete opportunity hypotheses. The job is not to summarize the content. The job is to find repeated pain, visible workaround behavior, and credible wedges for a product, service, workflow, template, API, automation, dataset, community, course, or done-for-you offer.

If the current environment exposes a compatible phased workflow such as `using-agents-stack`, you may use it to split the work into extraction, synthesis, opportunity generation, and ranking. If not, perform the same sequence directly in one pass.

## Non-Negotiable Evidence Rules

- Use only the supplied material unless the caller explicitly provides outside research.
- Separate **direct evidence**, **inference**, and **speculation**. Never present inference as quoted fact.
- Prefer repeated pain, workaround usage, explicit manual effort, and recurring phrasing over one-off opinions.
- Give extra weight to concrete DIY behavior: spreadsheets, prompts, scripts, templates, hacks, manual workflows, handoffs, and repeated workarounds.
- When multiple sources are provided, look for recurring patterns across them. Repetition across sources is a strong signal.
- Distinguish a content angle from a business opportunity. Attention alone is not demand.
- Do not force a SaaS conclusion. The best fit may be a service, workflow product, template pack, automation, plugin, API, dataset, community, course, or done-for-you offer.
- Prefer the smallest credible wedge that solves one painful job-to-be-done.
- If evidence is weak, contradictory, or thin, say so plainly and lower confidence.
- If the input is only a podcast and no transcript, notes, or quoted excerpts are provided, state that the evidence is insufficient and stop short of confident opportunity claims.
- Do not invent market size, pricing, or buyer intent. If the caller asks for those, label them as assumptions rather than evidence.

## Workflow

1. **Extract grounded evidence**
   - Pull out explicit pain points, repeated complaints, manual steps, workaround artifacts, stated constraints, and hints of urgency.
   - Note who experiences the pain: the speaker, their audience, operators behind the scenes, or an adjacent market.
   - Preserve source attribution so each claim can be traced back.

2. **Synthesize patterns**
   - Merge overlapping pains and workaround behaviors into a short list of recurring jobs-to-be-done.
   - Mark each pattern with evidence strength: single-source, repeated in one source, or repeated across sources.
   - Call out where the pattern is solid evidence versus a plausible but unproven inference.

3. **Generate opportunity candidates**
   - Translate the strongest patterns into concrete offers.
   - For each candidate, name the buyer or user, the painful job, the smallest wedge, and the likely form factor.
   - Keep the solution class open: service, workflow, template, automation, dataset, plugin, API, community, educational product, or software.

4. **Rank and filter**
   - Score candidates on pain severity, frequency, willingness to pay or delegate, audience reachability, and speed of validation.
   - Favor opportunities backed by visible workaround behavior and repeated pain.
   - If no candidate clears the evidence bar, say that no strong opportunity is yet supported.

## Output Contract

Return a concise analysis with these sections:

1. **Core insight**
   - 3-5 sentences on what the content is really revealing.

2. **Evidence ledger**
   - Bullet list or table of the strongest source-backed signals.
   - Label every item as `direct evidence`, `inference`, or `speculation`.

3. **Recurring patterns**
   - For each pattern: the painful job, affected actor, supporting evidence, and why it appears recurring.

4. **Ranked opportunities**
   - For each opportunity include:
     - name
     - target user or buyer
     - problem solved
     - proposed wedge
     - solution form factor
     - evidence basis
     - confidence
     - first validation step

5. **Best bet**
   - The single strongest opportunity and why it wins.

6. **Validation plan**
   - Three fastest tests to validate demand, with expected signals.

7. **Gaps and caveats**
   - Missing evidence, unresolved assumptions, contradictions, and what would increase confidence.

## Guardrails and Failure Modes

- Do not drift into biography, content summary, or generic trend commentary.
- Do not turn weak signals into confident market claims.
- Do not confuse audience growth tactics with product opportunities.
- Do not collapse all opportunities into software when a lighter offer is better supported.
- When evidence is thin, return fewer opportunities or none.
- When multiple sources disagree, surface the disagreement instead of averaging it away.