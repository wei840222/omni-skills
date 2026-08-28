## Core Rules

### 1. Turn the Prompt Into a Resolvable Question First
- Use `references/question-design.md` before making any forecast that matters.
- If the target, threshold, deadline, or resolution source is fuzzy, the forecast is not auditable and the hit rate cannot improve.

### 2. Start With the Outside View Before the Story
- Pull a base rate or nearest reference class before building an inside-view narrative.
- Humans overweight unique details and underweight how often similar situations actually happen.

### 3. Run the BRACE Forecast Loop on Every Non-Trivial Prediction
- Use `references/forecast-loop.md`: Base rate, Resolution rule, Arguments both ways, Confidence assignment, Evaluation plan.
- A loop beats intuition because it forces evidence on both sides and leaves a trail for later scoring.

### 4. Express Uncertainty Numerically and Defend It
- Give a number, range, or explicit scenario split rather than words like "probably" or "maybe."
- Use `references/calibration.md` to map evidence quality, sample size, and model disagreement into probability levels.

### 5. Separate Signal From Narrative Heat
- Track what is actually predictive, what is merely interesting, and what is just recent or vivid.
- Strong stories with weak base rates are noise, not edge.

### 6. Update Only on Information That Changes the Odds
- Pre-commit to update triggers: deadline changes, threshold changes, a major driver flips, or new data changes the reference class.
- Constant micro-updating on every headline produces churn without better accuracy.

### 7. Score Every Meaningful Forecast and Learn From Misses
- Use `references/scoring-and-review.md` after resolution and store the result in the local scorecard.
- Unscored forecasts feel smart in the moment and teach nothing later.