---
name: australia
description: >
  Plan an Australia trip with local-perspective city bases, long-distance routing,
  season and weather windows, reef and outback safety buffers, food and wine corridors,
  and realistic flight-versus-drive tradeoffs. Use for Sydney, Melbourne, Brisbane/Gold
  Coast, Cairns/Reef, Adelaide/SA wine, Perth/WA, Hobart/Tasmania, Uluru/Red Centre,
  Great Ocean Road, family pacing, or multi-region route compression. Not for treating
  Australia as one compact destination, stacking Sydney+Melbourne+Reef+Uluru+Perth into
  a short trip, or inventing visa/biosecurity outcomes without official checks.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇦🇺"}'
  related-skills: '{"travel":"Multi-country or multi-region itineraries when Australia is only one stop.","booking":"Hotel, flight, car, and attraction reservation hygiene after the Australia route is chosen.","food":"Broader meal planning beyond the Australia food playbook.","english":"Booking and communication support when language scaffolding is the main need.","sydney":"Deeper Sydney visitor, resident, and neighborhood guidance when the trip is Sydney-centric."}'
---

## State location

Australia trip state may exist in `<workspace>/australia/`, `<workspace>/memory/australia/`, or `~/australia/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/australia/`, `<workspace>/memory/australia/`, `~/australia/`.
3. If none exists and the user wants planning context kept, create `<workspace>/australia/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/australia/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/memory.md` only when the user wants trip context kept across sessions. Legacy `~/Clawic/data/australia/` is a migration source only. Keep it out of the active lookup order, and move it only when the user asks.

### State tree

| Path | Purpose |
| --- | --- |
| `<state_root>/memory.md` | Trip context, activation preference, and evolving constraints |

## When to load

Load this skill for an Australia trip plan, multi-city route compression, Sydney/Melbourne city bases, reef or outback blocks, Great Ocean Road pacing, SA wine corridors, WA distance realism, Tasmania weather-aware driving, family travel, or practical flight-versus-drive tradeoffs.

Identify travel month, trip length, driving comfort, city-versus-nature split, heat/humidity tolerance, and must-see constraints before locking multi-base routes.

Read `references/sources.md` before repeating emergency numbers, entry/biosecurity claims, marine/stinger season notes, park access rules, or booking-critical visitor guidance. Re-check the official page for the traveler's dates before non-refundable bookings.

| Need | File |
| --- | --- |
| Empty state or first setup | `references/setup.md` |
| Core rules and tourist traps | `references/core-rules.md` |
| Region choice and route strategy | `references/regions.md` |
| Sample itinerary frames | `references/itineraries.md` |
| Long-distance route patterns | `references/road-trips.md` |
| Lodging strategy | `references/accommodation.md` |
| Entry and biosecurity | `references/entry-and-biosecurity.md` |
| Sydney playbook | `references/sydney.md` |
| Melbourne playbook | `references/melbourne.md` |
| Brisbane and Gold Coast | `references/brisbane-gold-coast.md` |
| Cairns and Reef | `references/cairns-reef.md` |
| Adelaide and SA | `references/adelaide-sa.md` |
| Perth and WA | `references/perth-wa.md` |
| Hobart and Tasmania | `references/hobart-tasmania.md` |
| Uluru and Red Centre | `references/uluru-red-centre.md` |
| Great Ocean Road | `references/great-ocean-road.md` |
| Food and wine | `references/food-guide.md`, `references/wine.md` |
| Experiences, beaches, hikes, nightlife | `references/experiences.md`, `references/beaches.md`, `references/hiking.md`, `references/nightlife.md` |
| Culture, kids, seasonality | `references/culture.md`, `references/with-kids.md`, `references/seasonality.md` |
| Parks, wildlife, transport, apps, telecoms, costs | `references/national-parks-and-permits.md`, `references/wildlife-safety.md`, `references/transport.md`, `references/apps.md`, `references/telecoms.md`, `references/payment-and-costs.md` |
| Safety | `references/emergencies.md` |
| Official source map | `references/sources.md` |
| Persisted trip context template | `assets/memory-template.md` |
| Evaluation harness only | `test-prompts.json` |

## Near-miss handoffs

- Multi-country routing beyond Australia → `travel`
- Reservation holds after the route is chosen → `booking`
- Broader cuisine planning beyond Australia playbooks → `food`
- Booking and communication scaffolding → `english`
- Sydney-only deep dive (visitor/resident/neighborhoods) → `sydney`

## Core rules

1. Prefer 2–3 anchors max on short trips; pair one urban cluster with one nature block and transfer buffers.
2. Be specific: name bases, timing windows, weather backups, and flight-versus-drive logic instead of brochure slogans.
3. Treat domestic transfer days as real calendar cost; they often consume most useful daylight.
4. Never treat Australia as one compact destination. Cap checklist-heavy Sydney+Melbourne+Reef+Uluru+Perth stacks.
5. Match the plan to hemisphere-opposite seasons, school holidays, wet-season reliability, bushfire/heat windows, and reef/marine conditions.
6. Deliver action plans: base logic, day flow, reservation deadlines, weather/safety backup, and a transport note for the chosen region.

## Operating plan

Answer the immediate question first. When the user wants a route, return:

- Base logic and the region cluster being chosen
- Day flow with realistic flight or driving windows
- Reservation deadlines (lodging, reef operators, parks, car pickup)
- Weather and safety backup for coastal, reef, desert, or remote days
- Food or wine note that avoids default tourist-trap strips when relevant
- First-day transport and connectivity plan

For an empty state file, follow `references/setup.md` and copy the structure from `assets/memory-template.md` into `<state_root>/memory.md` only after the user wants memory kept.

## Prefer these checks

- Compress region lists when the calendar only supports two bases plus one nature block.
- Re-check live weather, park, and marine pages before locking reef, desert, or long remote drives.
- Keep tasting and pub plans light on driving days; decide the non-driver in advance.
- For families, reduce back-to-back long transfers and always keep an indoor or low-heat backup.
- For entry/biosecurity and restricted goods, confirm the traveler's nationality and dates rather than assuming ETA/eVisitor defaults.

## Source freshness

Domain claims in this package were last bulk-checked against the URLs in `references/sources.md` (see file header). Before any booking-critical statement, open the matching official page again for the user's travel month and route.

## Security and privacy

Trip preferences stay in `<state_root>/` when the user opts into memory. Do not invent network side effects; this skill is guidance plus local state only.
