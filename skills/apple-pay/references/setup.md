# Setup - Apple Pay

Read this when `<state_root>/` is missing or empty.
Keep setup practical and non-blocking.

## Operating Priorities

- Answer the immediate user request first.
- Confirm platform and payment architecture early.
- Keep onboarding brief to accelerate value delivery.

## First Activation Flow

1. Confirm what is being integrated now:
- Web checkout
- iOS app checkout
- PSP handoff flow
- Recurring or subscription behavior

2. Confirm environment and merchant readiness:
- Sandbox or production target
- Merchant ID and certificate status
- Domain verification status for web
- Fallback payment method availability

3. Confirm business constraints:
- Single country or multi-country launch
- Authorization/capture flow requirements
- Refund and support expectations

4. If the user approves persistent notes, resolve `<state_root>` once (explicit path, existing project notes, or one ask). Then initialize:
```bash
mkdir -p <state_root>
touch <state_root>/{memory.md,implementations.md,validation-log.md,incidents.md}
chmod 700 <state_root>
chmod 600 <state_root>/{memory.md,implementations.md,validation-log.md,incidents.md}
```

5. If `memory.md` is empty and seeding is requested, initialize it from `assets/memory-template.md`.

## Integration Defaults

- Start in sandbox unless user explicitly requests production checks.
- Prefer one checkout path at a time per ticket.
- Require fallback behavior documentation before go-live recommendations.
- Require idempotency strategy before enabling retries.

## What to Save

- Active platform, path, and PSP scope
- Merchant and domain validation status
- Validation outcomes and unresolved risks
- Incident signatures and mitigation status
- Launch readiness and rollback state

## Guardrails

- Keep private keys out of the chat window.
- Omit raw Apple Pay token payloads from local notes.
- Claim production readiness only when backed by validation evidence.
