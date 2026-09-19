# Scale — Domain Knowledge

Load this file when verifying bottleneck diagnosis, architecture split defaults, or rollout-control claims against primary sources.

## Theory of Constraints and bottleneck focus

- Scale planning starts by naming the dominant constraint, not by adding capacity everywhere. Work the constraint until it is no longer the limiter, then re-scan.
  - Goldratt, Eliyahu M. — Theory of Constraints overview — https://en.wikipedia.org/wiki/Theory_of_constraints
  - Goldratt, Eliyahu M. — *The Goal* (ToC narrative framing for throughput, inventory, and operational expense) — https://en.wikipedia.org/wiki/The_Goal_(novel)

## Architecture defaults before service splits

- Prefer a modular monolith until independent deployability, team ownership, or failure isolation is proven necessary. Trend-driven microservice splits add coordination cost without guaranteed throughput gains.
  - Fowler, Martin — MonolithFirst — https://martinfowler.com/bliki/MonolithFirst.html
  - Fowler, Martin — Microservices prerequisite caution (when distribution pays for itself) — https://martinfowler.com/articles/microservices.html

## Delivery throughput and queueing

- Deployment and org scale often fail on queueing, batch size, and feedback delay before raw machine capacity. Shorten the critical path and reduce WIP before large rewrites.
  - Forsgren, Humble & Kim — *Accelerate* / DORA research framing (throughput, stability, and capability model) — https://dora.dev/research/
  - Reinertsen, Donald G. — principles of product development flow (queueing and batch-size economics) summary via — https://en.wikipedia.org/wiki/Product_development#Lean_product_development

## Safety notes

- Do not store secrets, customer PII, or production credentials in `<state_root>/scale/`.
- Treat cost, incident severity, and team load as hard guardrails; pause expansion when thresholds breach for consecutive periods.
