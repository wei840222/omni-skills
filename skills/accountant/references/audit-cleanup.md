# Audit packages and cleanup

Load for lender/audit/tax examination requests, PBC lists, or abandoned/inherited/migrated books.

## Scrutiny package (PBC style)

Produce what the request actually asks for; label draft vs final; use locked periods only.

Typical core:

- Trial balance and financial statements for the periods requested
- Bank reconciliations and statements (or exports) for material cash accounts
- AR/AP agings tying to TB
- Revenue roll-forward / deferred revenue schedule
- Payroll registers tying to expense
- Fixed-asset roll-forward
- Debt schedule and covenants summary
- Significant estimates and policies
- Access log of who prepared and who reviewed

Small-team control note: segregate who can create vendors, who can pay, and who reconciles — even if one person wears two hats, document compensating reviews.

## What examiners open first (pattern)

1. Cash and recon quality
2. Revenue cutoff and deferred revenue
3. Owner draws / related party
4. Payroll and trust-fund deposits
5. Large round-number estimates

## Cleanup — restart forward

Abandoned or messy books:

1. Diagnose: last period that ties (cash recon + TB).
2. Restart from that known-good balance and reconcile **forward** period by period — oldest-month grinding before the restart point only multiplies rework.
3. For gaps beyond practical reconstruction, document a reasoned opening balance entry with authorization and disclose uncertainty.
4. Record the cleanup plan and restart point in `<state_root>/memory.md`.

## Migration between systems

1. Freeze a conversion date.
2. Export TB, open AR/AP, FA register, deferred revenue, and open POs.
3. Import into the new system; prove TB and subledgers tie on day 1.
4. Run parallel recon for at least one full close when material.
5. Keep the old system read-only until the first locked close succeeds in the new system.

## Failure recovery

| Trigger | First fix | Still failing |
|---|---|---|
| No known-good period | Reconstruct cash from bank statements first | Escalate if under examination |
| Conversion TB off | Diff chart mapping and opening balances | Roll back import; remap; re-import once |
| Difference grows each month | Mark management reporting provisional | Full cleanup plan + possible fraud review (`escalate.md`) |
