# Flight Data APIs

Scope: building something that searches, prices, tracks or books flights. Pricing and tier details below were recorded in mid-2026 and move constantly — the **shape** of each provider is stable, the numbers are not. Verify on the provider's own pricing page before designing around a figure.

**Contents:** [Pick By What You Need To Do](#pick-by-what-you-need-to-do) · [Search And Book](#search-and-book) · [Search Only](#search-only) · [Status And Tracking](#status-and-tracking) · [Reference Data](#reference-data) · [Awards And Loyalty](#awards-and-loyalty) · [What Does Not Exist](#what-does-not-exist) · [Design Constraints](#design-constraints) · [Credentials](#credentials)

## Pick By What You Need To Do

| Need | Category | Reality |
|---|---|---|
| Show prices and send the user somewhere to buy | Metasearch affiliate feed | Easiest and cheapest; you never touch a ticket |
| Actually issue tickets | GDS or NDC aggregator | Requires an agreement, a deposit or bonding, and settlement plumbing |
| Track flights in the air | Status API | Cheap, plentiful, differentiated by latency and coverage |
| Analyse historical prices | Price-analysis endpoints or your own store | Historical price data is thin and mostly proprietary |
| Find award availability | Scraping-based aggregators | Legally grey, fragile, no official source exists |
| Anything else | Start with reference data and a status API; they cover most side projects | — |

## Search And Book

- **Amadeus for Developers** — the widest airline coverage of the self-serve options, with search, pricing, ancillaries and booking. Free test environment with synthetic or cached data; production requires an agreement and behaves differently from test. The test-to-production gap is the standard first surprise.
- **Duffel** — modern REST, NDC-first, a smaller but growing airline set, and the easiest path from zero to a real ticket. Subscription plus a per-booking fee; low-cost carriers are covered unevenly.
- **Kiwi's partner API** — virtual-interlining inventory, including combinations no airline sells, and multi-modal options. Verify self-transfer risk and the provider's current commercial terms before use.
- **Sabre and Travelport** — the other GDSs, enterprise sales cycles, not self-serve.
- Booking through any of these makes you a seller of travel, with the consumer-protection, refund and insolvency obligations that follow in most jurisdictions. That is a business decision before it is a technical one.

## Search Only

- **Skyscanner** and other metasearch partner programmes — cached prices, redirect-to-buy, partner approval required. Good for a comparison surface, useless for booking.
- **Travelpayouts and affiliate aggregators** — cached and lagging data, aimed at content sites. Fine for trends and "cheapest month" style features, wrong for quoting a bookable price.
- **Google Flights has no public API.** Scraping it breaches the terms of service; the QPX product it replaced was retired years ago. Any library claiming to offer it is scraping.
- Cached prices are the recurring failure: the price shown is not the price at checkout, and users blame you rather than the cache. State the age of the data in the UI.

## Status And Tracking

- **FlightAware AeroAPI** — the reference option for positions, delays and historical on-time data, with a usable free tier and per-call pricing above it.
- **FlightRadar24** — best-in-class positional and ADS-B data, tiered from hobbyist to enterprise.
- **AviationStack**, **AeroDataBox** and similar — schedules and status at low cost through API marketplaces, with correspondingly variable coverage outside major carriers.
- **OpenSky Network** — community ADS-B data, free for non-commercial use, with coverage gaps and no schedule layer.
- What to check before choosing: update latency, coverage of the specific carriers, historical-data availability, provider terms, and the intended use of operational data.

## Reference Data

- Airport, airline and aircraft codes, timezones and runway data are available from open datasets and from the paid providers as a bundled endpoint.
- IATA and ICAO codes are not interchangeable, and both exist for airports and airlines. Store both; resolving one to the other later is a data-cleaning project.
- Timezones are the quiet killer: schedule times are local, offsets change with daylight saving on different dates in different countries, and elapsed-time calculations silently break twice a year. Store UTC alongside local, always.
- Use the regulator or loyalty programme's published distance and applicability method when a compensation band or award chart depends on distance.

## Awards And Loyalty

- **No official award-availability API exists**, from any airline or alliance. Every product in this space scrapes, and each breaks when a carrier changes its site or blocks them.
- Keep loyalty-programme passwords out of agent-managed state. Prefer manual, user-supplied balances and retain only non-secret context (`memory-template.md`).
- Airline programme APIs, where they exist, are partner-only.
- The maintainable design is manual entry into `## Loyalty` in `<state_root>/memory.md`, refreshed on a user-approved cadence.

## What Does Not Exist

Worth saying early in any project, because these are the four things people assume:

- A unified award-search API across programmes.
- A public Google Flights API.
- A price-prediction API with published accuracy.
- A cross-airline API for booking with points.

## Design Constraints

- **Rate limits and caching**: search endpoints are expensive and slow. Cache aggressively by route and date, and never poll a search endpoint on a timer for a price alert — that is what price-analysis and calendar endpoints are for.
- **Price integrity**: a search result is an offer that expires. Re-price before checkout and handle the change in the UI; the alternative is a support queue.
- **Idempotency**: booking calls must be idempotent or you will double-book on a retry. This is the failure that costs real money.
- **Test environments lie**: cached or synthetic inventory, different error shapes, and no real ticketing. Budget time for the production-only bugs.
- **Storing personal data**: passenger names, dates of birth and document numbers are regulated personal data in most jurisdictions. Do not persist them beyond what the booking requires, and never in a project's plain-text store.
- **Displaying prices**: show total including taxes, and state the currency and the time of the quote.

## Credentials

Store API keys, client secrets, and OAuth tokens outside `<state_root>/`. Retain only a pointer such as `env:AMADEUS_CLIENT_SECRET`, `env:DUFFEL_API_KEY`, `keychain:flightaware-aeroapi`, or `1password:Dev/Kiwi`. When the user asks to save supplied configuration, retain the pointer and remove the secret value (`memory-template.md`).

**When a provider is chosen for a project**, record the choice — the provider, not the key — as a preference in `<state_root>/config.yaml` under `tooling`, so the next session does not re-run this comparison.
