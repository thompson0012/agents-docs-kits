# agents-docs-kits

Minimal agent docs kit for context injection, progressive disclosure, and reliable hand-off.

## Quick start

```bash
npx degit <owner>/<repo>/templates/base my-project
```

Then fill in the generated files:

- `AGENTS.md` — your project's retrieval contract (the only always-injected file)
- `docs/live/*` — current execution state (`current-focus`, `progress`, `todo`; add `roadmap` when the work is phased)
- `docs/reference/*` — durable project context (`architecture`, `codemap`, `memory`, `lessons`)

## If you want to…

| Goal | Start here |
|------|-----------|
| Use the shipped skill suite | Read `.agents/skills/using-labs21-suite/SKILL.md` — it routes across the current top-level families and direct leaves |
| Route design work | `using-design` — design foundations, tokens, generative UI, liquid-glass |
| Route analytical work | `using-reasoning` — calibration, framing, foresight, reality checks, advisory, multi-lens |
| Route software delivery | `delivery-control` — discovery, harness design, plan review, frontend evaluation, readiness |
| Track phased work | `docs/live/roadmap.md` |
| Start a new product from idea to architecture | `labs21-product-suite` — strategy → PRD → system architecture |
| Run a startup viability teardown | `startup-pressure-test` |
| Design or repair a prompt artifact | `meta-prompting` / `prompt-augmentation` |
| Author a reusable skill package | `create-skill` (leaf) / `create-router-skill` (router) |
| Compact context for handoff | `context-compaction` |
| Run a confidence or preflight check | `self-cognitive` |

## How progressive disclosure works

Read only what the current task needs:

1. Start with `AGENTS.md`.
2. Read `docs/live/current-focus.md` for the active objective.
3. Read `docs/live/progress.md` for continuity.
4. If the work spans phases, read `docs/live/roadmap.md`.
5. Read deeper docs only when the work requires them.

## Root-scaffold note

This `README.md` is documentation for the kit repository, not part of generated projects. If someone scaffolds from the repository root instead of `templates/base`, `degit.json` excludes this file.
