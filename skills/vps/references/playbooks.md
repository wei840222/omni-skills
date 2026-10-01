# VPS depth playbooks

Procedures condensed from the pre-refactor operational body. Re-check `references/sources.md` before restating provider UI labels, list prices, or product limits.

## Choosing provider and plan

1. Name the binding constraint (usually RAM for web apps; disk for large media; CPU for build/CI).
2. Shortlist by **user latency** and legal entity needs, then compare included transfer + overage + IPv4 fee.
3. Prefer a smaller plan plus a rehearsed rebuild over an oversized idle box.
4. Quote monthly price with provider + currency; if `provider` is unset, state the assumption first.

## Providers (orientation)

| Family | Strength | Watch-outs |
|---|---|---|
| Hetzner Cloud | Strong RAM/€, large included traffic | EU/US-centric; verify current auction/cloud SKUs live |
| DigitalOcean Droplets | Docs and predictable UX | Egress and add-ons add up; verify current rates |
| Vultr / Linode (Akamai) | Many regions | Product renames; open current docs for rescue/console paths |
| Contabo-class bulk | Cheap large specs | Oversubscription, slower support — non-SLA workloads |
| Lightsail-class | Fixed price inside a major cloud | That cloud's egress economics still apply |
| Scaleway / OVHcloud | EU entities and regions | Console and rescue flows differ; read provider docs |

## Provisioning notes

- Inject SSH keys at create time when the API/UI allows it.
- Stock images lag security fixes — patch before exposure.
- Record image name, region, plan, IPv4/IPv6, and provisioning script path in inventory.

## Access and lockout

1. Classify: refused vs timeout vs auth failure.
2. Timeout → provider firewall / routing / powered-off before guest sshd.
3. Refused → guest listen port or sshd down (console).
4. Auth → key, user, or `~/.ssh` permissions; read auth log from console.
5. Full lockout → web/serial console → rescue/recovery image → mount root → fix `sshd_config`/keys → exit rescue deliberately.
6. Read the disk before rebuild when data might still be intact.

## Firewall

- Provider layer: source-restricted SSH if possible; default-deny other inbound.
- Host layer: allow SSH (or admin VPN) first; then enable default-deny.
- Containers: publish to loopback; public entry via reverse proxy only.
- After changes, test from a **second** network path (phone LTE, second host).

## Security / abuse

- Abuse notice or unexpected outbound: take off the public network first if the console allows isolation.
- Treat unknown root as rebuild territory (Core rule 6).
- Respond inside the provider's stated window with what you changed.

## Backups vs snapshots

- Snapshots: fast rollback in-account; not offsite; often billed on disk size.
- Real backup: copy restorable without that provider login (object storage another account, other region/provider, or offline).
- Schedule restore drills; log duration and gaps under `## Due` / restore notes.
- For architecture depth, hand off to skill `backups`.

## Operations (four killers)

Order checks: filesystem full → inode full → OOM/no swap → CPU steal/noisy neighbor. Check reboot-required after unattended upgrades.

## Networking

- Private networks reduce exposure but are not a substitute for auth.
- Floating/reserved IPs often bill after destroy — release on teardown.
- PTR/rDNS must match outbound SMTP identity when self-hosting mail (usually prefer a relay).

## Email

- Expect port 25 blocks on many VPS products.
- Check IP reputation before spending time on DNS cosmetics.
- Transactional mail → reputable relay; keep PTR/SPF/DKIM coherent if you must self-send.

## Resizing

- CPU/RAM up: usually reboot-sized downtime.
- Disk up: often irreversible — treat as permanent bill floor.
- Horizontal split when ownership or SLA diverges, not only when CPU is high.

## Migration and teardown

1. Lower DNS TTL days ahead when names point at the box.
2. Copy data; verify checksums/app health on the target.
3. Cut over; watch error rates; raise TTL after stability.
4. Teardown list: instance, reserved/floating IP, volumes, snapshots, load balancers, firewall leftovers still billing.
5. Delete inventory row with destroy date.

## Incidents

Split provider status and path from guest failure before deep guest debugging. Use console when SSH path is the incident.

## Costs

Re-read bill line items in `SKILL.md` bill anatomy. Orphan hosts and leftover reserved IPs are the common silent leaks.

## Hosting layout

- One box vs many: see `references/experts.md`.
- Panel vs bare: automation intent decides.
- What runs on the box after the rented-machine side is settled may belong in skill `hosting`.
