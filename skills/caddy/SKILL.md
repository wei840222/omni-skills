---
name: caddy
description: >
  Configure Caddy as a reverse proxy with automatic HTTPS, Caddyfile syntax,
  certificate storage, Docker networking, reload/validate workflows, and
  reverse_proxy load-balancing. Use when writing or debugging a Caddyfile,
  fixing ACME/cert failures, WebSocket or header issues behind Caddy, or
  choosing Caddy over nginx/Traefik for simple automatic TLS. Prefer `nginx`
  or `traefik` for those stacks, `ssl` for raw ACME/cert tooling outside Caddy,
  and `docker` for container networking beyond Caddy service names.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔒","requires":{"bins":["caddy"]}}'
  related-skills: '{"nginx":"Nginx reverse proxy, location matching, and TLS termination when the stack is nginx-first.","traefik":"Traefik labels, entrypoints, and Docker provider routing instead of Caddyfile.","ssl":"Certificate issuance, renewal, and TLS debugging outside Caddy automatic HTTPS.","docker":"Compose networks, published ports, and volume mounts that Caddy depends on.","vps":"Host firewall, DNS A/AAAA, and public port exposure around the Caddy edge.","dns":"DNS records and ACME DNS-01 provider setup upstream of certificate issuance.","firewall":"Opening or forwarding TCP 80/443 (and UDP 443 for HTTP/3) to the Caddy process.","websocket":"App-level WebSocket protocol issues after the proxy upgrade path is correct."}'
---

# Caddy

Operator guidance for **Caddy reverse proxy + automatic HTTPS** via Caddyfile. Prefer Caddy when you want managed certificates and a short config; switch to `nginx` / `traefik` when that is already the edge.

This skill is **stateless** for credentials. Optional lab notes may use `<state_root>` (see State location). Never commit real TLS keys, ACME account material, or DNS API tokens into the package.

## When to load

Load for Caddy-specific work:

- Caddyfile site blocks, `reverse_proxy`, automatic HTTPS / ACME failures
- `caddy validate` / `fmt` / `reload` / `adapt` workflows
- Docker Compose service-name upstreams and `/data`+`/config` volumes
- WebSocket/SSE through Caddy, security headers, HTTP/3 enablement
- Choosing Caddy vs nginx/Traefik for a simple public HTTPS edge

Prefer other skills when the ask is mainly:

- nginx.conf / `proxy_pass` semantics → `nginx`
- Traefik labels / file provider → `traefik`
- certbot/acme.sh or generic TLS debugging → `ssl`
- container image/build/network primitives → `docker`
- VPS hardening and public exposure → `vps`

## State location

Optional operator notes (site inventory, staging ACME endpoint choice, non-secret upstream map) may live under `<workspace>/caddy/`, `<workspace>/memory/caddy/`, or `~/caddy/`. Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when available.
2. Otherwise the first existing directory in that order.
3. If multiple exist, use only the highest-precedence path and report duplicates.
4. Create `<workspace>/caddy/` only with user consent when no candidate exists.

Keep live Caddy data directories (`$XDG_DATA_HOME/caddy` or platform default under Conventions), private keys, and DNS provider tokens **out of the skill package and out of git**. Examples use placeholders such as `<UPSTREAM_HOST>:3000` and `<DNS_PROVIDER_TOKEN>`.

## Routing

Keep `SKILL.md` as the progressive-disclosure router; load supporting references only when needed:

- **Automatic HTTPS, ACME challenges, storage, staging CA** → `references/automatic-https.md`
- **Caddyfile reverse_proxy, headers, Docker upstreams, ops commands** → `references/caddyfile-and-ops.md`
- **Gate 6 primary sources** → `references/sources.md`

## Core rules

1. **Automatic HTTPS is the default** — give Caddy a public hostname, reachable ports 80/443, and persistent data storage; prefer Caddy-managed certificates unless a deliberate exception needs external ACME tooling ([Automatic HTTPS](https://caddyserver.com/docs/automatic-https)).
2. **Validate then reload** — `caddy validate --config <path>` then `caddy reload --config <path>` so a bad config keeps the previous process config instead of dropping the edge.
3. **Trust Caddy's proxy headers** — `reverse_proxy` sets `X-Forwarded-For` / `X-Forwarded-Proto` / `X-Forwarded-Host` by default; avoid duplicating them unless you are intentionally overriding.
4. **Preserve certificate storage** — the data directory is not a cache; losing it forces re-issuance and can hit CA rate limits. On Docker, persist `/data` and `/config`.
5. **Test against staging ACME** — point experiments at Let's Encrypt staging (or equivalent) before production issuance so rate limits do not block real names.

## Minimal patterns

Public reverse proxy (automatic HTTPS when DNS points here and 80/443 are open):

```caddyfile
example.com {
	reverse_proxy localhost:3000
}
```

Debug logging via global options:

```caddyfile
{
	debug
}

example.com {
	reverse_proxy localhost:3000
}
```

Format and check before reload:

```bash
caddy fmt --overwrite /etc/caddy/Caddyfile
caddy validate --config /etc/caddy/Caddyfile
caddy reload --config /etc/caddy/Caddyfile
```

## Safety

- Use placeholders for secrets; never embed DNS API tokens or private keys in examples committed to git.
- Prefer `caddy reload` over process restart on a live edge so connections are not dropped for a config-only change.
- Open both 80 and 443 for public HTTP-01 / TLS-ALPN issuance and HTTP→HTTPS redirect; use DNS-01 when the host is not publicly reachable on those ports.
- Add explicit security headers when the app does not; automatic HTTPS does not replace CSP / frame options.
