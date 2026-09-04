---
name: home-server
description: "Design, secure, and operate home servers: Docker services, remote access, backups, upgrades, and incident recovery. Use only for homelab, NAS, self-hosted-service, reverse-proxy, or home-network planning and operations that need a human-authorized change."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🏠"}'
  related-skills: '{"docker":"Applies container runtime and image practices to home-server workloads.","docker-compose":"Covers multi-service Compose definitions used by a home server.","linux":"Provides host administration and diagnostics for the underlying server.","self-host":"Extends home-server planning with self-hosting security and service strategy.","server":"Covers general server deployment and troubleshooting patterns."}'
---

## State location

Use persistent state only when the user asks to save or update home-server context. Before the first state operation, resolve `<state_root>` once:

1. Use an explicit user- or host-configured state path when supplied.
2. Otherwise, choose the first existing directory in this order: `<workspace>/home-server/`, `<workspace>/memory/home-server/`, then `~/home-server/`.
3. If none exists and the user approves saving state, create `<workspace>/home-server/` by default. If the host cannot provide `<workspace>`, ask for a state location instead of guessing from the current working directory.

Use the selected `<state_root>` for the entire invocation. When multiple candidate directories exist, use only the highest-precedence directory and tell the user; keep the other copies unchanged. Read `references/setup.md` before first-time onboarding and `references/memory-template.md` before creating or updating state.

## Operating flow

Use this entry point for a home-server decision or plan. Load only the reference named by the active branch below; routine facts stay in this file.

1. **Discover:** identify the host, critical services, data paths, exposure class (LAN-only, VPN-only, or internet-facing), and current backup/monitoring posture. Load `references/service-catalog.md` when creating or auditing an inventory, and load `references/home-server-domain.md` when a plan needs current source-backed security, container, or recovery guidance.
2. **Plan:** define trust boundaries, a rollback trigger, and the restore path before proposing a deployment or upgrade. Load `references/operations-checklists.md` for routine maintenance or changes.
3. **Apply with authority:** explain proposed files, service changes, external traffic, and state writes; obtain explicit user authorization before deploying, changing router exposure, or creating persistent files.
4. **Verify and record:** confirm health, disk capacity, certificate status, and backup freshness after a change. For an outage or recovery, load `references/incident-playbook.md` and preserve a concise timeline in `<state_root>/incidents.md` only with approval.

## State model

When persistent state is approved, use only the selected root:

```text
<state_root>/
├── memory.md          # Context, preferences, and open risks; required when state is enabled
├── services.md        # Service inventory and ownership; create when inventory is needed
├── backup-status.md   # Backup coverage and restore evidence; create when backups are reviewed
└── incidents.md       # Failure timeline and recovery notes; create during or after an incident
```

Keep state to reusable operational context. Represent secrets, raw `.env` contents, and private keys only by sanitized references or placeholders.

## Core rules

### Define trust boundaries first

Classify each service as LAN-only, VPN-only, or internet-facing before deployment. Keep administrative interfaces and databases behind local-network or VPN boundaries; place only intended public application routes behind an authenticated, maintained reverse proxy.

### Design for recovery

Identify every stateful data path before changing images or configuration. Verify a usable backup and a rollback path before upgrades; exercise restore procedures on a schedule rather than treating a successful backup job as restoration evidence.

### Prefer reproducible operations

Use declarative Compose files and explicit image versions or digests when the service supports them. Keep runtime variables documented as sanitized names and locations so a rebuild can be reproduced without copying secret values into skill state.

### Secure the host and observe it

Use key-based SSH, minimal intended network exposure, regular security updates, least-privilege service accounts, and restrictive file permissions. Track health checks, disk usage, certificate expiry, and backup freshness; investigate a missing or stale signal as an operational incident.

## Common traps

- Defining services before their data and restore paths can turn the first migration into data loss.
- Publishing application, database, and administration ports directly at the router expands the attack surface and complicates incident response.
- Mutable image tags make rollback and incident comparison unreliable.
- A backup without a tested restore path has unknown recovery value.
- A flat Docker network can allow unintended lateral access; segment services according to their communication needs.

## Privacy and authority

This skill may help plan and inspect a system. It does not open ports, deploy services, alter router settings, create persistent state, or send external requests unless the user explicitly authorizes that specific operation.

Network-facing integrations can disclose DNS or dynamic-DNS updates to the chosen provider, and optional monitoring can send telemetry to its configured destination. Service configuration, sanitized logs, backup manifests, and incident notes remain in `<state_root>/` unless the user authorizes another destination.
