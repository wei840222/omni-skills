# Refactor vs rewrite

Default: refactor. Rewrite is the trap that keeps giving. The conditions for rewrite are narrow and all must hold.

- **Refactor** = behavior-preserving restructuring, verified by tests. If behavior changed, it is a rewrite; call it what it is. Without tests you are gambling, not refactoring; build the harness first.
- Small commits, one concern each: rename in one commit, move in another, change logic in a third. A "cleanup" diff touching 50 files is unreviewable and carries bugs that surface weeks later or gets reverted wholesale.
- A refactor is done when the old path is deleted, not when the new one works. Two implementations running in parallel is half-finished debt, not payoff.
- **Strangler fig** = the refactor pattern for a wrong seam: route new traffic to the new implementation, migrate edge by edge, starve the old until you can delete it. Use incremental routing instead of a flag-flip cutover on a live system.
- **Rewrite** only when ALL hold: the architecture is fundamentally wrong (not just messy), the old system can run in parallel as reference and fallback, the team understands the old system's behavior (otherwise you rediscover its hidden requirements in production), and there is a strangler-style migration path.
- The **second-system effect**: the rewrite bloats because now you "know" all the features you should add. Freeze scope to parity-first; new features come after migration, must follow migration.
- A rewrite past ~2x the original build time is failing; cut scope or revert to strangler. The original was built under constraints you no longer respect, which is why rewrites overrun.
- Characterization tests are the bridge: before refactoring legacy code with no tests, pin its current behavior with tests that assert what it does (not what it should do). The #1 writes these before touching; the #1000 refactors blind and fixes the regressions in production.
