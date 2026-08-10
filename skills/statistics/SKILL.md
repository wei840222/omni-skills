---
name: statistics
description: Guide statistical reasoning from probability to inference. Use when the user asks about probability distributions, hypothesis testing, confidence intervals, regression analysis, p-values, effect sizes, sampling methods, Bayesian inference, causal inference, or interpreting statistical output from software.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📊"}'
---

## Workflow

1. **Assess user level** — start with a plain-language explanation, then offer notation, software detail, or proofs when the user asks for them.
2. **Visualize first** — always plot data before computing statistics
   - Histogram for distribution shape
   - Scatter plot for relationships
   - Box plot for group comparisons
3. **Specify the estimand and model** — identify the outcome, design/dependence, comparison or association of interest, and analysis model before selecting a test.
4. **Assess model fit in context** — use plots, residuals, design knowledge, and sensitivity analyses; a diagnostic does not create a universal pass/fail threshold.
5. **Select method and recovery path** — match the method to the estimand, then state how dependence, missingness, heteroscedasticity, nonlinearity, outliers, or multiplicity changes the analysis.
6. **Report completely** — effect sizes + confidence intervals + p-values + sample sizes

## Pre-Test Verification

Verify these conditions before running any test:
- [ ] Data quality: missing values handled, outliers documented
- [ ] Design, estimand, missing-data handling, dependence, and model diagnostics documented
- [ ] Exploratory vs confirmatory: same data cannot do both
- [ ] Multiple comparisons: define the confirmatory family and select a justified error-control or estimation strategy
- [ ] Effect size will be reported alongside p-value

**If a condition is uncertain or violated:** describe it, select a condition-specific recovery (for example Welch/robust methods for variance differences, clustered or repeated-measures models for dependence, multiple imputation/sensitivity analysis for missingness, or a transformed/nonlinear model), and report the limitation. Load `references/teaching-guide.md` only when correcting a user misconception.

## Common Pitfalls

**p-value misinterpretations** (ASA 2016):
- ❌ p-value = probability null hypothesis is true
- ✅ p-value = compatibility of the data with a specified statistical model, including its null hypothesis and assumptions
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
- 2 independent groups → estimate a mean difference with its interval; use a model appropriate to the design. Welch methods are often preferable when variances or group sizes differ.
- 2 paired observations → model the paired differences or use a paired/resampling method; do not treat repeated observations as independent.
- 3+ independent groups → estimate planned contrasts or use a regression/ANOVA model that matches the design; define the multiplicity family before follow-up comparisons.
- 3+ repeated groups → use a repeated-measures, mixed-effects, or other dependence-aware model; choose a rank-based method only when its estimand answers the question.

**Diagnostics and recovery**:
- Use QQ/residual plots and subject-matter knowledge alongside diagnostics. Shapiro–Wilk is applicable to 3–5000 non-missing observations, but it is not a method-selection cutoff.
- For heteroscedasticity, use Welch/heteroscedasticity-robust estimation, a suitable variance model, or sensitivity analyses; report the choice.
- For skewness, outliers, or nonlinearity, inspect influence and consider transformation, robust, generalized, or resampling approaches that preserve the stated estimand.
- Mann–Whitney and Kruskal–Wallis assess distributional/rank differences; describe that estimand rather than presenting them as automatic replacements for a mean comparison.

**Relationships**:
- 2 continuous variables → inspect a scatter plot, define the association of interest, and use Pearson, rank, robust, or model-based measures with their assumptions stated.
- Predict continuous outcome from predictors → use a regression model; inspect residual pattern, functional form, leverage/influence, and collinearity in context rather than universal VIF or Cook's-D cutoffs.
- Predict binary outcome → use a logistic or other appropriate model; assess functional form, separation, dependence, calibration, and collinearity in context.

**Causal claims**:
- Observational data → need identification strategy:
  - Instrumental variables (IV): need valid instrument (relevant, exogenous)
  - Difference-in-differences (DiD): need parallel trends assumption
  - Regression discontinuity (RD): need clear cutoff, no manipulation
  - Propensity score matching: need all confounders measured
- Causal claims require an identification strategy; correlation alone is insufficient

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

## Critical Safeguards

These practices protect result validity — apply them as standard procedure:
1. For confirmatory families, predefine the estimands and select a justified FWER, FDR, hierarchical, or estimation-focused strategy
2. Use identification strategy for causal claims from observational data → separates correlation from causation
3. Report confidence intervals alongside p-values → provides effect magnitude and precision
4. Check confidence interval width when p > 0.05 → distinguishes "no effect" from "insufficient data"
5. Address assumption violations before interpreting results → ensures result validity
6. Report all analyses conducted → maintains reproducibility and avoids publication bias

**If any safeguard cannot be met → explain why it matters, document the limitation**

## References

Load when needed:
- `references/asa-statements.md` — ASA 2016/2019 guidance on p-values, effect sizes, and moving beyond significance thresholds
- `references/teaching-guide.md` — 13 common misconceptions with corrections and teaching analogies (load when user shows misunderstanding)
