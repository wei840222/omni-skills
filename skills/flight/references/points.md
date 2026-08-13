# Points, Miles, and Elite Status

Scope: earning, valuing, and protecting a balance, plus whether a tier is worth pursuing. Verify programme rules and award availability before a transfer or redemption.

**Before answering anything about balances, tiers, or requalification**, read `## Loyalty` in `<state_root>/memory.md` and `<state_root>/flown/<year>.md` when those records exist.

**Contents:** [Three Currencies, Not One](#three-currencies-not-one) · [Valuation](#valuation) · [Earning From Flying](#earning-from-flying) · [Earning Without Flying](#earning-without-flying) · [Crediting Decisions](#crediting-decisions) · [Elite Status](#elite-status) · [Is The Tier Worth It](#is-the-tier-worth-it) · [Expiry And Housekeeping](#expiry-and-housekeeping) · [Cards And Annual Fees](#cards-and-annual-fees)

## Three Currencies, Not One

Conflating these is the source of most bad advice.

| Currency | What it does | Where it lives |
|---|---|---|
| Redeemable points/miles | Buy award tickets and upgrades | The airline programme, or a transferable bank programme |
| Qualifying units (miles, segments, points, spend) | Earn and keep elite tier | The airline programme only, never transferable, reset each qualifying year |
| Transferable bank points | Move into airline programmes at a ratio, usually one-way | The card issuer's programme |

Transferable points are worth more than airline points because they are optional: they become whichever programme has the seat. That optionality is destroyed the moment they are transferred, which is why the transfer happens after the seat is confirmed, never before (Rule 7).

## Valuation

```
cpp = (cash price of the same ticket − taxes and fees payable on the award) ÷ points required × 100
```

Worked: a £480 cash fare, an award at 25,000 points plus £180 in surcharges. (480 − 180) ÷ 25,000 × 100 = **1.2 cpp**.

- Baselines to beat: roughly **1.2-1.5 cpp** in economy, **2 cpp and above** in premium cabins where cash prices are irrational. Below the baseline, pay cash and keep the points.
- Compare against the fare you would **actually buy**. Valuing an award against a first-class fare nobody would pay produces a fantasy cpp; this is how points blogs justify redemptions that were bad.
- Subtract the value of what the award loses: points earned on the cash fare, status credit, and often change flexibility.
- Points have no fixed worth. Programmes devalue without notice, and several have moved to dynamic pricing where the chart is whatever the cash price is — which caps the achievable cpp permanently.
- **Expiring points are worth their redemption value at any cpp above zero.** The baselines apply to points you can keep.

## Earning From Flying

- Most programmes now earn on **money spent with the airline**, not distance flown; distance-based earning survives mainly for partner flights, where a published table maps the operating carrier's fare class to a percentage of distance.
- Earning can vary by fare class, operating carrier, and crediting programme. Check the current programme rule before assuming a flight earns.
- Elite tiers multiply earning, which is where most of a tier's redeemable value actually comes from.
- Credit-posting and retro-claim windows vary by programme. Verify the current programme policy before action; when the user asks to retain flight history, use `<state_root>/flown/<year>.md`.

## Earning Without Flying

For most people this dwarfs earning from flying:

- **Co-branded and transferable-points cards**: the sign-up bonus on one card usually exceeds a year of economy flying.
- **Transfer bonuses** between bank programmes and airlines run periodically. A 20-30% bonus improves cpp by the same proportion — but only transfer against a seat already held.
- **Shopping and dining portals**, stacked with a card's category bonus.
- **Hotel and rental partners**, and programme-to-programme conversions, which are usually poor value in the airline direction.
- **Buying points** is worth it only against a specific, confirmed, high-cpp redemption where the purchase price per point is comfortably below the cpp achieved — never speculatively.

## Crediting Decisions

Every flight can usually be credited to any programme in the alliance, and the choice is made **at check-in at the latest**.

- Credit where the earning table is best for that fare class, or where the tier progress matters most — those are frequently different programmes, and one must be chosen.
- Concentrating in one programme reaches a tier; spreading can maximise redeemable points. When the user asks to retain the preference, record `loyalty_focus` in `<state_root>/config.yaml`.
- Some programmes earn on partner flights but do not count them for their own tier. Read both tables, not one.

## Elite Status

The qualifying year rarely matches the calendar year, and the metric differs by programme: distance flown, segments, spend, or a points-per-fare hybrid. All of them can usually be topped up by spending on a co-branded card.

Benefits, roughly in order of real value: free checked bags and seat selection, priority security and boarding, lounge access on the right routes, earning multipliers, waived change fees, upgrade instruments, and last — because it is the least reliable — the operational upgrade.

Status matching and challenges are real: a competing programme will often match a tier held elsewhere, sometimes with a flying requirement inside a window. Worth checking whenever the user changes their base airport or their main airline.

## Is The Tier Worth It

Run the arithmetic rather than the feeling:

```
value = (bag fees avoided + seat fees avoided + lounge visits × the price of a day pass
         + extra points earned × your cpp + change fees waived)
cost  = incremental spend or flying done only to qualify
```

A mileage run — flying purely to qualify — is worth it only when `cost per qualifying unit × units still needed < value of the tier for the coming year`, and only when the tier is genuinely close. Two thirds of the way and running out of year is usually a signal to let it go and requalify next year from a full runway.

Record the requalification date and the current progress in `## Loyalty`, and put the date in `## Due`. Tiers are lost silently to a deadline nobody diarised.

## Expiry And Housekeeping

- Expiry policies vary from "never" to "24 months of inactivity". Where activity resets the clock, the cheapest activity is a portal purchase, a small transfer, or a dining registration — not a redemption.
- Orphan balances too small to redeem are worth burning on magazines, upgrades of ancillaries, or charity transfers before they expire worthless.
- Household pooling exists in several programmes and quietly rescues balances that would each be useless.
- Family accounts, programme mergers and airline consolidations all produce forced conversions; when one is announced, check the ratio and the deadline.
- Loyalty programmes can change earning, redemption, and account terms. Verify the programme's current rules before a transfer or redemption.

## Cards And Annual Fees

When the user asks to track a card's travel benefits, store the non-sensitive subscription information in `<state_root>/finances/subscriptions.md`: name, provider, annual fee with currency, renewal date, and expiring benefits. Keep card numbers out of `<state_root>/`.

The retention question — keep, downgrade or close — is answered by comparing the fee against benefits actually used in the last twelve months, which is exactly what that row records.

**After any balance, tier, progress figure or expiry date is seen, write it into `## Loyalty` with its `As of` date**, and put every expiry — points, tier, voucher, card credit — into `## Due`. A balance without a date is not a number anyone can act on next quarter.
