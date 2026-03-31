# Project Agent Guide

This `AGENTS.md` is the constitutional root for `templates/base`. Read it first. Local `AGENTS.md` files add subtree-specific rules and cannot override this file.

## Mandatory First Reads

1. Read this file first for any work touching `templates/base`.
2. Before acting in `.agents/`, `.agents/skills/`, `.agents/skills-optional/`, `docs/`, `docs/live/`, or `docs/reference/`, read the indexed local guide for that subtree.
3. If you copy only part of this template, revalidate every parent-relative guide path before relying on local rules.

## Skill Invocation Precedence

- Check project-local shipped skills under `.agents/skills/` before relying on generic knowledge.
- Use the most specific shipped skill that matches the task.
- Treat `.agents/skills-optional/` as opt-in surfaces, not default bundled truth.

## Injected Context Contract

- This root `AGENTS.md` is the only always-in-context index for the template hierarchy.
- Pull deeper guides and docs on demand; do not assume child guides or `docs/*` content were injected unless you read them.
- Keep the root guide short, truthful, and index-like.

## Hierarchical Discovery

- Local guides may add subtree-specific rules, but they cannot override this file.
- Every must-read local `AGENTS.md` must appear in the discovery index in the same change that adds or removes it.
- Do not hide required guidance in non-indexed leaves.

## Live-Doc Writeback Obligation

- In this template, `docs/live/` remains inert until a copied repo localizes it into real project state.
- If work changes the template live-doc contract or localization expectations, update the governing docs in the same change.
- Do not seed or preserve plausible live-doc state as shipped template truth.

## Reference Writeback Gate

- Before yielding after meaningful work, decide whether any `docs/reference/*` file must change to keep durable truth aligned.
- If no reference-doc update is needed, record that conclusion explicitly in your working notes.
- Do not describe planned or optional surfaces as shipped truth.

## Cross-System Precedence

- Root constitutional rules win over subtree guides.
- A deeper local guide may narrow behavior inside its durable boundary, but it does not own root-level policy.
- When a copied repo localizes these templates, explicit copied-repo truth beats template placeholder content.

## Discovery Index

| Topic | Location |
|-------|----------|
| Agent package boundary | `.agents/AGENTS.md` |
| Shipped skill package rules | `.agents/skills/AGENTS.md` |
| Optional skill package rules | `.agents/skills-optional/AGENTS.md` |
| Documentation workflow rules | `docs/AGENTS.md` |
| Live-doc scaffold rules | `docs/live/AGENTS.md` |
| Reference-doc rules | `docs/reference/AGENTS.md` |