# Initiative Roadmap

This file is the non-runnable roadmap for the broader initiative. It does not select the runnable sprint; `docs/live/features.json` still does that.

- Source goal: Prove the starter harness end to end with durable live state, one runnable sprint at a time, and a visible UI slice that survives review and resume.
- Current slice: `FEAT-001` - dark mode context provider and polished toggle retry after review feedback.
- Ordered remaining slices/phases:
  1. Drain explicit compounding for `FEAT-001`, then repair the failed review findings and rerun execution plus review for the same slice.
  2. Close or honestly park `FEAT-001` before any new runnable sprint is selected.
  3. After the queue is clear and the current slice is resolved, choose the next dependency-ready backlog item from `docs/live/features.json` if one exists.
- Stop or re-authorization condition: Stop when `FEAT-001` exhausts retries, requires a new scope decision, or when no later bounded slice is ready. A human must re-authorize before inventing another initiative slice.
- Visible remaining-work summary: One active slice still needs review-driven repair, `compound_pending_feature_ids` still contains `FEAT-001`, and no later runnable slice has been selected yet.
