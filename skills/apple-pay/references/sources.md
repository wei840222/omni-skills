# Sources - Apple Pay

Verified at handoff time (2026-10-03). Prefer these URLs over memorized API details.

## Agent Skills packaging

| Claim | Source | URL |
|-------|--------|-----|
| Frontmatter, progressive disclosure, packaging rules | Agent Skills Specification | https://agentskills.io/specification |
| Reference validator behavior | skills-ref | https://github.com/agentskills/agentskills/tree/main/skills-ref |

## Apple Pay platform

| Claim | Source | URL |
|-------|--------|-----|
| Product overview and platform entry | Apple Pay | https://developer.apple.com/apple-pay/ |
| PassKit framework | Apple Developer Documentation | https://developer.apple.com/documentation/passkit |
| Apple Pay on the Web | Apple Developer Documentation | https://developer.apple.com/documentation/apple_pay_on_the_web |
| Server setup for Apple Pay on the Web | Setting Up Your Server | https://developer.apple.com/documentation/apple_pay_on_the_web/setting_up_your_server |
| `PKPaymentRequest` native request object | PassKit | https://developer.apple.com/documentation/passkit/pkpaymentrequest |
| Merchant identifier creation | Apple Developer Account Help | https://developer.apple.com/help/account/configure-app-capabilities/create-a-merchant-identifier |
| Wallet/Apple Pay documentation cluster | PassKit Apple Pay and Wallet | https://developer.apple.com/documentation/passkit_apple_pay_and_wallet/apple_pay |

## PSP-mediated path (example)

| Claim | Source | URL |
|-------|--------|-----|
| Stripe Apple Pay integration guidance | Stripe Docs | https://docs.stripe.com/apple-pay |
| Stripe Apple Pay product page / entry | Stripe | https://stripe.com/docs/apple-pay |

## Claim map used in this skill

- Merchant validation must run on the server for web → Apple "Setting Up Your Server".
- Native iOS uses PassKit `PKPaymentRequest` → PassKit docs.
- Merchant ID is an Apple account capability → Merchant identifier help.
- PSP path still requires Apple merchant prerequisites plus PSP token mapping → Stripe Apple Pay docs as one verified PSP example.
- Sandbox vs production separation and domain association are release blockers → Apple Pay on the Web + validation checklist in this package.
