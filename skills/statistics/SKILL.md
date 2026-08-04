---
name: statistics
description: Guide statistical reasoning from probability to inference. Use when the user asks about probability distributions, hypothesis testing, confidence intervals, regression analysis, p-values, effect sizes, sampling methods, Bayesian inference, causal inference, or interpreting statistical output from software.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📊"}'
---

## Workflow

1. **Assess user level** — notation familiarity, software mentioned, problem complexity
   - If user mentions R/Python/Stata → assume intermediate, use technical terms
   - If user describes data in plain language → assume beginner, start with concrete examples
   - If user asks about formulas or proofs → assume advanced, provide mathematical detail
2. **Visualize first** — always plot data before computing statistics
   - Histogram for distribution shape
   - Scatter plot for relationships
   - Box plot for group comparisons
3. **State assumptions** — every test has assumptions; check them explicitly
   - Normality: Shapiro-Wilk (n < 50) or visual inspection of QQ plot
   - Equal variance: Levene's test or ratio of largest/smallest SD < 2
   - Independence: study design, not testable statistically
4. **Select method** — match test to data structure and research question
5. **Report completely** — effect sizes + confidence intervals + p-values + sample sizes

## 🔴 CHECKPOINT: Before Running Any Test

**STOP and verify:**
- [ ] Data quality: missing values handled, outliers documented
- [ ] Assumptions checked (normality, equal variance, independence)
- [ ] Exploratory vs confirmatory: same data cannot do both
- [ ] Multiple comparisons: if testing >1 hypothesis, apply correction
- [ ] Effect size will be reported alongside p-value

**If any check fails → load `references/teaching-guide.md` for common pitfalls**

## Common Pitfalls to Avoid

**p-value misinterpretations** (ASA 2016):
- ❌ p-value = probability null hypothesis is true
- ✅ p-value = probability of data this extreme IF null is true
- ❌ p < 0.05 means effect is real
- ✅ p < 0.05 means data are unusual under null (could still be bias/confounding)
- ❌ "Non-significant" (p > 0.05) = no effect
- ✅ p > 0.05 = insufficient evidence against null (check confidence interval width)

**Other frequent errors**:
- ❌ Correlation implies causation → ✅ Always consider confounders, need experimental/causal design
- ❌ Large samples fix bias → ✅ Large n reduces random error, not systematic error
- ❌ Post-hoc power analysis → ✅ Determined by p-value; use confidence intervals instead
- ❌ Failing to reject H₀ = accepting H₀ → ✅ Absence of evidence ≠ evidence of absence
- ❌ SD = SE → ✅ SD = population spread, SE = sampling precision

## When to Use Each Method

**Comparing groups** (continuous outcome):
- 2 groups, independent → Independent t-test (if normal + equal variance) OR Mann-Whitney U (if not)
- 2 groups, paired → Paired t-test (if differences normal) OR Wilcoxon signed-rank
- 3+ groups, independent → One-way ANOVA (if normal + equal variance) OR Kruskal-Wallis
- 3+ groups, repeated → Repeated-measures ANOVA OR Friedman test

**Decision rules for normality**:
- n < 30: Shapiro-Wilk test (p < 0.05 → non-normal)
- n ≥ 30: Visual inspection of QQ plot + histogram
- Severe skewness or outliers → use non-parametric alternative

**Decision rules for equal variance**:
- Levene's test p < 0.05 → unequal variance
- Ratio of largest SD / smallest SD > 2 → unequal variance
- If unequal: use Welch's t-test (not Student's t-test), or Welch's ANOVA

**Relationships**:
- 2 continuous variables → Pearson correlation (if both normal) OR Spearman correlation (if not) + scatter plot
- Predict continuous outcome from predictors → Linear regression (check residuals, multicollinearity VIF < 5, influence Cook's D < 1)
- Predict binary outcome → Logistic regression (check linearity of logit, no multicollinearity)

**Causal claims**:
- Observational data → need identification strategy:
  - Instrumental variables (IV): need valid instrument (relevant, exogenous)
  - Difference-in-differences (DiD): need parallel trends assumption
  - Regression discontinuity (RD): need clear cutoff, no manipulation
  - Propensity score matching: need all confounders measured
- Cannot claim causation from correlation alone

## Reporting Standards

Follow domain-specific guidelines:
- **Randomized trials**: CONSORT — [consort-statement.org](http://www.consort-statement.org)
- **Observational studies**: STROBE — [strobe-statement.org](https://www.strobe-statement.org)
- **Systematic reviews**: PRISMA — [prisma-statement.org](http://www.prisma-statement.org)

**Always report**:
- Effect size with 95% confidence interval (e.g., "mean difference = 2.3, 95% CI [1.1, 3.5]")
- Exact p-value (e.g., "p = 0.023", not "p < 0.05")
- Sample size for each group/analysis
- Software and version (e.g., "R version 4.3.1", "Python 3.11 with scipy 1.11")
- All analyses conducted, not just significant ones

## 🛑 STOP: Red-Light Dangerous Actions

**NEVER do these without explicit justification:**
1. Run multiple tests without correction → inflates false positive rate
2. Claim causation from observational data without identification strategy
3. Use post-hoc power analysis → circular reasoning
4. Interpret p > 0.05 as "no effect" → check confidence interval width
5. Ignore assumption violations → results may be invalid
6. Report only significant results → publication bias

**If user insists on these → explain why it's problematic, document the issue**

## References

Load when needed:
- `references/asa-statements.md` — ASA 2016/2019 guidance on p-values, effect sizes, and moving beyond significance thresholds
- `references/teaching-guide.md` — 13 common misconceptions with corrections and teaching analogies (load when user shows misunderstanding)
