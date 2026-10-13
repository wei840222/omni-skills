# Sources (Gate 6)

Full URLs verified while refactoring this skill (2026-10-14). Re-check before
restating product defaults, Docker chain behavior, or CLI flags.

## Agent skill format

- Agent Skills specification index: https://agentskills.io/llms.txt
- Agent Skills specification: https://agentskills.io/specification
- Reference validator package: https://github.com/agentskills/agentskills/tree/main/skills-ref

## Ubuntu UFW / host firewall

- Ubuntu Server — Firewalls (ufw introduction):
  https://documentation.ubuntu.com/server/how-to/security/firewalls/
  Takeaways: ufw is the default Ubuntu firewall frontend; eases iptables; supports IPv4/IPv6 host rules; simple allow/deny examples including SSH from a host or subnet; `--dry-run` prints resulting rules without applying; not a full replacement for complex netfilter policy.
- `ufw(8)` manual (Ubuntu noble):
  https://manpages.ubuntu.com/manpages/noble/man8/ufw.8.html
  Takeaways: default install is disabled with incoming deny, outgoing allow, routed deny; add allow rules before `enable`; SSH enable prompts unless `--force`; `status` treats Anywhere as v4/v6 any; IPV6 controlled via `/etc/default/ufw`; numbered delete; logging levels; `limit` for basic rate limiting.
- Ubuntu Community UFW page:
  https://help.ubuntu.com/community/UFW
  Supporting examples and application profiles (secondary to manpage + Server docs).

## nftables

- nftables wiki — main: https://wiki.nftables.org/wiki-nftables/index.php/Main_Page
- nftables wiki — simple rule management:
  https://wiki.nftables.org/wiki-nftables/index.php/Simple_rule_management
  Takeaways: `nft add rule` targets table/chain; counters optional; insert vs append analogous to iptables `-I`/`-A`.

## Docker packet filtering

- Packet filtering and firewalls:
  https://docs.docker.com/engine/network/packet-filtering-firewalls/
  Takeaways: Docker creates firewall rules for bridge networks (not ipvlan/macvlan/host); default backend iptables with nftables option; Docker + UFW incompatible for published ports because NAT diverts traffic before UFW INPUT/OUTPUT; do not casually modify Docker-managed rules.
- Docker with iptables:
  https://docs.docker.com/engine/network/firewall-iptables/
  Takeaways: `DOCKER-USER` is the supported chain for user filters before Docker forward rules; packets accepted in Docker chains never reach user rules appended to `FORWARD`; match original destination with `conntrack` after DNAT; examples restrict external source IPs with insert+DROP patterns; established/related accept should precede broad DROP.

## Cloud provider firewalls

- Hetzner Cloud Firewalls overview:
  https://docs.hetzner.com/cloud/firewalls/overview/
  Takeaways: unspecified traffic is blocked on inbound and permitted on outbound when no rules are set; rules allow listed addresses/directions.
- DigitalOcean Cloud Firewalls:
  https://docs.digitalocean.com/products/networking/firewalls/
  Takeaways: network-based stateful firewall for Droplets; blocks traffic not expressly permitted; allow/deny actions with deny precedence over overlapping allows.
- Amazon EC2 security groups:
  https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html
  Takeaways: security groups control inbound and outbound traffic for associated instances; default VPC group used if none specified; rule changes apply automatically to associated instances; OS firewalls remain valid additional controls.
- Amazon VPC security group rules (companion):
  https://docs.aws.amazon.com/vpc/latest/userguide/security-group-rules.html
  Supporting detail on authorizing/revoking inbound and outbound rules.

## Related protocol notes (cross-skill)

- WireGuard listens on UDP; example ports such as 51820 are conventional, not protocol-fixed (see `vpn` / `wireguard` sources and https://www.wireguard.com/protocol/).
