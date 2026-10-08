# Sonoff Orchestration Playbooks

Use these patterns for multi-device automation.

## Playbook 1: Safe Batch Rollout

1. Define target cohort and blast-radius cap.
2. Validate mode compatibility across the cohort.
3. Run a canary command on one device.
4. Verify state convergence.
5. Roll out in small batches with checkpoints.
6. Halt on repeated divergence and hand off to incident containment.

## Playbook 2: Mixed Plane Coordination

When cloud and LAN are both active:

- define primary plane and fallback plane up front
- prevent duplicate writes across planes for the same logical action
- verify state from one authoritative source per step
- log when the fallback path is triggered and why

## Playbook 3: Incident Containment

When states diverge or devices flap:

1. Freeze further writes.
2. Snapshot affected state across active planes.
3. Classify the issue: auth, mode mismatch, transport, offline device, or identity map drift.
4. Apply minimal corrective commands only after classification.
5. Verify recovery before resuming automation.

## Observability Baseline

Track for each run:

- run id and timestamp
- target count and success rate
- selected control plane
- first failure signature
- rollback or remediation outcome
- canary device id and canary result
