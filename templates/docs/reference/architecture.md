# Architecture Reference

This starter assumes an agent-operated product repository with durable file-based state. Chat history is disposable; the repository is not.

## Canonical topology

- `AGENTS.md`: operating contract for the whole repo.
- `docs/reference/architecture.md`: stable technical boundaries and state precedence.
- `docs/reference/design.md`: stable UI quality bar and review expectations.
- `docs/live/features.json`: machine-readable backlog and active sprint pointer.
- `docs/live/progress.md`: append-only ledger of shipped or archived outcomes.
- `docs/live/memory.md`: durable learnings, environment quirks, and conventions.
- `.harness/<feature-id>/`: the only place for active sprint-local execution state.
- `docs/archive/<feature-id>_timestamp/`: immutable historical sprint artifacts after closure.
- `docs/scripts/*`: optional helpers; never the source of truth for state.

## Stack assumptions

- The product surface is a modern app with UI work that benefits from browser-based verification.
- Framework specifics belong in sprint contracts and code, not in the harness itself; the harness stays portable across React/Vite/Next-style repos.
- UI flows should expose deterministic selectors or hooks so browser QA can verify behavior without relying on brittle copy.
- Agents may use scripts and tooling, but must write outcomes back into repository state files.

## Routing boundaries

The `using-agents-stack` skill package should route work across these boundaries:

- `project-initializer`: create or normalize the repo operating skeleton.
- `generator-proposal`: shape a backlog item into a bounded sprint proposal and contract.
- `generator-execution`: implement only the approved active sprint.
- `adversarial-live-review`: verify the result from observable behavior and record pass/fail.
- `evaluator-contract-review`: challenge scope, acceptance criteria, and contract quality before or after execution.
- `state-update`: synchronize local sprint outcomes back to `docs/live/*` and archive folders.

No skill should skip the file handoff between those phases. Planning, execution, review, and state publication are separate concerns even when performed by one agent.

## State locations and precedence

1. Human edits and explicit user instructions.
2. Active sprint-local state in `.harness/<active-feature>/`, especially `contract.md` and `status.json`.
3. Global live state in `docs/live/features.json`, `docs/live/progress.md`, and `docs/live/memory.md`.
4. Stable reference intent in `docs/reference/*`.
5. Derived outputs from `docs/scripts/*` or ad hoc tooling.

Use local state to decide how to continue the active sprint. Use global state to decide what the project should work on next. If they disagree, resolve the conflict explicitly; do not silently invent a merge.

## Single-active-sprint rule

Exactly one feature may be active in `.harness/` at a time. New work stays pending in `docs/live/features.json` until the active sprint is reviewed and either:

- passed, published to `docs/live/*`, then archived under `docs/archive/`, or
- failed/cancelled, preserved in place for resume with an updated next action.

## Resume and archive procedure

- Resume by reading `docs/live/features.json`, then `.harness/<feature-id>/status.json`, then the file named by `resume_from`.
- Keep implementation notes, handoff context, and review findings inside the active sprint folder while work is live.
- After a sprint is complete and state is updated, copy or move the final local artifacts to `docs/archive/<feature-id>_timestamp/`.
- Never mix archived artifacts back into `.harness/`; active and historical state must stay separate.
