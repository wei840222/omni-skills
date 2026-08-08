# Ledger software

Load for QuickBooks, Xero, Wave, Sage, FreeAgent, spreadsheet ledgers, bank feeds, rules, or conversion balances.

## Account structure

- Map the chart to reporting needs before turning on feeds.
- Prefer tracking categories/classes for dimensions (location, product, project) over exploding the chart.
- Keep clearing accounts for processors and payroll and empty them each period.

## Bank feeds and rules

- Rules **propose**; a human confirms.
- Auto-add only for fixed-amount, single-vendor matches the operator has verified repeatedly.
- Review suggested matches for transfers between own accounts — book as balance-sheet transfers (cash ↔ cash), keeping income/expense clear of internal moves.

## Spreadsheet ledger controls

- One journal tab with running TB proof (debits = credits per entry and in total).
- Separate AR/AP subledgers that tie.
- Lock tabs for closed periods; changes only via reversing entries on an open period sheet.
- Version the file or export a PDF TB at each lock.

## Conversion balances

When moving systems or starting mid-life:

1. Enter opening balances that match the conversion TB.
2. Prove AR/AP open items detail = control.
3. Leave historical P&L out of the conversion unless the project explicitly reconstructs history.
4. First month after conversion gets extra recon attention.

## Feature traps

| Symptom | Check |
|---|---|
| Profit looks fine, cash does not | Unreconciled accounts; A/R not collecting |
| Duplicate expenses | Feed + manual bill both posted |
| Tax liability drifts | Tax codes not applied on invoices |
| Inventory always wrong | Items set to non-inventory / expense-on-PO |

## Failure recovery

| Trigger | First fix | Still failing |
|---|---|---|
| Feed duplicates | Exclude matched; undo batch | Rebuild account from statement |
| Rule miscodes silently | Turn rule to propose-only; reverse series | Document corrected coding rule in memory |
| Conversion opening off | Diff each BS account to old TB | Delay go-live until day-1 tie passes |
