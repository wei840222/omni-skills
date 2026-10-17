# Validation Checklist - Google Pay

Use this checklist before recommending release.

## Merchant and environment

- Merchant profile configured for the correct environment.
- Gateway and Google Pay configuration are aligned.
- Test and production credentials are separated.
- Web origin or Android package configuration is correct.

## Functional paths

- Happy-path payment succeeds.
- User cancellation path is handled without checkout lock.
- Declined payment path returns actionable messaging.
- Retry path works without duplicate authorization.
- Fallback card or alternative payment path is available.

## Platform matrix

- Real Android device tests executed for supported versions when Android is in scope.
- Web tests executed on Chrome and Android browsers in scope.
- Unsupported browser behavior is explicit and safe.

## Data and consistency

- Server totals always match displayed totals.
- Idempotency behavior validated with repeated requests.
- Webhook or callback reconciliation confirms final state.
- Logs and notes contain no raw token payloads.

## Observability and safety

- Payment events include request id and outcome.
- Alerts exist for elevated failures or timeouts.
- Rollback plan is documented and tested.

## Release gate

Do not recommend production rollout until all checklist sections pass with
evidence recorded under `<state_root>/validation-log.md` when durable notes are
enabled.
