---
name: banking
description: >
  Run retail and business banking operations: request intake, payment controls,
  reconciliation triage, fraud containment, compliant customer messaging, and
  escalation boundaries. Use for onboarding workflows, transfers, disputes,
  outages, or ops guidance that must stay control-first; not for household
  budgeting (`money`), ledger teaching (`accounting`), outbound client invoices
  (`invoice`), product payment rails coding (`payments`), or portfolio picks
  (`invest`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏦"}'
  related-skills: '{"payments":"Implements product payment rails and transaction code paths once banking ops controls are clear.","accounting":"Teaches ledgers, GAAP/IFRS, and statement mechanics rather than live bank ops.","invoice":"Issues outbound client invoices and credit notes, not bank-side payment controls.","money":"Sequences household debt, buffers, and savings rather than bank operations.","invest":"Chooses accounts, brokers, and portfolios after cash and control questions are settled."}'
---

# Banking

Own **control-first banking operations support**: classify the request, confirm jurisdiction and account context, verify payment controls, contain fraud before root-cause work, and keep customer wording factual. This skill does not log into bank portals, move funds, or give definitive legal advice.

## State location

Banking operational notes may exist in `<workspace>/banking/`, `<workspace>/memory/banking/`, or `~/banking/`.
Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one; resolve it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/banking/`, `<workspace>/memory/banking/`, `~/banking/`.
3. If multiple candidates exist, keep only the highest-precedence directory, report the conflict, and leave siblings unchanged.
4. If none exists and notes must be created, default to `<workspace>/banking/` only after brief consent.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd. An existing `~/banking/` may be read; otherwise ask before creating data.
6. Keep the selected `<state_root>` fixed for the whole invocation.

Use the selected `<state_root>` for every state path in this skill. Outside this section, every skill-state path uses `<state_root>/...`. Skill resources stay under `references/`. Never treat the literal string `<state_root>` as a filesystem path. Never write full account numbers, authentication secrets, or unnecessary personal identifiers into state files. Never write learned preferences into `SKILL.md`.

```text
<state_root>/
├── memory.md              # Status, activation scope, operating context
├── incidents.md           # Open fraud and operations incidents
├── payment-controls.md    # Verified controls by rail and account type
└── communication-notes.md # Approved customer messaging patterns
```

Load `references/memory-template.md` before creating or reshaping state files. Load `references/setup.md` when `<state_root>` is missing or empty and setup is still authorized.

## When to use

- Retail or business banking ops: onboarding support, payment execution guidance, reconciliation triage
- Suspected fraud, unauthorized activity, payment outage, or control failure
- Customer-safe status wording that must stay neutral and time-bounded
- Escalation when KYC/AML/sanctions, legal interpretation, or irreversible release lacks approvals

**Not this skill**

| Job | Skill |
|-----|-------|
| Household debt / buffer / savings order | `money` |
| Ledger teaching / GAAP-IFRS judgment | `accounting` |
| Outbound client invoice PDF lifecycle | `invoice` |
| Product payment rail implementation | `payments` |
| Broker / fund / portfolio selection | `invest` |

## Ordered workflow

1. **Classify** — Label one primary category: onboarding, payment execution, reconciliation, fraud/incident, dispute/chargeback, or compliance/policy. If unclear, ask one short clarification. Load `references/intake-checklist.md`.
2. **Context** — Capture jurisdiction/region, customer type (consumer or business), account type, rail, urgency, and impacted funds before compliance-sensitive steps.
3. **Controls** — For any transfer path, verify ownership/beneficiary source, amount/currency/fees, cutoff, approval threshold, dual-control, and rollback/recall. If any required control is unknown, pause execution advice and request it. Load `references/payment-ops.md`.
4. **Incidents** — For unauthorized activity or funds at risk, contain first (freeze/hold when policy allows, preserve IDs/timestamps, notify owners), then scope, recover, and close out. Load `references/incident-response.md`.
5. **Communicate** — Status, owner, next step, and ETA window only. Load `references/customer-messaging.md` for templates.
6. **Escalate / bound** — Sanctions/AML indicators, KYC bypass, blocked-fund release without approvals, or definitive legal interpretation → specialist path. Load `references/compliance-scope.md`.
7. **Persist** — Write only durable controls, decisions, and incident outcomes under `<state_root>/` using the memory template.

## Always-on defaults

- Classify before product explanations or transfer steps.
- Jurisdiction and account context before compliance-sensitive guidance.
- Containment before root-cause on fraud / unauthorized activity.
- Plain status language: known facts, current action, owner, next checkpoint.
- Memory holds controls and outcomes only — no full PANs, auth secrets, or unnecessary PII.
- Operational guidance only: no bank-portal login, no automatic fund movement, no undeclared network calls, no self-modification of this skill package.
- Legal determinations go to qualified compliance/legal teams; this skill structures facts and controls.

## Failure branches

| Signal | Action |
|--------|--------|
| Category unclear | One clarifying question; hold multi-step guidance |
| Required control unknown | Pause execution advice; request the missing control |
| New beneficiary + urgent same-day wire | Treat as high-risk; run incident posture before release advice |
| Unauthorized / funds at risk | Containment path first; then intake and dispute docs |
| KYC/AML/sanctions bypass or identity alteration without evidence | Refuse; escalate per `references/compliance-scope.md` |
| User wants definitive legal conclusion | State boundary; route to qualified counsel with fact pack |
| Multiple state roots | Use highest-precedence only; report conflict; no auto-merge |

## Quick reference

| Need | Load |
|------|------|
| Domain rules, traps, security envelope | `references/domain.md` |
| First-use activation and context capture | `references/setup.md` |
| State file shapes and status values | `references/memory-template.md` |
| Intake fields and response sequence | `references/intake-checklist.md` |
| Rails, pre-exec controls, reconciliation | `references/payment-ops.md` |
| Severity, containment, recovery, closeout | `references/incident-response.md` |
| Customer-safe templates and banned wording | `references/customer-messaging.md` |
| In/out of scope and escalation triggers | `references/compliance-scope.md` |
| Verified primary sources for Gate 6 facts | `references/sources.md` |

Load at most one deep reference beyond the active workflow step unless the user explicitly asks for a second topic.
