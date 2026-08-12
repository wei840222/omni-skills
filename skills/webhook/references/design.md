# Webhook Event Design

## Payload Structure
* Include a specific event `type` field (e.g., `{"type": "order.created"}`) so receivers can route and filter events efficiently.
* Include an ISO 8601 timestamp with a timezone offset to indicate exactly when the event occurred.
* Deliver the full resource representation in the payload if possible. This saves the receiver from having to make a synchronous API call back to your service to fetch the data.
* Include an `api_version` field to manage breaking changes to the payload schema over time.

## Security Checklist
* Accept and register HTTPS endpoints only.
* Provide a mechanism for users to rotate webhook secrets. Support multiple active secrets concurrently during the rotation window.
* Keep sensitive information (e.g., passwords, API keys) out of webhook payloads. The webhook URL and signature provide authentication, while transport encryption provides payload confidentiality.
* Apply a separate delivery quota to each receiver endpoint so a slow or misconfigured receiver remains isolated from other deliveries.
