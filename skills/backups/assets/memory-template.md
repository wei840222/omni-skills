# Backups state template

Create files under the resolved `<state_root>` only after consent when the directory does not already exist. Do not write secrets into these files.

## inventory.md

- Systems and data classes
- RPO / RTO targets
- Owners and escalation

## jobs.md

- Tool (`restic`, `borg`, `pg_dump`, …)
- Schedule
- Destination (media / account / region)
- Immutability flags

## restore-drills.md

| Date | Scope | Target environment | Duration | Result | Gaps |
| --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | | | | pass/fail | |

## retention.md

- Daily / weekly / monthly tiers
- Legal or compliance holds
- Last policy review date

## incidents.md

- Failed job id / timestamp
- Root cause
- Fix and follow-up drill
