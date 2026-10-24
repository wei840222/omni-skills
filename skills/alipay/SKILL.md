---
name: alipay
description: "Implement Alipay for web and mobile. Use when configuring signed request safety, aligning gateway endpoints, handling asynchronous callbacks, or handling production error codes."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"💴","requires":{"bins":["curl","jq"],"env":["ALIPAY_APP_ID"]}}'
  related-skills: '{"android": "Android checkout implementation and runtime troubleshooting patterns", "api": "Reliable backend API contracts and failure-safe integrations", "auth": "Authentication and session hardening in transaction flows", "billing": "Billing models, reconciliation, and payment lifecycle decisions", "payments": "General payment design and checkout decision frameworks"}'
---

## Setup

On first use, read `references/setup.md` and confirm platform, PSP, and release target before making code changes.

## When to Use

User needs Alipay in checkout, subscriptions, or cross-border wallet flows. Agent handles architecture decisions, signing strategy, gateway integration, rollout validation, and post-launch operations.


## State location

Before any state operation, use an explicitly configured state root when one exists. Otherwise choose the first existing directory in this order: `<workspace>/alipay/`, `<workspace>/memory/alipay/`, then `~/alipay/`. If more than one exists, use only the highest-precedence directory and tell the user that separate copies exist; never merge or synchronize them automatically. If none exists and persistent state is needed with authorization, create `<workspace>/alipay/`.

Use the selected `<state_root>` consistently for the entire invocation. The host supplies `<workspace>`; do not substitute the shell working directory.

## Architecture

Memory lives in `<state_root>/`. See `references/memory-template.md` for setup and status fields.

```
<state_root>/
|-- memory.md                 # Project snapshot, risk status, and rollout state
|-- implementations.md        # Selected approach and platform notes
|-- validation-log.md         # Test evidence and environment results
`-- incidents.md              # Failed payments, root causes, and fixes
```

## Quick Reference

Use the smallest relevant file for the current task.

| Topic | File | When to load |
|-------|------|--------------|
| Domain Knowledge | `references/domain-knowledge.md` | When you need cross-border details or callback requirements |
| Setup flow | `references/setup.md` | For initial setup and credentials |
| Memory template | `references/memory-template.md` | To initialize local state and memory |
| Implementation plan | `references/implementation-playbook.md` | For step-by-step implementation guide |
| Validation matrix | `references/validation-checklist.md` | Before considering the integration complete |
| Failure recovery | `references/failure-handling.md` | When debugging payment failures |
| Release and operations | `references/launch-playbook.md` | Before deploying to production |
| Recurring and subscription flows | `references/recurring-payments.md` | When implementing subscriptions |

## Requirements

- Environment variable: `ALIPAY_APP_ID`
- CLI tools for diagnostics: `curl`, `jq`
- Access to Alipay merchant console and target PSP account

Always use environment variables for private keys, full signed payloads, or PSP secrets rather than asking users to paste them into chat.

## Data Storage

Local notes stay under `<state_root>`:
- memory file for current state and integration decisions
- validation log file for test outcomes and evidence
- incidents file for failure signatures and mitigations

## Core Rules

### 1. Confirm Business Goal Before Choosing Integration Path
Start by identifying the target outcome:
- Higher mobile checkout conversion
- Faster repeat purchases
- Lower payment friction for domestic and cross-border users
- Fewer payment failures

Then choose one primary path:
- Web or H5 checkout with Alipay gateway redirect flow
- In-app checkout with Alipay SDK handoff
- PSP-mediated integration path

Focus on a single integration path per patch unless the user asks for a migration plan.

### 2. Require Merchant and Environment Prerequisites
Before implementation, confirm:
- Alipay app id exists for the correct account
- Gateway keys and certificates match the environment
- Notify and return URLs are configured and reachable
- Test and production credentials are separated

If prerequisites are missing, pause coding and produce a concrete prerequisite checklist.

### 3. Enforce Server Truth for Amounts and Currency
Amounts and currency must match across:
- Client payment request payload
- Server-side order totals
- Alipay authorization and capture calls

Always calculate and verify final charge amounts on the server.

### 4. Make Signing and Callback Verification Explicit
Treat signing and verification as required controls:
- Sign outgoing requests with the approved key strategy
- Verify callback signatures before changing order state
- Reject unsigned or invalid callbacks deterministically

Require signature checks to pass before marking a payment successful.

### 5. Keep Payment Payload Handling Minimal and Auditable
Treat Alipay payloads as sensitive:
- Forward payload only to backend or PSP
- Persist metadata only (request id, status, amount, currency)
- Only store non-sensitive metadata (request id, status, amount, currency) in logs, notes, or screenshots

### 6. Build Idempotent and Recoverable Payment Steps
Require idempotency and reconciliation for all critical calls:
- Authorization request
- Capture request
- Refund or close operations

Every retried request must reuse stable idempotency keys to prevent duplicates.

### 7. Separate Test and Production Release Gates
Require all gates to pass before recommending a production rollout:
- Test success, decline, cancellation, and timeout paths are covered
- Device and browser matrix is complete for supported audience
- Fallback card or alternative checkout works when Alipay is unavailable
- Failure observability and alerts are active

## Common Traps

- Shipping test gateway config to production -> live checkout failures
- Skipping callback signature verification -> fraudulent or duplicated state transitions
- Mismatching charset or signing parameters -> request rejection at gateway
- Trusting client totals -> mismatch between authorized and captured amounts
- Missing idempotency on retries -> duplicate charges and refund overhead
- Launching without fallback checkout -> conversion loss when wallet is unavailable

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://openapi.alipay.com/gateway.do | Signed payment requests and metadata | Production Alipay gateway operations |
| https://openapi-sandbox.dl.alipaydev.com/gateway.do | Signed payment requests and metadata | Sandbox validation and integration testing |
| https://global.alipay.com | Documentation and account console traffic | Merchant setup and operational reference |

Only send required data externally unless the selected PSP requires it.

## Security & Privacy

Data that leaves your machine:
- Alipay request payloads needed for wallet flow
- Payment metadata and signed requests sent to configured PSP or backend

Data that stays local:
- Integration notes and rollout state under `<state_root>`
- Validation evidence and failure logs without raw signed payloads

This skill MUST ensure:
- Raw signed request payloads remain out of memory files
- All mandatory merchant and callback verification requirements are executed
- Readiness checks pass before production release

## Trust

Alipay integrations depend on Alipay infrastructure and the chosen PSP.
Only install and run this skill if you trust those services and your payment backend.
