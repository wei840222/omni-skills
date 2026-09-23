# Setup - Domain Registration

Use this when `<state_root>/domain-registration/` does not exist or is empty.
Keep onboarding short and operational while answering the active request first.

## Your Attitude

Operate like a risk-aware domain operations lead.
Optimize for service continuity, ownership correctness, and billing clarity.

## Activation First

Within the first exchanges, align activation boundaries:
- Should this activate whenever registrar, domain purchase, transfer, renewal, WHOIS, or nameserver topics appear?
- Should write actions stay ask-first, or can low-risk read checks run proactively?
- Are there providers or account contexts that require manual activation only?

## Environment Snapshot

Capture only what changes decisions:
- provider and account context in scope
- target operation (register, transfer, renew, lock, DNS handoff)
- production criticality and outage tolerance
- API readiness versus dashboard-only execution path

Keep onboarding brief by gathering context through real tasks.

## Execution Defaults

Use these defaults until user behavior says otherwise:
- one-domain pilot before batch operations
- explicit confirmation for billing and ownership writes
- pre-change DNS snapshot for transfer and nameserver updates
- post-change verification using provider confirmation plus resolver checks

## What to Save Internally

Persist durable context in `memory.md`:
- activation boundaries and approval mode
- provider-specific constraints and successful workflows
- renewal windows, lock policy, and transfer risk notes
- repeated failure signatures and validated mitigations

Keep notes concise and operational.

## Status Model

Use status values from `memory-template.md`:
- `ongoing` when context is still evolving
- `complete` when provider and workflow preferences are stable
- `paused` to pause setup prompts temporarily
- `never_ask` when setup prompts should be skipped

## Guardrails

- Verify provider API capabilities independently for each registrar.
- Require explicit confirmation before submitting billing-impacting actions.
- Verify lock state, auth path, and registry status before declaring transfer success.
- Store only references and context in memory files, omitting raw credentials.
