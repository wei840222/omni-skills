# Statements and ties

Load when building or validating a balance sheet, income statement, cash flow statement, ratios, or management pack figures.

## Statement ties that must hold

Run applicable ties before any number leaves the session. Each is an equality; a break names its own cause.

| Tie | Both sides | Usual break cause |
|---|---|---|
| Balance sheet balances | Assets = Liabilities + Equity | Unbalanced import; missing opening balance |
| Profit reaches equity | NI = Δ RE + distributions − contributions | Direct posts to RE; closed period moved |
| Cash foots | CFS ending cash = BS cash = sum of reconciled cash accounts | Unreconciled account; misclassified deposit |
| AR subledger | Aging total = AR control | JE posted straight to control |
| AP subledger | Aging total = AP control | Same as AR |
| Payroll | Gross wages on returns = wage expense ± accrual movement | Net-pay-only postings |
| Transaction tax | Tax liability = filed unpaid + collected since last return | Tax collected booked as revenue |
| Inventory | Count × costing method = inventory account | Purchases expensed on payment |
| Fixed assets | Register cost and accum. dep. = ledger accounts | Disposal missing in books |
| Year over year | Prior closing BS = current opening BS | Prior period edited after close |

## Cash flow presentation

- Default for reporting: **indirect** method (starts from net income; adjusts non-cash and working capital).
- Build **direct** method only when the operator manages collections and payments from it day to day.
- Ending cash on the cash flow statement must equal balance sheet cash.

## Common-size and ratios (decision-oriented)

Compute only ratios that change a decision for this entity. Typical set:

- Gross margin, operating margin
- Current ratio / quick ratio when liquidity is the question
- DSO, DPO, inventory days when working capital is the question
- Debt / equity or debt service coverage when leverage or covenants matter

Always label period, basis (`accounting_basis`), currency (`base_currency`), and comparative columns on the same basis.

## Failure recovery

| Trigger | First fix | Still failing |
|---|---|---|
| BS does not balance | Find unbalanced JE or import | Rebuild TB from source modules |
| Cash flow ≠ BS cash | Check recon status of each cash account | Rebuild CFS from two BS + P&L |
| Subledger ≠ control | List JEs to control only | Reverse and repost through subledger |
