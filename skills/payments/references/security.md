# Payment security

## PCI DSS posture

**PCI DSS** applies when you store, process, or transmit cardholder data.

| Common SAQ path | Typical pattern | Burden |
|-----------------|-----------------|--------|
| SAQ-A | Fully hosted checkout; no card data on your page/server | Lowest self-assessment path for e-commerce |
| SAQ-A-EP | Embedded fields on your origin with tokenization | Longer questionnaire |
| SAQ-D | You handle card data on your systems | Full program; expensive |

**Design goal:** stay on hosted checkout or provider elements so card data never
hits your servers. Confirm current SAQ eligibility with QSA/official PCI materials
via `references/sources.md` — do not invent compliance certificates.

### Hard prohibitions

- Store CVV/CVC anywhere, ever
- Log full PAN
- Store unencrypted card data
- Transmit card data without TLS
- Give broad engineer access to live cardholder data stores

### Required habits

- Hosted fields / Checkout / equivalent tokenization
- HTTPS on every payment surface
- Isolate payment code paths and secrets
- Monitor anomalous auth patterns

## Fraud prevention

### Signals (examples)

| Signal | Typical concern |
|--------|-----------------|
| Billing/shipping mismatch | Medium |
| New free-mail + high AOV | Medium |
| Many fails then success | High |
| High-risk geo + VPN patterns | Elevated (context!) |
| Velocity spikes | High |
| AVS / CVC failures | Elevated |

Tools often used with Stripe: **Radar** and rules; third-party platforms (e.g.
Sift) for multi-channel risk. Manual review queues for high-value first orders.

### 3-D Secure / SCA

Extra cardholder authentication (Visa/MC branded flows). Benefits often include
liability shift when authentication succeeds; costs include friction and some
conversion loss. Enable thoughtfully for higher-risk, high-value, or
regulation-driven (e.g. PSD2 SCA) traffic — confirm market rules in sources.

## Chargebacks / disputes

Customer disputes via issuer. You may lose funds plus fees.

### Common reasons

- Fraudulent use
- Product not received
- Not as described
- Duplicate charge
- Subscription cancel confusion

### Prevention

- Clear billing descriptor
- Delivery / access evidence
- Plain refund policy
- Easy cancel path
- Fast support on billing questions

### Response

Submit evidence packs (delivery, ToS acceptance, usage logs, 3DS proof) inside
the provider deadline. Win rates vary widely; do not promise percentages.

## Refunds

| Situation | Typical stance |
|-----------|----------------|
| Inside stated window / not delivered / duplicate | Full refund path |
| Partial service | Partial refund / credit |
| Outside policy with clear notice | Deny with plain explanation |
| Open dispute already filed | Coordinate — avoid double-credit chaos |

Refund through the provider API/dashboard; document reason; expect some
processor fees to remain non-refundable depending on provider.

## What you may store

**OK (typical):** provider customer IDs, subscription status, payment method brand
+ last4 for display, invoice URLs, internal order IDs.

**Never:** full PAN, CVV, track data, PIN, raw magnetic / chip data.

## Incident response (card data suspected)

1. Contain affected systems
2. Scope: tokens only vs cardholder data
3. Notify counsel / provider as required
4. Follow legal/PCI notification duties — do not improvise public statements alone
5. Rotate keys, fix root cause, document timeline

**Raw card breach implies mandatory reporting paths and material fines risk.**
Another reason to keep PAN completely off your servers.
