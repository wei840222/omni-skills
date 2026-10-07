# Budget and Payments

Use this when budget anxiety, scope creep, or payment timing is the current bottleneck. Persist numbers to `<state_root>/weddings/{event}/budget.md` only after the user consents to durable notes.

## Budget Structure

Track four numbers separately:

- target ceiling
- currently committed spend
- already paid deposits
- remaining balances with due dates

That separation matters because a wedding can look "under budget" while still creating a cash-flow problem in the final month.

## Core Categories

Use one line per category:

| Category | Target | Committed | Paid | Remaining | Due Date | Notes |
|----------|--------|-----------|------|-----------|----------|-------|
| Venue | | | | | | |
| Catering | | | | | | |
| Photography | | | | | | |
| Flowers | | | | | | |
| Music | | | | | | |
| Attire | | | | | | |
| Rentals | | | | | | |
| Stationery | | | | | | |
| Beauty | | | | | | |
| Transport | | | | | | |
| Misc / contingency | | | | | | |

Category share benchmarks from commercial wedding media are market-specific and change yearly. Prefer the user's real quotes and ceiling over published average percentages. When citing any external average, open a live source the same session and label it as scenario input only.

## Decision Rules

- No upgrade is "small" if it creates budget drift in three categories at once.
- Protect a contingency line. Weddings almost always discover hidden labor, rush fees, or last-minute add-ons.
- When the user wants to add something, ask what gets reduced, delayed, or removed to pay for it.

## Payment Discipline

- Put every deposit and final balance on the backward timeline immediately.
- Mark which payments are non-refundable and which are only partially refundable.
- If family members are paying for something, record who owns the decision and who needs approval before a commitment is made.
- Never store full card numbers, CVVs, bank logins, or payment tokens in state. Last-four or a secret pointer only.
- Draft vendor acceptance or payment instructions for user review; do not send money or sign on the user's behalf.
