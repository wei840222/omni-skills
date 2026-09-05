# Payoff cadence

The #1 amortizes continuously; the #1000 oscillates between "ship only features" and "stop everything to clean up." Both ends of that oscillation are failures.

- Sustained allocation: **~15-25% of capacity on debt, every sprint, indefinitely.** Below ~10% the interest outruns the payoff and debt grows. Above ~30% delivery freezes, the business loses patience, and the swing to 0% follows.
- Use continuous amortization instead of a "debt sprint" or a "hardening sprint" as the primary mechanism. Debt sprints confess that continuous amortization failed; they become the only time debt gets paid, so debt accrues faster between them. Use one to break a crisis, then return to the allocation.
- If a hardening cadence is required: a slot every 4-6 sprints, not every sprint. Every-sprint hardening is continuous amortization with worse optics.
- **Opportunity-based payoff** is the default: when a feature touches a debt-bearing area, pay the debt there as part of the feature estimate. The feature absorbs the cost; the debt shrinks where the work is. Boy-scout rule, scoped to what you touched, not a license to go hunting.
- Reserve the dedicated allocation for high-interest structural debt no upcoming feature will touch. Wait for the feature and the interest compounds; pay it proactively.
- Two hats: when adding function, keep restructuring separate; when restructuring, keep adding function separate. Mixing both in one commit hides the refactor from review and entangles the test surface. Call scope expansion out explicitly; silent "I refactored while I was in there" erodes review trust.
- Tie every payoff to a measurable outcome: cycle time down in module X, flaky-test rate below threshold, dependency off the EOL list. "Cleaner code" is not a measurable outcome and loses every priority conflict with a feature. Most "debt payoff" sprints return 0 measurable gain because they paid debt that wasn't the bottleneck.
