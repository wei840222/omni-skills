# Topology and Network Placement

## Placement defaults

| Concern | Default | Escalate when |
|---------|---------|---------------|
| Failure domain | Multi-AZ in one region | Correlated AZ risk, residency, or RTO needs a second region |
| Workload subnets | Private | Only controlled ingress (LB, API gateway) is public |
| Service discovery | DNS / platform service names | Hard-coded IPs block migration |
| East-west trust | Authenticate and encrypt internal paths | Perimeter-only trust is insufficient under breach assumptions |
| Blast radius | Cells or bulkheads by tenant/cohort | A single shared data plane would take all users down together |

## Networking rules

- Public exposure only at load balancers or equivalent ingress; application runtimes stay private.
- Plan multi-account or multi-project connectivity (peering, hub-and-spoke, transit) before the account count explodes.
- Segment networks so a compromised tier cannot freely roam (security groups/NACLs/firewall policies as defense in depth).
- Prefer platform-native service identity over long-lived network-location trust alone.
- Keep packet-level debugging (`dig`, route tables, TLS handshake failures) in the `network` skill; this file decides placement, not packet forensics.

## Multi-region patterns

- **Warm standby** — replica data + scaled-down compute; moderate RTO, lower steady cost.
- **Hot standby / active-passive** — near-ready compute; faster RTO, higher cost.
- **Active-active** — only with clear data-conflict rules, global traffic management, and operational skill to run it.

Choose the weakest pattern that still meets documented RTO/RPO. Active-active without a conflict story is an outage generator.

## Cell-based and bulkhead ideas

- Split serving into cells that own a user or tenant shard.
- Limit blast radius so one bad deploy or dependency failure cannot take 100% of traffic.
- Apply bulkheads between critical and best-effort paths (checkout vs recommendations).
