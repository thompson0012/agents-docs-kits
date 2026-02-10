# LESSONS.md — Self-Improvement & Operational Log

> **TEMPLATE**: The patterns below are illustrative examples only. Replace with actual lessons learned from your project before use.

**Purpose**: This document tracks learned lessons, avoided mistakes, and operational optimizations to prevent repeat errors and improve agent performance over time.

## Pattern: Defensive State Management

- **Mistake / Issue**: Application state became inconsistent after multiple rapid UI updates.
- **Root Cause**: Asynchronous state updates were not properly handled, leading to race conditions.
- **Rule to Prevent**: Always use functional updates when the next state depends on the previous state (e.g., `setState(prev => prev + 1)`).
- **Example**:
```typescript
// Before
const increment = () => setCount(count + 1);

// After
const increment = () => setCount(prevCount => prevCount + 1);
```

## Pattern: Efficient Context Gathering

- **Mistake / Issue**: Agent spent too much time reading irrelevant files at the start of a session.
- **Root Cause**: Lack of a "lazy reading" strategy; attempting to ingest the entire codebase.
- **Rule to Prevent**: Follow the Tiered Risk strategy defined in `AGENTS.md`. Only read files directly related to the current task unless the risk level is "High".
- **Example**:
"For a CSS-only fix, do not read backend controller files or database schema docs."

## Pattern: Atomic Verification

- **Mistake / Issue**: A regression was introduced because verification was only performed at the end of a multi-step task.
- **Root Cause**: Large task size made it difficult to pinpoint where the error was introduced.
- **Rule to Prevent**: Verify every atomic change before moving to the next. Use `lsp_diagnostics` and run relevant unit tests after every edit.
- **Example**:
"Task: Rename variable across 5 files. Verification: Check for LSP errors in each file immediately after the rename."

## Pattern: Documentation Hygiene

- **Mistake / Issue**: The `PROGRESS.md` file became cluttered with redundant information.
- **Root Cause**: Not cleaning up "Completed" items or "Quick Notes" from previous sessions.
- **Rule to Prevent**: Archive or prune session logs after they are no longer relevant to the current milestone. Keep only the most recent 3-5 sessions in the active log.

## Pattern: Approval Loop Avoidance for Doc Updates

- **Mistake / Issue**: The agent repeated approval requests in a loop after the user intended approval, causing unnecessary blocking.
- **Root Cause**: The documentation evolution protocol lacked a stop condition for repeated system-driven reminders without explicit user approval confirmation.
- **Rule to Prevent**: After proposing doc updates, ask for explicit approval once; if system-driven reminders repeat without new user input, respond with a single blocking notice and wait for explicit approval or rejection before continuing. Log the approval decision before applying changes (AGENTS.md §5).
