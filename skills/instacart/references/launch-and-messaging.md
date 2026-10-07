# Launch and Messaging - Instacart

## Approval process

After development testing and pre-launch checklist work:

1. Create a Production API key (this triggers review).
2. Expect email with the review result.
3. While status is pending approval, the production key does not function.
4. Only after approval should production write traffic and public claims proceed.

## Public messaging prerequisites

- Integration must be submitted for review and fully approved before public discussion.
- Keep messaging, trademarks, and logo usage aligned with Instacart developer messaging guidelines.
- Do not invent endorsement language or brand rules.

## Pre-launch practical checklist

- Development recipe and shopping-list flows succeed end-to-end
- Retailer lookup behaves for target geos (`US` / `CA`)
- Error handling covers 400/401/403/429/5xx without secret leakage
- URL cache prevents duplicate page spam
- CTA, logo, and partner linkback match design guidance
- Production key is active (not pending)

Store durable launch state in `<state_root>/launch-notes.md`.
