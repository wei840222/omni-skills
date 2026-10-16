---
name: travel
description: >
  Maintain a traveler standing system for wishlist destinations, passport and
  visa readiness, Schengen-style day counts, shared bookings, points expiry,
  trip budgets, disruption claims, and post-trip debriefs. Use when someone
  names a place to visit someday, checks entry rules before dates are fixed,
  counts days already spent in a rolling allowance, records a reservation or
  cancel deadline, handles a cancelled flight, missing bag, stolen passport,
  or claim, chooses the next trip against season and budget, travels with
  children, a group, elderly parents, or a pet, stays longer than a month, or
  has points or elite status about to expire. Prefer `travel-planning` for one
  trip day-by-day itineraries, `flight` for fare search, `booking` for lodging
  search, `car-rental` for hire cars, and `expat` for permanent relocation.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"✈️"}'
  related-skills: '{"travel-planning":"Day-by-day itinerary and multi-city routing for one trip.","flight":"Fare search, award travel, baggage, and flight disruption claims.","booking":"Accommodation search and booking completion after a destination is chosen.","car-rental":"Vehicle hire pricing and insurance handoff for self-drive segments.","expat":"Permanent relocation, residence visas, and settling abroad."}'
---

## State location

Travel standing-system state may exist in `<workspace>/travel/`,
`<workspace>/memory/travel/`, or `~/travel/`. Before reading or writing state,
resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/travel/`, `<workspace>/memory/travel/`, `~/travel/`.
3. If several candidate directories exist, use only the highest-precedence one and
   report the separate copies; do not merge or cross-write.
4. If none exists and the user wants continuity, create `<workspace>/travel/`
   when `<workspace>` is available; otherwise ask for a state root instead of
   guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every travel-owned state path in this skill.
Shared reservation rows live at `<state_root>/bookings/<year>.md` when that
shared box is part of the same resolved root family; update only rows this skill
wrote, matched on locator. Legacy `~/Clawic/data/travel/` is a migration source
only—keep it out of the active lookup order and migrate only with named consent.
Scripts and shell examples must receive the resolved filesystem path; never treat
the literal string `<state_root>` as a directory name.

## Data and privacy

At the start of a session that needs continuity, read
`<state_root>/config.yaml` and `<state_root>/memory.md` (including `## Boxes`
and `## Due`). Open any file `## Boxes` names when its condition applies.
Before answering about a reservation or date, read
`<state_root>/bookings/<current year>.md` when it exists. If state is missing,
work from defaults and say so only when `home_airports` or `passport_countries`
would change the advice.

Write durable outcomes before the session ends: wishlist captures, reservation
changes, document renewals, border-day counts, spend baselines, claims, loyalty
status, finished-trip debriefs, and reusable procedures. Use
`assets/memory-template.md` as the only template for new durable files.

Exclude credentials from `<state_root>/`. Store pointers such as
`1password:Travel/Passport` and keep issuing country, expiry, and last four only.
Never execute purchases, bookings, or cancellations—prepare the page, deadline,
and amount for the user to confirm.

Value precedence: `<state_root>/config.yaml` → optional shared
`<state_root>/profile.yaml` → Configuration defaults in
`references/configuration.md`.

## When to use

- Capture or rank destinations against season, budget, and company
- Check passport validity, visas, ETA/ETIAS-style authorization, vaccines, or rolling day allowances before fixing dates
- Record or change reservations and free-cancel deadlines
- Handle disruption: delay, cancellation, missed connection, lost bag, stolen documents, illness, raised advisory
- Travel with children, groups, elderly parents, pets, or stays past one month
- Close the loop after returning home
- Not for one-trip day plans (`travel-planning`), fare shopping (`flight`), lodging search (`booking`), car hire (`car-rental`), or emigrating (`expat`)

## Quick reference

| Situation | Play | Load |
|---|---|---|
| Wishlist / next destination | Capture decision-ready or intersect window × season × budget | `references/wishlist.md` |
| Passport / visa / day count | Check validity windows and count rolling allowances backwards | `references/documents.md` |
| Vaccines / meds / insurance | Lead times and cover windows before non-refundables | `references/health.md` |
| Cost / cards / FX | Quote a dated total, not a bare fare | `references/money.md` |
| Reservation made or deadline | Shared bookings row + `## Due` | `references/bookings.md` |
| Travel day / connections | Ticket-structure buffers and declaration rules | `references/travel-day.md` |
| Disruption / stolen docs | Stabilize trip first, then claim | `references/disruption.md` |
| Safety / advisories | Prevention list + emergency card | `references/safety.md` |
| Packing / kit | Standing kit refined by unused gear | `references/kit.md` |
| Ground transport / passes | Price legs against passes | `references/transport.md` |
| Companions | Whose constraint governs money and pace | `references/companions.md` |
| Long stay / nomad | Legal day counting and connectivity | `references/long-stays.md` |
| Business / per diem | Policy and receipt shape first | `references/business-trips.md` |
| Points / status | Expiry before optimization | `references/loyalty.md` |
| Just home | 48-hour debrief | `references/debrief.md` |
| Material facts refresh | Re-open official pages before non-refundables | `references/sources.md` |

## Core rules

1. **Archive before web.** Read memory, place files, and spend baselines before searching. Say which source you used.
2. **Entry permission before dates.** Treat passport validity and rolling allowances as booking gates. Many destinations effectively need ~6 months remaining validity at travel time—confirm on the destination authority page. Schengen short-stay practice commonly also needs a passport issued within the previous 10 years and valid at least 3 months beyond intended departure; verify on EC border/visa pages before quoting. Count rolling limits backwards from intended entry (Schengen orientation: 90 days in any 180). Worked example and live sources: `references/documents.md` and `references/sources.md`.
3. **Every number is a dated total.** transport + lodging + local transport + food + activities + insurance + fee stack. Name the four largest lines (`references/money.md`).
4. **Book by irreversibility.** Permission → scarce release-date item → long-haul transport → lodging → everything else. Prefer refundable rates while the trip is conditional.
5. **Buffers are computed.** One ticket: carrier MCT is the floor. Separate tickets: plan generous self-transfer buffers (orientation ≥3 h international / ≥2 h domestic) and treat last departure as a hotel risk. Airport arrival orientation: 2 h international / 90 min domestic, scaled by `risk_posture` (`references/travel-day.md`).
6. **Unwritten reservations do not exist.** Write `<state_root>/bookings/<year>.md` and free-cancel lines under `## Due` immediately.
7. **Under-plan anchors.** `itinerary_density` sets fixed-time anchors per day; keep the rest as candidates.
8. **Debrief within 48 hours.** Actual total, three recommendations, one skip, unused gear, learned per-day rate (`references/debrief.md`).

## Output gates

Before a plan, quote, or recommendation:

- Passport / authorization / rolling day count checked or explicitly marked unverified
- Number is a dated total with currency
- Archive consulted when state exists
- Mentioned reservations and deadlines are written or queued to write
- No purchase/cancel is being executed—only prepared
- Durable session learning landed via `assets/memory-template.md`
- No passport, card, or password values were stored

## Configuration, traps, expert forks

Load `references/configuration.md` for defaults and preference areas,
`references/traps.md` for common failure modes, and
`references/expert-disagreements.md` for genuine trade-offs. Soften absolute
medical, legal, and fee claims: route red-flag symptoms to clinicians or local
emergency numbers and re-check official pages before non-refundable spend.
