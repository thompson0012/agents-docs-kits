# Shipped Skills Guide

This `AGENTS.md` extends `../AGENTS.md`. Root constitutional rules cannot be overridden.

## Local Scope

This directory contains the template's shipped top-level skill packages. Inventory only the immediate child directories here and ignore filesystem noise such as `.DS_Store`.

## Owns

- the immediate child directories in this folder as shipped top-level packages
- the truthful shipped inventory for the template's default skill surface

## Does Not Own

- optional packages under `../skills-optional/`
- nested child inventories owned by individual router packages

## Required Reads

1. Read `../AGENTS.md` first.
2. Read `../../AGENTS.md` when package-surface changes affect the wider `.agents/` boundary.
3. Read the target package's `SKILL.md` before editing that package.

## Local Update Rules

- Keep the inventory truthful to the actual immediate child directories in this folder.
- Do not claim packages that live only in `../skills-optional/` as part of the shipped default surface.
- When the shipped top-level package surface changes, update this file in the same change.

## Failure Modes to Avoid

- leaving removed packages listed as shipped
- promoting an optional package into shipped truth without updating both inventories
- treating nested router children as if they were top-level shipped packages

## Current Top-Level Directories

- `context-compaction/`
- `create-router-skill/`
- `create-skill/`
- `delivery-control/`
- `labs21-product-suite/`
- `meta-prompting/`
- `prompt-augmentation/`
- `self-cognitive/`
- `startup-pressure-test/`
- `using-design/`
- `using-labs21-suite/`
- `using-reasoning/`