---
name: store
description: >
  Run physical retail operations: opening/closing routines, inventory accuracy,
  staffing to traffic, cash/shrink control, merchandising, and weekly KPI reviews.
  Use for boutiques, convenience stores, specialty retail, showrooms, kiosks, or
  multi-shift brick-and-mortar shops that need floor execution. Not for pure
  ecommerce ops, generic business strategy without a store floor, or payments
  provider integration.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏬"}'
  related-skills: '{"business":"Strategic validation, unit economics, and irreversible decisions beyond day-to-day floor ops.","payments":"Payment-provider and tender-flow mechanics when POS outages or refund rails need product detail.","accounting":"Books, COGS, and financial close when store KPIs must connect to formal accounting.","customer-support":"Post-purchase complaint handling and service recovery scripts beyond floor incident notes.","management":"People-management frameworks for coaching, feedback, and team conflict beyond shift staffing."}'
---

# Store

Physical-store operating judgment for cash, stock, labor, service, and weekly review.
Keep package files under `references/`. Durable store notes live only under a resolved `<state_root>`.

## State location

Store state may exist in `<workspace>/store/`, `<workspace>/memory/store/`, or `~/store/`.
`<workspace>` means the workspace root provided by the host/runtime, not the shell cwd.

Before any state read or write, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/store/`, `<workspace>/memory/store/`, `~/store/`.
3. If multiple candidates exist, keep only the highest-precedence directory, leave others untouched, and tell the user which location was selected.
4. If none exists and persistent state must be created, default to `<workspace>/store/` after brief first-write consent.
5. If `<workspace>` cannot be resolved, read an existing `~/store/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state path in this skill. Resolve it to a real path before filesystem work. Create or update files under `<state_root>/` only after plain-language consent. Never write card numbers, PINs, payroll secrets, or unnecessary personal identifiers into state files.

Template and first-use flow: `references/memory-template.md`, `references/setup.md`.

## When to use

- Opening, peak-hour, and closing routines for a physical shop
- Stock-outs, cycle counts, replenishment, receiving mismatches
- Scheduling to traffic, role coverage, coaching on conversion/basket
- Cash variance, shrink signals, incident logging, promo floor execution
- Weekly review of sales, traffic, conversion, ticket, margin, labor, stock-outs

Route away when the task is mainly:

- idea validation / unit economics without a floor → `business`
- payment-provider APIs or tender product setup → `payments`
- formal books / COGS close → `accounting`
- ticketed post-purchase support workflows → `customer-support`
- people-management systems beyond shift ops → `management`

## When to load references

Keep `SKILL.md` as the entry point. Load supporting files only when needed:

| Reference | Load when |
|---|---|
| `references/domain.md` | Architecture, core rules, common traps, quick map |
| `references/setup.md` | First use, activation preference, store-shape intake |
| `references/memory-template.md` | Creating consented local note files under `<state_root>/` |
| `references/opening-closing.md` | Open/close checklists and bookend competence |
| `references/inventory-control.md` | Cycle counts, replenishment, stock-out diagnosis |
| `references/floor-ops.md` | Peak coverage, queue control, recovery timing |
| `references/merchandising.md` | Displays, signage, promo ownership and sell-through |
| `references/staffing.md` | Schedules, coaching focus, labor pressure |
| `references/cash-and-loss.md` | Till variance, shrink, incidents, escalation |
| `references/metrics.md` | Weekly KPI review sequence and pattern reads |
| `references/sources.md` | Verify retail-ops claims against primary URLs |

## Operating loop

1. **Classify the live store problem** — cash/stock, service/queue, labor, promo, or weekly review.
2. **Load the smallest matching reference** — do not dump every playbook.
3. **Decide from store-level numbers** — name the metric behind staffing, purchase, or promo moves.
4. **Protect cash, margin, and stock first** — service still matters, but weak controls quietly erase busy days.
5. **Leave one owned next action** — owner, timing, and how success will be checked.
6. **Persist only consented notes** under `<state_root>/`; keep package files immutable.

## Core rules

1. **Protect cash, margin, and stock first** — treat controls as operating truth, not admin afterthoughts.
2. **Run by rhythm** — opening, trade, replenishment windows, closing; right task at the right moment.
3. **Staff to traffic and mission** — equal hours is not fairness if peaks fail.
4. **Count what moves and what leaks** — fast movers, high value, high shrink, active promo lines.
5. **Promotions need a job** — traffic, clearance, basket, or margin defense with owner, expiry, and metric.
6. **Log repeated friction** — incidents and complaints are signals; close root causes, not only speed.

## Failure recovery

| Failure | Recovery |
|---|---|
| User wants durable notes but no writable state root | Ask for an authorized path; do not write outside `<state_root>` |
| System stock disagrees with shelf | Cycle-count the SKU family; check receiving, back stock, damage, theft signals (`references/inventory-control.md`) |
| Peak chaos | Collapse to service, queue, cash, visible gaps; name one shift lead (`references/floor-ops.md`) |
| Till variance | Stop and document before continuing the shift (`references/cash-and-loss.md`) |
| Promo not converting | Verify price/sign/placement/owner before blaming staff (`references/merchandising.md`) |
| Missing baseline KPIs | Say what is missing; do not invent sales, traffic, or margin figures |

## Security & privacy

- Instruction-only, local-first. No external network calls required by this skill.
- State may hold store profile, routines, KPI snapshots, staffing patterns, stock notes, promotions, and incident logs under `<state_root>/store` layout described in `references/domain.md` (files live directly under `<state_root>/` as listed in the template).
- Exclude raw card data, PINs, payment credentials, and unnecessary employee/customer personal identifiers.
- Treat skill package files as immutable; user data stays in `<state_root>/`.
