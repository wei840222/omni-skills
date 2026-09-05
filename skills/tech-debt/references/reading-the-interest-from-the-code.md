# Reading the interest from the code

The #1 reads the interest from behavior, not from a complexity dashboard. Metrics are lagging; behavior is current.

- **Cycle time trending up in one module** = accruing interest. Plot change-to-merge time per module; a ~2x rise over a quarter is a loud signal. Throughput on similar-scope features dropping 20-30% over 6-12 months with stable headcount = debt, not morale.
- **Bug concentration**: a module producing bugs at > ~2x its share of code is a hot spot. The bugs are the interest paid in production.
- **Fear signal**: nobody wants to touch a file, or every change to it ships with a "be careful" comment. Fear is the most honest interest gauge; ask the team which files they avoid.
- **Untouched-but-central files**: a core file untouched for 6+ months is latent debt. The team has routed around it; when a feature finally forces a change, the cost surprises everyone.
- **Flaky-test rate**: > ~1-2% of runs flaky erodes trust; engineers start ignoring red, which hides real regressions. Track the rate; when it climbs, test debt is accruing fast.
- **PR size creeping up in one area**: changes that used to be 50 lines are now 300 for the same feature. The abstraction is fighting you; that is architecture debt.
- Complexity metrics (cyclomatic, cognitive, duplication %) flag candidates but do not prioritize. Target the intersection of top change-frequency and top complexity: the bulk of future defects lands there. A high-complexity file nobody touches is not priority debt.
