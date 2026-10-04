# Prompting for taste — creative generation

## Committee problem

Default model outputs feel generic because they sample the high-probability average:

- What most writers/designers would do
- Statistical mean, not individual excellence

Goal: shift the sampling region toward a coherent taste manifold, then edit.

## Practices that work

### 1. Identity anchoring over instruction stacking

Weak: “Write elegantly with varied sentence structure and sophisticated vocabulary.”

Stronger: “Write as someone who cuts every vague phrase on sight; each sentence earns its keep.”

Stacked abstract constraints often hedge. A coherent identity activates a tighter stylistic cluster.

### 2. Negative space definition

List hard rejects:

```text
Never use "dive into"
Never start with "In today's world"
Never explain why something matters — let it matter
Never use exclamation points for empty enthusiasm
Never hedge with "it's worth noting"
```

Prune generic peaks while leaving room for distinctive choices.

### 3. One sharp example over ten explanations

One on-domain example beats generic “good writing” advice.

- Punchy product copy → show punchy product copy
- Elegant technical prose → show elegant technical prose

Models interpolate from examples; stay in the right region.

### 4. Temperature is variance, not taste

Higher temperature increases variance (brilliance and garbage). Prefer moderate temperature and better targeting over randomness-as-creativity.

### 5. Fewer simultaneous style demands

Each extra constraint is another band to satisfy. “Concise + metaphorical + formal + funny” often collapses to the average of each band.

One strong aesthetic direction outperforms a long style checklist:

- “Write like you’re too tired to lie”
- “Make it feel expensive without saying expensive”
- “Museum gift-shop card: one idea, perfect edges”

### 6. Author the first line, continue the rest

Taste often lives in momentum. Write the opening sentence in the target voice, then continue. That is few-shot prompting with perfect position.

### 7. Rejection criteria over vague acceptance criteria

```text
Reject and regenerate if:
- Opens with a rhetorical question
- Uses "game-changer" or "revolutionize"
- Lists more than three items without need
- Explains what should be shown
- Sounds like generic 2015 marketing copy
```

Boundaries of bad are easier to enforce than a fuzzy center of good.

## Core insight

Taste is not installed by longer instruction lists alone. Create conditions where distinctive output is the path of least resistance: shift the distribution, then edit with calibrated judgment and user corrections stored under `<state_root>/`.
