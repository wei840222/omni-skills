---
name: webhook
description: Design, implement, or review secure webhook receivers and senders. Use when integrating provider event callbacks or delivering events to customer endpoints.
metadata:
  openclaw: '{"emoji":"🪝"}'
---

## Webhook Delivery Workflow

Use this skill to establish a portable webhook delivery contract before implementation or review:

1. Identify the direction: consume a provider's events or publish events to customer endpoints.
2. Define authentication, replay prevention, idempotency, response semantics, and delivery observability before handling production traffic.
3. Keep provider-specific signature formats and retry rules in the integration's own documentation and configuration.

## References

Load the following references based on the task context:

* For an endpoint that consumes third-party webhooks, read `references/receiving.md` for signature verification, idempotency, response classification, and fast acknowledgment.
* For a service that publishes webhooks to customer endpoints, read `references/sending.md` for delivery classification, retries, signing, timeouts, and delivery records.
* For event payload structure and endpoint security, read `references/design.md`.
* For claim freshness, primary-source provenance, and scope limits, read `references/research.md`.
