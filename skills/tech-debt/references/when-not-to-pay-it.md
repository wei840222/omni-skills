# When not to pay it

The #1000 pays debt to feel clean; the #1 pays it to unblock a specific future move or to stop a measured bleed. Refuse to pay when:

- The code is slated for deletion or rewrite within ~2 quarters. Verify it is staying first; paying down debt in code you are about to delete is pure waste.
- The debt has no measurable interest (nobody touches the area, no bugs, no fear). Park it; the payoff cost exceeds the lifetime interest. Revisit on the prune cadence.
- You cannot articulate the trigger or the outcome. "It is messy" is not a trigger; "cycle time here is 2x and rising" is. No trigger = no payoff.
- The fix is a "clean slate" rewrite with no parallel-run plan. The rewrite trap: the old system keeps the lights on while the new one bloats (second-system effect), and you ship neither.
- The fix is to disable a flaky test. That converts test debt into hidden production debt; the regression the test was catching now ships. Fix the test, or quarantine it with a ticket and a deadline.
- You are gold-plating: abstracting before you have three concrete examples, or generalizing a path with one caller. Premature abstraction is itself debt; it freezes a design before you know its shape.
