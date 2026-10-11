---
name: health-insurance
description: >
  Evaluate medical usage, model total annual health costs, and compare insurance
  plans. Use when selecting, comparing, or renewing health insurance coverage,
  weighing HDHP/HSA versus copay plans, checking network or formulary fit, or
  running enrollment and renewal deadlines. Not for clinical diagnosis (`doctor`),
  general health planning without plan choice (`health`), or pure household
  budgeting without insurance mechanics (`money`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏥"}'
  related-skills: '{"health":"Health planning context that informs insurance priorities before plan choice.","doctor":"Provider interaction and visit preparation once coverage constraints are known.","compare":"Generic side-by-side decision frameworks when the question is structure rather than insurance rules.","money":"Household cash-flow and budget sequencing around premiums and out-of-pocket risk."}'
---

# Health Insurance

Own **structured health-insurance decisions**: lock coverage context, build a utilization profile, compare plan mechanics before premium, model low/expected/high annual cost (including HSA/HDHP rules), surface coverage failure modes, and execute enrollment with evidence. This package stores only user-approved local notes under `<state_root>/`; it does not call insurer APIs or submit enrollments.

## State location

Health-insurance state may exist in `<workspace>/health-insurance/`, `<workspace>/memory/health-insurance/`, or `~/health-insurance/`.
Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one; resolve it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/health-insurance/`, `<workspace>/memory/health-insurance/`, `~/health-insurance/`.
3. If multiple candidates exist, keep only the highest-precedence directory, report the conflict, and leave siblings unchanged.
4. If none exists and notes must be created, default to `<workspace>/health-insurance/` only after brief consent.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd. An existing `~/health-insurance/` may be read; otherwise ask before creating data.
6. Keep the selected `<state_root>` fixed for the whole invocation.

Use the selected `<state_root>` for every state path in this skill. Outside this section, every skill-state path uses `<state_root>/...`. Skill resources stay under `references/`. Never treat the literal string `<state_root>` as a filesystem path. Never write full policy numbers, government IDs, payment credentials, or authentication secrets into state files. Never write learned preferences into `SKILL.md`.

```text
<state_root>/
├── memory.md       # Durable coverage profile and decision context
├── comparisons/    # Side-by-side plan worksheets
├── renewals/       # Deadline and renewal notes
└── notes/          # Short approved observations
```

Load `references/memory.md` before creating or reshaping state files. Load `references/setup.md` when `<state_root>` is missing or empty and setup is still authorized.

## When to load

Load for plan selection, renewal, HDHP/HSA versus traditional plan trade-offs, network/formulary checks, annual cost modeling, or enrollment/renewal deadline execution. Prefer adjacent skills when the ask is clinical care planning (`doctor`), general health habits without insurance choice (`health`), generic comparison framing (`compare`), or household budget sequencing without plan mechanics (`money`).

## Progressive disclosure

Load a reference only when that topic is in scope:

| Topic | Load |
|-------|------|
| First-use activation and context capture | `references/setup.md` |
| State file shape and status values | `references/memory.md` |
| Plan structure and coverage fit | `references/coverage-framework.md` |
| Annual cost scenarios and HSA/HDHP limits | `references/cost-model.md` |
| Final decision QA checklist | `references/comparison-checklist.md` |
| Enrollment, OEP/SEP, and proof artifacts | `references/enrollment-playbook.md` |
| Verified primary sources for limits and dates | `references/sources.md` |

Load at most one deep reference beyond the active workflow step unless the user explicitly asks for a second topic.

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
Include premium, deductible exposure, copays, coinsurance, HSA adjustments when relevant, and non-covered risk.
Recommend using expected-cost and downside-risk together, rather than premium alone.
Refresh IRS HSA/HDHP dollar limits from `references/sources.md` before citing a plan-year figure.

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

- Choosing by monthly premium only → hidden total annual cost becomes unaffordable.
- Ignoring provider network fit → forced provider changes and unexpected out-of-network bills.
- Skipping formulary checks → medication cost spikes after enrollment.
- Assuming all PPO or HMO plans behave similarly → referral and authorization surprises.
- Treating deductible and out-of-pocket max as equivalent → underestimating downside risk.
- Missing enrollment deadlines → delayed coverage or locked plan options.
- Citing stale HSA/HDHP limits → wrong tax-year contribution or OOP ceiling advice.

## Failure branches

| Signal | Action |
|--------|--------|
| Coverage target or source unclear | One clarifying question; hold multi-plan modeling |
| Required medication or provider unknown | Ask before ranking plans that gate on formulary/network |
| Plan-year HSA/HDHP dollars needed | Load `references/cost-model.md` + `references/sources.md`; quote year explicitly |
| Enrollment deadline inside 7 days | Switch to enrollment playbook; prioritize proof capture |
| User asks clinical diagnosis or treatment choice | State boundary; route care questions to `doctor` / clinicians |
| Multiple state roots | Use highest-precedence only; report conflict; no auto-merge |

## Security & Privacy

**Operational envelope**
- Instruction-only and local by default: no undeclared network calls, no insurer/broker login, no automatic enrollment or claim submission.
- Keep every durable note under the resolved `<state_root>/` after explicit user approval.
- Strip secrets and high-sensitivity identifiers before any write; keep plan nicknames, tiers, and decision context only.

**Data that leaves your machine**
- Nothing by default. This skill does not require credentials or external service access.

**Data stored locally (only with approval)**
- Insurance profile and comparison context the user wants remembered.
- Paths stay under `<state_root>/memory.md`, `comparisons/`, `renewals/`, and `notes/`.

## Trust

This is an instruction-only skill for structured health-insurance decisions.
No credentials are required. Dollar limits and marketplace dates in references are orientation baselines; re-check `references/sources.md` (and the live IRS / HealthCare.gov pages) before giving year-specific advice.
