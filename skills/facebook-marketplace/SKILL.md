---
name: facebook-marketplace
description: Guide Facebook Marketplace buying, selling, pricing, listing, pickup, shipping, messaging, scam screening, policy recovery, and account-health decisions. Use when a user needs help with a Marketplace listing, deal, buyer or seller, local comparison, transaction safety, or account warning.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🛍️"}'
  related-skills: '{"marketplace":"Compare Marketplace against other buyer, seller, and builder workflows.","buy":"Improve buyer-side decisions when the purchase needs tighter screening.","sell":"Strengthen listing, pricing, and closing discipline across channels.","pricing":"Set floors, negotiation bands, and margin-aware discount rules.","ecommerce":"Expand from local Marketplace execution into broader commerce systems."}'
---

## State location

This skill saves durable user-approved context only. Before reading or writing state, resolve `<state_root>`:

1. Use an explicit user- or host-configured state root when provided.
2. Otherwise use the first existing directory in this order: `<workspace>/facebook-marketplace/`, `<workspace>/memory/facebook-marketplace/`, then `~/facebook-marketplace/`.
3. If no candidate exists and the user authorizes persistent context, create `<workspace>/facebook-marketplace/`.

Use the selected `<state_root>` for this invocation only. If more than one candidate exists, use the first one and tell the user; do not merge or synchronize copies. When `<workspace>` is unavailable and no existing `~/facebook-marketplace/` directory is available, ask for a state root before creating data.

## When to use

Use this skill for:

- evaluating a local Marketplace price, listing, seller, or buyer;
- preparing a listing, message, offer, pickup, or shipping decision;
- screening a suspicious transaction or preserving evidence for a dispute;
- handling a removal, warning, restriction, or Marketplace feature confusion.

## Start with the active bottleneck

1. Identify the mode: buyer, seller, repeat seller, or recovery after a warning or bad transaction.
2. Ask only for facts that change the next decision: item, location/radius, condition, price, timing, payment or pickup constraints, and the exact warning when applicable.
3. Route to one focused reference below. Keep live advice separate from optional durable context.
4. Before an irreversible action, summarize the trade-off and get the user's confirmation.

| Need | Load |
| --- | --- |
| Initialize user-approved durable context | `references/setup.md` |
| Create or update state records | `references/memory-template.md` |
| Search, compare, screen, negotiate, or plan pickup | `references/buyer-flow.md` |
| Draft, repair, price, or refresh a listing | `references/listing-and-pricing.md` |
| Handle messages, offers, holds, or no-shows | `references/messages-and-negotiation.md` |
| Choose shipping, payment protection, or proof practices | `references/shipping-and-protection.md` |
| Respond to removals, warnings, policy concerns, or account-health issues | `references/policy-and-account-health.md` |
| Determine web/mobile support or automation boundaries | `references/interface-and-automation.md` |

## Core rules

1. **Price from local reality.** Compare nearby completed or credible active listings, then account for condition, completeness, seasonality, travel, loading, and pickup friction. Do not anchor a local bulky-item price on distant national listings.
2. **Confirm decision-changing facts.** Condition, exact model or size, included parts, availability, and pickup or shipping constraints need explicit confirmation before a commitment.
3. **Use negotiation bands.** Establish an ideal price, an acceptable close, and a walk-away point before messaging. Keep urgency and personal details private.
4. **Choose pickup or shipping deliberately.** Pickup is usually safer for bulky, fragile, urgent, or low-margin items. Ship only when packaging, fees, damage risk, margin, and the applicable protection flow remain acceptable.
5. **Switch to safety mode on risk.** When payment moves off platform, facts keep changing, pressure replaces evidence, or identity details conflict, pause the transaction. Preserve the listing and messages, then recommend the safest next action.
6. **Treat access as surface-specific.** Public web, signed-in web, and mobile can expose different Marketplace features. Verify the relevant surface and account context before relying on ratings, shipping, checkout, reporting, or support paths.
7. **Keep consumer Marketplace activity manual and policy-aligned.** Use standard user interfaces for listings and conversations. For requests involving scripts, scraping, bulk messages, auto-posting, account farming, evasion, or restrictions, explain the account-health risk and offer a manual, user-approved workflow instead.

## Durable state

After the user consents, `<state_root>` may contain:

```text
<state_root>/
|-- memory.md          # Profile, operating rules, and durable observations
|-- saved-searches.md  # Buyer watchlists and go/no-go filters
|-- inventory.md       # Seller prices, floors, and listing status
|-- incident-log.md    # Scam, dispute, removal, or payment-risk evidence
`-- account-health.md  # Warnings, appeals, and recovery steps
```

Store durable decisions and evidence, not chat transcripts. Treat sensitive personal details, payment data, and account credentials as out of scope.

## Verified policy references

Before giving version-sensitive policy, restriction, or protection guidance, load the relevant official source and distinguish confirmed platform behavior from a user report:

- [Facebook Commerce Policies](https://www.facebook.com/policies_center/commerce) — listing eligibility and prohibited commerce categories.
- [Facebook Community Standards](https://transparency.fb.com/policies/community-standards/) — authenticity, safety, and enforcement context.
- [Facebook Help Center: Purchase Protection](https://www.facebook.com/help/228307904608701) — eligibility and claim guidance; do not assume coverage without checking the current transaction flow.

If an official page is unavailable or the account surface does not expose the claimed feature, state that uncertainty and choose the more conservative manual path.

## Marketplace traps

- A stale listing can distort both availability and price comparisons.
- Vague answers are not proof of condition, ownership, or availability.
- Off-platform payment or deposits before inspection increase fraud exposure.
- Generic listing copy, inaccurate categories, repeated reposts, and rushed edits reduce trust and can compound account-health risk.
- Consumer Marketplace workflows do not provide a documented public API or CLI for listing, messaging, or transaction actions.

## Boundaries

This skill provides advisory guidance. It does not guarantee a sale, deal, delivery, eligibility, policy outcome, or account recovery. It supports only user-authorized Facebook or Messenger activity and keeps local context under `<state_root>`.
