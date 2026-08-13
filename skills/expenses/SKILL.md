---
name: expenses
description: Log, split, and report expenses, reimbursements, and budgets. Use when recording payments, splitting bills, settling group trips, or tracking budgets; route net-worth questions to personal-finance-tracker and bookkeeping to accountant.
metadata:
  openclaw: '{"emoji":"💸"}'
  related-skills: '{"personal-finance-tracker":"net worth, cashflow and debt, which read these totals as input","subscriptions":"the recurring-charge inventory in the shared finances/ box","invoice":"issuing invoices to clients, where rebillable costs end up","accountant":"bookkeeping, financial statements and tax filing beyond expense evidence","travel-planning":"the trip itself; this skill covers what the trip costs"}'
---

## State location

Expenses state may exist in `<workspace>/expenses/`, `<workspace>/memory/expenses/`, or `~/expenses/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/expenses/`, `<workspace>/memory/expenses/`, `~/expenses/`.
3. If multiple candidate directories exist, use the highest-priority one, keep the others independent, and tell the user which location was selected.
4. If none exists and the user asks to save an expense, split, settlement, claim, rule, budget, report, or reconciliation, create `<workspace>/expenses/`.

Use the selected `<state_root>` for every state operation in this skill. Legacy locations are migration sources only: propose a copy, validation, cutover, and rollback plan before any migration; do not move or delete existing data automatically.

## Core behavior

When `<state_root>` exists, read `<state_root>/config.yaml` and `<state_root>/memory.md` before using saved preferences or prior balances. Store durable records only after the user asks to record or change them, and name every file changed. Keep configuration in `<state_root>/config.yaml`, current balances and due dates in `<state_root>/memory.md`, monthly entries in `<state_root>/ledger/YYYY-MM.md`, and finalized settlements or reports in `<state_root>/reports/` when the user asks to retain them.

Record an entry with date, amount and currency, vendor, category, payer, and payment method. Mark unavailable fields as `unknown`, report totals with their currency and as-of date, and use the defaults below when no saved configuration exists. Keep card numbers, CVVs, PINs, banking logins, and tokens out of every state file; retain only a last four digits, card nickname, or a controlled-secret pointer such as `keychain:amex-personal`.

Treat related skill data as separate unless the user explicitly asks to coordinate it. For example, `subscriptions` owns recurring-charge inventory, `personal-finance-tracker` owns net worth, and `accountant` owns bookkeeping and tax filing.

## When To Use

- Recording spending as it happens: an amount, a vendor, a category, a payment method, a receipt
- Shared money: splitting a bill, a flat, a trip or a household, tracking who owes whom, and settling up
- Getting money back: employer reimbursement claims, per diems, mileage, client-rebillable costs
- Deciding whether something is a deductible business expense and what evidence it needs to survive
- A bounded budget — renovation, wedding, trip, launch — that needs a remaining number and an early warning
- Answering "where did it go": month closes, category trends, variance against budget, tax-year packs
- Act-as mode: this skill maintains the ledger itself. It does not advise on investing, debt payoff, or net worth (`personal-finance-tracker`), and does not run a budgeting methodology (`zero-based-budgeting`)

## Quick Reference

| Situation | Play |
|---|---|
| "I just paid €12 for lunch" | Record one six-field entry in the current monthly ledger; use `unknown` for unavailable details. |
| Weeks of receipts piled up unlogged | Backfill from the statement, then mark reconstructed entries. |
| Cash keeps vanishing from the log | Count the wallet and record the difference as one `cash-unlogged` entry. |
| "What category is this?" / misc is bloating | Apply the decision-value test and save a vendor rule when the user requests it. |
| Split the dinner / flat / trip | Record payer and beneficiaries separately, then update balances. |
| "Who owes who, and how do we settle?" | Net balances and propose the minimum transfers. |
| Work owes me money | Record the claim packet, policy limit, submission deadline, and status. |
| Per diem or mileage instead of receipts | Use the configured rate and units; verify the current applicable official rate before quoting one. |
| "Can I deduct this?" or rebill a client | Record the business purpose, mixed-use basis, and evidence needed for the applicable jurisdiction. |
| Receipt handling, budget, trip, foreign currency, reconciliation, or reports | Apply the configuration, traps, and taxonomy guidance below. |
| Refund, chargeback, deposit, duplicate charge | Record a negative entry against the original month and category, with a reference to the original entry. |

## Core Rules

1. **Log now, complete later; never the reverse.** An entry is six fields — date, amount with currency, vendor, category, payer, payment method. A field you do not have is written as `unknown` and the entry still goes in. The entry that waits for perfect data is the entry that never exists, and a log with gaps is worth more than a log with holidays.
2. **Transaction date, not posting date.** Card charges post 1-3 days after the purchase, and a purchase on the 30th that posts on the 2nd silently moves a month's total. Store the date the money was committed; keep the posting date only for reconciliation.
3. **Every amount carries its currency, in the value.** `62 USD`, never `$62` — the ledger will hold three currencies before the year is out and `$` is ambiguous across at least four of them. A foreign entry stores three fields: original amount with its currency, the rate as home-per-unit-foreign, and the rate date. Home amount = original × rate: 8,400 JPY at 0.0062 EUR/JPY = 52.08 EUR. Storing only the converted number destroys the entry the first time someone asks what the actual price was.
4. **Who paid and who owes are different fields.** One expense, two facts: the payer bears the cash, the beneficiaries bear the cost. Invariant after every shared entry: the net balances of a group sum to zero. If they do not, identify the incorrect split before adding anything else.
5. **A refund is a negative entry, not income.** Book it against the original month and the original category, referencing the original entry. Booked as income it inflates two numbers at once: the category total stays wrong forever and the month looks like it earned money. Same for a returned deposit — a deposit is a receivable when paid and a zero when returned, never a category expense.
6. **Always compare elapsed-share instead of a month-to-date number against a closed month.** Every stored total carries an `As of` date; a total whose as-of is not the last day of its period is partial and gets labeled as such in every sentence that reports it. Elapsed-share comparison instead: 1,400 EUR by day 12 of a 30-day month projects ~3,500 EUR, which is the number worth reacting to.
7. **Categories are stable or every comparison is a lie.** Renaming or resplitting a category applies retroactively across the whole history in the same turn, or it does not happen. The test for a new category is whether its number would change a decision; if not, it is a tag. `other` above ~5% of monthly spend signals that the taxonomy needs repair rather than that the month was unusual.
8. **Evidence is captured at payment or lost.** At or above `receipt_threshold`, an entry includes a receipt pointer; a business or reimbursable entry also includes the business purpose at the time of payment.

## Output Gates

Before delivering a number, a settlement, a claim or a report:

- Does every amount carry its currency, and does every foreign entry carry original, rate and rate date (Rule 3)?
- Is any total I am reporting a mix of month-to-date and closed periods (Rule 6)?
- After a shared entry or a settlement, do the group's net balances still sum to zero (Rule 4)?
- Did everything durable from this session land in its box — and did any new box get its `## Boxes` line in the same turn?
- Did I strip every card number, PIN, login and token from anything pasted in, leaving a `<kind>:<locator>` pointer in its place?
- Did I report the number without an opinion attached to it?

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| home_currency | text (ISO 4217) | USD | Currency for converted totals; entries retain the currency actually paid. |
| tax_year_start | text (MM-DD) | 01-01 | Boundary of the business year and receipt-retention clock. |
| receipt_threshold | number (home currency) | 75 | Amount at or above which a receipt pointer is required. |
| close_day | number (1-28) | 1 | Day the previous month is closed and reported. |
| settle_cadence | week \| month \| trip \| on_request | month | How often shared balances are netted. |
| default_split | equal \| by_income \| custom | equal | Split used when people are named but proportions are not. |
| budget_alert_pct | number (50-100) | 80 | Spend share at which a budget is flagged. |
| mileage_rate | number (home currency per km or mi) | none | Rate for mileage; verify the current official jurisdictional rate before quoting one. |
| private_categories | list | none | Categories excluded from shared or exported reports; their totals fold into `other`. |

Store stated preferences for tooling, conventions, platform/jurisdiction, safety posture, output format, cadence, and standing split policy in `config.yaml`. A preference changes future behavior only after the user states it.

## Traps

| Trap | Do instead |
|---|---|
| Designing categories before logging | Log flat first; split a category only when its number would change a decision. |
| Settling every pair separately | Net balances, then minimize transfers. |
| Booking a refund as income | Use a negative entry against the original month and category. |
| Keeping only a converted foreign amount | Store original amount, rate, and rate date. |
| Reconstructing business purpose at tax time | Record the purpose with the payment. |
| Treating a project budget as paid-to-date | Track committed and paid amounts separately. |
| Accepting dynamic currency conversion | Pay in the local currency after comparing disclosed options. |
| Waiting for every receipt before claiming | Submit partial reimbursement packets on the configured cadence. |
| Using one shared category with no participants | Record payer and beneficiaries per entry. |
| Changing categories only from today onward | Apply the change across history or retain the current categories. |
| Importing bank CSV without a dedupe key | Dedupe on date, amount, and safe account identifier. |
| Adding guilt to a report | Report the number and trend; the judgment belongs to the user. |

## Where experts disagree

- **Broad versus granular categories:** broad categories last; granular categories answer more questions. The boundary is decision value, with tags for secondary slicing.
- **Complete versus threshold logging:** complete logs support reconciliation, audits, shared settlement, and tax evidence; a sustainable personal log may use a floor for discretionary spending.
- **Equal versus income-based splits:** equal is simple; proportional may fit materially different incomes. Record the group rule before a disagreement.
- **Cash tracking:** itemized cash preserves category detail; treating a withdrawal as spent is easier to maintain but loses that detail.
