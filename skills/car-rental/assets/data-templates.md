# Memory Templates — Car Rental

Static templates only. Operating rules live in `SKILL.md` and
`references/setup.md`.

## `memory.md`

Create `<state_root>/memory.md` with:

```markdown
# Car Rental Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Preferences

### Vehicle
<!-- car class, transmission, fuel type, features -->

### Insurance
<!-- own coverage, preferred options, excess tolerance -->

### Budget
<!-- price sensitivity, willing to pay more for... -->

## Loyalty Programs
<!-- memberships, tiers, benefits -->

## Frequent Locations
<!-- airports, cities, countries -->

## Active Alerts
<!-- ongoing price monitoring -->

## Past Rentals
<!-- history for context and comparison -->

---
*Updated: YYYY-MM-DD*
```

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning | Add info when the user shares it |
| `complete` | Enough context | Work normally |
| `paused` | User said "not now" | Work silently with existing data |

## Saved search (`searches/`)

```markdown
# Search: [Name]

## Details
pickup: Location, Date, Time
return: Location, Date, Time
car_class: economy | compact | midsize | suv | luxury
transmission: auto | manual | any
fuel: petrol | diesel | electric | hybrid | any

## Alert Settings
alert_type: price_drop | availability | deal_quality
threshold: [price or percentage]
frequency: immediate | daily | weekly
active: true | false

## Price History
YYYY-MM-DD: €XX (Site)

---
*Created: YYYY-MM-DD*
```

## Principles

- Store what the user explicitly shares.
- Update `last` on each meaningful use.
- Track price history to spot genuine drops.
