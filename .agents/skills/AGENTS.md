# Repo Skills Guide

## Local Scope

This directory contains the root repository's shipped repo-local skill packages.

## Owns

- the immediate child skill directories in `.agents/skills/`
- the entrypoint SKILL files those directories expose

## Does Not Own

- `.agents/router-manifest.json`
- user-installed skills outside the repository
- template skill packages under `templates/base/.agents/skills/`

## Required Reads

1. Read root `AGENTS.md` first.
2. Read `.agents/AGENTS.md` before changing inventory or ownership under this subtree.
3. Read the target package's `SKILL.md` before editing that package.

## Local Update Rules

- Keep this inventory truthful to the actual immediate child directories in `.agents/skills/`.
- When a skill package is added, removed, renamed, or repurposed, update this guide, root `AGENTS.md`, `.agents/router-manifest.json`, and `docs/reference/codemap.md` in the same change.
- If a repo-local skill changes durable governance policy, review `docs/reference/memory.md` too.

## Failure Modes to Avoid

- claiming a skill package that does not exist
- updating only the skill package and forgetting the root or manifest pointers
- treating user/global skills as if they were part of this repo inventory

## Current Top-Level Directories

- `using-agents-md/`
