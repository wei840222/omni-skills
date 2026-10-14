---
name: new-zealand
description: >
  Plan New Zealand trips with island-aware corridors, realistic driving pace,
  outdoor safety, biosecurity, food, and regional bases. Use for Auckland,
  Wellington, Rotorua/Taupo, Queenstown, Christchurch, Nelson/Abel Tasman,
  Fiordland, road trips, ferries, Great Walks, wine, or family itineraries.
  Prefer `travel` for multi-country trip systems, `booking` for reservation
  completion after a base is chosen, `car-rental` for vehicle handoff details,
  `food` for cuisine logging beyond NZ regional guidance, and `english` for
  booking-language clarity.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇳🇿"}'
  related-skills: '{"travel":"Multi-country or multi-destination trip systems when New Zealand is one stop among several.","booking":"Reservation search and booking completion after a New Zealand base or corridor is chosen.","car-rental":"Vehicle pickup, insurance, and handoff logistics for self-drive NZ itineraries.","food":"General cuisine classification and food memory beyond New Zealand regional dishes.","english":"Communication clarity for booking messages and host conversations."}'
---

## State location

Optional New Zealand trip context may exist in `<workspace>/new-zealand/`,
`<workspace>/memory/new-zealand/`, or `~/new-zealand/`. Before reading or
writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/new-zealand/`, `<workspace>/memory/new-zealand/`, `~/new-zealand/`.
3. If several candidate directories exist, use only the highest-precedence one and
   report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create
   `<workspace>/new-zealand/` by default.
5. If the host cannot supply `<workspace>`, read an existing `~/new-zealand/`
   only; otherwise ask for a state root before creating data.
6. If older data exists only under `~/Clawic/data/new-zealand/` or
   `~/clawic/new-zealand/`, move it into the resolved `<state_root>/` after the
   user confirms, and say in one line that you moved it and from where.

Use the selected `<state_root>` for every state operation in this skill.
Create or update `<state_root>/memory.md` only when the user wants planning
context kept across sessions. Template: `assets/data-templates.md`.

```text
<state_root>/
└── memory.md     # Trip context, bases, constraints
```

Host-shared memory such as workspace `MEMORY.md` is outside `<state_root>` and
needs separate user consent. Do not store passport numbers, booking
confirmation secrets, or payment details in skill state.

## When to use

Load for **New Zealand** trip or local-insight questions:

- which island or corridor to prioritize for the available days
- bases for Auckland, Wellington, Rotorua/Taupo, Queenstown, Christchurch,
  Nelson/Abel Tasman, or Fiordland/Southland
- driving pace, ferries, domestic flights, and weather buffers
- Great Walks / hut booking timing, beach and wildlife safety
- food, wine regions, family pacing, and seasonal trade-offs

Prefer progressive disclosure: answer from this file and `references/domain.md`
first, then open only the topic files needed. Hand off when a sibling owns the
remaining job:

| Job | Skill |
|-----|-------|
| Multi-country trip systems | `travel` |
| Reservation completion after a base is chosen | `booking` |
| Vehicle pickup / insurance handoff detail | `car-rental` |
| Cuisine logging beyond NZ regional guidance | `food` |
| Booking-language clarity | `english` |

## Critical verification path

Before stating a **visa/NZeTA rule, biosecurity declaration list, DOC hut fee,
ferry timetable, toll rule, or emergency number nuance** as current fact:

1. Open `references/sources.md` for the canonical URL.
2. Re-check the live official page for that traveler type and date.
3. If the live page cannot be opened, say the claim is unverified and give the
   URL to check — do not invent a fee, booking window, or border rule.

Orientation ranges in this package are for routing only.

## Core path

1. Ask for **month**, **full days on the ground**, **island focus**, and
   **transport mode** before locking a route.
2. Prefer **one island or one corridor** for short trips; reject both-islands
   fantasies that erase driving reality.
3. Load `references/domain.md` for traps, then one leaf file for the active
   region or topic.
4. Add buffer before ferries, alpine days, Milford-type outings, and long drives
   after long-haul arrival.
5. Respect stored preferences in `<state_root>/memory.md` when present.

## Quick Reference

| Topic | File |
|-------|------|
| **General Domain Rules** | `references/domain.md` |
| **Official sources** | `references/sources.md` |
| **First-use / memory** | `references/setup.md`, `assets/data-templates.md` |
| **Major Hubs and Regions** | |
| Auckland complete guide | `references/auckland.md` |
| Wellington complete guide | `references/wellington.md` |
| Rotorua and Taupo complete guide | `references/rotorua-taupo.md` |
| Queenstown complete guide | `references/queenstown.md` |
| Christchurch complete guide | `references/christchurch.md` |
| Nelson, Abel Tasman, and Marlborough | `references/nelson-marlborough.md` |
| Fiordland and Southland playbook | `references/fiordland-southland.md` |
| **Planning** | |
| Core itineraries | `references/itineraries.md` |
| Island and region differences | `references/regions.md` |
| Where to stay by style | `references/accommodation.md` |
| Entry and biosecurity planning | `references/entry-and-biosecurity.md` |
| Useful apps | `references/apps.md` |
| **Food and Drink** | |
| Regional dishes and restaurant strategy | `references/food-guide.md` |
| Wine regions and tasting logic | `references/wine.md` |
| **Experiences** | |
| Signature experiences | `references/experiences.md` |
| Beaches and coastal planning | `references/beaches.md` |
| Hikes and track safety | `references/hiking.md` |
| Nightlife by city type | `references/nightlife.md` |
| **Reference** | |
| Culture, etiquette, expectations | `references/culture.md` |
| Seasonality and climate strategy | `references/seasonality.md` |
| Traveling with children | `references/with-kids.md` |
| Wildlife and outdoor safety | `references/wildlife-safety.md` |
| **Practical** | |
| Flights, ferries, trains, and driving | `references/transport.md` |
| Phone and internet | `references/telecoms.md` |
| Payments and cost planning | `references/payment-and-costs.md` |
| Emergencies and safety | `references/emergencies.md` |

## Security & Privacy

**Data that stays local:** optional trip preferences in `<state_root>/`.

**This skill does NOT:** access files outside the resolved `<state_root>/`,
scrape booking portals, or invent live visa/biosecurity/fee facts when official
pages are unavailable.
