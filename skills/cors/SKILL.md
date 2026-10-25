---
name: cors
description: >
  Configure Cross-Origin Resource Sharing (CORS) safely: preflight triggers,
  credentials vs wildcard origins, Allow/Expose/Vary headers, Max-Age caching,
  Private Network Access preflights, and browser debugging. Use when an API
  must allow a browser frontend on another origin, when OPTIONS preflight fails,
  when cookies/auth headers are blocked, when CDN caches break CORS, when
  Access-Control-* headers are missing on errors, or when localhost/private
  targets need Access-Control-Allow-Private-Network. Prefer `http` for broader
  status/caching/security-header guidance; prefer `rest-api` for contract-first
  API design beyond CORS; prefer `oauth` when the real issue is auth/token flow
  rather than origin policy.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔀"}'
---

# CORS

Knowledge-only guidance for configuring and debugging Cross-Origin Resource
Sharing. This skill does not store local configuration or persistent user state.

Load `references/sources.md` before restating header names, Max-Age browser caps,
Private Network Access requirements, or Fetch CORS algorithm details.

## When to use

- Designing `Access-Control-Allow-Origin` / credentials policy for a browser client on another origin
- Debugging failing OPTIONS preflights or missing Access-Control-* response headers
- Fixing cookie/auth header failures caused by `*` + credentials conflicts
- Correcting CDN/proxy cache breakage from missing `Vary: Origin`
- Handling Private Network Access when a public page calls localhost/private IP

Prefer `http` for general HTTP protocol work. Prefer `rest-api` for OpenAPI and
resource design. Prefer `oauth` when the failure is token/redirect related.

## Preflight triggers

A request is not "simple" (and needs a successful OPTIONS preflight) when any of
these apply:

- Any request header outside the CORS-safelisted set (Accept, Accept-Language,
  Content-Language, and Content-Type with restrictions)
- `Content-Type` other than `application/x-www-form-urlencoded`,
  `multipart/form-data`, or `text/plain`
- Methods other than CORS-safelisted methods (notably `PUT`, `DELETE`, `PATCH`,
  and custom methods)
- `ReadableStream` request body
- Upload event listeners on `XMLHttpRequest.upload`

One trigger is enough. Simple requests skip OPTIONS entirely.

## Credentials mode

- `Access-Control-Allow-Origin: *` cannot be combined with credentials; reflect an
  exact allowed origin instead
- Credentialed responses need `Access-Control-Allow-Credentials: true`
- Fetch: `credentials: 'include'`; XHR: `withCredentials = true`
- Without credentials mode, browsers omit cookies on cross-origin requests

## Wildcard limitations

- `*` is not a subdomain pattern; `*.example.com` is not a valid Allow-Origin value
- Never pair `*` with credentials; echo a validated allowlisted origin
- Prefer explicit `Access-Control-Allow-Headers` / `Access-Control-Expose-Headers`
  lists for broad client compatibility even when `*` is accepted in some browsers

## Origin validation

- Validate `Origin` against an allowlist before reflecting it
- Anchor host matches; a naive `example.com` substring check also matches
  `evilexample.com`
- Treat `null` Origin (sandboxed iframes, some `file://` cases) as untrusted and
  reject unless there is an explicit, documented exception
- Missing Origin usually means same-origin navigation or a non-browser client—
  decide the policy explicitly rather than reflecting blindly

## Vary header

- Include `Vary: Origin` whenever the response depends on Origin, even for a
  single allowed origin
- Without Vary, shared caches may reuse one origin's CORS response for another
- For preflight responses, also vary on `Access-Control-Request-Method` and
  `Access-Control-Request-Headers` when those affect the response

## Exposed headers

- By default JS can read only the CORS-safelisted response headers
  (Cache-Control, Content-Language, Content-Type, Expires, Last-Modified, Pragma)
- Custom headers such as `X-Request-ID` or `X-RateLimit-*` need
  `Access-Control-Expose-Headers`

## Preflight caching

- `Access-Control-Max-Age` reduces repeated OPTIONS traffic
- Browser caps apply (commonly ~2h in Chrome, up to 24h in Firefox); larger
  values are reduced silently
- Cache key is per origin + URL + request characteristics
- Use `0` or omit Max-Age while iterating on CORS config so stale preflights do
  not hide fixes

## Debugging

- A browser CORS error means the request usually reached the server; inspect
  server logs and the exact missing/forbidden header in DevTools
- Preflight failure: OPTIONS must return 2xx **with** the required CORS headers;
  404/500 on OPTIONS fails CORS even if the real route works
- `fetch` `mode: 'no-cors'` yields an opaque empty body—rarely the desired API
  integration path
- Confirm proxies are not stripping Access-Control-* headers after the app sets
  them

## Common server mistakes

- Setting CORS headers only on the main handler and forgetting OPTIONS
- Omitting CORS headers on 4xx/5xx so the browser hides the real error body
- Emitting multiple Allow-Origin values or a combined `"*", "https://example.com"`
  list—the header must be a single origin or `*`
- Reflecting Origin without allowlist validation

## Security boundaries

- Prefer allowlist reflection over blind Origin echo
- Treat CORS as a browser read gate, not a substitute for server enforcement;
  protect sensitive mutations with authentication and CSRF defenses
- Private Network Access: public websites calling loopback/private targets may
  need a PNA preflight success including
  `Access-Control-Allow-Private-Network: true` (see Chrome / WICG sources)

## Quick reference

| Situation | Play |
| --- | --- |
| Cookie / Authorization across origins | Exact Allow-Origin + Allow-Credentials; never `*` |
| OPTIONS fails for JSON POST | Treat as preflight; return 2xx + Allow-Origin/Methods/Headers |
| Works in app, breaks behind CDN | Add `Vary: Origin` (+ preflight request header varies) |
| JS cannot read rate-limit header | Add Access-Control-Expose-Headers |
| Public page → localhost API | Check Private Network Access preflight sources |
| Cite normative rules | `references/sources.md` |
