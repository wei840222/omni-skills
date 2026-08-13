## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| home_currency | text (ISO 4217) | USD | Currency every total, budget and report converts to; entries always keep the currency actually paid alongside (Rule 3) |
| tax_year_start | text (MM-DD) | 01-01 | Boundary of the business year and the start of the retention clock |
| receipt_threshold | number (home currency) | 75 | Amount at or above which an entry is flagged incomplete without a receipt pointer (Rule 8) |
| close_day | number (1-28) | 1 | Day the previous month is closed and reported; writes the recurring row in the `## Due` table |
| settle_cadence | week \| month \| trip \| on_request | month | How often shared balances are netted and a settlement statement is offered |
| default_split | equal \| by_income \| custom | equal | Split applied when the user names people but not proportions |
| budget_alert_pct | number (50-100) | 80 | Share of an envelope at which spend is flagged, including committed-but-unpaid money |
| mileage_rate | number (home currency per km or mi) | none | Rate used to turn distance into money; while unset, verify the applicable official rate for the jurisdiction and tax year before quoting one |
| private_categories | list | none | Categories excluded from any shared, exported or household-level report; their totals fold into `other` |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Tooling** — how entries arrive (dictated in chat, a running inbox file, bank CSV import, receipt photos) and whether imports require review
- **Conventions** — category naming style, tag scheme for projects and trips, ledger cut (month vs week), and file naming for receipts
- **Platform** — jurisdiction and its retention and receipt rules, locale and date format, distance unit, and which cards and accounts exist
- **Safety posture** — what may leave the machine, which categories are private, and whether balances are shown to a group or only to the user
- **Output format** — report verbosity, whether every answer carries a trend line, and register (numbers-only vs commentary)
- **Cadence** — month close day, settlement rhythm, claim submission day, tax quarter dates, and budget review
- **Split policy** — standing rules per group (rent by room size, groceries equal, one person always fronts)

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Designing the category system before logging anything | Two weeks of design, zero entries, and the categories turn out wrong anyway because they were guessed | Log flat for two weeks, then derive categories from what actually appeared |
| Splitting round-robin — everyone pays everyone | A five-person trip can create an impractical number of transfers, so nobody finishes and the balances rot | Net first, then minimize transfers |
| Booking a refund as income | The category total is now wrong in both directions and the month reads as profitable | Negative entry against the original month and category (Rule 5) |
| Converting a foreign amount and keeping only the result | The original price is gone, so a disputed charge cannot be matched and the rate cannot be audited | Store original, rate, and rate date (Rule 3) |
| Reconstructing business purpose at tax time | Amounts survive reconstruction; purpose does not, and purpose is what is actually challenged | Write the purpose in the entry at payment (Rule 8) |
| Treating a project budget as spent-so-far | Signed quotes and deposits are already committed; the envelope is gone before the cash is | Track committed and paid separately |
| Accepting a terminal's offer to charge in the home currency | Dynamic currency conversion can add a markup on top of the card's own foreign-exchange charge | Pay in the local currency after comparing the disclosed options |
| Waiting for the full receipt pile before claiming | Employer claim windows can expire, turning a reimbursable expense into an unrecoverable cost | Submit partial packets on the configured cadence |
| One "shared" category for a couple or a flat | It answers how much was spent but not who owes whom | Record payer and beneficiaries per entry (Rule 4) |
| Recategorizing history "from now on" | Every month-over-month comparison across the boundary is silently invalid | Apply the change retroactively across the whole history, or retain the current categories (Rule 7) |
| Importing a bank CSV without a dedupe key | The same coffee can appear repeatedly across imports and the month becomes unusable | Dedupe on date, amount, and last four digits of the account |
| Guilt framing on a total | The user stops logging, which costs more than any single category ever did | Report the number and the trend; the judgment is theirs |

## Where Experts Disagree

- **Granular vs broad categories.** Broad categories survive years and get maintained; granular categories answer questions broad ones cannot. The frontier is decision value: split a category only when its own number would change a behavior, and use tags for everything else you want to slice by later.
- **Log everything vs log what matters.** Complete logs enable reconciliation and audits; partial logs (over a floor, say 10 units of home currency, plus all business and shared spend) survive longer because they cost less. A user who needs tax evidence or shared settlement has no choice — those must be complete; discretionary personal spend can run on a floor.
- **Split by income vs split equally.** Equal is defensible and frictionless; proportional may better reflect materially different incomes. Record the group rule before the first disagreement.
- **Cash tracking.** One school logs every cash purchase; the other withdraws a fixed amount, treats the withdrawal as spent, and never itemizes it. The second is more honest about what people actually sustain — but it destroys category data for the cash portion, which matters for anyone whose deductible spend is partly cash.
