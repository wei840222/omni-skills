---
name: animate
description: >
  Design and implement product UI motion systems across Flutter, React/Next.js,
  SwiftUI, Jetpack Compose, React Native, and web. Use for micro-interactions,
  navigation/shared-element transitions, modals/sheets, loading feedback,
  gesture response, motion tokens, reduced-motion fallbacks, and QA acceptance
  criteria. Prefer media/video tools for timeline editing or GIF encoding; prefer
  `design` / `figma` for pure visual taste or canvas mechanics without motion
  implementation.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎞️","requires":{"config":["<state_root>"]}}'
  related-skills: '{"flutter":"Flutter widget and navigation implementation beyond generic motion contracts.","react":"React/Next component and router patterns when motion is only one layer.","react-native":"RN/worklet/native-driver specifics past shared motion rules.","swift":"Swift/SwiftUI host patterns when Apple-platform motion is the main stack.","android":"Android/Compose platform constraints beyond cross-stack motion defaults.","design":"Visual design judgment when taste leads and motion is secondary.","figma":"Figma prototype and Smart Animate mechanics inside the design file.","frontend":"Broader web front-end architecture around CSS/JS motion choices.","css":"CSS transition/animation syntax depth without multi-stack product motion routing.","ui":"General UI product patterns when animation is not the primary ask.","animations":"Broader animation craft or non-product motion when not shipping app UI systems."}'
---

## State location

Animate preferences may exist in `<workspace>/animate/`, `<workspace>/memory/animate/`, or `~/animate/`.
`<workspace>` means the workspace root provided by the host/runtime, not the shell cwd.

Before any state read or write, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/animate/`, `<workspace>/memory/animate/`, `~/animate/`.
3. If multiple candidates exist, keep only the highest-precedence directory, leave others untouched, and tell the user which location was selected.
4. If none exists and persistent state must be created, default to `<workspace>/animate/` after brief first-write consent.

Use the selected `<state_root>` for every state path in this skill. Never write the literal string `<state_root>` to disk. Skill package files stay under `references/` and `assets/`; never write learned data into `SKILL.md`.

Legacy path `~/Clawic/data/animate/` is a migration source only. It is outside active lookup. Copy, validate, cut over, and keep a rollback path only after the user chooses migration.

```text
<state_root>/
├── memory.md          # Durable motion preferences and platform context
├── tokens.md          # Approved duration, easing, and spring ladders
├── patterns.md        # Proven interaction and transition patterns
├── platform-notes.md  # Stack-specific implementation decisions
└── qa.md              # Regressions, low-end findings, accessibility notes
```

## When to load

Load this skill when the user needs **product UI motion** designed or implemented:

- micro-interactions, press/hover feedback, toggles, forms
- navigation, shared-element, modal/sheet/drawer transitions
- loading, success, error, retry, optimistic-update motion
- cross-stack motion systems, tokens, reduced-motion fallbacks, QA criteria

Route away when the primary task is:

- pure visual taste without implementation → `design`
- Figma canvas/prototype mechanics → `figma`
- CSS syntax-only depth without product motion routing → `css`
- non-product / media timeline animation → media tools or `animations`
- stack framework work with no motion contract → `flutter` / `react` / `react-native` / `swift` / `android` / `frontend`

## Setup

After resolving `<state_root>`, if `<state_root>/memory.md` is missing or empty, read `references/setup.md` and follow it while still answering the current motion question first. Confirm before the first durable write. File shape: `assets/memory-template.md`.

## When to load references

Keep this file as the router; load the smallest matching reference.

| Need | File |
|------|------|
| Setup / activation preferences | `references/setup.md` |
| Memory file template | `assets/memory-template.md` |
| Core rules and failure traps | `references/core-rules.md` |
| Motion brief, tokens, contract | `references/motion-system.md` |
| Stack routing (Flutter…web) | `references/platform-routing.md` |
| Starter snippets by stack | `references/implementation-snippets.md` |
| Pattern catalog | `references/pattern-catalog.md` |
| Performance + accessibility | `references/performance-accessibility.md` |
| QA / regression checklist | `references/qa-playbook.md` |
| Security and privacy | `references/security-privacy.md` |
| Gate 6 verified sources | `references/sources.md` |

## Operating loop

1. **Clarify the motion job** — trigger, state change, intent (orientation / feedback / continuity / emphasis / delight), stack, and constraints.
2. **Write a motion contract** before code — initial/end state, duration or spring, interruption/cancel, reduced-motion fallback, acceptance criteria. Ban vague “smooth/premium” without values.
3. **Route to the safest high-level API** for the stack (`references/platform-routing.md`); drop lower only when lifecycle or gesture needs force it.
4. **Ship accessible + interruptible defaults** — compositor-safe properties, reduced-motion variant, focus/hit-target stability, real device budget.
5. **Verify** with preview/story, interrupted input, reduced motion, and mid-tier performance before calling done (`references/qa-playbook.md`).
6. **Persist only reusable defaults** under `<state_root>/` when consent allows.

## Core rules

1. Motion maps to a user-facing state change, not decoration.
2. Every deliverable includes a reduced-motion path and cancellation behavior.
3. Prefer `transform` / `opacity` / stack-native layout animation primitives; avoid layout thrash and infinite ornamental loops.
4. Cover loading, error, empty, disabled, retry, and optimistic paths when relevant.
5. Leave deterministic previews or tests for critical animated flows when the stack supports them.
6. Do not store secrets or unnecessary personal data in motion memory.

## Failure modes

| Condition | Response |
|-----------|----------|
| No `<state_root>` yet | Resolve per State location; answer first; ask once before create |
| Request is “make it smooth” only | Force a motion contract with numbers and fallback |
| Stack unclear | Ask one clarifying question; propose a stack-neutral contract meantime |
| Reduced motion required | Swap travel/bounce/parallax for opacity/color/instant confirm |
| Conflicting candidate state dirs | Highest precedence only; report conflict |
| Media/video editing ask | Route out; do not stretch this skill into encoders |

## Out of scope

- Video editing, GIF/Lottie authoring pipelines, or media encoding
- Pure graphic-design taste without product motion implementation
- Disabling OS accessibility animation settings for the user
- Rewriting this skill package from runtime memory

## Safety

- Examples use placeholders only; never commit real tokens or private paths.
- Memory writes stay under the resolved `<state_root>/` after consent.
- Do not exfiltrate motion notes, device inventories, or user identifiers.