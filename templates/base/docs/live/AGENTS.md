# Live Docs Guide

This `AGENTS.md` extends `../AGENTS.md`. Root constitutional rules cannot be overridden.

## Local Scope

These files are runtime-state scaffolds for copied repos. In the template, they must remain inert until a downstream repo localizes them.

## Owns

- the inert scaffold contract for `current-focus.md`, `progress.md`, `todo.md`, `roadmap.md`, `runtime.md`, and `qa.md`
- the rule that copied repos must localize these files before relying on them as truth

## Does Not Own

- active repo-runtime state in the root repository
- durable reference policy under `../reference/`

## Required Reads

1. Read `../AGENTS.md` first.
2. Read this file before relying on any file under `docs/live/`.
3. Re-read the template root guide if copied-repo localization changes the contract.

## Local Update Rules

- Do not treat placeholder labels as active repo state.
- Do not seed fake objectives, progress, blockers, or handoff notes.
- `roadmap.md`, `runtime.md`, and `qa.md` may remain planned or unused in a downstream repo until that workflow is activated.

## Failure Modes to Avoid

- shipping plausible-looking live state inside the template
- treating copied-repo truth as if it should flow back into the inert template scaffold
- storing durable policy here instead of in reference docs