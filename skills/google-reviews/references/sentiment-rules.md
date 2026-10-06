# Sentiment Rules — Google Reviews

Use deterministic heuristics first, then optional model refinement. Always keep evidence attached.

## Classification baseline

- `positive`: clear praise, favorable outcome, no unresolved complaint
- `neutral`: factual note without strong positive or negative tone
- `negative`: clear dissatisfaction, unresolved issue, or strong warning
- `mixed`: explicit positives and negatives in the same review

## Theme taxonomy

Apply one or more themes when evidence exists:

- service-quality
- delivery-or-wait-time
- pricing-value
- product-quality
- staff-behavior
- refund-or-resolution
- listing-accuracy
- safety-or-trust
- hours-or-availability

## Alert triggers

Flag high urgency when any condition is true:

- Negative review includes legal, fraud, safety, discrimination, or health claims
- 7-day negative ratio rises above the configured threshold
- Average rating drops sharply versus baseline in a single refresh window
- Multiple independent reviews converge on the same unresolved theme within the cooldown window

## Confidence guidance

- High: consistent multi-review evidence with adequate volume and recent timestamps
- Medium: clear direction but limited volume or mixed sources
- Low: single review, stale sample, or conflicting source modes

State confidence next to the conclusion. Prefer "provisional" language when volume is thin.
