# Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/stripe-api-integration/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| stack | node \| python \| ruby \| php \| go \| java \| dotnet \| http | http | Language of every code example; `http` means raw requests with no SDK assumed |
| api_version | text (Stripe version date) | none (account default) | Parameter and object shapes used in examples, and whether metered billing is written with meters or legacy usage records (Rule 7) |
| default_currency | text (ISO 4217) | usd | Currency of every example and quote, and which exponent Rule 2 applies |
| billing_model | one-time \| subscription \| marketplace \| invoicing \| mixed | subscription | Which guide leads an ambiguous question, and which events the webhook baseline includes |
| live_mode_policy | test-only \| confirm-each \| free | confirm-each | Whether a live-key write is emitted at all, and with what confirmation step (Rule 9, Output Gates) |
| metadata_keys | list | [] | Keys attached to every created object in examples (Rule 4) |
| tax_handling | none \| stripe_tax \| external | none | Whether tax parameters appear in create calls and which invoice fields are treated as required (`references/tax.md`) |
| reconciliation_day | number (1-28) | 5 | Day of month for the reconciliation row in the `## Due` table (`references/reconciliation.md`) |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Tooling** — SDK versus raw HTTP, web framework and its raw-body handling, whether the Stripe CLI is available for local forwarding, Elements versus Checkout versus Payment Links — affects every example's shape
- **Conventions** — idempotency-key naming scheme, metadata schema, product and price naming, statement descriptor, invoice numbering — affects generated calls and `customers.md`
- **Platform** — account country and entity, presentment currencies, which payment methods are enabled, payout schedule — affects `payments.md` and `payments.md`
- **Safety posture** — live-mode gating, whether delete and refund calls are emitted at all, approval before anything customer-visible — affects Output Gates and `traps.md`
- **Output format** — full error handling and retries in samples versus the minimal call, comments, framework scaffolding — affects every code block
- **Integrations** — tax engine, analytics and revenue recognition, dunning tooling, fraud tooling, accounting system that consumes payouts — affects `invoices.md` and `payments.md`
- **Restrictions** — PCI scope the user will not exceed, payment methods or regions they refuse, data they will not store — affects `payments.md` and `payments.md`
- **Cadence** — reconciliation day, dispute-rate review, API version upgrade window, key rotation interval — affects the `## Due` table

