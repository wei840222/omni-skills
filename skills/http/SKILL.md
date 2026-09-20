---
name: http
description: >
  Apply proper HTTP methods, status codes, headers, and caching strategies.
  Load when debugging API responses, configuring CORS/security headers, or
  handling HTTP redirects and conditional requests.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌐","os":["linux","darwin","win32"],"displayName":"HTTP"}'
  related-skills: '{"api":"Use for third-party REST/GraphQL client integration beyond protocol mechanics.","cors":"Use for detailed Cross-Origin Resource Sharing policy design.","postman":"Use for Postman collections and Newman runs when HTTP debugging needs a collection harness.","web":"Use for full website build/deploy work beyond HTTP protocol guidance."}'
---

Research notes for redirects, caching, conditional requests, and security headers live in `references/sources.md`.

## Redirects (Often Confused)

- 307 vs 308: both preserve method; 307 temporary, 308 permanent—use these for POST/PUT redirects
- 301/302 may change POST to GET (browser behavior)—use 307 or 308 for API redirects with body
- Include `Location` header with absolute URL—relative may fail in older clients
- Redirect loops: limit to 5-10 follows; infinite loops crash clients

## Caching Combinations

- `Cache-Control: no-store` for sensitive data—kept strictly in memory
- `no-cache` still caches but revalidates every time—requires revalidation on every request
- `private, max-age=0, must-revalidate` for user-specific, always-fresh content
- `public, max-age=31536000, immutable` for versioned static assets
- `Vary: Accept-Encoding, Authorization` when response depends on these headers—forgetting Vary breaks caching

## Conditional Requests

- `ETag` + `If-None-Match`: prefer for APIs—content hash based
- Strong vs weak ETags: `"abc"` vs `W/"abc"`—weak allows semantically equivalent responses
- `If-Match` for optimistic locking: fail update if resource changed since read
- 412 Precondition Failed when `If-Match` fails—prefer this over 409 Conflict for failed preconditions

## CORS Preflight Triggers

- Custom headers (anything not Accept, Accept-Language, Content-Language, Content-Type simple values)
- Content-Type other than: application/x-www-form-urlencoded, multipart/form-data, text/plain
- PUT, DELETE, PATCH methods—even to same origin if other conditions met
- ReadableStream body—triggers preflight
- Preflight cached per `Access-Control-Max-Age`—set to 86400 to reduce OPTIONS spam

## Security Headers (Always Set)

- `Strict-Transport-Security: max-age=31536000; includeSubDomains`—HSTS, once set can't easily undo
- `X-Content-Type-Options: nosniff`—prevents MIME sniffing attacks
- `X-Frame-Options: DENY` or `SAMEORIGIN`—prevents clickjacking
- `Content-Security-Policy`—complex but essential; start with report-only mode

## Range Requests

- `Accept-Ranges: bytes` signals support—clients can request partial content
- `Range: bytes=0-1023` requests first 1024 bytes; `bytes=-500` requests last 500
- Return 206 Partial Content with `Content-Range: bytes 0-1023/5000`
- 416 Range Not Satisfiable if range invalid—include `Content-Range: bytes */5000`

## Error Response Best Practices

- Structured JSON errors: `{"error": {"code": "VALIDATION_FAILED", "message": "...", "details": [...]}}`
- Include request ID in error response—enables log correlation
- Keep stack traces strictly out of production responses—log server-side, return generic message
- 409 Conflict for business rule violations (duplicate email, insufficient funds)—instead of generic 400

## Retry Patterns

- Retry only idempotent methods by default—GET, PUT, DELETE, HEAD
- POST retry needs idempotency key—`Idempotency-Key: <client-generated-uuid>`
- Exponential backoff: 1s, 2s, 4s, 8s... with jitter—prevents thundering herd
- Respect `Retry-After` header—can be seconds or HTTP date
- Set reasonable timeout (30s typical)—ensure timeouts have an upper bound

## Headers Often Forgotten

- `Vary`: must include headers that affect response—CORS without `Vary: Origin` breaks
- `Content-Disposition: attachment; filename="report.pdf"` for downloads
- `X-Request-ID`: generate if not present, propagate to downstream services
- `Accept-Language` for localized responses—respect with graceful fallback

## Connection Behavior

- HTTP/1.1 without `Content-Length` or chunked = connection close after response
- `Transfer-Encoding: chunked` for streaming—can't set Content-Length
- HTTP/2 is binary, multiplexed—no head-of-line blocking at HTTP level
- HTTP/3 uses QUIC (UDP), eliminating TCP head-of-line blocking and reducing connection setup latency
- WebSocket upgrade: GET with `Connection: Upgrade`, `Upgrade: websocket`
