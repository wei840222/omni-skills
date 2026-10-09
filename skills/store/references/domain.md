## Architecture

Memory lives in `<state_root>/` (see `SKILL.md` State location). If missing or empty, run `references/setup.md`. See `references/memory-template.md` for structure.

```text
<state_root>/
├── memory.md          # Status, store profile, active priorities
├── routines.md        # Opening, peak-hour, and closing standards
├── inventory.md       # Stock priorities, adjustments, replenishment notes
├── staff.md           # Roles, shift habits, coaching notes
├── kpis.md            # Sales, traffic, conversion, ticket, margin
├── promotions.md      # Offer goals, timing, execution notes
└── incidents.md       # Loss, customer issues, equipment, safety events
```

## Quick Reference

Load only the smallest playbook that matches the current store problem so the operating advice stays fast and specific.

| Topic | File | Use it for |
|-------|------|------------|
| Setup and activation flow | `references/setup.md` | Decide how proactively the store support should jump in |
| Memory structure and starter files | `references/memory-template.md` | Create local store notes without storing sensitive data |
| Opening and closing routines | `references/opening-closing.md` | Open strong, close clean, and prevent shift-to-shift drift |
| Inventory control rules | `references/inventory-control.md` | Cycle counts, replenishment priorities, and stock-out diagnosis |
| Floor management during the day | `references/floor-ops.md` | Peak-hour priorities, queue control, and recovery timing |
| Merchandising and promo execution | `references/merchandising.md` | Displays, signage, promo ownership, and sell-through checks |
| Scheduling and coaching | `references/staffing.md` | Shift coverage, coaching focus, and labor-pressure decisions |
| Cash, shrink, and incident handling | `references/cash-and-loss.md` | Till variance, loss signals, incidents, and escalation discipline |
| Weekly metrics and review rhythm | `references/metrics.md` | KPI review, action ownership, and next-week operating focus |

## Data Storage

Local store notes live in `<state_root>/`.
Before the first write in a session, explain the planned files in plain language and ask for confirmation.

## Core Rules

### 1. Protect Cash, Margin, and Stock First
- Treat cash handling, stock accuracy, and shrink prevention as the store's operating truth.
- A store can look busy while quietly losing money through poor controls.

### 2. Run the Store by Predictable Rhythm
- Separate the day into opening, trade hours, replenishment windows, and closing.
- Time tasks appropriately to ensure service and standards remain aligned.

### 3. Make Decisions from Store-Level Numbers
- Track sales, traffic, conversion, average ticket, gross margin, stock-outs, and labor hours.
- Base staffing, purchasing, and promotion recommendations entirely on specific metric justifications.

### 4. Keep Inventory Accurate Enough to Trust
- Recount fast-moving, high-value, and high-shrink items more often than the rest.
- Inventory records that drift even slightly ruin replenishment, promotions, and profit analysis.

### 5. Staff to Traffic and Mission
- Schedule around real demand peaks, delivery windows, and known task loads.
- Schedule hours to protect service during busy periods rather than defaulting to equal distribution.

### 6. Promotions Must Have a Clear Job
- Every promotion needs a goal: drive traffic, clear stock, raise basket size, or defend margin.
- If the offer has no owner, expiry, and success metric, treat it as noise.

### 7. Log Repeated Friction and Close the Loop
- Capture incidents, customer complaints, equipment issues, and recurring floor bottlenecks.
- Focus on eliminating the root cause of recurring problems rather than merely handling them faster.

## Common Traps

- Chasing total sales only -> margin, conversion, or labor productivity quietly deteriorate.
- Replenishing from memory -> empty pegs, overstock, and stock-outs compound together.
- Running promos without floor execution -> offer exists on paper but customers miss it completely.
- Scheduling by fixed habit -> busy hours get understaffed while quiet hours absorb payroll.
- Counting everything at month end only -> shrink and receiving errors become impossible to trace.
- Treating complaints as one-offs -> recurring service failures stay invisible.