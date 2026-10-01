# Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Hardening SSH from a single session | The edit that breaks sshd also removes your ability to fix it | Second session; fallback proven first (Core rule 1) |
| Moving SSH off port 22 as "security" | Removes untargeted bot noise; stops zero targeted attacks; breaks tooling that assumes 22 | Keys only, no password auth, rate limiting; port change is log hygiene, not safety |
| Provider snapshots treated as backups | Live in the account that can delete them; not restorable elsewhere; billed per disk GB | 3-2-1 with one copy outside the provider account (Core rule 4) |
| "Nobody knows this IP" | Address space is scanned continuously; first auth attempt often arrives within minutes of boot | Default-deny inbound at both layers before the first public service |
| Databases bound to `0.0.0.0` behind a firewall | One container publish or firewall reload and it is public | Bind localhost or private interface, **and** filter |
| Unattended upgrades with no reboot policy | Packages install; running kernel/libs stay old; dashboard stays green | Stated reboot policy + `## Due`; check reboot-required marker |
| Oversizing on day one "to be safe" | Pay premium monthly; never learn the real constraint; grown disk often cannot shrink | Start one step below the guess; watch ~two weeks; step up (Core rule 5) |
| First restore during the incident | Fails on unwritten details: passphrase, DB version, config outside data dir | Timed restore on a scratch box quarterly; gaps go into the runbook |
| Cleaning a compromised server | Trusts binaries an attacker could rewrite | Fresh image + data from before intrusion (Core rule 6) |
| Mail from a fresh VPS address | Port 25 often blocked; recycled IPs may already be listed | Check reputation and PTR before building; use a relay for transactional mail |
| Migrating by changing DNS first | Traffic splits for the old TTL; writes land on both sides | Lower TTL days ahead, cut over, then raise TTL |
| Destroying without teardown | Reserved addresses, volumes, snapshots, load balancers keep billing | Teardown checklist, then delete inventory row with date |
