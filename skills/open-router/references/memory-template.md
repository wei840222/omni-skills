# Routing State Template

When persistent state is authorized, create `<state_root>/memory.md` with this structure:

```markdown
# OpenRouter Memory

## Status
status: ongoing
last: YYYY-MM-DD
integration: pending | complete | paused | skip_setup

## Activation
- Auto-activate when:
- Explicit-only topics:
- Out-of-scope topics:

## Stack Context
- Client type:
- Provider wiring:
- Auth mode:
- Region or latency constraints:

## Routing Policy
- Workload class:
- Primary model:
- Fallback model:
- Trigger for fallback:

## Budget Guardrails
- Monthly budget:
- Per-task budget:
- Escalation threshold:

## Incident Log
- Date:
- Failure mode:
- Impact:
- Verified fix:
```

`ongoing` means routing context is still changing; `complete` means use the established policy; `paused` means retain it without new setup questions; `skip_setup` means avoid setup prompts. Store decisions and outcomes, never raw secrets.
