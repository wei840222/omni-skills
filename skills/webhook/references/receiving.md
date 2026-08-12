# Webhook Receiving: Best Practices

## Signature Verification
* Verify the HMAC signature for every request to confirm the payload's origin.
* Extract the raw body bytes. Parsed JSON objects might reorder keys, which breaks the signature generation.
* Use a timing-safe string comparison function to validate the signature and prevent timing attacks.
* If the signature is missing or invalid, reject the request with HTTP 401 Unauthorized and log the attempt for investigation.

## Replay Prevention
* Extract the timestamp from the webhook payload or headers.
* Compare the timestamp with the current server time.
* Reject requests older than the acceptable tolerance (usually 5 minutes). This prevents captured webhooks from being replayed.
* Allow a small clock skew (1-2 minutes) to account for time drift between servers.
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
* Return 4xx for permanent failures (e.g., invalid signature, unrecognized event type). This signals the sender to stop retrying.
* Return 5xx for temporary failures (e.g., database unavailable). The sender will retry using exponential backoff.
* Log the full payload on error, taking care to redact sensitive fields.
