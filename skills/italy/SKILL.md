---
name: italy
description: >
  Plan Italy trips with region-aware city routing, ZTL and rail logistics,
  local food playbooks, and practical tourist safety. Use for Rome, Florence,
  Venice, Naples/Amalfi, Tuscany countryside, or multi-region corridors with
  realistic transfer buffers. Prefer `travel` for multi-country systems,
  `booking` after a base is chosen, `car-rental` for self-drive segments,
  `food` beyond the Italy food playbook, `italian` for language, and
  `rome` / `venice` when the ask is city-resident depth rather than Italy
  trip routing. Not for inventing nationality-specific visa outcomes,
  stacking Rome + Venice + Amalfi into one short trip without overnight
  buffers, or treating ZTL as optional when driving into historic centers.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇮🇹"}'
  related-skills: '{"travel":"Multi-country trip systems when Italy is one stop among several.","booking":"Reservation search and booking completion after an Italy base or corridor is chosen.","car-rental":"Vehicle pickup and insurance handoff for self-drive Tuscany/countryside segments—pair with ZTL avoidance.","food":"Deeper restaurant and cuisine planning beyond the Italy food playbook.","english":"Communication clarity for bookings, menus, and service interactions.","italian":"Italian language support when local wording is the main need.","travel-planning":"Day-by-day multi-stop itineraries when the trip leaves Italy.","rome":"Rome-resident neighborhood, cost, and lifestyle depth beyond visitor routing.","venice":"Venice neighborhood and water-transport depth beyond a visitor day plan."}'
---

## State location

Optional Italy trip context may exist in `<workspace>/italy/`,
`<workspace>/memory/italy/`, or `~/italy/`. Before reading or writing
state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/italy/`, `<workspace>/memory/italy/`, `~/italy/`.
3. If several candidate directories exist, use only the highest-precedence one and
   report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create
   `<workspace>/italy/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. Create
or update `<state_root>/memory.md` only when the user wants trip context kept
across sessions. Legacy `~/Clawic/data/italy/` is a migration source only—
keep it out of the active lookup order, and move it only when the user asks.
Scripts and shell examples must receive the resolved filesystem path; never
write the literal string `<state_root>` to disk.

## When to load

Load this skill for an Italy trip plan, itinerary, city-versus-region corridor
choice, rail/self-drive tradeoffs, ZTL risk, local food routing, museum booking
timing, or family pacing question. Identify passport or entry pathway, travel
month, corridor preference, and driving intent before locking a route.

Read `references/sources.md` before repeating Schengen/ETIAS status, emergency
numbers, rail fares, ZTL fines, or museum ticket rules. Re-check the matching
official page for that nationality and travel date before the user books
non-refundable flights, trains, or island ferries.

| Need | File |
| --- | --- |
| Empty state or first setup | `references/setup.md` |
| Official source map | `references/sources.md` |
| Sample 4–14 day frames | `references/itineraries.md` |
| Lodging strategy | `references/accommodation.md` |
| Rome | `references/rome.md` |
| Florence / Tuscany city | `references/florence.md` |
| Venice | `references/venice.md` |
| Naples & pizza | `references/naples.md` |
| Regions overview | `references/regions.md` |
| Food & restaurants | `references/food-guide.md` |
| Wine | `references/wine.md` |
| Experiences & bookings | `references/experiences.md` |
| Beaches | `references/beaches.md` |
| Hiking | `references/hiking.md` |
| Nightlife / aperitivo | `references/nightlife.md` |
| Culture & etiquette | `references/culture.md` |
| Family travel | `references/with-kids.md` |
| Trains, buses, driving, ZTL | `references/transport.md` |
| SIM / connectivity / apps | `references/telecoms.md`, `references/apps.md` |
| Safety & emergencies | `references/emergencies.md` |
| Persisted trip context | `assets/data-templates.md` |

## Architecture

```text
<state_root>/
└── memory.md     # Trip context, route logic, and evolving constraints
```

## Core rules

1. Route by corridor, not wish list: Rome, Florence/Tuscany, Venice, Naples/Amalfi,
   and Sicily/Sardinia each behave like different trips.
2. Confirm entry and border friction before non-refundables using
   `references/sources.md` (Schengen / ETIAS / MFA orientation).
3. Prefer rail between major cities; treat self-drive as a countryside tool and
   park outside historic centers—ZTL cameras issue real fines.
4. Be specific: name a restaurant, neighborhood, booking window, or transfer—
   not generic “try pasta in Italy.”
5. Match local timing: riposo, late dinner, Monday museum closures, August
   closures in inland towns.
6. Flag tourist-trap patterns with replacements (Testaccio/Trastevere over
   Piazza Navona dining; bacari over San Marco menus).
7. Deliver operational plans: base strategy, transfer windows, reservation
   deadlines, weather/crowd downgrade, and a route-specific safety note.

## Operating plan

Answer the immediate question first. When the user wants a route, return:

- Base / corridor logic
- Day flow with transfer windows
- Reservation deadlines or sellout risks (Uffizi, Vatican, popular trains)
- Crowd or heat backup
- Safety note for the chosen corridor (pickpocket / ZTL / heat)
- Cash vs card note for markets and small towns

For an empty state file, follow `references/setup.md` and copy the structure from
`assets/data-templates.md` into `<state_root>/memory.md` only after the
user wants memory kept.

## Common traps

- Stacking Rome + Florence + Venice + Amalfi into one short trip with no overnight buffers.
- Driving into historic centers and collecting ZTL camera fines.
- Booking museum tickets on-site for Vatican, Uffizi, or Accademia in peak season.
- Ordering cappuccino after breakfast or asking for Alfredo / chicken pasta as local dishes.
- Paying seated café prices when a standing bar espresso was intended.
- Eating dinner before kitchens open (~19:30–20:00 in many cities).
- Accepting “free” gifts from street sellers who then demand payment.

## Source freshness

Domain claims in this package were last bulk-checked against the URLs in
`references/sources.md` (see file header). Before any booking-critical statement,
open the matching official page again for the user's passport and travel month.
