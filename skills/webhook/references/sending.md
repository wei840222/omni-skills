# Webhook Sending: Best Practices

## Delivery Strategy and Retries
* Implement an exponential backoff strategy with jitter for retries (e.g., 1m, 5m, 30m, 2h, 8h).
* Limit the maximum number of retry attempts (e.g., 5-10 times) to prevent infinite loops.
* Classify responses through an explicit delivery policy: terminal configuration or authentication failures complete the delivery, while documented transient statuses continue through the retry schedule.
* Honor `Retry-After` and apply the receiver contract to 408, 425, and 429 rather than treating every 4xx response as terminal.
* Treat timeouts as failures and schedule a retry.

## Signature Generation
* Sign the raw JSON body to guarantee integrity. Document the specific signing algorithm used (e.g., HMAC-SHA256).
* Include a timestamp in the signature calculation to allow receivers to prevent replay attacks.
* Format the signature header clearly, for example: `Webhook-Signature: t=timestamp,v1=signature`. This format allows for future versioning.
* Provide clear verification code examples in multiple languages to reduce integration friction for receivers.

## Timeouts and Network
* Set a strict request timeout (for example, 5-10 seconds) and release the delivery worker for the next scheduled attempt when it expires.
* Deliver each attempt to the registered endpoint with redirects disabled; require a subscription update before changing the destination.
* Require a valid HTTPS certificate chain for every delivery endpoint.

## Delivery Tracking
* Record the details of every delivery attempt, including the URL, HTTP status code, response time, and response body.
* Provide a dashboard for users to view the delivery status of their webhooks and the retry queue.
* Include a manual retry mechanism for users to replay failed webhooks once they have resolved issues on their receiver endpoint.
* Retain webhook logs for a reasonable period (7-30 days) for debugging purposes.
