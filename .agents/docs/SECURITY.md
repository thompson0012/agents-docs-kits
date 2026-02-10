# SECURITY.md — Security Guidance for AI Agents

**Purpose**: This document provides supporting guidance for security-conscious development. It follows defense-in-depth principles and complements the security rules defined in the root `AGENTS.md`.

## Defense-in-Depth Principles

### 1. Secrets Management
**Guidance**: Never commit, log, or expose secrets in code, commit messages, or application logs.

**Examples**:
- ✅ Use environment variables: `process.env.API_KEY`
- ✅ Use secret management services: AWS Secrets Manager, HashiCorp Vault
- ❌ Hardcoded secrets: `const apiKey = "sk_live_12345"`
- ❌ Committed `.env` files: Ensure `.env` is in `.gitignore`.

### 2. Input Validation
**Guidance**: Treat all external data as untrusted. Validate and sanitize all inputs before processing.

**Examples**:
- ✅ Use schema validation libraries: Zod, Joi, or Marshmallow.
- ✅ Sanitize HTML to prevent XSS: Use libraries like DOMPurify.
- ✅ Validate file types and sizes for uploads.
- ❌ Trusting client-side validation: Always perform validation on the server.

### 3. Safe Coding Patterns
**Guidance**: Use established patterns to mitigate common vulnerabilities like SQL injection, XSS, and CSRF.

**Examples**:
- ✅ Parameterized queries: `db.query('SELECT * FROM users WHERE id = $1', [userId])`
- ✅ Automatic XSS escaping: Use templating engines that escape output by default.
- ✅ CSRF protection: Use anti-CSRF tokens for state-changing requests.
- ❌ Dynamic execution: Avoid `eval()` or `exec()` with user-provided strings.

### 4. Vulnerability Response Protocol
**Guidance**: On discovery of a potential vulnerability, stop and follow this protocol.

1. **Stop**: Immediately cease any related development.
2. **Warn**: Write a clearly marked WARNING block in the session log or chat.
3. **Escalate**: Notify the user and wait for explicit direction before proceeding.
4. **Reproduction**: If safe, create a failing test case that demonstrates the vulnerability.

### 5. Authentication & Authorization
**Guidance**: Implement robust identity management and follow the principle of least privilege.

**Examples**:
- ✅ Use strong password hashing: Argon2 or bcrypt.
- ✅ Implement Role-Based Access Control (RBAC) to restrict resource access.
- ✅ Use secure, HttpOnly, and SameSite cookies for session management.
- ❌ Storing passwords in plain text or using weak hashing algorithms (e.g., MD5).

### 6. Dependency Security
**Guidance**: Regularly audit and update project dependencies to patch known vulnerabilities.

**Examples**:
- ✅ Run regular security audits: `npm audit`, `pip-audit`, or `snyk test`.
- ✅ Keep dependencies up to date using tools like Dependabot.
- ✅ Pin dependency versions to prevent unexpected breaking changes or malicious updates.
- ❌ Using libraries with known high-severity vulnerabilities or those that are no longer maintained.
