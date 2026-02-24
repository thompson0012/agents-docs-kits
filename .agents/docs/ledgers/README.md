# Ledgers

> Active task objective ledgers. One file per non-trivial task.

## Naming Convention

```
[YYYY-MM-DD]-[short-task-slug].md
```

Example: `2026-02-24-agents-stack-optimization.md`

## Lifecycle

```
[Task Start]
     |
     v
+-----------------------------+
| Create ledger file          |
| from OBJECTIVE_LEDGER.md    |
| template                    |
+-----------------------------+
     |
     v
+-----------------------------+
| Update with checkpoints     |
| every 20-30 min or          |
| on milestone                |
+-----------------------------+
     |
     v
+-----------------------------+
| Mark status: completed      |
| Add final summary           |
+-----------------------------+
     |
     v
+-----------------------------+
| Archive or delete           |
| (completed tasks)           |
+-----------------------------+
```

## Rules

- One ledger per non-trivial task
- Must have objective, scope, and success_criteria before work starts
- Checkpoints required every 20-30 min or on milestone
- Drift must be recorded and resolved before continuing
- Mark `status: completed` with final summary when done

## Active Ledgers

| File | Task | Status | Created |
|------|------|--------|---------|
| `2026-02-24-agents-stack-optimization.md` | Agents stack optimization | completed | 2026-02-24 |
