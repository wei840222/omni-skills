---
name: parking
description: >
  Find, verify, and reserve parking worldwide with provider selection,
  live-signal triage, and local memory for favorite places and cities.
  Use when the user needs parking now, wants to pre-book for an airport or
  event, needs the right local parking app for a city, or wants help comparing
  parking options across providers. Prefer `maps` for pure navigation /
  geocoding, `travel-planning` for whole-trip itineraries, `booking` for
  non-parking reservation terms, `compare` for generic option matrices, and
  `car-rental` when the core ask is multi-day self-drive rather than a bay.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🅿️","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"booking":"Compare reservation terms, cancellation rules, and booking friction across providers.","car-rental":"Add pickup, return, and vehicle-access context when parking sits inside a driving trip.","compare":"Turn multiple parking options into a clear side-by-side decision.","maps":"Use map providers, geocoding, and route links to ground parking search in real geography.","travel":"Fold parking into standing travel docs and long-lived trip boxes.","travel-planning":"Whole-trip itineraries and budgets beyond a single parking decision."}'
---

# Parking

Help the user find, verify, and (when they approve) hand off to reservation or
payment surfaces for parking. Distinguish map discovery from payment apps and
true reservation inventory. Keep durable favorites and city defaults under
`<state_root>/` only after consent.

## State location

Parking preferences and notes may exist in `<workspace>/parking/`,
`<workspace>/memory/parking/`, or `~/parking/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/parking/`, `<workspace>/memory/parking/`, `~/parking/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable state must be created, default to
   `<workspace>/parking/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. If older
notes exist only at `~/Clawic/data/parking/`, propose a copy/validation/cutover
plan and wait for user confirmation before any migration. Never write the
literal string `<state_root>` to disk.

## When to use

- Quick parking nearby right now
- Airport, train-station, stadium, and venue parking that benefits from
  pre-booking
- Repeated home-city parking where favorites, vehicle limits, and local
  operator habits matter
- Travel planning where the correct provider changes by country or city
- Parking platform research and API scouting for product or integration work

## Quick reference

Load only the smallest file needed for the current parking job (keep SKILL.md
as the router):

| Need | Load |
|------|------|
| Setup / activation | `references/setup.md` + `assets/data-templates.md` |
| Provider / market matrix | `references/provider-registry.md` |
| City patterns | `references/city-patterns.md` |
| Search / book / verify workflows | `references/execution-playbook.md` |
| Public / partner API notes | `references/api-notes.md` |
| Official source ledger | `references/source-ledger.md` |
| Verified URL pins | `references/sources.md` |
| Migration from legacy Clawic paths | `references/migration.md` |

## Requirements

- No credentials are required for planning, provider selection, or official web
  research.
- Live bookings, plate entry, or payment flows require the user to approve the
  chosen provider and any data sent to it.
- Request confirmation before creating persistent local parking memory. Offer a
  one-off mode to discard favorites, city defaults, and discovery notes.
- Promise a guaranteed space only when the provider explicitly exposes
  reservation inventory or confirmed booking status.

## Core rules

### 1. Classify the parking mode before searching

Separate the job into one of five modes: find-now, pre-book, recurring-city,
operator research, or API scouting. Mixing instant parking, on-street payment,
and guaranteed reservation into one workflow degrades answers quickly.

### 2. Default to the lightest successful path

If the user just needs parking now, start with map discovery plus the strongest
official operator or aggregator for that city. Use deeper provider comparison
only when the quick path is ambiguous, expensive, full, or clearly unreliable.
Keep a simple nearby request focused on immediate options rather than a long
market audit.

### 3. Distinguish discovery, payment, and reservation surfaces

- Google Maps, Apple Maps, and Parkopedia are discovery surfaces first.
- Apps such as RingGo, PayByPhone, EasyPark, APCOA Connect, and Parking.sg
  often solve payment or session start; rely on reservation surfaces for
  guaranteed inventory.
- Reservation marketplaces such as SpotHero, ParkWhiz, JustPark EventPass,
  Onepark, Parclick, Q-Park Prebook, and many operator-native airport or venue
  flows are the right surfaces for guaranteed entry when available.

### 4. Verify reservation-critical constraints before recommending

Check entry window, exit rules, in-and-out privileges, height limit, EV
charging, motorcycle or van support, license-plate requirements, and
cancellation terms. For airports and events, confirm walking distance, shuttle
dependency, venue match, and whether the booking is for a specific car park or
only a zone. A cheap option is wrong if the user's vehicle or timing cannot use
it.

### 5. Be precise about availability language

- "Reservable now" means the provider is offering a booking path for the
  requested window.
- "Reported open" means a listing says the facility is operating; use
  reservation surfaces to guarantee a bay.
- "Real-time occupancy" should only be claimed when an official provider or
  city API exposes it directly.

### 6. Keep local parking memory only with consent

Offer to remember home city, recurring venues, favorite facilities, vehicle
constraints, and trusted providers locally in `<state_root>/`. Store durable
notes; keep raw payment data or full booking receipts out of memory. Promote
user-confirmed discoveries such as hidden entrances, repeat scams, and reliable
operator patterns into the local favorites, cities, or findings notes.

### 7. Treat city and country as first-class routing signals

Use `references/provider-registry.md` to choose the right platform family for
the market before assuming Google results or one familiar app will work. Dense
urban centers often use payment apps and operator-native garages, while airports
and major venues often use reservation marketplaces. When entering a new market,
verify the dominant local stack instead of assuming North American or UK
patterns apply worldwide.

### 8. Keep research evidence attached to local discoveries

Save only discoveries that came from the user, an official provider, or a
clearly identified city or operator source. Tag low-confidence hearsay as
unverified and keep it out of favorites until it repeats or gets confirmed. Use
`references/source-ledger.md`, `references/api-notes.md`, and
`references/sources.md` to separate facts, partnership-only APIs, and "no public
API found" cases.

## Common traps

- Treating a pay-by-phone parking app as proof that a space can be reserved —
  many apps start a session only after the driver finds a bay.
- Claiming "spots available" from a static listing page — treat open hours and
  active inventory as distinct concepts.
- Ignoring plate, height, or vehicle-type restrictions — the booking looks fine
  until gate entry fails.
- Recommending street parking for a high-stress event or airport drop —
  uncertainty and enforcement risk overwhelm the small savings.
- Assuming one global app dominates every market — parking is highly local and
  often city-specific.
- Saving raw booking confirmations or payment details — keep reusable parking
  knowledge; exclude sensitive receipts.

## External endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| https://maps.google.com and https://maps.apple.com | place text, coordinates, route context | Quick parking discovery, map links, and local navigation handoff |
| https://www.parkopedia.com and Parkopedia parking data products | location, time window, optional vehicle filters | Global parking discovery, facility detail, and broad market coverage |
| https://spothero.com and https://developer.parkwhiz.com | destination, venue, dates, time window, optional vehicle metadata | North America reservation search and parking booking APIs |
| https://www.justpark.com, https://eventpass.justpark.com, https://ringgo.co.uk, https://www.q-park.co.uk, https://www.apcoaconnect.com, https://www.paybyphone.com | location code, destination, plate, and time window | UK and Europe parking reservation or payment workflows |
| https://parclick.com, https://www.onepark.co, https://www.parkmobile.io, https://parkplus.io, https://www.parking.sg, and official city data portals such as https://data.gov.hk/en/ | destination, date range, vehicle type, plate when required, and occupancy query parameters | Regional booking, payment, or official parking data lookups |

No other data should be sent externally unless the user approves another
official provider or city source.

## Security and privacy

Data that may leave the machine:

- parking destination or venue
- city and time window
- coordinates and route context
- plate number only when the chosen provider requires it for entry or billing
- vehicle profile fields such as height or EV requirement when they change the
  result

Data that stays local:

- favorite parking places and entrances in `<state_root>/favorites.md`
- home-city defaults and provider order in `<state_root>/cities.md`
- user-confirmed discoveries and warnings in `<state_root>/findings.md`
- activation rules and parking boundaries in `<state_root>/memory.md`

## Scope

This skill handles:

- finding, comparing, and explaining parking options
- choosing the right provider family for each city and task
- verifying reservation-critical constraints before the user commits
- maintaining lightweight local memory for favorites, cities, and discoveries
  after approval

## Out of scope

- Pure navigation or geocoding without a parking decision → `maps`
- Whole-trip itineraries and lodging timing → `travel-planning` / `travel`
- Non-parking marketplace booking terms → `booking`
- Generic side-by-side matrices with no parking domain rules → `compare`
- Multi-day self-drive rental logistics → `car-rental`
- Storing payment card data, account passwords, or unnecessary booking receipts
- Claiming guaranteed inventory without provider evidence
- Undeclared anti-bot scraping flows
- Inventing live availability or occupancy
- Treating one country's parking workflow as universal

## Trust

This skill can send parking queries, dates, route context, plate numbers, or
vehicle constraints to the selected parking marketplace, operator, payment app,
maps provider, or official city data source. Use live parking flows only when
the user trusts the chosen provider with that data.
