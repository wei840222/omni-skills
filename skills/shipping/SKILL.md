---
name: shipping
description: Optimize parcel shipping decisions across carrier selection, landed-cost math, HS code compliance, and delivery exception playbooks. Trigger when evaluating shipping options, quoting rates, preparing international documentation, or responding to carrier delays.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "\ud83d\udce6"}'
  related-skills: '{"ecommerce": "Store operations and conversion workflows.", "marketplace": "Multi-platform selling and fulfillment strategy.", "inventory": "Stock planning and replenishment control.", "sell": "Listing, pricing, and sales execution.", "buy": "Purchasing decisions and supplier-side evaluation."}'
---
## Setup

On first use, read `references/setup.md` for integration guidelines.

## State location

Shipping state may exist in `<workspace>/shipping/`, `<workspace>/memory/shipping/`, or `~/shipping/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/shipping/`, `<workspace>/memory/shipping/`, `~/shipping/`.
3. If none exists and state must be created, default to `<workspace>/shipping/`.

Use the selected `<state_root>` for every state operation in this skill.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for structure and status fields.

```text
<state_root>/
|- memory.md             # Durable shipping context and preferences
|- carrier-rules.md      # Preferred carriers and service constraints
|- international.md      # Country and customs notes
`- incidents.md          # Repeated failure patterns and resolutions
```

## Quick Reference

Load the smallest relevant reference for the current task on demand:

- `references/setup.md`: Load on first use to define primary carriers and operational context.
- `assets/memory-template.md`: Load when writing to `<state_root>/memory.md`.
- `references/carrier-selection.md`: Load when evaluating SLA options or calculating total landed cost.
- `references/international-customs.md`: Load before creating cross-border shipping documentation.
- `references/exception-playbook.md`: Load when responding to a delayed, lost, or damaged package.

## Core Rules

### 1. Confirm Shipment Profile First
Before recommending any option, confirm:
- Origin and destination
- Package count, dimensions, and weight
- Delivery deadline and budget ceiling
- Value, fragility, and regulatory constraints

Require all inputs before optimizing.

### 2. Price for Total Landed Cost
Show total cost rather than just carrier label price:
- Transport fee
- Packaging and handling
- Fuel, remote, residential, signature, and insurance surcharges
- Duties, taxes, and brokerage where applicable

If any component is unknown, mark it as estimate and show risk.

### 3. Select Carrier by SLA Risk Rather Than Sticker Price
Pick service based on the real failure cost:
- Time-critical shipment: prioritize reliability and claims process
- Low-value shipment: prioritize cost efficiency
- International shipment: prioritize customs support and tracking depth

State tradeoffs explicitly before final recommendation.

### 4. Validate Compliance Before Label Purchase
For cross-border shipments, verify:
- Commodity description and HS code quality
- Declared value consistency with invoice
- Prohibited or restricted item checks
- Incoterm and importer responsibilities

Halt when documentation is incomplete.

### 5. Run Tracking Checkpoints Proactively
Set checkpoints at minimum for:
- Label created without a scan within 24h
- Customs hold or pending documents
- Out for delivery delays beyond promised window

For each checkpoint, provide next action and owner.

### 6. Treat Exceptions as Playbooks Instead of Improvisation
Use a defined response path for lost, damaged, delayed, returned, or refused shipments:
- Capture facts and evidence first
- Notify customer with realistic timeline
- Open claim/escalation within carrier deadline
- Decide reshipment vs refund based on cost and SLA

### 7. Save Reusable Shipping Intelligence
After each meaningful case, update memory with:
- Carrier performance by route
- Recurring surcharge patterns
- Packaging failures and fixes
- Country-specific documentation pitfalls

This turns shipping from reactive to compounding.

## Common Traps

- Comparing rates without normalizing surcharges -> false savings and margin loss.
- Guessing box size from product photos -> dimensional weight surprises.
- Declaring vague item descriptions -> customs holds and rejections.
- Promising delivery dates without scan confirmation -> avoidable support escalations.
- Filing claims without evidence package -> denied reimbursement.
- Treating every delay as carrier fault -> misses internal pick-pack bottlenecks.

## Security & Privacy

**Data that leaves your machine:**
- None by default from this skill itself.

**Data that stays local:**
- Shipping context and learned patterns under `<state_root>/`.

**This skill does NOT:**
- Access undeclared external services automatically.
- Buy labels or place shipping orders automatically.
- Retrieve tracking events from carrier APIs automatically.
- Store payment credentials or full card data.
- Modify files outside `<state_root>/` for memory.
