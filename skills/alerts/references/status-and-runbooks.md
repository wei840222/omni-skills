# Status page and runbook automation

## Status page

When P0/P1 fires:

1. Open or update an incident within ~5 minutes of confirm.
2. Post a short initial assessment, ETA if known, and workaround if any.
3. Map alert labels to **components** (API, Database, Auth, Agent workers, etc.).
4. Partial impact → **Degraded Performance** (or equivalent), not “Operational”.
5. Resolve the incident only when the parent alert clears and synthetic checks pass.

Keep public wording factual; no internal secrets, no blame.

## Runbook links

- Every page should include a mobile-reachable runbook URL.
- Prefer stable wiki paths over chat scrollback.
- Format example: `Alert: High CPU on web. Runbook: https://wiki.example/runbooks/high-cpu-web`

## Automated remediation

Safe to automate when reversible and logged:

- restart a clearly stuck service unit
- clear known full-disk temp paths the user pre-approved
- reset rate-limit counters when the provider API supports it safely

**Require human approval** before:

- scaling down capacity
- deleting data or queues
- production schema / IAM changes
- anything irreversible or cross-tenant

## Audit log

For each automated action record:

- timestamp
- action
- target
- result
- correlation ID
- approval chain (none / user / manager)

Store under `<state_root>/alerts/incidents/` only when the user wants persistence.

## Post-incident

- Keep a short timeline: detect → page → mitigate → resolve.
- Feed noisy rules back into `fatigue.md` changes.
- Do not auto-write long postmortems unless the user asks.
