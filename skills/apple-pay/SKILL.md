---
name: apple-pay
description: >
  Implement Apple Pay for web and iOS checkout with merchant validation,
  server-trusted totals, token safety, sandbox testing, and production
  rollout gates. Use when adding wallet checkout, diagnosing merchant
  session or domain association failures, or planning recurring capture
  through a PSP. Prefer `payments` for provider selection across cards
  and wallets, `ios` for general iOS app work without payment tokens,
  `app-store-connect` for Apple account ops outside merchant validation,
  and `auth`/`api` when the task is identity or backend contracts only.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🍎","requires":{"bins":["curl","jq"],"env":["APPLE_PAY_MERCHANT_ID"]},"os":["darwin","linux","win32"],"displayName":"Apple Pay"}'
  related-skills: '{"api":"Backend contracts, webhooks, and failure-safe integrations around Apple Pay authorization.","app-store-connect":"Apple developer account and capability ops outside merchant-session validation.","auth":"Authentication and session hardening adjacent to checkout identity.","ios":"iOS app implementation and device debugging when payment tokens are not the focus.","payments":"Provider selection and multi-method checkout design beyond Apple Pay alone."}'
---

## Setup

On first use, load `references/setup.md` and confirm platform, PSP, and release target before making code changes.

## State location

Before the first state read, create, or update, resolve `<state_root>` once:

1. Explicit path supplied by the user for this integration.
2. Existing project-local Apple Pay notes directory already in use.
3. Otherwise ask once; do not create notes until the user approves a path.

Use `<state_root>/memory.md`, `<state_root>/implementations.md`, `<state_root>/validation-log.md`, and `<state_root>/incidents.md` as needed. Runtime notes stay outside the skill package and version control. Read-only guidance needs no state creation. If multiple candidate roots exist, stop and ask which copy is authoritative; never merge silently.

## When to Use

User needs Apple Pay for checkout, subscriptions, or wallet-first conversion improvements. Agent handles architecture choice, merchant setup, token safety, launch validation, and post-launch operations.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for setup and status fields.

```
<state_root>/
|-- memory.md                 # Project snapshot, risk status, and rollout state
|-- implementations.md        # Selected approach and platform notes
|-- validation-log.md         # Test evidence and environment results
`-- incidents.md              # Failed payments, root causes, and fixes
```

## Quick Reference

Use the smallest relevant file for the current task.

| Topic | File |
|-------|------|
| Setup flow | `references/setup.md` |
| Memory template | `assets/memory-template.md` |
| Implementation plan | `references/implementation-playbook.md` |
| Validation matrix | `references/validation-checklist.md` |
| Failure recovery | `references/failure-handling.md` |
| Release and operations | `references/launch-playbook.md` |
| Recurring and subscription flows | `references/recurring-payments.md` |
| Official sources | `references/sources.md` |

## Requirements

- Environment variable: `APPLE_PAY_MERCHANT_ID`
- CLI tools for diagnostics: `curl`, `jq`
- Access to Apple merchant account assets for the target environment

Keep private keys and full certificate private material out of chat.

## Data Storage

Local notes stay under `<state_root>/`:
- memory file for current state and integration decisions
- validation log file for test outcomes and evidence
- incidents file for failure signatures and mitigations

## Core Rules

### 1. Confirm Business Goal Before Choosing Integration Path
Start by identifying the target outcome:
- Higher checkout conversion
- Faster repeat purchases
- Cleaner mobile payment UX
- Lower payment failures

Then choose one primary path:
- Web with Apple Pay JS and merchant session backend
- Native iOS with PassKit
- PSP-mediated integration (for example Stripe, Adyen, Braintree)

Maintain a single path per patch, unless the user requests a migration plan.

### 2. Require Merchant and Domain Prerequisites
Before implementation, confirm:
- Merchant ID exists and matches target environment
- Payment processing certificate exists and is valid
- Domain association file is hosted and reachable for web
- Sandbox and production credentials are separated

If any prerequisite is missing, pause coding and produce a concrete prerequisite checklist.

### 3. Enforce Server Truth for Amounts and Currency
Amounts and currency must match across:
- Client request payload
- Server-side cart or order totals
- PSP authorization and capture calls

Rely solely on server totals for the final charge amount.

### 4. Keep Token Handling Minimal and Auditable
Treat Apple Pay payment tokens as sensitive:
- Forward token payload only to backend or PSP
- Persist metadata only (request id, status, amount, currency)
- Keep raw token payloads entirely out of logs, notes, and screenshots

### 5. Build Idempotent and Recoverable Payment Steps
Require idempotency and reconciliation for all critical calls:
- Authorization request
- Capture request
- Refund or void operations

Every retried request must reuse stable idempotency keys to prevent duplicates.

### 6. Separate Sandbox and Production Release Gates
Recommend production rollout only when all gates pass:
- Sandbox success, decline, cancellation, and timeout paths are tested
- Device and browser matrix is complete for supported audience
- Fallback card or alternative checkout works when Apple Pay is unavailable
- Failure observability and alerts are active

### 7. Include Support and Incident Paths in Every Delivery
For each implementation, include:
- What customer sees on success and failure
- Which errors are recoverable vs terminal
- What support team should do first for each failure class
- Rollback or kill-switch decision point

Prefer stable payment reliability over feature breadth.

## Common Traps

- Running merchant validation from the client -> exposes sensitive flow and fails reviews
- Trusting client-side totals -> mismatch between authorized and captured amounts
- Reusing sandbox credentials in production -> live checkout failures at launch
- Treating simulator-only tests as release evidence -> real devices still fail
- Missing idempotency on retries -> duplicate charges and refund overhead
- Launching without fallback checkout -> conversion loss when wallet is unavailable

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://apple-pay-gateway.apple.com | Merchant validation request payload | Establish merchant session for Apple Pay on the web |
| https://apple-pay-gateway-cert.apple.com | Merchant validation request payload (sandbox/cert path) | Validate merchant sessions in non-production environments |
| https://appleid.apple.com | Account and merchant auth metadata | Apple account and merchant identity operations |

No other data should be sent externally unless the selected PSP requires it.

## Security & Privacy

Data that leaves your machine:
- Merchant validation requests to Apple endpoints
- Payment tokens sent to the configured PSP or backend

Data that stays local:
- Integration notes and rollout state under `<state_root>/`
- Validation evidence and failure logs without raw tokens

This skill does NOT:
- Store raw payment tokens in memory files
- Skip mandatory Apple merchant requirements
- Enable production release without explicit readiness checks

## Trust

Apple Pay integrations depend on Apple infrastructure and the chosen PSP.
Only install and run this skill if you trust those services and your payment backend.

## Related Skills
- `payments` - General payment design and checkout decision frameworks
- `app-store-connect` - Apple ecosystem account and operational workflows
- `ios` - iOS implementation and device-level debugging patterns
- `auth` - Authentication and session hardening in transaction flows
- `api` - Reliable backend API contracts and failure-safe integrations
