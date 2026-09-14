---
name: rental
description: Manage, negotiate, and review rentals for housing, vacation stays, or
  equipment with market analysis, scam detection, and lease review. Trigger for tenant
  search, landlord pricing/screening, Airbnb/VRBO host or guest workflows, car/tool
  rentals, lease red-flag review, or true-cost comparisons. Bypass pure real-estate
  investing, property development, or hotel loyalty strategy without a rental decision.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔑"}'
---

## State location

Optional rental tracking state may exist in `<workspace>/rental/`, `<workspace>/memory/rental/`, or `~/rental/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/rental/`, `<workspace>/memory/rental/`, `~/rental/`.
3. If none exists and state must be created, default to `<workspace>/rental/`.

Use the selected `<state_root>` for every state operation in this skill.
Create optional children only when needed:

| Path | Role |
|------|------|
| `<state_root>/memory.md` | Active role, search criteria, and short working notes |
| `<state_root>/properties/{slug}.md` | Tracked housing or vacation candidates |
| `<state_root>/leases/{slug}.md` | Lease-review notes and clause flags |
| `<state_root>/equipment/{slug}.md` | Equipment or vehicle rental comparisons |

## Roles

Load the matching guide based on the user's situation:

| Role | Guide | When to load |
|------|-------|--------------|
| Tenant | `references/tenant.md` | Finding housing, applications, lease review |
| Landlord | `references/landlord.md` | Pricing, screening, property management |
| Vacation Host | `references/vacation.md` | Airbnb/VRBO listing optimization |
| Vacation Guest | `references/vacation.md` | Booking and comparing vacation rentals |
| Equipment | `references/equipment.md` | Cars, tools, and gear rentals |
| Research sources | `references/sources.md` | Citing Gate 6 anchors or refreshing domain facts |

## Core Capabilities

**Search and analysis**
- Calculate true cost (rent + utilities + commute + fees)
- Compare properties or rentals side-by-side
- Detect scam patterns (below-market price, payment before viewing, out-of-country landlord pressure)

**Applications and negotiation**
- Prepare documentation checklists
- Draft application cover letters
- Research comparables for negotiation leverage

**Lease review**
- Flag problematic clauses (auto-renewal, excessive fees, entry without notice)
- Explain legal terms in plain language
- Remind the user that local statute controls; this skill is guidance, not legal advice

## Quick Commands

```text
Search for 2BR apartments in [area] under $2000
Calculate true monthly cost including commute to [workplace]
Review this lease for red flags
Help me negotiate rent down
Is this listing a scam?
```

## Operating Rules

1. Identify role first, then load only the needed reference file.
2. Prefer primary market and statute sources over generic blog advice; record full URLs when refreshing facts.
3. For lease or deposit disputes, surface red flags and recovery steps, then point the user to local tenant/landlord resources or counsel when stakes are high.
4. Keep session notes under `<state_root>/...` when the user wants continuity; otherwise keep guidance ephemeral.
5. Keep payment-card full numbers, government ID images, and raw credit-report files out of skill state; ask only for the minimum fields the workflow needs.
