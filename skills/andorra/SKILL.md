---
name: andorra
description: >
  Plan Andorra trips with parish-level bases for skiing, hiking, shopping,
  wellness, and cross-border logistics. Use when choosing Andorra la Vella vs
  Escaldes vs Canillo/Ordino, winter ski transfers, spa weekends, roaming outside
  the EU, or Barcelona/Toulouse arrival routes. Not for multi-country trip systems
  (`travel`), deep cuisine workflows (`food`), or Catalan/French language production
  (`catalan` / `french`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇦🇩"}'
  related-skills: '{"travel":"Multi-country itineraries and general travel memory beyond Andorra-only parish routing.","food":"Deeper cuisine workflows beyond Andorran food pointers.","catalan":"Catalan language production and register rather than Andorra logistics.","french":"French writing and register for border-side service context."}'
---

# Andorra

Parish-aware trip planning for a tiny mountain country: base choice beats brochure scenery, winter and summer behave differently, and roaming / border / parking realities matter more than slogans.

## State location

Resolve `<state_root>` before any preference read/write:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory:
   `<workspace>/andorra/`,
   `<workspace>/memory/andorra/`,
   `~/andorra/`.
3. If none exist and the user asked to persist data, create
   `<workspace>/andorra/`.

| Path | Required? | Role |
|------|-----------|------|
| `<state_root>/memory.md` | optional | Trip style, season, base preferences, history |

Do not treat the literal string `<state_root>` as a filesystem path. Skill resources stay under `references/` and `assets/`. Host-shared memory such as workspace `MEMORY.md` is outside `<state_root>` and needs separate consent.

Template: `assets/memory-template.md`.

## Setup

If `<state_root>` is missing or empty, read `references/setup.md` and start naturally. Ask season, trip style, arrival city, car vs bus, nights, and group before locking a parish base.

## When to load

Load when the user is planning an **Andorra** trip or needs local logistics:

- which parish to sleep in for ski, hike, spa, shopping, or family trips
- Grandvalira / Pal Arinsal access vs capital convenience
- Barcelona / Toulouse arrivals, buses, driving, parking, border queues
- duty-free shopping tactics and customs reality re-entering Spain/France
- roaming outside the EU, eSIM, offline maps
- Caldea / wellness days and bad-weather backups

Route away when the ask is mainly:

- multi-country routing systems → `travel`
- restaurant technique or deep cuisine systems → `food`
- Catalan or French writing/production → `catalan` / `french`

## Quick reference

| Need | Load |
|------|------|
| Core rules, traps, security | `references/rules.md` |
| 7 parishes at a glance | `references/regions.md` |
| Capital logistics | `references/andorra-la-vella.md` |
| Spa + central comfort | `references/escaldes-engordany.md` |
| Grandvalira / family snow | `references/canillo.md` |
| Quieter mountain base | `references/ordino.md` |
| Sample season plans | `references/itineraries.md` |
| Stay by style/budget | `references/accommodation.md` |
| Apps and booking tools | `references/apps.md` |
| Food pointers | `references/food-guide.md` |
| Wine reality check | `references/wine.md` |
| Bookable experiences | `references/experiences.md` |
| Hiking timing/safety | `references/hiking.md` |
| Spas / rainy-day reset | `references/wellness.md` |
| Nightlife / après-ski | `references/nightlife.md` |
| Shopping + customs | `references/shopping.md` |
| Culture / etiquette | `references/culture.md` |
| Traveling with kids | `references/with-kids.md` |
| Arrivals, buses, driving | `references/transport.md` |
| Roaming / eSIM / Wi-Fi | `references/telecoms.md` |
| Emergency numbers | `references/emergencies.md` |
| Official source anchors | `references/sources.md` |
| Preference file shape | `assets/memory-template.md` |

## Core rules

1. **Specific over scenic.** Name parish, lift area, avenue, or transfer—not “great mountains.”
2. **Base matches trip style.** Capital/Escaldes for shopping+spa short stays; Canillo/Encamp for Grandvalira; Ordino/La Massana for quieter mountain; Sant Julià for southern access/Naturland.
3. **Timing changes everything.** Winter weekends = border traffic + packed parking; summer = hikes/bike/lakes; shoulder seasons need mixed openings.
4. **Call out real constraints.** No train in; EU roaming often fails; snow chains/tires may matter; mountain plans need weather backup.
5. **Shopping is a tactic.** Guide by category; compare electronics; customs allowances still apply when re-entering Spain/France.
6. **Match the traveler** using the matrix in `references/rules.md`.
7. **Persist only with consent.** Preferences go under `<state_root>/memory.md` after the user agrees.

## Security and privacy

- Trip preferences stay local under `<state_root>` after consent.
- This skill does **not** make network requests, scrape live weather/traffic, or access files outside `<state_root>` and skill resources.
- For live road/snow/weather status, point the user to official sources in `references/sources.md` and apps in `references/apps.md`—do not invent live conditions.
- Never store payment cards, passport scans, or booking passwords in skill state.

## Common traps

| Trap | Prevention |
|------|------------|
| Assume EU roaming covers Andorra | Warn pre-border; eSIM / offline maps (`references/telecoms.md`) |
| Sleep in capital for ski-first trip | Prefer Canillo/Encamp/slope corridor (`references/rules.md`) |
| Winter drive without chains/tires check | Flag road reality (`references/transport.md`) |
| Treat “duty free” as always cheaper | Compare by category + customs (`references/shopping.md`) |
| One rigid mountain plan | Always give indoor/spa/town backup |
| Day-trip only mindset | Note early/late windows that need an overnight base |

## Default first answer shape

1. Confirm season + trip style + car/bus + nights.
2. Recommend **one primary parish base** and one fallback.
3. Give the main daily transfer or walk pattern.
4. Name 1–2 book-ahead items (spa, ski pass, weekend hotel).
5. State roaming/border/parking caveat that fits the plan.
6. Offer to save preferences under `<state_root>` only if useful.
