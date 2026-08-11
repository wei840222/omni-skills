---
name: delegate
description: Delegate bounded, independent tasks to sub-agents when parallel work costs less than manual execution; select capability tiers, recover from failures, and verify results.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📤"}'
---

## Core Rule

Spawn cost < task cost → delegate. Otherwise, do it yourself.

## Model Tiers

Choose from the models available in the current runtime. Confirm model availability, limits, and pricing with that runtime's current provider documentation before spawning.

| Tier | Capability profile | Relative cost | Use for |
|------|--------------------|---------------|---------|
| Small | Fast execution for straightforward, high-volume work | Low | Search, summarize, format, classify |
| Medium | Strong reasoning and code generation | Moderate | Code, analysis, synthesis |
| Large | Frontier reasoning for difficult, multi-step work | High | Architecture, complex reasoning |

**Rule of thumb:** Start with smallest tier. Escalate only if output quality insufficient.

## Spawn Checklist

Every spawn must include:
```
1. TASK: Single clear deliverable (not "help with X")
2. MODEL: Explicit tier choice
3. CONTEXT: Only files/info needed (never full history)
4. OUTPUT: Expected format ("return JSON with...", "write to file X")
5. DONE: How to signal completion
```

Load `assets/templates.md` for copy-paste spawn templates when preparing a spawn checklist.

## Error Recovery

| Error Type | Action |
|------------|--------|
| Sub-agent timeout (>5 min no response) | Kill and retry once |
| Wrong output format | Retry with stricter instructions |
| Task too complex for tier | Escalate: Small→Medium→Large |
| Repeated failures (3x) | Abort, report to user |

Load `references/errors.md` for recovery patterns and escalation logic when encountering an error or sub-agent timeout.

## Verification

Never trust "done" without checking:
- **Code:** Run tests, check syntax
- **Files:** Verify they exist and have content
- **Data:** Spot-check 2-3 items
- **Research:** Confirm sources exist

## Manual Execution

Execute tasks manually yourself instead of delegating if:
- They are quick to complete (<30 seconds)
- They require continuous conversation context
- They require user clarification mid-task
