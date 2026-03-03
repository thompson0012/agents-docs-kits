# Roles System Prompts

Purpose-built system prompts for multi-agent execution, especially swarm-style tasking.

## Included Roles

- `swarm-coordinator.md`: decomposes work, assigns owners, and manages handoffs.
- `researcher.md`: gathers evidence and constraints with read-only exploration.
- `implementer.md`: executes approved changes with verification.
- `reviewer.md`: performs risk-first review and identifies regressions.
- `verifier.md`: validates outcomes against tests/checklists and acceptance criteria.
- `assignment-protocol.md`: shared protocol for role assignment and handoff format.

## Usage

1. Pick a role based on the task phase and risk profile.
2. Inject role prompt as system context for that agent.
3. Use `assignment-protocol.md` handoff contract between role transitions.
4. Keep one coordinator in charge of objective/scope drift control.

## Scope Rules

- Role prompts define behavior constraints, not business requirements.
- Product/project truth still comes from `AGENTS.md` and `/.agents/docs/*`.
- In conflicts, follow the priority order defined in `AGENTS.md`.
