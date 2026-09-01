# Output Gates

Before emitting integration code or a diagnosis, check:

- Every POST/PUT/PATCH example includes `Content-Type: application/json` (or the API's required type)
- No secret appears in a URL, code literal, or logged output — env var references only
- Every pagination loop terminates on the API's `has_more`/cursor signal, not on `len(items)`
- Retry logic distinguishes 4xx (skip retrying, fix the request) from 429/5xx (backoff and retry)
- Webhook handler verifies signature on the raw body before parsing (→ `references/webhooks.md`)
- Money handled in the currency's own convention (minor units, exponent), IDs as strings (→ `references/data-formats.md`)
- Examples reference the `default_environment` credential (sandbox unless the user asked for live)
