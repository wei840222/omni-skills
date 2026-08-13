# Prices Over Time, And Flights In The Air

Scope: two kinds of watching. Before the ticket, watching a price until it hits a target. After the ticket, watching the operation until the aircraft is on the ground.

**Before setting an alert or answering "is this a good price"**, read `## Routes` in `<state_root>/memory.md` when it exists. Compare only like-for-like observations and state the freshness gap.

**Contents:** [What Prediction Can And Cannot Do](#what-prediction-can-and-cannot-do) · [Building The Reference Range](#building-the-reference-range) · [Setting Alerts That Work](#setting-alerts-that-work) · [Buying Decision](#buying-decision) · [Price Drops After Purchase](#price-drops-after-purchase) · [Watching The Operation](#watching-the-operation) · [The Day Of Travel](#the-day-of-travel) · [What To Record](#what-to-record)

## What Prediction Can And Cannot Do

Say this plainly whenever a user asks whether prices will go up:

- **No public service predicts a specific route's future price.** Consumer prediction features are directional summaries of history, and their accuracy is not published in a form anyone can check.
- Historical observations can help compare a specific route, but do not predict its future price.
- What is *not* usable: any claim about the best day of the week to buy, any single "book N days ahead" number applied across routes, and any percentage saving quoted without the route it came from.
- The reliable edge is not prediction. It is knowing **this route's own price distribution** and having a target set before emotion arrives.

## Building The Reference Range

A range is worth more than a prediction, and it takes four observations to have one.

- Record the price in `## Routes` each time the route is searched: the price with its currency, the date seen, the dates searched, and the cabin. Four to six observations across a couple of months bound the route.
- The comparison must be like for like: same cabin, same bag inclusion, same number of stops. A cheaper number that is Basic economy with no bag is not a lower price.
- Note the **shape**, not just the low: a route that sits at 430-700 with occasional 380s behaves differently from one that never moves off 500.
- Peak dates have their own range. Christmas on the same route is a different distribution, and mixing them makes both useless.
- One row per route in `## Routes`, overwritten on each check — never a second row for the same route.

## Setting Alerts That Work

- Set a user-approved target against comparable route observations, not a generic percentage.
- Include flexible dates only when the traveller permits them.
- Two alerts on the same route with different targets is a reasonable setup: one at "good", one at "book immediately".
- Alert fatigue is real. Any alert that fires weekly is set wrong and will be ignored when it matters.
- Record where each alert lives in the `Alert` column of `## Routes` — an alert nobody can find later is an alert nobody can cancel.
- Set a user-approved check cadence based on departure date, route availability, and tolerance for price movement; record comparable observations.

## Buying Decision

Book when any of these is true, and say which one:

- The price is at or below the target derived from the stored range.
- The itinerary is scarce: thin route, few frequencies, peak date, or a party that needs seats from one fare bucket.
- The fare has seller-confirmed cancellation terms that make a decision reversible.

Do not book because a site says "only 2 seats left at this price" — that is a bucket count, and it is displayed to create urgency as much as to inform.

## Price Drops After Purchase

- A few carriers and some jurisdictions allow rebooking at the lower price, usually as a credit rather than cash, and typically only within a defined window.
- A seller-confirmed cancellation or change term can make a rebook reversible; verify current applicability before acting.
- Card price-protection benefits have largely disappeared for travel; check the current benefits guide rather than the folklore.
- Otherwise the correct answer is: the price paid was a decision made with the information available, and re-checking after purchase only buys regret. Say it once and stop watching the route — and delete its `## Routes` row.

## Watching The Operation

From about T-24h, and earlier for a trip with no slack:

- **The inbound aircraft is the best available predictor.** Find the aircraft's previous flight; if it is two hours late arriving, your departure is two hours late, whatever the departure board says.
- Airline apps notify earlier than departure boards and usually earlier than email.
- Independent tracking services show the aircraft's position, its actual airborne time and its historical on-time record for that flight number — the last of these is worth checking *before* booking a tight connection.
- Weather at the destination and at the hub matters more than at the origin, and air-traffic control programmes are published in some markets hours before airlines announce anything.
- Gate changes are common and are announced late. Terminal changes are rarer and more expensive to miss.
- Operational signals can indicate a possible disruption; verify status through the carrier before advising or acting.

## The Day Of Travel

- Check in at the opening of the window when seats are assigned then, or when the carrier charges for airport check-in.
- Re-verify terminal and check-in information for a codeshare with the operating carrier.
- Arrive against the airport's own published security wait, not a habit. Some airports publish live queue times.
- Keep the boarding pass in the airline app and one offline copy; keep the barcode image out of `<state_root>/`.
- If a delay is building, gather carrier-confirmed alternatives and the applicable fare or passenger-rights terms.

## What To Record

When the user asks to watch a route, record comparable prices with date and source in its `## Routes` row. When a ticket is retained, add it to `<state_root>/bookings/<year>.md`; when a flight or claim is retained, use the corresponding record in `<state_root>/flown/` or `<state_root>/claims/`.
