# Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/ecommerce/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| platform | shopify \| woocommerce \| bigcommerce \| magento \| custom \| headless \| none | none | Dialect of every code example, app-vs-code recommendation, and migration advice; while unset, name the platform assumed before emitting platform-specific code (`platforms.md`) |
| business_model | dtc \| marketplace-first \| wholesale \| subscription \| hybrid | dtc | Which spokes lead an answer, and whether retention, buy-box or net-terms guidance applies |
| home_market | text (country code) | none | Tax regime, consumer-law windows, carrier set and currency assumptions; while unset, name the jurisdiction assumed before any legal or fiscal answer (Rule 8) |
| currency | text (ISO code) | from `profile.yaml`, else USD | Currency of every price, fee and margin figure, and the unit written into shared boxes |
| psp | text (processor name) | none | Fee math, decline-code triage, dispute workflow and webhook examples in `payments.md` |
| monthly_orders | number (orders/month) | 300 | Scale band: sync interval, 3PL break-even, automation vs manual process, support staffing (`fulfillment.md`, `support.md`) |
| target_margin_pct | number (0-100) | 40 | Floor that gates discounts, marketplace entry and ad bids (Rule 4) |
| max_discount_pct | number (0-100) | 20 | Ceiling on any promo, code, or service compensation before it needs explicit approval (`pricing.md`, `support.md`) |
| target_ltv_cac | number (ratio) | 3 | Spend ceiling in Rule 5 and the go/no-go on a new channel |
| fraud_posture | loose \| balanced \| strict | balanced | Review thresholds, 3DS routing and auto-cancel rules in `fraud.md` |
| pci_scope | hosted-fields \| redirect \| self-hosted-fields | hosted-fields | How much of the payment path may be touched at all, and which SAQ the store is answering (`payments.md`) |
| bulk_change_confirm | bool | true | Whether bulk price, catalog, inventory or customer-wide operations are emitted behind an explicit confirmation |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Integrations** — the chosen ESP, reviews app, subscription app, helpdesk, 3PL, tax engine, analytics stack, feed manager (the choice, never credentials) — affects which integration path every answer assumes
- **Conventions** — SKU and variant naming, product-title format, collection structure, URL and redirect patterns, discount-code grammar, order-number scheme — affects `catalog.md` and generated artifacts
- **Platform and markets** — countries shipped to, languages, currencies presented, DDP vs DAP posture, marketplaces in use — affects `tax.md`, `fulfillment.md`, `marketplaces.md`
- **Safety posture** — appetite for auto-refunds and no-return refunds, fraud auto-cancel, whether destructive bulk operations are emitted at all — affects Output Gates, `returns.md`, `fraud.md`
- **Brand and policy** — discount philosophy (never discount vs always-on promo), tone of customer replies, return generosity, urgency tactics allowed — affects `support.md`, `conversion.md`, `pricing.md`
- **Restrictions** — categories never sold, channels ruled out, claims that must not be made, regulated product rules — affects `catalog.md` and `acquisition.md`
- **Work order** — which valid sequence the store runs: margin gate before creative work or after, staging-then-production versus direct edits for bulk price and catalog changes, whether a promo needs a CM sign-off before it is built, which reviews gate a launch or a replatform cutover — affects the step order of the workflows in `pricing.md`, `catalog.md`, `platforms.md` and `peak.md`
- **Cadence** — metrics review day, stock count frequency, dead-stock sweep, dispute check, price/COGS refresh, peak planning start — every accepted cadence becomes a row in the `## Due` table of `memory.md`
- **Output register** — code-first vs explanation-first, whether every answer carries the margin figure, dashboard vs prose — affects the shape of every reply
