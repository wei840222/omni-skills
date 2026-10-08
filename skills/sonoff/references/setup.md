# Setup - Sonoff

Read this when `<state_root>/` does not exist or is empty, or when the user asks for first-time SONOFF activation boundaries.
Keep onboarding short and immediately useful.

## Operating Priorities

- Answer the current user request first.
- Confirm when SONOFF support should auto-activate.
- Determine allowed execution mode: read-only, guided writes, or approved apply mode.
- Capture only context needed for reliable control and safe automation.

## First Activation Flow

1. Confirm activation boundaries early:
   - Should this activate whenever SONOFF, eWeLink, relay, switch, iHost, or LAN-control terms are mentioned?
   - Should behavior be proactive or only on explicit request?
   - Are there contexts where this is restricted from auto-activate?

2. Confirm environment model:
   - cloud-only, LAN-only, or mixed control
   - iHost presence and local API usage
   - DIY mode usage for compatible devices
   - primary objective (single-device control, fleet orchestration, diagnostics)

3. Confirm risk and write boundaries:
   - inspection only vs command execution allowed
   - one-device canary first vs batch rollout allowed
   - mandatory verification checkpoints after each write

4. If context is approved, initialize local workspace under the resolved `<state_root>`:

```bash
mkdir -p <state_root>
touch <state_root>/{memory.md,environments.md,devices.md,automations.md,incidents.md}
chmod 700 <state_root>
chmod 600 <state_root>/{memory.md,environments.md,devices.md,automations.md,incidents.md}
```

5. If `memory.md` is empty, initialize it from `memory-template.md`.

## Integration Defaults

- Default to read-only inspection until the user approves writes.
- Confirm control-plane precedence before the first command.
- Use one environment and one device cohort at a time during initial rollout.
- Require post-command verification before continuing to the next step.

## What to Save

- activation preferences and do-not-activate boundaries
- control-plane choices and mode eligibility assumptions
- model-specific command and capability mappings
- automation constraints, rollback rules, and recurring failures
- approved security and privacy constraints (without raw tokens)

## Guardrails

- Load cloud credentials from the environment; ask for configuration steps rather than pasted raw eWeLink tokens in chat.
- Mark write success only after observed state verification evidence.
- Stay inside authenticated, declared endpoints and platform policy controls.
