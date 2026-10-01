---
name: amsterdam
description: >
  Assist with Amsterdam travel, relocation, work, study, or local life by routing
  to neighborhood, transport, housing, visa orientation, cost, and lifestyle guides.
  Use for visitor itineraries, moving/settling checklists, tech-career orientation,
  cycling and GVB transit, or 30% ruling / HSM overview. Not for filing a visa,
  booking non-refundable travel, or stating a nationality-specific entry rule without
  re-checking the official IND/Iamsterdam page for that passport and date.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🚲"}'
  related-skills: '{"travel":"Multi-country or Europe-wide itinerary framing when Amsterdam is only one stop.","booking":"Reservation hygiene for hotels, flights, and tickets after the Amsterdam plan is set.","food":"Broader meal planning beyond Amsterdam food area notes.","dutch":"Language support for menus, gemeente forms, and daily phrases.","cycling":"General bike-fit and ride craft beyond Amsterdam street norms.","europe":"Schengen / multi-city Europe routing when the trip is not Amsterdam-centric.","housing":"Cross-city housing search process when Amsterdam is one candidate market.","flight":"Flight shopping and buffer planning into AMS.","expat":"General expat settling patterns that are not Amsterdam-specific."}'
---

## State location

Amsterdam planning or move context may exist in `<workspace>/amsterdam/`, `<workspace>/memory/amsterdam/`, or `~/amsterdam/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/amsterdam/`, `<workspace>/memory/amsterdam/`, `~/amsterdam/`.
3. If none exists and the user wants planning context kept, create `<workspace>/amsterdam/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/amsterdam/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/memory.md` only when the user wants trip or move context kept across sessions. Legacy `~/Clawic/data/amsterdam/` is a migration source only. Keep it out of the active lookup order, and move it only when the user asks.

This skill is primarily **routing knowledge**. Durable notes are optional; do not invent a CRM or booking ledger unless the user asks to keep state.

## When to load

Load for Amsterdam **visitor**, **relocation**, **work/study**, or **local-life** questions:

- 1/3/7-day itineraries, attractions, lodging zones, day trips
- neighborhood fit (Centrum, De Pijp, Jordaan, Oud-West, Noord, IJburg, suburbs)
- bikes, GVB, NS, why not to rent a car in the core
- cost of living, housing market reality, settling checklist (BSN, DigiD, huisarts)
- tech salaries orientation, startups, Highly Skilled Migrant / 30% ruling overview
- safety, coffeeshop rules, canal and bike-theft basics

Route away when the task is mainly:

- multi-country Europe trip design → `travel` / `europe`
- hotel/flight booking ops → `booking` / `flight`
- Dutch language learning → `dutch`
- generic housing search outside Amsterdam → `housing`
- live visa filing for a specific passport → open live IND pages + tell the user to confirm; do not invent thresholds from memory

Read `references/sources.md` before repeating salary bands, rent medians, IND salary thresholds, OV fares, or emergency numbers. Re-check the official page before the user books non-refundable travel or relies on a visa number.

## When to load references

Load the smallest reference that matches the current need; keep this file as the entry point.

| Need | File |
|------|------|
| Verified source URLs (Gate 6) | `references/sources.md` |
| Attractions | `references/visitor-attractions.md` |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` |
| Where to stay | `references/visitor-lodging.md` |
| Tips & day trips | `references/visitor-tips.md` |
| Neighborhood comparison | `references/neighborhoods-index.md` |
| Centrum / Jordaan / De Wallen | `references/neighborhoods-centrum.md` |
| De Pijp / Oud-Zuid / Rivierenbuurt | `references/neighborhoods-south.md` |
| Oud-West / Westerpark / Bos en Lommer | `references/neighborhoods-west.md` |
| Noord / Oost / IJburg | `references/neighborhoods-east-north.md` |
| Amstelveen / Buitenveldert / Zuidoost | `references/neighborhoods-suburban.md` |
| Choosing a neighborhood | `references/neighborhoods-choosing.md` |
| Food overview | `references/food-overview.md` |
| Dutch cuisine | `references/food-local.md` |
| International dining | `references/food-international.md` |
| Dining areas | `references/food-areas.md` |
| Dietary & practical food | `references/food-practical.md` |
| Moving & settling | `references/resident.md` |
| Transport | `references/transport.md` |
| Cycling norms | `references/cycling.md` |
| Cost of living | `references/cost.md` |
| Safety & laws | `references/safety.md` |
| Weather & climate | `references/climate.md` |
| Local services | `references/local.md` |
| Tech industry | `references/tech.md` |
| Business setup | `references/business.md` |
| Visas & 30% ruling | `references/visas.md` |
| Startups | `references/startup.md` |
| Culture | `references/culture.md` |
| Healthcare | `references/healthcare.md` |
| Education | `references/education.md` |
| Expat life | `references/lifestyle.md` |

## Operating rules

1. **Ask for constraints early**: passport/nationality (for entry), dates or season, budget band, solo/couple/family, bike comfort, and whether the goal is visit vs move.
2. **Prefer bikes + GVB over cars** inside the urban core; explain parking cost and one-way maze only when the user insists on driving.
3. **Housing honesty**: free-sector rent is competitive; do not promise social-housing speed. Separate visitor lodging from resident leases.
4. **Legal caution**: cannabis is a regulated coffeeshop model, not a free-for-all; public smoking and street dealing remain risk. Quote emergency **112**.
5. **Money**: quote ranges as orientation with the date/source caveat; net salary depends on 30% ruling, household, and tax year.
6. **Language**: English is widely usable in tech and tourism; still point to `dutch` for gemeente/long-stay friction.
7. **No secrets or bookings**: never store passport numbers, BSN, or payment data in skill files. Booking confirmations belong in user-controlled state only if requested.

## Safety boundaries

- Not a substitute for IND, gemeente, employer immigration counsel, or a licensed advisor.
- Do not invent current HSM salary thresholds, tourist-tax rates, or museum ticket prices from memory—open `references/sources.md` and the live page.
- Do not encourage illegal substance purchase outside licensed channels or unsafe canal behavior.
- Treat user-provided addresses and employer details as private.
