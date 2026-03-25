# Harness Delivery Control Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a portable multi-session harness layer and an independent frontend evaluator to the software-delivery family, with explicit handoff docs and honest routing from the existing website-building and agent-practices surfaces.

**Architecture:** Extend the existing `software-delivery` router rather than creating a parallel delivery family. Add two nested leaves: `harness-design` for cross-session planner/generator/evaluator control, and `frontend-evaluator` for browser-facing independent acceptance. Keep builder-side QA in `website-building`, reuse its shared browser QA methodology from an evaluator stance, and add two new live-doc templates (`runtime.md`, `qa.md`) so baton state and evaluation evidence survive across sessions.

**Tech Stack:** Markdown skill packages, JSON router metadata and eval fixtures, template live/reference docs, existing `create-skill` and `create-router-skill` validators, `scripts/audit_base_template_skills.py`.

---

## Chunk 1: Software-delivery harness surface

### Task 1: Extend the software-delivery router for harness control

**Files:**
- Modify: `templates/base/.agents/skills/software-delivery/SKILL.md`
- Modify: `templates/base/.agents/skills/software-delivery/references/children.json`
- Modify: `templates/base/.agents/skills/software-delivery/evals/evals.json`
- Modify: `templates/base/.agents/skills/software-delivery/evals/trigger-evals.json`

- [ ] **Step 1: Add failing router coverage first**
  - Add one direct eval that should route to `software-delivery/harness-design` for a request about planner/generator/evaluator orchestration.
  - Add one direct eval that should route to `software-delivery/frontend-evaluator` for a request about independent browser-facing acceptance.
  - Add one trigger eval for harness-control language and one trigger eval for strict frontend signoff language.

- [ ] **Step 2: Update the router decision order in `SKILL.md`**
  - Insert `harness-design` before the plan-review lanes.
  - Insert `frontend-evaluator` immediately before the existing `website-building` step.
  - Narrow the `website-building` step so it clearly means build work plus builder-side QA, not independent evaluator signoff.
  - Add router outputs for `software-delivery/harness-design` and `software-delivery/frontend-evaluator`.

- [ ] **Step 3: Update `children.json` to match the new routing contract**
  - Add a `harness-design` child with route conditions for cross-session orchestration, explicit baton passing, and planner/generator/evaluator separation.
  - Add a `frontend-evaluator` child with route conditions for independent browser-facing acceptance.
  - Add an explicit cross-family dependency note that the evaluator uses the shared interactive browser QA methodology currently documented under `website-building/shared/12-playwright-interactive.md`.
  - Update the existing `website-building` child summary so it is honest about owning builder-side QA rather than independent evaluation.

- [ ] **Step 4: Validate the router shape**
  - Run: `python3 templates/base/.agents/skills/create-router-skill/scripts/validate_router.py templates/base/.agents/skills/software-delivery --strict`
  - Expected: pass.

- [ ] **Step 5: Commit the router update**

```bash
git add templates/base/.agents/skills/software-delivery/SKILL.md \
  templates/base/.agents/skills/software-delivery/references/children.json \
  templates/base/.agents/skills/software-delivery/evals/evals.json \
  templates/base/.agents/skills/software-delivery/evals/trigger-evals.json
git commit -m "feat: extend software-delivery for harness control"
```

### Task 2: Create the `harness-design` leaf skill

**Files:**
- Create: `templates/base/.agents/skills/software-delivery/harness-design/SKILL.md`

- [ ] **Step 1: Draft the skill boundary and workflow**
  - State that the skill activates only after the base router has already determined that cross-session control or explicit role separation is the real problem.
  - Define the three execution modes: `single-session`, `compacted-continuation`, and `planner-generator-evaluator`.
  - Name `context-compaction` as the canonical mechanism behind `compacted-continuation` when the same role continues with a fresh context budget.
  - Make the mode-selection rules observable: slice size, need for fresh-session skepticism, browser-facing/high-risk outputs, and baton-handoff requirements.

- [ ] **Step 2: Encode the role contracts**
  - Define planner, generator, and evaluator ownership.
  - Make return paths explicit: implementation defect -> generator, scope/contract defect -> planner, environment/setup defect -> blocked.
  - Require updates to `docs/live/current-focus.md`, `docs/live/progress.md`, `docs/live/runtime.md`, and `docs/live/qa.md` when those artifacts are in play.

- [ ] **Step 3: Validate the new leaf**
  - Run: `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/software-delivery/harness-design --strict`
  - Expected: pass.

- [ ] **Step 4: Commit the new leaf**

```bash
git add templates/base/.agents/skills/software-delivery/harness-design/SKILL.md
git commit -m "feat: add harness-design delivery skill"
```

### Task 3: Create the `frontend-evaluator` leaf skill

**Files:**
- Create: `templates/base/.agents/skills/software-delivery/frontend-evaluator/SKILL.md`

- [ ] **Step 1: Draft the evaluator contract**
  - Require exactly three verdicts: `pass`, `fail`, `blocked`.
  - Require four output sections: evidence matrix, defects by severity, retry instructions, and final verdict.
  - State clearly that the evaluator must not implement fixes or silently accept generator claims.

- [ ] **Step 2: Tie the evaluator to shared browser QA without forking it**
  - Reference the shared interactive browser QA methodology by name and current path.
  - Require the evaluator to execute that methodology from a fresh evaluator stance.
  - Treat partial execution, unsupported claims, or unrecorded evidence as automatic failure conditions.
  - Resolve the spec's artifact-format question by choosing markdown as the canonical evidence format in `docs/live/qa.md`; do not add a JSON artifact schema unless implementation reveals a real second consumer.

- [ ] **Step 3: Validate the new leaf**
  - Run: `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/software-delivery/frontend-evaluator --strict`
  - Expected: pass.

- [ ] **Step 4: Commit the new leaf**

```bash
git add templates/base/.agents/skills/software-delivery/frontend-evaluator/SKILL.md
git commit -m "feat: add frontend evaluator skill"
```

---

## Chunk 2: Discovery and web-flow integration

### Task 4: Make the evaluator discoverable from website-building

**Files:**
- Modify: `templates/base/.agents/skills/website-building/SKILL.md`
- Modify: `templates/base/.agents/skills/website-building/references/children.json`
- Modify: `templates/base/.agents/skills/website-building/shared/12-playwright-interactive.md`

- [ ] **Step 1: Update website-building metadata**
  - Add `software-delivery/frontend-evaluator` as a follow-on recommendation from each website-building child in `references/children.json`.
  - Keep the recommendation framed as a non-trivial or signoff-sensitive follow-on, not a required route for every trivial site edit.

- [ ] **Step 2: Update the router guidance**
  - In `website-building/SKILL.md`, distinguish builder-side browser QA from independent evaluator signoff.
  - Add a short note that non-trivial browser-facing work should usually pass through `software-delivery/frontend-evaluator` before final acceptance.

- [ ] **Step 3: Update the shared QA guide**
  - Add a small section in `shared/12-playwright-interactive.md` that explains the handoff from builder QA to independent evaluation.
  - Require the builder to leave enough visible evidence for a fresh evaluator to reproduce the claim set.

- [ ] **Step 4: Validate the website-building router**
  - Run: `python3 templates/base/.agents/skills/create-router-skill/scripts/validate_router.py templates/base/.agents/skills/website-building --strict`
  - Expected: pass.

- [ ] **Step 5: Commit the web-flow integration**

```bash
git add templates/base/.agents/skills/website-building/SKILL.md \
  templates/base/.agents/skills/website-building/references/children.json \
  templates/base/.agents/skills/website-building/shared/12-playwright-interactive.md
git commit -m "feat: connect website-building QA to frontend evaluator"
```

### Task 5: Update top-level routing and discovery surfaces

**Files:**
- Modify: `templates/base/.agents/skills/using-agent-practices/SKILL.md`
- Modify: `templates/base/.agents/skills/using-agent-practices/references/category-map.md`
- Modify: `templates/base/.agents/skills/using-agent-practices/evals/evals.json`
- Modify: `templates/base/.agents/skills/using-agent-practices/evals/trigger-evals.json`
- Modify: `README.md`
- Modify: `templates/base/AGENTS.md`

- [ ] **Step 1: Expand top-level router language**
  - In `using-agent-practices/SKILL.md`, add explicit language that multi-session runtime control, planner/generator/evaluator orchestration, and strict frontend acceptance gates belong under `software-delivery`.
  - Keep `coding-and-data`, `website-building`, and `self-cognitive` as narrower follow-ons rather than parallel replacements.

- [ ] **Step 2: Add top-level router coverage**
  - Add one direct eval and one trigger eval for harness-control requests.
  - Add one direct eval and one trigger eval for strict frontend evaluation requests.
  - Make the expected outputs land on `software-delivery`, not directly on `website-building` or `self-cognitive`.

- [ ] **Step 3: Refresh the human-facing discovery docs**
  - In `references/category-map.md`, list `software-delivery/harness-design` and `software-delivery/frontend-evaluator` as part of the software-delivery surface.
  - In `README.md`, expand the software-delivery bullet so it mentions harness control and independent frontend evaluation.
  - In `templates/base/AGENTS.md`, update the project-local skill guidance and read order so the new harness surfaces are discoverable without forcing them onto trivial work.

- [ ] **Step 4: Validate the top-level router**
  - Run: `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-agent-practices --strict`
  - Expected: pass.

- [ ] **Step 5: Commit the discovery updates**

```bash
git add templates/base/.agents/skills/using-agent-practices/SKILL.md \
  templates/base/.agents/skills/using-agent-practices/references/category-map.md \
  templates/base/.agents/skills/using-agent-practices/evals/evals.json \
  templates/base/.agents/skills/using-agent-practices/evals/trigger-evals.json \
  README.md templates/base/AGENTS.md
git commit -m "feat: expose harness routing across discovery surfaces"
```

---

## Chunk 3: Handoff-doc templates and completion checks

### Task 6: Add runtime and QA live-doc templates

**Files:**
- Create: `templates/base/docs/live/runtime.md`
- Create: `templates/base/docs/live/qa.md`
- Modify: `templates/base/docs/reference/architecture.md`
- Modify: `templates/base/docs/reference/codemap.md`

- [ ] **Step 1: Create `runtime.md`**
  - Add sections for current mode, baton owner, next-role entry criteria, reset-versus-compaction rule, artifact pointers, and stop/escalation conditions.
  - Keep it concise and template-friendly, matching the style of the existing live docs.

- [ ] **Step 2: Create `qa.md`**
  - Add sections for claim-to-evidence mapping, browser QA evidence summary, defect severity, verdict, and retry contract.
  - Make markdown the canonical artifact shape.

- [ ] **Step 3: Update the reference docs**
  - In `templates/base/docs/reference/architecture.md`, describe the new harness control surface and how `runtime.md` and `qa.md` fit alongside `current-focus.md`, `progress.md`, and `todo.md`.
  - In `templates/base/docs/reference/codemap.md`, add the new live-doc paths and the two new software-delivery leaves as high-value paths.

- [ ] **Step 4: Read back the templates for consistency**
  - Confirm the terminology matches the approved spec: `single-session`, `compacted-continuation`, `planner-generator-evaluator`, `pass`, `fail`, `blocked`.

- [ ] **Step 5: Commit the handoff-doc templates**

```bash
git add templates/base/docs/live/runtime.md \
  templates/base/docs/live/qa.md \
  templates/base/docs/reference/architecture.md \
  templates/base/docs/reference/codemap.md
git commit -m "feat: add harness runtime and QA live docs"
```

### Task 7: Refresh repo continuity docs and run final verification

**Files:**
- Modify: `docs/live/current-focus.md`
- Modify: `docs/live/progress.md`
- Modify: `docs/live/todo.md`
- Modify if the implementation changes durable repo boundaries: `docs/reference/architecture.md`
- Modify if the implementation changes high-value entrypoints: `docs/reference/codemap.md`

- [ ] **Step 1: Update continuity docs**
  - In `docs/live/current-focus.md`, replace the active objective with the harness-delivery-control implementation while it is in flight.
  - In `docs/live/todo.md`, add and sequence the harness implementation task.
  - In `docs/live/progress.md`, record the new skills, discovery-surface changes, live-doc templates, verification, and the next recommended action.

- [ ] **Step 2: Run final validation commands**
  - Run:
    - `python3 templates/base/.agents/skills/create-router-skill/scripts/validate_router.py templates/base/.agents/skills/software-delivery --strict`
    - `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/software-delivery/harness-design --strict`
    - `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/software-delivery/frontend-evaluator --strict`
    - `python3 templates/base/.agents/skills/create-router-skill/scripts/validate_router.py templates/base/.agents/skills/website-building --strict`
    - `python3 templates/base/.agents/skills/create-skill/scripts/validate.py templates/base/.agents/skills/using-agent-practices --strict`
    - `python3 scripts/audit_base_template_skills.py`
    - `git diff --check`
  - Expected: all pass.

- [ ] **Step 3: Request focused review**
  - Ask a reviewer subagent to check router honesty, the builder-vs-evaluator boundary, the new live-doc contract, and whether the website-building follow-on recommendation is discoverable but not over-applied.

- [ ] **Step 4: Commit the continuity and verification pass**

```bash
git add docs/live/current-focus.md docs/live/progress.md docs/live/todo.md \
  docs/reference/architecture.md docs/reference/codemap.md
git commit -m "docs: record harness delivery control rollout"
```
