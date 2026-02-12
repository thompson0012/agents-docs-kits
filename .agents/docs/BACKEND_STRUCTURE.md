# BACKEND_STRUCTURE.md — Backend Architecture & API Patterns

> **TEMPLATE**: The patterns and code examples below are illustrative examples only. Adapt to your actual project's framework and conventions before use.

> **EXAMPLE ASSUMPTIONS**: Examples use a TypeScript/Express-style controller and schema validation as illustration.
> If your backend stack differs, keep the architecture intent (separation of concerns, validation, secure defaults) but rewrite examples to match your framework/runtime.

**Purpose**: This document provides deeper, example-heavy rules for backend development, focusing on maintainable API patterns, data flow, and security.

## Preferred Patterns

**Purpose**: Document the architectural styles and coding patterns used throughout the backend.

- **Controller-Service-Repository**: Decouple the API handling, business logic, and data access layers.
- **DTOs (Data Transfer Objects)**: Use DTOs for request and response validation to ensure a clean interface.
- **Middleware for Cross-Cutting Concerns**: Use middleware for authentication, logging, and error handling.

**Example (fictional, delete before use): Controller Method**
```typescript
async function createUser(req: Request, res: Response) {
  try {
    const userData = createUserDto.parse(req.body);
    const user = await userService.register(userData);
    res.status(201).json(user);
  } catch (error) {
    next(error); // Delegate to error handling middleware
  }
}
```

## Do / Don’t Table

**Purpose**: Quick reference for common backend development practices.

| Do | Don't |
|----|-------|
| Use parameterized queries to prevent SQL injection. | Use string concatenation for building database queries. |
| Return appropriate HTTP status codes (e.g., 404 for Not Found). | Return 200 OK for every request, even when an error occurs. |
| Implement structured logging for easier debugging. | Use `console.log` for logging in production. |

## Folder & Naming Conventions

**Purpose**: Maintain a consistent project structure.

- **Layered Structure**: Group files by layer (e.g., `src/controllers/`, `src/services/`, `src/repositories/`).
- **camelCase**: Use camelCase for function names and variables.
- **Singular/Plural**: Use plural for route paths (e.g., `/users`) and singular for resource models (e.g., `User`).

## Common Gotchas & Anti-patterns

**Purpose**: Highlight pitfalls to avoid.

- **Fat Controllers**: Avoid putting business logic in the controllers. Delegate to services instead.
- **Deep Nesting**: Avoid deeply nested callbacks or promise chains. Use `async/await` for better readability.
- **Unvalidated Input**: Never trust data from the client. Always validate input against a schema.

## Security & Data Flow

- **Secrets Management**: Never commit secrets to version control. Use environment variables or a secret management service.
- **Input Validation**: Use a library like Zod or Joi to validate all incoming request data.
- **Authentication/Authorization**: Ensure that all protected routes are properly authenticated and authorized based on user roles.
