# Automatic HTTPS and certificates

Operational rules aligned with Caddy's Automatic HTTPS docs. Re-check live pages via `sources.md` before restating CA endpoints or challenge defaults.

## Activation

Automatic HTTPS turns on when Caddy knows a hostname or IP it is serving (Caddyfile site address, JSON host matcher, CLI `--domain` / `--from`, etc.).

It does **not** fully activate when you:

- explicitly disable automatic HTTPS
- provide no hostnames/IPs
- listen only on the HTTP port
- prefix the site with `http://` in the Caddyfile
- only load certificates manually (unless `ignore_loaded_certificates` is set)

Public names get certificates from public ACME CAs (defaults include Let's Encrypt and ZeroSSL with issuer fallback). Local/internal names and many IP forms use Caddy's local CA under the data directory (`pki/authorities/local`).

## Public hostname checklist

Before expecting a publicly trusted cert:

1. DNS A/AAAA for the name points at this host **before** Caddy tries issuance.
2. Ports **80** and **443** are reachable externally (or forwarded to Caddy). HTTP-01 needs 80; TLS-ALPN needs 443; HTTP→HTTPS redirect also uses the HTTP port.
3. The data directory is **writable and persistent** (not a wiped container layer).
4. The hostname appears in config in a form Caddy manages.

Wildcard names (`*.example.com`) need a challenge path that can prove DNS control — typically **DNS-01** with a supported provider plugin — not plain HTTP-01 on a single host A record alone.

## ACME challenge types

| Challenge | What the CA checks | Typical requirement |
| --- | --- | --- |
| HTTP-01 | Resource over HTTP on port 80 | Port 80 reachable to Caddy |
| TLS-ALPN-01 | Special TLS handshake on port 443 | Port 443 reachable to Caddy |
| DNS-01 | `_acme-challenge` TXT on the name | DNS API credentials / delegated zone |

HTTP-01 and TLS-ALPN-01 are enabled by default; Caddy may pick among enabled challenges and learn which succeeds. Enabling DNS-01 (provider credentials required) is the path for internal-only hosts, many wildcards, and networks that cannot expose 80/443.

On failure, Caddy retries, rotates challenge/issuer, and backs off (including use of staging during some Let's Encrypt retry paths). Treat repeated production failures as a DNS/port/storage problem first, not "run certbot beside Caddy" by default.

## Local HTTPS

For `localhost`, loopback IPs, and similar internal hosts, Caddy serves HTTPS with its local authority. Trust install is a convenience (`caddy trust` / first-run prompt) and may fail in containers or unprivileged services — operators must place the root in the right trust stores when internal PKI matters.

Local HTTPS does **not** use public ACME.

## On-demand TLS

On-demand TLS obtains a certificate during the first handshake for a name not pre-listed. Enable only when names are truly dynamic (customer domains, late DNS). Always configure an **ask** restriction (or equivalent automation policy) so arbitrary SNI cannot exhaust CA quota. Prefer static site addresses when the name set is known.

## Storage and multi-instance

Default file storage lives under the platform data directory (see Conventions / `sources.md`): Linux often `$XDG_DATA_HOME/caddy` or `$HOME/.local/share/caddy`. Official container images commonly persist **`/data`** (certificates, keys, ACME state) and **`/config`**.

- Treat the data directory as durable state, not a cache.
- Multiple Caddy instances managing the same names need **shared storage** (or a single manager); separate local disks cause duplicate issuance fights.
- Export/import storage (`caddy storage export` / `import`) when migrating hosts deliberately.

## Staging and rate limits

Public CAs rate-limit failed and successful issuance. For experiments:

- point automation at Let's Encrypt **staging** (or another non-production directory) until the flow works
- fix DNS and port forwarding before flipping back to production issuers
- avoid purging production storage just to "retry HTTPS"

## Tailscale special case

Hostnames ending in `.ts.net` are not managed like normal public ACME names; Caddy coordinates with a local Tailscale HTTPS setup when that integration is enabled. Verify Tailscale HTTPS permissions separately from Let's Encrypt troubleshooting.
