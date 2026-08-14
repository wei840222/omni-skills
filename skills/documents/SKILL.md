---
name: documents
description: Build and query a personal document system for IDs, contracts, certificates, and important files. Use when the user asks where a document is, needs passport or lease details, wants expiry tracking, or wants to catalog a new important file.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"📄"}'
---

## State location

Document state may exist in `<workspace>/documents/`, `<workspace>/memory/documents/`, or `~/documents/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/documents/`, `<workspace>/memory/documents/`, `~/documents/`.
3. If none exists and the user asks to create or retain a document system, default to `<workspace>/documents/`.

Use the selected `<state_root>` for every state operation in this skill. If multiple candidates exist, use the highest-precedence one, report the duplicate state, and keep the other copies unchanged. Treat prior Clawic or `~/docs/` paths as migration sources only; migrate them only through a user-approved copy, validation, and cutover.

Create directories or records only when the user asks to catalog, save, or set up the system. Do not invent missing document contents.

## Core Behavior

- User needs a document → locate instantly under `<state_root>`
- User receives an important doc → help catalog it after confirmation
- User asks "where is my X" → answer from index or category files in seconds
- Prefer read-only lookup first; write only on explicit catalog/update requests

## File Structure

```
<state_root>/
├── identity/
│   ├── passport.md
│   ├── drivers-license.md
│   └── national-id.md
├── financial/
│   ├── tax-returns/
│   ├── bank-accounts.md
│   └── investments.md
├── property/
│   ├── lease.md
│   ├── deed.md
│   └── insurance.md
├── medical/
│   ├── insurance.md
│   └── records/
├── work/
│   ├── contracts/
│   └── certifications/
├── legal/
│   ├── will.md
│   └── power-of-attorney.md
├── vehicles/
│   └── car.md
├── scans/                 # optional digital copies; keep encrypted when possible
└── index.md
```

## Reference Formats

- Load `references/document_formats.md` for Document Entry Format and Quick Reference Index templates.

## Identity Documents

- Passport: number reference, issue/expiry, renewal timeline
- Driver's license: number reference, expiry, real ID status
- National ID: number reference, where issued
- Birth certificate: location of original
- Social Security / national ID equivalents: number reference, card location

## Financial Documents

- Tax returns: by year, location
- Bank accounts: institution, account refs
- Investment accounts: broker, account refs
- Loan documents: terms, payment info

## Property Documents

- Lease: terms, landlord contact, renewal date
- Deed: property details, recording info
- Home insurance: policy number, coverage, agent
- Warranties: appliances, systems, expiry dates

## Medical Documents

- Insurance cards: policy, group number
- Vaccination records: dates, types
- Prescriptions: current medications
- Medical history: major procedures, conditions

## Vehicle Documents

- Registration: plate, expiry
- Insurance: policy, coverage
- Title: loan status, location
- Maintenance: service history

## Work Documents

- Employment contracts: current, past
- Certifications: expiry dates, renewal requirements
- Performance reviews: by year
- Stock/equity: grant documents, vesting

## Lookup workflow

1. Resolve `<state_root>`.
2. Read `<state_root>/index.md` when present.
3. Open the matching category file (for example `property/lease.md`).
4. If missing, report what was checked and offer to catalog the document.
5. If the path or file is unreadable, leave state unchanged and state the blocker.

## What To Surface

- "Your passport expires in 8 months"
- "Driver's license renewal due next month"
- "Health insurance card is in medical/insurance.md"
- "Last tax return filed: 2023"

## Common Requests

- "I need my passport number" → `identity/passport.md`
- "When does my lease end" → `property/lease.md`
- "Health insurance info" → `medical/insurance.md`
- "Car registration" → `vehicles/car.md`

## Expiry Tracking

Flag documents expiring within:

- 6 months: passport (many destinations expect remaining validity near arrival; verify the destination authority before travel — overview: https://en.wikipedia.org/wiki/Passport_validity)
- 2 months: licenses, registrations
- 1 month: insurance renewals

If expiry data is missing, ask for the date instead of guessing.

## Security Notes

- Store sensitive numbers as references, not full plain-text secrets in chat replies
- Keep full numbers out of casually shared notes when a reference or last-4 pattern is enough
- Physical location tracking: "home safe", "filing cabinet"
- Digital scans: encrypted folder recommended under `<state_root>/scans/`
- Share emergency-access info only when the user explicitly requests it

## Progressive Enhancement

- Week 1: catalog identity docs with expiry dates
- Week 2: financial and property
- Week 3: medical and vehicles
- Ongoing: add as documents arrive

## Best Practices

- Keep sensitive identifiers as secure references rather than full plain-text values in shared notes
- Update records immediately after renewals
- Maintain accurate physical and digital locations
- Track expiry dates and surface upcoming renewals early
