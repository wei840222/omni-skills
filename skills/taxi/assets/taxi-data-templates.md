# Taxi state templates

Copy into the resolved `<state_root>/` only after the user asks to persist data.

## memory.md template

Copy to `<state_root>/memory.md`:

```markdown
# Taxi Preferences

## Saved Addresses
| Label | Address | Notes |
|-------|---------|-------|
| Home | | |
| Work | | |
| Airport | | Terminal preference |

## App Preferences
| App | Status | Notes |
|-----|--------|-------|
| Uber | | |
| Lyft | | |
| Bolt | | |
| Local: | | |

## Payment
- Preferred method nickname / last four:
- Business profile:
- Expense category default:

## Special Needs
- Wheelchair accessible: no
- Car seat needed: no
- Pet-friendly: no
- Preferred vehicle: standard

## Behavior
- Price sensitivity: medium
- Willing to wait for lower surge: yes
- Max acceptable surge: 2x
- Prefer scheduled rides: when possible
- Share trip tracking with:

---
*Last updated: YYYY-MM-DD*
```

## trips.md template

Copy to `<state_root>/trips.md`:

```markdown
# Trip History

## YYYY-MM

| Date | Route | App | Cost | Promo | Category | Notes |
|------|-------|-----|------|-------|----------|-------|

### Monthly Summary
- Total: $0
- Business: $0
- Personal: $0
- Promos saved: $0
```

## accounts.md template

Copy to `<state_root>/accounts.md`:

```markdown
# App Accounts

## Uber
- Email:
- Phone:
- Rating:
- Credits: $0
- Business profile: no

## Lyft
- Email:
- Rating:
- Credits: $0

## Referral Links
| App | Your code | Bonus |
|-----|-----------|-------|
```

## promos.md template

Copy to `<state_root>/promos.md`:

```markdown
# Active Promos

## Current Codes
| App | Code | Discount | Expires | Terms |
|-----|------|----------|---------|-------|

## Referral Credits
| App | Balance | Notes |
|-----|---------|-------|

## Sources to Check
- In-app offers and email receipts
- Credit card portal travel offers
- Student/corporate discounts
- Third-party aggregators (verify stacking rules in-app)

---
*Last checked: YYYY-MM-DD*
```
