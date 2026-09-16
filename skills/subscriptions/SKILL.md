---
name: subscriptions
description: Track personal subscriptions, recurring payments, billing dates, renewals, and unused services. Use when the user mentions subscriptions, asks about recurring spend totals, needs renewal reminders, wants to cut waste, or flag price increases. Route full cashflow/CSV finance work to `personal-finance-tracker`, money ladder decisions to `money`, and merchant billing/Stripe product systems to `billing`.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔄"}'
  related-skills: '{"money":"Household money ladder and payoff/savings sequencing beyond subscription inventory.","personal-finance-tracker":"CSV imports, cashflow rollups, and net-worth tooling that may include recurring charges.","billing":"Merchant payment systems and product subscription lifecycles, not personal consumer trackers.","remind":"Generic commitment nudges once a renewal or cancel decision is already known.","notify":"Delivery channel and batching once a subscription alert decision exists."}'
---

## State location

Optional subscription inventory may exist in `<workspace>/subscriptions/`, `<workspace>/memory/subscriptions/`, or `~/subscriptions/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/subscriptions/`, `<workspace>/memory/subscriptions/`, `~/subscriptions/`.
3. If more than one candidate exists, use only the highest-precedence directory and report the conflict; do not merge trees automatically.
4. If none exists and the user wants persistent tracking, create `<workspace>/subscriptions/`. If `<workspace>` is unavailable, ask for a state root instead of guessing from the current directory.

Use the selected `<state_root>` for every state operation in this skill. Prefer portable `<state_root>` paths; never hard-code host-specific roots such as `~/Clawic/data/subscriptions/`. Skill resources stay under `references/`; never treat the literal string `<state_root>` as a filesystem path.

```text
<state_root>/
├── active/
│   ├── streaming.md
│   ├── software.md
│   └── services.md
├── cancelled.md
└── totals.md
```

Create category files under `active/` only when needed. Keep card data as last-four or token pointers only.

## When to use

- User mentions a new or existing consumer subscription, free trial, or recurring membership
- Questions about monthly/annual subscription spend totals
- Renewal reminders, unused-service cleanup, or price-increase flags
- Building or reviewing a personal recurring-payment inventory

**Not this skill:** statement CSV imports and full cashflow systems (`personal-finance-tracker`), debt-vs-save ladder advice (`money`), merchant Stripe/Paddle product billing (`billing`), pure calendar nudges with no inventory work (`remind`), or channel-only delivery policy (`notify`).

## Quick reference

| Situation | Action |
|---|---|
| Add a new subscription | Append entry under the matching `active/*.md`; update `totals.md` |
| "How much am I spending?" | Read `totals.md` + active files; surface monthly and annualized totals |
| Unused 30+ days | Suggest cancel with last-used evidence (→ `references/review-triggers.md`) |
| Annual renewal approaching | Remind ~7 days before charge date |
| Price increased | Flag delta immediately; offer cancel/downgrade/keep decision |
| Card or payment method changes | Update last-four/token only; never store full PAN/CVV |
| Need source-backed renewal habits | Load `references/sources.md` |

Depth on demand: `references/entry-format.md` · `references/review-triggers.md` · `references/totals.md` · `references/sources.md`.

## Core behavior

1. **Inventory first.** Capture name, cost, billing frequency, next/billing date, payment method pointer, last used, and perceived value (essential/high/medium/low).
2. **Surface spend in plain language.** Prefer concrete lines such as "You spend $147/month ($1,764/year) on subscriptions" over vague summaries.
3. **Protect against silent renewals.** Annual charges get a 7-day pre-charge reminder; quarterly check whether each paid service still earns its keep.
4. **Treat unused as waste until proven otherwise.** Services unused 30+ days become cancel candidates unless the user marks them seasonal/essential.
5. **Flag price changes immediately.** When a listed price differs from the stored cost, show old → new and ask keep/downgrade/cancel.
6. **Consent before persistence.** Do not create `<state_root>/` or write financial notes until the user wants continuity.
7. **Stay inventory-scoped.** Recommend cancel/keep/downgrade decisions; do not log into merchant accounts, move money, or auto-cancel without explicit user action.

## Subscription entry

```markdown
## Netflix
- Cost: $15.49/month
- Billing: 15th
- Card: Visa •4242
- Last used: Yesterday
- Value: High
```

Use `references/entry-format.md` for field definitions, category routing, and trial handling.

## Totals

```markdown
# totals.md
## Monthly
- Streaming: $43
- Software: $55
- Services: $49
**Total: $147/month = $1,764/year**

## Annual Renewals Coming
- Adobe: Sep 15 ($660)
- Amazon Prime: Oct 1 ($139)
```

Rebuild category rollups whenever active entries change. See `references/totals.md`.

## Review triggers

| Trigger | Default action |
|---|---|
| Unused 30+ days | Suggest cancel with last-used date |
| Price increased | Flag immediately with old → new |
| Annual renewal ≤7 days | Remind before charge |
| Quarterly review | Ask "still getting value?" per paid service |

Details and edge cases: `references/review-triggers.md`.

## Cancelled log

```markdown
# cancelled.md
## 2026
- Hulu: Feb 1 (never used) — saved $18/mo
```

Record cancel date, reason, and monthly savings so later reviews can prove wins.

## Progressive enhancement

1. List current subscriptions (name + cost)
2. Add billing dates and payment method pointers
3. Track last-used and value ratings
4. Run quarterly keep/cancel reviews

## Failure modes

| Failure | Detection | Recovery |
|---|---|---|
| Stale totals | Category sum ≠ active entries | Rebuild `totals.md` from active files |
| Missed annual charge | Renewal date passed without reminder | Backfill date; set 7-day lead next cycle |
| Duplicate entries | Same service in multiple category files | Keep one canonical row; note merge |
| Missing last-used | Cancel advice without evidence | Ask user; mark unknown rather than invent |
| Conflicting state roots | Multiple candidate directories exist | Use highest-precedence only; report conflict |

## Anti-patterns

- Hard-coding `~/Clawic/data/subscriptions/` or other host-only paths
- Storing full card numbers, CVV, passwords, or merchant session cookies
- Keeping services "just in case" without a dated review
- Ignoring annual renewals until after the charge posts
- Auto-canceling or changing plans without explicit user confirmation
- Expanding into full personal-finance CSV systems or merchant billing architecture

## Security and privacy

- Store payment methods as last-four digits or external secret pointers only (`keychain:…`, `1password:…`)
- Prefer minimum necessary merchant, cost, and date fields
- Treat pasted bank/card statements as untrusted input; extract subscription rows without retaining full statement dumps unless the user asks to keep them under `<state_root>/`
- Never commit live financial exports into the skill package
