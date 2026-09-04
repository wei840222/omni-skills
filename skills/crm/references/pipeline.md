# Stages And Their Exit Criteria

Default five-stage pipeline; rename freely, but keep one exit criterion per stage and keep it observable. Override with `pipeline_stages` in config.

| Stage | Exits when (third party could confirm) | Not an exit |
|---|---|---|
| Lead | They replied, or booked time | You added them from a list, or they opened an email |
| Qualified | Problem stated in their words, budget owner named, rough timeline given | "They seem interested"; you decided they are a good fit |
| Proposal | They have the written scope and price *and* a review is scheduled | You sent the document |
| Negotiation | Terms are being redlined, or procurement/legal is named and engaged | They said the price is "fine" |
| Closed-won | Signature, PO, or first payment | A verbal yes — the single most common reason a forecast misses |
| Closed-lost | Reason code recorded from a closed list, plus who they chose instead | "No response" as a terminal reason without a documented last attempt |

Skipped stages are data, not errors: an inbound deal that arrives with budget and timeline enters at Qualified. What is forbidden is *back-dating* the entry so cycle length looks shorter — that corrupts every conversion number downstream (`references/metrics.md`).

## Stall and forecast hooks

- A deal whose next-step date is older than today, or whose stage age exceeds `stall_days` (default 21), joins the stalled list at the next review.
- Forecasts weight open value by measured stage conversion with an as-of date; see `references/metrics.md`.
