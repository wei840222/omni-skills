# Source Connectors — Google Reviews

Keep source behavior explicit. Prefer official APIs when the user can authorize them; fall back to exports or user-approved page checks.

## Source matrix

| Source | Typical coverage | Preferred access | Main risks |
| --- | --- | --- | --- |
| Google Business Profile reviews | Verified location reviews and owner replies | Business Profile API (`accounts.locations.reviews`) with OAuth | Missing locations, delayed sync, reply moderation latency |
| Places / Maps public review signals | Consumer-facing place ratings and selected review text | Places API Place Details (field-masked) or user-approved page check | Field availability varies by API version and SKU; attribution rules apply |
| Google Shopping / merchant review signals | Product or merchant sentiment where exposed | Merchant Center / Merchant API workflows or user export | Sparse text, account scoping, product-vs-merchant mismatch |
| Manual Google review pages | Spot checks and verification | User-approved fetch only | Rate limits, layout drift, incomplete history |

## Connector rules

1. Define owner and permissions before the first fetch for each source.
2. Save connector status per brand: `active`, `degraded`, `blocked`.
3. Keep last-success timestamp and last-error reason for troubleshooting.
4. Use source-specific retry policy; stop after bounded retries and surface the failure.
5. State the access mode (`api`, `export`, `page-check`) in every user-facing result.

## Business Profile notes

- Listing, retrieving, replying to, and deleting review replies are account-scoped owner workflows. Consumer research does not require reply rights.
- Replies are reviewed against Google content policies and may take minutes to days before public posting.
- Customers can edit reviews after a reply; treat edit events as first-class deltas.

## Places / Maps notes

- Place Details can return rating and review fields when requested with the correct field mask.
- Display and attribution requirements from Google Maps Platform docs still apply when surfacing review text.
- If a field is unavailable for the configured API version, say so and fall back to another authorized path.

## Shopping / merchant notes

- Product review and merchant review pipelines are not interchangeable with location Business Profile reviews.
- Prefer user exports or documented Merchant Center workflows when direct review APIs are unavailable in the current project.
- Do not invent Shopping review payloads from unrelated product listing fields.

## Refresh windows

- Heartbeat: short trailing window (for example last 24–72h)
- Deep refresh: wider trailing window (for example 7–30d) to catch late edits
- Backfills: only when baseline is missing or the source contract changed

## Fallback order

1. Official API path with valid credentials and scope
2. User-provided export
3. Manual page verification with user approval
