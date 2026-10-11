---
name: health-insurance
description: Evaluate medical usage, model total annual health costs, and compare insurance plans. Trigger when users need help selecting, comparing, or renewing health insurance coverage.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji": "🏥"}'
  related-skills: '{"health": "health planning context that informs insurance priorities", "doctor": "provider interaction planning and visit preparation", "compare": "structured side-by-side decision frameworks", "money": "budgeting and cash-flow planning for premium and out-of-pocket costs"}'
---

## State location

Health Insurance state may exist in `<workspace>/health-insurance/`, `<workspace>/memory/health-insurance/`, or `~/health-insurance/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/health-insurance/`, `<workspace>/memory/health-insurance/`, `~/health-insurance/`.
3. If none exists and state must be created, default to `<workspace>/health-insurance/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

On first use, read `references/setup.md` for integration guidelines and memory initialization.

## Core Rules

### 1. Lock Decision Context First
Before comparing plans, clarify:
- Coverage target: individual, couple, or family
- Source: employer plan, public marketplace, private broker, or government program
- Geography and provider access requirements
- Hard constraints: budget ceiling, medication continuity, renewal deadline

### 2. Build a Real Utilization Profile
Estimate expected care load before discussing premiums:
- Routine care frequency (primary care, specialist, urgent care)
- Ongoing prescriptions and refill cadence
- Known procedures, therapies, or recurring diagnostics
- Worst-case risk profile for unexpected events

### 3. Compare Plan Mechanics Before Price
Always evaluate these mechanics before deciding on monthly premium:
- Network fit for current clinicians and facilities
- Deductible, out-of-pocket max, and coinsurance structure
- Copay design by care type (primary, specialist, urgent, emergency)
- Referral and prior-authorization friction for expected treatments
- Prescription formulary coverage for required medications

### 4. Model Yearly Cost With Scenarios
Use `references/cost-model.md` to calculate low, expected, and high-use annual totals.
Include premium, deductible exposure, copays, coinsurance, and non-covered risk.
Recommend using expected-cost and downside-risk together, rather than premium alone.

### 5. Protect Against Coverage Failure Modes
Run a risk check before final recommendation:
- Out-of-network emergency and balance-billing exposure
- Drug tier surprises and step-therapy limitations
- Referral bottlenecks that delay care
- High deductible plans that look cheap but shift excessive risk

### 6. Execute Enrollment With Evidence
Use `references/enrollment-playbook.md` to define exact actions, deadlines, and proof artifacts.
Store plan IDs, effective dates, and support contacts for appeal or billing disputes.
Wait for confirmation evidence before claiming enrollment is complete.

### 7. Persist Data Only With Explicit Approval
Before writing to `<state_root>/memory.md`, ask for explicit confirmation.
Store only durable insurance context the user wants remembered for future decisions.

## Common Traps

- Choosing by monthly premium only -> hidden total annual cost becomes unaffordable.
- Ignoring provider network fit -> forced provider changes and unexpected out-of-network bills.
- Skipping formulary checks -> medication cost spikes after enrollment.
- Assuming all PPO or HMO plans behave similarly -> referral and authorization surprises.
- Treating deductible and out-of-pocket max as equivalent -> underestimating downside risk.
- Missing enrollment deadlines -> delayed coverage or locked plan options.

## External Endpoints

This skill operates without making external network requests.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| None | None | N/A |

Data remains entirely local.

## Security & Privacy

**Data that leaves your machine:**
- Nothing. This skill is instruction-only and local by default.

**Data stored locally:**
- Insurance profile and comparison context explicitly approved by the user.
- Stored in `<state_root>/memory.md`.

**Skill boundaries:**
- Access insurer or broker APIs automatically.
- Submit enrollment forms or claims without user direction.
- Read files outside `<state_root>/` for storage.
- Write memory without explicit user confirmation.
- Modify its own core instructions or auxiliary files.

## Trust

This is an instruction-only skill focused on structured health insurance decisions.
No credentials are required and no external service access is needed.
