---
name: yelp
description: Search Yelp businesses and reviews, compare local options, and audit listing quality with official APIs, public pages, and safe action boundaries. Use when Yelp-specific ratings, review signals, local business comparisons, or listing audits are needed.
metadata:
  openclaw: '{"emoji":"⭐","requires":{"bins":["curl","jq"]}}'
  related-skills: '{"apple-maps":"Opens a selected business for directions and location confirmation.","google-reviews":"Cross-checks Yelp signals against Google review patterns and reputation drift.","maps":"Adds routing, geocoding, and distance checks before the user acts on a shortlist.","restaurants":"Turns shortlisted places into dining recommendations and decision filters.","tripadvisor":"Cross-checks travel-heavy restaurant and attraction choices outside Yelp."}'
---

## State location

Yelp state may exist in `<workspace>/yelp/`, `<workspace>/memory/yelp/`, or `~/yelp/`. Before a state operation, resolve `<state_root>` once for the invocation:

1. Use an explicitly configured state path when one is supplied.
2. Otherwise, use the first existing directory in this order: `<workspace>/yelp/`, `<workspace>/memory/yelp/`, then `~/yelp/`.
3. When multiple candidates exist, use only the highest-precedence location and report that separate copies exist.
4. When none exists and the user requests persistent Yelp preferences or notes, create `<workspace>/yelp/`.
5. When the host does not provide `<workspace>`, use an existing `~/yelp/`; otherwise request a state path before creating data.

Keep the selected `<state_root>` for all state operations. Create `sessions/`, `businesses/`, `api/`, and `audits/` only when the corresponding Yelp task needs them.

## When to use

Use this skill for Yelp-specific local-business discovery, direct comparison, review-signal analysis, delivery or takeout checks where Yelp exposes those signals, or listing audits for owners and operators.

## Architecture

Memory and task notes use `<state_root>/`.

```text
<state_root>/
├── memory.md
├── sessions/
│   └── YYYY-MM-DD.md
├── businesses/
│   └── {city-or-segment}.md
├── api/
│   ├── alias-cache.md
│   └── request-log.md
└── audits/
    └── {business}.md
```

## Reference routing

| Resource | Load when |
| --- | --- |
| `references/setup.md` | First use or a missing `<state_root>` |
| `references/memory-template.md` | Creating or updating `<state_root>/memory.md` |
| `references/api-workflows.md` | Calling the official Yelp API with `YELP_API_KEY` |
| `references/search-playbook.md` | Discovering or comparing local businesses |
| `references/review-analysis.md` | Clustering complaints or interpreting review signals |
| `references/listing-audit.md` | Auditing a business listing |
| `references/access-boundaries.md` | Assessing authorization or access limits |

## Requirements

- Public-page verification needs no credentials; API workflows need `YELP_API_KEY`.
- Owner-side tasks require the user’s explicit approval and authorized access.
- Confirm before sending phone numbers, exact addresses, or account-scoped listing data to live Yelp endpoints.

## Core rules

1. Choose page, API, or audit mode before querying and state the source mode in the result.
2. Resolve the exact business by location, category, alias, or phone before comparison. Ask one disambiguation question if identity remains unclear.
3. Keep consumer research separate from owner-side work. Prepare drafts only after the user requests them and authorization is established.
4. Rank with rating, review volume, recency, complaint themes, price fit, and category match together.
5. Re-check time-sensitive operational fields—hours, delivery, takeout, transactions, and attributes—before the user acts.
6. Persist reusable filters, shortlist reasons, and verified aliases under `<state_root>/`; exclude API keys, headers, and signed URLs.
7. For discovery, provide a shortlist with fit, trade-offs, and next checks. For audits, group high-impact fixes first. For review analysis, separate evidence, inference, and uncertainty.

## Safe operation

Use official API requests with a valid `YELP_API_KEY` or normal navigation of visible Yelp pages. If an API field is unavailable, say so; if public and API data conflict, surface the conflict. Account-only work stays at the draft or checklist stage until explicit authorization is confirmed.

## Common mistakes

- Normalize distance or market before comparing businesses from different neighborhoods.
- Treat low-volume or stale reviews as provisional signals rather than stable rankings.
- Re-check operational flags at decision time.
- Maintain the consumer-research and owner-action boundary.
- Record redacted request information only.

## External endpoints

| Endpoint | Data sent | Purpose |
| --- | --- | --- |
| `https://api.yelp.com/v3/businesses/search` | Query text, location or coordinates, category, price, and sort filters | Discover businesses and candidates |
| `https://api.yelp.com/v3/businesses/search/phone` | Phone number and country code | Resolve an exact business |
| `https://api.yelp.com/v3/businesses/{id_or_alias}` and `/reviews` | Business ID or alias plus locale parameters | Fetch details, attributes, photos, hours, and reviews |
| `https://api.yelp.com/v3/transactions/delivery/search` | Location and optional category or price filters | Check delivery candidates where supported |
| `https://www.yelp.com/*` | Normal browser navigation signals and user search terms | Verify visible public-page evidence |

Send no other data externally unless the user approves it. Yelp receives business names, search terms, location hints, phone numbers, and requested filters for live calls.
