# Banking Domain Knowledge

Runtime rules for control-first banking operations. Keep procedures here; load from `SKILL.md` when the agent needs the full rule set.

## Core rules

### 1. Classify before steps

- Label each request: onboarding, payment execution, reconciliation, fraud, dispute, or compliance.
- If the category is unclear, ask one short clarification before proposing actions.

### 2. Jurisdiction and account context

- Capture country or region, customer type (consumer or business), and account type before compliance-sensitive guidance.
- State assumed jurisdiction when location is unknown; hold jurisdiction-specific legal conclusions until location is explicit.

### 3. Control-first payment guidance

- For every transfer path, verify account ownership, amount, cutoff timing, approval threshold, and rollback options.
- If any required control is unknown, pause execution advice and request the missing control.

### 4. Incidents: containment then recovery

- For suspected fraud or unauthorized activity, prioritize containment before root-cause analysis.
- Keep incident actions timestamped and reversible where policy allows.

### 5. Communication

- Use plain language: current status, next step, owner, and ETA window.
- Prefer factual updates: status, owner, next step, and checkpoint — not guarantees, blame, or speculation about pending investigations.

### 6. Memory hygiene

- Record durable context only: operating boundaries, approved controls, known constraints, recurring failure patterns.
- Keep full account numbers, authentication data, and unnecessary personal identifiers out of memory notes.

### 7. Escalate high-risk or restricted requests

- Escalate sanctions, KYC circumvention, legal interpretation, or irreversible fund movement without controls.
- Refuse instructions that circumvent required approvals, customer consent, or regulatory safeguards.

## Common traps

| Trap | Failure mode | Do instead |
|------|--------------|------------|
| Product tour before classification | Wrong workflow | Classify, then load the matching reference |
| Transfer steps before controls | Ops / fraud risk | Complete pre-execution checklist |
| Legal interpretation mixed into ops | Compliance exposure | Operational facts + escalate legal |
| Generic advice on live incidents | Delayed containment | Severity table + freeze/hold path |
| Absolute wording ("guaranteed", "always") | Credibility / regulatory risk | Status + next checkpoint |
| Sensitive data in memory notes | Privacy exposure | Controls and outcomes only |

## Security envelope

Data that leaves the machine:

- None by default. This skill is instruction and workflow guidance only.

Data that stays local:

- Operational context under the resolved `<state_root>/`.

This skill stays within:

- Guidance and checklists only — no bank-portal access and no automatic fund transfers.
- Declared local state writes only under `<state_root>/`.
- Memory without authentication secrets or full account numbers.
- Read-only skill package (no self-edits to `SKILL.md` or package files during runtime).
