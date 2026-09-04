# Service inventory

Use this reference when designing, documenting, or auditing a service inventory. Keep the inventory in `<state_root>/services.md` only after the user approves persistent state.

## Required fields

- Service name and purpose
- Runtime: container, VM, or host process
- Data location and backup owner
- Exposure: LAN-only, VPN-only, or internet-facing
- Authentication boundary and administration-access policy
- Health-check source and alert destination

| Service | Runtime | Data path | Exposure | Backup | Health check |
|---|---|---|---|---|---|
| Example: nextcloud | Docker | `/srv/nextcloud` | VPN-only | Nightly snapshot | Uptime probe |

Assign each service a primary and fallback owner. Record a reverse-proxy route for every intended internet-facing service, and record the tested restore procedure for every stateful service. Review health and disk trends weekly, patch and certificate status monthly, and run a restore drill plus dependency review quarterly.
