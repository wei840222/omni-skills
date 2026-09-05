# Situations

| Situation | Play |
|---|---|
| PM won't approve cleanup time | Don't ask for a debt sprint. Price the fork: "feature Y is 8 days as-is, 5 days if we first fix auth." The ~15-25% allocation lives inside feature estimates, not a separate ask. |
| A module nobody wants to touch | Measure cycle time + bug rate there. If both trend up it is accruing interest: schedule payoff tied to the next feature that touches it, characterization tests first. |
| Inherited codebase, no tests | Don't refactor first. Ship the next feature behind a characterization test on the behavior you depend on; build the harness incrementally. A big "add tests" effort stalls. |
| New tech lead proposes a rewrite | Default to refactor + strangler. Rewrite only if the seam is fundamentally wrong, the old can run in parallel, and there is a migration path. Parity-first scope. |
| Flaky tests are everywhere | Fix flaky tests first, then reduce suite duration when it drives skips, then add coverage in the riskiest module. Quarantine only with an owner and deadline while the repair proceeds. |
| A dependency is going EOL | Forced payoff with a deadline. Schedule 1-2 quarters before the EOL date; security overrides the queue. Not optional debt. |
| Two teams duplicated the same service | Only pay if both copies are still evolving. If one is frozen, leave it; the coupling from extracting is not worth it. Rule of three before extracting. |
| Register has 200 items, nothing gets paid | It is a graveyard. Triage to ~10-20 items with triggers and carry costs; archive the rest. A long register demoralizes; a short acted-on one pays. |
| "We'll clean it up after launch" | Get a date and an owner in the plan now, or treat the debt as permanent. Without both, the promise is rarely honored. |
| Velocity dropped, team "got slower" | Check whether the drop tracks a module that got harder to change. 20-30% throughput drop on similar scope in 6-12 months with stable headcount = debt, not morale. |
| A refactor PR touches 50 files | Reject or split. One concern per commit; bundled "cleanup" hides bugs and blocks review. |
