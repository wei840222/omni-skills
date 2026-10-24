---
name: groupon
description: Find, vet, and compare Groupon vouchers. Use for local-deal research, fine-print checks, merchant validation, redemption planning, and Groupon booking or refund problems.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎟️"}'
  related-skills: '{"booking": "Plan reservations and compare travel or stay options.", "buy": "Evaluate real value and compare purchase alternatives.", "shopping": "Broaden a product or deal search beyond Groupon.", "travel": "Connect local offers with larger trip planning decisions.", "tripadvisor": "Validate hospitality and attraction quality with broader review signals."}'
---

## State location

Groupon preferences and follow-up notes are optional local state. Before reading or writing state, resolve `<state_root>` once:

1. Use an explicitly configured path from the user or host.
2. Otherwise use the first existing directory: `<workspace>/groupon/`, `<workspace>/memory/groupon/`, then `~/groupon/`.
3. If none exists and persistent notes would help, ask permission, create `<workspace>/groupon/`, and use it as `<state_root>`.

Use the selected `<state_root>` for this run. Keep payment details, login secrets, full voucher barcodes, and claim codes out of local files. If `<state_root>/memory.md` is missing or empty, read `references/setup.md` before creating preferences.

## Core workflow

1. **Scope** — capture the deal type, city, date window, party size, budget, and travel tolerance. Distinguish discovery from checking an exact voucher.
2. **Screen** — read the full fine print and use `references/deal-qualification.md` to assess merchant quality, booking friction, usable value, and the true out-of-pocket cost.
3. **Verify** — load `references/merchant-checks.md` when reviewing restrictions or a merchant. If a critical term is missing or ambiguous, report the gap and downgrade confidence.
4. **Decide** — return a clear verdict. Prefer a usable deal over a larger headline discount with poor availability or hidden costs.
5. **Act with approval** — search, compare, shortlist, or draft support text freely; get explicit user confirmation before buying, gifting, booking, redeeming, or submitting a refund request.

For a purchased voucher, booking failure, or refund question, first identify whether it is unused, booked, redeemed, shipped, or disputed. Then read `references/recovery.md`, confirm the current deal-specific Groupon policy in live official help content, and separate confirmed facts from the user’s requested outcome.

## Reference map

| Need | Read |
| --- | --- |
| First-time preferences or state setup | `references/setup.md` |
| State-file structure and statuses | `references/memory-template.md` |
| SAVE scorecard and decision-ready output | `references/deal-qualification.md` |
| Merchant trust and restriction checks | `references/merchant-checks.md` |
| Vertical-specific watchouts | `references/category-playbook.md` |
| Booking, support, or refund recovery | `references/recovery.md` |

## Decision-ready output

```text
Verdict: Recommend | Recommend with caveats | Skip
Best fit: [deal or category]
Why it wins: [up to 3 bullets]
Blocking terms: [if any]
True cost: [price + known extras]
Next step: [buy now, hold, compare, contact merchant, request support]
```

## Decision checks

- Compare true cost, merchant quality, and redemption friction rather than discount percentage alone.
- Read the full fine print before recommending a deal marked “restrictions apply.”
- Classify each voucher and verify live policy before outlining a recovery path.
- Store only minimal follow-up context in `<state_root>`.

## Scope and privacy

This skill finds and compares Groupon offers, screens merchants and terms, and guides checkout, booking, and recovery with approval boundaries. Groupon searches transmit search terms, location context, and deal URLs to Groupon; support or booking details leave the device only when the user asks to submit them. Label availability, savings, merchant quality, and refund eligibility as unconfirmed until current evidence verifies them.
