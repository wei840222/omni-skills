# CORS research sources

Verified 2026-10-19. Prefer these URLs over memory when restating header rules.

## Normative / primary

- **Fetch Standard — CORS protocol** — preflight algorithm, safelisted requests/headers, and CORS response checks — https://fetch.spec.whatwg.org/#cors-protocol
- **Fetch Standard — HTTP CORS protocol** — HTTP header processing for CORS — https://fetch.spec.whatwg.org/#http-cors-protocol
- **MDN — CORS guide** — practical preflight, credentials, and debugging overview (canonical MDN path) — https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS

## Response headers

- **MDN — Access-Control-Allow-Origin** — exact origin vs `*`, credentials interaction — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin
- **MDN — Access-Control-Allow-Credentials** — credentialed CORS responses — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Credentials
- **MDN — Access-Control-Max-Age** — preflight cache lifetime — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Max-Age
- **MDN — Access-Control-Expose-Headers** — which response headers JS may read — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Expose-Headers
- **MDN — Vary** — cache correctness when responses depend on Origin — https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary
- **MDN — CORS missing Allow header from preflight** — common preflight failure mode — https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS/Errors/CORSMissingAllowHeaderFromPreflight

## Private Network Access

- **Chrome Developers — Private Network Access preflight** — why public→private/loopback calls need an additional preflight success — https://developer.chrome.com/blog/private-network-access-preflight
- **Chrome Developers — Private Network Access update** — rollout/behavior updates for PNA — https://developer.chrome.com/blog/private-network-access-update
- **WICG Private Network Access** — draft specification for private network permission prompts/preflights — https://wicg.github.io/private-network-access/
- **Chrome Status — Private Network Access** — feature tracking — https://chromestatus.com/feature/5436853517811712

## Agent Skills format

- https://agentskills.io/llms.txt
- https://agentskills.io/specification
- https://agentskills.io/skill-creation/best-practices
- https://github.com/agentskills/agentskills/tree/main/skills-ref

## Notes / corrections from baseline

- Legacy short link `https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS` redirects to the Guides path above; cite the Guides URL.
- MDN currently has **no** dedicated `Access-Control-Allow-Private-Network` header reference page (HTTP 404 on 2026-10-19); cite Chrome/WICG instead of inventing an MDN header URL.
- Historical W3C TR/cors material redirects into the Fetch Standard; prefer Fetch anchors.
