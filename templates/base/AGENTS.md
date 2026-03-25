# Project Agent Guide

## Repo Purpose

This repository uses a minimal agent documentation structure for recall, progressive disclosure, and reliable hand-off in a single worktree.

## Injected Context Contract

- Inject `AGENTS.md` at session start.
- Treat `AGENTS.md` as the only always-in-context index.
- Retrieve additional docs on demand from `docs/live/` and `docs/reference/`; do not preload the full docs set.

## Project-Local Skills

- If a needed skill is not already loaded from `~/.agents/skills`, check the project's `.agents/skills/` directory before assuming the skill is unavailable.
- Treat `.agents/skills/` as the project-local skill surface: use the most specific relevant skill there when the repository ships task-specific guidance.
- Read `.agents/skills/using-agent-practices/SKILL.md` as the router index whenever the right project-local skill or family router is not obvious.
- For non-trivial software feature work that still needs discovery, planning, delivery-control decisions, or independent frontend signoff, consider `.agents/skills/software-delivery/SKILL.md` before jumping straight to implementation; keep trivial or already-clear work on the direct skill path.
- Read only the smallest relevant skill or subdirectory needed for the task; do not preload the entire project skill tree.

## Progressive Disclosure Rules

- Start here, then read only the smallest set of docs needed for the task.
- Read `docs/live/current-focus.md` for the active objective, scope, and constraints.
- Read `docs/live/runtime.md` when the work runs under explicit delivery control, crosses session boundaries, or depends on planner/generator/evaluator baton state.
- Read `docs/live/progress.md` for session continuity, touched files, latest verification, and the next recommended action.
- Read `docs/live/qa.md` when independent acceptance evidence or evaluator verdicts matter.
- Use `docs/live/progress.md`'s `Next Recommended Action` as the default resume pointer unless user direction or `docs/live/current-focus.md` overrides it.
- Use `docs/live/progress.md`'s `Verification Status` before claiming completion or resuming work in a previously touched area.
- Read `docs/live/todo.md` only when selecting or sequencing among multiple plausible next actions, or when `docs/live/progress.md` does not already make the next step clear.
- Read `docs/reference/codemap.md` when you need to find where to work, identify likely entrypoints, or map a subsystem.
- Read `docs/reference/architecture.md` when system boundaries, invariants, or component relationships matter.
- Read `docs/reference/implementation.md` only for technical execution details.
- Read `docs/reference/design.md` only for product intent, UX, or behavior rules.
- Read `docs/reference/memory.md` for durable decisions, policies, or truths that should survive beyond the current task.
- Read `docs/reference/lessons.md` after mistakes, failed attempts, or surprising outcomes worth reusing.

## Read Order by Task Type

- Start or resume work: `AGENTS.md` → `docs/live/current-focus.md` → `docs/live/progress.md`
- Resume controlled multi-session work: `AGENTS.md` → `docs/live/current-focus.md` → `docs/live/runtime.md` → `docs/live/progress.md` → `docs/live/qa.md` when evaluator evidence exists
- Pick the next task: `AGENTS.md` → `docs/live/current-focus.md` → `docs/live/progress.md` → `docs/live/todo.md` when prioritization is still needed
- Find where to work: `AGENTS.md` → `docs/live/current-focus.md` → `docs/live/progress.md` → `docs/reference/codemap.md`
- Implement or change behavior: `AGENTS.md` → `docs/live/current-focus.md` → `docs/live/progress.md` → `docs/reference/implementation.md`
- Adjust product or UX behavior: `AGENTS.md` → `docs/live/current-focus.md` → `docs/live/progress.md` → `docs/reference/design.md`
- Understand system boundaries before changing behavior: `AGENTS.md` → `docs/live/current-focus.md` → `docs/live/progress.md` → `docs/reference/architecture.md`
- Recover durable decisions or repo truths: `AGENTS.md` → `docs/live/current-focus.md` → `docs/live/progress.md` → `docs/reference/memory.md`
- Learn from prior mistakes or failed attempts: `AGENTS.md` → `docs/live/current-focus.md` → `docs/live/progress.md` → `docs/reference/lessons.md`
- Cross-cutting work: read `docs/reference/architecture.md` first, then `docs/reference/implementation.md` and `docs/reference/design.md` as needed after the live docs.

## Update Rules After Meaningful Work

- Update `docs/live/current-focus.md` when the active objective, scope, constraints, or success criteria change.
- Update `docs/live/runtime.md` when the active execution mode, baton owner, entry criteria, or reset-versus-compaction rule changes.
- Update `docs/live/progress.md` after meaningful work with current state, completed work, blockers, touched files, verification, and next recommended action.
- Update `docs/live/qa.md` when an evaluator or explicit acceptance pass records evidence, defects, verdicts, or retry conditions.
- Update `docs/live/todo.md` when priorities or next actions change.
- Update `docs/reference/architecture.md` when boundaries, invariants, or major component relationships change.
- Update `docs/reference/codemap.md` when high-value paths, entrypoints, or subsystem locations change materially.
- Update `docs/reference/memory.md` when a decision, policy, or truth should persist beyond the current session.
- Update `docs/reference/lessons.md` when a mistake, anti-pattern, failed attempt, or hard-won fix is worth preserving.
- Keep every update concise so the next session can recover state quickly.

## Reference Writeback Gate
- Before yielding after meaningful work, explicitly decide whether any `docs/reference/*` file must change; do not leave this to user prompting or memory.
- If the change introduces or revises a durable default, policy, packaging rule, routing rule, or repo truth, update `docs/reference/memory.md`.
- If the change introduces or revises a reusable mistake pattern, false start, migration regret, anti-pattern, or hard-won fix, update `docs/reference/lessons.md`.
- If the change alters system boundaries, family ownership, component relationships, or other invariants, update `docs/reference/architecture.md`.
- If the change alters high-value entrypoints, package locations, router locations, or where a subsystem lives, update `docs/reference/codemap.md`.
- If none of those files need changes, state that conclusion explicitly in your working notes before completion: `No reference-doc update needed because ...`.
- Path-based default: if you changed skill packages, router metadata, or package layout under `.agents/skills/`, assume a `docs/reference/*` review is required and write down why each relevant reference doc did or did not change.