---
name: ireland
description: >
  Plan an Ireland trip with local-perspective city bases, coastal routing, pub and
  food choices, weather-aware pacing, and realistic driving or transit tradeoffs.
  Use for Dublin, Cork/Kerry, Galway/Connemara, Wild Atlantic Way segments, Ancient
  East loops, family pacing, or pub-music nights. Not for treating full-island loops
  as short itineraries, treating scenic road distance as motorway time, or inventing
  border/visa outcomes without official checks.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇮🇪"}'
  related-skills: '{"travel":"Multi-country or multi-region itineraries when Ireland is only one stop.","booking":"Hotel, rail, car, and attraction reservation hygiene after the Ireland route is chosen.","food":"Broader meal planning beyond the Ireland food playbook.","irish":"Irish language and local phrase support for menus and on-the-ground talk.","english":"Booking and communication support when language scaffolding is the main need.","esim":"Connectivity and eSIM setup once city or coastal bases are set."}'
---

## State location

Ireland trip state may exist in `<workspace>/ireland/`, `<workspace>/memory/ireland/`, or `~/ireland/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/ireland/`, `<workspace>/memory/ireland/`, `~/ireland/`.
3. If none exists and the user wants planning context kept, create `<workspace>/ireland/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/ireland/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/memory.md` only when the user wants trip context kept across sessions. Legacy `~/Clawic/data/ireland/` is a migration source only. Keep it out of the active lookup order, and move it only when the user asks.

### State tree

| Path | Purpose |
| --- | --- |
| `<state_root>/memory.md` | Trip context, activation preference, and evolving constraints |

## When to load

Load this skill for an Ireland trip plan, Dublin city break, Cork/Kerry or Galway/Connemara routing, Wild Atlantic Way segment choice, Ancient East heritage loops, pub and live-music nights, weather-aware coastal pacing, family travel, or practical driving versus transit tradeoffs.

Identify travel month, trip length, driving comfort on the left, city-versus-coast split, and must-see constraints before locking multi-base routes.

Read `references/sources.md` before repeating emergency numbers, public-transport claims, border-day logistics, or booking-critical visitor rules. Re-check the official page for the traveler's dates before non-refundable bookings.

| Need | File |
| --- | --- |
| Empty state or first setup | `references/setup.md` |
| Core rules and tourist traps | `references/operating-rules.md` |
| Region choice and route strategy | `references/regions.md` |
| Sample itinerary frames | `references/itineraries.md` |
| Lodging strategy | `references/accommodation.md` |
| Dublin playbook | `references/dublin.md` |
| Cork playbook | `references/cork.md` |
| Galway playbook | `references/galway.md` |
| Wild Atlantic Way pacing | `references/wild-atlantic-way.md` |
| Food and pubs | `references/food-guide.md`, `references/nightlife.md`, `references/wine.md` |
| Experiences, beaches, hikes | `references/experiences.md`, `references/beaches.md`, `references/hiking.md` |
| Culture and family | `references/culture.md`, `references/with-kids.md` |
| Transport and apps | `references/transport.md`, `references/apps.md`, `references/telecoms.md` |
| Safety | `references/emergencies.md` |
| Official source map | `references/sources.md` |
| Persisted trip context template | `assets/memory-template.md` |
| Evaluation harness only | `test-prompts.json` |

## Near-miss handoffs

- Multi-country routing beyond Ireland → `travel`
- Reservation holds after the route is chosen → `booking`
- Irish-language phrases → `irish`
- Broader cuisine planning beyond Ireland playbooks → `food`
- eSIM/connectivity setup → `esim`

## Core rules

1. Prefer one city base plus one coastal region for short trips; cap longer trips at 2–3 bases to limit transfer fatigue.
2. Be specific: name neighborhoods, timing windows, and fallback plans instead of brochure slogans.
3. Treat Temple Bar as a one-pass novelty, not the default every night; push better-value pub and food areas when the user wants atmosphere without peak tourist markup.
4. Never treat scenic road distance as motorway time. Build weather fallback into every coastal day.
5. Flag full-island loops, one-night county hopping, and same-day overpacked ticket stacks as common traps.
6. Match the plan to month and daylight: shoulder seasons for value/crowds, peak summer for early lodging, winter for culture-first city breaks.
7. Deliver action plans: base logic, day flow, reservation deadlines, weather backup, and a transport note for the chosen region.

## Operating plan

Answer the immediate question first. When the user wants a route, return:

- Base logic and the region cluster being chosen
- Day flow with realistic transfer or driving windows
- Reservation deadlines (lodging, ticketed sites, car pickup)
- Weather backup for coastal or outdoor days
- Nightlife or food note that avoids default tourist traps
- First-day transport and connectivity plan

For an empty state file, follow `references/setup.md` and copy the structure from `assets/memory-template.md` into `<state_root>/memory.md` only after the user wants memory kept.

## Prefer these checks

- Compress region lists when the calendar only supports one city plus one coastal segment.
- Re-check live transport and weather pages before locking long rural drives or cliff visits.
- Keep tasting and pub plans light on driving days; decide the non-driver in advance.
- For families, reduce back-to-back long scenic drives and always keep an indoor backup.
- For border/North day trips, confirm ID and logistics rather than assuming seamless same-day hops.

## Source freshness

Domain claims in this package were last bulk-checked against the URLs in `references/sources.md` (see file header). Before any booking-critical statement, open the matching official page again for the user's travel month and route.

## Security and privacy

Trip preferences stay in `<state_root>/` when the user opts into memory. Do not invent network side effects; this skill is guidance plus local state only.