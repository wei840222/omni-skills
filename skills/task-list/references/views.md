# Views and ordering

## Buckets

- `Inbox`: captured but not ready to execute.
- `Today`: should be visible now.
- `Upcoming`: dated work not yet ready for Today.
- `Anytime`: active work with no current date pressure.
- `Someday`: intentionally deferred ideas.
- `Waiting`: delegated or externally blocked work.
- `Done`: completed work awaiting archive or review.

## Ordering

Within a view, order overdue due dates, due today, reached start dates, high priority, intentional manual order, then oldest unresolved change. Preserve prior visible order for a complete tie.

Overdue work is a risk signal. Surface it and let the user promote, defer, renegotiate, or drop it; do not automatically flood Today. Show recurrence only at its next intended appearance, and expose the owner, blocker, and chase date for Waiting.
