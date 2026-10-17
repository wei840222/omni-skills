---
name: google-pay
description: >
  Implement Google Pay for web and Android with merchant prerequisites,
  gateway tokenization, server-trusted totals, idempotent authorization, and
  production rollout gates. Use when adding or debugging a Google Pay button,
  wallet capability checks, PAYMENT_GATEWAY vs DIRECT tokenization, PSP token
  handoff, launch validation, or payment-incident triage. Prefer `payments` for
  provider selection and PCI boundaries, `billing` / `subscriptions` for
  recurring lifecycle and dunning, `stripe-api-integration` or `paypal` for
  PSP-specific API debugging, `webhook` for generic receiver security, and
  `android` for non-payment Android build/release work.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💳","requires":{"bins":["curl","jq"],"env":["GOOGLE_PAY_MERCHANT_ID"]},"configPaths":["<state_root>/"]}'
  related-skills: '{"android":"Non-payment Android app build, Play packaging, and device tooling around an in-app Google Pay button.","billing":"Subscription billing state machines, proration, and dunning after Google Pay captures the initial method.","payments":"Provider selection, one-off checkout design, and PCI-safe payment handling beyond Google Pay wallet specifics.","paypal":"PayPal REST and wallet flows when the PSP path is PayPal rather than Google Pay.","stripe-api-integration":"Stripe call-level debugging once Google Pay tokens are handed to Stripe.","subscriptions":"Offer-shape and renewal product design when Google Pay is only the initial capture path.","webhook":"Generic webhook receiver security and idempotency for PSP async payment events."}'
---

# Google Pay

Ship **wallet-safe Google Pay checkout** for web and Android: confirm merchant
and gateway prerequisites, choose one tokenization mode, keep amounts
server-trusted, forward tokens only to backend/PSP, and block production advice
until validation evidence exists.

## State location

Google Pay integration notes, validation evidence, and incident rows may exist
in `<workspace>/google-pay/`, `<workspace>/memory/google-pay/`, or
`~/google-pay/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/google-pay/`, `<workspace>/memory/google-pay/`, `~/google-pay/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable state must be created, default to
   `<workspace>/google-pay/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. If older
notes exist only at `~/Clawic/data/google-pay/`, propose a copy/validation/cutover
plan and wait for user confirmation before any migration. Never write the
literal string `<state_root>` to disk. Never store PAN/CVV, private keys, full
token payloads, or PSP secrets in state files.

## When to use

- Web or Android Google Pay button / wallet checkout
- Merchant profile, origin, package, or gateway readiness checks
- Choosing `PAYMENT_GATEWAY` vs `DIRECT` tokenization
- Token handoff, idempotent auth/capture/refund, and launch gates
- Decline, timeout, duplicate-charge, or missing-button incident triage

## Quick reference

Load only the smallest file needed. Keep this `SKILL.md` as the router:

| Need | Load |
|------|------|
| First-use setup / consent | `references/setup.md` + `assets/data-templates.md` |
| Path selection (web / Android / PSP) | `references/implementation-playbook.md` |
| Pre-release validation matrix | `references/validation-checklist.md` |
| Failure classes and response loop | `references/failure-handling.md` |
| Progressive rollout and kill switches | `references/launch-playbook.md` |
| Initial capture vs recurring renewals | `references/recurring-payments.md` |
| Verified source pins (Gate 6) | `references/sources.md` |

## Requirements

- Environment variable: `GOOGLE_PAY_MERCHANT_ID` (merchant context for the active environment)
- CLI tools for diagnostics: `curl`, `jq`
- Access to Google Pay business console and the target PSP account

Keep private keys, full token payloads, and PSP secrets outside of chat and
local notes.

## Architecture

Optional durable notes live under the resolved `<state_root>/`:

```text
<state_root>/
|-- memory.md              # Project snapshot, risk status, rollout state
|-- implementations.md     # Selected path and platform notes
|-- validation-log.md      # Test evidence and environment results
`-- incidents.md           # Failure signatures, root causes, mitigations
```

Create optional files only when that work starts. Do not pre-create empty trees.

## Core rules

1. **Confirm the business goal before choosing a path.** Pick one primary path
   per change: web Google Pay API + gateway tokenization, Android in-app Google
   Pay API, or PSP-mediated integration. Do not mix incompatible patterns in one
   patch unless the user requested an explicit migration.
2. **Require merchant and environment prerequisites.** Confirm merchant profile,
   gateway/PSP Google Pay support for target countries, isolated test vs
   production credentials, and correct web origin or Android package
   configuration before coding. If prerequisites are missing, pause and produce
   a checklist.
3. **Enforce server truth for amount and currency.** Client payment data
   requests, server cart/order totals, and PSP authorization/capture must match.
   Never trust client-supplied totals for the final charge.
4. **Keep token handling minimal and auditable.** Forward the Google Pay token
   only to backend or PSP. Persist metadata only (request id, status, amount,
   currency). Exclude raw token payloads from logs, notes, and screenshots.
5. **Choose tokenization explicitly.** Prefer `PAYMENT_GATEWAY` for most
   integrations. Use `DIRECT` only when the user explicitly owns decryption and
   PCI scope. Document risk review before switching modes.
6. **Build idempotent recoverable payment steps.** Authorization, capture,
   refund, and void retries must reuse stable idempotency keys per logical
   attempt.
7. **Separate test and production release gates.** Recommend production only
   after success/decline/cancel/timeout paths, supported device/browser matrix,
   fallback checkout, and failure alerts are evidenced.

## Workflow

1. Read `references/setup.md` and resolve `<state_root>` before writing notes.
2. Confirm platform, PSP, environment, and tokenization mode.
3. Load `references/implementation-playbook.md` for the selected path only.
4. Implement with server-trusted totals and token-forwarding boundaries.
5. Run `references/validation-checklist.md` in the target environment.
6. For recurring products, load `references/recurring-payments.md` and hand
   renewals to `billing` / `subscriptions` + the PSP skill.
7. For launch, follow `references/launch-playbook.md`; for incidents, follow
   `references/failure-handling.md`.
8. Refresh mutable API/product claims from `references/sources.md`.

## Common traps

- Shipping test merchant/gateway config to production
- Mismatched gateway merchant ids across environments
- Skipping `isReadyToPay` / capability checks before rendering the button
- Trusting client totals for authorization amount
- Retrying without idempotency keys (duplicate charges)
- Launching without a working fallback checkout
- Treating one-time Google Pay payloads as if they alone own recurring renewals

## External endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| `https://pay.google.com` | Wallet / payment-request payloads | Google Pay client wallet interactions |
| `https://pay.google.com/gp/p/js/pay.js` | Script request metadata | Load Google Pay JavaScript client |
| Chosen PSP / backend endpoints | Payment token + order metadata | Authorization, capture, refunds |

Limit external transmission to what the selected PSP and backend require.

## Security and privacy

Leaves the machine:

- Google Pay request payloads needed for the wallet flow
- Payment token payloads sent to the configured backend or PSP

Stays local under `<state_root>/`:

- Integration notes and rollout state
- Validation evidence and failure logs **without** raw token payloads

Out of scope:

- Storing raw token payloads in memory files
- Bypassing merchant/gateway prerequisites
- Declaring production readiness without validation evidence

## Trust

Google Pay integrations depend on Google infrastructure and the chosen PSP.
Only continue if those services and the payment backend are trusted for the
workload.
