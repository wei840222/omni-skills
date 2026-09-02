# Suppliers

Normalize the counterparty before filing.

## Canonicalization
- Canonical name + aliases live under `<state_root>` supplier memory
- Identity prefers supplier tax ID; fall back to canonical name when tax ID is absent
- Record usual VAT rate and parsing quirks for repeat suppliers

## Monitoring
- Expected cadence helps detect missing invoices
- Price-rise watch compares new unit/totals against recent history
- Changed bank details are a fraud halt until verified out of band
