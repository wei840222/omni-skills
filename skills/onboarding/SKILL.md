---
name: onboarding
description: >
  Design and optimize user onboarding flows that maximize activation and
  minimize time-to-value. Load when designing sign-up forms, empty states,
  checklists, first-run tours, onboarding email sequences, or activation metrics.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🚀","os":["linux","darwin","win32"],"displayName":"Onboarding"}'
  related-skills: '{"growth":"Use when onboarding is one stage inside a broader growth system or channel experiment program.","product":"Use for product strategy, PMF, and launch work beyond first-run activation.","product-manager":"Use for roadmap and requirement work that feeds onboarding scope.","retention":"Use after activation for cohort retention, churn prevention, and reactivation.","ux":"Use for broader UX research and interaction design outside first-run flows."}'
---

Use this skill for first-run activation design. Deeper research notes and source URLs live in `references/sources.md`.

Load `references/sources.md` when you need activation benchmarks, empty-state patterns, or lifecycle-email timing evidence.

## Define Activation First

Answer before designing anything:

- What specific action means the user got value?
- What % of signups currently reach it?
- What is the minimum path to get there?

If these are unanswered, onboarding will optimize the wrong metric.

## Measure the Funnel

Build the current-state table:

| Step | Users | Drop-off |
|------|-------|----------|
| Signed up | 100% | - |
| Step 2 | ?% | ?% |
| Step 3 | ?% | ?% |
| Activated | ?% | ?% |

Biggest drop-off first. Everything else is distraction.

## Signup Form

At signup, require only: email + password.
Defer every other field until after first value is delivered.

For each extra field, estimate: users lost × LTV = cost of that field.

## Segmentation Question

One question only, immediately after signup:

"What's your main goal?" with 3–4 options.

Route each answer to a different:

- First action
- Empty-state copy
- Email sequence

More than 4 paths adds complexity without benefit.

## Checklist Pattern

Structure:

- 4–6 items maximum
- First item already complete when shown (quick-win psychology)
- Order by value delivered, not internal logic
- Persist across sessions
- Show a visible completion reward

Format: action verb + outcome

- Good: "Create your first project"
- Weak: "Projects" (no action, no outcome)

## Empty State Formula

Every empty screen needs:

1. What will appear here (1 sentence)
2. Visual of the populated state or an example
3. ONE primary action button

Prefer pre-populated templates over a blank slate.

## Email Sequence

| Day | Trigger | Content |
|-----|---------|---------|
| 0 | Signup | Welcome + single quick-win CTA |
| 1 | Not activated | Reminder + how-to |
| 3 | Not activated | Social proof / success story |
| 7 | Not activated | Feature highlight |
| 14 | Inactive | "We miss you" + incentive |

Stop the sequence immediately when the user activates.

## Tooltips vs Modals

- **Tooltip**: single UI element, non-blocking
- **Modal**: requires a decision, blocks the UI
- **Tour**: max 3–5 steps or users skip

Show only to first-time users; skip returning users.
Trigger contextually, not on every login.

## Metrics

Track weekly:

- Signup → activation rate
- Time to activate (median)
- Drop-off by step
- Day 1 / Day 7 retention: activated vs non-activated

Activated users should retain about 2–3× better. If not, redefine activation.

## Common Failures

Prefer these safer defaults instead of the failure modes below:

- Collect details only after first value, not before buy-in
- Keep tours short; long tours raise skip rates
- Segment paths instead of one flow for everyone
- Send follow-up email when the tab may close after signup
- Demonstrate value before gating core features behind upgrade
