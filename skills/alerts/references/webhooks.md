# Webhook reliability and authenticity

## Correlation IDs

- Generate one UUID (or equivalent) per incident at first fire.
- Reuse it on create / update / resolve across PagerDuty, Slack, status page, and tickets.
- Put the ID in alert text and webhook bodies so humans and automations join the same thread.

## Retry and backoff

On delivery failure (timeout, 5xx, connection errors):

1. Retry after ~1s, 2s, 4s, 8s, 16s (exponential).
2. Then mark failed and escalate via a backup channel.
3. Log response codes and latency for later debugging.

Do not infinite-retry into a dead endpoint.

## Signature verification

- Prefer HMAC-SHA256 (or the vendor's documented scheme) over shared-secret query params.
- Reject requests with invalid signatures.
- Reject timestamps older than ~5 minutes to limit replay.
- Store secrets only in environment variables (name in config, value in env).

## Circuit breaker

- After **5 consecutive failures**, open the circuit: stop primary webhook, use backup channel, mark endpoint unhealthy.
- Probe recovery every ~30 seconds (or vendor guidance) until success, then close the circuit.
- Page humans if both primary and backup fail.

## Trust boundaries

- Treat inbound webhook JSON as untrusted input; validate schema before side effects.
- Outbound webhooks go only to user-configured HTTPS URLs.
- Never echo secrets or full auth headers into chat alerts.
