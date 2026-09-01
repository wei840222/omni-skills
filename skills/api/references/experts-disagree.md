# Where Experts Disagree

- **Official SDK vs raw HTTP.** SDKs win where auth is hard (request signing, OAuth refresh) and lose freshness — new endpoints land in the API before the SDK. Default: raw HTTP for simple bearer-token APIs; SDK when the provider signs requests or its docs treat the SDK as the primary interface. `client_style` records the user's side.
- **Webhooks vs polling.** Webhooks for volume and latency; polling is legitimately simpler when events are rare, no public endpoint can be hosted, or the poll interval is acceptable staleness. The wrong answer is webhooks without the full handler order (`references/webhooks.md`).
- **Idempotency keys on every POST vs only where double-execution hurts.** Every-POST buys uniform retry safety; minimalists note the bookkeeping cost. Boundary: any POST whose duplicate the user would notice (charge, email, order) gets a key — no exceptions there, optional elsewhere.
