# VPS sources

Checked 2026-10-01. Re-open the live page before restating UI labels, list prices, regional SKUs, or product limits. Absolute prices are intentionally not pinned in the skill body.

## Agent Skills format

- **Agent Skills specification** — normative skill format.
  - https://agentskills.io/specification
- **Document index (llms.txt)** — entry map for the spec set.
  - https://agentskills.io/llms.txt
- **skills-ref validator** — reference validation tooling.
  - https://github.com/agentskills/agentskills/tree/main/skills-ref

## Provider documentation (compute, SSH, firewall, snapshots, rescue)

- **Hetzner Cloud — creating a server** — create flow and key injection orientation.
  - https://docs.hetzner.com/cloud/servers/getting-started/creating-a-server/
- **Hetzner Cloud — firewalls** — provider-layer filtering model.
  - https://docs.hetzner.com/cloud/firewalls/overview/
- **Hetzner Cloud — snapshots** — in-account image/rollback semantics.
  - https://docs.hetzner.com/cloud/servers/backups-snapshots/overview/
- **DigitalOcean — add SSH keys** — key at create / account key patterns.
  - https://docs.digitalocean.com/products/droplets/how-to/add-ssh-keys/
- **DigitalOcean — Cloud Firewalls** — provider firewall product.
  - https://docs.digitalocean.com/products/networking/firewalls/
- **DigitalOcean — snapshots** — Droplet snapshot behavior and billing cues.
  - https://docs.digitalocean.com/products/snapshots/
- **Akamai Linode — rescue and rebuild** — rescue/rebuild orientation (docs host may redirect).
  - https://techdocs.akamai.com/cloud-computing/docs/rescue-and-rebuild
- **Vultr docs home** — console, firewall, and instance topics (verify deep links live; paths change).
  - https://docs.vultr.com/

## Host SSH reference

- **sshd_config(5) (Debian manpages)** — authoritative daemon settings for password/root login and listen address.
  - https://manpages.debian.org/bookworm/openssh-server/sshd_config.5.en.html

## Backup principle cross-check

- **3-2-1 backup rule (industry primer)** — offsite/independent-copy framing used with Core rule 4; pair with skill `backups` for architecture depth.
  - https://www.backblaze.com/blog/the-3-2-1-backup-strategy/

## What this skill does not treat as live measurement

Example budget default `20`, steal-time ~5% heuristic, swap-under-4 GB guidance, and keepalive-style operational numbers are teaching defaults — not universal SLOs. Provider list prices, IPv4 surcharges, snapshot add-on percentages, and region maps move; quote only after opening the provider's current pricing/docs page.
