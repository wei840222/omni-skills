# Firewall operations

Concrete command sequences. Replace placeholders. Prefer dry-run and second
sessions on production hosts.

## UFW (Ubuntu default frontend)

UFW is Ubuntu's default host firewall frontend over netfilter. It is aimed at
simple host rules, not a full policy language.

### Baseline secure host (SSH from one admin IP)

```bash
# 1) Admin path BEFORE enable
sudo ufw allow proto tcp from <ADMIN_CIDR> to any port 22 comment 'ssh-admin'

# optional: rate-limit SSH from anywhere only if source allowlist is impossible
# sudo ufw limit 22/tcp comment 'ssh-limit'

# 2) Defaults
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw default deny routed

# 3) Optional web
# sudo ufw allow 80/tcp comment 'http'
# sudo ufw allow 443/tcp comment 'https'

# 4) Preview, then enable (keep second SSH session open)
sudo ufw --dry-run enable
sudo ufw enable
sudo ufw status verbose
sudo ufw status numbered
```

Notes from `ufw(8)`:

- On install, UFW is **disabled** with default incoming **deny**, outgoing **allow**, routed **deny**.
- You may add rules before enable; after enable, chains are not flushed on each simple add.
- Under SSH, `enable` prompts by default; `ufw --force enable` skips the prompt (use only when intentional).
- IPv6: set `IPV6=yes` in `/etc/default/ufw` for dual-stack filtering; `ufw allow 22` then covers v4 and v6.
- Delete carefully with `ufw status numbered` then `ufw delete <NUM>` (dual-stack generics may need two deletes).

### Useful variants

```bash
# Subnet admin SSH
sudo ufw allow proto tcp from 192.168.0.0/24 to any port 22

# Named service / app profile
sudo ufw app list
sudo ufw allow OpenSSH

# Explicit interface
sudo ufw allow in on eth0 to any port 443 proto tcp

# Dry-run any mutation
sudo ufw --dry-run deny 25/tcp
```

## nftables sketch (simple filter)

```bash
sudo nft add table inet filter
sudo nft add chain inet filter input '{ type filter hook input priority 0; policy drop; }'
sudo nft add chain inet filter forward '{ type filter hook forward priority 0; policy drop; }'
sudo nft add chain inet filter output '{ type filter hook output priority 0; policy accept; }'
sudo nft add rule inet filter input ct state established,related accept
sudo nft add rule inet filter input iif lo accept
sudo nft add rule inet filter input tcp dport 22 ip saddr <ADMIN_CIDR> accept
# sudo nft list ruleset
```

Prefer distribution-native units and `/etc/nftables.conf` persistence over one-off interactive rules when hardening for real.

## Docker: restrict published ports via DOCKER-USER

When containers must publish on the host address and UFW is insufficient:

```bash
# Allow established flows first, then tighten sources on the external interface
sudo iptables -I DOCKER-USER -m state --state RELATED,ESTABLISHED -j ACCEPT
sudo iptables -I DOCKER-USER -i <EXT_IF> ! -s <ADMIN_OR_CLIENT_CIDR> -j DROP
```

Match original public destination after DNAT with `conntrack` when needed (see Docker iptables docs). Persist rules with the host's normal iptables-persistent/nft mechanism.

Safer default when possible:

```bash
# publish only on loopback; put nginx/caddy on host :443
docker run --publish 127.0.0.1:8080:80 ...
```

## Outside-in verification

```bash
# On host
sudo ufw status verbose
ss -lntu
# From another network
nc -vz <HOST_IP> 22
nc -vz <HOST_IP> 443
curl -I --max-time 5 https://<HOST_NAME>
```

Interpret:

- **Refused** — reachable stack, port closed or rejected.
- **Timeout** — filtered/dropped or blackholed path (cloud FW, intermediate ACL, asymmetric route).

## Lockout recovery order

1. Provider web console / serial / IPMI — fix rules or disable guest firewall temporarily.
2. Cloud firewall attachment — open admin CIDR at the provider layer first.
3. Snapshot/restore only after confirming the bad rule set is identified.
4. Re-apply least-privilege rules with a second session before leaving console-only mode.
