---
name: bali
description: >
  Choose a Bali base and operating plan for a trip, relocation, remote stay,
  study, family move, or business setup. Use for neighborhoods, visas, costs,
  housing, food, transport, climate, healthcare, schools, and local practicalities.
  Not for booking flights, filing a visa, or giving nationality-specific legal
  advice without an official source check.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌴"}'
  related-skills: '{"expat":"Plan the broader move, settling, and adaptation around a Bali base.","travel":"Build a general itinerary when Bali is only one stop.","food":"Deepen cuisine, dietary, or restaurant planning beyond Bali area defaults.","startup":"Founder legal vehicle, fundraising, and go-to-market beyond Bali base selection."}'
---

## State location

Bali state may exist in `<workspace>/bali/`, `<workspace>/memory/bali/`, or `~/bali/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/bali/`, `<workspace>/memory/bali/`, `~/bali/`.
3. If none exists and state must be created, default to `<workspace>/bali/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Do not merge them.
5. If `<workspace>` cannot be resolved, read an existing `~/bali/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/memory.md` only when the user wants planning context kept across sessions.

## When to load

Load this skill for a Bali trip, relocation, remote stay, study, family move, or business setup. Identify purpose, nationality, dates, and budget before naming a base.

Read `references/sources.md` before repeating a visa duration, fee, housing range, levy amount, or legal rule. Re-check the official page for that nationality and travel date before the user books flights, signs a lease, or pays a visa fee.

| Need | File |
| --- | --- |
| Empty state or first setup | `assets/memory-template.md` |
| Domain rules, traps, legal boundary | `references/domain.md` |
| Research links and official portals | `references/sources.md` |
| Neighborhood comparison or base choice | `references/neighborhoods-index.md`, `references/neighborhoods-choosing.md` |
| One area | `references/neighborhoods-canggu.md`, `references/neighborhoods-seminyak.md`, `references/neighborhoods-ubud.md`, `references/neighborhoods-south.md` |
| Visa, levy, stay compliance | `references/visas.md` |
| Housing and monthly cost | `references/cost.md`, `references/resident.md`, `references/tech.md` |
| Food | `references/food-overview.md`, then the matching `references/food-*.md` |
| Transport, climate, safety, healthcare | `references/transport.md`, `references/climate.md`, `references/safety.md`, `references/healthcare.md` |
| Culture, lifestyle, local admin, driving | `references/culture.md`, `references/lifestyle.md`, `references/local.md`, `references/driving.md` |
| Schools, business, startup ecosystem | `references/education.md`, `references/business.md`, `references/startup.md` |
| Visitor route, lodging, attractions | matching `references/visitor-*.md` |
| Persisted trip context | `assets/memory-template.md` |

## Core rules

1. Split the request into trip, relocation, remote work, study, family move, or business before recommending places.
2. Treat Canggu, Seminyak, Ubud, Sanur, Nusa Dua, Jimbaran, and Uluwatu as different markets. Load the area file before answering housing, work, or schooling questions.
3. Stay permission is not work permission. Do not treat Visa on Arrival / B1 tourism entry as a default remote-work or local-business answer. Quote durations and fees only from the official page checked for this answer.
4. Bali tourist levy is separate from visa cost. If the levy or immigration page was not opened, say what to re-check and stop short of a booking recommendation.
5. Give prices as dated IDR ranges. Local warung food and simple housing can be low-cost; imported goods, premium villas, private drivers, and international schools are not.
6. Treat wet-season rain, flooding, mold, and Nyepi island-wide restrictions as operational constraints, not footnotes.
7. Prefer licensed transport at night. Scooter plans need IDP/helmet/insurance realism; do not push scooters on users uncomfortable with chaotic traffic or wet roads.
8. For drugs, overstay, visa misuse, and temple etiquette, give the current legal or cultural boundary and the official or local-authority source. Do not rely on forum hearsay.

## Bali-specific traps

- Choosing one base for the whole island.
- Treating VOA/B1 as an indefinite stay path.
- Missing the separate Bali tourist levy.
- Signing a long lease before testing commute, flood exposure, noise, and internet.
- Running business or local work activity on tourist status without compliance checks.
- Using a stale housing number as a fixed budget.
- Ignoring Nyepi, ceremony traffic, or peak-season availability when pricing transport or lodging.

## Security and privacy

Keep planning context in the selected `<state_root>` only. Do not read or write outside that directory for this skill. Do not send passport, visa, or payment details to a third party from this skill.
