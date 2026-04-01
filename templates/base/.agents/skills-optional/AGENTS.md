# Optional Skills Guide

This `AGENTS.md` extends `../AGENTS.md`. Root constitutional rules cannot be overridden.

## Local Scope

This directory contains the template's optional top-level skill packages. Inventory only the immediate child directories here and ignore filesystem noise such as `.DS_Store`.

## Owns

- the immediate child directories in this folder as optional top-level packages
- the truthful optional inventory for packages that are not part of shipped default truth

## Does Not Own

- the shipped default inventory under `../skills/`
- nested child inventories owned by individual optional packages

## Required Reads

1. Read `../AGENTS.md` first.
2. Read `../../AGENTS.md` when a package move affects the wider `.agents/` boundary.
3. Read the target package's `SKILL.md` before editing that package.

## Local Update Rules

- Packages in this directory are not part of shipped default truth unless a downstream repo both includes and enables them.
- Shipped inventories must not claim these optional packages by default.
- When an optional package is promoted into the default shipped surface, update every affected inventory in the same change.

## Failure Modes to Avoid

- describing optional packages as shipped default truth
- moving a package into the shipped surface without updating the shipped inventory
- treating nested package contents as if they were top-level optional packages

## Current Top-Level Directories

- `coding-and-data/`
- `cx-ticket-triage/`
- `data-exploration/`
- `feature-spec/`
- `media/`
- `using-documents/`
- `using-finance/`
- `using-legal/`
- `using-marketing/`
- `using-research/`
- `using-sales/`
- `visualization/`
- `website-building/`