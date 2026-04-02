---
name: harness-navigation
purpose: Determine the current state of the project and route the execution to the correct next phase.
trigger: At the beginning of every new agent session.
inputs:
  - docs/live/features.json
  - .harness/<active-sprint>/status.json (if it exists)
outputs:
  - Tool calls to load the appropriate phase-specific skill.
boundaries:
  - Do not write code or evaluate design.
  - Do not alter the backlog priorities.
next_skills:
  - project-initializer
  - generator-proposal
  - evaluator-contract-review
  - generator-execution
  - adversarial-live-review
  - state-update
---

# Instructions: The Harness State Machine

You are operating within a multi-agent harness. Your job is to read the physical state files and figure out what phase the project is in. Follow this exact decision tree:

## Step 1: Check Global Initialization
Read `docs/live/features.json`. 
- If the file is empty, missing, or contains no backlog items:
  **Action**: Load the `project-initializer` skill and begin the bootstrapping phase.

## Step 2: Check for Active Sprints
If `features.json` is populated, look for any feature where `"status": "in_progress"`.
- If NO features are `in_progress`:
  **Action**: Identify the highest priority feature marked `"status": "pending"`. Load the `generator-proposal` skill to start a new sprint.
- If a feature IS `in_progress`:
  **Action**: Move to Step 3.

## Step 3: Check Local Sprint Checkpoints
Navigate to the local `.harness/<feature-id>/` directory for the active sprint and read the files present.

1. **If `status.json` says `"phase": "paused_by_timeout"`**:
   The previous session crashed. Read the `resume_from` field, verify the current state of the codebase, and load the skill corresponding to that phase.

2. **If `review.md` exists**:
   The Adversarial Evaluator has finished grading the code. 
   **Action**: Load the `state-update` skill to process the PASS/FAIL result.

3. **If `handoff.md` exists (but no `review.md`)**:
   The Generator has finished writing code and the dev server is active, but it hasn't been tested yet.
   **Action**: Load the `adversarial-live-review` skill to begin UI testing.

4. **If `contract.md` exists (but no `handoff.md`)**:
   The Generator and Evaluator have agreed on the exact definition of "done", but no code has been written yet.
   **Action**: Load the `generator-execution` skill to begin coding.

5. **If `sprint_proposal.md` exists (but no `contract.md`)**:
   The Generator has proposed a plan, but the Evaluator has not approved it.
   **Action**: Load the `evaluator-contract-review` skill to judge the proposal.

## Critical Constraint
Do NOT attempt to perform the actual work of these phases yourself. Your only job is to load the correct skill into your context window using the `load_skill` tool, which will alter your persona to fit the required phase.
