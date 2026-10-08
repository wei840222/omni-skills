---
name: ssl
description: >
  Issue, renew, and debug TLS/SSL certificates and HTTPS endpoints with certbot,
  ACME clients, openssl, and server configs (Nginx, Apache, Caddy, Traefik,
  HAProxy, Node). Use for Let's Encrypt issuance, chain/expiry/hostname errors,
  mixed content, format conversion (PEM/DER/PKCS#12), and automated renewal.
  Prefer `nginx`/`caddy`/`traefik` for reverse-proxy routing beyond TLS
  termination, `network` for generic reachability outside certificates, and
  `oauth` for application auth rather than transport TLS.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔒"}'
  related-skills: '{"caddy":"Automatic HTTPS and simpler reverse-proxy configs when Caddy owns termination.","linux":"Host permissions, systemd timers, and firewall ports that block ACME or private-key reads.","network":"Layer-3 reachability, DNS, and routing diagnosis outside certificate content.","nginx":"Nginx reverse-proxy routing, upstreams, and TLS termination directives beyond issuance.","oauth":"Application identity (JWT/OAuth) separate from transport-layer TLS.","traefik":"Traefik ACME resolvers and router TLS when the edge is Traefik."}'
---

# SSL / TLS certificates

Stateless domain skill for **HTTPS certificate lifecycle and secure-connection debugging**. It does not store private keys, account credentials, or host inventories in the package.

## When to load

Load when the user needs:

- free DV certs via Let's Encrypt / ACME (`certbot`, acme.sh, Caddy auto-HTTPS, Traefik ACME)
- expiry, chain incomplete, hostname mismatch, mixed content, or authority-invalid errors
- openssl inspection of live endpoints or on-disk certs
- certificate format conversion (PEM, DER, PKCS#12, PKCS#7)
- server TLS snippets for Nginx, Apache, Caddy, Traefik, HAProxy, or Node
- renewal automation and dry-run validation

Prefer sibling skills when the job is mainly:

| Job | Skill |
| --- | --- |
| Nginx locations, upstreams, proxy errors | `nginx` |
| Caddy site blocks beyond auto-HTTPS | `caddy` |
| Traefik routers/services beyond ACME | `traefik` |
| DNS/routing/firewall reachability | `network` / `linux` |
| App auth (JWT, OAuth) | `oauth` |

## Core path

1. Confirm the failure class (issuance, chain, expiry, name mismatch, mixed content, client trust).
2. Inspect with openssl before rewriting server config.
3. Prefer full chain files (`fullchain.pem`) and automated renewal over one-off manual certs.
4. After any config change, reload the server and re-check verify return code `0 (ok)`.

## Depth on demand

| Need | Load |
| --- | --- |
| Tasks, quick commands, error matrix, cert types, renewal defaults | `references/domain.md` |
| PEM/DER/PKCS conversions and key/cert match checks | `references/formats.md` |
| Nginx / Apache / Caddy / Traefik / HAProxy / Node patterns | `references/servers.md` |
| Diagnostic commands and per-problem fix branches | `references/troubleshooting.md` |
| Gate 6 primary sources and current limits | `references/sources.md` |

## Safety defaults

- Keep private keys mode `600` (or tighter) and out of git, chat logs, and skill packages.
- Use Let's Encrypt **staging** while developing ACME clients; production has rate limits.
- Renew 90-day certificates around day 60; never rely on last-day manual renewal.
- Serve intermediates with the leaf (`fullchain` / chain file); browsers may hide incomplete-chain bugs that `curl` still fails on.
