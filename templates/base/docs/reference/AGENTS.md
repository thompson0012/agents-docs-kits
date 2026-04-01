# Reference Docs Guide

This `AGENTS.md` extends `../AGENTS.md`. Root constitutional rules cannot be overridden.

## Local Scope

These files store durable template truth, not transient or live session state.

## Owns

- `architecture.md` for template system boundaries and invariants
- `codemap.md` for high-value template paths and entrypoints
- `implementation.md` for technical execution details and operator-facing procedures
- `design.md` for product intent, UX behavior, and other design rules
- `memory.md` for durable decisions and policies
- `lessons.md` for reusable mistakes and anti-patterns

## Does Not Own

- transient task state or live session progress
- copied-repo runtime state after localization

## Required Reads

1. Read `../AGENTS.md` first.
2. Read this file before updating `docs/reference/*`.
3. Read the specific target reference file that matches the durable change.

## Local Update Rules

- Keep only durable truth here.
- Do not write transient task state into reference docs.
- Review this subtree whenever template package boundaries, live-doc contracts, or shipped-vs-optional truth changes.

## Failure Modes to Avoid

- recording temporary blockers or handoff notes in durable docs
- leaving stale paths or ownership claims after package/layout changes
- updating only one durable truth surface when the same change altered multiple reference boundaries