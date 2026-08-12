# Webhook Receiving: Best Practices

## Signature Verification
* Verify every request with the provider's documented signature scheme to confirm the payload's origin.
* Extract the raw body bytes. Parsed JSON objects might reorder keys, which breaks body-signature verification.
* Use a timing-safe string comparison function whenever validating a secret-derived signature.
* If the signature is missing or invalid, return the delivery contract's documented 4xx response and log the attempt for investigation.

## Replay Prevention
* Extract and verify the timestamp when the provider includes it in the signed input.
* Compare the timestamp with the current server time using the provider's documented tolerance; five minutes is a common provider policy, not a universal default.
* Reject requests older than the accepted tolerance to prevent captured webhooks from being replayed.
* Allow the provider's documented clock-skew margin for time drift between servers.
* Store processed event IDs and reject duplicates, even if they arrive within the valid time window.

## Idempotency (Critical)
* Treat webhook delivery as at-least-once. Senders will retry on timeouts or network issues.
* Store processed event IDs in a durable data store (e.g., Redis, database) for 24-72 hours.
* Ensure all webhook handlers are idempotent. Processing the exact same event multiple times must yield the same system state as processing it once.

## Fast Response
* Acknowledge the webhook with HTTP 200 or 202 immediately after signature validation.
* Defer actual processing to an asynchronous background job or queue.
* Respond quickly because senders typically enforce a 5-30 second timeout. Slow responses lead to retries and duplicate events.

## Error Handling
* Return 2xx to indicate successful receipt. The sender will mark the event as delivered.
* Return the documented 4xx response for terminal failures (e.g., invalid signature, unrecognized event type).
* Return 5xx for temporary failures (e.g., database unavailable) so a compliant sender can retry.
* Log the full payload on error, taking care to redact sensitive fields.
