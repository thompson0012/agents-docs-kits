# Project Agent Guide

## Injected Context Contract

- Inject `AGENTS.md` at session start.
- Treat `AGENTS.md` as the only always-in-context index.
- Retrieve additional docs on demand from `docs/live/` and `docs/reference/`; do not preload the full docs set.

## Skill Priority

Skills take precedence over model knowledge.

1. **Project-Local Skills** — check `.agents/skills/` first for repository-specific guidance.
2. **User Skills** — check `~/.agents/skills/` for user-installed capabilities.
3. **Model Knowledge** — fallback only when no skill applies.

Read `.agents/skills/using-labs21-suite/SKILL.md` as the router index whenever the right project-local skill or family router is not obvious.

## Progressive Disclosure Rules

Read only the smallest set of docs needed for the task:

- `docs/live/current-focus.md` — active objective, scope, constraints.
- `docs/live/roadmap.md` — phased work, goal lineage, phase handoffs. Read when work spans multiple phases or needs compaction-sensitive continuity.
- `docs/live/progress.md` — session continuity, touched files, verification, next action. Use its `Next Recommended Action` as the default resume pointer.
- `docs/live/todo.md` — read only when sequencing among multiple plausible next actions.
- `templates/base/docs/live/runtime.md` — baton state and execution mode when working inside template delivery-control flows.
- `templates/base/docs/live/qa.md` — evaluator evidence and verdicts when working inside template delivery-control flows.
- `docs/reference/codemap.md` — where to work, entrypoints, subsystem locations.
- `docs/reference/architecture.md` — system boundaries, invariants, component relationships.
- `docs/reference/implementation.md` — technical execution details.
- `docs/reference/design.md` — product intent, UX, behavior rules.
- `docs/reference/memory.md` — durable decisions, policies, truths that survive beyond one session.
- `docs/reference/lessons.md` — reusable mistakes, anti-patterns, hard-won fixes.

## Read Order by Task Type

| Task | Read path |
|------|-----------|
| Start or resume work | `AGENTS.md` → `current-focus` → `progress` |
| Roadmap-driven phased work | `AGENTS.md` → `current-focus` → `roadmap` → `progress` |
| Template delivery-control work | `AGENTS.md` → `current-focus` → `templates/base/docs/live/runtime.md` → `progress` → `templates/base/docs/live/qa.md` |
| Pick the next task | `AGENTS.md` → `current-focus` → `progress` → `todo` |
| Find where to work | `AGENTS.md` → `current-focus` → `progress` → `codemap` |
| Implement or change behavior | `AGENTS.md` → `current-focus` → `progress` → `implementation` |
| Adjust product or UX behavior | `AGENTS.md` → `current-focus` → `progress` → `design` |
| Understand system boundaries | `AGENTS.md` → `current-focus` → `progress` → `architecture` |
| Recover durable decisions | `AGENTS.md` → `current-focus` → `progress` → `memory` |
| Learn from prior mistakes | `AGENTS.md` → `current-focus` → `progress` → `lessons` |

## Pre-Implementation Alignment

Before writing code or creating files:

1. **Objective Match** — which line in `current-focus.md` defines this work?
2. **Scope Boundary** — which out-of-scope item prevents something you might otherwise do?
3. **Minimal Change** — what is the smallest change that achieves the objective?

If you cannot answer all three with specific references, re-read `docs/live/current-focus.md`.

## Drift Detection

Pause and re-read `docs/live/current-focus.md` if:

- Implementation requires files not listed in scope.
- You are editing files outside the touched-files history in `progress.md`.
- A "small fix" has expanded to touch 3+ additional files.
- You are adding features not requested in the objective.

## Update Rules After Meaningful Work

- `docs/live/current-focus.md` — when objective, scope, constraints, or success criteria change.
- `docs/live/roadmap.md` — when phase goals, phase boundaries, or goal-retirement status change.
- `docs/live/progress.md` — after meaningful work: state, completed work, blockers, touched files, verification, next action.
- `docs/live/todo.md` — when priorities or next actions change.
- `templates/base/docs/live/runtime.md` — when execution mode, baton owner, or reset-vs-compaction rules change in template delivery-control flows.
- `templates/base/docs/live/qa.md` — when evaluator evidence, defects, verdicts, or retry conditions are recorded in template delivery-control flows.
- `docs/reference/*` — see Reference Writeback Gate below.

## Reference Writeback Gate

Before yielding after meaningful work, explicitly decide whether any `docs/reference/*` file must change:

| Trigger | Update |
|---------|--------|
| New or revised durable default, policy, packaging rule, routing rule, or repo truth | `memory.md` |
| Reusable mistake, anti-pattern, failed attempt, or hard-won fix | `lessons.md` |
| Changed system boundaries, family ownership, component relationships, or invariants | `architecture.md` |
| Changed entrypoints, package locations, router locations, or subsystem locations | `codemap.md` |

If none apply, state that conclusion explicitly before completion.

Path-based default: if you changed skill packages, router metadata, or package layout under `.agents/skills/`, assume a `docs/reference/*` review is required.
