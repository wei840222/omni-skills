# State Management — Personal Finance Tracker

## Architecture

Local workspace is optional and only created with user consent after `<state_root>` resolution in `SKILL.md`.

```text
<state_root>/
├── memory.md        # High-signal money context and review cadence
├── accounts.md      # Balances, account roles, sync notes
├── recurring.md     # Bills, subscriptions, annual charges, due dates
├── plans.md         # Debt payoff, savings, cut list, next actions
└── reviews.md       # Weekly and monthly snapshots
```

Create optional files only when the matching feature is needed. Do not pre-expand every template into empty files.

## Security and Privacy

**Data that stays local when the user opts in:**

- Balances, recurring bills, review notes, and debt priorities in `<state_root>/`
- CSV files and local script outputs run on the user's machine

**This skill does NOT:**

- Connect to banks or fintech APIs on its own
- Send transaction data to undeclared external services
- Create local storage without user consent
- Move money, cancel subscriptions, or change accounts automatically

**Guardrails:**

- Store only high-signal summaries; exclude full credentials or card numbers
- Ask before persisting any sensitive context
- Prefer local CSV analysis to cloud processing
- Scripts accept a real filesystem path for CSV input; they never treat the literal string `<state_root>` as a path
