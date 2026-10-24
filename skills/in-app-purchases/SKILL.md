---
name: in-app-purchases
description: Implement in-app purchases, auto-renewable subscriptions, and paywalls across iOS and Android. Use this when the user needs to integrate StoreKit, Google Play Billing, or RevenueCat, verify receipts, or design conversion-optimized paywalls.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"💳"}'
  related-skills: '{"android": "Android app structure and Play Console workflows around billing.", "app-store-connect": "App Store Connect API, metadata, and review submission around IAP products.", "billing": "Server-side subscription charging, invoices, webhooks, and tax outside store IAP.", "flutter": "Cross-platform mobile IAP plugins and shared purchase flows.", "ios": "Native iOS build, entitlements, and StoreKit-adjacent app patterns.", "mobile-app-analytics": "Retention, funnel, and subscription metrics after monetization ships.", "monetize": "Broader pricing model and launch sequencing outside store SDK details.", "paywall": "Paywall UX patterns and conversion experiments.", "pricing": "B2B/SaaS list-price design when the ask is packaging rather than store IAP.", "testflight": "iOS/macOS beta distribution used before production IAP validation."}'
---

## When to Use

User needs to implement in-app purchases, subscriptions, paywalls, or store monetization flows. Agent handles native APIs (StoreKit 2, Google Play Billing), cross-platform SDKs (RevenueCat, Adapty, Qonversion), paywall design, server verification, and subscription analytics.

## When to Load References

| Topic | File | When to load |
|-------|------|--------------|
| iOS StoreKit 2 | `references/storekit.md` | Product load, purchase, finish, restore on iOS |
| Android Billing | `references/google-play.md` | Play Billing Library, acknowledge, Real-time developer notifications |
| Flutter packages | `references/flutter.md` | Cross-platform plugin choice and shared purchase glue |
| RevenueCat SDK | `references/revenuecat.md` | Entitlements, offerings, customer info, webhooks |
| Platform comparison | `references/platforms.md` | Native vs managed SDK tradeoffs |
| Server verification | `references/server.md` | Receipt/JWS verify, entitlements DB, webhook handlers |
| Paywall design | `references/paywalls.md` | Pricing presentation, trials, A/B patterns |
| Subscription metrics | `references/analytics.md` | Trial start, convert, churn, LTV instrumentation |
| Testing & sandbox | `references/testing.md` | StoreKit config, sandbox accounts, license testers |
| Sources | `references/sources.md` | Unstable pricing, policy, or API claims |

## Core Rules

### 1. Choose architecture first
| Approach | When to use | Tradeoff |
|----------|-------------|----------|
| Native only | Single platform, full control | More code, no cross-platform sync |
| RevenueCat/Adapty | Cross-platform, fast launch | Platform fee, external dependency |
| Hybrid | Native client + own backend | Full control, more backend work |

### 2. Managed platform SDKs
| Platform | Pricing signal | Best for |
|----------|----------------|----------|
| RevenueCat | Free under published MTR threshold, then ~1% | Most apps, strong docs |
| Adapty | Free under published MTR threshold, then ~0.6% | Cost-conscious, paywall A/B |
| Qonversion | Free under published MTR threshold, then higher % | Simple setup |
| Superwall | Paywall-focused pricing | Paywall experimentation only |
| Glassfy | Free under published MTR threshold, then low % | Budget option |

Confirm current MTR thresholds and fees from vendor docs before quoting numbers in production plans. See `references/sources.md`.

### 3. Product types
| Type | iOS | Android | Use case |
|------|-----|---------|----------|
| Consumable | Yes | Yes | Credits, coins, lives |
| Non-consumable | Yes | Yes | Permanent unlock |
| Auto-renewable | Yes | Yes | Subscriptions |
| Non-renewing | Yes | No native equivalent | Season pass / time-limited access |

### 4. Server verification is required
Verify receipts and signed transactions on the server; do not grant durable entitlements from client-only success callbacks:
- iOS: App Store Server API with JWS verification
- Android: Google Play Developer API + purchase acknowledgment
- RevenueCat or similar: webhooks + REST entitlement reads

### 5. Handle all transaction states
| State | Action |
|-------|--------|
| Purchased | Verify → grant → finish/acknowledge |
| Pending | Wait; show pending UI |
| Failed | Show error; block grant |
| Deferred | Wait for parental approval |
| Refunded | Revoke immediately |
| Grace period | Limited access; prompt payment update |
| Billing retry | Maintain access during retry window |

### 6. Subscription lifecycle events
Handle these via native notifications or webhooks:
- INITIAL_PURCHASE → grant access
- RENEWAL → extend access
- CANCELLATION → mark will-expire
- EXPIRATION → revoke access
- BILLING_ISSUE → prompt payment update
- GRACE_PERIOD → limited access window
- PRICE_INCREASE → collect required consent (iOS)
- REFUND → revoke and flag
- UPGRADE/DOWNGRADE → apply proration rules

### 7. Restore purchases
Required by store guidelines:
- Provide a visible restore control
- Support logged-out restore where the platform allows
- Handle Family Sharing on iOS
- Keep cross-device entitlement sync consistent with the chosen backend

### 8. Paywall practices
Load `references/paywalls.md` for patterns:
- Present value before price
- Use clear pricing anchors (commonly 2–3 options)
- Make free trial terms explicit
- Add social proof only when real
- Treat copy, price, and layout as experiment variables

### 9. Testing strategy
| Environment | iOS | Android |
|-------------|-----|---------|
| Dev/Debug | StoreKit Configuration file | License testers |
| Sandbox | Sandbox Apple IDs | Internal testing track |
| Production | Real accounts | Production |

Sandbox subscription time compression (verify current Apple table before relying on it):
- 1 week → minutes-scale
- 1 month → minutes-scale
- 1 year → about one hour

### 10. Store policy boundaries
- Digital goods consumed in-app generally require platform IAP
- Physical goods and real-world services may use external processors (for example Stripe)
- Reader / external-link exceptions are narrow and jurisdiction-specific; check current Apple/Google policy before advising
- Platform commission (often 15–30%) applies to qualifying digital sales

## Common Traps

- Testing with real money instead of sandbox / license testers
- Leaving transactions unfinished → delayed grant or auto-refund risk
- Hard-coding local prices instead of fetching store localized prices
- Missing a transaction observer / purchase update listener → lost out-of-app purchases
- Granting entitlements before server verification
- Ignoring grace-period and billing-retry states
- Weak paywall clarity that collapses conversion regardless of price
- Shipping without trial/start/cancel/refund metrics
- Omitting restore → App Review rejection risk
- Ignoring Family Sharing edge cases

## Safety

- Never commit `.p8`, Play service-account JSON, shared secrets, or raw receipts into git
- Prefer env vars / secret stores for API keys
- Keep webhook handlers idempotent and audit-logged
- Treat client purchase success as untrusted until server verification completes
