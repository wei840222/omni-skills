# Setup - Google Colab

Read this when `<state_root>/` is missing or empty, or when activation preferences are still unsettled.
Keep activation lightweight and useful from the first exchange.

## Operating Priorities

- Answer the immediate notebook task first.
- Confirm when this skill should auto-activate in future conversations.
- Identify whether the user is prototyping, benchmarking, teaching, or preparing production handoff.
- Keep discovery narrow unless additional context directly improves the current outcome.

## First Activation Flow

1. Confirm integration behavior early:
   - Should this activate whenever Colab, notebooks, runtime errors, or model training appears?
   - Should it jump in proactively or only when explicitly requested?
   - Are there situations where it must remain silent?

2. Confirm execution context:
   - read-only planning vs runnable notebook guidance
   - CPU-only constraints vs GPU/TPU tiers
   - strict cost boundaries vs speed-first tradeoffs

3. Confirm data and safety boundaries:
   - allowed sources: Drive, GCS, URLs, or local files
   - sensitive data handling constraints
   - mandatory dry-run before high-cost training

4. If context is approved, resolve `<state_root>` with the skill State location rules, then initialize only what is needed:

```bash
# After <state_root> is resolved to a real path:
mkdir -p "<state_root>"
touch "<state_root>"/{memory.md,notebooks.md,runtimes.md,datasets.md,incidents.md,experiments.md}
chmod 700 "<state_root>"
chmod 600 "<state_root>"/{memory.md,notebooks.md,runtimes.md,datasets.md,incidents.md,experiments.md}
```

Do not hard-code `~/google-colab` when another higher-precedence candidate already exists. Do not treat the literal string `<state_root>` as a filesystem path.

5. If `memory.md` is empty, initialize from `assets/memory-template.md`.

## Integration Defaults

- Start in planning plus dry-run mode unless the user asks for direct execution guidance.
- Prefer one notebook objective at a time until baseline reproducibility is proven.
- Require dependency pins and runtime notes before recommending long jobs.
- Require checkpoint and rollback notes before high-cost runs.

## What to Save

- activation preferences and escalation boundaries
- runtime constraints and approved dependency strategy
- dataset sources, schema assumptions, and validation outcomes
- recurring failure patterns and fixes that worked
- experiment decisions and success criteria

## Guardrails

- Never request secrets in plain chat; use secure mounting patterns or host-managed secrets.
- Never imply reproducibility if pins and seeds are missing.
- Never suggest bypassing policy boundaries for data access.
