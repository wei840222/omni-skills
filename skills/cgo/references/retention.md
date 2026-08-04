# Retention and Engagement

## Retention Benchmarks (2024-2026)

### SaaS B2B Revenue Retention

| Metric | Median | Top Quartile | Trend |
|--------|--------|--------------|-------|
| Gross Revenue Retention (GRR) | 88% | 93%+ | Down from 90% three years ago |
| Net Revenue Retention (NRR) | 101% | 115%+ | Compression from expansion slowdown |

Top PLG companies (Slack, Notion, Figma) achieve NRR 120%+ through self-serve expansion.

### Mobile App Retention (Adjust 2024)

| Type | D1 | D7 | D30 |
|------|-----|-----|------|
| Mobile games (median) | 25% | 6% | 2% |
| Mobile games (top 10%) | 40%+ | 15%+ | 8%+ |
| Social apps | 30-40% | 12-18% | 5-8% |
| Utility apps | 20-30% | 8-12% | 3-5% |

### E-commerce Repeat Purchase

- Median repeat purchase rate: 20-27% within 12 months
- Top DTC brands: 40%+ repeat rate
- Average order value globally: $150-180 (2025), up 5-8% YoY

### SaaS User Retention (Product Usage)

| Product Type | D1 | D7 | D30 | D90 |
|-------------|-----|-----|------|------|
| B2B SaaS (high-value) | 60% | 40% | 25% | 15% |
| Consumer SaaS | 35% | 18% | 8% | 3% |
| Marketplace (buyer) | 25% | 12% | 5% | 2% |

## Retention Framework

### Time-Based Cohorts
- **Day 1** — First session completion, core action taken
- **Week 1** — Return visits, habit signals
- **Month 1** — Sustained usage, feature depth
- **Long-term** — Plateau identification, power user patterns

### Leading Indicators of Retention
- Users who complete 3+ core actions in first session retain 2-3x better
- Time-to-first-value < 5 minutes correlates with D30 retention lift of 15-25%
- Feature adoption breadth (not depth) predicts long-term retention
- "Aha moment" varies by product — find it through behavioral cohort analysis, not assumptions

## Engagement Levers

### Habit Formation
- **Trigger** — External (notification) or internal (emotion) cue
- **Action** — Simple behavior with low friction
- **Variable reward** — Unpredictable positive outcome
- **Investment** — User effort that increases future value (stored data, reputation, integrations)

### Re-engagement
- **Email sequences** — Onboarding drips, win-back campaigns
- **Push notifications** — Personalized, timed, limited frequency
- **In-app triggers** — Feature announcements, usage milestones
- **Retargeting** — Bring back churned or dormant users

## Churn Analysis

### Warning Signals
- Usage frequency decline (most predictive: 2-week drop in daily users)
- Feature breadth narrowing (users stop exploring)
- Support ticket patterns (sudden spike = product issue; gradual = competitive loss)
- Payment failures (involuntary churn = 20-40% of total churn in subscription businesses)
- Integration disconnections (removing Slack/CRM integrations signals intent to leave)

### Intervention Timing
- **Early signals** — Proactive outreach, feature education (within 48h of signal)
- **At-risk** — Personalized offers, success calls (usage down 50%+ over 2 weeks)
- **Churned** — Win-back campaigns, exit surveys (within 7 days of churn)

### Involuntary Churn Prevention
- Dunning sequences: retry at 1h, 24h, 72h, 7d with smart retry logic
- Payment method updater (Stripe Card Updater, Braintree token network)
- Pre-expiry notification emails 30/14/7 days before card expiration

## Activation Connection

Retention problems often trace to activation failures:
- Users who don't reach aha moment churn 3-5x faster
- First session depth predicts long-term retention better than session count
- Onboarding friction creates false churn signals (users who never complete setup aren't "churned" — they never started)
- Fix activation before optimizing retention campaigns

## 🔴 Failure Modes and Recovery

### If retention is declining but you don't know why:
1. **Check activation first** — Are new users reaching aha moment? If not, fix onboarding before retention campaigns
2. **Segment by cohort** — Is the problem with new users (activation) or existing users (engagement)?
3. **Analyze leading indicators** — Track time-to-first-value, feature adoption breadth, session depth
4. **Check involuntary churn** — Payment failures = 20-40% of subscription churn; implement dunning sequences

### If retention campaigns aren't working:
1. **Timing mismatch** — Are you reaching users before or after they've decided to leave? Target within 48h of signal
2. **Wrong segment** — Are you targeting users who never activated? Fix activation first
3. **Generic messaging** — Are you sending the same message to all at-risk users? Segment by churn reason
4. **Channel fatigue** — Are you over-using one channel? Rotate email, push, in-app, retargeting

### If you can't measure retention properly:
1. **Define "active" clearly** — Is it login, core action, or value delivery? Use the metric that predicts long-term retention
2. **Check cohort quality** — Are you comparing apples to apples? Control for seasonality, marketing campaigns, product changes
3. **Leading vs lagging** — If you only track D30 retention, you're reacting too late. Track D1, D7, and leading indicators

## ❌ Anti-Patterns (Do NOT Do These)

❌ **Optimizing retention before fixing activation** — You're filling a leaky bucket. Fix the hole first.

❌ **Using generic retention benchmarks** — A 40% D1 for social apps is median, not good. Context matters (product type, user source, geography).

❌ **Ignoring involuntary churn** — Payment failures, expired cards, and failed renewals = 20-40% of churn. Implement dunning before retention campaigns.

❌ **Sending retention emails to users who never activated** — They're not "at-risk," they never started. Fix onboarding first.

❌ **Measuring retention by login** — Login ≠ value. Track core actions that predict long-term retention (e.g., "created 3 projects" for project management tools).

❌ **Reacting to D30 retention** — By then, users have already left. Track D1, D7, and leading indicators (time-to-first-value, feature adoption).

❌ **Treating all churn the same** — Segment by churn reason (product issue, competitive loss, involuntary, never activated). Each needs different intervention.

