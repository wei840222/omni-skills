# Retention & conversion benchmarks

Load when comparing measured cohorts to published bands. **Always prefer the user’s cohort curves.** Published numbers are orientation, not targets carved in stone.

## How to read this file

1. Match **category** (social, transactional, consumer SaaS, gaming, etc.).
2. Match **window** (D1/D7/D30 habit vs month-6 user retention vs 12-month NRR).
3. Match **denominator** (install → open, signup → activated, trial → paid).
4. If the source window differs from the user’s metric, say so — do not silently equate D7 with M6.

## Month-6 user retention (research-backed orientation)

From Lenny Rachitsky with Casey Winters and a panel of growth practitioners (*What is good retention?*, 2020) — **user retention at ~6 months**:

| Business type | GOOD (approx.) | GREAT (approx.) |
|---------------|----------------|-----------------|
| Consumer social | ~25% | ~45% |
| Consumer transactional | ~30% | ~50% |
| Consumer SaaS | ~40% | ~70% |
| SMB / mid-market SaaS | ~60% | ~80% |
| Enterprise SaaS | ~70% | ~90% |

Source: https://www.lennysnewsletter.com/p/what-is-good-retention-issue-29

### Net revenue retention at ~12 months (same research)

| Business type | GOOD (approx.) | GREAT (approx.) |
|---------------|----------------|-----------------|
| Consumer SaaS | ~55% | ~80% |
| Bottom-up SaaS | ~100% | ~120% |
| Land-and-expand VSB SaaS | ~80% | ~100% |
| Land-and-expand SMB / mid-market | ~90% | ~110% |
| Enterprise SaaS | ~110% | ~130% |

NRR > 100% implies expansion outpaces churn/contraction. Consumer SaaS “good” NRR can sit well below 100% in that research set — do not grade a consumer sub with enterprise NRR expectations.

## Short-window mobile habit tables (legacy package heuristics)

These D1/D7/D30 grids shipped with the original skill as **category heuristics** for early habit. They are **not** the same study as the M6 table above. Use them only for early-warning conversations when M6 is unavailable, and label them as unverified industry folklore relative to Lenny/Casey M6 research.

### Day 1

| Category | Poor | Average | Good | Great |
|----------|------|---------|------|-------|
| Gaming (casual) | <30% | 30–40% | 40–50% | >50% |
| Gaming (mid-core) | <25% | 25–35% | 35–45% | >45% |
| Social | <35% | 35–45% | 45–55% | >55% |
| Productivity | <25% | 25–35% | 35–45% | >45% |
| Health / fitness | <20% | 20–30% | 30–40% | >40% |
| Finance | <20% | 20–30% | 30–40% | >40% |
| E-commerce | <15% | 15–25% | 25–35% | >35% |

### Day 7

| Category | Poor | Average | Good | Great |
|----------|------|---------|------|-------|
| Gaming (casual) | <10% | 10–15% | 15–20% | >20% |
| Gaming (mid-core) | <8% | 8–12% | 12–18% | >18% |
| Social | <15% | 15–25% | 25–35% | >35% |
| Productivity | <10% | 10–18% | 18–25% | >25% |
| Health / fitness | <8% | 8–15% | 15–22% | >22% |
| Finance | <12% | 12–20% | 20–28% | >28% |

### Day 30

| Category | Poor | Average | Good | Great |
|----------|------|---------|------|-------|
| Gaming (casual) | <3% | 3–7% | 7–12% | >12% |
| Social | <8% | 8–15% | 15–22% | >22% |
| Productivity | <5% | 5–10% | 10–15% | >15% |
| Health / fitness | <4% | 4–8% | 8–14% | >14% |

## Conversion heuristics (label as hypotheses)

### Free → paid

| Model | Poor | Average | Good | Great |
|-------|------|---------|------|-------|
| Freemium | <1% | 1–2% | 2–4% | >4% |
| Free trial (7d) | <10% | 10–20% | 20–30% | >30% |
| Free trial (14d) | <8% | 8–15% | 15–25% | >25% |
| Reverse trial | <5% | 5–10% | 10–18% | >18% |

These bands are orientation only. Product category, price, and trial design dominate. Cite them as hypotheses unless the user supplies measured conversion.

### Onboarding

| Metric | Poor | Average | Good |
|--------|------|---------|------|
| Signup completion | <40% | 40–60% | >60% |
| Activation rate | <20% | 20–40% | >40% |
| Time to value | >5 min | 2–5 min | <2 min |

Define activation as a product-specific event, not “opened app.”

## Monthly churn / NRR quick grid (SaaS-shaped consumer)

Legacy package heuristics by list price — replace with measured revenue churn:

| List price | Poor monthly churn | Average | Good |
|------------|--------------------|---------|------|
| <$10/mo | >10% | 6–10% | <6% |
| $10–50/mo | >8% | 4–8% | <4% |
| >$50/mo | >5% | 3–5% | <3% |

For NRR quality language, prefer the Lenny/Casey 12-month NRR table above over a single generic “>110% = great” rule applied to every consumer sub.

## PMF linkage

Flattening retention curves (cohort % active stabilizing) are a standard PMF signal in practitioner writing collected by Lenny (*How to know if you've got product-market fit*): https://www.lennysnewsletter.com/p/how-to-know-if-youve-got-productmarket

YC’s *The real product-market fit* stresses depth of demand over vanity launch metrics: https://www.ycombinator.com/library/5z-the-real-product-market-fit

Sequoia’s Arc PMF framework is another stage vocabulary when teams need shared language for “how close are we?”: https://sequoiacap.com/article/pmf-framework
