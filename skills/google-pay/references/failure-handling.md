# Failure Handling - Google Pay

Use this file to classify failures fast and choose the next action.

## Common failure classes

| Class | Typical symptom | First action |
|------|------------------|--------------|
| Merchant readiness failure | Button hidden or flow not available | Verify merchant profile and environment configuration |
| Token processing failure | Authorization declined or token parsing error | Validate backend parsing and PSP mapping |
| Environment mismatch | Test payload sent to production path | Confirm credential and endpoint separation |
| Timeout or network errors | Checkout stalls before confirmation | Add retry strategy and clear user fallback |
| Duplicate authorization | Repeated charges on retry | Verify idempotency key usage and retry policy |

## Incident response loop

1. Record failure signature and affected scope (no raw tokens).
2. Check whether the issue is deterministic or intermittent.
3. Validate prerequisites before code-level changes.
4. Apply the smallest fix and rerun the validation checklist.
5. Log mitigation and preventive action in `<state_root>/incidents.md` when durable notes are enabled.

## User-facing response rules

- Explain whether the user can retry immediately.
- Offer fallback payment without losing cart context.
- Avoid exposing internal error identifiers in UI text.

## Hard stop conditions

Pause rollout when:

- Merchant readiness fails in production.
- Decline rates exceed the normal baseline without explanation.
- Fallback flow is broken for a significant segment.
- Duplicate authorizations are detected in live traffic.
