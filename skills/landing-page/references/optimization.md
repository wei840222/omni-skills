# Landing Page Optimization

## Pre-Launch Checklist

### Performance
- [ ] Measure deployed-page performance with field data when available; use PageSpeed Insights or another lab tool to investigate a regression
- [ ] Images compressed and lazy-loaded
- [ ] No render-blocking resources
- [ ] Core Web Vitals passing

### Mobile
- [ ] Fully responsive (test at 375px width)
- [ ] Tap targets are large enough to operate reliably; test the implemented controls on representative mobile devices
- [ ] CTA visible without scrolling on mobile
- [ ] Text readable without zooming

### Accessibility
- [ ] Verify text contrast against WCAG 2.2 SC 1.4.3 (normally 4.5:1; see `references/research.md` for exceptions)
- [ ] Alt text on all images
- [ ] Focusable interactive elements
- [ ] Keyboard navigation works

### Tracking
- [ ] Analytics and consent behavior match the owner's measurement and privacy requirements
- [ ] CTA button click events tracked
- [ ] Form submission events tracked
- [ ] UTM parameters preserved

---

## Analytics Setup

### Essential Events

| Event | When to fire | What to track |
|-------|--------------|---------------|
| page_view | On load | Source, device, location |
| cta_click | CTA button click | Button text, position |
| form_start | First field interaction | Form ID |
| form_submit | Form completed | Form ID, time to complete |
| scroll_depth | 25%, 50%, 75%, 100% | Percentage |

### Key Metrics

Use the primary conversion event as the decision metric. Segment it by the visitor attributes that could explain a meaningful difference (for example, traffic source, device, landing-page variant, or campaign). Supporting measures such as scroll depth, CTA clicks, form starts, form completion, and page performance help locate friction; they do not have universal "good" thresholds.

---

## A/B Testing

### What to Test (High Impact)

1. **Headline** — Different angles, specificity
2. **CTA copy** — Button text and surrounding copy
3. **Hero image** — Product vs outcome vs human
4. **Social proof** — Testimonials vs stats vs logos
5. **Form length** — Fields required vs optional

### Testing Rules

- State one falsifiable hypothesis and the primary metric before launch
- Change the smallest page element that can test that hypothesis
- Set the sample size from the baseline rate, minimum detectable effect, error tolerance, and test method
- Keep targeting and traffic conditions comparable, then document the decision and result

### Experiment decision record

Record the baseline date range, audience, primary event definition, hypothesis, variant, sample-size method, quality checks, result, and the release decision. If the test is underpowered, technically invalid, or confounded by a material traffic change, keep the baseline and redesign the experiment.
---

## Common Problems & Fixes

### High Bounce Rate

| Cause | Fix |
|-------|-----|
| Slow load time | Compress images, defer scripts |
| Mismatch with ad/source | Align messaging |
| Confusing hero | Clearer headline, simpler layout |
| Wrong traffic | Review targeting, keyword match |

### Low CTA Clicks

| Cause | Fix |
|-------|-----|
| CTA not visible | Move above fold |
| Weak CTA copy | Action verb + benefit |
| Too many options | Single CTA per section |
| No urgency | Add scarcity or incentive |

### High Form Abandonment

| Cause | Fix |
|-------|-----|
| Too many fields | Remove non-essential |
| Privacy concerns | Add trust signals |
| Confusing labels | Test with real users |
| Mobile issues | Larger inputs, auto-complete |

---

## Iteration Cycle

1. **Baseline** — Define the conversion event and capture a representative baseline
2. **Hypothesize** — State: "If we change X, metric Y will improve because Z"
3. **Test** — Run the smallest valid experiment that isolates X
4. **Analyze** — Verify data quality, review the primary metric, then inspect relevant segments
5. **Decide** — Release, retain, or redesign based on the predeclared decision rule
6. **Document** — Record the result so the next experiment starts from evidence

### Prioritization Matrix

| Impact | Effort | Priority |
|--------|--------|----------|
| High | Low | Do first |
| High | High | Plan carefully |
| Low | Low | Quick wins |
| Low | High | Skip |

---

## Tools

### Analytics
- Google Analytics 4 (free, comprehensive)
- Plausible (privacy-focused, simple)
- Mixpanel (event-based, funnels)

### A/B Testing
- Google Optimize (deprecated, but alternatives exist)
- Optimizely (enterprise)
- VWO (mid-market)
- PostHog (open source)

### Heatmaps & Session Recording
- Hotjar (freemium)
- FullStory (enterprise)
- Microsoft Clarity (free)

### Performance
- PageSpeed Insights (free)
- GTmetrix (free)
- WebPageTest (free, detailed)


## Evidence and sources

Load `references/research.md` before making current accessibility, performance, analytics, experimentation, or publishable-claim recommendations. It records the authoritative sources and the boundary for context-dependent benchmarks.
