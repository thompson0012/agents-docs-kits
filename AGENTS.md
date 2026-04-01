# Project Agent Guide

## Repo Purpose

This repository uses a layered guidance system for recall, progressive disclosure, and reliable hand-off across active repo work and template-package work.

## Startup Minimum

### repo work

Read these in order before acting on repo-runtime or repo-governance work:
1. `AGENTS.md`
2. `docs/live/current-focus.md`
3. `docs/live/progress.md`

Then read the smallest local guide for the subtree you will touch.

### template work

Read these in order before acting under `templates/base/`:
1. `AGENTS.md`
2. `docs/live/current-focus.md`
3. `docs/live/progress.md`
4. `templates/base/AGENTS.md`

Then read the indexed template-local guide for the subtree you will touch.

## Scope Fences

- Repo work uses root `docs/live/*` as active state and root `docs/reference/*` as durable truth.
- Template work uses `templates/base/**` guidance; template live docs remain inert scaffolds until a copied repo localizes them.
- Do not treat `templates/base/docs/live/*` as active repo state.

## Decision Order

Apply these checks in order.

1. If the task changes `AGENTS.md`, local-guide boundaries, routing metadata, or doc-governance ownership, route to `.agents/skills/using-agents-md/SKILL.md`.
2. If the task touches root docs, read `docs/AGENTS.md` first, then `docs/live/AGENTS.md` or `docs/reference/AGENTS.md` as needed.
3. If the task touches repo-local skills or router metadata under `.agents/`, read `.agents/AGENTS.md` first, then `.agents/skills/AGENTS.md` when working inside `.agents/skills/`.
4. If the task touches `templates/base/`, read `templates/base/AGENTS.md` first, then follow its discovery index.
5. If no repo-local surface fits, use the narrowest user/global skill that matches the task.

## Escalation Rules

- Ambiguous route: choose the smaller owning surface first, then record the cross-boundary decision in `docs/live/progress.md` if the work expands.
- Missing repo-local skill or guide path: do not silently improvise. Repair the pointer if you are changing governance, or fall back to the nearest owning guide and record the gap in `docs/live/progress.md`.
- Conflicting guidance: root `AGENTS.md` wins over deeper repo guides; `templates/base/AGENTS.md` wins only inside the template subtree.
- Interrupted governed work: rerun the relevant startup minimum and the reference writeback gate before yielding.

## Failure Modes to Avoid

- skipping the startup minimum because the task feels routine
- treating template live-doc scaffolds as if they were active repo truth
- editing a governed subtree without reading its nearest local guide
- changing skill paths, router metadata, or high-value entrypoints without reviewing `docs/reference/*`
- adding a leaf `AGENTS.md` for a transient folder or single-file rule
- silently falling back to generic behavior when a repo-local pointer is stale or missing

## Verification for Router Changes

For root AGENTS/router-governance changes, run:
- `python3 -m unittest scripts.tests.test_agents_router`
- `python3 scripts/validate_agents_router.py`
- `git diff --check`

## Update Rules After Meaningful Work

- Update `docs/live/current-focus.md` when the active objective, scope, constraints, or success criteria change.
- Update `docs/live/progress.md` after meaningful work with current state, completed work, blockers, touched files, verification, and next recommended action.
- Update `docs/live/todo.md` when priorities or next actions change materially.
- Update `docs/reference/architecture.md` when system boundaries, invariants, or component relationships change.
- Update `docs/reference/codemap.md` when high-value entrypoints, package locations, or subsystem paths change.
- Update `docs/reference/memory.md` when a durable decision, policy, or repo truth should persist beyond the current session.
- Update `docs/reference/lessons.md` when a reusable mistake pattern, anti-pattern, or hard-won fix is worth preserving.

## Reference Writeback Gate

- Before yielding after meaningful work, explicitly decide whether any `docs/reference/*` file must change.
- If the change introduces or revises a durable default, policy, packaging rule, routing rule, or repo truth, update `docs/reference/memory.md`.
- If the change introduces or revises a reusable mistake pattern or anti-pattern, update `docs/reference/lessons.md`.
- If the change alters boundaries, family ownership, or component relationships, update `docs/reference/architecture.md`.
- If the change alters high-value entrypoints, package locations, router metadata, or where a subsystem lives, update `docs/reference/codemap.md`.
- If none of those files need changes, state: `No reference-doc update needed because ...`.
- Path-based default: if you changed skill packages or router metadata under `.agents/`, assume a `docs/reference/*` review is required and record why each relevant file did or did not change.

## Discovery Index

| Topic | Location |
| --- | --- |
| Repo agent subtree | `.agents/AGENTS.md` |
| Repo skill inventory | `.agents/skills/AGENTS.md` |
| Repo router manifest | `.agents/router-manifest.json` |
| Repo docs subtree | `docs/AGENTS.md` |
| Repo live-doc rules | `docs/live/AGENTS.md` |
| Repo reference-doc rules | `docs/reference/AGENTS.md` |
| Template constitutional root | `templates/base/AGENTS.md` |