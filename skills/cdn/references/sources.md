# CDN research sources (Gate 6)

Verified reachable official documentation used while hardening this skill.
Re-check before quoting plan prices, free-tier limits, or API paths that may
drift.

## Core product docs

| Topic | Source | URL |
| --- | --- | --- |
| Cloudflare API reference | Cloudflare Docs | https://developers.cloudflare.com/api/ |
| Cloudflare cache purge | Cloudflare Cache docs | https://developers.cloudflare.com/cache/how-to/purge-cache/ |
| Cloudflare published IP ranges | Cloudflare | https://www.cloudflare.com/ips/ |
| Cloudflare plan overview | Cloudflare | https://www.cloudflare.com/plans/ |
| CloudFront CreateInvalidation API | AWS Docs | https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_CreateInvalidation.html |
| CloudFront pricing / free tier | AWS | https://aws.amazon.com/cloudfront/pricing/ |
| bunny.net Core API overview | bunny.net Docs | https://docs.bunny.net/reference/bunnynet-api-overview |
| bunny.net pricing | bunny.net | https://bunny.net/pricing/ |
| Fastly CLI reference | Fastly Developer Hub | https://developer.fastly.com/reference/cli/ |
| Fastly pricing | Fastly | https://www.fastly.com/pricing/ |

## Claim handling notes

- **CLI invalidation shapes** (CloudFront `create-invalidation`, Cloudflare
  `/purge_cache`, Bunny `/purge`) follow the vendor docs above; distribution
  IDs and zone IDs remain caller-supplied placeholders.
- **Bandwidth unit costs** in `providers.md` are rough comparative order-of-
  magnitude only. Replace with the vendor calculator for any buying decision.
- **CloudFront “free tier”** language must follow the current AWS pricing page
  (amount and duration change); do not hard-code expired promotions as fact.
- **Origin allowlists** must use the provider’s current published IP list
  (e.g. Cloudflare IP ranges page), not a copied historical CIDR table alone.
