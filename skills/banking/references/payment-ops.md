# Payment Operations Guide

Use for payment execution guidance and settlement troubleshooting. Speeds and reversibility below are typical operational patterns, not guaranteed SLAs — confirm the institution's published cutoff and recall rules for the live rail.

## Rail selection snapshot

| Rail | Typical speed | Reversibility | Primary risk |
|------|---------------|---------------|--------------|
| Internal transfer | Immediate | Medium | Wrong-account routing |
| ACH / batch credit transfer | Same day to next day | Medium (return windows) | Cutoff miss and return codes |
| Domestic wire (e.g. Fedwire-class) | Same day when released | Low after release | Irreversible once settled |
| Card settlement | 1–3 days | Medium (dispute windows) | Chargeback timing |
| International / correspondent | 1–5+ days | Low | Compliance holds, beneficiary mismatch |

## Pre-execution controls

Before any transfer flow:

1. Confirm sender authority and account status.
2. Validate beneficiary details using an approved source (callback, trusted directory, dual entry).
3. Confirm amount, currency, and fee handling.
4. Check cutoff window and expected settlement time for that rail.
5. Verify required approvals and dual-control were completed.
6. Confirm rollback, recall, or freeze path if release goes wrong.

## Reconciliation triage

When balances fail to match:

1. Verify timing mismatch first (cutoff, weekend, timezone, value date).
2. Check duplicate postings and partial settlements.
3. Compare ledger amount against processor or correspondent statement.
4. Isolate one transaction ID and trace full lifecycle.
5. Record root cause and the prevention control to add.

## High-risk signals

- New beneficiary plus urgent same-day release request
- Amount far above normal customer pattern
- Repeated correction requests after approval
- Manual override request with no documented reason

Treat high-risk signals as incident candidates and switch to `references/incident-response.md`.
