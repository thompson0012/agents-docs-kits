# Objective Ledger

> **Version**: 1.0.0  
> **Status**: PRODUCTION  
> **Last Updated**: 2026-02-24

Single source of truth for task objectives, scope, and checkpoints. Prevents drift in long-running tasks.

---

## Schema

```yaml
ledger:
  task_id: string           # Unique identifier
  created_at: ISO8601       # Creation timestamp
  updated_at: ISO8601       # Last update timestamp
  
  objective:
    summary: string         # One-line objective
    details: string         # Detailed description
    success_criteria:       # List of completion criteria
      - string
    
  scope:
    in_scope:              # What's included
      - string
    out_of_scope:          # Explicitly excluded
      - string
    constraints:           # Technical/business constraints
      - string
      
  checkpoints:
    - id: number              # Sequential checkpoint ID
      timestamp: ISO8601      # When recorded
      type: time|milestone|drift_detected  # Why recorded
      summary: string         # What was accomplished
      decisions:              # Key decisions made
        - string
      drift_flags:            # Any objective/scope drift
        - string
      next_steps: string      # Immediate next actions
      
  status: active|completed|blocked|abandoned
  final_summary: string     # Filled on completion
```

---

## Architecture

```
[Task Start]
    |
    v
+------------------+      +------------------------+
| Create Ledger    |----->| Initialize Fields      |
|                  |      | - objective            |
|                  |      | - scope                |
|                  |      | - constraints          |
+------------------+      +------------------------+
         |
         v
+------------------+      +------------------------+
| Work Loop        |----->| Drift Detector         |
| (execute tasks)  |      | - compare to objective |
|                  |      | - flag divergence      |
+------------------+      +-----------+------------+
         |                            |
         v                            v
+------------------+      +------------------------+
| Record Checkpoint|<-----+ Log checkpoint details |
|                  |      | - summary              |
| - time-based     |      | - decisions            |
| - milestone      |      | - drift flags          |
| - drift detected |      | - next steps           |
+------------------+      +------------------------+
         |
         v
+------------------+
| Task Complete    |
| - final summary  |
| - lessons learned|
+------------------+
```

---

## Checkpoint Rules

**Trigger Conditions:**
1. **Time-based**: Every 20-30 minutes of continuous work
2. **Milestone-based**: After completing a significant sub-task
3. **Drift-detected**: When objective/scope divergence is identified

**Required Fields per Checkpoint:**
- `summary`: What was accomplished since last checkpoint
- `decisions`: Key decisions made (can be empty)
- `drift_flags`: Any deviations from objective/scope
- `next_steps`: Immediate next actions

---

## Drift Detection

**What counts as drift:**
- Work expanding beyond `in_scope` items
- Technical decisions conflicting with `constraints`
- Success criteria becoming unclear or unachievable
- External requirements changing mid-task

**Process when drift detected:**
1. Record drift in checkpoint `drift_flags`
2. Pause and assess: Accept, reject, or modify objective
3. If accepting: Update objective/scope with rationale
4. Log decision in checkpoint
5. Continue with updated objective

---

## Template

```markdown
# Task: [Brief Title]

> **Task ID**: [uuid or short-id]  
> **Created**: [ISO8601]  
> **Updated**: [ISO8601]  
> **Status**: active

## Objective

**Summary**: [One-line objective]

**Details**: [Detailed description of what needs to be done]

**Success Criteria**:
- [ ] [Criterion 1]
- [ ] [Criterion 2]
- [ ] [Criterion 3]

## Scope

**In Scope**:
- [Item 1]
- [Item 2]

**Out of Scope**:
- [Item A - explicitly excluded]
- [Item B - future work]

**Constraints**:
- [Technical constraint 1]
- [Business constraint 2]

## Checkpoints

### Checkpoint 1: [timestamp]

**Type**: time|milestone|drift_detected

**Summary**: [What was accomplished]

**Decisions**:
- [Decision 1 with rationale]
- [Decision 2 with rationale]

**Drift Flags**:
- [None]
- OR: [Description of drift + resolution]

**Next Steps**: [Immediate actions to take]

---

## Final Summary

[Completed only when status = completed]

**Outcome**: [Success/failure description]
**Lessons**: [What was learned]
**Follow-up**: [Any deferred work]
```

---

## Integration

- **Created by**: Session bootstrap when new task starts
- **Updated by**: Agent during checkpoints
- **Read by**: Session bootstrap to resume tasks
- **Stored**: `.agents/docs/ledgers/[task-id].md`

**Active Task Ledger**: Linked from `.agents/docs/PROGRESS.md`