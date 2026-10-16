---
name: car-rental
description: >
  Find and compare car rental deals, track dynamic pricing alerts, and analyze
  rent vs lease vs buy for vehicle needs. Use when the user needs a hire car,
  airport or city pickup quote, insurance and deposit guidance, one-way drop
  fees, long-term rental or subscription comparison, or lease-vs-rent advice.
  Prefer `travel` / `travel-planning` for whole-trip standing systems and
  itineraries, `taxi` for on-demand rides rather than multi-day self-drive,
  `parking` for bay search after a car is secured, `booking` for lodging, and
  `buy` when the ask shifts to purchasing a vehicle.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🚗"}'
  related-skills: '{"travel":"Standing travel docs, wishlists, and long-lived trip boxes that may include self-drive segments.","travel-planning":"Day-by-day itineraries where a hire car is only one leg.","taxi":"On-demand rideshares and car services instead of multi-day self-drive.","parking":"Bay search and reservation after a rental car is secured.","booking":"Lodging and non-vehicle reservation terms.","buy":"Vehicle purchase research when rent/lease is no longer the right path.","compare":"Generic option matrices outside rental-specific total-cost rules."}'
---

# Car Rental

Help the user find, compare, and decide on vehicle hire. Always compare more
than one source, price the **total** cost (not the headline daily rate), and
resolve durable preferences under `<state_root>/` only after consent.

## State location

Car-rental preferences, saved searches, and alerts may exist in
`<workspace>/car-rental/`, `<workspace>/memory/car-rental/`, or `~/car-rental/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/car-rental/`, `<workspace>/memory/car-rental/`, `~/car-rental/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable state must be created, default to
   `<workspace>/car-rental/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. If older
notes exist only at `~/Clawic/data/car-rental/`, propose a copy/validation/cutover
plan and wait for user confirmation before any migration. Never write the
literal string `<state_root>` to disk.

## When to use

- Short airport or city rentals with multi-site price comparison
- One-way drop-offs, mileage caps, young-driver or debit-card constraints
- Insurance / CDW excess checks against the user's existing coverage
- Price-drop or availability alerts the user explicitly requested
- Rent vs long-term rental vs lease vs buy for a known duration

## Quick reference

Load only the smallest file needed. Keep this SKILL.md as the router:

| Need | Load |
|------|------|
| First-use setup / consent | `references/setup.md` + `assets/data-templates.md` |
| Aggregators, fleets, subscriptions | `references/sites.md` |
| Rent vs lease vs buy framework | `references/comparison.md` |
| Verified source pins (Gate 6) | `references/sources.md` |

## Core rules

1. **Compare multiple sources.** Check at least two distinct channels (for
   example one aggregator and the winning company's direct site, or two
   aggregators). Prefer three when time allows: aggregator, direct, budget.
2. **Price total cost.** Include insurance (CDW / theft / liability), fuel
   policy, airport fees and taxes, mileage overage, one-way fees, and age
   surcharges before recommending.
3. **Apply saved preferences.** Use preferred class, transmission, fuel,
   insurance stance, and loyalty programs from `<state_root>/memory.md` when
   present.
4. **Alerts only with permission.** Ask frequency, notify on meaningful drops
   (about 15%+), and let the user disable anytime.
5. **Match product to duration.**

| Duration | Prefer |
|----------|--------|
| 1–7 days | Standard rental |
| 1–4 weeks | Long-term rental or subscription |
| 1–6 months | Lease or subscription |
| 6+ months | Lease, finance, or buy |

6. **Location intelligence.** Airport counters often cost more than city
   depots; check IDP / local licence rules and seasonal demand before locking
   a quote.

## Cost traps to navigate

Steer the user toward safer defaults rather than scare lists:

- Prefer **full-to-full fuel** unless refuelling before return is genuinely
  impractical; prepaid fuel is often overpriced.
- Treat basic CDW as incomplete when excess is high (€1000+); check credit-card
  or travel-insurance secondary coverage first.
- Confirm **one-way drop fees** before booking different cities.
- In Europe, filter for **automatic** when needed — cheapest rows are often
  manual.
- Recalculate deals that advertise low daily rates with tight **mileage caps**.
- Plan for **credit-card holds** (€1000–3000). Debit cards are frequently
  refused or require extra proof; verify the primary driver's physical card.

## Output expectations

- Name the sources checked and the total-cost assumptions.
- Separate headline rate from fees, insurance, and deposit holds.
- When lease/buy enters the conversation, load `references/comparison.md`
  before recommending.
- Prefer other skills when the ask is itinerary-wide (`travel-planning`),
  rideshare (`taxi`), parking only (`parking`), or vehicle purchase (`buy`).
