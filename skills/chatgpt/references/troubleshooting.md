# ChatGPT Troubleshooting

When ChatGPT feels wrong, diagnose the failure mode before rewriting the whole
request.

## Symptom table

| Symptom | Likely cause | Best fix |
|---------|--------------|----------|
| Too generic | No real output contract or no audience context | Rebuild the packet with deliverable and constraints |
| Ignores instructions | Conflicting rules, buried requirements, or stale context | Put non-negotiables in a short ordered list and use a fresh surface |
| Repeats the same phrasing every time | Overloaded custom instructions or strong pattern carryover | Use Temporary Chat and simplify durable instructions |
| Contradicts earlier project decisions | Weak decision log or duplicate sources | Restate the current source of truth and update the project charter |
| Hallucinates facts | No evidence requirement or outdated assumptions | Force confirmed vs inferred labeling and verify freshness |
| Gets worse after many turns | Chat sprawl and incremental patching | Restart with the latest brief, files, and one concrete goal |
| GPT creation blocked | Plan/workspace policy or retirement/migration window | Check current help docs; migrate reusable instructions to plugins when required |

## Reset prompt

```text
Start over from this source of truth only.
Ignore prior draft choices that are not restated below.
First restate the task, inputs, constraints, and success criteria in 6 bullets.
Then wait for confirmation before drafting.
```

## Escalation order

1. Tighten the packet.
2. Remove stale or conflicting context.
3. Switch to Temporary Chat or a fresh Project.
4. Reduce the task to one pass.
5. Package a reusable GPT/plugin only after the workflow is stable and allowed.

## Anti-pattern

Do not keep appending "be more precise," "be less generic," or "follow
instructions better." That treats the symptom, not the cause.
