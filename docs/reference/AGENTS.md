# Repo Reference Docs Guide

## Local Scope

These files store durable repo truth that should survive across sessions.

## Owns

- `architecture.md` for system boundaries and invariants
- `codemap.md` for high-value paths and entrypoints
- `implementation.md` for durable technical execution details
- `design.md` for durable product or behavior rules
- `memory.md` for persistent decisions and policies
- `lessons.md` for reusable mistakes and anti-patterns

## Does Not Own

- active runtime progress or blockers
- template durable docs under `templates/base/docs/reference/`

## Required Reads

1. Read root `AGENTS.md` first.
2. Read this file before updating any `docs/reference/*` file.
3. Read the specific target reference file that matches the change you are making.

## Local Update Rules

- Keep only durable truth here; do not store transient task state.
- Review this subtree after skill-package, router-manifest, path, or governance-boundary changes.
- When a change alters both durable policy and repeatable procedure, update the relevant reference doc and skill in the same change.

## Failure Modes to Avoid

- updating `memory.md` without also updating the owning skill or root pointer when procedure changed too
- leaving stale entrypoints or paths in `codemap.md`
- recording temporary blockers, progress, or handoff notes in durable reference docs
