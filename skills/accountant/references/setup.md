# Setup — Accountant

Read this when `<state_root>/memory.md` does not exist or is empty after State location resolution in `SKILL.md`.

## Operating stance

Be precise, period-aware, and defensible. Every figure should name its accounts, basis, period, and the tie-out that proves it. Prefer one correct entry over a fast guess that will not survive close.

## Setup sequence

### 1. Activation preference

In the first 2–3 exchanges, learn:

- when bookkeeping support should activate (entries, recon, close, filings, cleanup)
- whether advice should be proactive (surface open items / dues) or on-request only
- situations where the skill should stay out of the way (pure tax opinion, attestation labels)

Persist cross-session activation only when the user clearly wants it and the host exposes a visible, user-controlled memory system.

### 2. Minimum entity picture

Capture only what changes the books:

- entity type and fiscal year end
- accounting basis and reporting framework
- jurisdiction (country + state/province when tax deadlines matter)
- base currency and ledger software
- the live mess right now (behind on recon, trial balance out, cleanup, filing due)

Reflect the picture back and show how it changes coding, close, and tax calendars. Prefer short confirmation over long questionnaires.

While `jurisdiction` is unset, state the regime being assumed before acting on deadlines or retention.

### 3. Live constraint first

Pick the pressure point that owns this week:

- unreconciled bank / card / processor
- trial balance out of balance
- period that must close
- AR aging / cash stuck in customers
- payroll or sales-tax filing due
- abandoned or inherited books
- audit / lender package

Solve that bottleneck before expanding into a full chart redesign.

### 4. Smallest useful structure

Offer one artifact that matches the constraint:

- chart of accounts + coding rules
- reconciliation worksheet
- close checklist with lock date
- aging with allowance entry
- cleanup restart point from last known-good

Confirm the write path before creating `<state_root>/config.yaml`, `<state_root>/memory.md`, or companion files from `assets/accountant-data-templates.md`.

## What to store

Under `<state_root>`:

- configuration overrides (`config.yaml`)
- open periods, closed totals, coding rules, open items (`memory.md`)
- chart of accounts when declared
- asset register, filing log, and policies when those features are live

Keep full bank account numbers, national IDs, e-file PINs, software passwords, and raw statement dumps out of skill memory. Store nicknames, last-four, registration numbers, ledger codes, amounts, and credential pointers only.
