# Assets and inventory

Load for capitalization, depreciation, disposals, leases, inventory costing, NRV, or shrinkage.

## Capitalization test

Capitalize when **both** are true:

1. Unit cost ≥ `capitalization_threshold` per invoice or item
2. Useful life > 1 year

**US tax de minimis safe harbor (IRS final tangibles regulations / Notice 2015-82):** taxpayers **without** an applicable financial statement (AFS) may elect to deduct qualifying amounts up to **$2,500** per invoice or item when also expensed in books; taxpayers **with** an AFS may use up to **$5,000**. The safe harbor excludes inventory and land. Amounts above the safe harbor still follow ordinary repair-vs-capitalize analysis — the ceiling is not an automatic capitalize-everything rule. Confirm election mechanics and book policy for the filing year.

Default skill config uses **2500** (no-AFS case). Set **5000** when the entity maintains a qualifying AFS and elects that ceiling. For non-US books, use local GAAP/tax rules instead of importing the IRS dollar amounts.

Otherwise expense. Write the policy once; apply it when profit is strong and when it is embarrassing.

## Depreciation

- Book method follows `reporting_framework` and useful life / salvage policy.
- Tax method may differ (book-tax difference) — track both when filings need it.
- Entry each period: Dr depreciation expense / Cr accumulated depreciation.
- Contra-asset accounts are reduced through disposal or correction entries, not by casually debiting them away to “clean up” the BS.

## Disposal

1. Record depreciation through disposal date if material.
2. Remove cost and accumulated depreciation.
3. Record proceeds.
4. Plug gain/loss to the income statement.
5. Update `<state_root>/asset-register.md`.

## Leases (directional)

Under common modern frameworks (US GAAP ASC 842 / IFRS 16 style), many leases put a right-of-use asset and lease liability on the balance sheet. Classify finance vs operating (or IFRS single model) from the contract facts, and put material multi-year leases on the balance sheet once the framework requires it.

## Inventory costing

| Method | Notes |
|---|---|
| FIFO | Widely accepted; ending inventory approximates current cost |
| Weighted average | Stable; common in perpetual systems |
| LIFO | Permitted under US GAAP in many cases; **prohibited under IFRS**; US tax conformity can force books to follow tax LIFO |

Perpetual vs periodic changes the timing of COGS entries, not the physical reality.

### NRV and shrinkage

- Write inventory down when NRV < carrying amount per policy.
- Book shrinkage when count < books: Dr shrinkage/COGS / Cr inventory.

## Failure recovery

| Trigger | First fix | Still failing |
|---|---|---|
| Register ≠ ledger | List additions/disposals missing | Rebuild register from invoices + prior TB |
| Margin swings with buying | Check whether purchases hit expense | Move to inventory asset + COGS on sale |
| Lease missing on BS | Read contract term and framework | Engage specialist for complex modifications |
