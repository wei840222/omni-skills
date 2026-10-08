# Unit economics (CAC, LTV, payback)

Load when reviewing spend efficiency, channel mix, churn math, or LTV:CAC. Always state denominators and margin basis.

## Core formulas

### Customer Acquisition Cost (CAC)

```text
CAC = Total fully loaded acquisition spend / New paying customers
```

- Include ads, content production allocated to acquisition, tools, and people time when material.
- Segment by channel: CAC(organic), CAC(paid), CAC(referral).
- If the user only has installs, report **CPI** separately. Do not call install cost “CAC” when LTV is payer-based.

### Lifetime Value (LTV)

```text
LTV_revenue ≈ ARPU × average lifetime months
LTV_revenue ≈ ARPU / monthly revenue churn   (when churn is stable)
LTV_contribution ≈ contribution margin per period × expected periods
```

State explicitly whether LTV is **gross revenue** or **contribution margin** (after payment fees, COGS, variable support, refunds). Contribution-margin LTV is required before calling payback “profitable.”

### Payback period

```text
Payback_months = CAC / monthly contribution per customer
```

Heuristic targets (not covenants):

- Often cited ~**< 6 months** for venture-backed consumer when capital is patient.
- Tighter (often ~**< 3 months**) when bootstrapped or capital-constrained.

Replace heuristics with the user’s cash runway and payback policy when provided.

### LTV:CAC ratio

| Ratio (contribution LTV) | Read |
|--------------------------|------|
| < 1:1 | Losing money on the margin definition in use — stop scale |
| 1:1–2:1 | Fragile — fix retention, monetization, or CAC quality |
| ~3:1 | Common healthy target once definitions are honest |
| > 5:1 with growth ambition | May be under-investing in proven channels |

## By-channel template

| Channel | Spend | New paying customers | CAC | D30 retention | Est. contribution LTV | LTV:CAC |
|---------|-------|----------------------|-----|---------------|------------------------|---------|
| Meta | | | | | | |
| Google | | | | | | |
| Organic | | | | | | |
| Referral | | | | | | |

### Warning signs

- Paid CAC > ~2× organic CAC with worse retention → paid quality or creative mismatch.
- High LTV variance by channel → segment offers and onboarding; do not blend.
- Payback > 12 months without funding that explicitly supports it → unsustainable scale.

## Churn analysis

| Type | Formula | Insight |
|------|---------|---------|
| User churn | Lost users / starting users | Volume leak |
| Revenue churn | Lost MRR / starting MRR | Value leak |
| Net revenue retention | (Start MRR + expansion − churn − contraction) / start MRR | Expansion health |

### Illustrative category bands (hypotheses — replace with measured cohorts)

Short-window habit signals differ from **month-6 user retention** research. Prefer Lenny/Casey M6 bands in `references/benchmarks.md` for “is this good retention?” debates when M6 exists.

| Category | Example “good” D7 habit signal (legacy package heuristic) | Example “good” D30 |
|----------|-------------------------------------------------------------|--------------------|
| Gaming | higher bar than productivity casual | still low absolute D30 |
| Productivity | mid | mid |
| Social | higher early return | higher D30 when network forms |
| Fitness | mid-low without habit design | mid-low |

Do **not** treat any single D7 number (including legacy “> 20%”) as universal PMF. Pair short-window tables with category M6 guidance and the user’s own flattening cohort curves.

## Related sources

See `references/sources.md` (unit economics / retention topics).
