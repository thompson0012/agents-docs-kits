# GUIDELINES.md — How to Write & Maintain Project Documentation

**Purpose**: This document provides supporting guidance for AI agents on how to create, update, and structure the key documents referenced in `AGENTS.md`. 

*Note: This is a supporting guide. Canonical rules reside in `AGENTS.md`.*

## General Principles

- **Conciseness**: Documents should be concise yet complete, aiming for clarity over length.
- **Formatting**: Use Markdown with semantic headings (`##`, `###`), bullet lists, and tables to improve readability.
- **Version Control**: Changes should be committed with descriptive, atomic messages.
- **Traceability**: Statements should be grounded in the codebase, requirements, or recorded decisions.
- **Approval**: Major updates to any document should be proposed to the user for approval.
- **Iteration**: Documents should be updated as new insights or corrections occur. **Self‑maintenance**: `AGENTS.md` and `/docs/*` are agent‑maintained artifacts; the agent must keep them current and aligned with user conversations and decisions, using the Doc Evolution Protocol.

## Version Control Workflow

Guidance for maintaining a clean and traceable project history:

- **Atomic Commits**: Each commit should represent a single, logical change.
- **Message Format**: Prefer `type(scope): description` (e.g., `feat(auth): add login form validation`).
- **PR Hygiene**: Pull requests should include a clear summary of changes and reference relevant tasks or issues.

## Document-Specific Guidance

### PROGRESS.md (Session State Log)
- **Purpose**: Lightweight state carry-over between sessions.
- **Structure Recommendation**:
  - Session summary and date at the top.
  - Sections for Completed, In Progress, Blockers, and Quick Notes.
- **Example**: "Finished API integration for user profiles; blocking on database migration script."

### PRD.md (Product Requirements)
- **Purpose**: Single source of truth for product goals and features.
- **Structure Recommendation**: Overview, Goals/Metrics, Personas, Features (MoSCoW), and Non-Functional Requirements.
- **Example Goal**: "Reduce page load time by 30% to improve user retention."

### IMPLEMENTATION_PLAN.md
- **Purpose**: Roadmap for technical execution.
- **Structure Recommendation**: Milestones, Phases, Open Decisions, and Task Breakdowns.
- **Verification**: Each phase should include explicit verification steps (e.g., "Run unit tests", "Manual UI check").

### LESSONS.md (Operational Patterns)
- **Purpose**: Log of learned optimizations and avoided mistakes.
- **Structure Recommendation**: Issue description, Root cause, and a pattern to prevent recurrence.
- **Example**: "Avoided using global state for temporary form data; used local component state instead."

### TECH_STACK.md
- **Purpose**: Documentation of versions and allowed tools.
- **Discipline**: Use an "unknown until confirmed" approach for any tech stack assumptions.

### SECURITY.md (Security Guidance)
- **Purpose**: Defense-in-depth guidance for security-conscious development.
- **Key Areas**: Secrets management, input validation, and safe coding patterns.

## Communication Standards

### Before Starting Work (RECOMMENDED)
```
ASSUMPTIONS I'M MAKING:
- [Assumption 1 - let user correct before wasted work]
- [Assumption 2]
```

### Plan Template (RECOMMENDED)
Use this format when proposing a plan (especially for anything > 20 lines or > 1 file per `AGENTS.md` §4).

```
PLAN:
- Goal:
- Scope (in):
- Non-goals (out):
- Constraints (tools, time, compatibility, risk tier):
- Assumptions (explicit; link to PRD/TECH_STACK where relevant):
- Risks / unknowns:

TASK BREAKDOWN (atomic, verifiable):
- Task 1:
  - Files/areas:
  - Success criteria:
  - Verification (tests/build/lsp/manual):
  - Dependencies/blockers:
- Task 2:
  - ...

ROLLBACK / STOP CONDITIONS:
- If [X] fails, do [Y] (revert, pause, escalate, ask for approval).
```

### Plan & Task Recordkeeping (RECOMMENDED)

If you want plans and task breakdowns to remain traceable across sessions, use the conventions in `docs/PLANS.md`.

Recommended approach:
- Keep the approved plan in a dated folder under `/docs/plans/.../plan.md`
- Keep the plan’s atomic checklist in `/docs/plans/.../tasks.md`
- Link to the plan folder from `docs/PROGRESS.md` (session timeline)
- Avoid duplicating the same checklist in multiple places; prefer linking

### After Completing Work (RECOMMENDED)
```
CHANGES MADE:
- [file/location]: [what changed and why]
```

### Proposing Documentation Updates
When updating any document (per AGENTS.md §5):
1. Analyze current state and identify necessary changes
2. Propose using `PROPOSED DOC UPDATE` format (see AGENTS.md §5)
3. Wait for explicit user approval
4. Update and log summary in PROGRESS.md

## Writing Conventions

- Use active voice and professional tone.
- Avoid jargon unless it is part of the project's domain glossary.
- Prefer tables for comparing options or listing tokens.
- Keep examples practical and easy to follow.

This document may be updated by following `AGENTS.md` §5 (Documentation Evolution Protocol).
