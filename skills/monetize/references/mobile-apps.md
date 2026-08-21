# Mobile Apps: Monetization Plan

## Choose the value and model

| Model | Value pattern | First question |
|---|---|---|
| Subscription | Repeated, continuing value | What value recurs each billing period? |
| Consumable purchase | A replenished unit such as credits | Can customers understand and control consumption? |
| One-time unlock | Durable feature value | Does the feature remain valuable without ongoing service cost? |
| Paid app | Clear value before purchase | Can the listing establish the outcome before trial? |
| Advertising | Free experience with attention inventory | Does ad load preserve the core experience? |

Select a model only after naming the customer outcome, cost to serve, expected usage, refund path, and support capacity. A subscription fits continuing value; it is not a default for a static utility.

## Price and receipt model

For each candidate price, calculate:

```
net receipts = list price - store fee - applicable taxes - refunds/chargebacks - variable delivery cost
active customers needed = target monthly contribution / net monthly contribution per active customer
```

Read `references/industry-benchmarks.md` to identify the applicable current Apple or Google Play fee. Model a range when eligibility, country, taxes, or billing route varies.

## Paywall experiment

1. Define the value moment the customer experiences before the paywall.
2. Choose one change to test: offer framing, timing, package, price, or trial terms.
3. Set a primary metric (for example, completed purchase per eligible user) and guardrails (refunds, early cancellation, support contacts, and review sentiment).
4. Record audience eligibility, dates, assignment, sample/decision rule, and results.
5. Keep the winning variant only when it improves the primary metric without violating guardrails; otherwise restore the baseline and document the learning.

Show a clear price, billing period, renewal terms, and a reachable way to restore purchases or obtain support. Use the current store documentation for platform-specific paywall, refund, grace-period, and introductory-offer implementation.

## Offer design

Offer packages that map to distinct customer needs. Present the recurring period and total commitment clearly. A trial is useful only when the product can demonstrate continuing value during the trial; measure post-trial retention before scaling it.

## Implementation handoff

Provide the chosen billing products, entitlement rules, restore-purchase behavior, analytics events, and customer-support path to the implementation owner. Confirm SDK APIs and store configuration in their current official documentation instead of copying a version-specific code snippet from this skill.
