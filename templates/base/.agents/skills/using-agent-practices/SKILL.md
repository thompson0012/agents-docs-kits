---
name: using-agent-practices
description: Use when the user may need a first-party skill from `.agents/skills` and the right leaf skill or family router is not obvious yet.
---

# Using Agent Practices

Use this skill to route a request to the narrowest correct first-party skill in this repository.

Do not solve the user's substantive task here. Pick the right next skill or decide that no first-party skill is needed.

For the current category map and skill inventory, read `references/category-map.md` when the route is unclear or the suite has changed.

## Core Contract

- Choose exactly one target: a single leaf skill, a family router such as `using-reasoning` or `using-sales`, or no suite skill.
- Prefer the narrowest correct fit over the most impressive fit.
- If no first-party skill clearly adds value, say so and answer directly.
- Do not stack multiple primary suite skills from this router.
- Route to a family router only when the ambiguity is inside that family.

## Category Order

Apply these checks in order.

### 1. Orchestration and continuity
- Need a compacted session state, handoff snapshot, or continuation summary -> `context-compaction`
- Need a confidence check, postmortem, lessons learned, repeatable workflow extraction, or preflight verification -> `self-cognitive`

### 2. Prompt artifact creation
- The requested deliverable is itself a prompt, system prompt, prompt template, or prompt architecture -> `meta-prompting`

### 3. Specialized business and design skills
- Need a harsh startup viability simulation, market reality check, CAC/churn/runway stress test, or 180-day startup narrative -> `startup-pressure-test`
- Need design tokens, a brand system, or a brand spec from brand inputs -> `generating-design-tokens`
- Need an Apple-like liquid glass browser effect using CSS/SVG refraction and displacement maps -> `liquid-glass-design`

### 4. Sales workflows
- Need sales help and the request could plausibly mean account research, meeting prep, or personalized outreach -> `using-sales`

### 5. Reasoning and strategy requests
If the task is mainly about understanding, framing, advising, or scenario-planning a problem, route to `using-reasoning`.

### 6. No suite skill
If none of the above fits cleanly, do not force a suite skill.

## Router Output

Return one of these forms and then invoke the selected skill if needed:

- `Route to context-compaction.`
- `Route to self-cognitive.`
- `Route to meta-prompting.`
- `Route to startup-pressure-test.`
- `Route to generating-design-tokens.`
- `Route to liquid-glass-design.`
- `Route to using-sales.`
- `Route to using-reasoning.`
- `No agent-practices skill needed; answer directly.`

Add one sentence explaining why the selected route is the narrowest correct fit.

## Failure Modes to Avoid

- routing to a specialist because of one keyword when the artifact type points elsewhere
- routing to `using-reasoning` for requests that are clearly prompt, continuity, startup, or design work
- sending a request to multiple sibling skills in parallel from this router
- forcing a suite skill onto a simple request that does not benefit from special instructions
- routing an ambiguous sales request straight to one leaf when `using-sales` should narrow it first
