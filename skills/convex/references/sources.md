# Convex primary-source review (2026-09-28)

## Function boundaries and webhooks

- Convex Docs, Queries — <https://docs.convex.dev/functions/query-functions>. Query contexts provide read access and auth; use validated arguments and bounded results.
- Convex Docs, HTTP Actions — <https://docs.convex.dev/functions/http-actions>. Inbound webhooks use a routed HTTP action; parse and validate the request, call internal mutations for data writes. HTTP actions are not automatically retried on errors.
- Convex Docs, Indexes — <https://docs.convex.dev/database/reading-data/indexes/>. Index fields have an order; indexed equality/range expressions must follow it. A schema index speeds and orders access. Index additions may backfill; index removal on deploy deletes that index.
- Convex Docs, OCC and Atomicity — <https://docs.convex.dev/database/advanced/occ>. Mutation read/write operations commit atomically under optimistic concurrency control; place indexed lookup, deduplication status, and the corresponding write in a single mutation, and handle external calls outside that transaction.
- Convex Docs, Schemas — <https://docs.convex.dev/database/schemas>. Optional fields permit additive rollouts while old records are being migrated; replacing a required field must account for existing documents and clients. A schema index alone is not a SQL `UNIQUE` constraint.
- Stripe Docs, webhook signatures — <https://docs.stripe.com/webhooks/signature>. Verify the `Stripe-Signature` header against the unchanged raw request body and endpoint signing secret; formatting or JSON parsing before verification breaks the signature.

## Audit classification and corrected claims

- Version-sensitive: function types, HTTP action routing and retry semantics, mutation atomicity, schema optional fields, and index expression rules above; verified against the linked official docs on 2026-09-28. The target application's installed Convex SDK version is unknown: verify its lockfile and actual function APIs before use. No precise SDK version or price is asserted.
- Stable domain: tenant authorization, explicit consent for deployment/state persistence, event-ID deduplication, additive data migration. These are operational recommendations, not product guarantees.
- Correction: `skills/convex/references/schema-and-indexes.md` previously suggested generic uniqueness constraints and universal index coverage. The refactor specifies transactional indexed lookups and allows justified bounded scans; verify the concrete application invariant and its tests.
- Correction: `skills/convex/references/operations-playbook.md` now distinguishes inbound HTTP action from internal database mutation and forbids assuming HTTP action retries. Stripe raw-body signature verification is backed by the linked Stripe documentation; for other providers, follow their current contract.
