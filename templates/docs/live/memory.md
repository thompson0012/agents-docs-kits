# Live Memory

Store only durable learnings here. Append dated notes when a fact will help a future agent avoid rediscovery. Do not copy transient sprint logs into this file.

## Verified learnings

- [2026-04-02] Browser-driven acceptance tests are more reliable when interactive elements expose stable hooks such as `@theme-toggle` instead of relying on visible copy alone.
- [2026-04-02] Visual review is not trustworthy until the utility CSS or token pipeline is confirmed to be loaded; broken styling can create false design failures.

## Environment quirks

- [2026-04-02] `docs/scripts/*` may help with orchestration, but repository truth still lives in `docs/live/*` and `.harness/<feature-id>/`.
- [2026-04-02] Resume interrupted work from `.harness/<feature-id>/status.json` and its `resume_from` pointer rather than reconstructing state from memory.

## Team conventions

- [2026-04-02] Only one active sprint is allowed at a time. Everything else stays pending in `docs/live/features.json`.
- [2026-04-02] Failed review does not close a sprint; keep the sprint live, preserve artifacts, and propagate corrective next actions back into the backlog.
- [2026-04-02] Put cross-sprint facts here only after they are observed more than once or clearly affect future work.

## Do not store here

- one-off shell output,
- temporary blockers already captured in a sprint handoff,
- duplicate copies of contracts or reviews,
- speculative ideas that have not been verified.
