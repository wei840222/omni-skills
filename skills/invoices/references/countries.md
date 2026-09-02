# Countries

Jurisdiction defaults belong in `<state_root>/config.yaml` (`country`, retention, filing calendar).

## Operating rule
- While `country` is unset, state the retention and filing assumptions before acting
- Prefer local statutory retention over a global default when config names a country
- For cross-border invoices, record seller country, buyer country, and whether reverse charge applies
- Load `tax-rules.md` for e-invoicing mandates and retention ranges, then override with country-specific config
