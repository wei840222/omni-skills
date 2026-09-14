# Self-Hosting Rules

Operational checklist for deploying and maintaining self-hosted services with Docker/Podman. Load this file when planning a new stack or reviewing an existing one.

## Before Installing Anything

- Backups first — decide where data lives and how it is backed up before deploying, not after data exists
- Check resource requirements — many services need more RAM than expected; OOM kills corrupt data
- Verify the project is actively maintained — abandoned projects become security liabilities
- Record service owner, compose path, ports, and restore owner in `<state_root>/self-host/inventory.md`

## Docker Fundamentals

- Always use named volumes or bind mounts for persistent data — anonymous volumes are lost on container removal
- Pin image versions (`nginx:1.25.3` not `nginx:latest`) — latest changes unexpectedly and breaks setups
- Set restart policy (`unless-stopped` or `on-failure`) — containers require explicit restart policies to start after reboot
- Use `docker compose down` not `docker compose rm` — down handles networks and volumes properly
- Prefer one compose project per service boundary so networks and volumes stay auditable

## Networking

- Keep database ports private and internal — only the reverse proxy should have public exposure
- Use a reverse proxy (Traefik, Caddy, Nginx Proxy Manager) — handles SSL, routing, and security in one place
- Create Docker networks per project — default bridge network lacks DNS resolution between containers
- Bind admin interfaces to localhost only (`127.0.0.1:8080:8080`) — not all traffic needs to be public
- Prefer WireGuard/Tailscale for remote admin over broad WAN port forwards

## SSL and Domains

- Use automatic SSL with Let's Encrypt — Caddy and Traefik do this natively
- For local/LAN access, use a real domain with DNS challenge — prevents browser certificate warnings
- Wildcard certificates simplify multi-service setups — one cert for `*.home.example.com`
- Re-verify ACME challenge type (HTTP-01 vs DNS-01) against current proxy docs before quoting steps

## Security Essentials

- Change all default passwords immediately — bots scan for default credentials within hours
- Enable automatic security updates for the host OS — unpatched systems get compromised
- Use fail2ban or equivalent — brute force attacks are constant
- Keep services behind authentication (Authelia, Authentik, or built-in auth) — not everything has safe defaults
- Disable root SSH; use key-only authentication — password SSH is a vulnerability
- Never commit secrets in `docker-compose.yml`; use `.env` / secret mounts excluded from version control

## Backups

- Test restores, not just backups — untested backups are wishful thinking
- 3-2-1 rule: 3 copies, 2 different media, 1 offsite — local RAID is not backup
- Automate backup schedules — manual backups get forgotten
- Back up Docker volumes, not containers — containers are ephemeral, data is not
- Record last successful restore drill in `<state_root>/self-host/backup-notes.md`

## Monitoring

- Set up uptime monitoring (Uptime Kuma is self-hostable) — know when services die before users tell you
- Monitor disk space — full disks cause silent failures and corruption
- Log rotation is mandatory — Docker logs grow forever by default and fill disks
- Consider resource monitoring (Netdata, Prometheus) — spot problems before they are critical

## Maintenance

- Schedule regular update windows — services need updates; plan for downtime
- Document everything you deploy — future you will not remember why that container exists
- Keep a compose file repo — reproducibility matters when hardware fails
- Test updates on staging when possible — production surprises are painful
- After image bumps, re-check volume mounts, env keys, and reverse-proxy upstream ports

## Home Server Specifics

- Dynamic DNS if the ISP does not provide a static IP — Cloudflare, DuckDNS work well
- UPS protects against power-loss corruption — especially important for databases
- Consider power consumption — some hardware costs more in electricity than cloud hosting
- Port forwarding exposes the home network — prefer VPN instead when possible

## Common Mistakes

- Putting everything on one machine with no redundancy — single point of failure for all services
- Ignoring updates for months — security vulnerabilities accumulate
- No firewall rules — assuming "nobody knows my IP" is not security
- Storing secrets in docker-compose.yml committed to git — use env/secret files excluded from VCS
- Over-engineering from day one — start simple, add complexity when needed
