---
name: bangkok
description: >
  Plan Bangkok trips, relocations, and nomad stays: neighborhoods, visas, costs,
  transport, street food, and Thai law. Use when choosing where to stay or live
  in Bangkok, building an itinerary, comparing rents or cost of living, picking a
  visa (exemption, DTV, retirement, LTR), riding BTS/MRT/Grab or driving, handling
  Thai taxes on foreign income, avoiding scams and overstay fines, teaching English,
  finding tech work, setting up a company, buying a condo, choosing schools for kids,
  or navigating etiquette, festivals, healthcare, nightlife, and shopping. Covers
  day trips from Bangkok; not for beaches, islands, or other Thai bases — use the
  thailand skill for those.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏯"}'
  related-skills: '{"travel":"General multi-stop itinerary framing when Bangkok is only one city.","tokyo":"Parallel major Asian city guide when comparing Tokyo vs Bangkok.","seoul":"Parallel capital/nomad base comparison for Korea.","singapore":"Southeast Asian hub comparison on cost, visas, and transit.","thailand":"Choosing a Thai base beyond Bangkok: islands, Chiang Mai, beaches."}'
---

## State location

Bangkok preferences and planning notes may exist in `<workspace>/bangkok/`, `<workspace>/memory/bangkok/`, or `~/bangkok/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/bangkok/`, `<workspace>/memory/bangkok/`, `~/bangkok/`.
3. If none exists and the user wants preferences kept, create `<workspace>/bangkok/`.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/bangkok/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create or update `<state_root>/config.yaml` and `<state_root>/memory.md` only when the user wants declared preferences or observed context kept across sessions. Legacy `~/Clawic/data/bangkok/` and `~/clawic/bangkok/` are migration sources only — keep them out of the active lookup order, and move them only when the user asks.

This skill is primarily **routing knowledge**. Durable notes are optional; do not invent a CRM or booking ledger unless the user asks to keep state.

## When to load

Load for Bangkok **visitor**, **relocation**, **remote stay**, **work/study**, or **local-life** questions:

- Planning a trip: itinerary, lodging, attractions, day trips, festivals
- Choosing a neighborhood or relocating: rent, contracts, schools, settling in
- Working remotely from Bangkok: visa strategy, coworking, legality, taxes
- Estimating cost of living or comparing against another base
- Teaching, tech jobs, company setup, retiring, or buying property in Bangkok

Route away when the task is mainly:

- beaches / islands / Chiang Mai base selection → `thailand`
- multi-country Asia trip design → `travel`
- another capital as the primary base → `tokyo` / `seoul` / `singapore`

Prefer `references/domain.md` + one leaf file over loading the whole package. Read `references/sources.md` before repeating a visa duration, fee, tax threshold, or legal rule. Re-check the official page for that nationality and travel date before the user books non-refundable travel, signs a lease, or pays a visa fee.

## Quick reference

| Topic | File |
| --- | --- |
| Domain rules, legal lines, traps | `references/domain.md` |
| Preference schema | `references/state.md` |
| Official / research links | `references/sources.md` |
| **Visitors** | |
| Attractions (must-see vs skip) | `visitor-attractions.md` |
| Itineraries (1/3/7 days) | `visitor-itineraries.md` |
| Where to stay | `visitor-lodging.md` |
| Tips & day trips | `visitor-tips.md` |
| **Neighborhoods** | |
| Quick comparison | `neighborhoods-index.md` |
| Sukhumvit (Asok, Thonglor, Ekkamai) | `neighborhoods-sukhumvit.md` |
| Silom, Sathorn, Riverside | `neighborhoods-silom.md` |
| Ratchathewi, Ari, Phaya Thai | `neighborhoods-ari.md` |
| Old Town, Chinatown, Rattanakosin | `neighborhoods-oldtown.md` |
| Choosing guide | `neighborhoods-choosing.md` |
| **Food** | |
| Overview & street food culture | `food-overview.md` |
| Street food guide | `food-street.md` |
| Thai cuisine essentials | `food-thai.md` |
| International & fine dining | `food-international.md` |
| Best areas for dining | `food-areas.md` |
| Dietary & practical | `food-practical.md` |
| **Practical** | |
| Moving & settling | `resident.md` |
| Transport (BTS, MRT, taxis, Grab) | `transport.md` |
| Driving, licenses, buying vehicles | `driving.md` |
| Cost of living | `cost.md` |
| Thai taxes (180-day rule, remittance) | `taxes.md` |
| Safety & scams | `safety.md` |
| Weather & seasons | `climate.md` |
| Local services (banking, SIM) | `local.md` |
| Shopping, malls, tailors, VAT refund | `shopping.md` |
| **Career & life stages** | |
| Digital nomad guide | `nomad.md` |
| Teaching English | `teaching.md` |
| Tech industry & startups | `tech.md` |
| Business setup | `business.md` |
| Retiring in Bangkok | `retirement.md` |
| Buying property (condo quota, FET) | `property.md` |
| Visas (exemption, DTV, retirement, LTR) | `visas.md` |
| **Lifestyle** | |
| Culture & customs | `culture.md` |
| Festivals & annual calendar (Songkran) | `festivals.md` |
| Kids, schools & family life | `families.md` |
| Healthcare & hospitals | `healthcare.md` |
| Nightlife & entertainment | `nightlife.md` |
| Expat lifestyle & social | `lifestyle.md` |
| Thai language basics | `language.md` |
| **Anything else** | Ask role + timeline first (`references/domain.md` Rule 1), then route to nearest file; short visit defaults to `visitor-tips.md`, staying defaults to `resident.md` |

## Core path

1. Identify **role** and **timeline** (tourist days vs months vs relocation) before naming a neighborhood or visa.
2. Load `references/domain.md` for visa/tax/cultural red lines and traps; load leaf files only for the active branch.
3. Quote money as **ranges in ฿** with approximate USD at ~35 THB = $1; never a single false-precision price.
4. Flag volatile items (visa terms, tax rules, cannabis rules) as verify-before-money; open `references/sources.md` and the live official page when the user is about to commit.
5. Respect stored preferences in `<state_root>/config.yaml` when present (`references/state.md`).
