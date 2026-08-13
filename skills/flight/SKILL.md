---
name: flight
description: Manage flight searches, bookings, points, baggage rules, and disruption claims. Use for flight options, fare rules, award travel, ticket changes, or passenger-rights questions; load the relevant reference before live searches or current-rule advice.
metadata:
  version: "1.0.3"
  openclaw: '{"emoji":"✈️"}'
  related-skills: '{"travel-planning":"Extends flight choices into an itinerary, packing list, and whole-trip budget."}'
---

## State location

Flight state may exist in `<workspace>/flight/`, `<workspace>/memory/flight/`, or `~/flight/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/flight/`, `<workspace>/memory/flight/`, `~/flight/`.
3. If none exists and the user asks to retain flight state, default to `<workspace>/flight/`.

Use the selected `<state_root>` for every state operation in this skill. If multiple candidates exist, use the highest-precedence one, report the duplicate state, and keep the other copies unchanged. Treat prior Clawic paths as migration sources only; migrate them only through a user-approved copy, validation, and cutover.

## State and privacy

When `<state_root>/config.yaml` or `<state_root>/memory.md` exists, read the needed file before using saved preferences or answering about an existing trip. Read `<state_root>/bookings/<year>.md` only for a request that concerns an existing booking, date, or locator. If the needed state does not exist, work from the current request and disclose any assumption that changes the search.

Create state only when the user asks to save, track, or update durable flight information. Read `references/memory-template.md` before creating a record. Keep credentials in an external secret store and retain only a non-secret pointer such as `env:DUFFEL_API_KEY`; keep passport and ID numbers, boarding-pass barcodes, programme PINs, and card numbers out of state.

Use `<state_root>/bookings/<year>.md` for a saved flight ticket. Find its record locator first; update only that `Type: flight` entry. Store cancellation, flown-flight, claim, or voucher status in the corresponding state record only when the user asks to retain it.

## Reference Loading

Read `references/search.md` for fare research, `references/points.md` for loyalty decisions, `references/tracking.md` for price monitoring, `references/booking.md` for reservation workflows, and `references/apis.md` for provider integration. Before giving a current rule, deadline, compensation amount, or entry requirement, read `references/current-rules.md` and verify the rule against the applicable official source.

## When To Use

- Finding, comparing or pricing a flight: routes, dates, alternate airports, cash versus miles, "is this a good price", "should I book now"
- Deciding what to buy: fare families and fare rules, refundability, basic economy, direct versus OTA, one ticket versus two
- Anything after the ticket exists: seats, upgrades, baggage, name corrections, schedule changes, check-in, connections that look tight
- Something went wrong: delay, cancellation, missed connection, denied boarding, downgrade, delayed or damaged bag — including whether money is owed and how to claim it
- Loyalty economics: award searches, transfer partners, cents-per-point, elite status, requalification, expiring points and vouchers
- Trip-critical paperwork tied to a specific itinerary: passport validity, visas, ESTA/ETA, transit rules, minors, pets, assistance
- Mode: **advise by default** — present options with their total cost and let the user pick; search, monitor, draft a claim, or fill a form only when requested. The user completes purchases and payment.
- For an itinerary, packing list, or whole-trip budget, hand off to `travel-planning`.

## Quick Reference

| Situation | Play | Depth |
|---|---|---|
| "Find me a flight to X" | Confirm origin and date flexibility, then compare total cost per option | `references/search.md` |
| "Is this a good price?" | Compare a dated, like-for-like total against saved observations when available | `references/tracking.md` |
| "Should I book now or wait?" | Compare fare conditions, availability, and the traveller's flexibility; avoid generic timing promises | `references/tracking.md` |
| Cheap fare, unclear inclusions | Read the operating carrier's fare family, bag, seat, change, refund, and no-show rules | `references/booking.md` |
| Connection, baggage, disruption, refund, documents, assistance | Verify the carrier, airport, and applicable authority's current rule before advice | `references/current-rules.md` |
| Cash or miles, award space, transfer partners | Calculate value against the real cash price and confirm availability before a transfer | `references/points.md` |
| Building something that searches or tracks flights | Confirm provider capabilities, terms, and credentials | `references/apis.md` |
| Anything else about flying | Answer directly, then state the total cost and the next deadline it creates | — |

## Core Rules

1. **State the search assumptions.** Confirm or disclose the origin, dates, cabin, passengers, baggage, and acceptable connections before comparing options. Compare alternate dates or airports only when the traveller permits the trade-off.
2. **Price the trip, not the fare.** `total = fare + required bags + seat selection + payment costs + surface transport + change exposure`. Apply the same line items to every option.
3. **Verify fare conditions with the seller.** Use comparison tools to discover options, then confirm fare family, baggage, change, refund, and ticketing terms with the carrier or seller before a recommendation.
4. **Make the booking channel an explicit trade-off.** Compare price, ticket control during disruption, support, and connection risk before recommending a carrier or third-party seller.
5. **Check entry requirements against the current itinerary.** Verify passport, visa, transit, and onward-travel requirements through the destination authority or carrier guidance before non-refundable purchase; entry rules depend on traveller nationality and route.
6. **Treat self-transfers separately.** Check the published connection constraints for a single ticket. For separate tickets, state the missed-connection exposure and obtain the traveller's approval for the added risk.
7. **Value an award against a comparable cash ticket.** `cpp = (cash price − award taxes and fees) ÷ points × 100`. Confirm award availability before a transferable-points transfer.
8. **Explain ticket-rule risks with a compliant alternative.** If a proposed itinerary could forfeit later segments or baggage control, show the carrier rule and compare a one-way, open-jaw, or separate-ticket alternative.
9. **Confirm ticketing status.** Before calling an itinerary booked, verify the ticket number, passenger name, current itinerary, and fare rules with the seller.

## True Cost

The comparison table that makes the decision. Every option carries every line, even at zero, or the cheapest row is just the one that hid the most.

| Line item | Where it bites | How to price it |
|---|---|---|
| Base fare + carrier-imposed charges | Award tickets too: surcharges are levied on points bookings by several carriers | The number after taxes, in `currency` |
| Cabin bag | Low-cost carriers sell the overhead bin separately; a personal item under the seat is what "free" means | Priced at booking is cheaper than at the airport, which is cheaper than at the gate — often by 2-3× |
| Checked bag | Cheapest online pre-purchase, dearest at the desk | Per direction, per passenger; on separate tickets, per ticket |
| Seat | Assignment, family seating, and paid selection differ by fare and carrier | Confirm the carrier's current rule before pricing it |
| Payment surcharge | Card-type surcharges and currency conversion when the fare is not in your currency | Pay in the fare's own currency and let your card convert |
| Surface transport | The "same city" airport that is 90 minutes away | Both ends, both directions, at the actual hour of arrival |
| Change and cancel exposure | The fare's own rule, not the airline's brand | Fee + fare difference, or the value of the credit and its expiry |
| Time | A 21-hour two-stop against a 9-hour non-stop | State the elapsed hours next to the price; do not decide it for them |

## Deadlines That Expire Value

This domain loses more money to clocks than to bad prices. When the user asks to track a deadline, store it in `<state_root>/memory.md` with its source and the itinerary it applies to.

| Clock | Typical window | Consequence of missing it |
|---|---|---|
| Cancellation, check-in, assistance, and voucher deadlines | Seller, carrier, and itinerary-specific | The available option or credit may expire |
| Baggage report and claim | Carrier and applicable convention | Evidence or a claim may be harder to establish |
| Passenger-rights claim | Applicable jurisdiction | The statutory deadline may expire |
| Points, tier, passport, visa, and ETA | Programme or authority-specific | Travel or benefits can be unavailable |

## Timing and price monitoring

Price behavior is route-, date-, and inventory-specific. Use `references/tracking.md` to compare dated, like-for-like observations and set a user-approved alert or target; do not represent a generic booking window as a guarantee.

## Rights At A Glance

Read `references/current-rules.md` before quoting a compensation amount, deadline, or legal entitlement. Verify the current threshold and applicability against the official authority for the itinerary.

| Where | What triggers money | Roughly how much | Care regardless of cause |
|---|---|---|---|
| EU / UK passenger rights | Applicability, delay, notice, carrier, and exceptional-circumstance tests | Verify current official guidance | Care may be owed under the applicable rule |
| United States | Refund and denied-boarding rights depend on the event and current DOT rule | Verify current official guidance | Carrier commitments may add support |
| Other jurisdictions and international baggage claims | Rules vary by itinerary and convention | Verify the relevant authority or carrier guidance | Verify the applicable obligation |

## Output Gates

Before presenting an option, a booking, or a claim:

- Does every option in the comparison carry the same cost lines, including bags and surface transport (Rule 2)?
- Have I named the fare rule that decides what happens if this trip changes — change fee, credit, refund, or nothing?
- Does every connection in what I am recommending clear the MCT-plus-buffer test, and did I say what happens if it is missed (Rule 6)?
- Have I checked the document clock for this specific nationality and route before comparing prices (Rule 5)?
- Am I quoting a compensation amount or a deadline? Then I checked the current rule rather than reciting it.
- **Persistence:** when the user asks to retain a ticket, observed price, balance, expiry, claim, or voucher, create the scoped record described in `references/memory-template.md` and include any source-backed deadline.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; when persistence is requested, store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| home_airports | list (IATA codes, preferred first) | none | Origin for every search and price alert; while unset, name the assumed origin before searching (Rule 1) |
| passport_country | list (ISO country codes, one per traveller document) | none | Makes clear that entry requirements must be checked for each traveller and itinerary |
| cabin | economy \| premium-economy \| business \| first | economy | Cabin searched and priced, and the cpp baseline applied in Rule 7 |
| currency | text (ISO 4217) | from `profile.yaml`, else USD | Currency of every quote, target price and stored amount |
| max_stops | number (0-2) | 1 | Filters itineraries before comparison; 0 turns non-stop into a hard requirement rather than a preference |
| connection_buffer_min | number (minutes) | 30 | Added to the carrier or airport connection requirement when the traveller asks for a buffer |
| carry_on_only | bool | false | Removes checked-bag cost from the True Cost table and changes the fare family recommended |
| separate_tickets_ok | bool | false | Whether self-transfer and virtual-interlining itineraries are offered at all |
| booking_channel | direct \| ota \| either | direct | Where options are sourced and bought (Rule 4) |
| loyalty_focus | text (programme or alliance) | none | Which programme's award availability and earning rules are checked first |

Preference areas — customizable dimensions; when persistence is requested, a stated preference is recorded in `<state_root>/config.yaml` and applied from then on:

- **Tooling** — which metasearch, aggregator and award-search tools the user trusts, and which they refuse to buy through — affects the three sources of Rule 3
- **Comfort and timing** — red-eye tolerance, earliest departure and latest arrival, aircraft and cabin preferences, seat type, maximum elapsed journey time — affects option ranking
- **Restrictions** — airlines vetoed for any reason, no basic economy, no overnight layovers, dietary and special meals, accessibility needs, travelling with a companion who has their own constraints — affects filtering before options are shown
- **Risk posture** — appetite for non-refundable fares, self-transfer, tight connections and error fares; whether travel insurance is expected on every trip — affects booking and connection recommendations
- **Payment ecosystem** — which points currency and cards the user actually holds, which airline programme credits their flying, whose lounge access matters — affects points analysis
- **Presentation** — how many options to show, whether to lead with cheapest or fastest, whether every answer carries the total-cost table — affects the shape of every recommendation
- **Cadence** — how often to check watched routes, when to audit points and tiers, when to re-check passport validity — affects the `## Due` table

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Comparing headline fares across carriers | The fares include different products; the cheapest headline is frequently the dearest trip | The True Cost table, every line filled for every option (Rule 2) |
| Booking two tickets to save money without saying so | The saving can shift missed-connection risk to the traveller | Price it as a different product and state the carrier, immigration, baggage, and rebooking exposure |
| Trusting an aggregator's baggage figures | Aggregators infer allowances and get fare families wrong, especially on low-cost and basic fares | Confirm on the operating carrier's own fare page before quoting a total |
| Booking an award before the seat is confirmed | Transferred points are stranded in a programme the user does not use | Confirm or hold the seat, then transfer (Rule 7) |
| Treating a schedule change as bad luck | A carrier policy or applicable law may offer a remedy | Read the carrier policy and applicable official guidance before advising |
| Accepting a voucher during a disruption | A voucher can change the traveller's available options | Compare refund, reroute, voucher, and statutory-claim implications before accepting |
| Leaving the airport without a bag report | Later evidence can be harder to establish | Follow the carrier's current baggage-report procedure and retain the report reference |
| Adding the frequent-flyer number after flying | Earning and retro-credit rules vary by fare class and programme | Attach the number at booking when possible and verify the programme's current policy |
| Assuming the marketing carrier's baggage rules apply | Allowance depends on the itinerary and carrier rules | Identify the operating carrier and verify the current baggage policy |
| Renewing a passport "when it expires" | Most refusals happen on valid passports that fail the 6-month or 10-year rule | Diary the renewal against the rule, not the expiry date (Rule 5) |
| Chasing a price daily | Repeated, non-comparable checks create noise | Set a user-approved target and cadence in `references/tracking.md` |
| Buying trip insurance without reading the card benefit already held | Coverage may overlap or leave gaps | Compare the current card terms with the proposed policy before purchase |

## Where Experts Disagree

- **Book early versus wait.** Both camps are right about different products: on a route with many carriers and daily frequencies, waiting for a target price wins; on a thin route, a peak date or a family-sized party, the cheap inventory sells out and waiting only buys a worse seat map. Frequency and party size decide, not the calendar.
- **Direct versus OTA.** Consolidator and OTA pricing on multi-carrier itineraries is genuinely cheaper and sometimes the only way to combine two airlines on one ticket. The disagreement is about disruption handling, and it is settled by who has to reissue the ticket at 6am (Rule 4).
- **Points maximizing versus cash simplicity.** Above roughly 2 cpp in a premium cabin the points game beats cash back by a wide margin; below ~1.2 cpp it is an unpaid hobby with devaluation risk. The frontier is how much flying is already happening — points optimization pays in proportion to volume.
- **Insurance versus card coverage.** Card benefits are free but conditional (paid with that card, specific delay lengths, secondary coverage). Standalone policies pay more reliably on medical and cancellation. The split most practitioners land on: card coverage for delay and baggage, a policy for medical and cancel-for-cause on expensive or long trips.
- **Self-transfer platforms.** Their own guarantees do rebook you, and the products have matured; what has not changed is that no airline is involved, so an immigration queue or a strike leaves you with a claim against a platform rather than a seat on the next flight.

## Research Sources

- [Flight Compensation Regulation 261/2004 (Wikipedia)](https://en.wikipedia.org/wiki/Flight_Compensation_Regulation)
- [Montreal Convention (Wikipedia)](https://en.wikipedia.org/wiki/Montreal_Convention)
