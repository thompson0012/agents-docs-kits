# Repo Agent Subtree Guide

## Local Scope

This subtree owns repo-local skills and machine-readable routing metadata for the root repository.

## Owns

- `.agents/skills/` as the repo-local skill inventory
- `.agents/router-manifest.json` as the machine-readable routing manifest for root governance surfaces

## Does Not Own

- root `docs/live/*` session state
- root `docs/reference/*` durable truth
- any guidance under `templates/base/`

## Required Reads

1. Read root `AGENTS.md` first for startup order, scope fences, and escalation rules.
2. Read `skills/AGENTS.md` before acting under `.agents/skills/`.
3. Use `router-manifest.json` when checking which repo-governance surface owns a task.

## Local Update Rules

- Keep `.agents/router-manifest.json` aligned with the real repo entrypoints it advertises.
- When a repo-local skill path or ownership boundary changes, update root `AGENTS.md` and `docs/reference/codemap.md` in the same change.
- Do not hide must-read repo guidance in unindexed files under this subtree.

## Failure Modes to Avoid

- leaving stale router paths in the manifest after moving a repo-local skill
- treating this subtree as if it also governed template-package skills
- changing repo-local skill ownership without reviewing the root discovery index and codemap
