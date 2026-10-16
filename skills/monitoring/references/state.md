# Monitoring state hygiene

This skill is **stateless by default**. Persist inventory only when the user
asks for continuity across sessions.

## Resolver (must match SKILL.md)

1. Explicit user/host state root wins.
2. Else first existing:
   `<workspace>/monitoring/` → `<workspace>/memory/monitoring/` → `~/monitoring/`.
3. On duplicates, keep highest precedence and report the rest; never merge.
4. On miss, create `<workspace>/monitoring/` only after confirmation.
5. Freeze `<state_root>` for the invocation; pass real paths to scripts — never
   the literal string `<state_root>`.

## Suggested layout

```text
<state_root>/monitoring/
├── inventory.md   # monitor URL, kind (http/tcp/cron), owner, severity
├── compose/       # relative paths or notes for Prometheus/Grafana/Loki stacks
└── pointers.md    # secret-manager names / DSN labels only
```

## Rules

- **Pointer-only secrets:** store `SENTRY_DSN_NAME=ops/sentry-prod`, never the
  DSN value. Same for Grafana admin passwords and cloud keys.
- **No auto-migrate** from `~/Clawic/data/monitoring/` or similar; copy only
  with explicit confirmation and leave a short note in `inventory.md`.
- Skill resources stay under `references/`; do not treat them as mutable state.
- Deleting monitors, silences, or retention policies that discard data requires
  an explicit confirmation gate.
