---
name: frontend
description: >
  Guide frontend UI implementation with React, Next.js, Tailwind, typography,
  color systems, mobile-first layout, accessibility, Core Web Vitals, and
  interaction feedback. Use when building landing pages, dashboards, forms,
  component libraries, or polishing production web UI. Prefer `design` for
  quantified visual critique, `css`/`tailwindcss` for stylesheet mechanics,
  `react`/`nextjs` for framework internals, `ux` for heuristic flow review,
  `forms`/`dashboard` for specialized surfaces, and `inspiration` for gallery
  references before coding.
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"🖥️"}'
  related-skills: '{"css":"Cascade, layout bugs, and render-performance CSS outside Tailwind-first guidance.","dashboard":"Analytics dashboard IA and chart/table composition beyond generic frontend patterns.","design":"Quantified hierarchy, spacing, and visual critique before implementation.","design-system":"Token and component-system governance across products.","forms":"Multi-step form validation, error recovery, and field UX beyond general traps.","inspiration":"Gallery and screenshot references before committing to an aesthetic.","nextjs":"App Router, RSC, caching, and Next.js deployment mechanics.","react":"React component patterns, hooks, and state beyond stack recommendations.","tailwindcss":"Utility-class debugging, theme config, and Tailwind build setup.","ux":"Nielsen heuristics and cognitive-load review of flows rather than visual implementation."}'
---

# Frontend

Ship production web UI with a mobile-first stack, distinctive typography,
purposeful color, accessible interaction, and Core Web Vitals targets. This
skill is **knowledge-only guidance**: it does not create a persistent state
tree and does not call network APIs or store user data.

## Quick Reference

| Topic | Load when | File |
|-------|-----------|------|
| Stack & tooling | Choosing Next.js/Tailwind/shadcn defaults | `references/stack.md` |
| Typography rules | Font pairing, scale, measure | `references/typography.md` |
| Color systems | 70-20-10, themes, depth | `references/colors.md` |
| Mobile patterns | Breakpoints, touch, stacking | `references/mobile.md` |
| Animation | Motion budget, reduced-motion | `references/animation.md` |
| Examples | Landing, dashboard, checkout prompts | `references/examples.md` |

## Core Rules

### 1. Mobile-First Always
- Start with a single-column mobile layout, then enhance upward
- Collapse every multi-column grid to one column below the first breakpoint
- Keep interactive targets at least **44×44 CSS px** (WCAG 2.2 target-size guidance)
- Validate on real devices, not only simulators

### 2. Typography Matters
- Prefer distinctive fonts over generic stacks (Inter, Roboto, Arial)
- Use dramatic size jumps (2×+), not timid increments
- Keep body text at 16–18px minimum with ~65–75 character measure
- See `references/typography.md` for pairings and scale

### 3. Color with Purpose
- Apply the 70-20-10 rule: primary, secondary, accent
- Commit to light **or** dark; avoid muddy mid-gray themes
- Prefer depth via gradients, grain, or layered surfaces instead of flat solid white
- See `references/colors.md` for CSS variables and patterns

### 4. Feedback on Every Interaction
- Acknowledge taps within ~100ms
- Prefer optimistic updates when rollback is safe
- Show loading states for operations longer than ~1s
- Preserve user input when validation or submit fails

### 5. Accessibility Non-Negotiable
- Text contrast ≥ 4.5:1; UI-component contrast ≥ 3:1
- Visible focus on every interactive control
- Semantic landmarks (`nav`, `main`, `section`, `article`)
- Full keyboard paths for primary flows

### 6. Performance from Start
- Lazy-load below-fold media and heavy widgets
- Reserve image space to limit layout shift
- Code-split large feature islands
- Target **LCP < 2.5s** and **CLS < 0.1** (web.dev Core Web Vitals)

### 7. One Memorable Element
- Give each page one deliberate memorable treatment (type, hero motion, or layout)
- Commit to an aesthetic; timid mid designs usually fail review

## Frontend Traps

| Trap | Consequence | Fix |
|------|-------------|-----|
| Generic fonts | Looks interchangeable | Distinctive display + body pairing |
| Flat solid backgrounds | Lifeless surface | Gradients, grain, layered depth |
| Desktop-first layout | Breaks majority mobile traffic | Mobile-first single column first |
| Form error clears input | User rage / abandoned submit | Preserve input, highlight the field |
| Missing loading states | Feels broken | Immediate progress feedback |
| Timid type scale | Weak hierarchy | 2×+ jumps for headlines |

## Scope

In scope:
- Frontend patterns and production polish guidelines
- Stack and tooling recommendations (React, Next.js, Tailwind, shadcn/ui)
- Responsive, accessible, performant implementation guidance

Out of scope (hand off instead):
- Network requests, auth, or data persistence owned by backend skills
- Quantified visual critique without implementation → `design`
- Deep CSS cascade debugging → `css`; Tailwind build/theme debugging → `tailwindcss`
- React/Next.js framework internals → `react` / `nextjs`
- Heuristic UX audit of flows → `ux`
- Pure inspiration galleries → `inspiration`

## Security & Privacy

Read-only guidance only. Do not collect, send, or store user data through this skill.
