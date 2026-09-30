# Verification (Faithfulness → Coverage)

Scope: auditing a draft summary against the source. Order is mandatory.

## Pass 1 — Faithfulness (summary → source)

For each summary sentence:

- Point to a supporting span.
- Check numbers, negations, hedges, quantifiers, dates, attribution character-for-character where required.
- Unsupported claim → cut or demote to "not stated in the source".

## Pass 2 — Coverage (source → summary)

From the source side:

- Were decision-changing items kept (money, risk, dissent, deadline, limitation)?
- If cut, does the omission note name them when `omission_note` requires?

## When to run

Governed by `verify_pass`: `always` | `long-only` (~≥2000 source words) | `never` (still run on user challenge).

## User challenge loop

On "you missed X" / "that isn't in the source": run both passes in order; patch the summary; record durable corrections in memory Boxes when appropriate.
