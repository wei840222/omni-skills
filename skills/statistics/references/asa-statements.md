# ASA Statements on p-values and Statistical Significance

## 2016 Statement: Context, Process, and Purpose

**Source**: Ronald L. Wasserstein & Nicole A. Lazar, "The ASA's Statement on p-Values: Context, Process, and Purpose," *The American Statistician* 70(2), 2016. [DOI: 10.1080/00031305.2016.1154108](https://doi.org/10.1080/00031305.2016.1154108). See also the [ASA release](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf).

### Key Principles

1. **P-values measure compatibility, not truth probability**
   - A p-value measures the compatibility of the observed data with a specified statistical model, including the null hypothesis and its analysis assumptions; in a tail-area formulation it is the probability, under that model, of data at least this incompatible.
   - It does NOT measure the probability that the null hypothesis is true
   - It does NOT measure the probability that the data arose by random chance alone

2. **Statistical significance ≠ scientific importance**
   - A small p-value does not imply practical or scientific importance
   - A large p-value does not imply the null hypothesis is true
   - Context, effect size, and study design matter more than the p-value alone

3. **No single threshold should replace scientific judgment**
   - The conventional p < 0.05 threshold is arbitrary
   - Dichotomizing results as "significant" or "non-significant" loses information
   - P-values should be interpreted continuously, not as pass/fail

4. **P-values do not measure all sources of bias**
   - They do not account for multiple comparisons
   - They do not account for selective reporting
   - They do not account for violations of assumptions

### Common Misinterpretations to Correct

- ❌ "p = 0.03 means there's a 3% chance the null is true"
- ✅ "p = 0.03 means that IF the null were true, we'd see data this extreme only 3% of the time"

- ❌ "p > 0.05 means there's no effect"
- ✅ "p > 0.05 means we don't have strong evidence against the null, but an effect may still exist"

- ❌ "p < 0.05 means the effect is real"
- ✅ "p < 0.05 means the data are unusual under the null, but the effect could still be due to bias, confounding, or chance"

## 2019 Statement: Moving to a World Beyond "p < 0.05"

**Source**: Ronald L. Wasserstein, Allen L. Schirm & Nicole A. Lazar, "Moving to a World Beyond 'p < 0.05'," *The American Statistician* 73(sup1), 2019. [DOI: 10.1080/00031305.2019.1583913](https://doi.org/10.1080/00031305.2019.1583913)

### Key Recommendations

1. **Move beyond statistical significance thresholds**
   - Abandon the "p < 0.05" dichotomy
   - Report p-values as continuous measures of evidence
   - Focus on effect sizes and confidence intervals

2. **Embrace uncertainty quantification**
   - Confidence intervals show plausible values for the parameter
   - They convey both magnitude and precision
   - Wider intervals = more uncertainty

3. **Prioritize estimation over testing**
   - "How big is the effect?" is more informative than "Is the effect different from zero?"
   - Report effect sizes with confidence intervals
   - Discuss practical significance

4. **Be transparent about analysis choices**
   - Pre-register hypotheses and analysis plans when possible
   - Report all analyses conducted, not just significant ones
   - Distinguish exploratory from confirmatory analyses

### Practical Implications

**Instead of:**
- "The result was significant (p = 0.03)"

**Report:**
- "The effect size was X (95% CI: [lower, upper]), p = 0.03"
- Discuss whether the effect is practically meaningful
- Consider the precision of the estimate (width of CI)

**Instead of:**
- "There was no significant difference (p = 0.15)"

**Report:**
- "The estimated difference was X (95% CI: [lower, upper]), p = 0.15"
- Note whether the CI excludes practically important effects
- Consider whether the study had adequate power

## Application in Practice

When interpreting or reporting statistical results:

1. **Always report effect sizes** — Cohen's d, odds ratios, regression coefficients, etc.
2. **Always report confidence intervals** — they show precision and plausible values
3. **Report exact p-values** — not just "p < 0.05" or "p > 0.05"
4. **Discuss practical significance** — is the effect large enough to matter?
5. **Acknowledge limitations** — sample size, measurement error, potential biases
6. **Avoid dichotomous language** — "significant" vs "non-significant" obscures the continuous nature of evidence
