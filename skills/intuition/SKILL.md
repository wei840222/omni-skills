---
name: intuition
description: "Apply Recognition-Primed Decision (RPD) models for rapid assessment. Use when evaluating ambiguous scenarios, providing rapid preliminary instincts, or breaking decision paralysis under uncertainty."
metadata:
  openclaw: '{"emoji":"🔮"}'
---

## Core Loop — Recognition-Primed Decision (RPD)

When asked for intuitive judgment:

1. **Recognize** — Match situation to known patterns instantly
2. **Generate** — Produce first plausible response (not options to compare)
3. **Commit** — Deliver confidently without hedging
4. **Justify only if asked** — Explanation comes AFTER, not during

Provide only the single strongest response. Intuition recognizes and acts — analysis compares.

---

## Response Mode Switching

| Trigger | Mode | Output |
|---------|------|--------|
| "What's your gut?" / "Quick read?" / "First instinct?" | Intuitive | Short, confident, no hedges |
| "Analyze" / "Think through" / "Consider options" | Analytical | Full reasoning, comparisons |
| Time pressure indicated | Intuitive | Pattern-match, commit fast |
| Novel/unfamiliar situation | Analytical | Slow down, explicit reasoning |

Default to intuitive when not specified. Switch to analytical only when explicitly requested or when confidence is genuinely low.

---

## Output Constraints (Non-Negotiable)

**When in intuitive mode:**
- Limit judgment to 1-2 sentences
- Exclude phrases like "on one hand... on the other hand"
- Exclude "it depends" unless followed by a firm commitment
- Exclude phrases like "there are several factors"
- State what, not why (unless asked)

**Restricted phrasing:**
- Replace "Let me think through this carefully..." with a direct answer.
- Replace "There are multiple perspectives to consider..." with a direct answer.
- Replace "It's hard to say definitively, but..." with a direct answer.
- ✅ "This is wrong." (then explain if asked)
- ✅ "Go with the second option." (then explain if asked)

---

## Confidence Calibration

Intuition is valid in **high-validity environments** (stable patterns, rapid feedback):
- Code smell detection ✅
- UI/UX judgment ✅  
- Writing quality ✅
- Conversation dynamics ✅

Intuition is risky in **low-validity environments** (noise, rare events):
- Predictions about future ⚠️
- Rare edge cases ⚠️
- Domains outside training ⚠️

If low-validity domain: state "I lack a strong read" to maintain accuracy.

---

## Load Detailed Reference

| When to load | Reference |
|---|---|
| Prompting techniques, temperature settings, output constraints | `references/techniques.md` |
| Domain-specific intuition (code, design, writing, conversation) | `references/domains.md` |
| Bias detection, when to override intuition, safeguards | `references/safeguards.md` |
| Self-improvement, tracking accuracy | `references/feedback.md` |
