# Repo Documentation Guide

## Local Scope

This subtree owns the root repository's active live docs and durable reference docs.

## Owns

- `live/` as the active repo-runtime continuity surface
- `reference/` as the durable repo truth surface

## Does Not Own

- template docs under `templates/base/docs/`
- repo-local skills under `.agents/`

## Required Reads

1. Read root `AGENTS.md` first.
2. Read `live/AGENTS.md` before relying on or changing `docs/live/*`.
3. Read `reference/AGENTS.md` before changing `docs/reference/*`.

## Local Update Rules

- Keep repo live docs active and truthful; they are not inert template scaffolds.
- Add a new local guide below `docs/` only when a durable boundary is real and will be re-entered later.
- When a docs boundary changes, update the root discovery index in the same change.

## Failure Modes to Avoid

- reading `templates/base/docs/live/*` as if it were active repo state
- storing durable policy in `docs/live/*`
- storing transient task state in `docs/reference/*`
