---
name: server
description: >
  Manage web and application services on a host: process supervision, ports,
  reverse-proxy handoff, TLS termination boundary, worker sizing, deployments,
  and hop-by-hop troubleshooting. Use when a service fails to survive reboot,
  returns 502/504/413/499, binds the wrong interface, needs worker/pool/timeout
  sizing, needs a symlink release with rollback, or a Compose/self-hosted app
  must stay healthy behind a proxy. Not for nginx directive-level tuning
  (`nginx`), Caddyfile syntax (`caddy`), certificate issuance/renewal (`ssl`),
  host OS failures such as boot/cron/disk/permissions (`linux`), image builds
  (`docker`), Kubernetes (`k8s`), or machine provisioning/firewalling (`vps`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🖥️"}'
  related-skills: '{"caddy":"Caddyfile syntax and automatic HTTPS when the edge is Caddy.","docker":"Image builds and container runtime internals beyond host service handoff.","k8s":"Kubernetes workloads instead of single-host process supervision.","linux":"Host boot, disks, permissions, cron, and OOM underneath the service layer.","nginx":"Directive-level nginx configuration and debugging beyond service topology.","ssl":"Certificate issuance, renewal, and chain problems at the TLS boundary.","vps":"Provisioning, SSH hardening, and firewalling the machine itself."}'
---

# Server

Service-layer judgment for single-host web and application stacks. Preferences and
observed inventory may persist under a portable `<state_root>`; package depth stays
under `references/`.

## State location

Server state may exist in `<workspace>/server/`, `<workspace>/memory/server/`, or
`~/server/`. `<workspace>` means the workspace root provided by the host/runtime,
not the shell cwd.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/server/`, `<workspace>/memory/server/`, `~/server/`.
3. If none exists and state must be created, default to `<workspace>/server/`.

Use the selected `<state_root>` for every state operation in this skill.

| Path | Required? | Role |
|------|-----------|------|
| `<state_root>/config.yaml` | optional | Proxy, supervisor, OS family, and safety defaults the user declared |
| `<state_root>/memory.md` | optional | Observed services, baselines, incidents, `## Boxes`, `## Due` (no secrets) |
| `<state_root>/artifacts/` | optional | Working unit/vhost snippets captured during emergencies |

If legacy data exists only under `~/.clawic/server/` or similar vendor paths, treat
it as a migration source — move only after the user asks, then say in one line what
moved and from where. Never treat the literal string `<state_root>` as a filesystem
path. Never store credentials, private keys, or full connection strings under
`<state_root>/`; write pointers such as `env:DATABASE_URL` or `file:/etc/myapp/env`.

Shared inventories stay outside this package:

- hosts → `<workspace>/servers/servers.md`
- domains → `<workspace>/domains/domains.md`

This skill owns the *service* layer: which process runs where, on which port, under
which supervisor. In a shared box, update or remove only rows this skill wrote.

## When to load

Load when the user needs:

- a web/app service that survives reboot, logout, and crash (units, sockets, users, ports)
- reachability failures while the process appears up: refused, wrong interface, 502/504/413/499, redirect loops, broken WebSockets or uploads
- sizing what is already live: workers, pools, keepalive, timeouts, file descriptors
- shipping a version with a named rollback artifact (release dirs + `current` symlink)
- keeping Compose / self-hosted apps alive behind a proxy

Hand off when a sibling owns the job:

| Job | Skill |
| --- | --- |
| nginx directive-level tuning | `nginx` |
| Caddyfile / Caddy auto-HTTPS details | `caddy` |
| certificate issuance, renewal, chain | `ssl` |
| host boot, disks, permissions, cron, OOM | `linux` |
| image builds / container runtime internals | `docker` |
| Kubernetes workloads | `k8s` |
| machine provision, SSH harden, firewall | `vps` |

## Core path

1. **Name the hops** before editing: client → proxy → app → dependency. The layer that emits the error is rarely the owner.
2. **Read-only evidence first**: listeners (`ss -tlnp`), supervisor state, effective configs, recent logs.
3. **One reversible change**: validate syntax, prefer reload over restart, confirm impactful commands.
4. **Verify on the affected path**, then record durable facts under `<state_root>`.
5. **Load depth on demand** — one file under `references/` for the current job.

Working defaults to keep adjacent hops honest:

- Timeout ladder (shortest inside): DB statement 5s < app request 15s < proxy read 30s < client/LB idle 60s.
- Keepalive ladder (longest inside): app idle > proxy upstream keepalive (Node default `keepAliveTimeout` 5s vs nginx `keepalive_timeout` 75s is a classic intermittent 502).
- Bind apps to `127.0.0.1` or a Unix socket unless the port must be public; publish Docker as `127.0.0.1:PORT:PORT`.
- Concurrency for blocking workers: `min(2×cores+1, (usable_RAM×0.75)÷RSS_per_worker)`, then respect DB `max_connections` across every app.
- Releases live in `releases/<id>/` with a `current` symlink; rollback flips the symlink.

## Depth on demand

| Need | Load |
| --- | --- |
| Workflow, core rules, defaults, stack choices, security | `references/domain.md` |
| Failure signatures, output gates, config knobs, traps | `references/troubleshooting.md` |
| Proxy vs app TLS/header boundary | `references/reverse-proxy.md` |
| Official docs for version-sensitive claims | `references/sources.md` |

## Safety defaults

- Diagnostics are read-only by default.
- Service-affecting actions (`restart`, `stop`/`halt`, `down`, `rm`, `prune`, firewall changes, `-v`) ship with impact, a reload alternative when one exists, and an explicit confirmation step.
- Prefer validate + reload (`nginx -t` / `caddy validate` / `systemd-analyze verify`, then reload) over restart for live traffic.
- Record durable changes before the session ends: deploys, rollbacks, measured capacity, outages and real causes.
- Precedence for any preference value: `<state_root>/config.yaml` → `<workspace>/profile.yaml` → Configuration table defaults in `references/troubleshooting.md`.
