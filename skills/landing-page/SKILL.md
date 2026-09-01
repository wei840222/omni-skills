---
name: landing-page
description: 'Create or audit conversion-focused landing pages: page structure, landing-page copy, primary CTAs, social proof, accessibility, performance, measurement, and experiment design. Use when building a SaaS, ecommerce, lead-generation, event, waitlist, service, or comparison landing page; improving a weak hero or CTA; diagnosing bounce, low CTA clicks, or form abandonment; or planning a focused A/B test. Not for implementing a site UI, general brand strategy, or writing a multi-page website.'
metadata:
  openclaw: '{"emoji":"🖥️","displayName":"Landing Page"}'
---

## State location

This skill is stateless and does not store local configuration.

## When to use

Use this skill for a page built around one measurable conversion event: a purchase, trial, demo request, lead form, registration, or waitlist signup. Start by confirming the audience, offer, traffic source, conversion event, and the evidence available for product claims.

## Quick reference

| Need | Load |
|---|---|
| Choose a page type and its conversion path | `references/templates.md` |
| Plan page sections, proof placement, and CTA hierarchy | `references/sections.md` |
| Draft or audit headline, subhead, CTA, proof, and objection copy | `references/copy.md` |
| Diagnose performance, accessibility, instrumentation, or experiments | `references/optimization.md` |
| Verify publishable claims or current implementation guidance | `references/research.md` |

## Workflow

1. **Choose the conversion path.** Name one primary conversion event and its success metric. Use `references/templates.md` to select the page pattern that matches the offer.
2. **Build the information hierarchy.** Load `references/sections.md` and place the value proposition, proof, objections, and primary CTA in an order that serves the visitor's decision.
3. **Write credible copy.** Load `references/copy.md` to draft outcome-focused headlines, clear subheads, CTA labels, and objection handling. Treat testimonials, metrics, guarantees, urgency, and competitor claims as publishable only when the owner can substantiate them.
4. **Run the pre-launch checks.** Load `references/optimization.md` to verify responsive behavior, accessible interaction and contrast, performance, analytics events, consent requirements, and the conversion path.
5. **Measure before changing.** Establish a baseline for the primary conversion event. When a metric is weak, use the symptom-to-diagnosis table in `references/optimization.md`; test one explicit hypothesis at a time and retain the result.

## Operating rules

- Keep the page centered on one primary visitor outcome and one primary CTA. A secondary action is appropriate only when it advances the same conversion path for visitors not ready for the primary action.
- State benefits in visitor language and qualify product, pricing, performance, review, availability, and scarcity claims with evidence the owner can verify.
- Pair proof with its context: identify the source, timeframe, population, or terms that make a metric or testimonial meaningful.
- Make the primary path usable with keyboard navigation, visible focus, descriptive labels, and sufficient contrast. Supply meaningful alt text for informative images; mark decorative images appropriately in implementation.
- Preserve attribution and user choices according to the analytics and consent setup chosen by the owner.

## Common correction paths

| Signal | First correction | Load |
|---|---|---|
| Visitors leave quickly | Check message match between traffic source and hero; clarify the promised outcome | `references/optimization.md`, `references/copy.md` |
| CTA clicks are low | Make the primary action and its value visible; remove competing page goals | `references/sections.md`, `references/copy.md` |
| Form completion is low | Keep only fields required for the stated next step; clarify data use and value exchange | `references/optimization.md` |
| An experiment is inconclusive | Keep the baseline, formulate one hypothesis, and extend or redesign the test using an adequate sample | `references/optimization.md` |

## Execution boundary

Use this skill to define or audit the conversion strategy and publishable content. Hand the approved requirements to the implementation workflow for UI code, design-system components, server-side forms, consent tooling, and deployment.

## Avoidable patterns

Replace vague promises, fabricated proof, unexplained scarcity, inaccessible controls, and simultaneous unrelated CTAs with specific, verifiable content and a coherent conversion path.
