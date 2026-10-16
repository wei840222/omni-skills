# REST API Sources

Live-checked during local takeover of Jules session `5335078998024883537`
(2026-10-17, Asia/Taipei). Prefer these URLs over model memory for normative
claims. Re-check before quoting version-sensitive details.

## Claim inventory and freshness

| Topic | Freshness | Source of truth | Refactor outcome |
| --- | --- | --- | --- |
| Agent Skills package shape | Spec-sensitive | agentskills.io specification + skills-ref | Frontmatter `version` + JSON-string `openclaw` / `related-skills`; no `displayName` / `os` in openclaw. |
| OpenAPI contract-first | Stable domain | OpenAPI 3.1 | Contract before handlers; examples + security per operation. |
| HTTP semantics / status | Stable domain | RFC 9110 | Method/status policy; 307/308 for method-preserving redirects. |
| Problem Details errors | Stable domain | RFC 9457 (successor to RFC 7807) | Stable machine `code` + human `message`; Problem Details when ecosystem uses it. |
| API abuse / BOLA | Stable domain | OWASP API Security Top 10 (2023) | Object-level authz; rate limits; schema validation. |
| Resource / versioning style | Stable guidance | Google AIP (API Improvement Proposals) | Additive change preference; versioned routes for breaks. |
| Pagination / JSON:API | Optional style | JSON:API format | Cursor pagination guidance retained as one proven pattern. |

## Verified sources

### Agent Skills

- **Document index** — entry point for current Agent Skills docs. <https://agentskills.io/llms.txt>
- **Specification** — normative package / frontmatter / progressive-disclosure rules. <https://agentskills.io/specification>
- **skills-ref validator** — reference validator package (`uvx --from skills-ref agentskills validate`). <https://github.com/agentskills/agentskills/tree/main/skills-ref>

### OpenAPI / HTTP

- **OpenAPI Specification 3.1** — normative OpenAPI document model. <https://spec.openapis.org/oas/v3.1.0.html>
- **Swagger OpenAPI hub** — publisher hub linking the same specification family. <https://swagger.io/specification/>
- **RFC 9110 — HTTP Semantics** — methods, status codes, and redirect semantics. <https://datatracker.ietf.org/doc/html/rfc9110>
- **RFC 7231 (historic)** — earlier semantics document still widely cited. <https://www.rfc-editor.org/rfc/rfc7231>

### Errors

- **RFC 9457 — Problem Details for HTTP APIs** — current Problem Details standard. <https://www.rfc-editor.org/rfc/rfc9457.html>
- **RFC 7807** — predecessor Problem Details document (superseded by 9457). <https://datatracker.ietf.org/doc/html/rfc7807>

### Security

- **OWASP API Security Top 10 (2023)** — BOLA, broken auth, unrestricted resource consumption, and related API risks. <https://owasp.org/API-Security/editions/2023/en/0x11-t10/>

### API design guidance

- **Google AIP overview** — resource-oriented design guidance. <https://cloud.google.com/apis/design>
- **Google AIP — Errors** — error model guidance. <https://cloud.google.com/apis/design/errors>
- **Google AIP — Resources** — resource naming and ownership. <https://cloud.google.com/apis/design/resources>
- **Google AIP — Versioning** — compatibility and versioning guidance. <https://cloud.google.com/apis/design/versioning>
- **JSON:API format** — optional document/pagination conventions. <https://jsonapi.org/format/>

## Obsolete or rejected claims

- Do not keep `metadata.openclaw.displayName` / broad `os` arrays as required
  openclaw fields; follow current refactored siblings (`gcp`, `fastapi`).
- Do not treat Jules' soft wording-only patch or fabricated CHANGELOG `#891` as
  Gate evidence.
- Do not cite the OWASP project root URL that currently 404s; use the 2023
  Top 10 edition URL above.
