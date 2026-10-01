# Sources - Glovo

Verified primary sources used for Gate 6 domain accuracy (retrieved 2026-10-01).

## Product and marketplace

- [Glovo — home](https://glovoapp.com/) — multi-category delivery (food, groceries, shops, pharmacies); address-gated discovery; countries listed on the public marketing surface include Spain, Italy, Ukraine, Romania, Georgia, Portugal, Poland, Morocco, and others.
- [Glovo Corporate](https://about.glovoapp.com/) — Spanish tech company; multi-category marketplace connecting customers, businesses, and couriers across Europe, Central Asia, and Africa; public metrics cited on the corporate site (countries, monthly couriers, partner businesses).

## Legal and privacy

- [Glovo Legal Terms and Conditions](https://glovoapp.com/en/legal/terms/) — contractual terms for platform use, orders, and account obligations.
- [Glovo Privacy](https://glovoapp.com/en/legal/privacy/) — personal-data handling for addresses, orders, and account activity (same legal hub as terms on the public site).

## Operating implications retained in this skill

1. **Address first** — public UX requires an address/city before nearby inventory is meaningful.
2. **Multi-category** — food is not the only vertical; groceries, shops, and pharmacies are first-class.
3. **Real purchase surface** — checkout uses the user's own session cookies/payment methods; the skill must not invent stock, ETA, or promo validity.
4. **No public developer order API relied on** — this skill is browser/app-session oriented; it does not assume a public order-placement API for agents.

When region-specific fees, ETA, or promo rules matter, re-read the live Glovo page for that address rather than copying marketing numbers into memory.
