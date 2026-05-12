---
name: agentic-engineering-principles
description: Use when designing APIs, making architectural decisions, adding features, writing implementation code, or reviewing code. Provides guardrails that steer AI toward minimal, evidence-driven, composable primitives and away from over-design, speculative abstraction, and pattern-mapping.
version: 1.0.0
---

# Agentic Engineering Principles

Use this skill when any code, design, or architectural decision is being made — during implementation, proposal, review, or brainstorming.

## Core Rule (Overrides All Others)

**Useful > Correct.**

When minimalism and usefulness conflict, pick useful. Architecturally "correct" code that nobody can use is wrong.

## When to Apply

Apply these principles the moment you reach for:

- A new function, class, module, or abstraction layer
- A new config file, environment variable, or build step
- An interface with only one implementation
- A parameter you're adding "just in case"
- Code you're keeping "because it might be useful later"
- A pattern from another framework you're about to map onto this one

## Quick Check (Before Every Change)

Answer these four questions before committing any code:

1. Where's the caller-side code? Does it actually work?
2. Which concrete use case requires this addition?
3. Can this be solved at a lower level? (parameter > method > class > module > new layer)
4. Am I making a composition decision the user should make?

## Detailed Principles

See [references/principle-details.md](references/principle-details.md) for the full set of 16 principles across design thinking, architecture, decision discipline, debuggability, and performance.

See [references/anti-patterns.md](references/anti-patterns.md) for the table of patterns to actively avoid.

## Execution Mode

When this skill is active:

1. **Before writing code** — run the four quick-check questions
2. **After writing code** — scan for removable code, unused abstractions, unnecessary indirection
3. **During review** — ask: "What was added, and what can be removed?"
4. **When document grows** — stop and ask why. Good design shrinks documentation.

## Decision Tree

```
Adding something?
├── Does a concrete use case exist? → NO → Don't add
├── Can existing API handle it? → YES → Don't add
├── Can it be a parameter instead of a method? → YES → Add parameter
├── Can it be a method instead of a class? → YES → Add method
├── Can it be a class instead of a module? → YES → Add class
└── None of the above → Add module (last resort)

Keeping something around?
├── Is it tested through a real use case? → NO → Delete it
├── Does it have only one implementation? → YES → Inline it
└── Would the user miss it? → NO → Delete it
```
