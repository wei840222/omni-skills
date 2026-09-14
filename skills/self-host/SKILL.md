---
name: self-host
description: >
  Deploy and maintain self-hosted services with Docker, reverse proxies, backups,
  and long-term reliability. Use for home-server or VPS service planning, compose
  hardening, private networking, SSL, monitoring, and restore-tested backup loops.
  Prefer `docker`/`docker-compose` for runtime debugging, `caddy`/`traefik` for
  proxy syntax, `sysadmin` for host surgery, and `home-server` for full homelab design.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🖥️","requires":{"anyBins":["docker","podman"]}}'
  related-skills: '{"docker":"Container runtime, image, and Compose trap debugging when the ask is Docker mechanics rather than whole-service self-host strategy.","docker-compose":"Multi-container Compose definitions and dependency wiring.","caddy":"Caddyfile reverse-proxy and automatic HTTPS configuration.","traefik":"Traefik routers, entrypoints, TLS, and Docker labels.","sysadmin":"Linux host administration, packages, storage, and diagnostics under the service stack.","home-server":"Broader homelab design covering remote access, NAS, and household network layout.","backups":"Dedicated backup strategy design beyond the self-host checklist defaults."}'
---

## When to load

Load this skill when the user asks to deploy, harden, or maintain a self-hosted service on a home server or VPS: Docker/Podman stacks, reverse proxies, private databases, SSL, monitoring, backups, or long-term ops hygiene.

Prefer more specific skills when the ask is narrow:

- `docker` / `docker-compose` — runtime, image, or Compose debugging
- `caddy` / `traefik` — reverse-proxy syntax and TLS wiring
- `sysadmin` — host-level Linux surgery without a service-strategy ask
- `home-server` — full homelab architecture beyond one service stack
- `backups` — deep backup/restore program design

## State location

Resolve `<state_root>` in this order:

1. Explicit user- or host-configured state path when supplied
2. `<workspace>/.agents/state` when a local workspace is active
3. `$XDG_DATA_HOME` when set
4. `~/.local/share` on Linux/macOS defaults

Resolve once per invocation and keep it fixed. Prefer portable `<state_root>` paths; never hard-code host-specific roots such as `~/Clawic/data/self-host/`.

Skill state lives under `<state_root>/self-host/`. Create the directory only when the first persistent write is required.

```text
<state_root>/self-host/
|-- inventory.md        # Services, ports, owners, compose paths
|-- compose/            # Reviewed compose templates (optional)
|-- backup-notes.md     # What is backed up and last restore test
`-- runbooks/           # Service-specific recovery notes (optional)
```

## Progressive disclosure

| Situation | Load |
|-----------|------|
| Pre-deploy checklist, Docker defaults, networking, SSL, security, backups, monitoring, maintenance | `references/self-host-rules.md` |
| Verifiable source anchors for Gate 6 research and product docs | `references/sources.md` |

## Core workflow

1. **Inventory first** — name the service, data path, ports, auth boundary, and backup owner before writing compose.
2. **Isolate** — one project network, private DB ports, reverse proxy as the only public edge.
3. **Pin and persist** — pin image tags, named volumes/bind mounts, explicit restart policy.
4. **Secure** — change defaults, bind admin UIs to localhost or auth gateway, no secrets in git.
5. **Observe** — uptime, disk, and log rotation before go-live.
6. **Prove restore** — a backup without a tested restore is not done.
7. **Document** — record compose path, ports, and recovery notes under `<state_root>/self-host/`.

## Critical rules

1. Decide backup location and restore method before the first real data write.
2. Never publish database ports to the public internet; keep them on an internal Docker network.
3. Pin image versions; avoid floating `latest` for anything that holds state.
4. Prefer VPN (WireGuard/Tailscale) over broad port-forwarding for admin access.
5. Keep secrets in env files or a secret store excluded from git — never in committed compose.
6. Test restores, not only backup jobs.
7. Prefer simple, maintained stacks over day-one over-engineering.

## Failure modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| OOM / corrupt DB after deploy | Container restarts, I/O errors, missing writes | Check host RAM/limits; restore from last known-good volume backup |
| Accidental public DB port | `docker ps` / security scan shows host bind on 5432/3306/27017 | Remove host `ports`, keep internal network only, rotate credentials |
| Disk full from Docker logs | Writes fail, containers unhealthy | Enable log rotation; prune unused images/volumes after backup confirmation |
| Untested backup | Restore drill fails or path missing | Fix backup scope, re-run restore to a scratch location, update notes |
| Stale unmaintained image | CVEs, broken upstream, abandoned repo | Replace with maintained alternative; pin new tag; re-validate restore |

## Quick checks before go-live

- [ ] Named volume or bind mount for durable data
- [ ] Image tag pinned
- [ ] Restart policy set (`unless-stopped` or `on-failure`)
- [ ] DB/admin ports not publicly published
- [ ] Reverse proxy terminates TLS
- [ ] Default passwords changed
- [ ] Backup job + restore drill recorded
- [ ] Log rotation enabled
