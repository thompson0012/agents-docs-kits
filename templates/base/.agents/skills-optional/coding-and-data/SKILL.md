---
name: coding-and-data
description: Use when a request requires repository navigation, code changes, debugging, or structured data analysis and the safest path is to hand execution to a focused subagent.
---

# Coding and Data Routing

Use this skill when the work is hands-on and repository- or dataset-backed. The parent agent should frame the job, then delegate execution to a focused subagent instead of doing broad exploration itself.

## Delegate Immediately

For coding or data tasks:
- Do not read source files just to "get oriented" before delegating.
- Do not browse the tree, skim README files, or inspect code to form a vague architecture summary first.
- Limit parent-side work to non-code discovery: user requirements, ticket text, failing command output, named file paths, repository location, connector names, or dataset paths already available.
- Put that context in the subagent assignment and let the subagent explore the implementation details.

## Pick the Right Subagent

- Use `task` for multi-step implementation, debugging, refactors, or analysis that may touch several files.
- Use `quick_task` for mechanical edits, narrow data collection, or tightly scoped follow-through.
- If the user asks for multiple independent jobs, launch them in one `task` batch so they run in parallel.

## Repository Work

When the task is about code in a repository:
1. Identify the working tree or repository location already available in the current harness.
2. Gather the smallest non-code context needed: ticket text, acceptance criteria, reproduction steps, failing tests, branch or PR identifiers, and any explicit file list.
3. Delegate with a concrete assignment that names target files or symbols when known, plus the required verification.
4. Do not keep a parent-side shadow investigation of the same codebase.

If the repository is not available locally and its location cannot be derived from current context, ask for that missing location rather than guessing.

## Data Work

When the task is about SQL, warehouse questions, CSVs, or other structured data:
- Delegate when the work requires schema discovery, query design, cleaning, analysis, or visualization.
- Pass the actual data location the harness can use: file path, database name, connector name, table names, date range, or metric definitions.
- If the data location is unknown, resolve that first. Do not invent a connector, database, or file source to keep moving.
- Keep the assignment outcome-focused: what question must be answered, what artifact is needed, and what evidence or checks must accompany it.

## Reviews and Comparisons

Use parallel subagents when the user explicitly wants multiple implementations, multiple reviewers, or independent lines of investigation. Each subagent should have:
- a distinct assignment,
- non-overlapping ownership when possible,
- the same acceptance bar,
- and a clear final synthesis step for the parent agent.

## Parent-Agent Responsibilities After Delegation

After the subagent returns:
- read the result carefully,
- summarize what changed or what was learned,
- report the verification the subagent actually performed,
- and call out unresolved risks instead of smoothing them over.

Do not redo the subagent's implementation work unless the first pass clearly missed the assignment.