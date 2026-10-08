# Domain Knowledge

## Core behavior

| User signal | Action |
|-------------|--------|
| Shares a want | Capture item with priority, target, links |
| Asks what to buy | Surface by priority, then by target-vs-current gap |
| Asks for a price check | Compare observed prices to target and history |
| Decides to buy | Confirm best observed price, then log purchase after user completes checkout |
| Monthly review | Re-validate relevance and targets |

## Quick capture

```text
User: "I want those Sony headphones"
→ Draft item name / slug
→ Ask missing fields: priority, target price + currency, product link
→ After consent, write items/{slug}.md and priority index line
→ Start tracking from settings.md cadence
```

Minimum viable capture: **name + priority**. Target price and links are the next enrichment step, not blockers for a temporary stub when the user is in a hurry—mark missing fields `unknown` and ask on the next touch.

## Priority routing

When the user asks what to buy next:

1. List **must-have** items whose current best ≤ target (or within a user-defined tolerance).
2. Then must-have items with the largest percent drop from last check.
3. Then **want** items on a clear sale relative to target.
4. Keep **someday** off the default recommendation list unless the user asks for inspiration.

## Price checking

When checking prices:

1. Use user-provided links and preferred stores from `settings.md`.
2. Record only observed prices with store name, currency, and date.
3. Compare to target and to the previous history row.
4. Surface significant moves: below target, ≥15% drop from last check (default), or first time on a configured sale flag.
5. Update `Last checked` and append history when the price changed.

Do not invent market averages, "usual" street prices, or unverified coupon stacks.

## What to surface

- "Sony headphones dropped 30 USD this week (349 → 319); target remains 300."
- "3 must-have items are at or under target."
- "Kindle price unchanged for 60 days—keep waiting or retarget?"
- "Large sale window approaching—review high-priority open items."

## Smart suggestions (evidence-bound)

Allowed when grounded in the item file or user context:

- Sale-window timing the user already cares about (Prime Day, end of season, etc.) as a **calendar hint**, not a guarantee of a deeper discount.
- Refurbished / open-box only when the user accepts that channel and warranty terms are checked.
- Similar lower-cost alternative only after stating it is a substitute, not the saved SKU.
- Staleness prompt: "You added this 6 months ago—still relevant?"

## Purchase flow

When the user decides to buy a tracked item:

1. Re-read the item file and confirm the latest observed best price.
2. Summarize target vs actual and whether the buy hits / misses target.
3. Hand checkout to the user or to `buy` when execution help is requested; this skill does not place orders.
4. After the user confirms the purchase happened, append `purchased.md`, set item `Status: purchased`, and remove or strike the priority index line.
5. Offer `expenses` for spend logging when the user wants ledger continuity.

## Categories

Organize for browsing, not as a rigid taxonomy:

- Tech, Home, Clothing, Hobby, Gifts-for-self, user-defined

Category indexes are optional convenience; missing category never blocks capture.

## Review and hygiene

- Monthly: still want it? still the right model? target still sane?
- Before suggesting a new buy of something already listed, open the existing item first.
- Prefer updating history over deleting price rows.
- Close abandoned someday items only with user confirmation.

## Failure recovery

| Problem | Recovery |
|---------|----------|
| No `<state_root>` | Run setup consent; create workspace root only after yes |
| Duplicate roots | Stay on highest precedence; report others |
| Missing target price | Ask or mark `unknown`; still allow capture |
| Conflicting prices same day | Keep both rows with store labels; highlight spread |
| User wants impulse buy of unlisted item | Offer 24–48h cool-down **or** immediate capture as must-have/want before checkout help |
| Checkout requested here | Draft checklist; route execution to `buy` / user |

## Boundary with sibling skills

- List hygiene and saved wants → this skill
- Deep product comparison without list state → `shopping`
- Fair-value / manipulation check on a single quote → `price`
- Order placement / scam checkout → `buy`
- Gift recipient memory → `gifts`
- Affordability framing → `money`
