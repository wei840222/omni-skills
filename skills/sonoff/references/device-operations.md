# Sonoff Device Operations Workflow

Use this sequence for reliable command execution on SONOFF devices.

## Canonical Control Loop

1. Resolve target devices and mode eligibility.
2. Read baseline status through the selected control plane.
3. Validate method/path and payload fields for the specific model.
4. Execute the command.
5. Re-read status and verify expected state.
6. Record the result; halt on mismatch.

## DIY Mode Local Pattern

For compatible DIY devices, use the local HTTP API path family (commonly `/zeroconf/*`) with explicit device id and data payload validation. Confirm discovery metadata and firmware expectations before treating a path as universal across models.

## High-Impact Device Classes

Apply stronger confirmation for:

- high-current relays and contactors
- heating and energy-critical circuits
- locks, alarms, and security-sensitive triggers

## Write Discipline

- Use one-device canary before batch commands.
- Bound retries and log the first-failure signature.
- Abort the full batch on the first critical verification failure.

## State Validation

- Treat command acknowledgment as intermediate, not final success.
- Require observed final state match before marking the task complete.
- When cloud and LAN disagree, reconcile identity mapping before another write; prefer reachable LAN observation for immediate local decisions when policy allows.
