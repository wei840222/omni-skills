# Setup — Android Studio

Read on first use when no `<state_root>/memory.md` exists, or when the user wants
proactive IDE coaching. Keep the conversation natural; do not dump a checklist.

## Attitude

Help the developer get more out of the IDE. Focus on productivity gains and tools
they may not already use.

## Priority order

### 1. Integration consent

Ask early:

- Whether they want Android Studio assistance while working on Android projects
- Tips proactively vs only when asked

Save the preference under `<state_root>/memory.md` only with consent.

### 2. Environment

Capture:

- Android Studio version / codename (confirm via **Help → About**, not guesswork)
- Platform keymap: macOS vs Windows/Linux
- Main project types: Compose, Views, mixed, multi-module
- Experience level (affects which features to highlight first)

### 3. Pain points

Ask what slows them down:

- Slow builds or Gradle sync
- Debugging / startup attach
- Navigation in large codebases
- Emulator or device connectivity

## State writes

Use `assets/memory-template.md`. Write only under the resolved `<state_root>/`.
Never store keystore paths with passphrases, CI tokens, or `local.properties` secrets.
