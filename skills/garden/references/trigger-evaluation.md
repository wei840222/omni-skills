# Trigger Evaluation

This review exercises the `garden` description against realistic requests. The prompts remain read-only; the observations describe the expected routing decision.

| ID | Prompt | Expected route | Observed result |
|---|---|---|---|
| P1 | "I want a plan for rotating crops in my vegetable beds next year." | Activate `garden` | Activate: garden rotation and seasonal planning are in scope. |
| P2 | "My raised-bed tomatoes have yellow lower leaves. How should I investigate?" | Activate `garden` | Activate: a garden-context plant diagnosis is in scope. |
| N1 | "What is this houseplant, and how do I care for it?" | Route to `plants` | Route to `plants`: this is plant identification/care without garden context. |
| N2 | "Build a React dashboard for my greenhouse sensors." | Route to a software skill | Route to a software skill: this is software implementation rather than garden management. |

The description explicitly uses garden context to preserve the P1/P2 behavior while reducing overlap with the `plants` related skill.
