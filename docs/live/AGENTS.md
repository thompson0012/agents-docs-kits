# Repo Live Docs Guide

## Local Scope

These files carry the root repository's active runtime state across sessions.

## Owns

- `current-focus.md` for the active objective, scope, and constraints
- `progress.md` for continuity, touched files, verification, and next action
- `todo.md` for prioritized follow-up work when multiple next actions exist

## Does Not Own

- durable policy, architecture, or lessons
- template live-doc scaffolds under `templates/base/docs/live/`

## Required Reads

1. Read root `AGENTS.md` first.
2. Read this file before relying on `current-focus.md`, `progress.md`, or `todo.md`.
3. Re-read `current-focus.md` if work expands beyond the current scope.

## Local Update Rules

- Update `progress.md` after meaningful work with current state, touched files, verification, and next action.
- Update `current-focus.md` only when the active objective, scope, constraints, or success criteria change.
- Update `todo.md` only when prioritization or next actions materially change.

## Failure Modes to Avoid

- writing durable rules or system boundaries into live docs
- treating stale progress notes as permission to skip fresh verification
- confusing these active repo files with the inert template live-doc scaffolds
