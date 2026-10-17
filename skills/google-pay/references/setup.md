# Setup - Google Pay

Read this when `<state_root>/` is missing or empty, or on first activation.
Keep setup practical and non-blocking.

## Operating priorities

- Answer the immediate user request first.
- Confirm platform and payment architecture early.
- Avoid long onboarding before delivering value.

## First activation flow

1. Confirm what is being integrated now:
   - Web checkout
   - Android app checkout
   - PSP handoff flow
   - Recurring or subscription behavior

2. Confirm environment and merchant readiness:
   - Test or production target
   - Merchant profile and gateway status
   - Origin or package configuration status
   - Fallback payment method availability

3. Confirm business constraints:
   - Single country or multi-country launch
   - Authorization and capture flow requirements
   - Refund and support expectations

4. Resolve `<state_root>` using the State location rules in `SKILL.md` before
   creating any files. Never mkdir the literal string `<state_root>`.

5. If the user consents to durable notes and no state root exists yet, create
   the default resolved directory (`<workspace>/google-pay/` when `<workspace>`
   is available). Then create only the files needed for the current work:

```bash
# After resolving STATE_ROOT to a real absolute path:
mkdir -p "$STATE_ROOT"
chmod 700 "$STATE_ROOT"
touch "$STATE_ROOT/memory.md"
chmod 600 "$STATE_ROOT/memory.md"
# Optional when those workflows start:
# touch "$STATE_ROOT/implementations.md" "$STATE_ROOT/validation-log.md" "$STATE_ROOT/incidents.md"
# chmod 600 "$STATE_ROOT"/implementations.md "$STATE_ROOT"/validation-log.md "$STATE_ROOT"/incidents.md
```

6. If `memory.md` is empty, initialize it from `assets/data-templates.md`.

## Integration defaults

- Start in test mode unless the user explicitly requests production checks.
- Prefer one checkout path at a time per ticket.
- Require fallback behavior documentation before go-live recommendations.
- Require an idempotency strategy before enabling retries.
- Hand recurring renewals to `billing` / `subscriptions` plus the PSP skill.

## What to save

- Active platform, path, and PSP scope
- Merchant and gateway validation status
- Validation outcomes and unresolved risks
- Incident signatures and mitigation status
- Launch readiness and rollback state

## Guardrails

- Keep private keys, full token payloads, and PSP secrets outside chat.
- Exclude raw Google Pay token payloads from local notes.
- Claim production readiness only after obtaining explicit validation evidence.
- Legacy `~/Clawic/data/google-pay/` is migration-only; do not put it in the
  active lookup order or move it without user confirmation.
