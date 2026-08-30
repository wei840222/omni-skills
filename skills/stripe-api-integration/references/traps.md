# Stripe Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Fulfilling on the API response | The customer closes the tab, the request times out, or the method settles asynchronously — the money is real and the order is not | Fulfill on the event, ack fast, deduplicate by `event.id` (Rule 1) |
| One webhook endpoint for everything, subscribed to all events | Volume you do not handle, a version you did not choose, and one bad handler poisoning unrelated flows | One endpoint per concern, explicit event list, pinned version (`references/webhooks.md`) |
| `amount * 100` everywhere | Correct for USD and EUR, 100x wrong for JPY and KRW, 10x wrong for KWD and BHD | Look up the exponent per currency (Rule 2) |
| Storing the subscription state in your own database as the truth | Stripe changes state on its own schedule — renewals, retries, cancellations at period end | Your database mirrors; Stripe decides; the events reconcile the two |
| Deleting a price or product to change it | Prices are immutable in the parts that matter, and live subscriptions point at them | Create the new price, migrate subscriptions deliberately (`references/pricing-models.md`) |
| Testing only the happy path in test mode | The expensive bugs are all in renewal, retry, dispute and payout paths | Test clocks for time, deliberate declines for failure (`references/testing.md`) |
| Treating a refund as a dispute cure | Refunding after the dispute is filed loses both the money and the fee, and can look like double repayment | Refund *before* the dispute if the signal arrived early; otherwise fight or accept, choose one or the other, not both (`references/disputes.md`) |
| Retrying an off-session charge that asked for authentication | It will keep failing; the issuer wants the cardholder | Bring the customer back on-session (`references/sca-3ds.md`) |
| Reconciling by summing charges | Ignores fees, refunds, disputes, transfers and conversion; the number does not match the bank | Sum balance transactions per payout (Rule 8) |
| Using the same webhook secret across endpoints or environments | A test event verified by a live handler is an event you invented | One secret per endpoint, resolved from the environment, referenced by pointer instead of stored (`references/go-live.md`) |
| Building a marketplace on direct charges "because it is simpler" | Charge type sets fee flow, dispute liability and who owns the customer relationship — changing it later is a migration | Decide from liability and reporting first (`references/connect.md`) |
| Rotating keys by creating a new one and forgetting the old | The old key keeps working, and it is the one that leaked | Roll, deploy, verify traffic on the new key, then revoke — with a date in `## Due` (`references/go-live.md`) |

