# Software Delivery Router Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a `software-delivery` router family that captures the strongest portable lifecycle ideas from gstack without cloning its runtime-specific design.

**Architecture:** Create one top-level router package for non-trivial software feature delivery. Keep stage-specific review skills nested under that router, but continue reusing existing flat atomic skills (`using-reasoning`, `feature-spec`, `coding-and-data`, `website-building`, `self-cognitive`) through explicit router metadata rather than wrappers.

**Tech Stack:** Markdown skill packages, JSON router metadata/evals, existing `create-skill` and `create-router-skill` validators.

---

## Chunk 1: Router family creation

### Task 1: Create the software-delivery router

**Files:**
- Create: `templates/base/.agents/skills/software-delivery/SKILL.md`
- Create: `templates/base/.agents/skills/software-delivery/references/children.json`
- Create: `templates/base/.agents/skills/software-delivery/evals/evals.json`
- Create: `templates/base/.agents/skills/software-delivery/evals/trigger-evals.json`

- [ ] **Step 1: Draft router metadata and body**
  - Define the family boundary: routing non-trivial software feature delivery stages.
  - Children should include four nested review/discovery leaves plus external targets for `feature-spec`, `coding-and-data`, `website-building`, and `self-cognitive`.
  - Keep `recommends` honest and conditional.

- [ ] **Step 2: Validate router shape**
  - Run: `python3 templates/base/.agents/skills/create-router-skill/scripts/validate_router.py templates/base/.agents/skills/software-delivery --strict`
  - Expected: initial failures until all required files and metadata fields exist.

- [ ] **Step 3: Fix minimal router issues**
  - Add only the missing structure or metadata required to pass validation.

- [ ] **Step 4: Re-run router validation**
  - Run: `python3 templates/base/.agents/skills/create-router-skill/scripts/validate_router.py templates/base/.agents/skills/software-delivery --strict`
  - Expected: pass.

### Task 2: Create nested leaf skills

**Files:**
- Create: `templates/base/.agents/skills/software-delivery/feature-discovery/SKILL.md`
- Create: `templates/base/.agents/skills/software-delivery/plan-product-review/SKILL.md`
- Create: `templates/base/.agents/skills/software-delivery/plan-engineering-review/SKILL.md`
- Create: `templates/base/.agents/skills/software-delivery/plan-design-review/SKILL.md`

- [ ] **Step 1: Author leaf skill boundaries**
  - `feature-discovery`: shape a feature idea into a reusable problem/decision artifact before spec or implementation.
  - `plan-product-review`: critique scope, wedge, product value, and non-goals in a plan.
  - `plan-engineering-review`: critique architecture, data flow, edge cases, tests, observability, and reversibility.
  - `plan-design-review`: critique hierarchy, states, responsiveness, accessibility, and anti-slop for user-facing plans.

- [ ] **Step 2: Run strict leaf validation**
  - Run each:
    - `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/software-delivery/feature-discovery --strict`
    - `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/software-delivery/plan-product-review --strict`
    - `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/software-delivery/plan-engineering-review --strict`
    - `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/software-delivery/plan-design-review --strict`
  - Expected: initial failures if structure or links are incomplete.

- [ ] **Step 3: Fix minimal leaf issues**
  - Keep each leaf focused on one job; no wrappers, no runtime-specific preambles.

- [ ] **Step 4: Re-run strict leaf validation**
  - Expected: all pass.

---

## Chunk 2: Discovery surfaces and router integration

### Task 3: Wire discovery surfaces

**Files:**
- Modify: `templates/base/.agents/skills/using-agent-practices/references/category-map.md`
- Modify: `README.md`
- Modify: `templates/base/AGENTS.md`

- [ ] **Step 1: Update category map**
  - Add `software-delivery` as the route for non-trivial software feature lifecycle work.
  - Clarify its boundary relative to `using-reasoning`, `feature-spec`, `coding-and-data`, and `website-building`.

- [ ] **Step 2: Update README**
  - Add a short note that non-trivial software feature work can start with `software-delivery` when the user needs lifecycle guidance.

- [ ] **Step 3: Update template AGENTS guidance**
  - Add a conservative rule that agents should consider `software-delivery` for non-trivial feature development, while leaving trivial edits on the existing direct-skill path.

- [ ] **Step 4: Run relevant validation**
  - Run: `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-agent-practices --strict`
  - Expected: pass after edits.

---

## Chunk 3: Continuity and verification

### Task 4: Refresh continuity docs and verify

**Files:**
- Modify: `docs/live/progress.md`
- Modify if scope changes: `docs/live/current-focus.md`

- [ ] **Step 1: Update progress**
  - Record the new router family, touched files, verification, and next recommended action.

- [ ] **Step 2: Run final verification**
  - Run:
    - `python3 templates/base/.agents/skills/create-router-skill/scripts/validate_router.py templates/base/.agents/skills/software-delivery --strict`
    - `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/software-delivery/feature-discovery --strict`
    - `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/software-delivery/plan-product-review --strict`
    - `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/software-delivery/plan-engineering-review --strict`
    - `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/software-delivery/plan-design-review --strict`
    - `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-agent-practices --strict`
    - `python3 scripts/audit_base_template_skills.py`
    - `git diff --check`
  - Expected: all pass.

- [ ] **Step 3: Request focused review**
  - Ask a reviewer subagent to inspect router honesty, leaf boundaries, and discovery-surface wording before claiming completion.
