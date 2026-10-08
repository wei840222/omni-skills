# SSL domain knowledge

## Core tasks

| Task | Tool / method |
| --- | --- |
| Get free DV cert | `certbot`, acme.sh, Caddy automatic HTTPS, Traefik ACME |
| Check live cert status | `openssl s_client -connect host:443 -servername host` |
| View cert details | `openssl x509 -in cert.pem -text -noout` |
| Public grade / cipher survey | [SSL Labs](https://www.ssllabs.com/ssltest/) or `testssl.sh` |
| Convert formats | `references/formats.md` |
| Server TLS patterns | `references/servers.md` |

## Quick cert commands

```bash
# Let's Encrypt with certbot (nginx plugin example)
certbot certonly --nginx -d example.com -d www.example.com

# Check expiry on a live host
echo | openssl s_client -connect example.com:443 -servername example.com 2>/dev/null \
  | openssl x509 -noout -dates -subject -ext subjectAltName

# Verify chain completeness (look for Verify return code: 0 (ok))
openssl s_client -connect example.com:443 -servername example.com </dev/null
```

## Common errors

| Error | Cause | Fix |
| --- | --- | --- |
| `certificate has expired` / `NET::ERR_CERT_DATE_INVALID` | Leaf past `notAfter` | `certbot renew` (or force for that lineage) then reload server |
| `unable to verify the first certificate` / works in Chrome, fails in curl | Missing intermediate on the wire | Serve `fullchain.pem` (leaf + intermediates), not leaf-only `cert.pem` |
| hostname mismatch / `SSL_ERROR_BAD_CERT_DOMAIN` | Name not on cert SAN/CN | Re-issue covering every hostname clients use |
| mixed content | HTTP subresources on an HTTPS page | Upgrade asset URLs to HTTPS or send `Content-Security-Policy: upgrade-insecure-requests` |
| `ERR_CERT_AUTHORITY_INVALID` | Self-signed or untrusted CA | Use a public CA (Let's Encrypt DV) or install the private CA only for lab trust stores |

Detailed branches: `references/troubleshooting.md`.

## Certificate types

| Type | Use case |
| --- | --- |
| Single domain | One FQDN (`example.com`) |
| Wildcard (`*.example.com`) | All one-level subdomains (needs DNS-01) |
| Multi-domain (SAN) | Several distinct names on one cert (Let's Encrypt allows up to 100 identifiers per cert) |
| Self-signed | Local lab only — browsers warn and automation should treat as non-prod |

Let's Encrypt issues **DV** certificates only (not OV/EV). Default production lifetime is **90 days**; short-lived six-day certs also exist for clients that opt in. Recommend renewing 90-day certs about every **60 days**.

## Renewal defaults

```bash
# Safe rehearsal against the live lineage without publishing a replacement unless needed
certbot renew --dry-run

# Typical system timer/cron (certbot packages usually install this)
0 0 * * * certbot renew --quiet
```

Randomize routine renewal timing so large fleets do not stampede the CA. Use the [staging environment](https://letsencrypt.org/docs/staging-environment/) while building clients so production rate limits stay available for real hosts.

## Out of scope

- Application auth (JWT, OAuth) → `oauth`
- Host OS hardening, systemd, raw firewall ports → `linux`
- Generic L3 reachability / DNS debugging → `network`
- Deep reverse-proxy routing beyond TLS files → `nginx` / `caddy` / `traefik`
