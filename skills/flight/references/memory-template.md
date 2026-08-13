# Flight State Template

Use this reference only after the user asks to retain flight information. Resolve `<state_root>` first.

```text
<state_root>/
├── config.yaml                 # Optional saved preferences
├── memory.md                   # Optional routes, loyalty, and dated reminders
├── bookings/<year>.md          # Optional retained flight tickets
├── flown/<year>.md             # Optional completed-flight history
├── claims/<claim-id>.md        # Optional claim status and evidence index
├── projects/<trip>.md          # Optional itinerary summary
└── finances/subscriptions.md   # Optional non-sensitive travel-benefit tracking
```

Create only the record required by the user's request. Each retained entry records its source, date, purpose, and any user-approved reminder deadline. Keep credentials, payment-card numbers, passport or ID numbers, loyalty PINs, and boarding-pass barcodes outside `<state_root>/`.

## Ticket row

Use one row per retained ticket in `<state_root>/bookings/<year>.md`:

```markdown
| Locator | Type | Carrier | Route | Dates | Status | Source |
|---|---|---|---|---|---|---|
| ABC123 | flight | Example Air | TPE–NRT | 2026-10-12 | ticketed | carrier confirmation |
```

Update only the matching `Type: flight` row. Preserve the user's other travel records unchanged.
