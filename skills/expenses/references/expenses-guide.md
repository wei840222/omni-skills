## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `~/Clawic/data/expenses/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| home_currency | text (ISO 4217) | `profile.yaml` currency, else USD | Currency every total, budget and report converts to; entries always keep the currency actually paid alongside (Rule 3) |
| tax_year_start | text (MM-DD) | 01-01 | Boundary of the business year in `reports.md` and the start of the retention clock in `receipts.md` |
| receipt_threshold | number (home currency) | 75 | Amount at or above which an entry is flagged incomplete without a receipt pointer (Rule 8) |
| close_day | number (1-28) | 1 | Day the previous month is closed and reported; writes the recurring row in the `## Due` table |
| settle_cadence | week \| month \| trip \| on_request | month | How often shared balances are netted and a settlement statement is offered (`sharing.md`) |
| default_split | equal \| by_income \| custom | equal | Split applied when the user names people but not proportions (`sharing.md`) |
| budget_alert_pct | number (50-100) | 80 | Share of an envelope at which spend is flagged unprompted, including committed-but-unpaid money (`budgets.md`) |
| mileage_rate | number (home currency per km or mi) | none | Rate used to turn distance into money; while unset, say that the jurisdiction's official rate for the year (such as the IRS standard mileage rate for business use of a vehicle in the US, defined under 26 U.S.C. § 162) must be checked before quoting one (`reimbursement.md`) |
| private_categories | list | none | Categories excluded from any shared, exported or household-level report; their totals fold into `other` |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Tooling** — how entries arrive (dictated in chat, a running inbox file, bank CSV import, receipt photos) and whether imports are trusted without review — affects `capture.md` and `reconciliation.md`
- **Conventions** — category naming style, tag scheme for projects and trips, ledger cut (month vs week), file naming for receipts — affects `categories.md` and `receipts.md`
- **Platform** — jurisdiction and its retention and receipt rules, locale and date format, distance unit, which cards and accounts exist — affects `business.md`, `receipts.md` and `reimbursement.md`
- **Safety posture** — what may leave the machine, which categories are private, whether balances are shown to a group or only to the user — affects `reports.md` and `sharing.md`
- **Output format** — report verbosity, whether every answer carries a trend line, register (numbers-only vs commentary) — affects `reports.md`
- **Cadence** — month close day, settlement rhythm, claim submission day, tax quarter dates, budget review — affects the `## Due` table
- **Split policy** — standing rules per group (rent by room size, groceries equal, one person always fronts) — affects `sharing.md`

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Designing the category system before logging anything | Two weeks of design, zero entries, and the categories turn out wrong anyway because they were guessed | Log flat for two weeks, then derive categories from what actually appeared (`categories.md`) |
| Splitting round-robin — everyone pays everyone | A five-person trip settles in up to 20 transfers, so nobody finishes and the balances rot | Net first, then minimize: any group of n settles in at most n−1 transfers (`sharing.md`) |
| Booking a refund as income | The category total is now wrong in both directions and the month reads as profitable | Negative entry against the original month and category (Rule 5) |
| Converting a foreign amount and keeping only the result | The original price is gone, so a disputed charge cannot be matched and the rate cannot be audited | Store original, rate, rate date (Rule 3, `currency.md`) |
| Reconstructing business purpose at tax time | Amounts survive reconstruction; purpose does not, and purpose is what is actually challenged | Write the purpose in the entry at payment (Rule 8, `business.md`) |
| Treating a project budget as spent-so-far | Signed quotes and deposits are already committed; the envelope is gone before the cash is | Track committed and paid separately (`budgets.md`) |
| Accepting the terminal's offer to charge in your home currency | Dynamic currency conversion embeds a markup, commonly 3-7%, on top of the card's own FX | Always pay in the local currency (`travel.md`) |
| Waiting for the full receipt pile before claiming | Employer claim windows expire, commonly 30-90 days; an expired claim is a donation | Submit on `close_day` cadence, partial packets included (`reimbursement.md`) |
| One "shared" category for a couple or a flat | It answers how much was spent but never who owes whom, which is the only question that gets asked | Payer plus beneficiaries per entry (Rule 4) |
| Recategorizing history "from now on" | Every month-over-month comparison across the boundary is silently invalid | Retroactive across the whole history, or not at all (Rule 7) |
| Importing a bank CSV without a dedupe key | The same coffee appears three times across three imports and the month is unusable | Dedupe on date + amount + last four of the account (`reconciliation.md`) |
| Guilt framing on a total | The user stops logging, which costs more than any single category ever did | Report the number and the trend; the judgment is theirs |

## Where Experts Disagree

- **Granular vs broad categories.** Broad (8-15) survives years and gets maintained; granular answers questions broad cannot ("coffee", "kids' activities"). The frontier is decision value: split a category only when its own number would change a behavior, and use tags for everything else you want to slice by later (`categories.md`).
- **Log everything vs log what matters.** Complete logs enable reconciliation and audits; partial logs (over a floor, say 10 units of home currency, plus all business and shared spend) survive longer because they cost less. A user who needs tax evidence or shared settlement has no choice — those must be complete; discretionary personal spend can run on a floor.
- **Split by income vs split equally.** Equal is defensible and frictionless; proportional is fairer when incomes differ by more than roughly 2×, and it is the standing rule that most often goes unwritten and then gets relitigated. Whichever is chosen, write it down as a group rule before the first disagreement, not during it (`sharing.md`).
- **Cash tracking.** One school logs every cash purchase; the other withdraws a fixed amount, treats the withdrawal as spent, and never itemizes it. The second is more honest about what people actually sustain — but it destroys category data for the cash portion, which matters for anyone whose deductible spend is partly cash.
