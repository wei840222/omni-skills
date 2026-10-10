# Memory Template - Banking

Create `<state_root>/memory.md` with this structure when persistent notes are authorized:

```markdown
# Banking Memory

## Status
status: ongoing
version: 1.1.0
last: YYYY-MM-DD
integration: pending | complete | paused | never_ask

## Activation
- Auto-activate when:
- Activate only on explicit request for:
- Exclude activation for:

## Operating Context
- Jurisdiction:
- Customer profile:
- Account types:
- Payment rails:
- Cutoff windows:
- Approval controls:

## Active Incidents
- Incident:
  - Category:
  - Detection time:
  - Containment:
  - Current status:
  - Next action:

## Approved Communication Patterns
- Scenario:
  - Internal update format:
  - Customer update format:
  - Escalation trigger:

## Known Risks and Constraints
- Constraint:
  - Impact:
  - Mitigation:

## Notes
- Decision:
- Follow-up:

---
*Updated: YYYY-MM-DD*
```

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Context is still evolving | Keep gathering operational constraints naturally |
| `complete` | Context is sufficient | Run workflows without setup prompts |
| `paused` | User paused setup refinements | Continue with current context only |
| `never_ask` | User rejected setup prompts | Skip setup follow-ups going forward |

## Principles

- Keep entries brief, factual, and easy to verify.
- Update `last` after every meaningful banking workflow session.
- Store decisions and controls; keep sensitive raw account data out.
- Preserve incident history with timestamps and explicit outcomes.
- Optional companions under the same root: `incidents.md`, `payment-controls.md`, `communication-notes.md`.
