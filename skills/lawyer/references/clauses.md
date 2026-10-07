# Clauses that decide money

Load for cap, indemnity, IP, warranty, SLA, audit, confidentiality, data, payment, assignment, or forum fights. Ranges are market-typical for B2B software and services; adjust for industry and leverage.

## Market snapshot

| Clause | What actually decides it | Common market position |
|---|---|---|
| Limitation of liability | The carve-outs, not the number | 12 months fees paid; supercap 2–5× for data/IP |
| Indemnity | Who controls defence; survives the cap? | IP from vendor; misuse/data from customer; mutual confidentiality |
| IP ownership | Whether "work product" includes pre-existing / generic tooling | Customer owns deliverables; vendor keeps background + licence back |
| Term and termination | Convenience exit, notice, prepaid fees | 12 months, auto-renew, 30–90 days notice, pro-rata refund on vendor default |
| Warranty and SLA | Credit only vs exit right | Credits capped + termination after repeated misses |
| Confidentiality | Duration; trade secrets survive? | 3–5 years; perpetual trade secrets; four standard exclusions |
| Data protection | DPA, sub-processors, transfer mechanism | Art. 28-style DPA; sub-processor notice + objection |
| Payment | Net terms, interest, suspension, dispute mechanics | Net 30; stated interest; suspension after notice + cure |
| Assignment / CoC | Acquisition terminates or transfers? | Consent required; deemed for bona fide acquirer; free group reorg |
| Governing law / forum | Where you must sue and can afford to | Home if leverage; neutral third if neither moves |

## Rule 2 math

```text
real_exposure ≈ stated_cap + Σ(carve_out_risks)
insured_gap   ≈ supercap − relevant_policy_limit  (when positive)
```

Worked example: $10k/month SaaS → 12-month cap $120k; 3× breach supercap $360k; $250k cyber limit → $110k uninsured. Argue the insurance number.

## Fallback ladder pattern

For each stuck clause:

1. **Ask** — preferred position with one-sentence commercial reason
2. **Trade** — give a low-cost concession (audit cadence, liability floor, mutual form)
3. **Supercap / basket** — narrow unlimited risk into a multiple or basket
4. **Walk-away** — only if expected cost (Rule 5) exceeds deal value under `risk_posture`

Never negotiate the cap number while ignoring carve-out sentences — read them as one clause.

## Unlimited confidentiality

Vendors want confidentiality inside the general cap; customers want data/secrets outside it. Common landing: supercap (2–5×) rather than either extreme.
