# Setup — Walmart

Answer the current Walmart shopping question first. Only create durable state
after the user opts in.

## Resolve state first

Follow the State location section in `SKILL.md` before any create/read/write:

1. Prefer an explicit configured path when one exists.
2. Otherwise use the first existing candidate:
   `<workspace>/walmart/`, `<workspace>/memory/walmart/`, `~/walmart/`.
3. If several candidates exist, keep only the highest-precedence root and report
   the others; do not merge.
4. If none exists and durable notes are wanted, propose
   `<workspace>/walmart/` when `<workspace>` is available; otherwise ask for a
   path. Never invent a root from the current working directory.
5. If older notes exist only at `~/Clawic/data/walmart/`, propose a
   copy → validate → cutover plan and wait for confirmation before migration.

Never write the literal string `<state_root>` to disk.

## Storage notice

On first activation, tell the user:

- local Walmart planning notes can live under the resolved `<state_root>/`
- those notes are only for repeat ordering context (store choice, staples,
  substitution rules, recovery outcomes)
- passwords, card data, insurance data, and prescription identifiers stay out of
  local storage and out of chat

If the user declines memory, keep helping in one-off mode.

## Integration preference

Ask how this skill should activate:

- only when the user explicitly mentions Walmart
- for grocery / household restock requests where Walmart is the preferred store

## Automation preference

Ask which operating mode is allowed:

- planning only (default)
- browser-assisted execution on Walmart.com with a user-provided runtime
- seller-side Marketplace API work

Do not escalate beyond planning until the user explicitly approves.

## Household basics

Capture only what improves the next order:

- who the basket serves
- preferred Walmart store or delivery area
- usual order mode: pickup, delivery, shipping, or mixed
- weekly restock rhythm and budget guardrails
- preferred entry path: Purchase History, My Items, fresh cart, or seller API

## Substitution boundaries

Establish hard rules first:

- allergy-sensitive items
- baby formula / infant food
- pet food with brand or ingredient restrictions
- pharmacy / health-critical items
- brand-locked household staples

Then seed flexible swaps for produce, pantry staples, paper goods, and cleaning
items using `references/substitutions-playbook.md`.

## Seed files

After consent, create only the files needed now using
`assets/data-templates.md`:

1. `<state_root>/memory.md` (required for durable use)
2. `<state_root>/weekly-cart.md` when an active basket exists
3. `<state_root>/order-log.md` after the first completed or failed order
4. `<state_root>/exceptions.md` when hard substitution or pharmacy rules appear

Help immediately while setup runs; do not block the first useful answer on a
full memory interview.
