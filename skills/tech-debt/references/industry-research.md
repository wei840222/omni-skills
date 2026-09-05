# Industry Research on Technical Debt

The concept of technical debt was originally coined by Ward Cunningham to describe the trade-off between quick, imperfect code and long-term maintainability. Martin Fowler further developed the "Technical Debt Quadrant," distinguishing between reckless vs. prudent and deliberate vs. inadvertent debt.

Key modern insights:
- **Refactoring vs Rewriting**: Industry consensus strongly favors incremental refactoring (e.g., Strangler Fig pattern) over full rewrites, as rewrites often suffer from the "Second-System Effect" (Brooks) and take longer than expected, halting feature delivery.
- **Continuous Amortization**: High-performing teams continuously pay down debt (allocating ~15-25% of capacity) rather than halting delivery for "debt sprints."
- **Metrics vs Behavior**: While complexity metrics (cyclomatic complexity) provide indicators, behavioral signals like rising cycle times, high defect rates in specific modules, and team fear are the most reliable prioritizers for debt repayment.
