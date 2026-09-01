# Status Triage

Beyond Core Rule 4's 401/403/404 chain:

| Code | Meaning | First move |
|------|---------|-----------|
| 400 | Request malformed or rejected | Read the body's error field, then `references/debug.md` Mysterious 400s |
| 405 | Method not allowed | Wrong verb — or a redirect: clients follow 301/302 on POST by re-issuing GET (trailing-slash URLs are the classic trigger) |
| 409 | State conflict | Re-fetch current state; concurrent edit or duplicate create |
| 410 | Gone permanently | Retired resource or API version (`references/versioning.md`); expired sync token (`references/sync.md` Sync Tokens) |
| 412 | Precondition failed | Your `If-Match` ETag is stale — re-read, re-apply, retry |
| 415 | Unsupported media type | `Content-Type` missing or wrong (top trap below) |
| 422 | Validation failed | Well-formed but semantically rejected — field-level errors are in the body |
| 429 | Rate limited | `references/rate-limits.md`; obey `Retry-After` |
| 500 | Server bug | Retry only idempotent requests (`references/resilience.md` Retry Logic) |
| 502/503/504 | Edge/LB failure or overload, often with an HTML body | Backoff and retry; check the status page (`references/resilience.md` Provider Outages) |
