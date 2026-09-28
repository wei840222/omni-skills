## Core Rules

### 1. Start From the Contract, Not the Controller
Define resources, payload schemas, status codes, and error shapes in OpenAPI before writing handlers.

If the contract is unclear, implementation speed creates rework and breaks clients.

### 2. Keep Endpoint Semantics Predictable
Use stable naming, plural resources, and correct HTTP methods. Make idempotent behavior explicit for `PUT`, `DELETE`, and retryable `POST` operations.

Predictable semantics reduce client bugs and support safer retries.

### 3. Enforce Security by Default
Require authentication on non-public endpoints, apply authorization checks at resource boundary, validate input strictly, and sanitize output.

Enforce security controls exclusively on the backend.

### 4. Design for Failure Paths First
Specify error classes, timeout strategy, rate-limit behavior, and fallback expectations before scaling happy-path code.

APIs fail in production at edges, not in demos.

### 5. Make Data Changes Backward Compatible
Use additive schema migrations first, backfill data safely, and only remove old fields after client migration windows close.

Breaking database or response changes without rollout planning cause outages.

### 6. Test Contract, Behavior, and Operations
Cover OpenAPI contract validation, integration tests against real infrastructure, and end-to-end tests for critical user journeys.

Complement unit tests with integration and end-to-end tests to prove API reliability.

### 7. Ship With Observability and Runbooks
Expose request metrics, structured errors, trace identifiers, and health indicators. Document recovery steps for known failure modes.

If an API cannot be observed, it cannot be operated safely.

## Common Traps

- Building endpoints before defining response and error contracts -> incompatible clients and patchwork fixes.
- Mixing auth, business logic, and transport concerns in handlers -> brittle code and hidden security gaps.
- Treating pagination and filtering as optional -> unstable list endpoints and expensive queries.
- Returning inconsistent error bodies across services -> poor client DX and weak automation.
- Shipping without migration rollback steps -> long incidents when a release fails.

