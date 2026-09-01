# Landing Page Research and Evidence

Use this reference when a landing-page recommendation depends on a factual, current, or publishable claim. The page owner remains responsible for proving claims about its own product, customers, prices, results, guarantees, availability, and legal obligations.

## Evidence rules

- Pair product proof with its source, timeframe, and population. A testimonial or metric without context is marketing copy, not decision evidence.
- Match the landing-page message to the visitor's traffic source and the conversion event being measured. Record the baseline before treating a variant as an improvement.
- Treat percentage benchmarks, universal conversion rates, and fixed testing sample sizes as context-dependent. Calculate the test design from the baseline, minimum detectable effect, error tolerance, and traffic available.
- Make accessibility requirements testable in the implemented page rather than relying on visual inspection alone.

## Sources

### Accessibility

- W3C, *Understanding Success Criterion 1.4.3: Contrast (Minimum)* — https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html
  - Normal text needs a 4.5:1 contrast ratio under WCAG 2.2 SC 1.4.3; large-scale text has a 3:1 exception. Decorative and logo text have defined exceptions.
- W3C, *WCAG 2.2* — https://www.w3.org/TR/WCAG22/
  - Use the normative success criteria when implementation or conformance decisions require exact scope.

### Performance and experience measurement

- web.dev, *Web Vitals* — https://web.dev/articles/vitals
  - Core Web Vitals are user-experience signals. Measure the deployed page with field data where possible, then use lab data to investigate regressions.
- Google Analytics Help, *About events* — https://support.google.com/analytics/answer/9322688?hl=en
  - Events are the measurement unit in Google Analytics. Define event names and parameters around the actual conversion path, then validate collection before interpreting the funnel.

### Plain, usable interface copy

- GOV.UK Service Manual, *Writing for user interfaces* — https://www.gov.uk/service-manual/design/writing-for-user-interfaces
  - Use clear language that helps a person complete a task; content design should support the interface rather than add decoration.
