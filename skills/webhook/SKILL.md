---
name: webhook
description: Design, implement, or review secure webhook receivers and senders. Use when integrating provider event callbacks or delivering events to customer endpoints.
metadata:
  openclaw: '{"emoji":"🪝"}'
---

## Webhook delivery workflow

1. Identify the direction: consume a provider's events or publish events to customer endpoints.
2. Define authentication, replay prevention, idempotency, response semantics, and delivery observability before handling production traffic.
3. Resolve the provider-specific signature format, retry policy, timeout, and accepted status codes from the active provider contract. Do not generalize one provider's policy to another.

## Receiving webhooks

### Signature verification

- Verify every request with the provider's documented signature scheme. A common pattern is HMAC-SHA256 over the raw request body, but the exact signed fields are provider-specific.
- Preserve raw body bytes before parsing JSON, and compare a secret-derived signature with a timing-safe comparison.
- Reject a missing or invalid signature with the provider's documented terminal 4xx response and log the attempt with sensitive fields redacted.

### Replay prevention and idempotency

- When the provider signs a timestamp, validate it using the provider's documented tolerance and clock-skew margin; five minutes is common, not universal.
- Treat delivery as at-least-once. Store processed event IDs durably and make handlers idempotent: the same event delivered twice must leave the same system state.
- Retain event IDs for a deliberately selected window (often 24–72 hours) that balances retry protection and storage.

### Fast acknowledgment and errors

- After signature validation and durable queue acceptance, return the provider's documented 2xx response promptly and process work asynchronously. Keep receiver latency below the provider timeout.
- Classify responses explicitly: 2xx is accepted; terminal validation failures use the provider's documented 4xx response; temporary downstream failures use 5xx so a compliant sender can retry.
- Log enough context to investigate failures, but redact secrets and other sensitive payload fields.

## Sending webhooks

### Delivery and retries

- Use bounded exponential backoff with jitter (for example 1m, 5m, 30m, 2h, 8h) and a finite retry cap. This is an example schedule, not a replacement for a receiver contract.
- Treat timeouts as delivery failures. Apply the delivery policy to 408, 425, 429, and `Retry-After`; do not assume every 4xx response is terminal.
- Set a strict per-attempt timeout, disable redirects unless the contract explicitly permits them, and require a valid HTTPS certificate chain.

### Signing and tracking

- Sign the raw body with a documented algorithm, include a timestamp in the signed input, and publish an unambiguous signature-header format such as `Webhook-Signature: t=<timestamp>,v1=<signature>`.
- Record each attempt's endpoint, status code, response time, and safely-redacted response body. Provide a way to inspect failures and manually retry a delivery after the receiver is fixed.
- Retain delivery logs for a deliberately selected period (often 7–30 days) consistent with privacy and debugging needs.

## Event design and security

- Include an event `type`, an ISO 8601 timestamp with timezone, and `api_version`. Deliver the full resource representation when it is safe and practical; otherwise include a stable identifier.
- Register HTTPS endpoints only, allow safe secret rotation with overlapping active secrets, and keep passwords, API keys, and other secrets out of payloads.
- Isolate receivers with per-endpoint quotas or rate limits so one slow endpoint cannot degrade others.
- For critical actions, validate the event against the source API when the provider contract requires it; signed delivery alone does not prove every business precondition.

## Sources and freshness boundary

- Use the current provider documentation as the authority for integration-specific behavior. For stable patterns, consult the relevant provider documentation (for example Stripe or GitHub webhook guidance) and HTTP semantics in RFC 9110.
- Provider SDK APIs, endpoint configuration fields, signing algorithms, replay tolerances, retry schedules, and acknowledgment requirements are version-sensitive facts. Verify them at implementation time.
