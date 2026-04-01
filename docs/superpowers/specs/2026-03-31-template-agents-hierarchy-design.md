# Template AGENTS Hierarchy Design Spec

Date: 2026-03-31
Status: Draft approved for spec review

## Summary

Redesign the template AGENTS hierarchy so the root `AGENTS.md` acts as constitutional law and the top-level index, while a small number of stable subdirectory `AGENTS.md` files define local rules only where those rules genuinely diverge.

The design is optimized for the repository's critical success condition: `templates/base` must copy cleanly into downstream repos without leaking false state, stale inventories, or misleading workflow guidance. In particular, the template's live-doc surfaces must remain inert scaffolds until the copied repo localizes them.

A new hard requirement from the design review is that the root `AGENTS.md` must explicitly point to every must-read local `AGENTS.md`. If a local guide is required for correct work in a subtree, the root guide must make that discoverable rather than assuming an agent will stumble into it.

## Problem

The current repository already benefits from a split between a constitutional root and lower-level workflow guides, but the template system needs a stronger, more explicit architecture.

Without a disciplined hierarchy, several failure modes recur:

1. The root guide grows into a noisy operational manual instead of a strict first-read law and index.
2. Local guides appear in ad hoc places, become orphaned, or describe folders that are not durable boundaries in copied repos.
3. Template live docs look plausible enough that agents treat scaffold content as real project state.
4. Skill inventories and routing docs claim packages or surfaces that are planned, optional, deleted, or simply absent in the copied repo.
5. Partial subtree copies silently break parent-relative assumptions without any explicit revalidation rule.

The design must preserve the template as a truthful source scaffold rather than a half-live project snapshot.

## Goals

1. Keep the root `AGENTS.md` as the first rule layer and primary index.
2. Introduce local `AGENTS.md` files only at stable copied boundaries with real rule divergence.
3. Make template live docs explicitly inert until localized in the downstream repo.
4. Separate shipped and optional agent-package truth structurally, not just editorially.
5. Require the root guide to point to every must-read local `AGENTS.md`.
6. Keep the hierarchy shallow enough that agents can navigate it reliably.
7. Preserve truth after full-template copy into downstream repos.

## Non-Goals

- Do not put `AGENTS.md` in every folder.
- Do not add per-skill-family or per-leaf-skill guides unless those leaves become real governance boundaries later.
- Do not prefill template live docs with plausible project-specific content.
- Do not treat optional skill packages as part of shipped default truth.
- Do not claim partial subtree copy is fully supported without revalidation.

## Design Principles

### 1. Root is law, not a dumping ground

The root guide owns only rules that must apply everywhere:
- startup read order
- skill invocation precedence
- injected-context contract
- hierarchical discovery
- live-doc writeback obligation
- reference writeback gate
- cross-system precedence
- discovery index for all must-read local guides

The root guide should not absorb detailed operational semantics that belong to stable subtrees.

### 2. Local guides exist only at durable boundaries

A folder earns a local `AGENTS.md` only if all three are true:
1. it survives into downstream repos as a recognizable boundary,
2. it has rules meaningfully different from its parent,
3. those rules are important enough that leaving them only in the parent would mislead agents.

This rule keeps the hierarchy sparse and prevents drift from decorative local guides.

### 3. Structure truth and runtime truth must stay separate

Structure truth can ship in the template:
- `AGENTS.md`
- local subtree `AGENTS.md`
- `docs/reference/*`
- skill inventories that describe what actually exists in the template

Runtime truth must not be prefilled with plausible content:
- `docs/live/current-focus.md`
- `docs/live/progress.md`
- `docs/live/todo.md`
- `docs/live/roadmap.md`
- `docs/live/runtime.md`
- `docs/live/qa.md`

### 4. Truth beats convenience

Inventory-like docs must only name:
- files that exist now, or
- surfaces explicitly labeled as planned or optional.

The hierarchy should never rely on an agent inferring which references are aspirational.

## Proposed Layout

```text
templates/base/
├── AGENTS.md
├── docs/
│   ├── AGENTS.md
│   ├── live/
│   │   ├── AGENTS.md
│   │   ├── current-focus.md
│   │   ├── progress.md
│   │   ├── todo.md
│   │   ├── roadmap.md
│   │   ├── runtime.md
│   │   └── qa.md
│   └── reference/
│       ├── AGENTS.md
│       ├── architecture.md
│       ├── codemap.md
│       ├── memory.md
│       ├── lessons.md
│       ├── implementation.md
│       └── design.md
└── .agents/
    ├── AGENTS.md
    ├── skills/
    │   ├── AGENTS.md
    │   └── ...
    └── skills-optional/
        ├── AGENTS.md
        └── ...
```

## Ownership by Layer

### `templates/base/AGENTS.md`

Owns constitutional rules and the root discovery contract.

Required behavior:
- name every must-read local `AGENTS.md` in the root discovery index,
- distinguish between the existence of a subtree and the requirement to read that subtree's guide,
- remain short enough to scan before every session.

The root guide should link at minimum to:
- `docs/AGENTS.md`
- `docs/live/AGENTS.md`
- `docs/reference/AGENTS.md`
- `.agents/AGENTS.md`
- `.agents/skills/AGENTS.md`
- `.agents/skills-optional/AGENTS.md`

If later design work introduces another must-read local guide, the root discovery index must be updated in the same change.

### `templates/base/docs/AGENTS.md`

Owns documentation workflow:
- read order by task type,
- distinction between live and reference docs,
- update timing rules,
- treatment of planned documentation surfaces.

### `templates/base/docs/live/AGENTS.md`

Owns live-doc scaffold behavior and is the main guardrail for template safety.

It should define:
- template live docs are inert scaffolds,
- placeholder text must not be treated as active repo state,
- which live docs are required immediately after copy,
- which files may remain planned until a downstream repo activates that workflow,
- the minimum localization pass required before an agent can trust live docs.

### `templates/base/docs/reference/AGENTS.md`

Owns durable truth policy:
- what belongs in `architecture.md`, `codemap.md`, `memory.md`, and `lessons.md`,
- what should never be written into reference docs,
- reference writeback expectations after meaningful changes.

### `templates/base/.agents/AGENTS.md`

Owns the `.agents/` package boundary:
- what `.agents/` contains,
- how shipped and optional surfaces differ,
- what must stay truthful after copy,
- revalidation expectations after structural edits.

### `templates/base/.agents/skills/AGENTS.md`

Owns shipped-skill truth:
- only inventory the shipped skill surface,
- do not claim absent skills,
- require same-change updates when the shipped skill surface changes.

### `templates/base/.agents/skills-optional/AGENTS.md`

Owns optional-package semantics:
- optional skills are not part of shipped default truth,
- copied repos must not claim optional skills unless they are actually present and enabled,
- enabling optional packages requires updating the relevant local inventories and discovery docs.

## Copy Lifecycle Model

### State 1: Template state

Inside `templates/base`, files are scaffolds and guidance surfaces.

Requirements:
- local `AGENTS.md` files may ship because they describe structure truth,
- live docs must remain inert,
- any planned or optional surface must be labeled as such.

### State 2: Copied repo, pre-localization

Immediately after copy, the downstream repo has structure but not yet trustworthy runtime state.

Requirements:
- copied `AGENTS.md` files survive as guidance,
- copied `docs/live/*` files are still scaffolds until localized,
- agents must not infer an active objective or progress record from placeholder text.

### State 3: Localized repo

After localization:
- live docs contain real project state,
- local inventories describe the repo that actually exists,
- optional surfaces are either enabled and documented or absent and unclaimed,
- the copied AGENTS hierarchy now describes the downstream repo honestly.

## Guardrails

### 1. Boundary test before adding a local guide

No new local `AGENTS.md` without the three-part durable-boundary test.

### 2. Root-to-local must-read indexing

If a local `AGENTS.md` is required reading for correct work in a subtree, the root `AGENTS.md` must point to it explicitly.

This is a hard rule, not a suggestion.

The purpose is to prevent a copied repo from having hidden law surfaces that only experienced maintainers know about.

### 3. No false inventories

Inventory-style docs must never blur present, planned, and optional surfaces.

### 4. Inert live docs only

Template live docs must not contain:
- fake active objectives,
- fake completed work,
- plausible handoff notes,
- seeded progress entries that look live.

### 5. No orphaned local guides

If a local `AGENTS.md` exists, its parent and root discovery paths must make it discoverable according to the must-read rule.

### 6. Shipped and optional stay separate

Do not describe optional packages through shipped inventories or shipped subtree guides.

## Edge Cases and Expected Behavior

### Partial subtree copy

Unsupported by default.

If someone copies only part of the template tree, all parent-relative assumptions and local discovery paths must be revalidated before agents rely on them.

### Downstream repo deletes optional subtree

Expected behavior:
- shipped guides still tell the truth,
- no shipped inventory breaks,
- nothing claims optional packages are available by default.

### Downstream repo adds a new subsystem

Expected behavior:
- add a local `AGENTS.md` only if that subsystem passes the durable-boundary test,
- update parent discovery,
- update the root discovery index if the new local guide is must-read.

### Downstream repo renames folders

Expected behavior:
- parent-relative local guide references must be revalidated,
- this is a localization responsibility, not a template bug.

### Template evolves faster than copied repos

Expected behavior:
- downstream repos may diverge,
- template guides remain truthful scaffolds,
- copied repos are responsible for their own localized truth.

## Recommended Canonical Boundaries

These local guides should exist in the template:
- `templates/base/docs/AGENTS.md`
- `templates/base/docs/live/AGENTS.md`
- `templates/base/docs/reference/AGENTS.md`
- `templates/base/.agents/AGENTS.md`
- `templates/base/.agents/skills/AGENTS.md`
- `templates/base/.agents/skills-optional/AGENTS.md`

These should not exist yet:
- per-skill-family local guides,
- per-leaf-skill local guides,
- local guides in utility folders with no distinct contract.

## Validation Checklist

Use this checklist whenever the template AGENTS hierarchy changes:

- [ ] Root `AGENTS.md` remains constitutional and index-like.
- [ ] Root discovery index points to every must-read local `AGENTS.md`.
- [ ] Each local guide sits at a durable copied boundary.
- [ ] Each local guide owns rules that genuinely diverge from the parent.
- [ ] Template live docs remain inert and non-plausible as project state.
- [ ] Inventory docs distinguish present vs planned vs optional surfaces.
- [ ] Shipped and optional agent-package surfaces stay structurally separate.
- [ ] Partial-copy behavior is documented as requiring revalidation.
- [ ] No orphaned local `AGENTS.md` files exist.

## Rollout Recommendation

Implement the new hierarchy in this order:

1. tighten `templates/base/AGENTS.md` so it explicitly indexes all must-read local guides,
2. add `templates/base/docs/live/AGENTS.md`,
3. add `templates/base/docs/reference/AGENTS.md`,
4. add `templates/base/.agents/AGENTS.md`,
5. add `templates/base/.agents/skills/AGENTS.md`,
6. add `templates/base/.agents/skills-optional/AGENTS.md`,
7. validate every concrete path and every planned-surface label in one pass,
8. re-audit the copied-template truth model before merging.

## Decision

Adopt the stable-boundary hybrid hierarchy.

It gives the template system the strongest protection against false live state and stale local guidance while keeping the root guide small, authoritative, and effective as the first-read index.