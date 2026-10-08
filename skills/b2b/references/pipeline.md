# Pipeline Management — B2B

Load for coverage math, stage hygiene, stalled-deal recovery, and forecast categories. Metrics below are **decision aids**; substitute the team’s measured win rate and cycle length whenever available.

## Pipeline coverage (compute, don’t assume 3×)

**Definition:** how much open pipeline revenue is needed to hit a target, given win rate and how fast pipeline turns.

Salesforce’s modern coaching math (Jack Keenan, Salesforce Blog) rejects a fixed “3× quota” rule. 3× only fits a ~33% revenue win rate with a ~one-year cycle. Prefer:

```text
Pipeline needed ≈ Annual quota ÷ revenue win rate ÷ (365 ÷ sales cycle days)
```

Example from that guidance: `$100,000 ÷ 25% ÷ (365 ÷ 60) ≈ $65,757` of open pipeline—not 3× quota—when the cycle is ~60 days.

| Input | Source |
|-------|--------|
| Quota | User / company target for the period |
| Revenue win rate | Closed-won revenue ÷ pipeline revenue that was worked (team or rep actuals) |
| Cycle length | Median days first meaningful touch → close |

If win rate or cycle is unknown, ask for them or present a small scenario table instead of asserting a universal 3–4× “healthy range.”

## Other health metrics (define the cohort)

| Metric | Formula sketch | Notes |
|--------|----------------|-------|
| Win rate | Closed-won ÷ total closed (or revenue analog) | State time window and whether pulled-in deals count |
| Average cycle | Days first touch → close for won deals | Segment by segment/ACV when mixed |
| ASP / ACV | Revenue ÷ deals won | Watch mix shift before celebrating lifts |
| Slippage | Commit deals that miss the commit date | Track rate and reason codes; no universal “&lt;20%” law |

## Weighted pipeline

```text
Deal value × probability = weighted value
```

Replace default CRM percentages with **observed stage conversion** and deal-specific signals (economic-buyer access, paper process, multi-threading).

## Stage hygiene checklist

| Stage label (example) | Evidence that belongs |
|-----------------------|------------------------|
| Qualified | ICP fit + early BANT/MEDDIC signals |
| Discovery | Pain documented; stakeholders partially mapped |
| Demo / Eval | Technical validation scheduled with the right roles |
| Proposal | Commercial path credible; decision process clear |
| Negotiation | Economic buyer engaged; timeline mutual |
| Verbal | Written confirmation path; paperwork moving |

Mis-staged deals corrupt forecasts—move stage only when evidence exists.

## Review signals (calibrate thresholds)

Use as **prompts for inspection**, then adjust to team baselines:

| Signal | Default inspection trigger | If user supplies baseline |
|--------|----------------------------|---------------------------|
| Inactivity on an “active” opp | ~14 days with no meaningful touch | Use team SLA |
| Discovery dwell | ~60 days without progress | Use median time-in-stage |
| Zombie risk | ~2× median cycle, weak activity | Use org zombie definition |
| Single-threaded | Only one engaged contact | Require second thread before commit |
| Stalled | No dated next step | Set or drop from commit |
| Champion dark | Main advocate unresponsive | Multi-thread + re-qualify pain |
| Scope creep | Requirements expand without commercial commit | Re-anchor metrics and paper process |

## Pipeline review questions

1. When did we last speak with them, and who was in the room?
2. What is the next step, owner, and date?
3. Have we reached the economic buyer?
4. What could kill this deal (competition, status quo, paper process)?
5. What must be true to close by the stated date?

## Forecast categories

| Category | Meaning |
|----------|---------|
| **Commit** | High confidence for this period; evidence supports close path |
| **Best case** | Could close if named upside events occur |
| **Pipeline** | Real work remains; not this period |
| **Omit** | Remove from the forecast conversation |

Accuracy depends on honest categorization and the coverage math above—not on optimistic stage names.
