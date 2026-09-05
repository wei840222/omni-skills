# Debt types, by interest profile

Each type has a different interest curve and fix order. Know the type before choosing the play.

- **Architecture debt** = the seams are wrong (sync where async belongs, a god module, a boundary that leaks). High interest, structural blast radius, high payoff cost. Fix via strangler fig, always via strangler fig instead of a big-bang refactor. Shows as every cross-cutting feature taking longer than it should.
- **Test debt** = missing, slow, or flaky tests. Compounding interest: each untested change makes the next one scarier; flaky tests erode the trust that makes the suite useful. Fix order: flaky first (they poison the signal), then speed (a suite > ~10 min pushes people to skip), then coverage in the scariest module, not blanket coverage.
- **Dependency debt** = outdated, EOL, or CVE-bearing dependencies. Forced payoff on a deadline. Schedule 1-2 quarters before the EOL/CVE date; this is the one debt security gets to override the payoff queue for.
- **Duplication debt** = the same logic in two places. Mostly flat interest unless both copies are still evolving. Rule of three: copy once (acceptable), twice (smelly), three times (extract). If one copy is frozen, leave it; the coupling from extracting costs more than the duplication.
- **Doc debt** = stale or missing docs on decisions, APIs, onboarding. Low interest, high friction for new hires. Pay opportunistically when you touch the area; a "doc sprint" nobody reads is waste.
- **Dead-code debt** = unused code still in the repo. Near-zero interest but nonzero cognitive cost; every reader pays a tax. Cheapest payoff in the inventory: delete it. If you cannot prove it is unused, add a tombstone (deprecation log) and delete after a quiet release cycle.
