# Official Sources — Google Pay

Refresh mutable product, API, and country-support claims against these live
pages. Record the retrieval date in PR notes when a fact changes
recommendations.

## Agent Skills specification

- https://agentskills.io/llms.txt
- https://agentskills.io/specification
- https://agentskills.io/skill-creation/best-practices
- https://agentskills.io/skill-creation/optimizing-descriptions
- https://github.com/agentskills/agentskills/tree/main/skills-ref

## Google Pay product and developer docs

- Google Pay API hub: https://developers.google.com/pay/api
- Web overview: https://developers.google.com/pay/api/web/overview
- Android overview: https://developers.google.com/pay/api/android/overview
- Web tutorial: https://developers.google.com/pay/api/web/guides/tutorial
- Android tutorial: https://developers.google.com/pay/api/android/guides/tutorial
- Payment data cryptography: https://developers.google.com/pay/api/web/guides/resources/payment-data-cryptography
- Web request objects: https://developers.google.com/pay/api/web/reference/request-objects
- Google Pay & Wallet Console: https://pay.google.com/business/console

## Integration notes pinned from live docs (retrieved 2026-10-18)

- Prefer gateway tokenization (`PAYMENT_GATEWAY`) unless the merchant explicitly
  owns `DIRECT` decryption and PCI scope.
- Perform readiness / `isReadyToPay`-style checks before rendering the button.
- Amounts and currency in the payment data request must match server-side order
  totals; do not trust client-only figures for capture.
- Treat payment tokens as sensitive: forward to backend/PSP, do not log raw
  payloads, and keep test vs production merchant configuration separated.
- Recurring charges are owned by the PSP / billing backend after initial method
  capture; Google Pay alone is not a full subscription engine.
