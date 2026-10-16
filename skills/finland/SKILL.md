---
name: finland
description: >
  Plan Finland trips with verified Schengen entry orientation, season-aware
  corridor routing, rail-and-Lapland logistics, and practical tourist safety.
  Use for Helsinki city breaks, Lapland aurora/winter bases, Lakeland cabins,
  Turku/archipelago summers, VR night trains, HSL airport transfers, sauna
  etiquette, or family pacing. Prefer `travel` for multi-country systems,
  `booking` after a base is chosen, `car-rental` for vehicle handoff details,
  `food` beyond the Finland food playbook, and `english` for booking-language
  clarity. Not for inventing nationality-specific visa outcomes, promising
  aurora certainty, or stacking Helsinki + Lapland + archipelago into one
  short trip without transfer buffers.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇫🇮"}'
  related-skills: '{"travel":"Multi-country trip systems when Finland is one stop among several.","booking":"Reservation search and booking completion after a Finland base or corridor is chosen.","car-rental":"Vehicle pickup, insurance, and winter-equipment handoff for self-drive Finland segments.","food":"Deeper restaurant and cuisine planning beyond the Finland food playbook.","english":"Communication clarity for bookings, menus, and service interactions.","finnish":"Finnish language support when local wording is the main need.","travel-planning":"Day-by-day multi-stop itineraries when the trip leaves Finland."}'
---

## State location

Optional Finland trip context may exist in `<workspace>/finland/`,
`<workspace>/memory/finland/`, or `~/finland/`. Before reading or writing
state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/finland/`, `<workspace>/memory/finland/`, `~/finland/`.
3. If several candidate directories exist, use only the highest-precedence one and
   report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create
   `<workspace>/finland/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. Create
or update `<state_root>/memory.md` only when the user wants trip context kept
across sessions. Legacy `~/Clawic/data/finland/` is a migration source only—
keep it out of the active lookup order, and move it only when the user asks.
Scripts and shell examples must receive the resolved filesystem path; never
write the literal string `<state_root>` to disk.

## When to load

Load this skill for a Finland trip plan, itinerary, Schengen entry orientation,
Helsinki-versus-Lapland corridor choice, domestic rail/flight/car tradeoffs,
seasonal safety, sauna etiquette, or family pacing question. Identify passport
or entry pathway, travel month, corridor preference, cold/transfer tolerance,
and aurora expectation before locking a route.

Read `references/sources.md` before repeating visa durations, EES/ETIAS status,
customs thresholds, emergency numbers, or transport fares. Re-check the matching
official page for that nationality and travel date before the user books
non-refundable flights, cabins, or night trains.

| Need | File |
| --- | --- |
| Empty state or first setup | `references/setup.md` |
| Schengen stays, visas, EES/ETIAS | `references/entry-and-documents.md` |
| Customs, food, cash, border reality | `references/customs-and-border.md` |
| Macro-regions and corridor choice | `references/regions.md` |
| Sample 4–14 day frames | `references/itineraries.md` |
| Lodging strategy | `references/accommodation.md` |
| Budget friction and hidden costs | `references/budget-and-costs.md` |
| Cards, cash, tax-free, tipping | `references/payments-and-tax-free.md` |
| Flights, trains, buses, ferries | `references/transport-domestic.md` |
| Self-drive and winter roads | `references/road-trips-and-driving.md` |
| Parks, cabins, trails | `references/nature-and-national-parks.md` |
| Helsinki / capital region | `references/helsinki-and-capital-region.md` |
| Lapland | `references/lapland.md` |
| Lakeland / Tampere | `references/lakeland-and-tampere.md` |
| Turku / archipelago | `references/turku-and-archipelago.md` |
| Food, nightlife, family, access | `references/food-guide.md`, `references/nightlife.md`, `references/family-travel.md`, `references/accessibility.md` |
| Sauna and culture | `references/sauna-and-culture.md` |
| Safety and season | `references/safety-and-emergencies.md`, `references/weather-and-seasonality.md` |
| Connectivity and apps | `references/telecoms-and-apps.md` |
| Official source map | `references/sources.md` |
| Persisted trip context | `assets/finland-data-templates.md` |

## Architecture

```text
<state_root>/
└── memory.md     # Trip context, route logic, and evolving constraints
```

## Core rules

1. Route by season and daylight first: July city-hopping, September foliage,
   January aurora, and March family snow trips are different products.
2. Confirm entry and border friction before non-refundables using
   `references/entry-and-documents.md` and `references/customs-and-border.md`.
3. Choose one primary corridor for short trips: Helsinki/south, Lapland, or
   Lakeland/archipelago.
4. For any route beyond Helsinki, offer two transport models (rail/flight-heavy
   vs self-drive/bus-heavy) with tradeoffs.
5. Budget secondary costs: airport transfers, sleeper supplements, winter
   clothing, sauna/spa, groceries, alcohol, and activity pickups.
6. Treat aurora as probability management, never a guarantee.
7. Deliver operational plans: base strategy, transfer windows, booking risks,
   weather downgrade, and a route-specific safety note.

## Operating plan

Answer the immediate question first. When the user wants a route, return:

- Base / corridor logic
- Day flow with transfer windows
- Reservation deadlines or sellout risks
- Weather or darkness backup
- Safety note for the chosen corridor
- Cash vs card execution note for remote stops

For an empty state file, follow `references/setup.md` and copy the structure from
`assets/finland-data-templates.md` into `<state_root>/memory.md` only after the
user wants memory kept.

## Common traps

- Treating Helsinki and Lapland as a casual same-week add-on with no transfer buffer.
- Assuming winter is romantic by default without checking darkness, cold tolerance, and clothing.
- Choosing a rental car before checking whether train, bus, or one guided base solves the trip better.
- Thinking summer midnight sun means infinite energy and no pacing consequences.
- Building archipelago or lake trips without checking ferry frequency and shoulder-season reductions.
- Carrying a U.S.-style tipping mindset into a mostly service-included culture.
- Quoting border, visa, or EES/ETIAS details from memory instead of current official pages.

## Source freshness

Domain claims in this package were last bulk-checked against the URLs in
`references/sources.md` (see file header). Before any booking-critical statement,
open the matching official page again for the user's passport and travel month.
