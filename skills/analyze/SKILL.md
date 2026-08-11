---
name: analyze
description: Structured analysis for any input. Data, code, text, decisions, visuals. Prioritize, question, conclude.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧩"}'
---

Before analyzing: State what decision this serves. Pick a framework. Note first impression to challenge later.

## Before

- **Purpose in one line**: "This analysis helps decide ___"
- **What's missing**: 3+ unknowns that would change conclusions
- **First impression**: Write it — then seek counter-evidence

## During

- **Prioritize always**: 🔴 Critical (1-2 max) · 🟡 Important (2-3) · ⚪ Minor
- **Mark sources**: Every claim gets `[from input]` or `[inferred]`
- **Seek disconfirmation**: Dedicate space to "why I might be wrong"
- **Distinguish**: Facts vs opinions. Correlation vs causation.

## After

- **One-line summary**: Force analysis into one sentence
- **So what?**: End with action, not summary
- **Obviousness test**: Would someone say this without reading? → Deeper

## Traps

- **Superficial**: Paraphrasing ≠ analysis
- **Equal weight**: Everything yellow = nothing prioritized
- **Confirmation bias**: First impression became conclusion
- **Missing denominator**: "500 cancellations" of 600 or 50,000?
- **Invented data**: Stats without source = hallucination

## By Domain

| Domain | Focus | Watch |
|--------|-------|-------|
| Data | Grain, missing, outliers | Centinels, mixed types |
| Code | Production breaks, dead code | Style ≠ bugs |
| Text | Thesis, evidence strength | Unsourced claims |
| Decisions | Unlisted options, reversibility | Status quo bias |
| Visual | Dominance, consistency | Platform conventions |

## Frameworks

Pick one before starting:

- **MECE**: Mutually exclusive, collectively exhaustive. Ensure all categories are disjoint and cover the entire possible scope of the problem.
- **Pros/Cons+**: Add reversibility + cost of inaction
- **Pre-mortem**: Assume the project or strategy has already failed spectacularly in the near future, then work backward to determine what led to this failure. Helps counter overconfidence and groupthink.
- **Steel man**: Address the strongest form of an opponent's argument (or the strongest counter-argument to a thesis), even if it was not presented, by applying the principle of charity. Doing so tests the true robustness of the position.

## Output

```
🎯 PURPOSE: Decide [X]
🔴 CRITICAL: [Finding + source]
🟡 IMPORTANT: [Findings]
⚠️ COUNTER: [Contradictions]
➡️ ACTION: [Recommendation]
```
