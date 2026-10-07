# Rapid Lodging Workflows

Use this file only when the workspace has authorized Expedia Rapid lodging access.

## What Rapid is for

Rapid is the Expedia partner surface for custom lodging booking flows.

Use it when the task needs:
- structured property content
- live shop and price-check steps
- booking and booking-management flows

Use public web navigation to answer simple public Expedia search questions.

## Authentication reality

- Rapid uses Expedia-issued partner credentials.
- Signature authentication is required for Rapid API requests.
- Keep the API key, shared secret, generated signature, and timestamps out of markdown logs.

## Minimal auth pattern

```bash
TIMESTAMP=$(date +%s)
SIGNATURE=$(printf "%s%s%s" "<rapid-api-key>" "<rapid-shared-secret>" "$TIMESTAMP" | openssl dgst -sha512 -binary | xxd -p -c 256)
AUTH_HEADER="Authorization: EAN APIKey=<rapid-api-key>,Signature=${SIGNATURE},timestamp=${TIMESTAMP}"
```

Use the same timestamp for the signature and the header.

## Execution ladder

1. content or search discovery
2. shop or availability selection
3. price check
4. booking only after explicit approval
5. retrieve or manage booking when needed

Always execute the intermediate price check and validation steps before moving from initial search to booking.

## Booking-safe rules

- Price check before any booking recommendation.
- Re-surface cancellation and fee details after price check, not before.
- Treat hold or resume flows as temporary, not durable storage.
- Treat returned links or tokens as short-lived single-use elements.

## Logging safety

In `<state_root>/partners/request-log.md`, keep only:
- mode: rapid
- endpoint family
- safe query summary
- status
- timestamp

Exclude from logs:
- full auth headers
- shared-secret material
- traveler payment data

## When to stop

Stop and explain the blocker if:
- signature auth is not configured
- test vs production endpoint is unclear
- price check fails or the selected rate is no longer valid
- the task requires live payment but the user has not explicitly approved that step
