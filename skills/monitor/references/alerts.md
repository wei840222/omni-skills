# Monitor Alerts

## Configuration

Use the `config` entry in `assets/alert-examples.json` when drafting `<state_root>/config.json`. Monitor targets and schedules remain canonical in `<state_root>/monitors.json`; alert configuration contains channel preferences and per-monitor threshold overrides only. The default `log` channel records an event locally and is not evidence of an external notification.

The `ENV:` values are this package's credential-reference notation, not a built-in host expansion feature. Resolve each reference through the host secret mechanism immediately before sending. Persist a webhook destination reference/identifier when its URL contains a token; the asset's URL is an illustrative placeholder only. Confirm recipient, authorized data scope and channel availability before sending.

## Transition State

Use `<state_root>/alerts/state.json` per monitor to retain last known status, consecutive-failure count, outage-start timestamp, an event identifier, and per-channel delivery/attempt state. Serialize overlapping checks and use the host's atomic scoped-update mechanism; a parse failure or failed state write blocks delivery to prevent duplicate or lost transitions. Re-read state under the same lock before each update.

1. First observation: establish a known `ok`/`fail` baseline; send an initial alert only if explicitly requested. An `unknown` result establishes neither.
2. `ok` → `fail`: record outage start at the first failed sample and increment the streak. A positive integer `failure_threshold` (2 in the example) gates notification. Keep the transition pending until the threshold is reached rather than losing it when the second failure repeats the same status.
3. Repeated `fail`: update streak and result. Once eligible, allocate one failure event for the outage, including failure count; send it once per authorized channel. Further failed samples suppress new failure events.
4. `fail` → `ok`: reset the streak and close the outage. Send recovery only to channels for which a failure alert was successfully accepted, unless the user requested all recoveries. Include the duration between first failed and first recovered sample, labeled as sampled duration.
5. `unknown`: record the diagnostic separately; reset the consecutive-failure streak while preserving last known status and any open outage. A still-open pending transition can become eligible after a new full streak. A monitoring-error alert needs its own explicitly confirmed policy.

Read the failure/recovery payload examples from `assets/alert-examples.json`; their timestamps and figures are illustrative. Record UTC timestamps consistently. Availability, outage duration and recovery are limited by sampling interval and missed checks, not exact continuous measurements.

## Channel Execution

Prefer the host's supported notification tool when one exists. The following API contracts apply only where a direct HTTP adapter is exposed and authorized. Host messaging restrictions take precedence over shell examples.

### Pushover

The API accepts an HTTPS POST to `https://api.pushover.net/1/messages.json` with required `token`, `user`, and `message` form fields. URL-encode every field; plain form concatenation corrupts messages containing `&`, `+` or similar characters. Supply secrets through the host secret transport, keeping them out of command arguments, logs and persisted files.

Use connection and total-request deadlines (3 and 10 seconds are example policy values). Acceptance requires **HTTP 200 plus JSON `status: 1`**. This means received and queued by Pushover, not displayed/read on the recipient's device. A 4xx response or a JSON status other than 1 requires correcting the input/quota/account issue before another attempt. Redact diagnostics and report failed acceptance plainly.

### Webhook

Send a validated JSON payload with `Content-Type: application/json` to the exact confirmed destination through its authorized adapter. For an approved non-messaging HTTP adapter, curl's `--data-binary @-` preserves stdin JSON bytes; keep destination secrets protected by the host transport too. Interpret success using that destination's documented HTTP/body contract; a generic 2xx is not proof of downstream message delivery. Redirects require an explicit same-scope policy.

## Delivery Recovery and Spam Prevention

Persist the event and its channel-attempt intent before sending; record acceptance only after validating the response. Delivery errors remain pending with redacted diagnostics, not marked sent. Retry only the same event under a bounded host retry policy. Use an event identifier/idempotency key when supported.

A timeout or crash between sending and recording acceptance makes delivery ambiguous. Without receiver idempotency, present the uncertainty and follow the user's duplicate-vs-loss policy; exactly-once delivery is not guaranteed. A pending failure that recovers before confirmed delivery is resolved as a local incident and delivery-gap record, rather than sending a stale outage message. Suppression applies to successfully accepted events, not to unknown send outcomes.

## Sources

- Pushover required parameters, response contract and error handling: https://pushover.net/api
- curl URL encoding, stdin body preservation and deadlines: https://curl.se/docs/manpage.html

Thresholds, baseline rules, event state and retry policy are this package's explicit operational design, not provider defaults.
