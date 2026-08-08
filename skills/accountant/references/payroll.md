# Payroll and contractors

Load for payroll journal entries, employer taxes, PTO accruals, contractor classification, or information-return prep figures.

## Gross-to-net entry (pattern)

Every pay run needs the full shape, not a single net expense:

1. Dr wage / salary expense for **gross**
2. Cr cash for **net pay**
3. Cr liability accounts for each withholding (income tax, social contributions, benefits, garnishments — names vary by jurisdiction)
4. Dr employer payroll tax expense / Cr employer tax liabilities
5. Clear liabilities when deposits/filings are made

Net-pay-only posting hides gross wages and will not tie to payroll returns.

## PTO / leave accrual

When policy creates a vested obligation: Dr PTO expense / Cr PTO liability for the earned amount; reduce liability when leave is taken or paid out per policy.

## Contractor vs employee (control test — directional)

Factors commonly examined (jurisdiction-specific labels differ):

- who controls how, when, and where work is done
- who provides tools and bears profit/loss risk
- whether the worker can market services to others
- permanence and integration into the core business

Misclassification risk: back taxes, penalties, and reworked filings. When facts are mixed, produce the fact package and route classification decisions to a licensed adviser (`escalate.md`).

## Information returns

Track contractor payments that may require information returns (US Form 1099-NEC style thresholds and analogues elsewhere). Maintain payee legal name, tax id status (pointer only — not full id in free text if avoidable), amount, and address quality before filing season.

## Deposit schedules

Map each liability to its deposit due date in `## Due`. Trust-fund style withholdings (employee taxes held) are top priority — late deposit can create personal liability for responsible persons (`escalate.md`).

## Failure recovery

| Trigger | First fix | Still failing |
|---|---|---|
| Returns ≠ wage expense | Rebuild gross from payroll registers | Accrue missing employer taxes; reverse net-only posts |
| Contractor list incomplete | Export payments ≥ threshold by payee | Hold filing until identity data is complete |
| Deposit missed | Quantify exposure same day | Escalate trust-fund risk immediately |
