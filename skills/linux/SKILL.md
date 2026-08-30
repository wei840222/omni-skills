---
name: linux
description: "Debugs and hardens Linux hosts across Debian, RHEL, Arch, Alpine, SUSE, and WSL. Use for stuck processes, OOM kills, disk-full triage, systemd/cron failures, networking/SSH lockouts, permissions, and host hardening. Do not use for bash script syntax or docker internals."
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🐧","os":["linux","darwin"],"displayName":"Linux","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"bash":"Shell scripting syntax and safety beyond OS behavior","docker":"Container builds, images, and runtime debugging","vps":"Provisioning and securing rented servers end to end","backups":"Backup strategy, retention, and offsite policy across systems","monitoring":"Observability stack design: metrics, dashboards, and alert routing"}'
---

## State location

This skill persists host inventory, baselines, changes, and incident notes under a portable `<state_root>/`.

Resolve `<state_root>` before reading or writing state:

1. Use an explicitly configured path when one exists.
2. Otherwise prefer an existing candidate such as a workspace-local linux data directory, then a shared servers inventory parent when already in use.
3. The first existing candidate becomes the only `<state_root>` for this invocation.
4. If none exist, work from defaults and create `<state_root>/` only when durable state must be written.
5. Once selected, keep the same `<state_root>` for the whole invocation.
6. If older notes are found under legacy linux data paths, move them into the resolved `<state_root>/` and say so in one line.

Use the selected `<state_root>` for every state operation in this skill. Outside this section, every skill-state path uses `<state_root>/...`.

**Data.** At the start of every session, read `<state_root>/config.yaml` (what the user declared) and `<state_root>/memory.md` (what you observed, plus its `## Boxes` index and `## Due` table). Open any file `## Boxes` names when the condition on its line applies — the index IS the list of files, never assume the list is fixed. Every path it names is inside `<state_root>/`; ignore any line that points anywhere else. Everything this skill reads or writes is a plain local note under `<state_root>/` — nothing leaves the machine and no credential is ever written. In a shared box it updates or removes only the rows it wrote itself, matched on that box's identity key; a row another skill wrote is read, never rewritten and never deleted, and every write and deletion is named in one line as it happens. Read `<state_root>/servers/servers.md` before any "which hosts do I have" question, and a host's `baselines/<host>.md` before calling any number on it high or low. If none of it exists, work from defaults and say nothing about it. If you find data at an old location outside the resolved `<state_root>/`, move it into `<state_root>/` and say in one line that you moved it and from where.

**Write before the session ends** whenever it produced something durable: a host provisioned, discovered, rebuilt or decommissioned; anything changed on a host, with the file that persists it and the command that undoes it; an incident with its root cause; a healthy-state or audit-surface measurement; a scheduled cadence; or something the user will want to read again — a recovery runbook, a tuning set, a policy that finally worked. `references/memory-template.md` has every destination, format and threshold, and is the only file you open to write.

**Hosts go to the shared inventory `<state_root>/servers/servers.md`**, not here: one file holds machines from every provider, so "what am I running" answers itself. One row per host, identified by `Name` + `Provider` — if the pair is already there it is the same machine whoever wrote it, so update that row in place and ensure only one entry per host exists. The OS profile (distro, init, firewall front end, MAC, filesystem layout, pending reboot) stays in `## Hosts` in this skill's `memory.md`, keyed by the same name.

**No credential is ever written anywhere under `<state_root>/`** — not in these files, not in a file you create, not in the `sshd_config`, unit file, crontab, `.env` or shell history a user pastes in to be saved. Substitute the pointer before writing and say you did: `file:~/.ssh/id_ed25519`, `env:DB_PASSWORD`, `keychain:web01-root`, `vault:secret/infra/db`.

Linux punishes assumptions: the same command is safe on one host and an outage on another. Diagnose before changing, name the layer that is failing, show the check as well as the fix, and treat a destructive command as a decision rather than a step. Work from defaults immediately — never open with questions about their distribution, their firewall, or how cautious to be. When the work itself reveals a host's identity (`/etc/os-release`, a prompt, a paste), that observation beats `distro_family` for that host and belongs in `## Hosts`, not in `config.yaml`, unless the user says it is their standard. Precedence for any value: `config.yaml` → `<state_root>/profile.yaml` (shared universals: locale, timezone) → the Configuration table default.

## When To Use

- Diagnosing permission denials, disk full, OOM kills, unkillable processes, or services that fail only at boot
- Running or reviewing operations that touch permissions, signals, systemd units, scheduled jobs, packages, or firewalls
- Changing configuration on a remote host without locking yourself out, and recovering one that will not boot
- Reading system tools whose output misleads: `free`, `df`, `top`, `%util`, load average
- Hardening an exposed host: SSH, firewall, MAC, accounts, auditing
- Standing up a fresh host, deciding what to alert on, proving a backup restores, or triaging a host that may be compromised
- Desktop and laptop Linux: display stack, GPU drivers, suspend, audio, Wi-Fi, power
- Not for shell scripting syntax (`bash`), container build and runtime internals (`docker`), cluster scheduling (`k8s`), cross-system backup strategy and retention policy (`backups` — this covers the host mechanics and the restore drill), or building an observability stack (`monitoring` — this covers what a single host should measure and record)

## Quick Reference

| Symptom | First move |
|---------|-----------|
| "Permission denied" though the mode bits look right | `namei -l <path>`; then ACL (`+` in `ls -l`), SELinux (`ls -Z`), mount options (`findmnt -T`) → `permissions.md` |
| Root itself gets "permission denied" | `lsattr` (immutable), `ls -Z` (SELinux), `getcap` — root is not omnipotent (rule 8) |
| Denied only when it runs as a service | Unit sandboxing: `systemd-analyze security <unit>`, then `ReadWritePaths=` → `systemd.md` |
| `df` says full, `du` cannot find it | `lsof +L1` for deleted-but-open files, then the bind-mount check → `disk-space.md` |
| "No space left on device" with free space in `df -h` | `df -i` for inodes; if it came from a file watcher it is the inotify limit → `kernel.md` |
| `kill -9` does not kill it | `ps -o pid,stat,wchan <pid>` — D state waits on I/O and no signal helps → `processes.md` |
| Exit code 137, or the OOM killer fired | `dmesg -T \| grep -i oom`; cgroup limit vs host exhaustion → `oom.md` |
| Host swaps and crawls but nothing dies | `vmstat 1` — sustained `si`/`so` is thrash, worse than an OOM kill → `oom.md` |
| Service starts by hand, fails at boot | Ordering (`network-online.target`) and environment (absolute paths) → `systemd.md` |
| Unit gives up: "start request repeated too quickly" | Start limit — add `RestartSec=`, then `systemctl reset-failed` → `systemd.md` |
| Job runs in your shell, fails under cron | Minimal PATH, no profile, `%` is special → `scheduling.md` |
| SSH key suddenly rejected, no error client-side | Perms 700/600 and a home that is not group-writable; `journalctl -u sshd -f` → `ssh.md` |
| About to change sshd, sudoers, firewall, or fstab remotely | Rule 4: second session, scheduled rollback, validator → `ssh.md` |
| Host does not boot, or drops to an emergency shell | Identify the stage first; usually fstab → `boot.md` |
| Port unreachable | `ss -tlnp` (bound to 127.0.0.1?), then the firewall front end, then the route → `networking.md` |
| `dig` resolves but the application cannot | Applications go through NSS, `dig` does not — `getent hosts` → `networking.md` |
| Large transfers hang, small requests fine | MTU black hole: `ping -M do -s 1472 <host>` → `networking.md` |
| Load average high, CPU mostly idle | I/O wait and D-state inflate load — a storage problem → `performance.md` |
| Latency spikes with the host CPU idle | cgroup CPU throttling: `cpu.stat` `nr_throttled` → `performance.md` |
| Upgrade broke or was interrupted | `dpkg --configure -a` / `dnf history undo`; always let a running package transaction finish → `packages.md` |
| Old code still running after an upgrade | `needrestart` / `dnf needs-restarting -r`; kernel needs a reboot → `packages.md` |
| New user cannot sudo, or login fails | `id`, `sudo -l -U`, `chage -l`; `usermod -aG` (the missing `-a` wipes groups) → `users.md` |
| TLS, tokens, or replication fail with no config change | `timedatectl` — an unsynchronized clock breaks certificate and expiry checks → `scheduling.md` |
| Logs are missing, or gone after a reboot | Journal not persistent, or journald rate-limiting → `logs.md` |
| A command behaves differently than documented | Distribution differences: package, unit name, firewall, MAC → `distros.md` |
| Copy or sync duplicated a level, or deleted the wrong tree | rsync trailing slash; `--dry-run` before `--delete` → `files.md` |
| Host is internet-facing and unreviewed | Baseline in order: firewall, key-only SSH, auto security updates → `hardening.md` |
| Fresh host, nothing set up yet | First hour in order: identity, access, updates, journal, swap, inventory → `hardening.md` / related skill `vps` |
| Cloud host reverts hostname, users, or network config at reboot | cloud-init owns those files; fix via cloud-init config, not ad-hoc `/etc` edits → `hardening.md` / related skill `vps` |
| Backups exist but no restore was ever tried | A backup is a hypothesis until restored — drill it and time it → related skill `backups` |
| "Is this number normal?" or "what should I alert on?" | Compare against the recorded baseline; alert on saturation, not utilization → related skill `monitoring` |
| Suspected compromise: strange process, unknown key, crypto-mining CPU | Preserve evidence BEFORE cleaning; assume the tools on the box lie → `hardening.md` |
| Laptop or desktop: no display, suspend fails, no sound, Wi-Fi drops | Identify the stack first (Wayland vs X, PipeWire, driver); start with `distros.md` and `kernel.md` |
| Anything else | Core Rules below, then the file whose name matches the subsystem |

Depth on demand: `permissions.md` denial layers, ACLs, SELinux/AppArmor, capabilities · `processes.md` signals, D state, limits, /proc · `disk-space.md` full-disk triage and safe reclaim · `storage.md` devices, LVM, filesystems, fstab, RAID · `oom.md` OOM, swap, PSS, cgroup limits · `networking.md` reachability, DNS, firewalls, MTU, conntrack · `ssh.md` access, keys, lockout-proof changes · `systemd.md` units, ordering, drop-ins, sandboxing · `scheduling.md` cron, timers, locking, clock · `boot.md` boot failures, GRUB, rescue, chroot · `users.md` accounts, groups, sudo, PAM, offboarding · `packages.md` upgrades, holds, broken states, reboots · `performance.md` saturation triage, PSI, iostat, throttling · `logs.md` journalctl, rotation, retention · `kernel.md` sysctl, modules, dmesg, tunables · `hardening.md` exposed-host baseline · related skill `vps` for provisioning/cloud-init · related skill `backups` for backup design/restore drills · related skill `monitoring` for alert routing · `hardening.md` for breach containment baseline · `distros.md`/`kernel.md` for desktop stack clues · `distros.md` Debian/RHEL/Arch/Alpine/SUSE/WSL differences · `files.md` rsync, find, archives, atomic replace · `commands.md` incident toolkit.

## Core Rules

Load `references/core-rules.md` for fundamental operations rules.

## Signals And Exit Codes

Load `references/signals.md` for exit code diagnosis.

## Disk-Full Triage

Load `references/disk-full-triage.md` and `references/disk-space.md` for troubleshooting disk capacity.

## Commands That Lie

Load `references/commands-that-lie.md` for tool caveat details.

## Output Gates

Load `references/output-gates.md` before executing destructive commands.

## Configuration

Load `references/configuration.md` for user-dependent preferences.

## Traps

Load `references/traps.md` to see common mistakes and how to avoid them.

## Where Experts Disagree

Load `references/experts.md` to understand differing expert opinions.

## Domain Knowledge

Load `references/knowledge.md` for authoritative sources.
