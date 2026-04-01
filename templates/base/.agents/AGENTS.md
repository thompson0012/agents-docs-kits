# Agent Packages Guide

This `AGENTS.md` extends `../AGENTS.md`. Root constitutional rules cannot be overridden.

## Local Scope

This subtree defines the template's bundled agent packages.

## Owns

- `skills/` as the shipped top-level skill packages in this template
- `skills-optional/` as optional top-level packages that are shipped but not default bundled truth

## Does Not Own

- template docs under `../docs/`
- repo-root skills or router metadata outside `templates/base/`

## Required Reads

1. Read `../AGENTS.md` first.
2. Read `skills/AGENTS.md` before acting under `.agents/skills/`.
3. Read `skills-optional/AGENTS.md` before acting under `.agents/skills-optional/`.

## Local Update Rules

- Keep the split between shipped and optional package surfaces truthful.
- When a package moves between shipped and optional surfaces, update every affected inventory in the same change.
- Do not hide required template package guidance outside the indexed subtree guides.

## Failure Modes to Avoid

- describing optional packages as shipped default truth
- changing package ownership without updating the affected inventories
- treating this subtree as if it governed the template docs boundary too