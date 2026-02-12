# TEST_STRATEGY.md — Testing Standards & Strategy

> **STATUS**: TEMPLATE
> **OWNER**: Human (final authority) / AI (maintenance)
> **LAST REVIEWED**: 2026-02-12

*Note: This is a supporting guide. Core testing rules reside in `AGENTS.md` §4 (Error Protocol) and §7 (Engineering & Coding Standards — Test Default).* 

## Test-First for Bugs (Per AGENTS.md §4)

Per AGENTS.md §4 "Error Protocol":
- **Every bug must have a failing test** before the fix
- **Minimal Reproduction**: Simplest test that proves the bug exists
- **No Paper-Overs**: Tests must verify actual behavior, not mask failures

## Test Pyramid (Target Distribution)

| Type | Coverage Target | Purpose |
|------|-----------------|---------|
| **Unit** | 70% | Logic, utilities, pure functions |
| **Integration** | 20% | API endpoints, database interactions |
| **E2E** | 10% | Critical user flows (auth, checkout, etc.) |

## Coverage Minimums

- **New Code**: 80% minimum (exceptions require explicit approval)
- **Bug Fixes**: 100% (reproduction test is mandatory)
- **Refactors**: Maintain or improve existing coverage

## Test Organization

### Frontend (from FRONTEND_GUIDELINES.md)
- Component tests: Co-located with components (`Button.test.tsx`)
- Integration tests: `/tests/integration/`
- E2E tests: `/tests/e2e/`
- Use the test runner defined in TECH_STACK.md (example: Vitest)

### Backend (from BACKEND_STRUCTURE.md)
- Unit tests: Co-located with modules (`auth.test.ts`)
- API tests: `/tests/api/`
- Database tests: Use test DB with migrations

## When to Skip Tests

Per AGENTS.md §7 "Test Default":
- ✅ User explicitly opts out
- ✅ Prototype/throwaway code (mark with `@temporary`)
- ❌ "I'll add tests later" (not acceptable)
- ❌ "It's too simple to test" (write the test anyway)

## CI/CD Integration

- All tests must pass before merge (per `AGENTS.md` §9 Completion Checklist)
- Coverage reports generated on every PR
- Flaky tests are treated as failures: fix the root cause, or quarantine with explicit approval (and a tracked follow-up). Do not delete tests just to make CI pass.

## Examples

### Good Test (Minimal Reproduction)
```typescript
test('bug: user profile API returns 500 on empty bio', async () => {
  const user = await createUser({ bio: '' });
  const response = await api.getProfile(user.id);
  expect(response.status).toBe(200); // Should be 200, not 500
});
```

### Bad Test (Not Actually Testing Anything)
```typescript
test('profile works', async () => {
  const result = await getProfile();
  expect(result).toBeTruthy(); // ❌ What does this prove?
});
```

---

**Last Updated**: 2026-02-09  
**Maintained By**: AI agents per GUIDELINES.md
