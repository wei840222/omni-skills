---
name: dns
description: >
  Configure and debug DNS records. Use when handling TTL changes, email
  authentication (SPF/DKIM/DMARC), CAA records, www/wildcard setup, resolver
  mismatches, or Cloudflare proxy side effects.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌍"}'
  related-skills: '{"domain-registration":"Registrar purchase, transfer, and renewal before DNS handoff.","domains":"Domain portfolio and ownership context beyond record edits.","network":"Broader connectivity diagnosis when DNS is only one layer.","hosting":"Point domains at hosting targets after records are correct.","ssl":"Certificate issuance and renewal once DNS control is verified.","nginx":"Reverse-proxy and TLS termination after DNS reaches the origin."}'
---

## When to load

Load this skill for DNS record design, migration TTL planning, email authentication records, CAA hardening, www/wildcard behavior, `dig`-based debugging, and Cloudflare proxy vs DNS-only trade-offs.

## Progressive disclosure

- **Migrations and TTL:** load `references/migration-and-ttl.md`
- **Email deliverability (SPF, DKIM, DMARC):** load `references/email-authentication.md`
- **CAA / issuance control:** load `references/security-and-caa.md`
- **www and wildcards:** load `references/web-records.md`
- **Debugging (`dig`) and Cloudflare specifics:** load `references/debugging-and-providers.md`
- **Research sources:** load `references/sources.md` when verifying a claim before advising a change
