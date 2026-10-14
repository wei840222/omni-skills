# Subscription billing (payments lens)

For deep Stripe subscription object debugging, prefer `billing` and
`stripe-api-integration`. This reference covers product-level subscription design
shared across providers.

## Billing models

### Flat-rate

Fixed price per period. Simplest SaaS default.

### Tiered / volume

Price steps by seats or usage bands.

### Usage / metered

Pay for consumption (API calls, GB). Harder forecasting; needs metering pipeline.

### Hybrid

Base fee + overage. Stabilizes MRR with upside.

## Trial strategies

| Pattern | Trade-off |
|---------|-----------|
| Free trial, card required | Higher conversion intent; more start friction; forgotten-trial chargebacks risk |
| Free trial, no card | More starts; weaker conversion; needs nurture |
| Freemium | Viral potential; can cannibalize paid if free is too rich |

**Trial length:** short trials (about 7 days) suit simple products; 14–30 days
suit complex onboarding. Prefer the shortest period that still lets users reach
value — urgency helps, starvation hurts.

## Lifecycle events to design

| Event | Product response |
|-------|------------------|
| Trial started | Onboarding sequence |
| Trial ending soon | Upgrade reminder with clear price |
| Trial ended unpaid | Optional extension / discount path — policy-true only |
| Subscription activated | Confirm access + receipt |
| Payment failed | Dunning (email + smart retries) |
| Upgraded | Prorate policy explicit |
| Downgraded | Usually apply at period end unless product says otherwise |
| Canceled | Confirm end date; exit survey optional |
| Ended | Revoke paid access; win-back only if wanted |

## Dunning (failed payment recovery)

Involuntary churn from failed cards is a large share of total churn. A typical
recovery ladder:

1. Day 0: auto-retry + “update card” mail
2. Day 3: retry + stronger warning
3. Day 7: access-at-risk notice
4. Day 14: final warning before suspend
5. Day 15+: suspend paid features; keep limited recovery window
6. ~Day 30: cancel if still unpaid (align with provider retry settings)

Tune to provider smart-retries; do not invent fixed Stripe retry calendars from
memory — confirm current Billing behavior in docs.

## Proration

Mid-cycle plan changes need an explicit proration policy:

- **Upgrade:** charge difference now vs next invoice
- **Downgrade:** credit / apply at period end

Stripe and other PSPs expose proration knobs; set them deliberately and preview
invoices in test mode.

## Cancellation flow

**Make cancel easy and honest.** Dark patterns drive chargebacks and public
complaints.

**Do:**

- Clear Cancel control in account settings
- Confirm effective end date (usually end of paid period)
- Offer pause/downgrade as alternatives without trapping the user
- Optional short exit survey

**Avoid:**

- Hide cancel behind “email support only”
- Instant access cut when the customer paid through period end (unless they asked
  for immediate termination)
- Guilt-copy that misstates data deletion

Default healthy path: **cancel at period end**; immediate delete only on explicit
request.

## Metrics (orientation)

| Metric | Why it matters |
|--------|----------------|
| MRR / ARR | Recurring revenue baseline |
| Logo / revenue churn | Retention health |
| LTV | Long-run customer value |
| CAC | Acquisition efficiency |
| LTV:CAC | Unit economics (context-heavy; not a universal 3:1 law) |
| Net revenue retention | Expansion vs churn |
| Trial → paid | Funnel quality |

## Common mistakes

- Suspend instantly on first failed payment with no grace/dunning
- One failure email and silence
- Wrong proration mental math (always preview)
- Monthly-only catalog when annual would retain better
- Ambiguous “end of day” without timezone (prefer UTC or explicit offsets)
