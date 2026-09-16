# Entry format — subscriptions

Canonical fields for one subscription row under `<state_root>/active/`.

## Required fields

| Field | Meaning | Example |
|-------|---------|---------|
| Name | Service display name (heading) | `## Netflix` |
| Cost | Amount + period | `$15.49/month`, `$660/year` |
| Billing | Day/date cadence | `15th`, `Sep 15 annually` |
| Card / method | Last-four or pointer only | `Visa •4242`, `keychain:amex-travel` |
| Last used | Relative or ISO date | `Yesterday`, `2026-08-01` |
| Value | essential / high / medium / low | `High` |

## Optional fields

- Plan tier (Standard, Family, Pro)
- Seat count or household members covered
- Trial end date
- Cancel URL or in-app path the user already knows
- Notes (seasonal, shared family plan, employer-paid)

## Category routing

| File | Typical services |
|------|------------------|
| `active/streaming.md` | Video, music, games pass, news apps |
| `active/software.md` | SaaS, creative suites, cloud seats, developer tools |
| `active/services.md` | Delivery clubs, gym, storage, domain/email, misc memberships |

If a service spans categories, pick the primary spend purpose and keep a single row.

## Trials and free plans

- Track trial end date as the effective billing date
- When trial converts, rewrite Cost from `$0` to the paid amount the same day
- Free forever plans may stay out of totals unless the user wants inventory completeness

## Payment method hygiene

- Never store full PAN, CVV, OTP, or passwords
- Prefer `Visa •4242` or a secret manager pointer
- On card replacement, update the pointer only; leave historical cancelled rows unchanged
