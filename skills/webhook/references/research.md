# Webhook Research Record

## Claim inventory

* **Stable domain guidance:** authenticating the exact request body, replay resistance, idempotent handling, bounded retries, and delivery observability.
* **Provider-specific guidance:** signature algorithm, signed fields, replay tolerance, accepted acknowledgment status, retryable responses, and retry schedule. Resolve these from the active provider contract before implementation.
* **Version-sensitive guidance:** provider SDK APIs and endpoint configuration fields. Confirm these from the current provider documentation rather than this package.

## Receiving webhooks

* **Stripe — Webhooks:** <https://docs.stripe.com/webhooks> — use the raw request body for signature verification, return a successful response promptly, and handle duplicate events safely.
* **GitHub — Validating webhook deliveries:** <https://docs.github.com/en/webhooks/using-webhooks/validating-webhook-deliveries> — validate the delivery signature against the received payload and use a timing-safe comparison.
* **GitHub — Best practices for using webhooks:** <https://docs.github.com/en/webhooks/using-webhooks/best-practices-for-using-webhooks> — process deliveries efficiently and use webhook identifiers to support idempotent handling.

## Sending webhooks

* **RFC 9110 — HTTP Semantics:** <https://www.rfc-editor.org/rfc/rfc9110> — interpret response status codes in the delivery contract and treat retry decisions as protocol semantics rather than a blanket 4xx rule.
* **MDN — Retry-After:** <https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Retry-After> — honor server retry guidance when the receiver supplies it.

## Scope limit

These sources support portable design guidance. The integration owner supplies the authoritative provider-specific signature, retry, timeout, and status-code contract.
