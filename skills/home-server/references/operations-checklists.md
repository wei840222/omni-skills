# Operations checklists

Use this reference for routine operations, maintenance windows, or planned changes.

## Daily signals

- Review failed health checks, disk-utilization trend, and backup-job results.
- Treat missing monitoring data, stale backups, or unexplained capacity growth as a condition to investigate before making further changes.

## Weekly maintenance

- Review host and container update advisories, rotate or retain logs according to the service policy, and compare exposed ports with the intended exposure inventory.

## Before an upgrade

1. Verify the backup snapshot age and the latest restore evidence are acceptable for the service’s recovery objective.
2. Capture a sanitized deployment snapshot: image identifiers, ports, mounted paths, feature flags, and the rollback trigger.
3. Define the rollback owner and communication path.
4. Apply changes in a low-risk order: reverse proxy, shared services, then applications.

If backup or rollback evidence is unavailable, pause the upgrade plan and restore that evidence first. Keep raw environment variables and secret values out of notes; record sanitized placeholders instead.

## After an upgrade

- Validate login flow and critical user actions.
- Compare resource use with the pre-upgrade baseline.
- Record a brief result in `<state_root>/incidents.md` or the relevant operational log only with user approval.

## Monthly reliability check

- Exercise at least one end-to-end restore path.
- Reassign or retire services without an owner.
- Turn persistent warnings into owned actions with a due date.
