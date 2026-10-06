---
name: cdn
description: >
  Configure, optimize, and troubleshoot CDN deployments: provider choice,
  Cache-Control and cache keys, invalidation/purge pipelines, edge security
  (TLS, WAF, origin shield), and cache-miss debugging. Use when the user is
  setting up Cloudflare/CloudFront/Bunny/Fastly (or similar), tuning hit
  ratio, purging after deploy, hardening origin exposure, or diagnosing stale
  content and origin overload. Prefer `http` for pure protocol Cache-Control
  semantics, `dns` for DNS-only or proxy-vs-DNS-only record work, `ssl` for
  certificate issuance outside the CDN edge, `nginx` for origin reverse-proxy
  termination, and `network`/`firewall` when the problem is reachability or
  host packet filters rather than edge caching.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🌐"}'
  related-skills: '{"http":"Protocol-level Cache-Control, conditional requests, and status codes when the task is not CDN-edge specific.","dns":"DNS records, TTL, and Cloudflare proxy vs DNS-only before CDN hostname work.","ssl":"Certificate issuance and renewal once DNS control is verified outside CDN-managed certs.","nginx":"Origin reverse-proxy and TLS termination behind the CDN.","network":"Layer-3 reachability when CDN is only one hop among many.","firewall":"Host or edge packet filters that must allow only CDN egress IPs to origin.","aws":"Broader AWS account and IAM context when CloudFront sits inside a larger AWS design.","cloud":"General cloud landing-zone choices before locking a CDN provider."}'
---

# CDN

Edge caching and delivery guidance for public web and API traffic: when a CDN
helps, how to set cache policy, how to purge safely, how to keep the origin
off the public internet, and how to debug HIT/MISS and stale-content reports.

This skill is **stateless**. Keep provider accounts, zone IDs, API tokens, and
distribution configs in ordinary user files outside the skill package.

## When to load

| Need | Resource |
| --- | --- |
| Provider comparison, CLI purge snippets, selection matrix | `references/providers.md` |
| Cache-Control recipes, cache keys, invalidation strategies | `references/caching.md` |
| TLS, origin shield, WAF, rate limits, cache poisoning | `references/security.md` |
| HIT/MISS, stale content, origin overload, cert symptoms | `references/troubleshooting.md` |
| Deploy checklists and “do I need a CDN?” | `references/best-practices.md` |
| Dated official docs used for Gate 6 claims | `references/sources.md` |
| Evaluation harness only | `test-prompts.json` |

## Operating sequence

1. **Confirm the problem is edge delivery** (global latency, cache hit ratio, purge after deploy, origin hiding, WAF at the edge). If it is pure HTTP header semantics with no CDN product in play, prefer `http`.
2. **Identify provider and surface** (Cloudflare zone, CloudFront distribution, Bunny pull zone, Fastly service). Load `references/providers.md` for CLI/API shapes; verify live pricing and quotas on the vendor page before quoting costs.
3. **Separate browser cache, CDN cache, and origin**. Load `references/caching.md` for Cache-Control and key design; load `references/troubleshooting.md` when status is MISS/BYPASS/stale.
4. **Harden origin before widening cache**. Load `references/security.md` for TLS floor, authenticated origin pulls, CDN-only firewall allowlists, and sensitive `no-store` paths.
5. **Prefer versioned URLs over emergency full purge**. Use tagged/surrogate purge when the vendor supports it; full purge is last resort.
6. **Hand off when needed**: DNS apex/proxy mode → `dns`; origin nginx/TLS → `nginx`/`ssl`; raw connectivity → `network`/`firewall`.

## Scope

- Guidance only: no package-local writes, no required network calls from the skill package itself.
- Examples use placeholders (`{zone_id}`, `EDFDVBD6EXAMPLE`, `$BUNNY_API_KEY`, `***`). Never embed real tokens.
- Cost figures in references are indicative snapshots; always re-check the vendor pricing page for the user’s region and plan.
- Do not treat CDN presence as a substitute for origin authn/authz or correct `Cache-Control` on sensitive responses.

## Near-misses

| Request shape | Better skill |
| --- | --- |
| “What does `no-cache` vs `no-store` mean?” with no CDN product | `http` |
| “Fix my apex CNAME / proxy orange-cloud only” | `dns` |
| “Issue a Let’s Encrypt cert on the origin box” | `ssl` |
| “nginx reverse proxy + upstream TLS” | `nginx` |
| “Packets never reach the host / traceroute dies” | `network` / `firewall` |
| “Design the whole AWS account around CloudFront” | `aws` / `cloud` |
