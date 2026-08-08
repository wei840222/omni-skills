# Growth Metrics and Analysis

## North Star Metrics

### By Business Model (2024-2026 Examples)

| Model | North Star | Why | Real Examples |
|-------|------------|-----|---------------|
| SaaS | Weekly active users | Usage predicts retention | Slack: DAU, Notion: weekly active teams |
| Marketplace | GMV / transactions | Core value exchange | Airbnb: nights booked, Uber: rides/week |
| Media | Time spent | Attention monetization | Spotify: time listening, Netflix: hours streamed |
| E-commerce | Orders per period | Revenue driver | Amazon: orders/customer/year |
| Social | DAU/MAU ratio | Engagement intensity | Facebook: DAU, Instagram: daily time spent |
| PLG B2B | Activated teams/week | Self-serve conversion signal | Figma: active files, Miro: collaborative boards |

### North Star Criteria
- Measures value delivered to users
- Leading indicator of revenue
- Actionable by the team
- Simple to understand
- Not easily gameable

### North Star Anti-Patterns
- Revenue as north star (lagging, not actionable by product team)
- DAU without quality signal (bots, accidental opens)
- Metrics that plateau early (total signups)
- Metrics the team can't influence

## Funnel Metrics

### AARRR Framework
- **Acquisition** — How users find you (traffic, signups)
- **Activation** — First value moment (onboarding completion, aha moment)
- **Retention** — Users come back (DAU/WAU/MAU, cohort curves)
- **Revenue** — Users pay (conversion rate, ARPU, LTV)
- **Referral** — Users invite others (viral coefficient, NPS)

### Modern Funnel: AAARRR (Adding "A" for Awareness)
- **Awareness** — Target audience knows you exist
- **Acquisition** — They sign up or visit
- **Activation** — They experience value
- **Retention** — They come back
- **Revenue** — They pay
- **Referral** — They tell others

## Unit Economics

### Customer Acquisition Cost (CAC)
```
CAC = Total acquisition spend / New customers acquired
```

### Lifetime Value (LTV)
```
LTV = ARPU × Gross margin × Average customer lifespan
```

### Unit-economics interpretation

Interpret LTV:CAC and payback only after defining the acquisition-cost scope, gross/contribution margin, retention model, attribution method, segment, and cash constraint. A ratio or payback value is a decision input, not a universal health classification. When using an external benchmark, retain its source URL, publication date, population, geography, and metric definitions alongside the comparison.

```
Payback months = CAC / (ARPU × Gross margin)
```

## Cohort Analysis

### Building Cohorts
- Group users by signup week/month
- Track behavior over time
- Compare cohorts to each other

### What to Look For
- Retention curve shape (steep drop vs gradual)
- Plateau point (where retention stabilizes)
- Cohort improvements (are new users better retained?)
- Seasonal effects (holiday cohorts differ)

### Leading Indicator Cohorts (2024-2026 Practice)
- Identify behaviors in first session that predict long-term retention
- Example: "Users who invite 1 teammate in first week retain 3x better"
- Use these as activation milestones, not just vanity metrics
- Validate with holdout: do users who complete the behavior actually retain better?

### Predictive Cohort Analysis
- Track leading indicators (activation, engagement depth) alongside lagging (retention, revenue)
- Build early-warning dashboards: if leading indicators drop, retention will follow in 2-4 weeks
- Use for experiment evaluation: measure leading indicator lift, predict long-term impact

## Modern Attribution (2024-2026)

### Beyond Last-Touch
- **Multi-touch attribution** — Distribute credit across touchpoints
- **Incrementality testing** — Measure true causal impact (holdout groups, ghost ads)
- **Causal inference** — Use statistical methods to isolate channel impact
- **When to use what** — Attribution for optimization, incrementality for budget validation

### Attribution Pitfalls
- Last-touch over-credits bottom-of-funnel (search, retargeting)
- First-touch over-credits awareness (brand, content)
- Attribution models assume all tracked conversions are caused by ads (they're not)
- Always validate with incrementality testing on your biggest spend channels

## Dashboard Essentials

### Weekly Review
- North star metric trend
- Funnel conversion rates
- Acquisition by channel
- Retention cohort update
- Experiment results

### Monthly Deep Dive
- Unit economics health (LTV:CAC, payback)
- Channel performance comparison
- Segment analysis
- Growth model accuracy
- Forecast vs actual

## 🔴 Failure Modes and Recovery

### If your north star metric isn't driving growth:
1. **Check if it's a lagging indicator** — Revenue, total signups, or cumulative metrics plateau early and don't drive action. Switch to leading indicators (weekly active users, activation rate, time-to-first-value)
2. **Check if it's actionable** — Can your team actually influence this metric? If not, pick something more proximal to your work
3. **Check if it measures value delivery** — Does this metric reflect users getting value? DAU without quality signal (bots, accidental opens) is meaningless
4. **Check if it's easily gameable** — Can teams optimize for the metric without improving real outcomes? Add guardrails (e.g., "weekly active users" + "retention rate")

### If LTV:CAC looks unhealthy but you're not sure why:
1. **Check LTV calculation** — Are you using gross margin or revenue? Are you including expansion revenue? Are you using actual customer lifespan or assuming infinite retention?
2. **Check CAC calculation** — Are you including all costs (salaries, tools, overhead) or just ad spend? Are you amortizing correctly?
3. **Check cohort quality** — Are you averaging across all customers? Segment by acquisition channel, customer type, or time period to find where unit economics break down
4. **Check payback period** — Even with good LTV:CAC, if payback is >18 months you may have cash flow problems. Optimize for faster payback (self-serve, annual plans, expansion)

### If cohort analysis isn't giving you actionable insights:
1. **Check cohort definition** — Are you grouping by signup date only? Add behavioral cohorts (activated vs not, feature adoption depth, acquisition channel)
2. **Check time horizon** — Are you looking at D1/D7/D30 only? For B2B SaaS, you need D90/D180 to see real retention patterns
3. **Check leading indicators** — Are you waiting for retention data before acting? Track activation metrics and engagement depth as early signals (2-4 week lead time)
4. **Check segment variation** — Are you averaging across all users? Segment by acquisition channel, user type, or product version to find where retention breaks down

### If attribution is misleading your channel decisions:
1. **Check for last-touch bias** — Are you over-crediting bottom-of-funnel channels (search, retargeting)? Implement multi-touch attribution or incrementality testing
2. **Check for organic credit** — Are attribution models claiming organic conversions as paid? Use holdout groups to measure true incrementality
3. **Check for channel interaction** — Are you treating channels as independent? Users touch multiple channels; measure combined effect, not isolated ROI
4. **Check for seasonality** — Are you attributing holiday spikes to recent campaigns? Compare to same period last year and use control groups

## ❌ Anti-Patterns (Do NOT Do These)

❌ **Using revenue as your north star** — It's lagging, not actionable by product teams, and easily manipulated by pricing or one-time deals. Use leading indicators like weekly active users or activation rate.

❌ **Calculating LTV without gross margin** — Revenue ≠ profit. If your gross margin is 60%, your real LTV is 60% of what the formula says. Always include margin.

❌ **Averaging LTV:CAC across all customers** — This hides where unit economics break down. Segment by acquisition channel, customer type, and time period.

❌ **Using last-touch attribution for channel decisions** — It over-credits bottom-of-funnel and under-credits awareness. Use multi-touch or incrementality testing.

❌ **Ignoring payback period** — Even with good LTV:CAC, if payback is >18 months you have cash flow problems. Optimize for faster payback.

❌ **Waiting for D30 retention before acting** — By then it's too late. Track D1/D7 and leading indicators (activation, engagement depth) as 2-4 week early signals.

❌ **Using DAU without quality signal** — Bots, accidental opens, and one-time users inflate DAU. Combine with retention rate or engagement depth metrics.

❌ **Treating attribution models as truth** — They assume all tracked conversions are caused by ads (they're not). Validate with incrementality testing on your biggest spend channels.
