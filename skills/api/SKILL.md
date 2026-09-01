---
name: api
description: 'Use to debug, authenticate, or write client code for calling third-party REST/GraphQL APIs (e.g. Stripe, OpenAI). Triggers when the user asks to integrate a service, handle 401/403/429 errors, paginations, webhooks, or sync API data. Do not use for building new APIs.'
metadata:
  version: "1.3.7"
  openclaw: '{"emoji":"🔌"}'
  related-skills: '{"http":"Use for HTTP request construction and protocol-level behavior that is not specific to a third-party API.","json":"Use for JSON parsing, transformation, validation, and schema questions outside an API integration workflow.","webhook":"Use for webhook receiver design and delivery handling that needs depth beyond a provider-specific API integration."}'
---

## State location

This skill stores user preferences and integration context. Before its first state read or write, resolve `<state_root>` once for the invocation:

1. Use a user- or host-configured state root when one is explicit.
2. Otherwise, use the first existing directory in this order: `<workspace>/api/`, `<workspace>/memory/api/`, then `~/api/`.
3. If more than one candidate exists, select only the highest-precedence directory, report the separate copies, and keep them independent.
4. If no candidate exists and the user asks to save state, create `<workspace>/api/`. The host supplies `<workspace>`; treat the shell working directory as unrelated to state-root resolution.

Use the selected `<state_root>` for every state operation. Preferences and context follow `references/setup.md`.

REST and GraphQL API reference for 147 services: authentication, endpoints, rate limits, and per-service gotchas, plus pattern playbooks for everything that goes wrong between you and an API. User preferences live in `<state_root>/` — the only location this skill writes (see `references/setup.md` on first use). Former locations `~/Clawic/data/api/` and `~/clawic/api/` are migration sources only; do not move their contents without the user's explicit request.

## When To Use

- User names a service to integrate ("call the Stripe API", "post to a Slack channel") → its section via API Categories below
- A request that "should work" returns 401/403/429, times out, or silently returns wrong data → `references/debug.md` and the pattern files
- Designing the client side of any integration: retries, pagination, webhooks, streaming, file transfer, async job polling
- Choosing between similar providers in a category (email, auth, media) → compare sections in the same category file
- Not for building your OWN API (routing, schema design, versioning your endpoints) — this skill documents consuming others' APIs

## Quick Reference

| Situation | Read | When to load |
|-----------|------|--------------|--------------|
| Endpoints/auth for a named service | Its category file — API Categories table below | On demand |
| 401/403 that "should work", OAuth flow choice, JWT rejected | `references/auth.md` | On demand |
| Works in curl but not in code, works locally but not in prod, TLS errors, mysterious 400s | `references/debug.md` | On demand |
| Duplicated/missing items across pages, loop never ends | `references/pagination.md` | On demand |
| Timeouts, retries, flaky upstream, circuit breakers, provider outage | `references/resilience.md` | On demand |
| 429s, rate-limit headers, quota budgeting, spending less of the limit | `references/rate-limits.md` | On demand |
| Polling for changes, ETag/304 conditional requests, what to cache client-side | `references/caching.md` | On demand |
| Mirroring API data locally, incremental sync, detecting deletions, sync token expired | `references/sync.md` | On demand |
| Blocked by CORS, calling an API from frontend code, key would ship to the browser | `references/browser.md` | On demand |
| SSE stream buffers, hangs, or cuts off; events half-parsed; WebSocket drops | `references/streaming.md` | On demand |
| Receiving events, signature verification, duplicate deliveries | `references/webhooks.md` | On demand |
| Upload rejected with 400/411/413, download corrupted or truncated, presigned URLs | `references/files.md` | On demand |
| 202 Accepted, job polling, batch partial failures, async exports | `references/async-jobs.md` | On demand |
| The service speaks GraphQL (GitHub v4, Shopify, Linear) | `references/graphql.md` | On demand |
| Version pinning, `Sunset`/`Deprecation` headers, provider changed the API | `references/versioning.md` | On demand |
| Sandbox vs live, mocking providers, recorded fixtures, contract drift | `references/testing.md` | On demand |
| Money amounts, timestamps, big numeric IDs, unicode limits in payloads | `references/data-formats.md` | On demand |
| Multiple accounts/keys for one service | `references/credentials.md` | On demand |
| Core request safety, retries, and pagination invariants | `references/core-rules.md` | Before designing client code or diagnosing a broad integration failure |
| HTTP-status-specific diagnosis | `references/status-triage.md` | When the upstream returns an HTTP error response |
| Output preflight for generated code or diagnosis | `references/output-gates.md` | Immediately before returning client code or an operational diagnosis |
| Common integration failure patterns | `references/traps.md` | When reviewing an implementation or diagnosing a surprising result |
| Credential, sandbox, and webhook safety boundaries | `references/security.md` | Before handling credentials, selecting an environment, or exposing a webhook receiver |
| SDK-versus-HTTP, polling-versus-webhooks, or idempotency trade-offs | `references/experts-disagree.md` | When more than one safe implementation approach fits |
| Source provenance and version-sensitive claim verification | `references/research.md` | When validating advice that depends on a standard or changing vendor behavior |
| Anything else | `references/core-rules.md`, then the Official Docs link at the end of each API section | On demand |

## API Categories

| Category | File | Services | When to load |
|----------|------|----------|--------------|--------------|
| AI/ML | `references/apis/ai-ml.md` | anthropic, openai, cohere, groq, mistral, perplexity, huggingface, replicate, stability, elevenlabs, deepgram, assemblyai, together, anyscale | On demand |
| Payments | `references/apis/payments.md` | stripe, paypal, square, plaid, chargebee, paddle, lemonsqueezy, recurly, wise, coinbase, binance, alpaca, polygon | On demand |
| Communication | `references/apis/communication.md` | twilio, sendgrid, mailgun, postmark, resend, mailchimp, slack, discord, telegram, zoom | On demand |
| Realtime | `references/apis/realtime.md` | sendbird, stream-chat, pusher, ably, onesignal, courier, knock, novu | On demand |
| CRM | `references/apis/crm.md` | salesforce, hubspot, pipedrive, attio, close, apollo, outreach, gong | On demand |
| Marketing | `references/apis/marketing.md` | drift, crisp, front, customer-io, braze, iterable, klaviyo | On demand |
| Developer | `references/apis/developer.md` | github, gitlab, bitbucket, vercel, netlify, railway, render, fly, digitalocean, heroku, cloudflare, circleci, pagerduty, launchdarkly, split, statsig | On demand |
| Database | `references/apis/database.md` | supabase, firebase, planetscale, neon, upstash, mongodb, fauna, xata, convex, appwrite | On demand |
| Auth | `references/apis/auth-providers.md` | clerk, auth0, workos, stytch | On demand |
| Media | `references/apis/media.md` | cloudinary, mux, bunny, imgix, uploadthing, uploadcare, transloadit, vimeo, youtube, spotify, unsplash, pexels, giphy, tenor | On demand |
| Social | `references/apis/social.md` | twitter, linkedin, instagram, tiktok, pinterest, reddit, twitch | On demand |
| Productivity | `references/apis/productivity.md` | notion, airtable, google-sheets, google-drive, google-calendar, dropbox, linear, jira, asana, trello, monday, clickup, figma, calendly, cal, loom, typeform | On demand |
| Business | `references/apis/business.md` | shopify, docusign, hellosign, bitly, dub | On demand |
| Geo | `references/apis/geo.md` | openweather, mapbox, google-maps | On demand |
| Support | `references/apis/support.md` | intercom, zendesk, freshdesk, helpscout | On demand |
| Analytics | `references/apis/analytics.md` | mixpanel, amplitude, posthog, segment, sentry, datadog, algolia | On demand |

## Fast path

1. Resolve `<state_root>` only if this request needs saved preferences or context; otherwise use the documented defaults.
2. Identify the provider and load the matching `references/apis/*.md` category file, then the provider's indexed section only.
3. Load the symptom-specific reference from Quick Reference; for generated client code or an operational diagnosis, finish with `references/output-gates.md`.
4. Verify endpoint, quota, pricing, model, and deprecation claims against that provider section's Official Docs link before treating them as current.

## How to Navigate API Files

Each category file starts with an index table (API name → line number). Read the index, then only the section you need (50-100 lines each):

```bash
head -20 references/apis/ai-ml.md          # index
sed -n '139,251p' references/apis/ai-ml.md # one API's section (OpenAI, per the index)
```

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml` (loading and recording procedure: `references/setup.md`).

| Variable | Type | Default | Effect | On demand |
|---|---|---|---|
| example_language | curl \| python \| javascript \| go | curl | Language every request example is rendered in, across all category and pattern files | On demand |
| client_style | raw \| sdk | raw | Whether examples use raw HTTP or the provider's official SDK (tradeoff: Where Experts Disagree) | On demand |
| default_environment | sandbox \| live | sandbox | Which credential examples reference (`references/credentials.md` naming); live only on explicit request — enforced by the last Output Gate | On demand |
| retry_max | number (0-10) | 4 | Retry ceiling used in Core Rule 2's formula and all generated retry code | On demand |

Preference areas — customizable dimensions; a stated preference gets recorded in `<state_root>/config.yaml` and applied:

- **Tooling**: HTTP client library (requests/httpx, axios/fetch, net/http) and testing tool (curl, HTTPie, Postman) — shapes every snippet
- **Integrations**: the user's chosen provider per category (payments → Stripe, email → Postmark) — which service section answers a generic ask
- **Conventions**: credential env-var naming (default scheme: `references/credentials.md`), error-handling style (exceptions vs result values) — shapes generated code
- **Thresholds**: org-mandated timeouts and retry budgets — override the `references/resilience.md` defaults when stated
- **Safety posture**: whether examples may include write/mutating calls, confirm-before-live behavior — tightens or relaxes the environment gate
- **Output format**: snippet-only vs annotated walkthrough — answer verbosity
