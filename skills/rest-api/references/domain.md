# REST API Domain Rules

Framework-independent rules for designing and shipping REST APIs. Prefer this
file over inventing one-off conventions. Cite live standards from
`references/sources.md` when quoting normative behavior.

## Core rules

1. **Start from the contract.** Define resources, payload schemas, status codes,
   and error shapes in OpenAPI before writing handlers. Unclear contracts create
   client rework.
2. **Keep endpoint semantics predictable.** Use plural nouns for collections,
   correct HTTP methods, and explicit idempotency for `PUT`, `DELETE`, and
   retryable `POST` (idempotency keys for payments/provisioning).
3. **Enforce security by default.** Authenticate non-public operations, authorize
   at the resource/object boundary (prevent BOLA/IDOR), validate and coerce all
   inputs, and sanitize user-generated output. Enforce controls on the server
   only — never trust client-supplied roles.
4. **Design failure paths first.** Specify error classes, timeout budgets,
   rate-limit behavior, and fallbacks before scaling the happy path.
5. **Evolve data and responses additively.** Expand schema → deploy dual-read →
   backfill → flip writes → contract only after usage reaches zero. Breaking
   response or DB changes without a migration window cause outages.
6. **Test contract, behavior, and operations.** Validate OpenAPI against the
   server, run integration tests against real dependencies, and cover critical
   journeys end-to-end including error and timeout paths.
7. **Ship with observability and runbooks.** Expose request metrics, structured
   errors with stable `code`, trace/`request_id`, and health indicators.
   Document recovery for known failure modes.

## Contract workflow

1. List core resources, owners, canonical IDs, and immutable fields.
2. Separate client-facing models from persistence models.
3. For each operation: method, path, request/response schemas, error map,
   authorization requirement, and examples.
4. Adopt one error envelope everywhere, for example:

```json
{
  "error": {
    "code": "RESOURCE_NOT_FOUND",
    "message": "User not found",
    "request_id": "req_123",
    "details": []
  }
}
```

Keep `code` stable for machines; keep `message` clear for humans. Prefer Problem
Details ([RFC 9457](https://www.rfc-editor.org/rfc/rfc9457.html)) when the
ecosystem already uses it.

5. Publish only when OpenAPI validates, examples match implementation, error
   codes are tested, and security requirements are attached per operation.

## Endpoint rules

### URL and methods

- Nouns for resources: `/users`, `/orders/{order_id}`; prefer plural collections.
- Use `GET`, `POST`, `PATCH`, `PUT`, `DELETE` with strict semantics.
- Whitelist query parameters; document operators; reject unknown keys.

### Response shape

Keep simple resources flat or use a consistent `data` wrapper. List endpoints
include pagination metadata (prefer cursor pagination for stable ordering):

```json
{
  "data": [],
  "pagination": {
    "next_cursor": "abc",
    "has_more": true
  }
}
```

### Status code policy

| Code | Use |
| --- | --- |
| 200 | Successful reads and updates |
| 201 | Creates returning the created resource |
| 204 | Successful deletes without body |
| 400 | Invalid input |
| 401 | Missing or invalid authentication |
| 403 | Authenticated but forbidden |
| 404 | Missing resource |
| 409 | Version or state conflict |
| 412 | Failed precondition (`If-Match`) |
| 422 | Semantically invalid payload |
| 429 | Rate limit |
| 5xx | Server-side failure |

Use `307`/`308` when redirecting methods that carry a body; avoid accidental
POST→GET demotion from `301`/`302` browser behavior (see `http` skill / RFC 9110).

## Security baseline

- Authenticate first (API key, session, JWT, OAuth access token); authorize
  second at the object boundary.
- Validate path, query, and body against schemas; coerce types server-side.
- Secrets live in a secret manager; rotate on schedule and after incidents.
- Mask tokens, credentials, and full PII from logs.
- Per-user and per-IP rate limits; request size limits; timeout budgets.
- Explicit CORS origins; HTTPS in production; secure cookie flags when cookies
  are used.
- Before release: threat-model auth bypass and broken object-level
  authorization; cover sensitive endpoints with tests; audit logs include actor,
  action, resource, and `request_id`.

## Persistence and migrations

- Model for query patterns; index high-cardinality lookup paths; optimistic
  locking or version fields for concurrent writes.
- Keep transactions short; do not hold DB transactions open across network calls.
- Use outbox patterns when publishing domain events reliably.
- Expand → dual-read → backfill → flip writes → remove old columns only at zero
  usage. Keep tested rollback scripts and abort thresholds.

## Testing and observability

### Minimum release gate

Deploy only when all are true:

- Critical endpoint integration tests pass.
- Backward-compatibility checks pass for current clients.
- Error-handling and edge paths are tested, not only success paths.
- Performance budget is within the accepted threshold.

### Observability baseline

- Request count and latency by endpoint and status.
- Error rate by endpoint and stable error `code`.
- Dependency latency and failure rate.
- Saturation (queue depth, worker utilization).
- Structured logs with `request_id` (and `actor_id` when available).
- Alerts on user-impacting symptoms with runbook links.

## Release checklist

- OpenAPI updated and validated; breaking changes documented with migration path
  and sunset date.
- Authz verified on critical endpoints; secrets not hardcoded; rate/payload
  limits configured.
- Migration plan reviewed (expand/migrate/contract); rollback tested; integrity
  checks prepared.
- Integration and e2e tests passing; performance smoke done; error responses and
  logs verified.
- Dashboards for latency, error rate, saturation; alerts with owner; incident
  runbook current.
- Staged/canary plan; post-deploy verification commands; explicit go/no-go.

## Common traps

| Trap | Consequence | Fix |
| --- | --- | --- |
| Handlers before OpenAPI | Incompatible clients, patchwork fixes | Contract first |
| Auth + business + transport mixed in one handler | Hidden security gaps | Separate layers; authz at resource |
| Pagination treated as optional | Unstable lists, expensive queries | Cursor pagination + whitelist filters |
| Inconsistent error bodies | Poor client DX, weak automation | One envelope / Problem Details |
| Destructive migration in the same release as expand | Long incidents | Contract only after zero usage |
| Client-supplied roles trusted | Auth bypass / BOLA | Server-side object checks |
| Shipping without rollback | Stuck failed release | Tested rollback + abort thresholds |
| Logging secrets or full PII | Credential leak | Mask; pointer-only in state |

## Prefer sibling skills when

| Job | Skill |
| --- | --- |
| FastAPI routers / Depends / Pydantic | `fastapi` |
| Flask blueprints / app factory | `flask` |
| Django ORM / admin / DRF | `django` |
| Pure HTTP status/headers/caching | `http` |
| OAuth / OIDC / MFA protocols | `auth` |
| Calling Stripe/OpenAI/etc. | `api` |
| Pools, retries, service internals | `backend` |
