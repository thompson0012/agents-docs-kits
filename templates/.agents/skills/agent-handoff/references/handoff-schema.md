# Handoff Payload Schema

The handoff payload is a JSON object with the following required fields. Every field must be present; use `"N/A"` for empty string fields and `[]` for empty array fields.

## Schema

```json
{
  "goal": "<string: 1-3 sentences describing the ultimate objective>",
  "current_state": {
    "summary": "<string: 1 sentence completion status>",
    "artifacts": ["<string: completed deliverable>"]
  },
  "decisions_made": [
    {
      "decision": "<string: what was decided>",
      "reason": "<string: why it was decided>"
    }
  ],
  "constraints": ["<string: hard rule, phrased as 'Do not X'>"],
  "non_goals": ["<string: explicitly out of scope>"],
  "open_questions": ["<string: unresolved question>"],
  "next_step": "<string: single concrete action>",
  "context_anchors": [
    {
      "file": "<string: relative path>",
      "lines": "<string: line range, e.g. '42-128'>",
      "relevance": "<string: why the successor should read this>"
    }
  ]
}
```

## Field Descriptions

### goal
The ultimate objective of the overall task. 1-3 sentences. Focuses the successor on the big picture without requiring them to infer it from partial work.

### current_state

- **summary**: One sentence capturing whether the work is blocked, in progress, or partially complete.
- **artifacts**: A list of concrete, named deliverables. Each entry names a specific file, configuration, or output. Bad: "Worked on auth." Good: "Created `src/auth.py` with login and registration endpoints."

### decisions_made
Records choices the successor must not re-litigate. Each entry must include both the decision and its reason. This prevents wasted work from revisiting settled questions.

### constraints
Hard rules the successor must not violate. Phrase every entry as a prohibition: "Do not modify `migrations/`", not "Be careful with migrations."

### non_goals
Work explicitly declared out of scope. Prevents scope creep where the successor starts building adjacent features.

### open_questions
Questions the user has not answered, or problems the previous agent could not resolve. Tells the successor what is still unknown.

### next_step
A single, concrete, immediately executable instruction. NOT a plan or a list. The successor should be able to act on it without interpretation.

### context_anchors
Surgical pointers to files the successor needs. Each anchor specifies a file path, a line range, and the reason to read it. Anchors should reference the smallest unit of code needed — never entire directories.

## Example

```json
{
  "goal": "Build a REST API for user authentication with JWT-based login, registration, and password reset.",
  "current_state": {
    "summary": "Login and registration endpoints are implemented and tested. Password reset is not yet started.",
    "artifacts": [
      "Created src/auth.py with /login and /register POST endpoints",
      "Created tests/auth/test_login.py with 12 passing tests",
      "Configured JWT secret rotation in config/secrets.py"
    ]
  },
  "decisions_made": [
    {
      "decision": "Use PyJWT v2.8+ instead of python-jose",
      "reason": "python-jose is unmaintained since 2022; PyJWT has active releases and better RS256 support"
    },
    {
      "decision": "Store refresh tokens in Redis rather than the user table",
      "reason": "Refresh tokens are ephemeral and should be independently scalable; Redis TTL simplifies cleanup"
    }
  ],
  "constraints": [
    "Do not modify existing /login or /register endpoints — they are tested and approved",
    "Do not change the JWT payload structure — it is consumed by an external gateway"
  ],
  "non_goals": [
    "OAuth / social login integration",
    "Rate limiting — this is handled by the API gateway"
  ],
  "open_questions": [
    "Should password reset tokens expire after 15 minutes or 30 minutes? User has not yet confirmed."
  ],
  "next_step": "Read tests/auth/test_login.py lines 1-80 to understand test patterns and fixture setup, then create tests/auth/test_password_reset.py with expected test cases before implementing the endpoint.",
  "context_anchors": [
    {
      "file": "src/auth.py",
      "lines": "1-156",
      "relevance": "Existing login/register implementation — match this code style and error handling pattern"
    },
    {
      "file": "tests/auth/test_login.py",
      "lines": "1-80",
      "relevance": "Test patterns and fixtures to replicate for password reset tests"
    }
  ]
}
```

## Anti-Example

This is a BAD handoff payload. Every section is vague, actionable, or unspecific:

```json
{
  "goal": "I was trying to build an auth system and it was going pretty well.",
  "current_state": {
    "summary": "I worked on auth for a while and made good progress.",
    "artifacts": ["Did some coding on the auth module", "Fixed a few bugs"]
  },
  "decisions_made": [
    { "decision": "Used JWT", "reason": "Seemed like the right choice" }
  ],
  "constraints": ["Be careful with security"],
  "non_goals": [],
  "open_questions": [],
  "next_step": "Continue working on the auth API and finish the remaining endpoints.",
  "context_anchors": [
    { "file": "src/", "lines": "all", "relevance": "All the code is here" }
  ]
}
```
