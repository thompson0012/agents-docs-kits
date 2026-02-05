# guidelines.md ─ How to Write & Maintain Project Documentation
# Last meaningfully updated: 2026-XX-XX
# Purpose: Teach the coding agent exactly how to create, update, and structure every key document referenced in agents.md.
# Rules here are LAW — follow them precisely when writing or proposing changes to any .md file.

<general_principles>
- Keep documents **concise yet complete** — aim for clarity over length (target < 2000 words per file unless unavoidable).
- Use **Markdown** with semantic headings (##, ###), bullet lists, code blocks, tables, and XML-like tags only when they improve readability.
- **Version control everything** — commit changes with descriptive messages (e.g., "Update LESSONS.md: added new rule for X after correction").
- **Traceability** — every statement should be grounded in reality (code, user requirements, decisions). No hallucinations.
- **Human review gate** — after proposing major updates to any doc, always wait for user approval before considering it final.
- **Iterate ruthlessly** — after every correction or new insight, propose precise updates to the relevant file.
</general_principles>

<document_specific_guidelines>

## PRD.md / PRODUCT.md (Product Requirements Document)
- **Purpose** — Single source of truth for what the product should do, why, and for whom.
- **Structure** (use these headings exactly):
  1. ## Overview — one-paragraph summary of the product/feature.
  2. ## Goals & Success Metrics — business/user goals + measurable KPIs.
  3. ## User Personas — 2–4 key personas with needs/pain points.
  4. ## Features & Requirements — prioritized list (MoSCoW: Must/Should/Could/Won't).
  5. ## Non-Functional Requirements — performance, security, accessibility, scalability.
  6. ## Assumptions & Risks — explicit list.
  7. ## Out of Scope — what is deliberately not included.
- **Tone** — neutral, factual, product-manager voice. Avoid implementation details.
- **Updates** — only when user provides new requirements or pivots.

## IMPLEMENTATION_PLAN.md
- **Purpose** — Locked roadmap of phases, tasks, and decisions for the current milestone.
- **Structure**:
  1. ## Current Milestone — name & deadline.
  2. ## Phases — numbered, with estimated effort (S/M/L).
  3. ## Open Decisions — table: Decision | Options | Chosen | Reason.
  4. ## Task Breakdown — detailed, sequential steps with owners if team.
  5. ## Dependencies & Blockers — list with status.
  6. ## Risks & Mitigations.
- **Updates** — re-plan after every major change or blocker. Propose full rewrite if structure drifts.

## LESSONS.md (or corrections.md / anti-patterns.md)
- **Purpose** — Prevent repeat mistakes; self-improvement log.
- **Structure**:
  - Use reverse-chronological order (newest at top).
  - Each entry: 
    - Date / Session
    - Mistake / Issue
    - Root Cause
    - Rule to Prevent (exact wording to add to agents.md or here)
    - Example (code before/after if relevant)
- **When to update** — after every correction, bug fix, or user feedback. Propose ONE clear rule per entry.
- **Tone** — blunt, factual, no blame.

## TECH_STACK.md
- **Purpose** — Exact versions and allowed tools/libraries.
- **Structure**:
  - ## Frontend
  - ## Backend
  - ## Database / Infra
  - ## Dev Tools (lint, test, build)
  - ## Prohibited / Deprecated
- **Updates** — only after explicit upgrade or decision. Include migration notes if breaking.

## DESIGN_SYSTEM.md
- **Purpose** — Visual & interaction standards.
- **Structure**:
  - ## Tokens — colors, spacing, typography (use tables).
  - ## Components — list with usage & variants.
  - ## Motion & Accessibility — rules.
  - ## Icons & Assets — sources.
- **Updates** — when design tokens change or new components added.

## APP_FLOW.md / USER_FLOWS.md
- **Purpose** — High-level user journeys & screen flows.
- **Structure**:
  - ## Main Flows — numbered steps with conditions.
  - ## Edge Cases & Errors.
  - Use simple text-based diagrams (ASCII or Mermaid if supported).
- **Updates** — when UX changes or new flows added.

## FRONTEND_GUIDELINES.md / BACKEND_STRUCTURE.md / etc.
- **Purpose** — Stack-specific patterns & conventions.
- **Structure** — Mirror coding_standards in agents.md but deeper (examples, do/don't tables).
- **Updates** — when new patterns emerge or old ones break.

</document_specific_guidelines>

<update_protocol>
1. When proposing changes: output the **full updated file** with changes highlighted (e.g., ```diff``` or bold new sections).
2. Always ask: "Approve this update to [file]?"
3. After approval: confirm the change is committed (or propose commit message).
4. For minor fixes: propose inline edits.
5. For major rewrites: explain why the current structure is insufficient.
</update_protocol>

<core_rules>
- Never invent content — base everything on code, user input, or existing docs.
- Use consistent language & formatting across all docs.
- Prefer tables for lists/comparisons, code blocks for examples.
- End every major doc update with: "This document is now locked until next approved change."
</core_rules>
