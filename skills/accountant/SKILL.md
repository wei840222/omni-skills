---
name: accountant
description: Use when the user needs entity bookkeeping that closes — coding transactions to a chart of accounts, journal entries, bank/card/processor reconciliation, month-end close and lock, balance sheet/P&L/cash-flow ties, payroll or sales-tax/VAT figures, owner draws vs salary, inventory or fixed-asset capitalization, deferred revenue, cleanup of messy books, or an audit/lender package. Trigger even if they say the books do not balance, a Stripe deposit does not match sales, or a period must be closed without naming accountant. Not for company forecasting/fundraising (cfo), personal money (money), issuing client invoices (invoice), archiving supplier invoices (invoices), expense capture before the ledger (expenses), payment product build (billing), or bank payment ops (banking).
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"📊"}'
  related-skills: '{"banking":"Owns bank payment operations and account ops whose balances feed accountant reconciliations.","billing":"Builds payment and subscription systems whose processor payouts are reconciled here.","cfo":"Uses closed books for forecasts, runway, board packs, and capital decisions.","expenses":"Captures day-to-day spend before it is coded into the ledger.","invoice":"Issues client invoices that become receivables and revenue recognition here.","invoices":"Archives supplier invoices that become payables and expense entries.","money":"Handles personal budgeting and debt decisions outside entity books."}'
---

## State location

Accountant state may exist in `<workspace>/accountant/`, `<workspace>/memory/accountant/`, or `~/accountant/`. `<workspace>` means the workspace root provided by the host/runtime, not the shell's current working directory.

Before any state read, query, create, update, or delete, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/accountant/`, `<workspace>/memory/accountant/`, `~/accountant/`.
3. If none exists and state must be created, default to `<workspace>/accountant/`.

If multiple candidate directories exist, use only the first one, tell the user that multiple state directories were found, and leave the others untouched. Use the selected `<state_root>` for every state operation during the run. Create only the resolved filesystem path; the placeholder name `<state_root>` is documentation-only.

Legacy path `~/Clawic/data/accountant/` is a migration source only. It is outside active lookup. Copy, validate, cut over, and keep a rollback path only after the user chooses migration.

Shared finance boxes (accounts, subscriptions, budget) may live under a host-provided shared path such as `<workspace>/finances/` or a user-declared path. Treat those as external writes: list the actual path, minimum scope, and obtain consent before the first write. Prefer entity nicknames and last-four identifiers; store credential pointers only (`keychain:…`, `1password:…`, `env:…`, `file:…`).

## Setup

After resolving `<state_root>`, if `<state_root>/memory.md` is missing or empty, read `references/setup.md` and follow it. Confirm with the user before the first write to `<state_root>`.

## Primary workflow

Execute in order. Each step has a done-when check.

### Step 1: Resolve state and configuration

1. Resolve `<state_root>` with the State location procedure.
2. Load `<state_root>/config.yaml` when it exists, then `<state_root>/memory.md` (including `## Boxes` and `## Due`).
3. Apply configuration precedence: explicit config → host profile universals (currency, locale, country) → Configuration defaults in this skill.
4. While `jurisdiction` is unset, name the tax regime, deadlines, and retention rules being assumed before acting on them.

Done when: `<state_root>` is fixed, config sources are known, and any jurisdiction assumption is stated.

### Step 2: Classify the request

Pick one primary lane:

| Lane | Signals | Load |
|------|---------|------|
| Code / journal | which account, entry shape, basis | `references/bookkeeping.md` |
| Reconcile | bank, card, processor, difference | `references/reconciliation.md` |
| Close | month-end, lock, accruals, cutoff | `references/close.md` |
| Statements | BS / P&L / cash flow, ratios, ties | `references/statements.md` |
| AR / AP | aging, write-off, vendor bill | `references/subledgers.md` |
| People cost | payroll, contractor vs employee | `references/payroll.md` |
| Stock / assets | inventory, capitalize, depreciate | `references/assets-inventory.md` |
| Revenue / tax | deferred revenue, income tax, sales tax/VAT | `references/revenue-tax.md` |
| Owner pay | draw, salary, distribution | `references/owner-pay.md` |
| Scrutiny / cleanup | audit PBC, messy books, migration | `references/audit-cleanup.md` |
| Software | feeds, rules, conversion balances | `references/software.md` |

Load only the reference that owns the top lane. Expand after that lane is under control.

Done when: one primary lane owns the next actions.

### Step 3: Apply core rules and produce the artifact

1. Name both sides of every entry, the date (event date), and the open period.
2. Reconcile before reporting from a period (Rule 3).
3. Run the applicable ties in `references/statements.md` before any figure leaves the session.
4. Scan the escalate table in `references/escalate.md`. If a signal matches, that answer comes first.

**Filing and locked-period path:** Numbers already on a filed return or locked period are corrected with a reversing entry plus the correct entry in an open period. Amendment vs current-period adjustment is a licensed-professional decision when filed figures must change.

**Credential path:** State writes keep last-four identifiers, registration numbers, ledger codes, amounts, and pointer strings (`keychain:…`, `1password:…`, `env:…`, `file:…`). Full account numbers, national IDs, e-file PINs, and software passwords stay outside skill memory.

Done when: the deliverable balances, names accounts, and states its basis, period, and uncertainty.

### Step 4: Persist durable outcomes

Before each persistent create, update, or deletion, name the exact file and proposed durable outcome and obtain the user's explicit authorization for that write in the current task. Without it, return a proposed state diff in chat. After authorization, write only outcomes the next session should reuse: coding rules, closed or reopened periods, finished reconciliations with explained differences, capitalized assets, filing totals, accrual schedules, policies, or cleanup plans.

Templates: `assets/accountant-data-templates.md`. Lifecycle and box index rules: `references/memory.md`.

```text
<state_root>/
├── config.yaml              # required once preferences persist
├── memory.md                # required once persistence is enabled
├── chart-of-accounts.md     # optional declared chart
├── asset-register.md        # optional FA register
├── filing-log.md            # optional returns and totals
├── policies.md              # optional accounting policies
└── boxes/                   # optional topic boxes named from ## Boxes
```

In a shared box, update or remove only rows this skill wrote, matched on that box's identity key. Name every write and deletion in one line as it happens.

Done when: new or updated files sit under the resolved `<state_root>` and `memory.md` reflects the change.

### Step 5: Close the turn

Leave the operator with:

- the entry, reconciliation result, statement tie, or filing figure requested
- which accounts remain unreconciled (if any)
- open items and the next due from `## Due`
- one owner and due window per follow-up

Done when: each follow-up has an owner, a trigger, and a review window.

## Output validation checklist

Before delivering an entry, statement figure, filing total, or "here is where you stand":

- [ ] Every entry balances, names both accounts, and uses an event date in an open period
- [ ] Period recon status is finished or the unreconciled accounts and uncertainty are stated
- [ ] Applicable statement ties from `references/statements.md` were run
- [ ] Basis (`accounting_basis`) and currency (`base_currency`) are labeled; comparatives use the same basis
- [ ] Filing-year rates/thresholds were looked up when the figure feeds a return
- [ ] Escalate table in `references/escalate.md` was scanned; matching signals lead the answer
- [ ] Each durable outcome has current-task write authorization, or its proposed diff remains in chat

## Architecture

Runtime state lives under the resolved `<state_root>`. Skill resources stay in `references/` and `assets/` and are separate from runtime state.

## Quick reference

| Topic | File | When to load |
|-------|------|--------------|
| First-use setup | `references/setup.md` | `<state_root>/memory.md` missing or empty |
| Memory lifecycle | `references/memory.md` | Creating or updating persistent status |
| Copyable templates | `assets/accountant-data-templates.md` | Creating state files |
| Chart, entries, basis | `references/bookkeeping.md` | Coding and journal entries |
| Bank / card / processor | `references/reconciliation.md` | Making cash and processors match |
| Period end | `references/close.md` | Close checklist, cutoff, lock |
| Statements and ties | `references/statements.md` | BS, P&L, cash flow, ratios |
| AR and AP | `references/subledgers.md` | Aging, write-offs, three-way match |
| Payroll and contractors | `references/payroll.md` | Gross-to-net, 1099 vs W-2 style tests |
| Inventory and fixed assets | `references/assets-inventory.md` | Costing, capitalize, depreciate, leases |
| Revenue and tax | `references/revenue-tax.md` | Recognition, income tax, sales tax/VAT |
| Owner compensation | `references/owner-pay.md` | Draws, salary, distributions |
| Audit and cleanup | `references/audit-cleanup.md` | PBC packages, catch-up books |
| Ledger software | `references/software.md` | Feeds, rules, migrations |
| Licensed escalation | `references/escalate.md` | Trust-fund, amendment, attestation, fraud signals |
| Verified sources | `references/sources.md` | Re-check filing-year figures and primary URLs |
| Darwin triage score | `references/darwin-evaluation.md` | Gate 8 dimension breakdown and test summary |

## Core rules

1. **Every entry balances; the event date owns the period.** Debits = credits always. Cutoff: a cost incurred on the 30th belongs to that month even if the invoice arrives next month — accrue it (`references/close.md`).
2. **Basis is declared once and applied to everything.** `accounting_basis` accrual recognizes when earned or incurred; cash when money moves. Conversion: accrual revenue = cash receipts + closing AR − opening AR; accrual expense = cash paid + closing AP − opening AP.
3. **Reconcile before you report.** Statement, filing, and performance answers come from periods whose bank, card, and processor accounts already reconcile (both adjusted balances equal to the cent) or from an explicit uncertainty statement that names the open accounts (`references/reconciliation.md`).
4. **Materiality is set before it is needed.** Threshold = the smaller of `materiality_pct` × annual revenue (default 0.5%) and 5% of pretax income. Below it, correct in the current period; above it, correct the period of the error. Qualitative override: anything that flips profit/loss, breaches a covenant, changes a filed return, or involves suspected fraud is material at any size.
5. **Capitalize by threshold and life.** Capitalize when unit cost ≥ `capitalization_threshold` (default 2,500 per item/invoice for US taxpayers **without** an applicable financial statement under the IRS de minimis safe harbor; **5,000** with an AFS) AND useful life > 1 year. Otherwise expense. Apply the policy in both directions (`references/assets-inventory.md`).
6. **Entity money and owner money stay separate.** Personal spend on the business card is a draw. Business cost paid personally is a contribution or reimbursement. Coding either through P&L misstates profit and entity separateness (`references/owner-pay.md`).
7. **Corrections reverse and re-post.** A correction is a reversing entry plus the correct entry, both in an open period, both memoing what they fix.
8. **Close, then lock.** Closed means subledgers tie, accounts reconcile, uncategorized/suspense are empty, and the trial balance agrees — then lock the date and record totals (`references/close.md`).
9. **Filing figures trace to documents that outlive the assessment window.** US IRS baseline (confirm `jurisdiction`): keep supporting records **3 years** after filing in ordinary cases; **6 years** if unreported income > 25% of gross income on the return; **7 years** for claims of loss from worthless securities or bad-debt deductions; **indefinitely** if no return was filed or a fraudulent return was filed; employment tax records **at least 4 years** after the later of the date the tax becomes due or is paid. Look up non-US windows before destroying records (`references/revenue-tax.md`).

## Debits and credits (summary)

| Account type | Normal balance | Increases with | Closed at year end |
|---|---|---|---|
| Asset | Debit | Debit | No |
| Contra-asset | Credit | Credit | No |
| Liability | Credit | Credit | No |
| Equity | Credit | Credit | No |
| Contra-equity (draws) | Debit | Debit | Yes → RE |
| Revenue | Credit | Credit | Yes → RE |
| Contra-revenue | Debit | Debit | Yes |
| Expense / COGS | Debit | Debit | Yes → RE |

Full adjusting-entry shapes and double-count discipline: `references/bookkeeping.md`.

## Configuration

Defaults apply until the user states a preference. Store overrides in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| jurisdiction | text | none | Deadlines, thresholds, forms, retention |
| accounting_basis | cash \| accrual \| modified-cash | accrual | Recognition rule for every entry |
| reporting_framework | us-gaap \| ifrs \| local-gaap \| tax-basis | us-gaap | Statement presentation |
| entity_type | sole-trader \| partnership \| llc \| s-corp \| c-corp \| nonprofit | sole-trader | Equity and owner-pay structure |
| fiscal_year_end | MM-DD | 12-31 | Period boundaries |
| base_currency | ISO code | USD (or host profile) | Reporting currency |
| ledger_software | quickbooks \| xero \| wave \| sage \| freeagent \| spreadsheet \| other | spreadsheet | Software mechanics |
| materiality_pct | number | 0.5 | Rule 4 input |
| capitalization_threshold | number | 2500 | Rule 5 input |
| close_target_days | number | 10 | Close SLA after period end |
| chart_of_accounts | path | none | Usually `<state_root>/chart-of-accounts.md` |

## Gotchas

- **Processor deposit ≠ revenue:** book gross sales, then fees, refunds, and chargebacks separately.
- **Loan payment split:** principal reduces liability; only interest is expense.
- **Sales tax collected is a liability,** not revenue.
- **Net-pay-only payroll** leaves returns untied — post full gross-to-net.
- **Difference ÷ 9 with no remainder** often means transposition; **÷ 2** often means a side posted twice or reversed.
- **Cleanup runs forward** from the last known-good balance, oldest-first only after that restart point is fixed.
- **Indexed rates move yearly** — look up wage bases, mileage, contribution limits for the filing year.

## Traps

| Trap | Do instead |
|---|---|
| Booking a processor payout as revenue | Gross revenue, then each deduction |
| Whole loan payment to expense | Split principal vs interest |
| Owner draws as expense | Equity draw account |
| Own-account transfers as income/expense | Balance-sheet transfer only (cash ↔ cash) |
| Plugging a recon difference | Locate with ÷9 / ÷2 then date-range bisect |
| Leaving suspense at close | Empty before lock |
| Auto-add bank rules | Rules propose; human confirms except fixed single-vendor matches |
| Inventory expensed on payment under accrual | Asset on purchase, COGS on sale |
| Customer deposit as revenue | Deferred revenue until performance |

## Counter-examples

| Anti-pattern | Do this instead |
|---|---|
| Edit a posted entry inside a filed period | Reverse in an open period; amend only with a licensed professional |
| Report "how did we do" from unreconciled books | Finish bank/card/processor recon or state the uncertainty first |
| Answer growth or runway questions from open books | Close and lock, or hand closed figures to `cfo` |
| Store full IBAN / SSN / e-file PIN in memory | Store last-four + pointer string only |
| One COA account per vendor | Accounts for decisions; classes/tags for vendor detail |
| Start catch-up at the oldest month | Reconcile forward from last known-good |

## Security and privacy

- Default network behavior: no outbound calls. This skill is a local bookkeeping playbook and memory system.
- Local state: chart, coding rules, period status, asset register, filing history, and generated artifacts under `<state_root>`.
- Scope limits: accounting software, banks, payroll, and tax portals stay manual unless the user explicitly authorizes a specific action.
- Memory hygiene: nicknames, last four digits, tax registration numbers, ledger codes, and amounts only. Full account numbers, national IDs, e-file PINs, and software passwords stay outside skill memory (use pointer strings).
- Package integrity: leave skill package files unchanged during normal operation.
- Shared-box hygiene: rewrite only rows this skill authored; read other skills' rows without deleting them.

## Failure modes

### State root unresolved

If the host cannot supply `<workspace>` and no candidate directory exists, ask the user or host for an explicit state path before creating data.

### Multiple state copies

If more than one candidate exists, keep using the highest-precedence directory, report the conflict, and leave lower-precedence copies unchanged.

### Write failure

If a write fails, report the path and error, clean up partial files when safe, and pause further state changes until the user resolves the issue.

### Missing companion file

If the task needs a chart, asset register, filing log, or topic box that does not exist, create it from `assets/accountant-data-templates.md` only after the feature is needed.

### Trial balance or recon will not tie

Run the ÷9 and ÷2 tests, bisect by date range, then isolate import vs manual vs processor fee classes. If the difference grows across periods, switch to cleanup mode: load `references/audit-cleanup.md` and `references/escalate.md`, and mark statement answers as provisional until the break is explained.

### Escalate signal present

If any row in `references/escalate.md` matches, lead with that signal in one line, hold ordinary posting, and route to a licensed accountant, tax adviser, or counsel before the next entry.
