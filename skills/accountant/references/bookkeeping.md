# Bookkeeping — chart, entries, basis

Load when coding transactions, building journal entries, or converting between cash and accrual.

## Chart of accounts discipline

- Create an account when the split will change a decision; use classes/departments/tags for vendor or project detail.
- Prefer 30–80 meaningful accounts over one account per vendor.
- Uncategorized and suspense are transit only — empty them before lock.

## Entry construction

1. Identify the economic event and its date (not the typing date).
2. Name the two (or more) accounts and normal balances.
3. Confirm debits = credits.
4. Memo the business purpose and source document id.
5. Post only into an open period.

### Cash test

If money moved, one side is cash, card, or clearing. If neither side is a balance-sheet cash account, the entry is a reclassification — date it in the open period and memo what it fixes.

## Adjusting entry shapes

| Adjustment | Situation | Entry |
|---|---|---|
| Accrued expense | Cost incurred, invoice not yet received | Dr expense / Cr accrued liabilities |
| Accrued revenue | Delivered, not yet billed | Dr unbilled receivable / Cr revenue |
| Deferred revenue | Collected before delivery | Receipt: Dr cash / Cr deferred revenue; delivery: Dr deferred revenue / Cr revenue |
| Prepaid expense | Paid before consumption | Payment: Dr prepaid / Cr cash; period: Dr expense / Cr prepaid |
| Depreciation / amortization | Capital item in service | Dr depreciation expense / Cr accumulated depreciation |
| Valuation allowance | Estimated uncollectible or impaired | Dr matching expense / Cr allowance |

### Double-count rule

An accrual and the real invoice both hitting expense is the most common close error. Pick one discipline per account:

- (a) reverse the accrual on day 1 of the next period and let the invoice post normally, or
- (b) leave the accrual standing and post the invoice against the liability, not expense.

Record the chosen discipline under `## Coding Rules` in `<state_root>/memory.md`.

### Straight-line amortization

Monthly amount = total ÷ number of periods covered. Prorate first/last month by days when the term does not start on the 1st. A twelve-month policy starting the 17th still covers 12 months and often needs 13 schedule lines.

## Basis conversion

- Accrual revenue = cash receipts + closing AR − opening AR
- Accrual expense = cash paid + closing AP − opening AP

Declare `accounting_basis` once; mixing bases per transaction produces books that convert to neither cleanly.

## Common entry patterns

| Event | Debit | Credit |
|---|---|---|
| Sale on account | AR | Revenue (+ tax liability if collected) |
| Customer payment | Cash | AR |
| Vendor bill | Expense or inventory/asset | AP |
| Pay vendor | AP | Cash |
| Loan proceeds | Cash | Loan payable |
| Loan payment | Loan payable (principal) + interest expense | Cash |
| Owner contribution | Cash | Equity contribution |
| Owner draw | Owner draws (contra-equity) | Cash |
| Processor payout | Cash + fees + refunds/chargebacks | Clearing / revenue accounts per gross method |

## Failure recovery

| Trigger | First fix | Still failing |
|---|---|---|
| Entry will not balance | Re-check which account was omitted; verify amount signs | Rebuild from source document line by line |
| Same invoice accrued twice | Inspect open accruals vs AP | Reverse the duplicate in the open period |
| Import doubled a batch | Isolate by batch id / date range | Reverse the batch; re-import once with controls |
