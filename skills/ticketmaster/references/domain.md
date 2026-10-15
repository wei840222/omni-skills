# Ticketmaster Domain Knowledge

## Open Surface

- Open here: Discovery API search and lookup for events, venues, attractions, and classifications.
- Not open here: partner-only offers, cart, checkout, hold, publish, or inventory mutation flows.
- If the user asks for purchase automation, explain the boundary first instead of implying the open API can do it.

## Core Rules

### 1. Start with Discovery API, not purchase assumptions
- Use search and lookup endpoints for events, venues, attractions, and classifications first.
- Cart, order, hold, or refund actions are outside the open flow boundary.

### 2. Always pass `apikey` as a query parameter
- Official open endpoints expect `apikey`.
- Keep the key in `TM_API_KEY` and out of files, screenshots, and pasted examples.

### 3. Constrain the search before paging
- Prefer `keyword` plus location or identity filters such as `city`, `countryCode`, `dmaId`, `marketId`, `venueId`, or `attractionId`.
- Ticketmaster documents deep paging only while `size * page < 1000`, so tighten filters early.

### 4. Use UTC timestamps and read sales windows carefully
- `startDateTime`, `endDateTime`, and onsale filters should be ISO-8601 UTC strings like `2026-05-01T00:00:00Z`.
- Read `sales.public.startDateTime`, `sales.presales`, and `dates.start` before describing availability.

### 5. Inspect embedded objects, not just the event headline
- Read `_embedded.venues`, `_embedded.attractions`, classifications, locale, and price ranges when present.
- Venue or city mismatches usually mean the query is too broad or the market is cross-listed.

### 6. Respect documented quota and rate limits
- Default quota is 5000 calls per day with 5 requests per second.
- Cache event IDs and venue IDs locally when iterating on the same search space.

### 7. Keep local defaults local
- Store locale, country, city, market, and preferred sort order in `<state_root>/memory.md`.
- Keep API keys and purchase data strictly out of skill memory.

## Common Traps

- Using `countryCode` alone for large markets -> noisy result sets and wasted quota.
- Treating Discovery results as purchase confirmation -> the open API exposes listings, not checkout guarantees.
- Paging deep without filters -> results become unsupported once `size * page` reaches 1000.
- Using local time strings -> events shift or disappear; convert to UTC ISO timestamps.
- Ignoring locale -> multilingual markets can return names or links that look inconsistent.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| `https://app.ticketmaster.com/discovery/v2/*.json` | Search keywords, locale, timestamps, IDs, filters, and `apikey` | Search and fetch events, venues, attractions, and classifications |

Use GET discovery calls only. Keep everything else local.

No other data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- Search terms, filters, locale, timestamps, and IDs sent to Ticketmaster Discovery API
- Your API key sent as the documented `apikey` query parameter

**Data that stays local:**
- Preferences and defaults in `<state_root>/`
- Saved command patterns and notes you choose to keep

**This skill does NOT:**
- Place orders, hold inventory, or bypass partner-only purchase flows
- Store `TM_API_KEY` in skill memory
- Access files outside `<state_root>/`

## Scope

This skill ONLY:
- Uses the open Ticketmaster Discovery API surface
- Provides copy-ready curl queries and the bundled `assets/ticketmaster.sh` helper
- Stores local search defaults in `<state_root>/`

This skill NEVER:
- Uses hidden or undocumented endpoints
- Claims checkout, refunds, or seat locking through open Discovery API
- Writes secrets into local memory

## Trust

By using this skill, data is sent to Ticketmaster (ticketmaster.com).
Only install if you trust Ticketmaster with your search terms and event lookup data.
