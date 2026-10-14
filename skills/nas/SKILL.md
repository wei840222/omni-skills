---
name: nas
description: >
  Configure, secure, and optimize network-attached storage (Synology, QNAP,
  TrueNAS, Unraid, DIY): 3-2-1 backup vs RAID, remote access without exposing
  admin panels, Docker/app layout on limited NAS hardware, and media library
  structure for Plex/Jellyfin/Immich. Use when planning NAS storage capacity,
  hardening DSM/QTS/TrueNAS, choosing VPN vs QuickConnect, or structuring
  media/docker shares. Prefer `synology` for DSM-only playbooks, `docker` for
  Compose/image mechanics, `storage` for app-level database/object design, and
  `wireguard`/`vpn` when the remaining work is tunnel config.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🗄️"}'
  related-skills: '{"synology":"DSM-specific packages, Hyper Backup, and Container Manager once the box is Synology-only.","docker":"Dockerfile, Compose, publish, and container limits when the NAS is mainly a Docker host.","storage":"Application database/object/CDN storage design beyond NAS shares.","wireguard":"WireGuard peer and ListenPort details after VPN is chosen for remote access.","vpn":"VPN client/provider and kill-switch expectations outside NAS-hosted access.","security-best-practices":"Broader secure-by-default review beyond NAS admin hardening.","vps":"Rented-server lifecycle when the storage box is a VPS rather than appliance NAS.","network":"Generic reachability, DNS, and routing when packet path is not NAS-specific.","linux":"Host sysctl, filesystems, and distribution tools under DIY/TrueNAS SCALE Linux.","backups":"Generic backup policy language when the conversation is not NAS-appliance centered."}'
---

# NAS

Plan and harden **network-attached storage** for home lab and small office:
capacity math, backup that is not RAID, remote access without public admin
ports, Docker on constrained hardware, and media/photo library layout.

This skill is **stateless** for one-shot advice. It does not store credentials,
serial numbers, or live share inventories in the package.

## When to use

- Choosing or sizing Synology / QNAP / TrueNAS / Unraid / DIY NAS hardware
- RAID vs backup, 3-2-1 off-site copies, restore drills
- Remote access: Tailscale / WireGuard / tunnel vs QuickConnect vs port forward
- Docker/apps on NAS: arch limits, volume maps, memory caps
- Plex/Jellyfin/Immich folder layout and transcode expectations

Prefer `synology` when every step is DSM UI/package specific.
Prefer `docker` when the problem is Compose, image pin, or publish mechanics.
Prefer `storage` for application database/object architecture.
Prefer `wireguard` / `vpn` once only the tunnel remains.

## Safety order (always)

1. Identify model, OS/DSM/QTS version, filesystem, and whether the box is
   production, lab, or backup-only before destructive storage changes.
2. Confirm a recent **tested** backup (or accept explicit data-loss risk) before
   volume migration, RAID rebuild experiments, or mass permission rewrites.
3. Keep admin UIs off the public internet; prefer VPN or authenticated tunnel.
4. Never store NAS passwords, OTP seeds, QuickConnect secrets, or API tokens in
   skill files or chat logs meant for reuse.
5. Treat ARM vs x86_64 as a hard Docker compatibility gate before recommending
   images.

## Quick workflow

1. Lock platform (vendor/OS), capacity goal, workloads (file share / media /
   containers / backup target), and remote-access requirement.
2. Separate **redundancy** (RAID/mirrors) from **backup** (independent copies).
3. Load the smallest reference for the task; do not dump every table into the
   first reply.
4. Give ordered next actions with failure modes (wrong protocol, public DSM,
   untested backup, ARM image mismatch).
5. Hand off to `synology`, `docker`, or `wireguard` when the remaining work is
   vendor- or tool-specific.

## Routing

| Need | File |
| --- | --- |
| Critical domain rules (RAID, 3-2-1, exposure) | `references/domain.md` |
| Backup strategy and restore drills | `references/backup.md` |
| Remote access and hardening checklist | `references/security.md` |
| Docker/apps and architecture limits | `references/apps.md` |
| Media/photo library layout | `references/media.md` |
| Verified source URLs (Gate 6) | `references/sources.md` |

## Core rules (summary)

1. RAID/mirrors give hardware redundancy; backup needs separate copies and
   restore tests.
2. 3-2-1 is the minimum backup posture for irreplaceable data.
3. SMB for Windows/macOS clients, NFS for Linux; enable only needed protocols.
4. Expose zero NAS admin ports to the public internet.
5. Test restores quarterly; untested backups are unverified.
6. Replace default `admin` with named admin accounts and 2FA where available.
7. UPS with clean shutdown signaling is mandatory for write-heavy pools.
8. Snapshots help accidental delete on the same failure domain; they are not
   off-site disaster recovery.
9. Quote **usable** capacity after RAID, reserved space, and filesystem overhead.
10. Verify CPU arch before promising Docker images on J-series / low-end ARM.

Load `references/domain.md` when any of these rules drive the recommendation.
