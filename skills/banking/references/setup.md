# Setup - Banking

Read when `<state_root>/` is missing or empty and the user has authorized persistent banking notes.

## Attitude

Stay calm, exact, and operationally conservative. Optimize for safe execution, clear ownership, and fast recovery.

## Priority order

### 1. Integration

Define activation boundaries so this skill triggers in the right banking situations.

- Which banking topics should auto-activate.
- Whether to activate proactively for fraud and payment incidents.
- Where it should stay inactive and defer to another skill (`money`, `payments`, `accounting`, and similar).

### 2. Operating context

Collect only context required for accurate guidance.

- Jurisdiction and regulatory environment.
- Customer type (consumer, SMB, enterprise) and account types in scope.
- Supported payment rails and cutoff windows.
- Approval thresholds, dual-control policies, and escalation contacts.

### 3. Response preferences

- Preferred detail level for procedures and checklists.
- Incident posture: speed-first, precision-first, or balanced.
- Escalation style: immediate handoff or staged triage summary first.
- Communication tone for customer-facing updates.

## What to capture internally

Keep concise notes in `<state_root>/memory.md` and refresh after meaningful changes. Use `references/memory-template.md` for structure.

- Activation boundaries and activation-excluded contexts.
- Jurisdiction, account scope, and policy constraints.
- Approved payment controls and known failure points.
- Incident patterns with containment outcomes.
- Customer communication patterns accepted by stakeholders.

Create optional files (`incidents.md`, `payment-controls.md`, `communication-notes.md`) only when that feature is actually used.
