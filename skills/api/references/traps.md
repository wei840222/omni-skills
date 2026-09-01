# Traps

| Trap | Why it fails | Do instead |
|------|--------------|------------|
| Missing `Content-Type` on POST | Many APIs parse the body as form-encoded or reject with an unhelpful 400/415 | Always send `Content-Type: application/json` with JSON bodies |
| Trusting the default page size | Defaults are small; you silently process a fraction of the data | Loop until the API's completion signal (→ `references/pagination.md`) |
| Retrying 400 Bad Request | The request itself is invalid; identical retries burn quota and can trigger abuse detection | Fix the payload; retry only 429/5xx |
| Copy-pasted token fails with 401 | Trailing newline or wrapping quotes from the clipboard corrupt the header | `echo -n`, or trim before use |
| Testing against production keys | Live-mode side effects (real charges, real emails) during development | Sandbox key first; gate and prefixes in `references/testing.md` and `references/credentials.md` |
| One giant try/catch around the whole call | 401, 429, and 500 need different responses; a generic catch retries the unretryable | Branch on status class before any retry |
| Parsing each network chunk as one SSE event | TCP splits and merges events arbitrarily; JSON parse fails mid-token | Buffer to the blank-line delimiter (→ `references/streaming.md`) |
| Numeric IDs parsed as numbers | 64-bit IDs overflow JS's 2^53−1 and round silently | Treat every ID as an opaque string (→ `references/data-formats.md`) |
| Buffering a whole download in memory | Multi-GB export = OOM that dev-sized data never showed | Stream to disk; verify against `Content-Length` (→ `references/files.md`) |
| Calling a third-party API straight from the browser | Most APIs send no CORS headers, and any key in the bundle is public | Proxy through your backend; only provider-designated browser-safe keys ship client-side (→ `references/browser.md`) |
