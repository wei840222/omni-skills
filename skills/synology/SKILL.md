---
name: synology
description: >
  Plan, harden, and recover Synology NAS and DSM setups: storage and SHR layout,
  Hyper Backup / Snapshot Replication discipline, QuickConnect vs VPN exposure,
  package health, and Container Manager workflows. Use when the ask is
  DSM-specific (model/package gates, shared folders, Hyper Backup restore order,
  Drive/Photos, Container Manager on Synology). Prefer `nas` for multi-vendor
  NAS design, `backups` for vendor-neutral 3-2-1 policy, `docker` for Compose
  mechanics, `home-server`/`self-host` for broader homelab strategy, and
  `wireguard` when only the tunnel remains.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🗄️"}'
  related-skills: '{"nas":"Multi-vendor NAS capacity, RAID-vs-backup, and media layout when the box is not DSM-only.","backups":"Vendor-neutral backup architecture, immutability, and restore drills beyond Hyper Backup.","self-host":"Service ownership and long-term ops once Synology is only the host.","docker":"Dockerfile/Compose debugging when Container Manager is mainly a Docker host.","home-server":"Full homelab design covering network, remote access, and household services.","wireguard":"WireGuard peer and AllowedIPs details after VPN is chosen over QuickConnect."}'
---

## When to Use

Use this skill when the user needs **Synology-specific** execution: DSM planning, volume/SHR layout, shared folders, Hyper Backup, Snapshot Replication, QuickConnect, Synology Drive/Photos, package triage, Container Manager on Synology, migrations, upgrades, or DSM incident recovery.

Prefer sibling skills when the ask is broader or narrower:

- `nas` — multi-vendor NAS / TrueNAS / QNAP / Unraid design
- `backups` — retention, immutability, and restore program design beyond one appliance
- `docker` — Compose, image, publish, and daemon mechanics
- `home-server` / `self-host` — whole-homelab or service-strategy planning
- `wireguard` — tunnel config once remote access choice is VPN

## State location

Optional continuity notes may live under `<workspace>/synology/`, `<workspace>/memory/synology/`, or `~/synology/`. Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in that order.
3. If none exists and durable state must be created, default to `<workspace>/synology/` only with user consent.
4. When more than one candidate exists, use only the highest-precedence path, report the conflict, and leave other copies unchanged.
5. Do not invent `<workspace>` from the shell cwd.

If `<state_root>/` does not exist, read `references/setup.md`, explain planned local notes in plain language, and ask before creating files. See `assets/memory-template.md` for structure.

```text
<state_root>/
|- memory.md        # Model, DSM version, workloads, and guardrails
|- inventory.md     # Volumes, shares, packages, and exposure notes
|- services.md      # Container Manager, Drive, Photos, backup, and app notes
`- incidents.md     # Failures, recoveries, and postmortems worth reusing
```

## Architecture

This skill works statelessly for one-off Synology questions. Load only the smallest reference that changes the decision in front of you.

| Topic | File | Use it for |
|-------|------|------------|
| Setup flow and saved defaults | `references/setup.md` | Activate safely and decide whether continuity is useful |
| Memory schema and status values | `assets/memory-template.md` | Create durable notes without storing secrets |
| Volumes, Btrfs, SHR, and shared folders | `references/storage-and-shares.md` | Capacity, snapshots, permissions, migration planning |
| Hyper Backup, snapshots, rsync, restore order | `references/backup-and-recovery.md` | Real backup strategy and recovery sequencing |
| QuickConnect, VPN, reverse proxy, exposure | `references/remote-access-and-networking.md` | Remote access and network change safety |
| Packages, Drive, Photos, Container Manager | `references/packages-and-containers.md` | App selection, package triage, container caveats |
| Incident triage and evidence collection | `references/troubleshooting.md` | Fast diagnosis before risky changes |
| Official source map | `references/sources.md` | Live Synology / Agent Skills URLs for refresh |

## Requirements

- No credentials required for planning, review, or architecture work
- Live DSM changes may require admin access to the web UI and optional SSH
- Confirm whether the target NAS is production, homelab, or backup-only before changing anything
- Require explicit confirmation before deletions, package removals, share permission rewrites, exposure changes, restore operations, or storage migrations

## Data Storage

Store only context that improves later Synology work:

- exact model, DSM version, and which packages matter
- filesystem and volume facts that change recommendations
- approved backup destinations, restore priorities, and exposure boundaries
- recurring failures, confirmed fixes, and package-specific caveats

Do not store passwords, QuickConnect credentials, OTP codes, serial numbers, or copied support bundles with secrets.

## Core Rules

### 1. Identify the Box Before Giving Synology Advice
- Lock the exact model, DSM version, volume layout, filesystem, and installed packages before promising features or commands.
- Synology guidance changes materially with model family, DSM version, and whether the workload depends on Btrfs-only features.
- If that context is missing, ask for it before treating every NAS as interchangeable.

### 2. Separate Read-Only Diagnosis From Writes
- Start with inventory: storage health, free space, package status, backup state, and remote exposure.
- State whether the next step is read-only, additive, mutating, or destructive.
- Prefer a read-only inventory before deleting data, changing shares, or reinstalling packages when the complaint is only "it looks slow."

### 3. Treat SHR and RAID as Availability, Not Backup
- Disk redundancy protects against some hardware failures, not ransomware, accidental deletion, bad sync, or site loss.
- Every serious plan needs restore-tested backup layers such as Hyper Backup, Snapshot Replication, rsync, or an external copy.
- If restore testing is missing, say the backup posture is incomplete.

### 4. Internet Exposure Is Opt-In
- Prefer VPN or QuickConnect for remote admin convenience over raw DSM port forwarding.
- Reverse proxy and public access are explicit design choices that need MFA, update discipline, and blast-radius awareness.
- Default to private access methods rather than exposing DSM, SSH, or package dashboards to the public internet.

### 5. Verify Feature Gates Before Recommending Synology Features
- Snapshot Replication, immutable backup patterns, and some data-protection workflows depend on model support, filesystem, package availability, and licensing.
- Container Manager guidance depends on compatible models and package availability on the target DSM build.
- When a recommendation depends on support status, verify it before presenting it as available (Download Center + package notes).

### 6. Protect Production State Before Upgrades or Rebuilds
- Before DSM upgrades, package reinstalls, share moves, or container rewrites, confirm the recovery path and the configuration that must survive.
- Export or record key settings, confirm backup freshness, and define rollback before touching live services.
- If the user cannot explain how to undo the change, the plan is not ready.

### 7. End With an Execution Record
- Finish non-trivial work with a short record: target NAS, read-only findings, chosen action, validation steps, rollback path, and open risks.
- Save only that durable summary under `<state_root>/` if the user wants continuity.

## Safety Checklist

Before high-impact Synology changes:

- confirm the exact NAS, volume, share, and package being changed
- state whether the step is read-only, additive, mutating, or destructive
- confirm backup freshness and whether restore has ever been tested
- capture current screenshots, package versions, or config exports before upgrades or reinstalls
- ask for explicit confirmation before delete, downgrade, restore, remote exposure, or major permission changes

## Common Traps

- Treating Synology like generic Ubuntu with disks attached → wrong service assumptions and risky cleanup advice
- Confusing SHR or RAID with backup → false confidence until deletion, corruption, or ransomware happens
- Promising snapshots or replication without confirming filesystem and package support → recovery plan fails when it matters
- Opening DSM or SSH to the internet "just for now" → turns convenience into attack surface
- Recommending package reinstalls before collecting evidence → destroys the only clues needed to fix the issue safely
- Blaming performance on CPU alone → full volumes, indexing, broken thumbnails, parity checks, or bad remote sync often matter more
- Restoring everything at once after an incident → increases downtime and can overwrite evidence or good data

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://www.synology.com | Page requests and product references only unless the user asks for account or package actions | Verify current DSM, packages, compatibility, and official guidance |
| https://kb.synology.com | Page requests and query text only | Confirm current product behavior and troubleshooting steps |
| https://account.synology.com | Browser session data only when the user explicitly performs account-linked tasks | Synology account, package, and service operations approved by the user |
| https://quickconnect.to | QuickConnect identifiers and connection metadata only when the user explicitly tests remote access | Remote access routing and connectivity checks |

No other data should be sent externally unless the user explicitly approves third-party backup, VPN, DNS, or monitoring services.

## Security & Privacy

Data that may leave your machine:

- documentation lookups against Synology-owned sites
- account and session traffic only when the user explicitly performs Synology account or remote-access actions
- QuickConnect identifiers and connection metadata only when remote access is actively configured or tested

Data that stays local:

- model, package, backup, and recovery notes under `<state_root>/`
- screenshots, exports, or runbooks the user chooses to keep locally

This skill does NOT:

- ask the user to paste DSM passwords, OTP codes, or private keys into chat
- claim SHR, RAID, or sync are backups when they are not
- expose DSM or SSH publicly by default
- promise package, filesystem, or model features without verification when support matters

## Trust

This skill depends on Synology-owned documentation, account surfaces, and remote-access services when the user explicitly uses them. Only install and use it if you trust Synology with the approved operations and related metadata.

## Scope

This skill ONLY:

- plans and executes Synology DSM and NAS workflows with explicit safety gates
- covers storage, backup, remote access, package health, and Container Manager decisions
- keeps lightweight local memory under `<state_root>/` when the user wants continuity
- emphasizes restore-first thinking for incidents and migrations

This skill NEVER:

- pretends all Synology models and DSM builds support the same features
- treats redundancy as backup
- runs destructive storage or exposure changes without explicit confirmation
- replaces specialized camera automation, enterprise SAN design, or off-platform Kubernetes guidance
