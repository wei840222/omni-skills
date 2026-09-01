# Core Rules

1. **Raw request before client code.** Reproduce with curl first; if curl succeeds and the SDK fails, the bug is in SDK config (base URL, version pin, auth header name), not the API. Chains: `references/debug.md`.

2. **Backoff with full jitter, and `Retry-After` overrides it.** `sleep = random(0, min(cap, base × 2^attempt))`, base 1s, cap 30-60s, max `retry_max` attempts (default 4; AWS "full jitter"). Attempt 3 → sleep is a random value in [0, 8s], not exactly 8s — the randomness is what prevents synchronized retry storms. If the 429/503 carries `Retry-After`, obey it instead.

3. **Retry only idempotent operations by default.** Reuse the provider's idempotency key for a POST retry; after a create timeout without that guarantee, reconcile recent or retrievable resources before submitting another create. Details and key lifetime: `references/resilience.md`.

4. **Status triage in this order: 401 → credential, 403 → permission, 404 → maybe permission too.** 401 = the API doesn't know who you are (missing/expired/malformed token). 403 = it knows you and says no (scope, plan tier, IP allowlist). Some APIs (GitHub among them) return 404 for resources you lack access to, to avoid confirming existence — a "not found" on a resource you know exists is an auth bug, not a URL bug.

5. **HTTP 200 is not success.** Check the body for `error`/`errors` fields (GraphQL always returns 200 — `references/graphql.md`), batch endpoints for per-item failures (207 Multi-Status or a 200 with a mixed `results` array — `references/async-jobs.md`), and streams for completion (`references/streaming.md`).

6. **Both timeouts, always.** Set connect and read timeouts explicitly; a request without them hangs forever on a dead upstream. Values and rationale: `references/resilience.md`; for streams, read timeout means inter-chunk idle (`references/streaming.md`).

7. **Credentials in headers, keep out of URLs.** Query-param keys land in access logs, proxy caches, and browser history. Env vars only; naming scheme for multi-account setups: `references/credentials.md`.

8. **Paginate to completion or state that results are partial.** Terminate on the API's own signal (`has_more`, next cursor absent), not item count alone.
