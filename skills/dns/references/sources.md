# DNS Skill Research Sources

## Core DNS behavior

- **RFC 1034 / 1035** — domain concepts and message formats via https://www.rfc-editor.org/rfc/rfc1034 and https://www.rfc-editor.org/rfc/rfc1035
- **RFC 2181** — clarifications on TTL and RRset consistency via https://www.rfc-editor.org/rfc/rfc2181
- **RFC 8499** — DNS terminology via https://www.rfc-editor.org/rfc/rfc8499
- **dig(1) man page** — query diagnostics and trace mode via https://manpages.debian.org/bookworm/dnsutils/dig.1.en.html

## Email authentication

- **RFC 7208 — SPF** — single SPF TXT RRset and `all` mechanisms via https://www.rfc-editor.org/rfc/rfc7208
- **RFC 6376 — DKIM** — message signing via https://www.rfc-editor.org/rfc/rfc6376
- **RFC 7489 — DMARC** — policy publication and reporting via https://www.rfc-editor.org/rfc/rfc7489
- **DMARC.org overview** — operational DMARC rollout guidance via https://dmarc.org/overview/

## CAA and certificate issuance

- **RFC 8659 — CAA** — Certificate Authority Authorization via https://www.rfc-editor.org/rfc/rfc8659
- **Let's Encrypt — CAA** — issuance checks and common record forms via https://letsencrypt.org/docs/caa/

## Apex, aliases, and wildcards

- **RFC 1034 §3.6 / CNAME constraints** — CNAME cannot coexist with other data at the same owner name via https://www.rfc-editor.org/rfc/rfc1034
- **RFC 4592 — wildcards** — wildcard synthesis rules (apex is not matched by `*.example.com`) via https://www.rfc-editor.org/rfc/rfc4592
- **Cloudflare docs — CNAME flattening** — apex alias behavior and migration caveats via https://developers.cloudflare.com/dns/cname-flattening/

## Cloudflare proxy behavior

- **Cloudflare docs — proxy status** — orange-cloud HTTP proxy vs grey-cloud DNS-only via https://developers.cloudflare.com/dns/proxy-status/
- **Cloudflare docs — TTL** — proxied records use Cloudflare-controlled caching behavior via https://developers.cloudflare.com/dns/manage-dns-records/reference/ttl/
