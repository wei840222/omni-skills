# Uber Eats Domain Notes

Load this reference when a delivery, fee, cancellation, address, or support claim must be current. Prices, merchant availability, delivery coverage, promotions, cancellation, and refund outcomes are live values, so inspect the user's current Uber Eats page or official help surface before making a claim.

## Current-state checks

1. Confirm the active delivery address before comparing merchants; merchant availability, menus, fees, and ETA are location-dependent.
2. Before an order is placed, read the visible total, including item subtotal, delivery fee, service fee, taxes where shown, tip, and promotion status.
3. After an order is placed, inspect the live order page and the available official support options before describing an address change, cancellation, refund, or missing-item outcome.
4. When the browser is blocked, use the approved app or manual handoff. A browser error does not establish an Uber Eats service outage or an order state.

## Sources

- Uber Eats — https://www.ubereats.com/ — live merchant, menu, cart, fee, and checkout state.
- Uber Help — https://help.uber.com/ubereats — official order, cancellation, delivery, and support guidance. Help article paths can vary by market and account state.

## Claim inventory

| Claim class | Examples in this skill | Verification rule |
|---|---|---|
| Time-sensitive | Merchant availability, ETA, fees, promotions, taxes, cancellation, refunds | Read the current Uber Eats order or checkout page; treat displayed values as authoritative for that session. |
| Platform-specific | Browser access denial, app handoff, address-dependent catalog | Verify the current browser or app state before choosing a fallback. |
| Stable-domain | Draft cart versus purchase, approval before payment, sensitive-data handling | Apply the core workflow and safety boundaries in `SKILL.md`. |
