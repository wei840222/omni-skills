---
name: b2c
description: >
  Design consumer product strategy: validate demand, choose monetization, set
  activation and retention kill metrics, size CAC/LTV/payback with explicit
  denominators, and pick growth loops before scaling spend. Use when the user
  is building or diagnosing a B2C app, freemium/trial paywall, consumer SaaS,
  casual game, marketplace consumer side, or unit-economics review. Not for
  enterprise B2B deal qualification (`b2b`), pure CRM hygiene (`crm`), or
  multi-account campaign copy without a product strategy question (`outreach`).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📱"}'
  related-skills: '{"b2b":"Enterprise deal qualification, MEDDIC, and pipeline judgment when the customer is a company buying committee rather than end consumers.","growth":"Channel experiments and growth-program execution after the B2C stage, loop, and kill metrics are already chosen.","pricing":"Detailed price-point research and packaging math once the monetization model is selected.","retention":"Deep retention diagnostics and cohort instrumentation once stage priorities point at habit formation.","saas":"SaaS operating playbooks that span B2B and B2C once consumer-specific economics are already framed.","product":"General product discovery and roadmap craft adjacent to consumer-specific monetization and loops."}'
---

## When to use

Load for **consumer (B2C) product and growth judgment**:

- Pre-PMF activation, aha-moment design, and first-session value
- Monetization model choice (freemium, trial, subscription, hybrid) and paywall timing
- Unit economics: CAC, LTV, payback, LTV:CAC with stated denominators
- Growth-loop selection before scaling paid acquisition
- Category retention benchmarks and kill metrics by stage

Adjacent non-triggers (stay with the sibling skill instead):

- Enterprise multi-threaded deal strategy without a consumer product question → `b2b`
- Campaign sequences across many accounts with no product/loop decision → `outreach` / `growth`
- CRM import or Salesforce API work → `crm` / other systems skills

## Scope

Knowledge-only coaching. This skill does **not** own persistent product analytics state, billing configuration, or ad-account credentials. Ask for measured inputs; do not invent cohort rates, spend, or revenue.

## Primary workflow

Execute in order. Stop early when a missing input blocks a safe recommendation.

1. **Classify the ask** — demand validation, monetization/paywall, activation/retention, unit economics, growth loop / channel, or stage priority.
2. **Inventory known facts** — category, stage (pre-PMF / post-PMF / scaling), platform (mobile / web), monetization model, measured D1/D7/D30 or M6 retention, conversion definition, ARPU, spend, **new paying customers** (not installs alone), payback target, funding posture. Label unknowns explicitly.
3. **Load only the reference that owns the bottleneck**:

| Bottleneck | Load |
|------------|------|
| Monetization model, paywall placement, price anchors | `references/monetization.md` |
| CAC / LTV / payback formulas and channel tables | `references/economics.md` |
| Growth loop types and first-100-user tactics | `references/growth.md` |
| Category retention / conversion / NRR ranges | `references/benchmarks.md` |
| Verified sources used in this package | `references/sources.md` |

4. **Apply core operating rules** (below) to the known facts.
5. **Produce an evidence-bound output** — recommendation, missing-data asks, kill metric, and one next measurement or experiment. If benchmarks are used, state cohort window, category, and whether figures are hypotheses vs measured. If the user cannot supply spend or paying-customer counts, refuse CAC claims and list the exact inputs needed.

## Core rules

### 1. Stage-aware priorities

| Stage | Focus | Default kill / target signal |
|-------|-------|------------------------------|
| Pre-PMF | Activation + retention | Habit signal weak (e.g. D7 far below category “good”; M6 user retention not approaching Lenny/Casey consumer bands) → fix product before scale |
| Post-PMF | Acquisition + conversion | CAC payback longer than funding posture allows (often ~6 mo venture / tighter if bootstrapped) |
| Scaling | LTV optimization + loops | LTV:CAC sustainably under ~3:1 after contribution-margin clarity → optimize monetization/retention before more paid |

Treat table numbers as **decision heuristics**, not universal laws. Prefer the user’s measured cohorts over any published band.

### 2. Thirty-second first session

Consumer products often win or lose in the first session surface:

1. Is there a hook (emotional trigger, curiosity, concrete benefit)?
2. How many steps to first value (target: ≤3 meaningful actions)?
3. Is account creation deferred until after value is shown when legally and product-wise feasible?

### 3. Critical metrics (define denominators)

- **Activation**: % reaching a named aha moment in the first session (define the event).
- **Retention**: D1 / D7 / D30 and, when available, **month-6 user retention** by acquisition cohort.
- **Monetization**: trial or freemium → paid conversion, ARPU, payback period.
- **Referral**: invites × conversion (K-factor); organic vs paid mix.
- **CAC denominator**: `Total fully loaded acquisition spend / New paying customers` unless the user explicitly asks for cost-per-install. Never silently mix installs with payers.
- **LTV / payback**: state whether LTV is revenue or **contribution margin** after COGS, payment fees, and variable support. Payback = CAC / monthly contribution (or ARPU only if margin ≈ ARPU and stated).

### 4. Decision support sequence

For any B2C decision:

1. Validate demand with real complaints or willingness-to-pay signals.
2. Choose monetization model before obsessing over a single price point.
3. Name the activation moment in observable events.
4. Design at least one compounding loop; paid-only acquisition does not compound.
5. Set kill metrics before scaling spend.

### 5. Anti-patterns → preferred moves

| Instead of | Do |
|------------|----|
| Building only for power users | Design the default path for the casual majority who fund the business |
| Generous freemium that fully solves the job | Cap free at a natural limit or use trial so paid value is visible |
| MAU without an “active” definition | Define active event, then report retention on that event |
| B2B-style long demos for consumers | Show value fast; defer heavy onboarding |
| Ignoring emotion (status, FOMO, delight) | Pair rational benefit with a felt hook in the first session |
| Late paywall after free habit hardens | Place paywall after aha, at a natural limit, with a clear upgrade path |
| Scaling ads before retention flattens | Fix activation/retention until cohorts stabilize in-category |
| CAC from installs while LTV from payers | Recompute CAC on **new paying customers** or label CPI separately |

## Output contract

Return:

1. **Situation read** — stage, category, model, what is measured vs unknown.
2. **Recommendation** — one primary move (product, monetization, or loop), not a laundry list.
3. **Economics check** — formulas with denominators; mark unverifiable math as blocked.
4. **Kill / success metric** — explicit threshold and time window the user can instrument.
5. **Next ask or experiment** — the smallest measurement or test that would change the decision.
6. **Sources** — cite package references and external URLs only when claims need them; prefer `references/sources.md`.

## Reference routing

| Topic | File | Load when |
|-------|------|-----------|
| Monetization models & paywall design | `references/monetization.md` | Model choice, trial vs freemium, price anchors, paywall timing |
| Unit economics (CAC, LTV, payback) | `references/economics.md` | Spend efficiency, channel CAC, churn math, LTV:CAC |
| Growth loops & acquisition channels | `references/growth.md` | Loop design, channel matrix, first 100 users |
| Retention & conversion benchmarks | `references/benchmarks.md` | Comparing D1/D7/D30/M6 or conversion bands by category |
| Research sources | `references/sources.md` | Need provenance, dates, or claim disposition |
