---
name: retention
description: >
  Diagnose user and revenue retention with cohort definitions, churn signals,
  lifecycle engagement, cancel-flow design, and reactivation campaigns. Use when
  the user asks for retention or churn analysis, cohort tables, NRR/GRR, stickiness,
  win-back or dunning plans, or lifecycle stage tactics. Not for generic growth
  acquisition planning without a retention question (growth), pure billing setup
  without churn diagnosis (paddle / subscriptions), or broad product strategy with
  no retention metric (product / product-manager).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔒"}'
  related-skills: '{"analytics":"Broader measurement design when retention is one slice of a full analytics system.","email-marketing":"Campaign drafting, cadence, and deliverability once a reactivation audience is approved.","growth":"Acquisition and growth-model tradeoffs after retention constraints are clear.","metrics":"Metric taxonomy and dashboard hygiene beyond retention-specific formulas.","mobile-app-analytics":"Mobile-specific event and session retention when the product is an app.","onboarding":"Activation and aha-moment design that feeds early retention cohorts.","paddle":"Subscription billing, dunning, and involuntary churn operations for Paddle-billed products.","pricing":"Packaging and expansion levers that change NRR after retention diagnosis.","product":"Product discovery and roadmap framing when retention findings become product work.","product-manager":"PM prioritization and experiment design around retention hypotheses.","saas":"SaaS operating context when retention is part of a broader SaaS health review.","subscriptions":"Plan, renewal, and subscription-lifecycle mechanics adjacent to churn handling."}'
---

## When to load

| Need | Resource |
| --- | --- |
| Benchmarks, NRR formula citations, source windows | `references/sources.md` |
| Evaluation harness only | `test-prompts.json` |

## Operating sequence

1. **Lock definitions** before comparing numbers: unit (user, account, subscriber), activity event, cohort anchor (signup vs activation vs first paid), return window, and observation maturity.
2. **Choose the question**: early product retention, logo/revenue churn, NRR/GRR, feature stickiness, cancel friction, or reactivation.
3. **Build one cohort view** with segmentation (channel, plan, persona). Do not average power users into a single curve.
4. **Separate voluntary vs involuntary churn** and tenure vs inactivity before prescribing campaigns.
5. **Form one testable hypothesis** (metric → segment → cause → intervention) with success metric and stop rule.
6. **Draft outputs** the user can act on: table layout, signal checklist, cancel-flow copy, or campaign brief. Before any external send, billing change, or data deletion, pause for explicit user approval, then continue with the approved action only.
7. Load `references/sources.md` when citing benchmarks, formulas, or external ranges so dated windows stay attached to sources.

## Core metrics

Define the cohort and return event first. Formulas without those anchors are not comparable.

| Metric | Formula | Notes |
| --- | --- | --- |
| Day *n* retention | Users in cohort who meet the activity definition on day *n* ÷ cohort size | State whether day 0 is signup or activation. Do not publish a universal “healthy D30” band without a matching source window and product class. |
| Rolling retention | Users active in window *W* who were also active in the eligible baseline window ÷ eligible baseline users | Prefer retained intersection over population ratios such as WAU÷WAU. |
| Logo churn | Customers lost in period ÷ customers at period start | State period length (month/quarter/year). |
| Revenue churn (gross) | Recurring revenue lost to churn and contraction ÷ starting recurring revenue of the same cohort | Excludes expansion. |
| NRR (net revenue retention) | (Starting cohort recurring revenue + expansion − contraction − churned cohort revenue) ÷ starting cohort recurring revenue | Same starting customer set only; exclude newly acquired logos in the period. Often annualized for investor comps. |
| GRR (gross revenue retention) | (Starting cohort recurring revenue − contraction − churned cohort revenue) ÷ starting cohort recurring revenue | Cannot exceed 100%; useful when NRR hides logo loss. |

### Benchmark framing (dated sources)

Treat published bands as orientation, not targets:

- **User retention comps (Lenny Rachitsky with Casey Winters, 2020-06-09)** ask experts for **6-month user retention** and **12-month NRR**, not D30. Illustrative GOOD→GREAT **6-month user retention**: consumer social ~25%→~45%; consumer transactional ~30%→~50%; consumer SaaS ~40%→~70%; SMB/mid-market SaaS ~60%→~80%; enterprise SaaS ~70%→~90%. Illustrative GOOD→GREAT **12-month NRR**: consumer SaaS ~55%→~80%; bottom-up SaaS ~100%→~120%; land-and-expand SMB/mid-market ~90%→~110%; enterprise ~110%→~130%. Denominators and “active” definitions vary by expert; restate the window when citing.
- **SaaS logo/revenue churn (Paddle)** stresses that averages disagree by industry, ARPU, contract length, and stage. Paddle summarizes many studies as roughly **~5% median monthly** context with a wide band, and notes early PMF-seeking products can see much higher monthly churn. Prefer peer set + contract length over a single universal monthly target.
- **NRR interpretation (Stripe)** : >100% means existing customers expand enough to offset loss; 80–100% often needs churn and expansion diagnosis together; high NRR can still hide logo churn—pair with GRR and logo churn.

When the user asks “is D30 good?”, answer with definition checks first, then either compute from their data or explain that popular public comps are often **multi-month**, not D30.

## Cohort analysis

Track by **signup (or activation) cohort**, not only calendar week:

- Horizontal: periods since cohort anchor (0, 1, 2, …)
- Vertical: cohort labels (Jan W1, …)
- Cell: % of that cohort still meeting the activity definition

Look for:

- Cohorts that retain better after product or channel changes
- Drop-off cliffs (for example week-2 collapse → aha moment too late)
- Seasonality and segment masks (one channel or plan hiding the rest)

Prefer an **activation-anchored** cohort when signup includes many never-activated users; report both if stakeholders disagree.

## Churn signals

Flag risk **before** cancel when baseline-relative signals appear:

- Login or session frequency drops sharply from the user’s own baseline
- Core feature usage stops while the account remains billed
- Support spikes then go silent
- Repeated billing-page visits without plan change
- Seat removals or role downgrades
- Data export or bulk download requests
- Payment failures / dunning exhaustion (involuntary path)

Classify each case as **voluntary**, **involuntary** (failed payment, expired card), or **unknown** before choosing save offers vs billing recovery.

## Engagement loops

Retention needs a repeatable loop tied to the product’s natural cadence:

| Loop type | Trigger | Action | Reward |
| --- | --- | --- | --- |
| Personal | Digest or streak cue | Review updates | Visible progress |
| Social | Peer activity | Respond | Recognition |
| Content | New relevant item | Consume | Useful knowledge |
| Progress | Goal threshold | Complete step | Streak or status |

Calibrate frequency to real usage (daily tool ≠ monthly billing product). Variable rewards help only when the core job is already valuable.

## Lifecycle stages

Stages are product-dependent. Use the table as a planning scaffold, not a fixed calendar:

| Stage | Typical focus | Goal | Example tactics |
| --- | --- | --- | --- |
| Activation | First sessions | Reach aha / first value | Onboarding, setup checklist |
| Engagement | Early repeat use | Habit / routine | Tips tied to jobs-to-be-done |
| Retention | Ongoing value | Stable return behavior | Feature discovery, health checks |
| Expansion | Proven value | Depth or seats | Upsell only after usage evidence |
| Reactivation | After inactivity or cancel | Earned return | Win-back with new value + easy path |

## Reactivation campaigns

**Tenure ≠ inactivity.** “Churning after three months of tenure” is not automatically “90 days inactive.” Define inactivity as time since last qualifying activity (or cancel date) before picking a cadence.

Example **inactivity** ladder (adjust to product cadence; not universal law):

- Soft check-in after short inactivity
- Value + what’s-new after prolonged inactivity
- Incentive only when policy and margin allow
- Final feedback ask before suppression

Message shape:

```text
[Acknowledge absence] + [Concrete new value] + [One-click re-entry]
```

Campaign guardrails:

- Consent, legal basis, and channel preference
- Suppression list (unsubscribed, bounced, do-not-contact)
- Frequency cap and stop-on-return
- Separate tracks for voluntary cancel vs payment failure
- **Ask before send** for customer email/SMS/push from this skill

## Feature stickiness

Measure association carefully:

1. Define retained outcome and exposure window.
2. Compare users with vs without the feature **in the same cohort and segment**.
3. Check confounders (plan, tenure, acquisition source, company size).
4. Treat lift as a **hypothesis** until validated; do not quote generic “2× / 3× / 5×” multipliers without the user’s data.

Prioritize sticky features in onboarding only after the association survives basic controls.

## Churn prevention

When a risk signal fires:

1. In-product help tied to the failed job (not generic guilt copy)
2. Human follow-up only with clear ownership and user-approved channel
3. Billing recovery path for involuntary churn (update payment, retry, dunning)
4. Pre-renewal usage summary for accounts with declining value realization

### Cancel flow

Keep cancellation **reachable in a few steps**:

- Offer optional reason capture (not a hard gate that blocks cancel)
- Offer pause or plan-change when it truly fits the job
- Show concrete loss (data, seats, price lock) without dark patterns
- State only **verified** retention/deletion policy for data after cancel
- Provide a clear reactivation path when policy allows

## Common mistakes

- Measuring retention from raw signup when the product’s value starts at activation
- Mixing voluntary and involuntary churn in one playbook
- Equating account tenure with inactivity windows
- Reactivation mail with no new value and no suppression rules
- Letting NRR look healthy while logo churn rises
- One cohort curve with no segment split
- Mandatory multi-step “save” walls that obstruct cancel

## Near-miss handoffs

- Acquisition engine design without a retention metric → `growth`
- Billing provider dunning implementation → `paddle` / `subscriptions`
- Mobile session graphs and app events → `mobile-app-analytics`
- Full analytics stack design → `analytics` / `metrics`
- Packaging changes after NRR diagnosis → `pricing`
