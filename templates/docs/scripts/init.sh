#!/usr/bin/env sh
set -eu

# Fresh scaffold invariants:
# - new projects start with no active or parked workstream and no archive history
# - `.harness/` and `docs/archive/` stay empty until real work creates artifacts
# - the files written below are the canonical blank defaults

ensure_dir() {
  dir="$1"
  if [ ! -d "$dir" ]; then
    mkdir -p "$dir"
    printf 'created %s\n' "$dir"
  fi
}

write_file_if_missing() {
  path="$1"
  content="$2"

  if [ -e "$path" ]; then
    printf 'kept %s\n' "$path"
    return
  fi

  parent=$(dirname "$path")
  ensure_dir "$parent"
  printf '%s' "$content" > "$path"
  printf 'created %s\n' "$path"
}

# Topology directories
ensure_dir ".harness"
ensure_dir "docs/archive"
ensure_dir "docs/live"
ensure_dir "docs/reference"

# 7 phase directories
for phase in thesis challenge response synthesis contract build audit; do
  ensure_dir ".agents/skills/using-agents-stack/$phase"
done

# Reference files
ensure_dir ".agents/skills/using-agents-stack/references/templates/.harness"

# Live state
write_file_if_missing "docs/live/tracked-work.json" '{
  "active_workstream_id": null,
  "parked_workstream_ids": [],
  "workstreams": {}
}'

write_file_if_missing "docs/live/plan.md" '# Plan

## Why
<!-- Source goal: what problem does this project solve? -->

## What
- Active workstream: none
- Current layer: —
- Current phase: —
- Depth: 0
- Strongest artifact: —

## Next
- Immediate next action: create first workstream in tracked-work.json
- Blockers: none

## Lessons
<!-- Cross-workstream learnings -->
'

# status.json template
write_file_if_missing ".agents/skills/using-agents-stack/references/templates/.harness/status.json" '{
  "workstream_id": "",
  "depth": 0,
  "layer": "",
  "phase": "",
  "attempt": 0,
  "max_attempts": 3,
  "max_depth": 6,
  "blocked_reason": null
}'

# Reference docs
write_file_if_missing "docs/reference/architecture.md" '# Architecture Reference

Describe the project-specific runtime, entrypoints, major subsystem boundaries, integration boundaries, and orchestration rules.
'

write_file_if_missing "docs/reference/design.md" '# Design Reference

Describe the project-specific product intent, interaction model, visual system, and notable constraints.
'

printf '\nScaffold complete. Ready for first workstream.\n'
