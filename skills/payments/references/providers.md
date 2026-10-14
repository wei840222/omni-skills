# Payment providers comparison

Fee percentages change. Treat tables below as **orientation only** and re-open
`references/sources.md` (Stripe / Paddle / Lemon Squeezy pricing pages) before
advising a live fee.

## Full-service processors

### Stripe

- **Best for:** Developers, US/global B2C, marketplaces (Connect)
- **Merchant of record:** No (you are the seller; tax may need Stripe Tax or your own stack)
- **Pros:** Strong docs, broad payment methods, Checkout / Elements / Billing / Connect
- **Cons:** You own more tax/compliance work than MoR providers; international fee variance
- **Docs entry:** Checkout, webhooks, Billing, Connect (see sources)

### Paddle

- **Best for:** SaaS selling globally when VAT/GST outsourcing matters
- **Merchant of record:** Yes (Paddle is seller of record in MoR model)
- **Pros:** Tax handling, invoicing, chargeback operational load reduced vs direct PSP
- **Cons:** Higher all-in fees, less low-level control than Stripe
- **Docs entry:** Paddle Billing product + developer portal (see sources)

### Lemon Squeezy

- **Best for:** Indie / digital products wanting hosted checkout + MoR tax handling
- **Merchant of record:** Yes
- **Pros:** Fast setup, hosted checkout, tax handling
- **Cons:** Fewer deep platform features than Stripe; verify current catalog limits live
- **Docs entry:** Getting started + API guides (see sources)

### PayPal

- **Best for:** Buyer trust in specific demographics/regions; secondary wallet option
- **Merchant of record:** Depends on integration type
- **Pros:** Brand recognition, buyer protection expectations in some markets
- **Cons:** Account-risk operational stories; DX often weaker than Stripe for complex SaaS
- **Hand off deep REST work to** `paypal`

### Gumroad (and similar simple hosts)

- **Best for:** Single digital goods / creators with minimal engineering
- **Pros:** Fastest path to a hosted buy button
- **Cons:** Limited custom app integration depth vs Stripe Billing

## Decision framework

**Prefer Stripe when:**

- You need maximum control, custom access gating, or Connect marketplace splits
- Engineering can own webhooks, tax strategy, and support ops
- You already standardize on Stripe Billing / Tax / Radar

**Prefer Paddle / Lemon Squeezy when:**

- Selling digital/SaaS into many tax jurisdictions with a small team
- MoR (seller-of-record) reduces finance/legal load enough to justify fees
- Hosted checkout is acceptable UX

**Offer PayPal alongside a primary processor when:**

- Cart data shows abandonment without PayPal
- Target markets heavily expect PayPal as a wallet

**Use specialized high-risk processors when:**

- Mainstream PSPs reject the MCC / vertical (adult, some gambling, firearms, etc.)
- Expect higher fees, rolling reserves, and slower underwriting — verify with the processor, not generic blogs

## Fee orientation (example only)

For a notional `$100` card charge, public list pricing often lands near:

| Provider class | Orientation |
|----------------|-------------|
| Stripe online card (US list) | ~2.9% + $0.30 class fees — confirm on stripe.com/pricing |
| MoR (Paddle / Lemon Squeezy) | Higher all-in % + fixed fee — confirm on vendor pricing pages |

MoR fees buy tax/invoicing/chargeback ops. Do not present orientation numbers as
guarantees.

## Local payment methods

Markets may require local rails. Examples (verify coverage per provider):

- **EU:** SEPA, iDEAL, Bancontact, and country-specific methods
- **Brazil:** Pix (and historically Boleto where still relevant)
- **APAC wallets:** Alipay, WeChat Pay, GrabPay (coverage varies)
- **Crypto rails:** niche; treat settlement/risk separately

Stripe documents broad method coverage; always check the target country matrix
before promising a method.

## High-risk industries

Standard processors commonly reject or heavily restrict:

- Adult content
- Cannabis / CBD (jurisdiction-dependent)
- Gambling
- Firearms
- Some nutraceuticals / “high chargeback” verticals

Specialized names often cited: CCBill, Epoch, Segpay, Durango Merchant Services.
Underwriting is case-by-case — do not invent approval odds.
