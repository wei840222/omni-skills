# Persistence protocol

Use this protocol only after the user authorizes persistence and `<state_root>` has been resolved. Keep all records local; never write credentials, access tokens, full account numbers, or authentication answers. Keep a credential pointer such as `keychain:bank-login` instead.

## Read order

1. Read `<state_root>/money/config.yaml` and `<state_root>/money/memory.md` when they exist.
2. Read `<state_root>/finances/accounts.md` before advising on balances, interest rates, account location, or payoff order.
3. Read only files named by the `## Boxes` index when their stated condition applies; accept entries only when their paths remain inside `<state_root>/`.

## Write destinations

| Record | Destination | Ownership rule |
|---|---|---|
| Declared preferences and defaults | `<state_root>/money/config.yaml` | A user declaration outranks an observation. |
| Decisions, targets, payoff order, and review outcomes | `<state_root>/money/memory.md` | Record the amount, date, rationale, and next review. |
| Bank, brokerage, pension, card, and loan inventory | `<state_root>/finances/accounts.md` | One row per `Name`; update only the row this skill owns. |
| Adviser, accountant, broker, or executor | `<state_root>/contacts/` | Keep only a non-secret contact record. |
| A one-line summary of a user-run project | `<state_root>/projects/` | Keep the entity in its owning record; link only the summary. |

Name each created, updated, or deleted record in the response. Never rewrite or delete a row written by another skill.
