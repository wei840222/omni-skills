# Core Rules

## 1. Start from Product Intent and State Change
- Define the trigger, user goal, and state transition before choosing an effect.
- Map motion to one of five jobs: orientation, feedback, continuity, emphasis, or delight.
- Wait for clear intent before animating.

## 2. Write a Motion Contract Before Code
Every proposal must specify:
- Trigger and affected surfaces
- Initial state, end state, and reduced-motion fallback
- Duration, easing or spring, delay or stagger, and cancellation behavior
- Acceptance criteria: responsiveness, accessibility, parity, and performance

No vague wording like "smooth" or "premium" without values.

## 3. Route to the Safest Native Abstraction
Use the highest-level API that solves the job:
- Flutter: implicit animation widgets, `AnimatedSwitcher`, `TweenAnimationBuilder`, `Hero`
- React and Next.js: CSS-first transitions, Motion presence/layout APIs, and router-safe transitions before bespoke choreography
- SwiftUI: `withAnimation`, content transitions, `matchedGeometryEffect`
- Compose: `animate*AsState`, `AnimatedVisibility`, `updateTransition`
- React Native: native-thread or worklet-safe animation paths before JS-thread choreography
- Web: CSS `transform` and `opacity`, View Transitions, or framework-native transitions before GSAP-level complexity

Use higher-level primitives for interruption and lifecycle over low-level animation code.

## 4. Optimize for Compositor-Safe Motion and Interruption
- Prefer transform, opacity, color, and scale patterns that keep layout stable.
- Reserve width, height, top, left, and layout-driven loops for stacks providing a dedicated layout animation primitive.
- Define behavior for rapid taps, back gestures, dismiss, re-render, offscreen, and navigation cancel.
- Ensure users can always bypass or interrupt animations.

## 5. Ship Accessible Variants by Default
- Respect reduced-motion and system animation-scale settings.
- Replace large travel, parallax, bounce, blur-heavy flourishes, and infinite loops with calmer equivalents.
- Use multiple signals (color, text, icon) alongside movement to communicate status.
- Keep focus order, screen reader output, and hit targets stable during motion.

## 6. Cover Real Product States Including Edge Cases
- Animate loading, success, error, empty, disabled, retry, and optimistic-update states when relevant.
- Coordinate navigation, overlays, lists, forms, and async data so motion still works with latency and content changes.
- Deliver a sober V1 first, then a more expressive V2 only when constraints allow.

## 7. Verify with Previews, Tests, and Device Reality
- Leave deterministic previews, stories, or demo toggles for the motion states you touched.
- Add or update behavior, E2E, or visual tests when the app stack supports them.
- Validate reduced motion, mid-tier performance, and interrupted flows before calling it done.

## Common Traps

- Pretty animation without a user-facing reason -> extra motion, less clarity.
- Hardcoded timings per screen -> inconsistent product feel and painful iteration.
- JS or main-thread choreography for critical mobile motion -> dropped frames under load.
- Animating only happy-path states -> broken UX on loading, error, or rapid retries.
- Missing cancellation rules -> stuck overlays, ghost states, or navigation glitches.
- Shipping only one variant -> accessibility regressions and poor low-end performance.
