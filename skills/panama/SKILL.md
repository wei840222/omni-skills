---
name: panama
description: >
  Plan a Panama trip with region-aware routing, verified entry orientation,
  island and highland logistics, and practical tourist safety. Use for Panama
  City + Canal, Bocas del Toro, Guna Yala / San Blas, Boquete / Chiriquí,
  Santa Catalina / Coiba, or Azuero surf corridors with realistic transfer
  buffers. Not for inventing nationality-specific visa outcomes, stacking
  San Blas + Bocas + Boquete into one short trip, or treating Panama as a tiny
  country where everything fits without overnight buffers.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇵🇦"}'
  related-skills: '{"booking":"Keep hotel, flight, and excursion reservation hygiene after the Panama route is chosen.","car-rental":"Decide when a self-drive segment in Azuero, highlands, or Pacific coast actually helps.","english":"Support calls, bookings, and service interactions when language scaffolding is the main need.","food":"Extend meal planning beyond the Panama food playbook.","spanish":"Everyday Spanish for menus, bookings, and on-the-ground talk once the route is set.","travel":"Build a multi-country itinerary when Panama is only one stop.","travel-planning":"Day-by-day multi-stop itineraries when the trip leaves Panama."}'
---

## State location

Panama trip state may exist in `<workspace>/panama/`, `<workspace>/memory/panama/`, or `~/panama/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/panama/`, `<workspace>/memory/panama/`, `~/panama/`.
3. If none exists and the user wants planning context kept, create `<workspace>/panama/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/panama/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/memory.md` only when the user wants trip context kept across sessions. Legacy `~/Clawic/data/panama/` is a migration source only. Keep it out of the active lookup order, and move it only when the user asks.

## When to load

Load this skill for a Panama trip plan, itinerary, entry/solvency orientation, domestic flight-versus-boat choice, region pairing, island package constraints, or seasonal safety question. Identify passport, dates/month, corridor preference, and transfer tolerance before locking a route.

Read `references/sources.md` before repeating a visa duration, solvency amount, metro fare, park rule, or emergency number. Re-check the official page for that nationality and travel date before the user books a non-refundable flight or island package.

| Need | File |
| --- | --- |
| Empty state or first setup | `references/setup.md` |
| Passport, onward ticket, solvency | `references/entry-and-documents.md` |
| Affidavit, cash, Tocumen arrival | `references/customs-and-border.md` |
| Corridor selection | `references/regions.md` |
| Sample 4–12 day frames | `references/itineraries.md` |
| Lodging strategy | `references/accommodation.md` |
| Budget friction and cost traps | `references/budget-and-costs.md` |
| Flights, buses, ferries, water taxis | `references/transport-domestic.md` |
| Self-drive and road quality | `references/road-trips-and-driving.md` |
| Panama City | `references/panama-city.md` |
| Canal and nearby day trips | `references/canal-and-day-trips.md` |
| Bocas del Toro | `references/bocas-del-toro.md` |
| Guna Yala / San Blas | `references/guna-yala-and-san-blas.md` |
| Boquete / Chiriquí Highlands | `references/boquete-and-chiriqui-highlands.md` |
| Santa Catalina / Coiba | `references/santa-catalina-and-coiba.md` |
| Azuero / Venao / Pedasí / Cambutal | `references/azuero-and-pacific-coast.md` |
| Food, nightlife, family, access | `references/food-guide.md`, `references/nightlife.md`, `references/family-travel.md`, `references/accessibility.md` |
| Safety and season | `references/safety-and-emergencies.md`, `references/weather-and-seasonality.md` |
| Connectivity and apps | `references/telecoms-and-apps.md` |
| Official source map | `references/sources.md` |
| Persisted trip context | `assets/memory-template.md` |

## Core rules

1. Route by corridor, not wish list: City + Canal, Caribbean islands, western highlands, and Pacific surf each behave like different trips.
2. Lock entry compliance before non-refundable island or domestic segments.
3. Ask for month first: rain, rough seas, whale season, surf, and trail access change what is realistic.
4. Always offer two logistics models for multi-corridor routes (flight-heavy vs ground/boat-heavy) with tradeoffs.
5. Budget friction, not just room rates: airport transfers, boats, cash-only stops, park fees, and last-mile access.
6. Treat boat schedules, weather windows, cash needs, and indigenous-territory rules as hard constraints.
7. Deliver action plans: base strategy, transfer buffers, reservation timing, weather/sea fallback, and a route-specific safety note.

## Operating plan

Answer the immediate question first. When the user wants a route, return:

- Base / corridor logic
- Day flow with transfer windows
- Reservation deadlines
- Weather or sea-state backup
- Safety note for the chosen corridor
- Cash vs card execution note for islands and remote stops

For an empty state file, follow `references/setup.md` and copy the structure from `assets/memory-template.md` into `<state_root>/memory.md` only after the user wants memory kept.

## Common traps

- Combining Panama City, San Blas, Bocas, and Boquete in one short trip.
- Treating island transfers as flexible when sea conditions and first/last boats are the bottleneck.
- Booking San Blas or Coiba without confirming inclusions, cash needs, and luggage limits.
- Staying too far from the activity base and losing hours to transfers.
- Underpacking for humidity and rain, then struggling with wet gear on boats.
- Assuming cards work everywhere outside Panama City and major hotels.
- Stacking same-day international arrival with a remote island connection and no overnight buffer.

## Source freshness

Domain claims in this package were last bulk-checked against the URLs in `references/sources.md` (see file header). Before any booking-critical statement, open the matching official page again for the user's passport and travel month.
