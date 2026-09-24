---
name: thailand
description: >
  Choose a Thailand base and operating plan for a trip, relocation, remote
  stay, study, retirement, or business setup. Use for regions, visas, costs,
  housing, food, transport, climate, healthcare, and local practicalities.
  Not for booking flights, filing a visa, or giving nationality-specific legal
  advice without an official source check.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇹🇭"}'
  related-skills: '{"expat":"Plan the broader move, settling, and adaptation around a Thailand base.","travel":"Build a general itinerary when Thailand is only one stop.","travel-planning":"Track a multi-region Thailand route, buffers, and reservations."}'
---

## State location

Thailand state may exist in `<workspace>/thailand/`, `<workspace>/memory/thailand/`, or `~/thailand/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/thailand/`, `<workspace>/memory/thailand/`, `~/thailand/`.
3. If none exists and state must be created, default to `<workspace>/thailand/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Do not merge them.
5. If `<workspace>` cannot be resolved, read an existing `~/thailand/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/memory.md` only when the user wants planning context kept across sessions.

## When to load

Load this skill for a Thailand trip, relocation, remote stay, study, retirement, or business setup. Identify purpose, nationality, dates, and budget before naming a base.

Read `references/sources.md` before repeating a visa duration, fee, housing range, or legal rule. Re-check the official page for that nationality and travel date before the user books flights, signs a lease, or pays a visa fee.

| Need | File |
| --- | --- |
| Empty state or first setup | `references/setup.md` |
| Region comparison or base choice | `references/regions-index.md`, `references/regions-choosing.md` |
| One region | `references/regions-bangkok.md`, `references/regions-chiang-mai.md`, `references/regions-phuket.md`, `references/regions-islands.md`, `references/regions-north.md` |
| Visa, TDAC, work boundary | `references/visas.md` |
| Housing and monthly cost | `references/cost.md`, `references/resident.md`, `references/nomad.md` |
| Food | `references/food-overview.md`, then the matching `references/food-*.md` |
| Transport, climate, safety, healthcare | `references/transport.md`, `references/climate.md`, `references/safety.md`, `references/healthcare.md` |
| Culture, language, nightlife, tech, teaching, business | the matching file under `references/` |
| Visitor route, lodging, attractions | the matching `references/visitor-*.md` |
| Persisted trip context | `assets/memory-template.md` |

## Core rules

1. Split the request into trip, relocation, remote work, study, retirement, or business before recommending places.
2. Treat Bangkok, Chiang Mai, Phuket, the islands, and secondary provinces as different markets. Load the region file before answering housing, work, or schooling questions.
3. Stay permission is not work permission. A visa-exempt entry is tourism-only. Do not treat a Destination Thailand Visa (DTV) as a default remote-work answer unless the current official pathway matches the user's nationality and activity.
4. Quote visa durations, fees, and reporting rules only from the official page checked for this answer. If that page was not opened, say what to re-check and stop short of a booking recommendation.
5. Give prices as dated ranges. Local food and simple housing can be low-cost; imported goods, premium areas, and international schools are not.
6. Keep a buffer day for island ferries in the rainy season, and treat northern smoke season as a primary constraint rather than a weather footnote.
7. Prefer BTS/MRT proximity in Bangkok, weather-aware ferry buffers on islands, and licensed transport at night. Do not recommend an unregistered scooter plan.
8. For monarchy-related speech, cannabis, and controlled substances, give the current legal boundary and the official source. Do not rely on an older liberalization headline.

## Thailand-specific traps

- Choosing one base for the whole country.
- Booking a same-day international connection after an island ferry.
- Signing an annual lease before testing commute, flood exposure, and noise.
- Running business activity on tourist or visa-exempt status.
- Using a stale housing number as a fixed budget.
- Ignoring a Thai holiday when pricing transport or tours.

## Security and privacy

Keep planning context in the selected `<state_root>` only. Do not read or write outside that directory for this skill. Do not send passport, visa, or payment details to a third party from this skill.
