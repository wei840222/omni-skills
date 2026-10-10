# Setup - Safari Browser Control

Read this internally when `<state_root>/` is missing or empty. Keep the conversation natural and useful from the first reply. Explain storage only if the user asks or if trust depends on it.

## Your Attitude

- Make Safari control feel precise, explicit, and low-risk.
- Solve the current browser-control need first, then tighten activation defaults in the opening exchanges.
- Optimize for one verified action at a time. Avoid blind command spraying.

## Priority Order

### 1. First: Integration

Early in the conversation, confirm when this should activate:
- whenever Safari control, Safari automation, tab inspection, or Safari screenshots come up
- only when explicitly requested
- only for real-session Safari control, only for WebDriver setup, or both
- situations that should always stay out of scope

### 2. Then: Understand Their Control Surface

Learn the smallest set of details that changes the recommendation:
- whether the target is the real Safari session or an isolated session
- whether the immediate need is read, navigate, click, type, screenshot, or WebDriver launch
- whether direct Safari access exists right now
- whether the user is comfortable letting the agent touch their live tabs and cookies

### 3. Finally: Persistence and Boundaries

For recurring use, learn:
- whether Apple Events, Screen Recording, and WebDriver setup state should be remembered
- which commands or snippets are worth keeping
- which actions should always require explicit confirmation

## What You're Saving (internally)

- activation defaults and explicit boundaries in host memory when appropriate
- permission state, preferred control mode, snippets, recipes, and incident notes inside `<state_root>/`
- recurring no-go actions and reliable control patterns worth reusing

If the user approves local storage and `<state_root>/` does not exist, create it (after Gate 3 resolution in `SKILL.md`) and initialize `memory.md`, `permissions.md`, `sessions.md`, `snippets.md`, `recipes.md`, and `incidents.md` from `memory-template.md`.

## Default Behavior

- Start in read-and-verify mode. Avoid blind-control mode.
- Give one recommended next move first, then optional fallbacks if useful.
- Prefer read probes and screenshots before click or type actions.
- Keep privacy-sensitive surfaces explicit: open tabs, cookies, logins, clipboard, and screenshots.

## Guardrails

- Avoid implying you can see the live browser if direct Safari access is not available.
- Avoid asking for passwords, raw Keychain exports, or copied credential material.
- Verify focus before typing into Safari; do not send keystrokes when focus is uncertain unless the user approved that risk.
- Keep real-session control distinct from isolated WebDriver automation; do not treat them as equivalent.
