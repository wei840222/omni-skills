---
name: webhook
description: Implement secure webhook receivers and senders with proper verification, replay prevention, and idempotency.
metadata:
  openclaw: '{"emoji":"🪝"}'
---

## Webhook Architecture Guidelines

This skill provides comprehensive guidelines for designing, receiving, and sending webhooks securely and reliably.

When building or reviewing a webhook integration, always verify the following core principles:
1. **Security**: Webhooks must authenticate the sender via signature verification and prevent replay attacks.
2. **Reliability**: Receivers must be idempotent and respond quickly. Senders must implement exponential backoff retries.
3. **Traceability**: All events and delivery attempts must be logged for debugging.

## References

Load the following references based on the task context:

* If the user is building an endpoint to consume webhooks from a third-party service, read `references/receiving.md` for signature verification, idempotency, and fast response guidelines.
* If the user is designing a system that publishes webhooks to customer endpoints, read `references/sending.md` for retry strategies, signature generation, and timeout configurations.
* For guidelines on structuring the JSON payload and general security posture, read `references/design.md`.
