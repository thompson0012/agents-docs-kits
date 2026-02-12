# TASKS.md — Project & Session Task List

> **STATUS**: TEMPLATE
> **OWNER**: Human (final authority) / AI (maintenance)
> **LAST REVIEWED**: 2026-02-12

**Purpose**: This document provides a concrete, actionable checklist of tasks grouped by priority or session. It should be used to track atomic progress and ensure no requirements are missed.

## Template (fill this, then delete the example below)

## High Priority
- [ ] <task>

## This Session: <YYYY-MM-DD>

**Focus**: <focus>

- [ ] <task>

## Later (Backlog)
- [ ] <task>

## Example (fictional, delete before use)

## High Priority

- [ ] Implement robust error handling for the user registration API.
- [ ] Fix critical bug in the search indexing service.
- [ ] Prepare the staging environment for the upcoming stakeholder demo.

## This Session: February 7, 2026

**Focus**: Authentication Module

- [x] Create the initial `auth` controller and service.
- [x] Implement password hashing using Argon2.
- [ ] Write integration tests for the login endpoint.
- [ ] Update `APP_FLOW.md` with the new authentication journeys.

## Later (Backlog)

- [ ] Add support for multi-factor authentication (MFA).
- [ ] Implement an automated backup strategy for the production database.
- [ ] Research and propose a strategy for migrating to a serverless architecture.

## Conventions

- **Atomic Tasks**: Break large features into small, manageable tasks (e.g., "Implement hashing" instead of "Build auth").
- **Status Updates**: Use `- [ ]` for pending tasks and `- [x]` for completed ones.
- **Traceability**: Link tasks to relevant entries in `IMPLEMENTATION_PLAN.md` or `PRD.md` where possible.
- **Plan Link (optional)**: If this session follows an approved plan artifact, add a link to `/.agents/docs/plans/.../tasks.md` and prefer updating that checklist as the source of truth.
- **Session Focus**: Clearly define the goals for the current session at the start.
