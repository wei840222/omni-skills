## Core Rules

### 1. Choose the Expedia mode before doing anything else
- Use web mode for public-page research, redirect mode for partner search plus deeplink flows, and Rapid mode for lodging booking APIs.
- State the mode in the output so the user knows whether the result came from a public page, a redirect integration, or a partner booking surface.
- If partner credentials are missing, stay in web mode and explain the limit clearly.

### 2. Separate search, price check, and booking
- Expedia flows often expose a search result, then a price-validation step, then a booking step.
- Treat an initial listing price as an estimate requiring further validation before booking.
- Re-check cancellation, taxes, fees, and inventory freshness before saying a choice is ready to book.

### 3. Compare the real trip cost, not the headline number
- Include taxes, resort or property fees, bag or seat exposure when packages include flights, and transfer friction when a package looks cheap but fragile.
- If one option wins only because key costs are hidden until later, say that directly.
- For multi-room or multi-traveler cases, calculate exact costs using specified constraints instead of naive nightly multiplication.

### 4. Keep partner flows and consumer browsing separate
- Public Expedia pages are useful for visible evidence and manual comparison.
- Partner APIs are for authorized search, deeplinks, price checks, and bookings inside approved integrations.
- State API rights, partner status, or write access only when explicit proof is verified.

### 5. Treat flights as a specialized subproblem
- Expedia may surface flight inventory, but route quality, misconnect risk, baggage traps, and fare-family judgment still belong to deep flight analysis.
- Use Expedia here for packaging, combined-trip economics, and booking context.
- When flight complexity dominates the decision, hand off the route logic to `flight`.

### 6. Keep storage minimal and redacted
- Store reusable filters, accepted or rejected option patterns, and confirmed booking deadlines in `<state_root>/`.
- Keep API secrets, payment data, and full authorization headers completely out of storage.
- In request logs, keep only mode, endpoint family, safe params, status, and timestamp.

### 7. Return decision-ready outputs
- For search: give 3 to 5 options with why each survived filtering.
- For packages: show what is actually bundled, what remains exposed, and what should be re-checked.
- For partner work: separate current capability, required next call, and remaining blocker.


## Requirements

- No credentials required for Expedia public-page research and manual comparison.
- Partner API work is optional and needs Expedia-issued credentials for the specific surface in use.
- Rapid lodging work needs partner access plus the credentials required for signature authentication.
- Travel Redirect work needs Expedia-issued API key plus authorization credentials for redirect search flows.
- Confirm before sending passenger names, billing details, or partner account data to any live Expedia endpoint.


## Coverage

This skill is designed for Expedia-specific work that usually fails when an agent treats the platform like a generic travel site:
- hotel and vacation-rental discovery on Expedia
- package comparison where flights plus stays change the real total
- cars and activities discovery when Expedia is the execution surface
- partner-side search, deeplink, and booking flows
- booking-safe summaries before the user commits money


## Common Traps

- Quoting search prices as final totals -> taxes, fees, or package caveats appear later and break trust.
- Mixing partner API and public-page data without timestamps -> stale or contradictory results look authoritative.
- Treating every Expedia result like a lodging-only choice -> packages, flights, and add-ons change the decision shape.
- Assuming a deeplink is reusable forever -> tokenized or session-bound flows expire.
- Letting package savings hide weak flight shape or bad location -> the bundle looks cheap but performs badly.
- Logging authorization material or shared-secret artifacts -> avoidable credential leak.


## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| `https://www.expedia.com/*` | search terms, destination, dates, traveler counts, and navigation signals | public-page search, comparison, and verification |
| `https://apim.expedia.com/hotels/listings` | lodging query parameters plus partner auth headers | Travel Redirect lodging discovery and deeplink workflows |
| `https://api.ean.com/v3/*` and `https://test.ean.com/v3/*` | partner-authenticated lodging search, content, price-check, and booking payloads | Rapid lodging partner workflows |

No other data is sent externally unless the user explicitly approves another source.


## Security & Privacy

Data that may leave your machine:
- destination queries, travel dates, traveler counts, and optional partner search parameters sent to Expedia services

Data that stays local:
- shortlist notes, booking gates, recurring defaults, and redacted request logs in `<state_root>/`

This skill does NOT:
- store API keys, shared secrets, or payment details in markdown files
- claim partner capabilities without verified credentials
- book or modify travel without explicit user approval
- use hidden scraping, bypass, or anti-bot evasion techniques
- modify its own `SKILL.md`


## Trust

This skill can send travel search context and optional partner request data to Expedia services.
Only use live Expedia calls if you trust Expedia with the trip-planning or partner-integration context relevant to the task.


## Scope

This skill ONLY:
- searches and compares Expedia inventory with explicit evidence
- prepares booking-safe summaries for stays, packages, cars, and activities
- guides authorized Expedia partner workflows for redirect or Rapid lodging usage

This skill strictly ensures:
- verifying prices thoroughly before promising a final bookable price
- declaring account access or partner authorization only upon successful verification
- revealing stale data, fee uncertainty, and package tradeoffs clearly
