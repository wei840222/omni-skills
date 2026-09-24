---
name: shanghai
description: >
  Plan a Shanghai trip, relocation, study stay, remote base, or business setup.
  Use for neighborhoods, metro and DiDi, costs, food, climate, visas, residence
  registration, and local apps. Not for booking travel, filing a visa, or giving
  nationality-specific legal advice without an official source check.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌆"}'
  related-skills: '{"booking":"Handle hotel, transport, and activity reservations after the Shanghai plan is chosen.","chinese":"Support daily Mandarin tasks and local communication.","expat":"Plan the broader move and settling around a Shanghai base.","travel":"Build a multi-city route when Shanghai is only one stop."}'
---

## State location

Shanghai planning state may exist in `<workspace>/shanghai/`, `<workspace>/memory/shanghai/`, or `~/shanghai/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/shanghai/`, `<workspace>/memory/shanghai/`, `~/shanghai/`.
3. If none exists and state must be created, default to `<workspace>/shanghai/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Do not merge them.
5. If `<workspace>` cannot be resolved, read an existing `~/shanghai/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/memory.md` only when the user wants planning context kept across sessions.

## When to load

Load this skill for a Shanghai visit, relocation, study stay, remote base, or business setup. Identify purpose, nationality, dates, and budget before naming a neighborhood.

Read `references/sources.md` before repeating a visa duration, registration deadline, fee, rent, or legal rule. Re-check the official page for that nationality and travel date before the user books flights, signs a lease, or pays a visa fee.

| Need | File |
| --- | --- |
| Empty state or first setup | `references/resident.md` |
| Neighborhood comparison or choice | `references/neighborhoods-index.md`, `references/neighborhoods-choosing.md` |
| One area | the matching `references/neighborhoods-*.md` |
| Visa, work permit, registration | `references/visas.md` |
| Housing and monthly cost | `references/cost.md`, `references/resident.md` |
| Food | `references/food-overview.md`, then the matching `references/food-*.md` |
| Transport, climate, safety, healthcare, apps | `references/transport.md`, `references/climate.md`, `references/safety.md`, `references/healthcare.md`, `references/local.md` |
| Culture, schools, driving, tech, business, startup | the matching file under `references/` |
| Visitor route, lodging, attractions | the matching `references/visitor-*.md` |
| Official sources and dated ranges | `references/sources.md` |

## Core rules

1. Split the request into trip, relocation, study, remote work, or business before recommending places.
2. Treat Puxi and Pudong, and core versus outer districts, as different commute markets. Load the neighborhood file before answering housing or schooling questions.
3. A visa-free or tourist entry is not work permission. Quote stay length only from the official page checked for this nationality. British citizens currently have a 30-day visa-free window through 31 December 2026 for tourism, business visits, family or friend visits, or transit; paid work, journalism, study, and stays over 30 days need a visa first.
4. Register the place of stay with the local Public Security Bureau within 24 hours of arrival, and again after an address change. A hotel usually does this at check-in. A private stay does not.
5. Give prices as dated ranges from `references/sources.md` and `references/cost.md`. Do not present a February 2026 rent or salary figure as a current quote.
6. Metro plus a licensed ride-hail covers most days. Peak river crossings and Line 2 crowding are planning constraints, not footnotes.
7. WeChat and Alipay are the default payment and transit path. Set them up, plus a connectivity plan for blocked services, before arrival.
8. For drugs, drones, filming, demonstrations, and political speech, give the current legal boundary and the official source. Possession of illegal drugs, including cannabis, can lead to long sentences or the death penalty.

## Shanghai-specific traps

- Treating every district as equally walkable or English-friendly.
- Booking a cross-river commute from an off-peak listing photo.
- Arriving without a working payment app.
- Treating visa-free or business-visit entry as permission to work.
- Missing the 24-hour residence registration after a private stay or a move.
- Signing a lease before testing the peak-hour commute and summer humidity.
- Using a stale rent or school-fee number as a fixed budget.

## Security and privacy

Keep planning context in the selected `<state_root>` only. Do not read or write outside that directory for this skill. Do not send passport, visa, or payment details to a third party from this skill.
