# Paywall research sources (Gate 6)

Authoritative anchors used to keep paywall guidance aligned with store policy, subscription UX norms, and experiment hygiene. Prefer these over anecdotal growth blogs when rules conflict.

## Apple App Store / subscriptions
- **App Store Review Guidelines** — subscriptions, payments, and dark-pattern constraints via https://developer.apple.com/app-store/review/guidelines/
- **Auto-renewable subscriptions** — offer types, duration, and App Store Connect configuration via https://developer.apple.com/app-store/subscriptions/
- **Offering subscriptions** — trial, introductory, and promotional offer framing via https://developer.apple.com/documentation/storekit/in-app_purchase/original_api_for_in-app_purchase/subscriptions_and_offers/implementing_introductory_offers_in_your_app
- **StoreKit / In-App Purchase overview** — product request and purchase flow context via https://developer.apple.com/in-app-purchase/

## Google Play Billing / subscriptions
- **Google Play Billing** — integration overview via https://developer.android.com/google/play/billing
- **Subscription features / base plans and offers** — Play Console subscription structure via https://developer.android.com/google/play/billing/subscriptions
- **Payments policy** — Play payments and subscription policy constraints via https://support.google.com/googleplay/android-developer/answer/9858738
- **Real-time developer notifications** — subscription lifecycle events via https://developer.android.com/google/play/billing/rtdn-reference

## Monetization UX and experiment practice
- **RevenueCat — Paywalls** — paywall component and remote config patterns via https://www.revenuecat.com/docs/tools/paywalls
- **RevenueCat — Targeting / experiments** — paywall experiment framing via https://www.revenuecat.com/docs/tools/experiments-v1
- **RevenueCat — Charts & metrics** — conversion / trial metrics vocabulary via https://www.revenuecat.com/docs/dashboard-and-metrics/charts
- **Stripe Checkout / Pricing tables** (web SaaS baseline) — hosted pricing presentation patterns via https://docs.stripe.com/payments/checkout and https://docs.stripe.com/payments/checkout/pricing-table

## Consumer clarity
- **FTC — Negative option / subscription marketing** — clear consent and cancellation expectations via https://www.ftc.gov/business-guidance/resources/negative-option-marketing-rule
- **Apple Human Interface Guidelines — In-App Purchase** — purchase UX expectations via https://developer.apple.com/design/human-interface-guidelines/in-app-purchase

## Notes for agents
- Prefer store policy URLs when advising urgency timers, restore-purchase placement, or trial disclosure.
- Distinguish **paywall conversion UX** (this skill) from **billing implementation** (`in-app-purchases`) and generic pricing strategy (`pricing`).
- A/B guidance here is paywall-specific; general experiment design may route to `ab-test` when present.
