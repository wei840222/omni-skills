# Testing components

## Stack

Vitest (or Jest) + Testing Library + MSW for HTTP. Prefer role/label queries.

## What to assert

- What the user sees and can do (roles, labels, visible text, focus).
- Loading and error paths, not only the happy path.
- Avoid asserting internal state, mock call counts, or CSS class names.

## Async

- `findBy*` / `waitFor` for appearances; assert loading UI then settled UI.
- MSW handlers per test; reset between tests.

## Effects and Query

- Prefer testing through Query providers with a test client over mocking
  implementation details of fetch inside components.
