# API patterns — Umami / Plausible / PostHog

## Umami

- **Tracker**: script uses `data-website-id="<website-uuid>"`. Optional `data-host-url`, `data-domains`, and `data-auto-pageview`.
- **Auth (API)**: `Authorization: Bearer <api-key>`. Self-host also supports username/password; **Umami Cloud requires API keys**.
- **Cloud base**: `https://api.umami.is` (data plane also documents `https://cloud.umami.is/api/send` for send).
- **Send events**: `POST /api/send` with JSON `type` (`event` | `identify` | `performance`) and `payload.website` = website ID (not bare domain).
- **Gotcha**: analytics query timestamps in many Umami list/filter UIs and client helpers expect **milliseconds** (`Date.now()`, `int(time.time() * 1000)`), not seconds.

Sources: https://docs.umami.is/docs/api · https://docs.umami.is/docs/api/authentication · https://docs.umami.is/docs/api/sending-stats · https://docs.umami.is/docs/tracker-configuration

## Plausible

- **Stats API v2**: `POST https://plausible.io/api/v2/query` with header `Authorization: Bearer <STATS_API_KEY>` and JSON body including `"site_id": "<domain-as-registered>"` (the domain string you added in Plausible — **not** a separate opaque numeric id in the public examples).
- **Rate limit**: Stats API keys default to **600 requests per hour**; contact Plausible for higher limits.
- **Events API**: record pageviews/custom events with JSON body using `name`, `url`, `domain` (see Events API). Responses commonly `202 Accepted`.
- **Script**: default pageview on load; SPA needs manual pageviews / script extensions when client routing does not reload the document.

Sources: https://plausible.io/docs/stats-api · https://plausible.io/docs/events-api · https://plausible.io/docs/script-extensions

## PostHog

- **Capture**: public POST endpoints such as `/i/v0/e` and **`/batch`** send events with project `api_key` / project token in the JSON body (not a personal API key).
- **Batch**: `POST .../batch/` with `"batch": [ { "event", "distinct_id", "properties", ... }, ... ]`. Keep payload size within documented limits (commonly under ~20MB).
- **Properties**: must be JSON-serializable maps/values — no DOM elements or functions.
- **Private API rate limits**: authenticated private GET/POST/PATCH/DELETE endpoints are rate limited. Docs describe personal-API-key paths around **600/minute** in some modes, and broader CRUD budgets such as **480/minute** and **4800/hour**. **Public capture POSTs are not rate limited the same way.** Treat “1000/minute” folklore as unverified; use current PostHog rate-limit docs for the endpoint class you call.
- **Regions**: call the correct host (`us.i.posthog.com` / `eu.i.posthog.com` or self-hosted).

Sources: https://posthog.com/docs/api · https://posthog.com/docs/api/capture · https://posthog.com/docs/product-analytics/capture-events

## Shared auth hygiene

| Vendor | Secret | Typical header / field |
|--------|--------|------------------------|
| Umami | API key | `Authorization: Bearer <key>` |
| Plausible Stats | Stats API key | `Authorization: Bearer <key>` |
| PostHog capture | Project token | JSON `api_key` on capture/batch |
| PostHog private API | Personal API key | private endpoint auth |

Never commit real keys. Use env vars such as `UMAMI_API_KEY`, `PLAUSIBLE_API_KEY`, `POSTHOG_PROJECT_API_KEY`.
