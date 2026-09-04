# Incident response

Use this reference for an outage, suspected data loss, security event, or materially degraded service.

## Severity

- **Sev-1:** data at risk or total outage.
- **Sev-2:** major feature unavailable with a workaround.
- **Sev-3:** degraded performance or isolated failure.

## First five minutes

1. Stabilize by pausing automated changes and preserving available evidence.
2. Scope affected services, users, data paths, and recent changes.
3. Contain the fault by separating failed components from healthy traffic.
4. Communicate a concise status and next-update time to the affected owner.

Inspect service health, listening ports and connection errors, free space/I/O/filesystem status, and reverse-proxy, application, and host-security logs. Capture sanitized evidence that excludes credentials and unredacted environment files.

## Recovery sequence

1. Restore control-plane dependencies such as DNS, proxy, and authentication.
2. Recover stateful stores from the latest **verified** snapshot.
3. Restore stateless services.
4. Run functional smoke checks before returning full traffic.

If no verified snapshot exists, preserve the current state, state the recovery gap, and obtain an owner decision before attempting destructive remediation or an alternate recovery path.

## Follow-up

With approval, record a timeline, contributing factors, preventive actions with owners/dates, and detection improvements in `<state_root>/incidents.md`.
