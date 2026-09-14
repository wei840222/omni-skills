# Routing and escalation

## Domain routing

Route by expertise, not a single catch-all schedule:

| Signal class | Default owner |
|---|---|
| Database / storage durability | Data / DB team |
| API / backend latency and errors | Backend team |
| Cost, quota, platform limits | Platform team |
| Security / auth anomalies | Security on-call |
| Agent quality / loop / tool failures | Agent platform or owning product team |

Override with the user's real roster; the table is a starting template only.

## Progressive escalation

Example P1 ladder (adjust to the user's tooling):

1. Chat / ticket notification (immediate)
2. Wait ~5 minutes without ack → SMS / push
3. Wait ~10 more minutes → phone / high-urgency page
4. P0 lasting **>30 minutes** or impact **>100 users** (or user-defined blast radius) → add manager / incident commander

Always attach:

- severity
- correlation ID
- runbook URL (mobile-reachable)
- current blast radius estimate

## Time and impact context

- **Business hours:** primary team for P2+; still page P0/P1 per policy.
- **Off-hours:** on-call only for P0/P1 unless the user expands coverage.
- **Large blast radius:** escalate immediately even if the nominal severity looks low.

## Handoffs

- `notify` decides channel batching and quiet hours once the alert decision exists.
- `remind` is wrong for brand-new outages; it is for commitments already known to the user.
- `report` digests trends later; do not replace a P0 page with a daily email.
