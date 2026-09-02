# Approvals

Use when more than one person can authorize spend.

## Matching
- **2-way match**: invoice ↔ purchase order (PO)
- **3-way match**: invoice ↔ PO ↔ goods/services receipt
- Apply configured amount and quantity tolerances; anything outside tolerance needs explicit approval

## Controls
- Record who approved, when, and against which PO/receipt identity
- Keep segregation of duties: the requester should not be the sole approver for material amounts
- Route above-threshold invoices to the named approver before payment preparation
