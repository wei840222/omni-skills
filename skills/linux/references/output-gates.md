# Output Gates

Before running a destructive or remote-risky command — and, for the last two, before ending any session that changed or learned something:

- Variables in destructive paths expanded and echoed first — `rm -rf` targets use `"${VAR:?}"`?
- Fallback session open and a rollback scheduled before touching sshd, sudoers, firewall, fstab, or network config on a remote host?
- SIGTERM sent and waited before any `-9`?
- Persistence step included, or is this change gone at the next reboot?
- Blast radius previewed — `pgrep -af` before `pkill -f`, `find … -print` before `-delete`, `rsync -n` before `--delete`, `lsblk -f` before `mkfs`/`dd`?
- Command matches the host's `distro_family` — package manager, unit name, firewall front end, MAC system?
- Validator run where one exists (`sshd -t`, `visudo -c`, `mount -a`, `nft -c -f`, `systemd-analyze verify`)?
- Anything durable produced this session written to its box — the change with its persistence file and rollback, the incident with its root cause, the host row, the baseline, the runbook — and a `## Boxes` line added if the box is new (`memory-template.md`)?
- Nothing written under `<state_root>/` that authenticates anything: keys, hashes, passphrases and `EnvironmentFile` values replaced by `<kind>:<locator>` pointers, including inside text the user pasted?
