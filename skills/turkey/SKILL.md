---
name: turkey
description: >
  Plan a Turkey trip by cluster, entry pathway, and season. Use for Istanbul,
  Cappadocia, Aegean, Mediterranean, Black Sea, or southeast routing, domestic
  transport, and weather backups. Not for filing a visa, booking flights, or
  stating a nationality rule without checking the official source for that passport.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇹🇷"}'
  related-skills: '{"booking":"Keeps reservation names, deadlines, and confirmation hygiene aligned with the Turkey route.","car-rental":"Chooses a rental only when a coast or inland cluster actually benefits from a car.","food":"Extends regional meal planning beyond the Turkey food playbook.","travel":"Builds the multi-stop itinerary when Turkey is one part of a larger trip.","turkish":"Supports menus, bookings, and on-the-ground language once the route is chosen."}'
---

## State location

Turkey state may exist in `<workspace>/turkey/`, `<workspace>/memory/turkey/`, or `~/turkey/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/turkey/`, `<workspace>/memory/turkey/`, `~/turkey/`.
3. If none exists and the user wants planning context kept, create `<workspace>/turkey/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/turkey/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/memory.md` only when the user wants trip context kept across sessions. Legacy `~/Clawic/data/turkey/` is a migration source only. Keep it out of the active lookup order, and move it only when the user asks.

## When to load

Load this skill for a Turkey trip plan, itinerary, visa pathway check, domestic transport choice, regional routing, or seasonal safety question. Identify passport, dates, cluster, and pace before locking a route.

Read `references/sources.md` before repeating a visa duration, passport-validity rule, airport transfer, museum-pass scope, or emergency number. Re-check the official page for that nationality and travel date before the user books a non-refundable flight or pays a visa fee.

| Need | File |
| --- | --- |
| Empty state or first setup | `references/setup.md` |
| Visa, e-Visa, passport, booking names | `references/entry-and-documents.md` |
| Customs and first-hour arrival | `references/customs-and-arrival.md` |
| Regional route selection | `references/regions.md` |
| Sample itineraries | `references/itineraries.md` |
| Where to stay by route style | `references/accommodation.md` |
| Budget, cards, cash, tipping | `references/budget-and-costs.md`, `references/payments-and-tipping.md` |
| Flights, rail, buses, ferries, driving | `references/transport-domestic.md`, `references/road-trips-and-driving.md` |
| Museums and one regional playbook | `references/archaeology-and-museums.md`, then the matching regional file |
| Food, nightlife, family, access | `references/food-guide.md`, `references/nightlife.md`, `references/family-travel.md`, `references/accessibility.md` |
| Safety and season | `references/safety-and-emergencies.md`, `references/weather-and-seasonality.md` |
| Connectivity | `references/telecoms-and-apps.md` |
| Official source map | `references/sources.md` |
| Persisted trip context | `assets/memory-template.md` |

## Core rules

1. Keep one macro-cluster per week: Istanbul, Cappadocia plus Central Anatolia, one west-coast cluster, one Mediterranean cluster, or one southeast history cluster.
2. Confirm the entry pathway in `references/entry-and-documents.md` before non-refundable bookings. Visa-free, e-Visa, and consular visa are different paths, and the rule is passport-specific.
3. Offer two movement models when the route spans regions: flight-heavy for west-east compression, or surface-heavy inside one cluster where scenery and archaeology matter more than speed.
4. Load `references/weather-and-seasonality.md` before promising balloons, beaches, long ruins days, mountain roads, or Black Sea viewpoints.
5. Lock fragile pieces first: balloon backup, cave or old-town rooms, east-west flights, dense museum timing, and a car only when the cluster needs one.
6. Price the full route: airport transfers, peak premiums, fuel, tolls, parking, site tickets, and domestic baggage.
7. Every plan names the base, transfer windows, reservation deadlines, a weather or transport backup, and the safety note for that region.

## Operating plan

Answer the immediate question first. Then, when the user wants a route, return:

- Base-city logic and the cluster being chosen
- Day flow with transfer windows
- Reservation deadlines
- Weather or transport backup
- Safety note for the chosen region

For an empty state file, follow `references/setup.md` and copy the structure from `assets/memory-template.md` into `<state_root>/memory.md` only after the user wants memory kept.

## Common traps

- Treating Istanbul, Cappadocia, Antalya, Ephesus, and Mardin as one short seamless loop.
- Applying one visa pathway to every passport.
- Booking IST and SAW as if they were the same airport.
- Planning ruins, viewpoints, and beach time in July or August without a heat plan.
- Defaulting to a rental car inside a dense urban core.
- Covering the whole country instead of one west route or one east route.
- Building a Cappadocia day that fails if the balloon is cancelled.

## Security and privacy

Trip preferences stay in `<state_root>`. This skill reads and writes only that resolved directory for its own state. It does not fetch live prices or visa decisions; the agent checks `references/sources.md` and the official page when a time-sensitive fact is required.
