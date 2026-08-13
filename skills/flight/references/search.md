# Finding the Flight

Scope: from "I need to be in Lisbon in October" to a shortlist of priced options. Verify fare rules and purchase-channel terms with the seller before recommendation.

**Before searching**, read `## Routes` in `<state_root>/memory.md` when it exists. Use any saved dated observations as comparison context rather than a price guarantee.

**Contents:** [The Three Sources](#the-three-sources) · [The Search Grid](#the-search-grid) · [Alternate Airports](#alternate-airports) · [Itinerary Shapes](#itinerary-shapes) · [Low-Cost Carriers](#low-cost-carriers) · [Long-Haul Specifics](#long-haul-specifics) · [Stopover Programmes](#stopover-programmes) · [Presenting the Shortlist](#presenting-the-shortlist)

## The Three Sources

Each is blind to something the others see. Using one is how a recommendation ends up wrong in a way nobody notices until the airport.

| Source type | Sees | Blind to |
|---|---|---|
| Metasearch (calendar and map views) | Market shape, cheapest dates, cheapest destinations, price history for the route | Several low-cost carriers, fare-family detail, anything the carrier does not feed |
| Aggregator / OTA with virtual interlining | Combinations no single airline sells, low-cost carriers, one-way pairings | Whether the combination is protected, and the real baggage rules on each leg |
| The operating airline's own site | The fare rules you will be held to, fare families, real seat maps, ancillary prices, award space | Every other airline |

Search order that wastes least time: metasearch to find the date and the shape → aggregator to confirm nothing cheaper exists off-alliance → the operating carrier to price the actual product and buy it.

## The Search Grid

- Compare nearby dates only when the traveller permits date flexibility.
- Compare departure days when date flexibility exists; avoid treating a weekday pattern as a route-specific price guarantee.
- **Cheapest-month and map views** answer "where can we go for €200" and "when is this destination cheap" — the two questions users ask badly and get answered as fixed-date searches.
- **Search both directions separately** before assuming a return fare is best; on many low-cost and transatlantic routes two one-ways price lower and change independently.
- **Check the fare with one checked bag and a seat included**, not just the base — on legacy carriers the bundle is frequently cheaper than the base fare plus the same items bought separately.
- **Overnight and early departures** hide costs: a 06:00 departure often means a taxi or a hotel the night before. Price it or say it.

## Alternate Airports

Include every airport within roughly a 2-hour surface journey, then subtract the cost of getting there.

- `net saving = fare saving − (transport both ways + parking or extra night + hours × how the user values them)`. Show the subtraction; a €70 saving that costs €55 in buses and 3 hours is not a saving.
- Multi-airport cities behave differently at each end: a cheaper arrival airport at 23:40 with no public transport is a taxi fare, while the same airport at 14:00 is genuinely cheaper.
- Secondary airports named after a city they are 90+ minutes from are a recurring low-cost carrier trick — check the actual distance, not the name.
- Compare a positioning flight only when its total cost, time, baggage, immigration, and separate-ticket exposure are acceptable to the traveller.

## Itinerary Shapes

| Shape | When it wins | Watch |
|---|---|---|
| Return on one ticket | Legacy carriers, long-haul, anything where protection matters | Changing one leg often reprices the whole ticket |
| Two one-ways | Low-cost carriers, mixed carriers, uncertain return date | No protection between them; each has its own rules |
| Open jaw (into A, out of B) | Any trip that moves overland between cities | Often prices at or below the return; almost never searched |
| Multi-city | Three or more stops, or deliberate stopovers | Airline multi-city engines price better than aggregators here |
| Positioning flight | The long-haul fare from another city is materially lower | Separate ticket: state the missed-connection and overnight exposure |
| Round-the-world / alliance fare | Three or more continents in one trip | Priced by continents and mileage bands, booked with the alliance, not a website |

## Low-Cost Carriers

- Many are absent from metasearch entirely, or present with wrong ancillary prices. If a low-cost carrier serves the route, price it on its own site.
- The cabin-bag split is the trap: the free allowance is usually a small under-seat item, the overhead-bin bag is a paid extra, and buying it at the gate costs multiples of buying it online.
- Weight limits on cabin bags are enforced by some carriers and ignored by others; the enforcing ones weigh at the gate, where there is no cheap remedy.
- Priority boarding is sometimes the only way to guarantee bin space on full flights — that makes it part of the fare, not an upsell, on carriers that board by group.
- Check-in windows: several charge for airport check-in, and a few charge if you check in outside a set window. Put the check-in opening time in `## Due` at booking.
- Their disruption handling and applicable passenger rights vary; verify seller, carrier, and jurisdiction before recommendation.

## Long-Haul Specifics

- Aircraft type decides the experience more than the airline does: check the configuration for the specific flight number, not the fleet.
- A stop is not automatically worse. One stop with a 2-hour connection often lands earlier than a non-stop at an awkward hour, and prices 20-40% below it.
- Fifth-freedom flights — a carrier flying between two countries that are both foreign to it — sometimes put a premium-cabin product on a short route at a fraction of the usual price. Rare, worth checking on the classic corridors.
- Elapsed time, not flight time: a 21-hour two-stop and a 9-hour non-stop are different products. State both numbers.
- Day flights versus red-eyes are a comfort preference; when persistence is requested, record it in `<state_root>/config.yaml` under `comfort`.

## Stopover Programmes

Several carriers let you break the journey in their hub for days at no fare increase, sometimes with a free or subsidised hotel. This converts a connection into a second destination and is invisible to metasearch — it has to be built as a multi-city itinerary or booked through the carrier's own stopover product. Worth checking whenever the hub is somewhere the user would want to spend two days, and whenever a long connection is unavoidable anyway.

## Presenting the Shortlist

Three options, never more, each carrying the same lines from the True Cost table in `SKILL.md`: total in the user's currency, elapsed time, connections with their duration, bag and seat status, and the change rule in five words. Rank by whatever `presentation.lead_with` says, defaulting to total cost. Name the one you would pick and why in one sentence — a list of three with no recommendation pushes the decision back to the user unhelped.

When the user asks to track a route, record it in `## Routes` in `<state_root>/memory.md` — route, purpose, target price with currency, best observed total with date, and the comparable conditions.
