# MEMORY.md — Long-Term Architectural & Decision Log

> **STATUS**: TEMPLATE
> **OWNER**: Human (final authority) / AI (maintenance)
> **LAST REVIEWED**: 2026-02-12

**Purpose**: This document tracks the stable, rarely changing knowledge of the project. It serves as the long-term memory for architectural decisions, adopted patterns, and historical context.

## Architectural Decisions (ADR)

**Purpose**: Record significant architectural choices and the rationale behind them.

| Decision | Date | Status | Rationale | Alternatives |
|----------|------|--------|-----------|--------------|
| Example (fictional): Use Microservices for Auth | 2026-02-01 | Accepted | Decouples authentication from core business logic for easier scaling. | Monolithic auth, Third-party provider (Auth0). |
| Example (fictional): Event-Sourcing for Orders | 2026-02-05 | Proposed | Provides a complete audit trail and allows for complex temporal queries. | Traditional CRUD on relational database. |

## Adopted Patterns

**Purpose**: Document the coding patterns and architectural styles consistently used across the codebase.

- **Example (fictional): Repository Pattern**: Used for data access to decouple the business logic from the underlying storage mechanism.
- **Example (fictional): Functional Components**: All new UI components should be implemented as functional components using React hooks.
- **Example (fictional): Atomic Design**: The UI library is organized following atomic design principles (atoms, molecules, organisms, templates, pages).

## Domain Glossary

**Purpose**: Define key terms used within the project to ensure a shared understanding among stakeholders.

- **Example (fictional): Workspace**: A top-level container for projects and users.
- **Example (fictional): Sprint**: A fixed-length time box (usually 2 weeks) during which specific tasks are completed.
- **Example (fictional): Feature Flag**: A technique to turn a feature on or off without redeploying code.

## Historical Context

**Purpose**: Provide background information on the project's evolution, past failures, or significant milestones.

- **Example (fictional): Initial Prototype**: The first version of the app was built using a NoSQL database, but it was migrated to PostgreSQL after encountering scalability issues with complex joins.
- **Example (fictional): UI Rebrand (Jan 2026)**: A major visual update was performed to align with the new brand guidelines, focusing on a more minimalist and accessible design.
- **Example (fictional): Legacy API Support**: The `/api/v1` endpoints are maintained for backward compatibility with mobile clients but are scheduled for deprecation in Q3 2026.
