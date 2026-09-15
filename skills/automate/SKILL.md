---
name: automate
description: Spot repetitive deterministic work and turn it into durable scripts so
  agents stop burning tokens on format conversion, validation, fixed workflows, and
  other rule-based tasks. Load `references/signals.md` for detection patterns,
  `references/templates.md` for script skeletons, and `references/sources.md` for
  automation reliability notes.
metadata:
  openclaw: '{"emoji": "⚙️"}'
---

## When to load

Load this skill when the user is repeating the same transformation, validation, file
operation, or fixed workflow; when an agent is about to re-prompt for work that should
be a script; or when deciding Script vs LLM for a deterministic task.

## Quick Reference

| Topic | File |
|-------|------|
| Detection signals | `references/signals.md` |
| Script templates | `references/templates.md` |
| Research sources | `references/sources.md` |

## Core Principle

LLMs are expensive, slow, and probabilistic. Scripts are free, fast, and deterministic.

Every time you do something twice that could be scripted, you're wasting:
- **Tokens** — money burned on solved problems
- **Time** — seconds/minutes vs milliseconds
- **Reliability** — scripts fail predictably; LLMs fail randomly

When evaluating a task for automation, load `references/signals.md`. When ready to write
a script, load `references/templates.md`. For reliability and secrets guidance, load
`references/sources.md`.

---

## The Automation Test

Before doing any task, ask:

1. **Is this deterministic?** Same input → same output every time?
2. **Is this repetitive?** Will this happen again?
3. **Is this rule-based?** Can I write down the exact steps?

If yes to all three → **script it instead of using the LLM.**

---

## Script vs LLM Decision Matrix

| Task type | Script | LLM |
|-----------|--------|-----|
| Format conversion (JSON↔YAML) | ✅ | ❌ |
| Text transformation (regex) | ✅ | ❌ |
| File operations (rename, move) | ✅ | ❌ |
| Data validation | ✅ | ❌ |
| API calls with fixed logic | ✅ | ❌ |
| Git workflows | ✅ | ❌ |
| Judgement calls | ❌ | ✅ |
| Creative content | ❌ | ✅ |
| Ambiguous inputs | ❌ | ✅ |
| One-time unique tasks | ❌ | ✅ |

---

## Automation Triggers

When you notice yourself:

- Doing the **same task twice** → script it
- Writing **similar prompts repeatedly** → script the pattern
- **Formatting output** the same way → script the formatter
- **Validating data** with same rules → script the validator
- **Calling APIs** with predictable logic → script the integration

---

## Automation Proposal Format

When you spot an opportunity:

```
🔧 Automation opportunity

Task: [what you keep doing]
Frequency: [how often]
Current cost: [tokens/time per run]

Proposed script:
- Language: [bash/python/node]
- Input: [what it takes]
- Output: [what it produces]
- Location: [where to save it]

Estimated savings: [tokens/time saved per month]

Should I write it?
```

---

## Best Practices for Automation

- **Deterministic Pipelines:** Ensure your scripts are robust. If a task fails, fail loudly with an exit code rather than silently continuing.
- **Idempotency:** Automation scripts should ideally be safe to run multiple times without causing unwanted side effects.
- **Error Handling & Logs:** Log standard output and standard error separately.

## Script Standards

When writing automation:

1. **Single purpose** — one script, one job
2. **Idempotent** — safe to run multiple times
3. **Documented** — usage in comments at top
4. **Logged** — output what you're doing
5. **Fail loud** — exit codes, error messages
6. **No secrets hardcoded** — env vars or keychain

---

## Tracking Automations

Document what you've built:

```
### Active Scripts
- scripts/format-json.sh — JSON prettifier [saved ~2k tokens/week]
- scripts/deploy-staging.sh — one-command deploy [saved 5min/deploy]
- scripts/sync-env.sh — env file sync [eliminated manual errors]

### Candidates
- Weekly report generation — repetitive formatting
- Log parsing — same grep patterns every time
```

---

## The 3x Rule

If you do something **3 times**, it must become a script.

- 1st time: Do it, note that it might repeat
- 2nd time: Do it, flag as automation candidate  
- 3rd time: Pause execution. Write the script first, then run it.

---

## Better Practices

| Common Pattern | Optimal Pattern |
|----------------|-----------------|
| Re-prompt for same transformation | Write a script once |
| Use LLM for data validation | Write validation rules |
| Burn tokens on formatting | Use formatters (prettier, jq, etc.) |
| Ask LLM to remember procedures | Document in scripts |
| Solve same problem differently each time | Standardize with automation |

---

*Every script written = permanent token savings. Compound your efficiency.*
