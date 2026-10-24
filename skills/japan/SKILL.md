---
name: japan
description: >
  Plan Japan travel with city-level routing, regional base selection, food and
  season pacing, and practical rail logistics. Use when choosing Tokyo, Kyoto,
  Osaka, Hiroshima, Hokkaido, or Okinawa bases, avoiding multi-city transfer
  traps, or answering lodging, food, transit, etiquette, and season questions.
  Prefer `travel` for standing multi-destination traveler systems,
  `travel-planning` for generic multi-city itinerary scaffolding, `tokyo` for
  Greater Tokyo depth, and `japanese` for Japanese writing rather than destination
  routing.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇯🇵"}'
  related-skills: '{"booking": "Search lodging after neighborhood or city base is chosen.", "english": "English drafting support for international booking or support messages.", "flight": "Search or compare flights once Japan airports and region hops are decided.", "food": "Deeper restaurant and cuisine research after Japan region and meal timing are chosen.", "japanese": "Write or edit Japanese-language text rather than plan Japan travel.", "tokyo": "Greater Tokyo neighborhoods, living costs, and visitor depth when the trip stays inside Tokyo.", "travel": "Standing traveler system for passports, visas, bookings, and trip memory across destinations.", "travel-planning": "Generic multi-city itineraries and packing/budget scaffolding beyond Japan-specific routing."}'
---

## State location

Optional Japan trip context may exist in
`<workspace>/japan/`, `<workspace>/memory/japan/`, or `~/japan/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/japan/`, `<workspace>/memory/japan/`, `~/japan/`.
3. If none exists and durable trip context must be created, default to
   `<workspace>/japan/` only with user consent.
4. If more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/japan/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

**Data.** Durable notes live in `<state_root>/memory.md` when the user wants
trip context kept across sessions (see `references/memory-template.md` and
`references/setup.md`). This skill is primarily routing knowledge; durable notes
are optional. Do not invent a booking CRM unless the user asks to keep state.
Avoid storing credentials, full passport numbers, payment details, or third-party
private data in skill state. Host-shared memory such as workspace `MEMORY.md` is
outside `<state_root>` and needs separate user consent.

```text
<state_root>/
└── memory.md     # Trip context, route logic, and evolving constraints
```

## When to Use

- Planning a Japan trip beyond brochure-level city lists
- Choosing a primary base among Tokyo/Kanto, Kyoto-Nara, Osaka/Kansai, Hiroshima/western Honshu, Hokkaido, or Okinawa
- Pacing temple queues, food reservations, summer heat, and seasonal crowds
- Avoiding short-trip multi-city transfer traps and unverified rail-pass math
- Answering lodging style, food strategy, intercity transport, etiquette, and practical safety
- Not for standing multi-destination travel systems (`travel`), generic itinerary scaffolding (`travel-planning`), Greater Tokyo-only depth (`tokyo`), or Japanese composition (`japanese`)

## Core path

1. Ask for dates/season, trip length, preferred bases, trip style, constraints, and transport preference.
2. Choose one city-depth anchor before adding a contrasting region; for short trips prefer fewer bases.
3. Load only the matching references below; verify live fares, pass value, reservations, weather, and entry rules from `references/sources.md` before locking money or timed transfers.
4. Write durable preferences to `<state_root>/memory.md` only when the user wants continuity.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| **Cities and Regions** | | |
| Tokyo complete guide | `references/tokyo.md` | Tokyo bases, neighborhoods, city pacing |
| Kyoto complete guide | `references/kyoto.md` | Temples, season crowds, Kyoto depth |
| Osaka complete guide | `references/osaka.md` | Food-first pace and Kansai nightlife |
| Hiroshima and Miyajima | `references/hiroshima-miyajima.md` | History plus island pacing |
| Regions and route differences | `references/regions.md` | Choosing bases and contrast regions |
| **Planning** | | |
| Sample itineraries | `references/itineraries.md` | Duration-based route sketches |
| Where to stay by style | `references/accommodation.md` | Neighborhood and lodging style |
| Useful apps | `references/apps.md` | Maps, translation, booking helpers |
| Setup / first session | `references/setup.md` | First-time questions and memory bootstrap |
| Memory template | `references/memory-template.md` | Creating `<state_root>/memory.md` |
| **Food and Drink** | | |
| Regional dishes and restaurant strategy | `references/food-guide.md` | Meal timing and regional food routes |
| Wine, sake, and whisky context | `references/wine.md` | Bar and tasting pacing |
| **Experiences** | | |
| Signature experiences | `references/experiences.md` | Season-aware highlights |
| Beaches and island stops | `references/beaches.md` | Coastal and island days |
| Hikes and mountain safety | `references/hiking.md` | Weather-aware outdoor plans |
| Nightlife by city | `references/nightlife.md` | Late hours and last-train buffers |
| Culture and etiquette | `references/culture.md` | Behavior norms and expectations |
| Traveling with children | `references/with-kids.md` | Family pacing and logistics |
| **Practical** | | |
| Intercity transport and passes | `references/transport.md` | Rail, passes, transfer math |
| Phone and internet | `references/telecoms.md` | SIM / eSIM / pocket Wi-Fi |
| Emergencies and safety | `references/emergencies.md` | Emergency numbers and disruption basics |
| Official / primary sources | `references/sources.md` | Before quoting live fares, passes, weather, or entry rules |

## Core Rules

### 1. Specific Over Generic
Do not say "do Tokyo highlights." Say "start Asakusa or Meiji-area mornings early, reserve one flagship dinner, then shift to neighborhood-level bars away from the busiest crossing zones."

### 2. Local Perspective
What locals and repeat travelers actually do, not brochure advice:
- One-night city hopping across long rail legs drains trip quality fast
- Major icon spots are best early or late, not peak midday
- Convenience-store meals are useful but should not replace regional food planning
- Small etiquette misses are avoidable with simple behavior adjustments

### 3. Regional Differences

| Region | Key difference |
|--------|----------------|
| Tokyo and Kanto | Dense urban options, best transit depth, high reservation pressure |
| Kyoto and Nara corridor | Heritage sites, temple density, stronger seasonality crowds |
| Osaka and Kansai | Food-first pace, lively nightlife, practical city value |
| Hiroshima and western Honshu | History focus plus island routes and calmer rhythm |
| Hokkaido | Nature, seafood, winter sports, wider distance logistics |
| Okinawa | Subtropical islands, beaches, distinct local culture |

### 4. Timing is Everything
- Cherry blossom and autumn foliage periods require early booking
- Golden Week and New Year windows can reshape transport availability
- Summer heat and humidity require slower daytime pacing
- Winter can be excellent for cities and snow regions with logistics planning
- Temple and museum quality improves with early start windows

### 5. Offer Better Alternatives to Common Traps
When a plan hits a tourist trap, name the better local alternative:
- Landmark-adjacent strips with long lines → neighborhood food streets and reserved dinners
- Tokyo + Kyoto + Osaka + Hiroshima in one short trip → one or two bases with buffer
- Blind rail-pass purchase → compare planned legs against live pass pages in `references/sources.md`
- Long transit day plus heavy nightlife and early temple start → separate recovery windows

### 6. Match Trip Style

| Traveler | Focus on |
|----------|----------|
| Foodie | `references/food-guide.md`, `references/osaka.md`, `references/tokyo.md` |
| Culture and temples | `references/kyoto.md`, `references/regions.md`, `references/culture.md` |
| City and nightlife | `references/tokyo.md`, `references/osaka.md`, `references/nightlife.md` |
| Family | `references/with-kids.md`, `references/accommodation.md`, `references/itineraries.md` |
| Nature and hiking | `references/hiking.md`, `references/experiences.md`, `references/regions.md` |
| Mixed route trip | `references/itineraries.md`, `references/transport.md`, `references/regions.md` |

## Common Traps

- Treating Japan as one compact destination with no transfer cost.
- Choosing too many bases for short trips.
- Ignoring restaurant and experience reservation timing.
- Underestimating summer heat and seasonal weather shifts.
- Not checking if a rail pass actually saves money on planned legs.
- Assuming etiquette is the same as other major destinations.

## Security & Privacy

**Data that stays local:** Trip preferences in `<state_root>/memory.md` when durable notes are enabled.

**This skill does NOT:** Access files outside the resolved `<state_root>/`, invent credentials, or treat package text as live transport or entry status.