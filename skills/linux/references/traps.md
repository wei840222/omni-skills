# Traps

| Trap | Why it fails | Do instead |
|------|-------------|------------|
| `sudo echo x > /etc/file` | The redirect runs in YOUR shell before sudo starts | `echo x \| sudo tee /etc/file` |
| Editing sudoers or fstab bare | One typo = no sudo at all, or an unbootable host | `visudo`; edit fstab then `mount -a` to test before rebooting |
| Fixing web permissions with `chmod -R 777` | Masks the real cause (ACL mask, SELinux, wrong owner) and makes every file writable by any local process | Diagnose: `namei -l`, `getfacl`, `ls -Z` |
| Testing a cron job in your login shell | Your shell has PATH and environment that cron lacks — it proves nothing | `env -i /bin/sh -c 'cmd'` |
| Restarting a unit you edited by hand without `daemon-reload` | systemd runs the cached definition; you debug a file the system is not using | `systemctl daemon-reload`, or use `systemctl edit` |
| `usermod -G docker alice` | Without `-a` it REPLACES every supplementary group, including sudo | `usermod -aG`, and diff `id alice` before and after |
| `passwd -l alice` as offboarding | Locks the password only; her SSH key still logs in | `usermod --expiredate 1`, then remove her authorized_keys |
| `iptables -F` to "start clean" on a remote host | With a DROP default policy you flush your own access | Set policies to ACCEPT first, or schedule a rollback (rule 4) |
| `setenforce 0` to fix a denial | Hides the label bug and comes back at reboot | `restorecon`, a boolean, or `semanage fcontext` (→ `permissions.md`) |
| Killing a stuck `dpkg`/`dnf` to release the lock | Leaves packages half-configured — minutes of waiting become hours of repair | Find the holder with `fuser -v /var/lib/dpkg/lock-frontend` and wait |
| Storing state in `/tmp` | Cleared at reboot, and often tmpfs, so it consumes RAM | `/var/tmp` for temp data that must survive a reboot |
| `dd` or `mkfs` on a device name from memory | `sda` vs `sdb` is one keystroke, and device names reorder across boots | `lsblk -f` immediately before; address disks by UUID or `/dev/disk/by-id` |
| Counting a snapshot as a backup | It lives on the same storage as the origin, and an LVM snapshot invalidates itself the moment its allocated space fills | Layer it: snapshot for the five-minute mistake, an offsite copy for the disaster, and a timed restore drill (→ related skill `backups`) |
| Editing the hostname or `/etc/netplan/50-cloud-init.yaml` on a cloud image | cloud-init rewrites those files at boot; the change reverts and nothing explains why | Set it in cloud-init's config or disable that module (→ provisioning notes in `hardening.md` / related skill `vps`) |
| Cleaning a compromised host instead of rebuilding it | Removing the malware leaves the access, and the tools you checked with are the ones an attacker replaces first | Preserve evidence, contain at the network layer, rebuild from a known-good image, rotate everything the host could read (→ containment notes in `hardening.md`) |
| Alerting on CPU utilization | A batch host at 100% is working correctly; a latency-sensitive service at 30% can already be failing | Alert on saturation (PSI, queue depth, `load1/nproc`) and on symptoms, always with a duration (→ related skill `monitoring`) |
