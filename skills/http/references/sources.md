# HTTP Skill Research Sources

## Redirects and method preservation

- **MDN — 301 Moved Permanently** — documents that browsers may rewrite POST to GET on 301/302; prefer 307/308 when method and body must be preserved — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/301
- **MDN — 307 Temporary Redirect** — method and body preserved — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/307
- **MDN — 308 Permanent Redirect** — permanent redirect that preserves method and body — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/308
- **RFC 9110 §15.4** — redirect status code semantics — https://www.rfc-editor.org/rfc/rfc9110.html#name-redirection-3xx

## Caching and Cache-Control

- **MDN — Cache-Control** — `no-store` vs `no-cache`, `private`/`public`, `immutable`, and revalidation semantics — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control
- **RFC 9111 — HTTP Caching** — normative caching model — https://www.rfc-editor.org/rfc/rfc9111.html
- **MDN — Vary** — response variance and cache key correctness — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary

## Conditional requests

- **MDN — ETag** — strong vs weak validators — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/ETag
- **MDN — If-None-Match / If-Match** — conditional GET and optimistic concurrency — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-None-Match
- **MDN — 412 Precondition Failed** — failed conditional update semantics — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/412

## CORS preflight

- **MDN — CORS** — simple requests vs preflight, simple headers/content-types, and `Access-Control-Max-Age` — https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
- **Fetch Standard — CORS protocol** — preflight algorithm and simple request definition — https://fetch.spec.whatwg.org/#cors-protocol

## Security headers

- **MDN — Strict-Transport-Security** — HSTS directives and durability — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security
- **MDN — X-Content-Type-Options** — `nosniff` — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/X-Content-Type-Options
- **MDN — Content-Security-Policy** — CSP and report-only rollout — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy

## Range requests and connection behavior

- **MDN — Range / Content-Range / 206** — partial content mechanics — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Range
- **MDN — HTTP/2** — multiplexing and no HTTP-level HOL blocking — https://developer.mozilla.org/en-US/docs/Glossary/HTTP_2
- **MDN — HTTP/3** — QUIC transport and connection setup benefits — https://developer.mozilla.org/en-US/docs/Glossary/HTTP_3

## Errors, retries, and idempotency

- **MDN — 409 Conflict** — resource-state conflicts distinct from validation errors — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/409
- **IETF draft-ietf-httpapi-idempotency-key-header** — `Idempotency-Key` usage for safe POST retries — https://datatracker.ietf.org/doc/html/draft-ietf-httpapi-idempotency-key-header
- **MDN — Retry-After** — seconds or HTTP-date retry guidance — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Retry-After
