# Post-signature obligations

Load for auto-renewal, notice, cure, assignment, or change-of-control life after signature.

## Notice math (Rule 3)

```text
alarm = renewal_date − notice_period − notice_lead_days
        − deemed_receipt_days (if notice by post/email has deemed receipt)
```

- Count in the **unit the contract defines** (business days ≠ calendar days; ~40% drift over a 30-day window is common)
- Default `notice_lead_days` = 45 unless config says otherwise
- Write the alarm into `## Due` the same turn the clause is read
- An uncalendared notice window is an automatic renewal — the counterparty has no duty to remind you

## Cure periods

Track separately from renewal notice. A cure clock starts on effective receipt of notice of breach — apply deemed-receipt rules.

## Assignment and change of control

- Consent requirements may block an acquisition or customer transfer
- "Deemed consent for bona fide acquirer" and free group reorganisations are common middle grounds
- Check whether assignment needs notice only or prior written consent

## Surviving clauses

After termination, confidentiality, IP, accrued fees, and audit rights often survive. List survivors explicitly in the wind-down checklist.
