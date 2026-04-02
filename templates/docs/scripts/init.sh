#!/usr/bin/env sh
set -eu

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

ensure_dir ".agents/skills/using-agents-stack"
ensure_dir ".harness"
ensure_dir "docs/archive"
ensure_dir "docs/live"
ensure_dir "docs/reference"
ensure_dir "docs/scripts"

write_file_if_missing "docs/live/features.json" '{
  "project": "Replace with project name",
  "backlog": []
}
'

write_file_if_missing "docs/live/progress.md" '# Project Progress Ledger

Record dated sprint outcomes here. Append new entries; do not rewrite history.
'

write_file_if_missing "docs/live/memory.md" '# Durable Project Memory

Capture stable repo truths, environment quirks, and lessons future agents should reuse.
'

write_file_if_missing "docs/reference/architecture.md" '# Architecture Reference

Describe the current runtime, entrypoints, and major subsystem boundaries.
'

write_file_if_missing "docs/reference/design.md" '# Design Reference

Describe the current UX intent, visual system, and product constraints.
'
