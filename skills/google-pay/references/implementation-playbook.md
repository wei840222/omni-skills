# Implementation Playbook - Google Pay

Use this file to choose a path and avoid mixing incompatible patterns.

## Path A: Web checkout

1. Confirm browser and region support for Google Pay.
2. Render the Google Pay button only after capability / `isReadyToPay` checks pass.
3. Build the payment data request with server-trusted totals and currency.
4. Prefer `PAYMENT_GATEWAY` tokenization unless `DIRECT` is explicitly required.
5. Submit the payment payload to backend or PSP for authorization.
6. Return deterministic success and failure states to the checkout UI.

## Path B: Android checkout

1. Configure the Google Pay API client and merchant context for the environment.
2. Build the request with exact server-trusted amount and currency.
3. Handle the callback and forward the token safely to backend/PSP.
4. Keep capture and settlement logic in backend or PSP.
5. Show fallback methods when Google Pay is unavailable.

## Path C: PSP-mediated integration

1. Confirm the PSP supports Google Pay in the target country and currency.
2. Align token format expectations between client and PSP API.
3. Enforce idempotency keys for authorization and capture calls.
4. Validate webhook handling for async state transitions (`webhook` skill).
5. Document a rollback strategy for elevated declines or PSP outages.

## Data integrity rules

- Currency and amount precision must match backend contracts.
- Checkout session ids must map to order ids one-to-one.
- Retries must preserve the idempotency key per logical payment attempt.
- Never persist raw Google Pay token payloads in notes or logs.

## Completion criteria

- Selected path is explicit.
- Prerequisites are validated.
- Validation checklist is complete for the target environment.
- Incident and rollback path is documented.
