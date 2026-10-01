---
name: vps
description: >
  Manage rented virtual private servers end to end: provider and plan choice,
  first-boot hardening, dual-layer firewalls, snapshots versus real backups,
  lockout recovery, resizes, IP moves, migrations, and teardown. Use when a box
  is unreachable, SSH refuses, a firewall rule is ignored, the disk filled, an
  abuse notice arrives, outbound mail fails, or the bill jumped on egress or
  IPv4. Not for Linux internals (`linux`), container runtime (`docker`),
  reverse-proxy/TLS (`nginx`), DNS design (`dns`), or managed platforms with no
  server to administer (`hosting`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🖧","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"linux":"Host internals, systemd, disks, and boot once you are on the box.","docker":"Container runtime, images, and Compose on the server.","nginx":"Reverse proxy, vhosts, and TLS in front of services.","dns":"Record design and TTL for migration cutovers.","monitoring":"Metrics, logs, and alerts once one box becomes several.","backups":"Offsite backup architecture beyond provider snapshots.","firewall":"Host and cloud packet-filter design around the instance.","hosting":"What to run on the box once the rented machine side is settled."}'
---

## When to load

Load for **rented-machine** work: provider/plan choice, first hour, SSH lockout, provider vs host firewall, snapshots/restores, resize, floating IP, abuse/suspension, egress bill shock, provider migration, teardown.

Do **not** load as the primary skill for OS internals (`linux`), containers (`docker`), reverse proxy/TLS (`nginx`), DNS records (`dns`), pure backup architecture (`backups`), or managed PaaS with no VM (`hosting`).

## State location

Optional inventory, VPS memory, and runbooks may live under `<workspace>/vps/`, `<workspace>/memory/vps/`, or `~/vps/`. Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/vps/`, `<workspace>/memory/vps/`, `~/vps/`.
3. If none exists and durable state must be created, default to `<workspace>/vps/` only with user consent.
4. When more than one candidate exists, use only the highest-precedence path, report the conflict, and leave other copies unchanged.

Shared inventories (servers, domains, finances, profile) may live beside the skill state root when the host already uses them — for example `<state_root>/../servers/servers.md` or an explicitly configured shared path. Prefer one shared servers inventory for every provider.

Keep private keys, root passwords, provider API tokens, and recovery codes **out of the skill package and out of git**. Store pointers only: `file:~/.ssh/id_ed25519`, `keychain:hetzner-api`, `1password:Infra/root-password`, `env:RESTIC_PASSWORD`.

At session start, read `<state_root>/config.yaml` (declarations) and `<state_root>/memory.md` (observations, `## Boxes`, `## Due`) when they exist. Declarations win over observations. Derive host-specific note paths from `## Boxes` dynamically; do not hard-code a fixed filename list. Before sizing, cost, access, or "what do I have" questions, read the shared servers inventory when present. If nothing exists, work from defaults and say nothing about missing state.

Write durable outcomes before the session ends: host create/rebuild/resize/destroy, port changes, snapshot policy, timed restore, spend numbers, recovery runbooks, cutover plans. Load `references/memory.md` for destinations and formats.

## Routing

Load supporting references only on demand:

- **Config variables and preference areas**: `references/configuration.md`
- **Common traps**: `references/traps.md`
- **Expert disagreements / trade-offs**: `references/experts.md`
- **Credential and storage guardrails**: `references/privacy.md`
- **Depth playbooks (provider, first hour, access, firewall, backups, ops, net, mail, resize, migrate, incidents, costs, hosting)**: `references/playbooks.md`
- **Gate 6 primary sources**: `references/sources.md`

## Core rules

1. **A second way in exists before you change the first one.** Before disabling password login, moving the SSH port, or enabling a firewall: confirm console/rescue or a second key works. Keep the current session open; prove the change from a *new* session; only then close the first.
2. **The provider account is the real root.** Whoever holds that login can rebuild, mount rescue, and delete snapshots. 2FA the provider login; scope and rotate API tokens; keep recovery codes offline.
3. **Two firewalls, different vantage points.** Provider firewall filters before the guest and survives a broken host. Host firewall (nftables/ufw/firewalld) is what container runtimes walk around. Default-deny inbound at both. `ufw deny 5432` does **not** close a Docker-published 5432 — publish to `127.0.0.1` and terminate publicly at a reverse proxy.
4. **A same-account snapshot is not a backup.** 3-2-1 with one copy restorable if the provider account is gone. Time a real restore on a cadence (`## Due`).
5. **Size from the binding constraint; treat disk as one-way.** RAM dominates most web workloads, not vCPU. CPU/RAM resizes are often reversible; **disk growth usually is not**. Start one step below the guess.
6. **After unknown root, rebuild from a fresh image.** Copy data out, not binaries or configs. Cleaning a compromised box leaves integrity as a guess.
7. **The build lives in a file.** Cloud-init or one provisioning script with the project. If recreate takes more than ~30 minutes unrehearsed, the outage length is that rebuild.
8. **Every price names provider and currency.** Specs vary ~2–4× across hosts once egress and IPv4 are counted. While `provider` is unset, state which console and plan names you assume before quoting (statement, not a questionnaire).

## The first hour

Order is load-bearing: three steps lock you out if early; two are hard to reverse later.

1. Create with SSH key **injected at creation** (prefer no emailed root password).
2. Confirm console or rescue **before** touching SSH/firewall.
3. Update packages on a stock image.
4. Non-root sudo admin + key; log in as that user in a second session.
5. Hostname, timezone (UTC unless declared), locale.
6. Swap or zram on anything under ~4 GB RAM.
7. Host firewall: allow SSH first, then default-deny inbound.
8. Provider firewall: same policy one layer out.
9. Disable password auth and root SSH from the second session with the first still open.
10. Unattended security updates **with** a stated reboot policy.
11. Backups configured and one restore tested before real data.
12. Write the host row, VPS-only attributes, and provisioning script location.

## Quick reference

| Situation | Play | Depth |
|---|---|---|
| Provider and size | Price the binding constraint (usually RAM); compare egress + IPv4, not vCPU count | `references/playbooks.md` |
| Provider quirk / Contabo-class bulk | Match workload risk to support and noisy-neighbor profile | `references/playbooks.md` |
| Fresh box | First Hour order above | this file |
| SSH refused / timeout / auth | Classify layer, then console vs network vs key | `references/playbooks.md` |
| Fully locked out | Console → rescue → mount/chroot; read disk before rebuild | `references/playbooks.md` |
| Firewall rule ignored | Provider vs host vs Docker chain | Core rule 3 |
| Abuse / suspension | Assume compromise; isolate; answer inside provider window | `references/playbooks.md` |
| Backups coverage | 3-2-1 + timed restore; snapshots ≠ offsite | Core rule 4 · `backups` |
| Disk/RAM/load pain | Disk → inodes → memory → steal time | `references/playbooks.md` |
| IPv6 / private net / floating IP / PTR | Address plan; what private net does not protect | `references/playbooks.md` |
| Outbound mail rejected | Port 25 policy, PTR/HELO, IP reputation; often use a relay | `references/playbooks.md` |
| Resize or second box | Vertical first; disk is one-way; horizontal for isolation/HA | Core rule 5 |
| Migrate or teardown | Lower TTL early; teardown reserved IP/volume/snapshot/LB | `references/playbooks.md` |
| Bill shock | Egress, IPv4, snapshots, stopped disks, orphan hosts | `references/playbooks.md` |

## Failure signatures

Shape names the layer: refused = something answered; timeout = nothing did; auth = right daemon said no.

| Signature | Likely cause | First move |
|---|---|---|
| `Connection refused` on SSH | sshd down or other port | Console: service + listen port |
| `Connection timed out` on SSH | Provider/host firewall or off-net | Provider firewall first |
| `Permission denied (publickey)` | Wrong key/user or open perms | Key 600, `.ssh` 700, auth log |
| Worked yesterday, refuses today | fail2ban or allowlist/IP change | Console: ban list before edits |
| Rule added, port still open | Container published ahead of host FW | Bind `127.0.0.1` or provider filter |
| Ping OK, services dead | Disk full / read-only root | Console: df + inodes |
| Slow, CPU idle | Steal time / noisy neighbor | Sustained steal ≳5%: migrate or dedicated |
| OOM wrong process | No swap; large RSS ≠ culprit | Swap/zram + limits |
| Boot fails after mount | Bad `/etc/fstab` | Rescue; `nofail` on non-root mounts |
| Suspended | Outbound abuse / open relay | Isolate; respond in window |
| Mail rejected / spam folder | Port 25, PTR/HELO, blacklist | Reputation before DNS busywork |
| Bandwidth bill, flat traffic | Backup egress or scraper | Direction + destination first |

## Bill anatomy

Plan price is rarely the whole bill. Ratios are stabler than list prices — verify on the provider page before committing money.

| Line item | Why it bites | Do instead |
|---|---|---|
| Egress overage | Allowances differ by >10× | Compare included transfer **and** overage rate; heavy assets → object storage/CDN |
| Dedicated IPv4 | Often billed attached or not | Count and release; IPv6 + proxy when clients allow |
| Snapshots / backup add-on | Per-GB of disk size; add-on often ~20% of plan | Retention count + prune cadence in `## Due` |
| Stopped servers | Disk + reserved address still bill | Snapshot+destroy, or accept parked cost in inventory |
| Orphan hosts | Forgotten experiments | Every host has `Owner`; unowned → teardown candidate |
| Early annual prepay | Locks you while list prices fall | Right-size, run ~2 months, then commit |

## Provider shortlist

Orientation only. Full caveats in `references/playbooks.md`. **Verify current plans and prices before quoting** (Gate 6).

| Need | Reach for | Because |
|---|---|---|
| Strong RAM/$ in EU | Hetzner | Mainstream price/RAM; large included traffic; EU/US footprint |
| Simple ops, US-centric docs | DigitalOcean | Predictable Droplet model; broad tutorials; managed add-ons |
| Many small regions | Vultr or Linode/Akamai | City latency often beats raw specs |
| Cheap bulk, tolerant work | Contabo-class | Specs/€ high; support/IO weaker — avoid revenue-critical SLAs |
| Already in a big cloud | Lightsail-class fixed VPS | Fixed price inside existing account; watch that cloud's egress |
| EU legal entity / residency | Scaleway, OVHcloud, Hetzner | Contract entity ≠ just datacenter pin |
| Hobby free tier | Always-free ARM tiers | Reclaimable; not for anything you would miss |
| Undecided | Console the user can already open | Practiced recovery path beats a datasheet |

## Output gates

Before a plan, command, or recommendation:

- Monthly cost with **currency and provider** stated (or explicit assumption).
- SSH/firewall/network change → fallback path + second-session proof named.
- Data fate if the box dies tonight → timed restore answer, not hope.
- Irreversible steps (disk growth, rebuild, address release, snapshot delete) flagged **before** the step.
- Destructive commands isolated from read-only copy-paste blocks; confirmation required.
- Inventory updated: servers row, VPS-only facts, change log, runbook/decision artifact when durable.

## Safety

- Read-only by default. Rebuild, destroy, disk growth, address release, snapshot deletion, and firewall enable need explicit confirmation and a named fallback.
- Never write live secrets under `<state_root>/` or into the skill tree.
- Prefer provider documentation live pages over memorized list prices.
