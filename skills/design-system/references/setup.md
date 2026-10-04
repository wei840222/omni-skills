# Setup — Design System

Read this when `<state_root>/` does not exist or is empty. Start the conversation naturally.

## Attitude

Help the user build a coherent visual language. A durable design system reduces one-off styling bugs and repeated redesign work.

## Priority order

### 1. Integration (first 2–3 exchanges)

Ask how they want help to run:

- Advise only vs enforce tokens when editing UI
- Which platforms matter first (web, native, design tools)

Save the integration preference to `<state_root>/memory.md` after consent to create state.

### 2. Situation

Explore only what changes the system shape:

- Existing system vs greenfield
- Platforms (web only, web + mobile, Figma variables)
- Stack (Tailwind, CSS variables, CSS-in-JS, native)
- Solo vs team documentation needs
- Existing tokens or patterns to preserve

Reflect back understanding before large structural proposals.

### 3. Depth on request

Some users want full token architecture; others want a thin starter kit. Adapt:

- Color strategy (primaries, semantic roles)
- Spacing base (4px vs 8px)
- Type scale (modular ratio vs fixed steps)
- Dark mode approach

## What you save

In `<state_root>/memory.md`:

- stack and platforms
- patterns to preserve
- documentation preferences
- team context
- constraints called out by the user

Optional drafts under `<state_root>/tokens/` only when the user wants exported artifacts kept across sessions.
