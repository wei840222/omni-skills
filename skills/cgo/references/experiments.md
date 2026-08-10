# Experimentation Frameworks

## Hypothesis Structure

```
We believe [change]
will result in [outcome]
because [rationale]
measured by [metric]
success threshold [number]
```

## Experiment Types

### A/B Tests
- **Single variable** — Change one thing, measure impact
- **Sample size** — Calculate required users before starting (use power analysis)
- **Duration** — Full business cycles, weekday/weekend coverage (minimum 1-2 weeks)
- **Segmentation** — New vs returning, paid vs free, geography

### Multivariate Tests
- **Multiple variables** — Test combinations simultaneously
- **Higher traffic required** — Need volume for statistical power
- **Interaction effects** — Discover how changes combine
- **Use when** — Testing 3+ variables with sufficient traffic (>100k users/month)

### Sequential Tests (2024-2026 Best Practice)
- **Always-on experiments** — Continuous testing with early stopping rules
- **Multi-armed bandits** — Allocate traffic dynamically to winners while exploring
- **Bayesian approaches** — More intuitive interpretation (probability of B > A)
- **CUPED** — Controlled Experiment Using Pre-Experiment Data to reduce variance
- **When to use** — High-velocity teams, limited traffic, need faster learnings

### Incrementality Testing
- **Holdout groups** — Measure true causal impact vs attribution
- **Ghost ads** — Compare exposed vs unexposed to same ad
- **Intent-to-treat** — Randomize at assignment level, analyze at treatment level
- **When to use** — Validating marketing spend, measuring brand campaigns

## Prioritization Framework

### ICE Score
- **Impact** — How big if it works? (1-10)
- **Confidence** — How sure are you? (1-10)
- **Ease** — How fast to implement? (1-10)
- **Score** — Average of three, rank by score
- **Use when** — Quick prioritization, early-stage teams

### RICE Score
- **Reach** — How many users affected per time period
- **Impact** — How much effect per user (0.25, 0.5, 1, 2, 3)
- **Confidence** — How sure (10%-100%)
- **Effort** — Person-weeks to implement
- **Score** — (Reach × Impact × Confidence) / Effort
- **Use when** — Resource-constrained teams, need to justify investment

### PIRATE Framework (2024)
- **Potential** — How big is the upside?
- **Importance** — How critical to business goals?
- **Readiness** — How ready is the team to execute?
- **Accuracy** — How confident in the hypothesis?
- **Time** — How long until results?
- **Ease** — How simple to implement?

## Statistical Rigor

### Before Launch
- Define primary metric (one per experiment)
- Calculate sample size needed (power analysis: 80% power, 5% significance)
- Set experiment duration (minimum 1-2 full business cycles)
- Document hypothesis and success criteria
- Pre-register experiment (share with team before starting)

### During Experiment
- No peeking with decisions (check data quality only)
- Monitor for bugs/errors (not significance)
- Document unexpected events (outages, holidays, competitive moves)
- Use sequential testing if you need to check early (pre-defined stopping rules)

### After Experiment
- Statistical significance check (p < 0.05 or Bayesian probability > 95%)
- Practical significance check (is the effect size meaningful for business?)
- Segment analysis (did it work for all user types?)
- Document learnings (even failed experiments teach something)
- Share results widely (build experimentation culture)

## Velocity Optimization

- **Test ideas, not perfection** — 80% solutions ship faster
- **Parallel experiments** — Multiple tests in different areas (avoid overlap)
- **Reusable infrastructure** — Feature flags, analytics, dashboards
- **Learning loops** — Failed tests still generate knowledge
- **Experiment backlog** — Maintain prioritized list of hypotheses
- **Democratize testing** — Enable product managers, designers to run experiments

## Common Pitfalls

- **Peeking problem** — Checking significance daily inflates false positive rate
- **Multiple comparisons** — Testing many metrics increases false discovery
- **Novelty effect** — Short-term lift from new feature, not real improvement
- **Seasonality bias** — Running tests during holidays or special events
- **Underpowered tests** — Too few users to detect meaningful difference
- **Stopping too early** — Calling winner before reaching sample size

## 🔴 Failure Modes and Recovery

### If experiments aren't showing significant results:
1. **Check sample size** — Did you reach the calculated sample size? If underpowered, extend duration or accept smaller effect size
2. **Check test duration** — Did you run for full business cycles? If too short, extend to 2+ weeks
3. **Check effect size** — Is the change too small to detect? Either increase sample size or test a bigger change
4. **Check variance** — Is there high variance in your metric? Use CUPED or segment analysis to reduce noise

### If you're running too many experiments:
1. **Check overlap** — Are tests interfering with each other? Use holdout groups or stagger launches
2. **Check prioritization** — Are you testing low-impact ideas? Use ICE/RICE to focus on high-potential hypotheses
3. **Check resources** — Do you have enough traffic/users? If limited, use sequential testing or bandit algorithms
4. **Check learning velocity** — Are you learning from each test? Document results and build on prior learnings

### If experiments show positive results but don't ship well:
1. **Check novelty effect** — Is the lift from curiosity or real value? Wait 2-4 weeks to see if effect persists
2. **Check segment variation** — Did it work for all user types? If only one segment, consider targeted rollout
3. **Check practical significance** — Is the effect size meaningful for business? A 0.1% lift may not justify the change
4. **Check implementation quality** — Did the production version match the test version? Audit for bugs or differences

## ❌ Anti-Patterns (Do NOT Do These)

❌ **Peeking at results daily** — You'll inflate false positive rate. Use sequential testing if you need early checks.

❌ **Running underpowered tests** — If you can't reach sample size, either test a bigger change or use sequential methods. Don't call a winner prematurely.

❌ **Ignoring novelty effect** — Short-term lifts from new features often fade. Wait 2-4 weeks before declaring success.

❌ **Testing during holidays or special events** — Seasonality biases results. Run tests during normal periods or control for seasonality.

❌ **Stopping tests early because they're "winning"** — You haven't reached sample size yet. Let the test run to completion.

❌ **Running multiple tests on the same users without holdouts** — Tests interfere with each other. Use holdout groups or stagger launches.

❌ **Optimizing for statistical significance without checking practical significance** — A 0.1% lift may be statistically significant but not business-meaningful.

❌ **Not documenting failed experiments** — Failed tests teach valuable lessons. Document hypotheses, results, and learnings.
