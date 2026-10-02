# Research sources (Gate 6)

Primary URLs used while verifying product UI motion guidance. Prefer these over memory when citing platform APIs, accessibility requirements, or timing defaults. Links below returned HTTP 200 at edit time (2026-10-02) with a normal browser UA unless noted.

## Cross-cutting accessibility and reduced motion

- **MDN — `prefers-reduced-motion`** — media query semantics and CSS examples — https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
- **web.dev — prefers-reduced-motion** — practical reduced-motion patterns for the web — https://web.dev/articles/prefers-reduced-motion
- **W3C WCAG 2.2** — normative accessibility success criteria including motion-related guidance — https://www.w3.org/TR/WCAG22/
- **WAI — Animation from interactions (WCAG understanding)** — why interaction-triggered animation needs control/fallback — https://www.w3.org/WAI/WCAG21/Understanding/animation-from-interactions

## Flutter

- **Flutter — Animations** — implicit/explicit animation model and widgets — https://docs.flutter.dev/ui/animations
- **Flutter — Accessibility** — accessibility and animation-related platform considerations — https://docs.flutter.dev/ui/accessibility-and-internationalization/accessibility

## React / web motion

- **Motion docs** — modern Motion (Framer Motion lineage) presence/layout APIs — https://motion.dev/docs
- **Framer Motion** — product documentation hub for React motion primitives — https://www.framer.com/motion/
- **MDN — View Transitions API** — document/same-document view transitions — https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API

## Apple platforms

- **Apple HIG — Motion** — motion principles for Apple platforms — https://developer.apple.com/design/human-interface-guidelines/motion
- **SwiftUI — Animation** — animation values and timing curves — https://developer.apple.com/documentation/swiftui/animation
- **SwiftUI — `animation(_:value:)`** — value-driven view animation — https://developer.apple.com/documentation/swiftui/view/animation(_:value:)

## Android / Compose / Material

- **Compose Animation introduction** — high-level Compose animation APIs — https://developer.android.com/develop/ui/compose/animation/introduction
- **Material 3 — Motion overview** — how Material motion works — https://m3.material.io/styles/motion/overview/how-it-works
- **Material 3 — Easing and duration** — applying easing and duration tokens — https://m3.material.io/styles/motion/easing-and-duration/applying-easing-and-duration

## React Native

- **React Native — Animated** — Animated API and native-driver guidance — https://reactnative.dev/docs/animated

## Agent Skills format (repo gates)

- Agent Skills document index — https://agentskills.io/llms.txt
- Agent Skills specification — https://agentskills.io/specification
- Optional directories — https://agentskills.io/specification#optional-directories
- Progressive disclosure — https://agentskills.io/specification#progressive-disclosure
- File references — https://agentskills.io/specification#file-references
- skills-ref validator package — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Notes for maintainers

- This skill is **product UI motion systems**, not video editing or media encoding.
- Timing ladders are engineering defaults; replace with design-system tokens when the product already defines them.
- When adding factual claims (API names, plan gates, a11y criteria), append the full URL here and in the PR Research Sources section.