# Product-launch operating references

Use this reference when turning the launch plan into an operational rollout, choosing a limited release, or defining launch monitoring. It supplements the core positioning, asset, channel, and retention guidance in `SKILL.md`.

## Safe rollout and recovery

Treat the launch as a reversible delivery process where the product architecture permits it:

1. Define a small initial audience and a success/abort signal before expanding distribution.
2. Exercise the sign-up, activation, support, and incident paths with that audience; record the result and the owner for each blocker.
3. Expand only after the agreed signals hold. Keep a rollback, feature-disable, or traffic-stop action ready for failures that affect users or data.
4. If a launch signal crosses its abort threshold, pause the next audience wave, communicate the current impact, stabilize the affected path, and reassess from fresh evidence rather than resuming on schedule.

A public announcement can be hard to retract, so use a soft launch to test the operational path. Where a product cannot be rolled back safely, use a narrower audience and an explicit incident plan instead of claiming reversibility.

## Monitoring plan

Before launch, name a small set of signals and thresholds that match the product:

| Signal | Why it matters | Example response when outside its threshold |
| --- | --- | --- |
| Successful sign-up and activation | Detects a broken first-use journey. | Pause the next audience wave; diagnose the failing step and verify the fix end to end. |
| Error rate and latency | Detects availability or capacity regressions. | Reduce traffic, apply the documented mitigation, and recheck the service-level signal. |
| Support volume and recurring issue | Detects confusion or unhandled user impact. | Update the support response and product guidance; escalate confirmed defects to the incident owner. |
| Retention or repeat use | Distinguishes durable adoption from an announcement spike. | Prioritize onboarding and lifecycle improvements before further acquisition spend. |

Choose thresholds from the product's normal baseline and capacity plan; do not reuse generic conversion or retention percentages as release gates. Assign an owner and check cadence for each signal before launch day.

## Sources

### Release safety and progressive exposure

- Google SRE, *Canary Release: Deployment Safety and Efficiency* — https://sre.google/workbook/canarying-releases/
  - Supports limited exposure, measurable release signals, and rollout control before broader release.

### Monitoring design

- Google SRE, *Monitoring Systems with Advanced Analytics* — https://sre.google/workbook/monitoring/
  - Supports selecting actionable monitoring signals and using monitoring to drive operational response.
