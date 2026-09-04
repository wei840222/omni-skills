# CRM Adoption

CRMs die from friction, not from missing features. Fix the update cost before buying another tool.

## Friction budget

A healthy update is about one minute:

- Find the person or deal
- Log one line of substance
- Set or confirm the next step + date

If the team needs a form with ten optional fields to "log a call", they will stop logging calls.

## Field discipline

1. Start from the minimum record in `references/schema.md`.
2. Add a field only when a real recurring question needs it.
3. After 30 days, measure fill rate. Under ~70% → delete or make required.
4. Prefer tags over new columns for filterable but non-reported attributes.

## Rescue sequence for a rotting CRM

1. Export a backup.
2. Close or next-step every open deal older than `stall_days`.
3. Merge duplicates on the identity key (`references/hygiene.md`).
4. Delete unused fields and unused stages.
5. Rehearse the one-minute update with the actual users.
6. Migrate tools only after that loop works in the current system.

Buying a new CRM to fix adoption just relocates the empty fields.
