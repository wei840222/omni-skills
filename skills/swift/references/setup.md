# Setup — Swift

Read this on first use to load user preferences. Proceed without interviewing the user.

## Your Attitude

Swift is safe by construction and unforgiving when you route around that safety. Write code that survives review: no silent force unwraps, no isolation holes, no error swallowed on the way out. Explain the failure mode, not just the fix.

## How To Load Preferences

1. Read `<state_root>/config.yaml` if it exists. Apply its values.
2. For anything absent, use the defaults in the Configuration table of `SKILL.md` — use the defaults silently.
   - `swift_language_mode: 5` (unless the project specifies otherwise), `build_tool: swiftpm`, `test_framework: swift-testing`, `target_platforms: apple`, `deployment_floor: none`, `force_unwrap_policy: tests-only`.
3. Read `<state_root>/memory.md` for prior context (their stack, recurring pain points). Absence is fine; proceed without comment.

Infer what the project already tells you before falling back to a default: `Package.swift` names the tools version, platforms, and language mode; the test target names the framework. What the repository states beats the table.

## Recording Preferences (on explicit save request)

When the user explicitly asks to save a preference or correction, resolve `<state_root>` using `SKILL.md`, inspect any existing file, then update only the corresponding record if host policy permits. A preference stated for the current task is applied now without automatically persisting it.

- On an authorized save, a named language mode, build tool, test framework, target platform, OS floor, or unwrap policy → update the matching key in `<state_root>/config.yaml`.
- On an authorized save, a stated habit or stance (formatter and rule set, access-control conventions, dependency appetite, diff vs full files, test-first) → record it under the relevant preference area in `<state_root>/memory.md`.
- On an authorized save, a correction → update the stored value so the correction is not needed twice.

Without an explicit request to save, store nothing. Both config.yaml and memory.md are optional; create only the requested child when an authorized write needs it.

## What Memory Holds

See `../assets/memory-template.md` for the file format. Track their project shape (app, library, server), the frameworks in play, migration state, and recurring pain points — but only from what they actually reveal.
