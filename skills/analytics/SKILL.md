---
name: analytics
description: >
  Deploy and harden privacy-first web analytics with Umami, Plausible, and
  PostHog: API auth patterns, event capture, rate limits, PII boundaries, and
  GDPR consent/retention defaults. Use when configuring tracking scripts, API
  keys, custom events, or privacy constraints. Prefer `plausible` or `umami`
  for single-vendor deep dives, and `mobile-app-analytics` for mobile store/
  Firebase funnels.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📊"}'
  related-skills: '{"plausible":"Deep Plausible Stats/Events API queries and site memory.","umami":"Umami self-host and tracker configuration details.","mobile-app-analytics":"Mobile retention/funnels via store consoles and Firebase.","mixpanel":"Product analytics event modeling outside privacy-first web stacks."}'
---

# Analytics

Cross-vendor guidance for **privacy-first web analytics** (Umami, Plausible, PostHog). This skill is **stateless** — it does not store credentials or persistent site inventories in the package.

## When to load

- Choosing or wiring Umami / Plausible / PostHog tracking scripts and APIs
- API auth mistakes (`site_id` vs domain, website ID + Bearer key, project token)
- Rate-limit / 429 backoff, batching, and JSON-serializable event properties
- GDPR consent, retention, and PII exclusion for custom events

Prefer other skills when the ask is mainly:

- Plausible-only stats queries / site memory → `plausible`
- Umami self-host traps (HASH_SALT, DB) → `umami`
- Mobile app retention / store consoles → `mobile-app-analytics`
- Mixpanel-style product analytics modeling → `mixpanel`

## Routing

Keep `SKILL.md` as the router; load supporting references only when needed:

- **API auth, capture endpoints, rate limits** → `references/api-patterns.md`
- **Consent, retention, PII, cookie-free caveats** → `references/privacy.md`
- **Environment split, bot filter, script-load checks** → `references/runtime.md`
- **Gate 6 primary sources** → `references/sources.md`

## Core rules

1. **Identify the vendor first** — Umami website UUID + Bearer API key; Plausible Stats API v2 `site_id` (domain as registered) + `Authorization: Bearer`; PostHog project token on capture/batch public endpoints.
2. **Keep secrets in env vars only** — never hardcode API keys or project tokens in skill text, commits, or client bundles meant for private endpoints.
3. **Events must be pure JSON** — PostHog properties must be JSON-serializable; exclude DOM nodes, functions, and PII (email, names, raw IP) from custom event payloads.
4. **Respect rate limits with backoff** — Plausible Stats API keys default to **600 requests/hour**; PostHog private CRUD endpoints are rate-limited (personal-API-key paths often ~600/min; public capture POSTs are not similarly capped). On HTTP 429 use exponential backoff.
5. **Separate dev from prod** — always use a separate project/site for local testing; production pollution is hard to reverse.
6. **Consent is not optional for EU personal data** — privacy-first or cookie-free tools still need an unambiguous legal basis when identifiers or cross-border processing apply; configure retention/deletion in each product.

## Safety

- Store API keys exclusively in environment variables.
- Exclude PII from custom events and person properties unless the user explicitly designs a compliant collection path.
- Verify `umami` / `plausible` / `posthog` globals (or network 202/200) before assuming pageviews landed.
