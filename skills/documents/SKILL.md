---
name: documents
description: Build a personal document system for instant access to IDs, contracts, certificates, and important files.
metadata:
  clawdbot: '{"emoji":"📄","os":["linux","darwin","win32"],"displayName":"Documents"}'
---

## State location
- Workspace docs: `$WORKSPACE_DIR/documents/`

## Core Behavior
- User needs a document → locate instantly
- User receives important doc → help catalog it
- User asks "where is my X" → answer in seconds
- Create `$WORKSPACE_DIR/documents/` as workspace

## File Structure
```
$WORKSPACE_DIR/documents/
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
└── index.md
```

## Reference Formats
- See `references/document_formats.md` for Document Entry Format and Quick Reference Index formats.

## Identity Documents
- Passport: number, issue/expiry, renewal timeline
- Driver's license: number, expiry, real ID status
- National ID: number, where issued
- Birth certificate: location of original
- Social Security: number reference, card location

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

## What To Surface
- "Your passport expires in 8 months"
- "Driver's license renewal due next month"
- "Health insurance card is in medical/insurance.md"
- "Last tax return filed: 2023"

## Common Requests
- "I need my passport number" → identity/passport.md
- "When does my lease end" → property/lease.md
- "Health insurance info" → medical/insurance.md
- "Car registration" → vehicles/car.md

## Expiry Tracking
Flag documents expiring within:
- 6 months: passport (travel requirement - many countries require passport validity of at least 6 months on arrival, see https://en.wikipedia.org/wiki/Passport_validity)
- 2 months: licenses, registrations
- 1 month: insurance renewals

## Security Notes
- Store sensitive numbers as references, not plain text
- Physical location tracking: "home safe", "filing cabinet"
- Digital scans: encrypted folder recommended
- Share access info with trusted person for emergencies

## Progressive Enhancement
- Week 1: catalog identity docs with expiry dates
- Week 2: financial and property
- Week 3: medical and vehicles
- Ongoing: add as documents arrive

## Best Practices
- Always store sensitive numbers securely and avoid plain text.
- Always update documents immediately after renewals.
- Always maintain accurate records of physical locations.
- Always track expiry dates and flag appropriately.
