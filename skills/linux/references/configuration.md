# Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| distro_family | debian \| rhel \| arch \| alpine \| suse | debian | Selects package manager, unit names, config paths, firewall front end, and MAC system in every command emitted (→ `distros.md`) |
| init_system | systemd \| openrc \| sysvinit | systemd | Routes service and boot guidance; non-systemd hosts skip `systemd.md` and timers in favour of the distro's init and cron |
| firewall_tool | auto \| ufw \| firewalld \| nftables \| iptables | auto | Which syntax firewall examples use; `auto` derives it from `distro_family` (ufw on debian, firewalld on rhel) |
| privilege_mode | sudo \| root-shell | sudo | Whether emitted commands carry a `sudo` prefix and whether sudo-specific traps (secure_path, sudoers.d naming) are surfaced |
| disk_alert_pct | number (50-95) | 80 | Filesystem usage at which disk triage is raised proactively rather than on request (rule 3) |
| load_alarm_ratio | number (0.5-4) | 1.0 | `load1 / nproc` ratio treated as saturation in capacity judgements (rule 6, `performance.md`) |
| destructive_confirm | bool | true | Whether every destructive command is preceded by its preview or dry-run (rule 9, Output Gates) |
| reboot_policy | allowed \| maintenance-window \| never | maintenance-window | Whether a required reboot is proposed inline, deferred to a window, or reported as a standing requirement (`packages.md`, `kernel.md`) |
| backup_tool | restic \| borg \| rsync \| snapshots \| none | none | Which restore and verification commands related skill `backups` emits; `none` means file-level examples use restic and volume-level examples use the platform's snapshot, stated as an assumption |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied:

- **Tooling**: editor, terminal multiplexer for long remote operations, monitoring stack, whether config management (Ansible, Puppet, Salt) owns `/etc` — affects whether fixes are proposed as commands or as managed configuration
- **Conventions**: where local units, scripts, and logs live; naming of hosts, volumes, and users — affects every path in examples
- **Platform**: cloud provider, bare metal, VM, WSL, container; architecture; filesystem in use; headless server vs desktop, and the display stack on a workstation — affects storage, boot, performance and desktop-stack guidance in `distros.md`/`kernel.md`
- **Safety posture**: dry-run everything vs act directly, change windows, backup or snapshot required before storage and fstab work — affects how much of a change is proposed before anything runs
- **Output format**: one-liners vs explained procedures, command blocks vs prose, how much diagnosis to show alongside the fix
- **Work order**: diagnose-then-fix vs fix-then-explain, and whether a review gate exists before production changes
- **Integrations**: log destination, alerting target, patch tooling, secret store — the choice, never the credentials
- **Restrictions**: compliance regime in force (CIS, STIG), forbidden tools or commands, air-gapped hosts with no package repository access
- **Cadence**: patch window, journal and log vacuum schedule, reboot drill, restore drill, audit-surface diff — every one of them lands as a row in the `## Due` table of `memory.md`
