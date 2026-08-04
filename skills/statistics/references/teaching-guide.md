# Teaching Statistics: Common Misconceptions and Corrections

## About p-values

### Misconception 1: "p-value is the probability the null hypothesis is true"

**Correction**: A p-value is the probability of observing data this extreme or more extreme, **given that the null hypothesis is true**. It's P(data | H₀), not P(H₀ | data).

**Teaching analogy**: "If I see someone with an umbrella, what's the probability it's raining?" That's P(rain | umbrella), not P(umbrella | rain). The p-value tells you how surprising the data is under the null, not how likely the null is.

### Misconception 2: "p < 0.05 means the effect is real"

**Correction**: A small p-value means the data are unusual under the null hypothesis, but the effect could still be due to:
- Bias (selection bias, measurement error)
- Confounding variables
- Multiple testing (if you test 20 hypotheses, expect 1 false positive by chance)
- Violations of test assumptions

**Teaching point**: Statistical significance is necessary but not sufficient. You also need:
- Valid study design
- Appropriate methods
- Practical significance
- Replication

### Misconception 3: "p > 0.05 means there's no effect"

**Correction**: A large p-value means you don't have strong evidence against the null, but:
- The study may be underpowered (too small to detect a real effect)
- The effect may exist but be small
- Measurement error may obscure the effect

**Teaching point**: "Absence of evidence is not evidence of absence." Check the confidence interval — does it exclude practically important effects?

## About Hypothesis Testing

### Misconception 4: "Failing to reject H₀ means accepting H₀"

**Correction**: Hypothesis testing is asymmetric. You can find evidence against the null, but you cannot prove the null is true. Failing to reject H₀ just means you don't have enough evidence to reject it.

**Teaching analogy**: A courtroom verdict of "not guilty" doesn't mean the defendant is innocent — it means the prosecution didn't prove guilt beyond a reasonable doubt.

### Misconception 5: "Statistical significance implies practical importance"

**Correction**: With a large enough sample, even trivial effects become statistically significant. A 0.1% difference might have p < 0.001 with n = 10,000, but that doesn't mean it matters in practice.

**Teaching point**: Always ask "How big is the effect?" not just "Is it significant?" Report effect sizes and confidence intervals.

## About Confidence Intervals

### Misconception 6: "The 95% confidence interval has a 95% probability of containing the true value"

**Correction**: The confidence interval is a random interval. Before you collect data, there's a 95% probability that the interval you'll compute will contain the true parameter. After you compute it, the interval either contains the true value or it doesn't — it's no longer random.

**Frequentist interpretation**: If you repeated the study many times, 95% of the computed intervals would contain the true parameter.

**Practical interpretation**: The confidence interval shows plausible values for the parameter, given the data. Wider intervals = more uncertainty.

### Misconception 7: "If the confidence interval includes zero, there's no effect"

**Correction**: The confidence interval shows the range of plausible values. If it includes zero, zero is plausible, but so are other values. The width of the interval tells you about precision.

**Teaching point**: A wide interval that includes zero means you're uncertain — you need more data. A narrow interval that includes zero but also excludes large effects suggests the effect is likely small.

## About Correlation and Causation

### Misconception 8: "Correlation implies causation"

**Correction**: Correlation can arise from:
- Direct causation (X → Y)
- Reverse causation (Y → X)
- Confounding (Z → X and Z → Y)
- Selection bias
- Measurement artifacts

**Teaching point**: To claim causation, you need:
- Temporal precedence (cause before effect)
- Association (correlation)
- No plausible confounders (or methods to control for them)
- A plausible mechanism

**Examples**:
- Ice cream sales and drowning deaths are correlated, but ice cream doesn't cause drowning — both increase in summer (confounding by season)
- Cities with more firefighters have more fire damage, but firefighters don't cause damage — larger fires get more firefighters (confounding by fire size)

## About Sample Size and Power

### Misconception 9: "Large samples fix everything"

**Correction**: Large samples reduce random error (increase precision) but do not fix systematic errors (bias). A biased estimate with n = 1,000,000 is still biased.

**Teaching point**: 
- Large samples → narrow confidence intervals (precise estimates)
- But if the estimate is biased, precision doesn't help
- "Garbage in, garbage out" regardless of sample size

### Misconception 10: "Post-hoc power analysis is useful"

**Correction**: Post-hoc (observed) power is completely determined by the p-value you already have. If p = 0.05, observed power ≈ 50%. If p < 0.05, observed power > 50%. It tells you nothing new.

**Teaching point**: Power analysis is useful **before** the study (to determine sample size), not after. After the study, the confidence interval tells you about precision.

## About Multiple Testing

### Misconception 11: "I can test 20 hypotheses and report the 3 that are significant"

**Correction**: If you test 20 independent hypotheses at α = 0.05, you expect 1 false positive by chance alone (20 × 0.05 = 1). Reporting only the significant results inflates the false positive rate.

**Solutions**:
- **Bonferroni correction**: Divide α by the number of tests (α/m). Conservative but simple.
- **Holm correction**: Step-down procedure, less conservative than Bonferroni.
- **False Discovery Rate (FDR)**: Controls the proportion of false positives among significant results. Less conservative, good for exploratory analyses.
- **Pre-registration**: Specify hypotheses and analysis plan before seeing data.

**Teaching point**: The more hypotheses you test, the more likely you'll find something significant by chance. Adjust for multiple comparisons or acknowledge the increased false positive rate.

## About Regression

### Misconception 12: "Adding more predictors always improves the model"

**Correction**: Adding predictors always increases R² (in-sample fit), but can lead to overfitting. The model may fit the current data well but perform poorly on new data.

**Solutions**:
- Use adjusted R², AIC, or BIC (penalize complexity)
- Cross-validation to assess out-of-sample performance
- Domain knowledge to select relevant predictors
- Regularization (LASSO, Ridge) for high-dimensional data

### Misconception 13: "Regression coefficients are causal effects"

**Correction**: Regression coefficients represent associations, controlling for other variables in the model. They are causal effects only if:
- All confounders are measured and included
- No measurement error in predictors
- Correct functional form
- No selection bias

**Teaching point**: "Correlation controlling for other variables" is still correlation. To claim causation from observational data, you need a valid identification strategy (instrumental variables, difference-in-differences, regression discontinuity, etc.).

## Teaching Strategies

1. **Use real data** — textbook examples with clean answers mislead. Real data is messy.
2. **Simulate** — show what happens under the null, what happens with small samples, what happens with multiple testing
3. **Visualize** — Anscombe's quartet, residual plots, confidence interval plots
4. **Ask critical questions**:
   - How was this measured?
   - Who was sampled?
   - What's missing?
   - What would falsify the claim?
5. **Emphasize uncertainty** — point estimates without intervals are incomplete
6. **Connect to decisions** — how would you use this information? What's the cost of being wrong?
