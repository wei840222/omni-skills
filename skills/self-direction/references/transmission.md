# Direction Transmission

Use this when spawning a sub-agent that must stay aligned with the user's
direction without receiving the entire model.

Write durable frames to `<state_root>/self-direction/transmission.md` when the
frame may be reused; otherwise pass an ephemeral frame in the spawn package.

## Frame template

```text
DIRECTION FRAME
context: Why this task exists
values: What matters for this work (verbatim; do not soften)
criteria: How to judge success
boundaries: What never to do; what always needs approval
resources: Time / money / token / attention budget
escalation: Exact conditions to stop and ask
done: Observable completion check
```

## Faithfulness rules

1. Include every relevant hard boundary, even if it seems obvious.
2. Preserve values exactly as captured — do not reinterpret or soften them.
3. Keep the why, not only the what.
4. Add escalation triggers for low-confidence or out-of-frame decisions.
5. Omit unrelated personal context and secrets.
6. After the sub-agent returns, verify the result against the same frame before
   accepting it.

## Minimal example

```text
context: Competitor landscape scan for pricing page rewrite
values: Accuracy over speed; cite primary sources
criteria: At least 3 independent sources per material claim
boundaries: Never interact with competitor accounts; never publish findings
resources: Max 1 hour; no paid API spend above $0 unless approved
escalation: Ask if a claim lacks sources or requires login
done: Bullet brief with URLs and residual unknowns
```

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Be helpful and use good judgment" | Replace with concrete values and boundaries |
| Softening "never publish" to "prefer draft" | Keep the hard limit |
| Omitting spend / privacy limits | Copy resource and boundary lines from the model |
| Accepting output without frame check | Diff the result against criteria and boundaries |
