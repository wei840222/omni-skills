# Revenue recognition and tax

Load for deferred revenue, subscriptions/milestones, income-tax estimates, sales tax/VAT/GST, or retention rules.

## Revenue recognition (five-step pattern)

Directional framework used by modern GAAP/IFRS-style standards:

1. Identify the contract
2. Identify performance obligations
3. Determine the transaction price
4. Allocate price to obligations
5. Recognize revenue when (or as) obligations are satisfied

Cash collection without delivery → **deferred revenue**. Delivery without billing → **unbilled receivable / contract asset** when enforceable.

### Gross vs net

If the entity controls the good or service before transfer, present **gross**. If it arranges for another party to provide it (agent), present **net**. Control indicators beat marketing language.

### Subscriptions and milestones

Build a schedule: cash in, deferred balance, monthly recognition, remaining obligation. At close, deferred revenue roll-forward must tie to the liability account.

## Income tax (bookkeeping view)

This skill prepares **figures and calendars**; it does not replace a licensed return preparer.

- Entity type drives which return and which owner-pay rules apply.
- Estimated taxes: track safe-harbor style rules for the jurisdiction and year; store the year beside each rate or threshold used.
- Book-tax differences (depreciation, accrual vs cash for tax, meals, etc.) need a simple schedule when material.
- Retention baseline from IRS “How long should I keep records?” (confirm for `jurisdiction` and non-tax creditors/insurers):
  - **3 years** after filing in ordinary cases (returns filed early treated as filed on the due date)
  - **6 years** if you do not report income that should be reported and it is more than **25%** of the gross income shown on the return
  - **7 years** if you file a claim for a loss from worthless securities or a bad-debt deduction
  - **Indefinitely** if you do not file a return, or if you file a fraudulent return
  - Employment tax records: **at least 4 years** after the later of the date the tax becomes due or is paid (employment-tax recordkeeping page also anchors retention after the year’s filings)
  - Property records: keep through the limitations period for the year you dispose of the property (basis and depreciation history)
  - Non-US windows are frequently longer — look up before destroying records

### Cash vs accrual method pressure (US)

IRC §448 limits the cash method for C corporations, partnerships with a C corporation partner, and tax shelters, with a gross-receipts exception. The inflation-adjusted average annual gross receipts ceiling is published in an annual revenue procedure — for **taxable years beginning in 2025**, Rev. Proc. 2024-40 sets the §448(c) test at **$31,000,000** (3-year average). Look up the procedure for the filing year rather than hard-coding an old $25M statute figure.

## Sales tax / VAT / GST

- Tax collected is a **liability**, not revenue.
- Nexus / registration thresholds are time-sensitive and jurisdiction-specific — look up for the year of sale; treat prior-year memory as a starting clue only.
- Exemption certificates: keep them complete and current; missing certificates become tax due.
- Reverse-charge and OSS/IOSS-style regimes (where applicable) change who remits — identify the regime before filing.
- Tie: sales-tax / VAT liability balance = returns filed and unpaid + tax collected since the last return.

## Rate lookup rule

Wage bases, mileage rates, contribution limits, reporting thresholds, and many tax rates are indexed or legislated. For any figure destined for a filing, look it up for the **filing year** and record the source year next to the number in working papers or `<state_root>/filing-log.md`.

## Failure recovery

| Trigger | First fix | Still failing |
|---|---|---|
| Deferred revenue will not roll | Rebuild schedule from contracts | Split by product/obligation |
| Tax liability ≠ returns | List collections vs filings by period | Find tax-in-revenue miscodes |
| Unknown nexus | Pause expansion claims; gather destination sales | Specialist before next return (`escalate.md`) |
