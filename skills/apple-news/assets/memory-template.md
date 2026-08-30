# Apple News memory template

After resolving `<state_root>` and obtaining approval for the write, create or update `<state_root>/memory.md` with this template:

```markdown
# Apple News Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Context
- Preferred reading themes and sources
- Preferred open mode: single link or confirmed set
- Preferred search Shortcut name, if configured

## Command reliability
- Working command path with last verified date
- Known permission prompts and outcomes
- Proven recovery path

## Safety defaults
- Confirmation required before multiple opens: yes/no
- Confirmation required before Shortcut execution: yes/no
- Preferred preview detail before launch

## Notes
- Explicitly stated user preferences
- Confirmed failures and proven fixes
```

Update `last` whenever command reliability or safety defaults change. Preserve earlier notes unless the user asks to remove them.
