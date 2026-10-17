# Official Sources — Whop

Refresh mutable product, API, sandbox, and affiliate claims against these live
pages. Record the retrieval date in PR notes when a fact changes
recommendations.

## Agent Skills specification

- https://agentskills.io/llms.txt
- https://agentskills.io/specification
- https://agentskills.io/skill-creation/best-practices
- https://agentskills.io/skill-creation/optimizing-descriptions
- https://github.com/agentskills/agentskills/tree/main/skills-ref

## Whop docs index and developer guides (retrieved 2026-10-18)

- Docs index: https://docs.whop.com/llms.txt
- Developer index: https://docs.whop.com/_llms/for-developers.txt
- Quickstart: https://docs.whop.com/developer/quickstart.md
- Auth & API Keys: https://docs.whop.com/developer/guides/auth-scoping.md
- iframe Authentication: https://docs.whop.com/developer/guides/authentication.md
- Permissions: https://docs.whop.com/developer/guides/permissions.md
- Development Proxy: https://docs.whop.com/developer/guides/dev-proxy.md
- Webhooks: https://docs.whop.com/developer/guides/webhooks.md
- Sandbox: https://docs.whop.com/developer/guides/sandbox.md
- Create a Checkout Link: https://docs.whop.com/payments/create-checkout-link.md
- Set Up Global Affiliates: https://docs.whop.com/affiliates/setup-global.md

## Integration notes pinned from live docs (retrieved 2026-10-18)

- Checkout links cover free, one-time, and recurring payment paths from the
  dashboard.
- Global affiliates default to a **30%** commission and can be changed per
  product (Global Affiliate Rate / Member Affiliate Rate).
- Production REST base: `https://api.whop.com/api/v1`. Sandbox REST base:
  `https://sandbox-api.whop.com/api/v1`. Sandbox frontend:
  `https://sandbox.whop.com`.
- Whop webhooks follow the Standard Webhooks specification
  (`webhook-id`, `webhook-signature`, `webhook-timestamp`). Prefer SDK verify
  helpers when available.
- Webhook envelopes pinned on/after `2026-08-14` use `account_id`; older or
  unpinned webhooks may still emit `company_id`.
- Credential modes include Account/App API keys, account-scoped user tokens,
  account access tokens, iframe user tokens (`x-whop-user-token`), and OAuth
  tokens. Keep API keys server-side.
- Sandbox is for payins and webhook plumbing; docs warn against relying on apps
  / messaging in sandbox, and note card-only alternative-payment limits. Treat
  Elements sandbox availability as a live fact.
- Local embedded-app development uses `@whop-apps/dev-proxy` / `whop-proxy` to
  inject iframe auth headers similar to production.
