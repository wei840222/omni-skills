# Research and Source Provenance — API

Use these primary sources to validate protocol-level claims and to refresh vendor-specific guidance before advising on a version-sensitive behavior. Vendor API sections retain their own Official Docs link as the authority for endpoint, model, quota, and pricing details.

| Topic | Primary source | Use when validating |
|---|---|---|
| HTTP semantics and status codes | <https://www.rfc-editor.org/rfc/rfc9110> | Method safety/idempotency, response status meaning, conditional requests, and header behavior |
| HTTP authentication framework | <https://www.rfc-editor.org/rfc/rfc9110#section-11> | Authentication challenges and credentials carried in HTTP requests |
| OAuth 2.0 authorization framework | <https://www.rfc-editor.org/rfc/rfc6749> | OAuth roles, authorization grants, access tokens, and refresh tokens |
| OAuth PKCE | <https://www.rfc-editor.org/rfc/rfc7636> | Public-client authorization-code flows and proof-key requirements |
| JSON Web Token | <https://www.rfc-editor.org/rfc/rfc7519> | JWT claim and token-format guidance |
| Server-Sent Events | <https://html.spec.whatwg.org/multipage/server-sent-events.html> | SSE framing, reconnection, and browser EventSource behavior |
| Webhook security | <https://cheatsheetseries.owasp.org/cheatsheets/Webhook_Security_Guidelines_Cheat_Sheet.html> | Signature verification, replay controls, source validation, and receiver hardening |
| Retry backoff and jitter | <https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/> | Timeout budgets, retries, and randomized backoff behavior |
| HTTP API design and safety practices | <https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design> | Pagination, idempotency, asynchronous request-reply, and API client design patterns |

## Claim mapping

- `references/core-rules.md` and `references/status-triage.md` use RFC 9110 for HTTP method and response semantics.
- `references/auth.md` and `references/browser.md` use RFC 6749, RFC 7636, and RFC 7519 for OAuth, PKCE, and JWT guidance.
- `references/streaming.md` uses the HTML Server-Sent Events specification for event framing and reconnect behavior.
- `references/webhooks.md` uses OWASP's webhook guidance for signature and replay defenses.
- `references/resilience.md` uses AWS Builders' Library guidance for timeout and jitter principles.

## Freshness rule

For current vendor details, read the Official Docs URL in the relevant `references/apis/*.md` section rather than relying on fixed model names, limits, plan tiers, or endpoint deprecations in this package.
