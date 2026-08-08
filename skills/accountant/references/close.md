# Close — period end, cutoff, lock

Load for month-end or year-end close, reopening a period, or setting close cadence.

## Dependency-ordered checklist

1. **Bank, card, loan, processor recon** complete for the period. Keep unresolved accounts open and state their impact; do not lock the period while they remain unresolved.
2. **AR and AP subledgers** tie to control accounts.
3. **Payroll** period posts complete; employer taxes and PTO accruals recorded.
4. **Inventory** count or perpetual roll-forward ties; COGS updated.
5. **Fixed assets**: additions, disposals, depreciation for the period.
6. **Revenue**: deferred revenue roll-forward; cutoff for deliveries.
7. **Accruals and prepaids** posted under the chosen double-count discipline.
8. **Intercompany / owner** items cleared or classified in equity correctly.
9. **Uncategorized and suspense** balances = 0.
10. **Trial balance** agrees; statement ties pass (`statements.md`).
11. **Lock** the period in the ledger; record closed totals and lock date in `<state_root>/memory.md`.
12. **Filings / management pack** use locked figures only.

Target calendar: `close_target_days` business days after period end (default 10). Prefer reversible estimates below materiality over waiting forever for a late document.

## Cutoff tests

- Cost incurred on the last day of the month belongs to that month even if the invoice arrives later → accrue.
- Cash received for work not yet delivered → deferred revenue, not revenue.
- Goods received not invoiced → accrue liability / inventory or expense per policy.

## Reopening a closed period

1. Confirm why (material error, missing entry, conversion fix).
2. Prefer correcting entries in the **open** period when immaterial.
3. If the period must reopen, document authorization, make the change, re-run ties, re-lock, and note impact on any figures already shared externally.
4. If a **filed tax return** used those numbers, load `escalate.md` and treat amendment vs current-period adjustment as a licensed-professional decision.

## Failure recovery

| Trigger | First fix | Still failing |
|---|---|---|
| Close blocked on one recon | Finish that account and quantify its impact | Keep the period open, assign an owner and due date, then re-run the close checklist |
| Suspense not empty | Research and code the remaining items with owner | Keep the period open until suspense is zero; track owner and due date outside the locked close result |
| Accrual vs invoice double-count | Inspect open accruals list | Reverse the duplicate; record discipline in coding rules |
