# Webhook Event Design

## Payload Structure
* Include a specific event `type` field (e.g., `{"type": "order.created"}`) so receivers can route and filter events efficiently.
* Include an ISO 8601 timestamp with a timezone offset to indicate exactly when the event occurred.
* Deliver the full resource representation in the payload if possible. This saves the receiver from having to make a synchronous API call back to your service to fetch the data.
* Include an `api_version` field to manage breaking changes to the payload schema over time.

## Security Checklist
* Enforce HTTPS for all webhook endpoints. Never transmit data over plain HTTP.
* Provide a mechanism for users to rotate webhook secrets. Support multiple active secrets concurrently during the rotation window.
* Do not include sensitive information (e.g., passwords, API keys) in the webhook payload. The webhook URL and signature provide authentication, but payload confidentiality relies on transport encryption.
* Rate limit outgoing webhooks per receiver endpoint. A slow or misconfigured receiver must not consume resources that affect deliveries to other users.
