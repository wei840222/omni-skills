# Setup - multi-engine-web-search

Read this on first use or when memory is missing.

## Goal

Decide when this skill should activate and which engines should be prioritized so the user skips manual choice each time.

## First Conversation (3 quick questions)

Ask these in natural language:

1. Activation mode:
- always when internet lookup is needed
- only when user asks explicitly
- mixed mode (always for news/facts, explicit for everything else)

2. Engine preference order:
- ask for top 3 preferred engines
- ask which engines to exclude

3. Search style:
- speed-first (fewer engines)
- balance (default)
- evidence-first (more cross-checking)

## Save Behavior

- Save user preferences in `<state_root>/memory.md` only after resolving `<state_root>` per `SKILL.md`.
- Optionally mirror a short activation preference into the host's main agent memory when the user wants automatic future routing.
- If the user is unsure, apply this default profile:
  - activation: mixed mode
  - priority: Google -> DuckDuckGo -> Brave -> Bing
  - blocked engines: none
  - style: balance

## Updates

If the user changes preference, update `<state_root>/memory.md` immediately and confirm the new behavior in one sentence.
