---
name: cro
description: Optimize conversion rates using funnel analysis, A/B testing, and statistical
  evaluation.
metadata:
  related-skills: null
  openclaw: '{"emoji": "📈"}'
---

## When to load

Load when the user asks to improve conversion rates for websites, landing pages, SaaS products, or eCommerce through funnel audits, A/B testing, or statistical evaluation.

## Quick Reference

| Topic | File |
|-------|------|
| A/B testing methodology | `references/testing.md` |
| Conversion audits | `references/audits.md` |
| Legal compliance | `references/legal.md` |
| Tools and integrations | `references/tools.md` |

## Core Rules

### 1. Statistical Rigor First
- 95% confidence minimum before calling any test
- Calculate sample size before starting — underpowered tests waste time
- Run tests to full duration — early peeking inflates false positives
- Document hypothesis before running — post-hoc rationalization is not science

### 2. Funnel Analysis Before Optimization
- Map entire journey: awareness, consideration, decision, retention
- Quantify drop-off at each step with specific numbers
- Revenue impact per improvement — prioritize by dollars, not percentages
- Segment by traffic source, device, user type — aggregates hide insights

### 3. One Variable Per Test
- Isolate changes to attribute results correctly
- Reserve multivariate testing only for extremely high-traffic contexts
- If you change two things and conversion improves, you learned nothing

### 4. Mobile-First Testing
- Test mobile variants explicitly — desktop assumptions fail on phones
- Majority of traffic is mobile, often worst conversion
- Touch targets, page speed, form friction all differ

### 5. Legal Compliance Non-Negotiable
- Cookie consent required in EU before tracking
- GDPR: personal data in experiments needs legal basis
- Dark patterns are illegal — fake urgency, confirm-shaming, hidden costs
- Accessibility (WCAG) is both legal requirement and conversion opportunity

### 6. Document Everything
- Hypothesis, variants, results, learnings in permanent record
- Losing tests are learning — document why hypothesis was wrong
- Share results across teams — wins in one funnel inform others

### 7. Revenue Connection
- Revenue targets tie to conversion targets — make the math explicit
- Prioritize evaluating signups by their conversion to revenue
- Prioritize by ICE: Impact, Confidence, Ease

## Common Traps

- Calling tests early because results look good — false positives waste resources
- "We changed everything and revenue went up" — no control group proves nothing
- Copy-pasting competitor tactics without context — what works for them may fail for you
- Optimizing for vanity metrics — engagement without revenue is vanity
- Testing without proper tracking setup — retroactive data is unreliable
