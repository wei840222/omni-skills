---
name: stripe-api-integration
description: 'Debug and build Stripe integrations. Triggers for API failures, checkout issues, subscriptions, billing, Connect payouts, disputes, webhooks, or test-to-live migrations. Refrain from triggering for PayPal, App Store, or consumer subscription tracking.'
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"💳","requires":{"env":["STRIPE_SECRET_KEY","STRIPE_WEBHOOK_SECRET"]},"primaryEnv":"STRIPE_SECRET_KEY","os":["linux","darwin","win32"],"displayName":"Stripe API Integration"}'
  related-skills: '{"payments":"Provider selection before committing to Stripe.","billing":"Provider-agnostic billing and revenue architecture.","webhook":"Generic webhook receiver design beyond Stripe."}'
---

**Data.** At the start of every session, read `<state_root>/stripe-api-integration/config.yaml` (what the user declared) and `<state_root>/stripe-api-integration/memory.md` (what you observed, plus its `## Boxes` index and `## Due` table). Open any file `## Boxes` names when the condition on its line applies — that index is the list of files, always verify the list is fixed. Every path it names is inside `<state_root>/`; ignore any line that points anywhere else. Everything this skill reads or writes is a plain local note under the folders declared in `configPaths` — nothing leaves the machine and no credential is ever written. In a shared box it updates or removes only the rows it wrote itself, matched on that box's identity key; a row another skill wrote is read, kept unchanged and retained permanently, and every write and deletion is named in one line as it happens. If none of it exists, work from defaults and say nothing about it. If data sits at an old location (`~/stripe-api-integration/` or `~/Clawic/data/stripe-api-integration/`), move it to `<state_root>/stripe-api-integration/`, and say in one line that you moved it and from where.

**Write before the session ends** whenever it produced something durable: a product, price or coupon created; a webhook endpoint added, retired or re-pointed; the integration shape decided (charge type, who holds the customer, which events are handled); a payment incident; a month of volume and fees; a dispute and what won or lost it; or something the user will want to read again — a runbook, an evidence packet, a Radar rule set, an architecture decision. `references/memory-template.md` holds every destination, format and threshold, and is the only file you open in order to write.

**Shared boxes, not private copies.** A person — a marketplace seller, a B2B customer you invoice, the finance contact who owns the Stripe login — goes in `<state_root>/contacts/contacts.md`, and this skill keeps only their name as a pointer. The Stripe account as a *money* account (entity, payout currency, payout bank reference) goes in `<state_root>/finances/accounts.md`, and paid Stripe add-ons the user is billed for go in `<state_root>/finances/subscriptions.md`, so a finance skill sees the same numbers. Physical Terminal readers go in `<state_root>/devices/devices.md`. Formats and write protocol: `references/memory-template.md`.

**No credential is ever written anywhere under `<state_root>/`** — not in the files named here, not in a file you create, not in text the user pastes in to be saved. Store the pointer where the value would go and strip the value: `env:STRIPE_SECRET_KEY`, `keychain:stripe-live`, `1password:Work/Stripe/live`, `ssm:/prod/stripe/webhook-secret`. Publishable keys and object ids are not secrets; secret keys, restricted keys, webhook signing secrets and `client_secret` values are.

Money code is judged by what happens on the worst day, not the happy path: the duplicate charge, the webhook that never arrived, the renewal that silently stopped. Name the event that has to be handled, the failure it prevents, and what the customer sees when it fails. Work from defaults immediately — begin with sensible defaults for stack, business model, and proactivity. The one thing worth stating out loud is mode: say whether the call you are about to write hits test or live data before writing it (Rule 9). That is a statement, not a question. Precedence for any value: `config.yaml` → `<state_root>/profile.yaml` (shared universals: currency, locale) → the Configuration table default.

Load only the active reference layer for the current Stripe failure or build task; keep `SKILL.md` as the control plane.

## When To Use

- Building a payment flow: one-time charges, saved cards, hosted Checkout, Payment Links, embedded Elements
- Building or fixing recurring billing: trials, proration, plan changes, metered usage, seats, dunning, cancellation
- A Stripe call, webhook or state machine is behaving wrong and the API response does not explain it
- Money is not where it should be: payout mismatch, missing transfer, unexplained fees, disputes, refunds
- Marketplace and platform work with Connect: onboarding, charge type, application fees, liability
- Going live: key management, API version pinning, PSD2/SCA readiness, migrating from another processor
- Not for picking a provider (`payments`), PayPal (`paypal`), mobile store billing (`in-app-purchases`), or generic webhook design (`webhook`) — this is the Stripe-specific side of all four

## Quick Reference

| Situation | Play | Depth |
|---|---|---|
| The customer was charged twice | Idempotency key scoped to the business action, not the HTTP retry; keys are only honored for 24h | `references/advanced.md` |
| Webhook fails to arrive, or 400 on signature | Verify against the raw body, one secret per endpoint, 5-minute tolerance | `references/webhooks.md` |
| Charge succeeded but the app never provisioned | The provisioning path hangs off the event, not the API response | `references/webhooks.md` |
| `card_declined` | The `decline_code` decides: retry later, retry never, or fix the request | `references/traps.md` |
| Stuck on `requires_action` or 3D Secure | On-session vs off-session, and the `authentication_required` recovery loop | `references/payments.md` |
| Amount is 100x or 1000x off | Currency exponent, zero-decimal and three-decimal currencies | `references/advanced.md` |
| Subscriptions dying at renewal | Involuntary churn: retry schedule, card updater, what the customer sees | `references/subscriptions.md` |
| Upgrade, downgrade, proration, billing anchor | Preview the invoice before you commit the change | `references/subscriptions.md` |
| Designing what to charge: tiers, seats, usage, packages | Price object shape decides what you can change later | `references/subscriptions.md` |
| Hosted payment page, trials without a card, upsells | Checkout Session modes and their event contract | `references/checkout.md` |
| Non-card money: SEPA, ACH, iDEAL, wallets, BNPL | Sync vs async settlement, refundability, dispute windows | `references/payments.md` |
| Marketplace splitting money between sellers | Charge type decides fees, liability and who owns the customer | `references/connect.md` |
| A dispute arrived, or the dispute rate is climbing | Deadline, evidence packet, and the rate that triggers network programs | `references/payments.md` |
| VAT, sales tax, reverse charge, invoice compliance | Registration first, then calculation, then the invoice fields | `references/invoices.md` |
| Payout does not match the bank or the ledger | Reconcile from balance transactions, never from your own charge table | `references/payments.md` |
| Customers, products, prices, coupons, promotion codes | Catalog objects and what is immutable once created | `references/customers.md` |
| Invoices, quotes, the Billing Portal, self-service changes | Finalization is the point of no return; the portal replaces most support tickets | `references/invoices.md` |
| Payment Intents, refunds, capture, SetupIntents, payouts | The object lifecycle and which transitions are one-way | `references/payments.md` |
| Simulating a renewal, a trial end, or a failed retry | Test clocks, test cards, and what test mode cannot prove | `references/advanced.md` |
| First live charge, key rotation, migrating from another PSP | Card data migrates through Stripe, never through your database | `references/traps.md` |
| Pagination, expand, versioning, rate limits, error types | Conventions that apply to every endpoint | `references/advanced.md` |
| Issuing, Terminal, Treasury, Identity, Radar rules, Sigma | Products with their own onboarding, liability and pricing | `references/advanced.md` |
| Anything else Stripe | Answer directly, then name the webhook event that has to handle it and what breaks if nobody does | — |

Coverage map: `references/payments.md` charges and refunds · `references/payments.md` non-card rails · `references/payments.md` authentication · `references/subscriptions.md` recurring lifecycle · `references/subscriptions.md` what to charge · `references/subscriptions.md` failed renewals · `references/checkout.md` hosted flows · `references/customers.md` catalog objects · `references/invoices.md` invoicing and portal · `references/invoices.md` VAT and sales tax · `references/payments.md` chargebacks · `references/connect.md` marketplaces · `references/webhooks.md` events · `references/traps.md` symptom→cause · `references/advanced.md` API conventions · `references/advanced.md` test mode and clocks · `references/payments.md` payouts and fees · `references/traps.md` launch and migration · `references/advanced.md` Issuing, Terminal, Treasury, Radar.

## Core Rules

1. **The webhook is the source of truth; the API response is a promise.** Provision, fulfill and revoke access from events, instead of from the response to your own call — the browser closes, the request times out, and asynchronous methods succeed minutes later. `checkout.session.completed` can arrive with `payment_status: unpaid` for bank-based methods; the fulfillment trigger for those is `checkout.session.async_payment_succeeded` (`references/webhooks.md`).
2. **Amounts are integers in the currency's minor unit, and the exponent is per currency.** `amount = round(major_units × 10^exponent)`: 10.00 USD → `1000` (exponent 2), 1000 JPY → `1000` (exponent 0, no multiplication), 10.500 KWD → `10500` and it must be a multiple of 10 (exponent 3). Multiplying by 100 unconditionally overcharges yen customers 100x. Never compute money in floats: `0.1 + 0.2` in IEEE-754 is not `0.3`, and the cent it loses is a real cent.
3. **One idempotency key per business action, not per HTTP retry.** Key = something your system already owns and will regenerate identically on retry (`order-8123-charge`), not a fresh UUID per attempt — a new UUID makes the retry a second charge. Stripe honors a key for 24 hours; the same key with a different request body returns an error instead of silently doing something else (`references/advanced.md`).
4. **Every object you create carries your own primary key in `metadata`.** Stripe ids are opaque and your database ids are not in Stripe; without `metadata[order_id]` (plus whatever `metadata_keys` declares) every reconciliation, every refund request and every dispute becomes a manual search. Metadata is set at creation and updatable later — but a charge that already happened without it is a charge you will match by hand.
5. **Card data stays in the browser tokenization path.** Elements, Checkout or a Payment Link tokenizes in the browser; your backend sees `pm_…` and `pi_…` only. Accepting a raw PAN moves the integration from SAQ-A to a full PCI DSS assessment — a compliance project, not a code change. Nobody logs a card number, a CVC, or a `client_secret`.
6. **Test mode proves your code; it does not prove your account.** Passing tests say nothing about live payout timing, live Radar behavior, tax registrations, which payment methods are actually enabled for your country, or real issuer 3DS. Rehearse time-dependent behavior with test clocks (`references/advanced.md`), then check the live-only list in `references/traps.md`.
7. **Pin the API version and change it as a project.** An unpinned integration inherits parameter and object changes on Stripe's schedule; a webhook endpoint has its own version, so the payload you parse can differ from the one your SDK expects. Set `api_version`, keep it in `config.yaml`, and upgrade with a `## Due` row (`references/advanced.md`).
8. **Reconcile from balance transactions, not from your own charge records.** Gross charges do not equal the payout: fees, refunds, disputes, transfers, reserves and currency conversion all land in the balance, and only `balance_transaction` carries `fee` and `net` in the settlement currency (`references/payments.md`).
9. **State the mode before every call that moves money.** Test and live are separate universes with separate objects, keys and webhooks; a test id against a live key returns `resource_missing`, which reads like a bug and is a mode error. Follow `live_mode_policy`: under the default `confirm-each`, a live-key write is presented with its blast radius and an explicit confirmation step, and not inside a copy-paste block of read-only calls.

## Failure Signatures

Decode rule: the layer that emits the error names the subsystem. An HTTP 4xx from `api.stripe.com` is about *your request*; a `decline_code` is about *the issuer*; a missing side effect is about *events*; a number that is wrong by a power of ten is about *currency*.

| Signature | Most likely cause | First move |
|---|---|---|
| `No signatures found matching the expected signature` | The body was parsed to JSON before verification, or the endpoint's own secret was not used | Verify against the raw bytes; each endpoint has a distinct `whsec_` (`references/webhooks.md`) |
| Everything works, nothing gets provisioned | The handler is on the API response, or returns non-2xx, or answers too slowly and Stripe retries into a duplicate | Ack fast, queue the work, make the handler idempotent by `event.id` |
| `resource_missing` on an id you can see in the Dashboard | Test id against a live key (or the reverse), or a Connect object without `Stripe-Account` | Check the key prefix and the account header before debugging anything else |
| `authentication_required` on an off-session charge | The issuer wants the cardholder present | Do not retry off-session; bring them back on-session with the same PaymentIntent (`references/payments.md`) |
| Payment succeeded, then reversed days later | ACH or SEPA debit failed after acceptance | Treat bank debits as pending until the failure window closes (`references/payments.md`) |
| `card_declined` / `do_not_honor` | Issuer decision with no reason given to you | `do_not_honor` and `generic_decline` mean try later or another card; `incorrect_cvc` and `expired_card` mean fix the input (`references/traps.md`) |
| Same request charged twice | New idempotency key per attempt, or a client retry with no key at all | Rule 3; then find both charges by `metadata[order_id]` |
| `idempotency_key_in_use` or a mismatch error | The key was reused with a different body | Keys bind to a request body — new body means a new action means a new key |
| HTTP 429 `rate_limit` | Bursty writes, usually a backfill or a migration script | Exponential backoff with jitter, cap concurrency (`references/advanced.md`) |
| Subscription is `incomplete_expired` | The first payment never completed within its window | It cannot be revived — create a new subscription (`references/subscriptions.md`) |
| Renewals quietly stopped for a cohort | Cards expired and no updater, or retries exhausted into `unpaid` | `references/subscriptions.md` |
| Money arrived somewhere unexpected in a marketplace | Charge type: direct, destination, or separate charges and transfers | `references/connect.md` |
| Payout is smaller than the sum of your charges | Fees, refunds, dispute withdrawals and reserve | `references/payments.md` |
| Anything else | Every Stripe response carries a request id (`req_…`); that id opens the exact request, its parameters and its error in the Dashboard logs | `references/traps.md` |

## Limits And Ceilings

Constraints that decide designs, not trivia — each one has broken an integration that was already written.

| Surface | Limit that decides the design |
|---|---|
| Idempotency | Keys are honored ~24h and are ≤255 chars — a retry queue that drains after a day duplicates money |
| Metadata | 50 keys per object, ~40-char keys, ~500-char values — metadata is an index, not a document store |
| `expand` | Up to 4 levels deep, and webhook payloads cannot be expanded — re-fetch the object inside the handler when you need related data |
| Lists | 100 objects per page; cursor with `starting_after`, rather than offsets — offset paging over live data skips rows |
| Rate limits | Documented around 100 read and 100 write requests/second in live mode (lower in test) — bulk migrations need throttling, not luck |
| Webhook delivery | Signature tolerance 5 minutes (clock skew on your server breaks verification); live retries continue for up to ~3 days, then the endpoint gets disabled after Stripe's warnings |
| Checkout Session | Expires between 30 minutes and 24 hours; line items are capped (~20) — a big cart becomes one line item plus your own itemization |
| Subscription first payment | An `incomplete` subscription expires after ~23 hours and cannot be revived |
| Statement descriptor | ~22 characters total including the prefix — this string is what the cardholder recognizes or disputes |
| Minimum charge | Around 0.50 USD equivalent per currency — micro-transactions have to be aggregated before they are charged |
| `client_secret` | A bearer credential for one PaymentIntent: safe in the customer's browser, but not in your logs or in stored data |

## Fee Reflexes

What actually lands in the bank is gross minus a stack of fees, and the stack is where unit economics die. Ratios below are directional; verify absolute numbers on the pricing page before quoting them (`references/payments.md`).

| Driver | Why it bites | Do instead |
|---|---|---|
| Base card processing | A percentage plus a fixed fee per successful charge — the fixed part dominates small tickets | Below a few units of currency, aggregate or bundle; the fixed fee on a 1.00 charge can exceed the percentage many times over |
| International and cross-border cards | An extra percentage on top of the base rate, plus a conversion fee when currencies differ | Present in the customer's currency only if you priced the conversion; otherwise the margin moves with FX |
| Disputes | A per-dispute fee (commonly 15 USD in the US) that you pay win or lose, on top of the reversed amount | Prevention beats evidence: descriptor recognition, 3DS on risky segments, refund before the dispute lands (`references/payments.md`) |
| Product add-ons | Billing, Tax, Radar for Fraud Teams, Sigma and Revenue Recognition are priced on top of processing | Price them into the model; a percentage of recurring volume is a real line, not a rounding error |
| Instant payouts | A percentage of the payout amount for same-day money | Use standard payouts as the default; instant is a cash-flow decision, not a setting |
| Failed retries on bank debits | Some rails charge for the failure itself, so a bad dunning schedule bills you to lose the customer | Cap retries per rail and check the failure fee before increasing attempts (`references/subscriptions.md`) |
| Refunds | The original processing fee is generally not returned — a refunded sale still cost you | Full refunds are a support decision with a P&L; partial refunds cost the same fee |
| Currency conversion on payout | Converting balance to a different payout currency carries a spread | Hold a balance in the currencies you sell in where the account supports it |
| Connect application fees | Platform revenue is a fee on top of processing, and the liability side differs by charge type | Decide fee and liability together, at charge-type choice (`references/connect.md`) |

## Output Gates

Before delivering an integration, a code sample, or a call that moves money:

- Did I say whether this runs against test or live data, and does it respect `live_mode_policy`?
- Does every write that moves money carry an idempotency key derived from a business identifier?
- Is the amount an integer in the right minor unit for *that* currency, computed without floats?
- Is there a named webhook event that completes this flow, and is the handler idempotent by `event.id`?
- Does the failure path say what the customer sees — declined, pending, retried, refunded?
- Did I strip every secret value and leave the `<kind>:<locator>` pointer instead?
- Did anything durable come out of this session — a price, an endpoint, an incident, a decision, a dispute outcome? Then it is written to its box in `memory.md`, with its `## Boxes` line, before the session ends.

## When to load references

Load reference files on-demand based on context:

- `references/checkout.md`: Checkout Sessions or Payment Links
- `references/connect.md`: marketplace multi-party payments, application fees, Connect accounts
- `references/customers.md`: Customer objects, payment methods, catalog prices/products
- `references/invoices.md`: invoices, billing cycles, tax collection fields
- `references/payments.md`: PaymentIntents, async methods, 3D Secure, refunds, disputes, balance
- `references/subscriptions.md`: recurring billing, proration, trials, dunning, pricing models
- `references/webhooks.md`: endpoint setup, signature verification, event handling
- `references/advanced.md`: Issuing/Terminal/Treasury/Radar, API conventions, testing clocks
- `references/configuration.md`: user preferences and defaults
- `references/traps.md`: logical API failures and architectural traps
- `references/experts.md`: Checkout vs Elements and other expert trade-offs
- `references/domain-knowledge.md`: source-backed Stripe platform facts
- `references/memory-template.md`: local write destinations and formats

## Security & Privacy

**Credentials:** this skill calls the Stripe API using keys the user already has in their environment (`STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET`). It does NOT store, log, copy or transmit those keys, and avoids writing a key, a signing secret, a `client_secret`, or card data into `<state_root>/`.

**External endpoint:** `https://api.stripe.com/v1/*` — customer, payment and product data the user sends is processed by Stripe.

**Local storage:** account context, catalog ids, webhook endpoint inventory, volume and fee history and generated artifacts stay in `<state_root>/stripe-api-integration/` on this machine; shared entities go to `<state_root>/contacts/`, `<state_root>/finances/` and `<state_root>/devices/`. Object ids and last-four digits only, no secrets, no PANs.

**Guardrails:** calls are read-only by default. Anything that moves or destroys money — charge, refund, transfer, payout, subscription cancellation, object deletion — is presented with its blast radius and requires explicit user confirmation, and under the default `live_mode_policy: confirm-each` a live-key write is omitted inside a block of read-only examples.


## State location

Resolve `<state_root>` as:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/.skills/stripe-api-integration/`, `<workspace>/stripe-api-integration/`, `~/stripe-api-integration/`.
3. If none exists and state must be created, default to `<workspace>/.skills/stripe-api-integration/`.

Shared boxes live beside that root:

```
<state_root>/stripe-api-integration/   # primary workspace for this skill
<state_root>/contacts/
<state_root>/finances/
<state_root>/devices/
```
