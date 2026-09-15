---
name: inventory
description: Maintain a markdown-based personal inventory system in <state_root>/inventory/ for tracking valuable items, locations, warranties, and insurance claims. Trigger when the user mentions acquiring new valuables or asks where an item is located.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"📦"}'
  related-skills:
    home: skills/home
---

## State location

Inventory records are persistent user state. Before reading or writing them, resolve `<state_root>` once for this invocation:

1. Use a user- or host-configured state root when one is explicitly provided.
2. Otherwise use the first existing directory in this order: `<workspace>/inventory/`, `<workspace>/memory/inventory/`, then `~/inventory/`.
3. If more than one candidate exists, use only the highest-precedence directory and report the duplicate state locations; do not merge or synchronize them.
4. If none exists and the user confirms saving inventory data, create `<workspace>/inventory/`. If `<workspace>` is unavailable, ask for a state root instead of guessing from the current directory.

Use the selected `<state_root>` for every inventory read or write. Keep skill resources under `references/`; never treat them as mutable user state.

## When to load

Load this skill when the user mentions acquiring valuables, asks to locate an item, needs warranty follow-up, or prepares an insurance claim or move. Focus on electronics, jewelry, items with warranties, and easily lost durable goods.

## Core behavior

- User mentions owning something valuable → offer to catalog
- Track location, value, warranty → keep items findable and insurable
- Moving or decluttering → surface relevant items from the resolved inventory tree
- Create `<state_root>/inventory/` only after the state-root resolution above

For source-backed insurance and documentation notes, load `references/sources.md`.

## Item entry

Record at least:

- Name and description
- Location: room, drawer, box, storage unit
- Purchase date and price when known
- Current estimated value
- Photo for identification when available
- Receipt or warranty details when available

## File structure

```text
<state_root>/inventory/
|-- electronics/
|   |-- macbook-pro-2023.md
|   `-- tv-living-room.md
|-- kitchen/
|-- garage/
|-- storage/
|-- index.md
`-- for-insurance.md
```

## Location tracking

- Be specific: "garage, shelf 3, red toolbox"
- Update when moved — stale locations frustrate later lookup
- "Where is X?" should have an instant answer from the inventory files
- Seasonal items: note when stored or retrieved

## Value tracking

- Purchase price vs current estimated value
- Depreciation for electronics: a rough estimate is enough
- Appreciation for collectibles: update periodically
- Total insured value: sum relevant items for insurance purposes

## Warranty management

- Expiration date
- Coverage scope
- Claim path
- Registration confirmation
- Follow up before a warranty expires

## Photos and evidence

- One clear photo minimum for valuables
- Serial number visible when applicable
- Condition documentation for insurance
- Store photos in the item folder or link them from the item file

## Progressive enhancement

- Week 1: catalog high-value items only
- Week 2: add electronics with warranties
- Month 2: room-by-room inventory
- Yearly: audit and update values

## Insurance preparation

- Generate a list of items over a user-chosen value threshold
- Calculate total replacement value
- Keep photos and receipts organized under the resolved tree
- Update after major purchases

## Moving support

- Filter by room: what is in the bedroom?
- Box tracking: which box holds what
- Unpacking checklist: verify arrival
- Update locations after the move

## Decluttering support

- Filter by last-used date when tracked
- Surface long-unused candidates for review
- Value check before selling
- Donation tracking for tax purposes when the user asks

## Serial numbers and receipts

- Serial numbers for electronics support theft recovery
- Link receipt photos or PDFs
- Save purchase confirmation references when available
- Note AppleCare or other extended warranties

## What to surface

- "Warranty expires next month on dishwasher"
- "You have 3 HDMI cables in the office drawer"
- "Total electronics value: €X"
- "When did I buy the drill?" → answer from the inventory file

## Categories

- Electronics: computers, phones, TVs, audio
- Appliances: kitchen, laundry, climate
- Furniture: major pieces worth insuring
- Tools: power tools especially
- Valuables: jewelry, watches, art
- Collections: books, records, games
- Outdoor: bikes, sports equipment

## Reliable defaults

| Prefer | Practice |
| --- | --- |
| Valuable or easily lost items | Skip cataloging every small consumable |
| Simple markdown under `<state_root>` | Avoid complex asset-management software unless the user asks |
| Durable goods | Redirect consumables to a shopping-list workflow |
| Confirm before bulk moves | Keep reorganization reversible |

## Lending tracking

- Item lent to whom and when
- Expected return date
- Follow up on unreturned items
- "Who has my drill?" → answer from inventory notes

## Maintenance tracking

- Items needing regular maintenance
- Last serviced date
- Service schedule such as HVAC filters
- Link to home-maintenance context via `skills/home` when relevant

## Integration points

- Home: maintenance schedules (`skills/home`)
- Receipts: purchase documentation
- Insurance: claims preparation
- Moving: box contents tracking
