# Research sources and domain guidance

## Definitions and categorization

- [Ward Cunningham's technical-debt metaphor](https://c2.com/doc/oopsla92.html) introduced technical debt as the cost of shipping an imperfect implementation and then paying it back through later refactoring.
- [Martin Fowler, TechnicalDebtQuadrant](https://martinfowler.com/bliki/TechnicalDebtQuadrant.html) distinguishes prudent and reckless debt from deliberate and inadvertent debt. Use the classification to understand origin; prioritize repayment by current cost and risk.

## Incremental change and legacy code

- [Martin Fowler, StranglerFigApplication](https://martinfowler.com/bliki/StranglerFigApplication.html) describes incrementally replacing a legacy system while the existing system continues to operate.
- [Michael Feathers, Working Effectively with Legacy Code](https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055) defines legacy code as code without tests and motivates characterization tests before behavior-preserving changes.

## Operational decision rule

Treat numeric allocation ranges and payoff horizons as planning heuristics rather than universal thresholds. Establish a local baseline for change frequency, lead time, defect concentration, risk, and expected payoff; then review the register on a regular cadence.
