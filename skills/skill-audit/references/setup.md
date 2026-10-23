# Setup — Skill Audit

Read this when `<state_root>/` is missing or empty.

## First-Time Setup

### 1. Resolve and create the state root

Resolve `<state_root>` with the State location rules in `SKILL.md` first.
Never create a directory whose name is the literal string `<state_root>`.

Tell the user what will happen:

- Preferences, the audit log, optional custom greps, and quarantine folders live only under `<state_root>/`
- No secrets are required for this skill
- Legacy Clawic paths are migrated on first write, not left as a second source of truth

Create the workspace only when durable state is needed:

```bash
mkdir -p "$RESOLVED_STATE_ROOT/quarantine"
```

### 2. Seed `config.yaml`

Write defaults the first time, then ask only about preferences the user cares about:

```yaml
strictness: standard   # or paranoid
log_verdicts: true
sweep_scope: []        # empty = all detected agent skill directories
report_format: full    # or summary
```

### 3. Seed `audit-log.md`

Create an empty log with a header so update diffs and sweeps have a baseline file:

```markdown
# Skill Audit Log

| Date | Slug | Version | Location | Verdict | Notes |
|------|------|---------|----------|---------|-------|
```

### 4. Optional `patterns.md`

Create only after an incident teaches a new grep (`references/incident.md` Close Out). Keep it as extra mechanical checks that run beside `references/checks.md`.

### 5. Migrate legacy locations

If data exists under `~/Clawic/data/skill-audit/`, `~/skill-audit/`, or
`~/clawic/skill-audit/`, move it into the resolved `<state_root>/` and say in
one line that you moved it and from where. Do not keep writing to both trees.

### 6. First conversation

1. Confirm what is being audited (path, registry install, update, sweep, or incident).
2. Run Pass 1 at minimum; escalate to the matching Quick Reference row.
3. Deliver a `references/report.md` verdict; append to the audit log when `log_verdicts` is on.
