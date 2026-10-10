---
name: safari
description: >
  Control Safari on macOS via AppleScript (real session tabs/cookies),
  safaridriver/WebDriver (isolated automation), screenshots, tab navigation,
  and verified read/click/type loops. Use for live Safari control, permission
  preflight, or Safari-only WebDriver. Prefer `playwright` for generic browser
  automation; `applescript`/`macos` for deeper script or permission work;
  `passkey` for WebAuthn; not for non-Safari browsers.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧭","os":["darwin"],"requires":{"bins":["osascript","safaridriver","screencapture"]}}'
  related-skills: '{"applescript":"Deeper AppleScript design beyond known-good Safari snippets.","macos":"Apple Events, Screen Recording, focus, and native macOS diagnostics.","playwright":"Cross-browser product automation once the task leaves real Safari.","ios":"Safari-adjacent flows that move to iPhone or iPad.","passkey":"Safari sign-in and WebAuthn without guessing credential rules."}'
---

# Safari

Own **macOS Safari control**: real-session AppleScript, isolated `safaridriver`/WebDriver, permission preflight, and screenshot verification. This skill does not replace Playwright for generic browser product automation.

## State location

Safari control notes may exist in `<workspace>/safari/`, `<workspace>/memory/safari/`, or `~/safari/`.
Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one; resolve it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/safari/`, `<workspace>/memory/safari/`, `~/safari/`.
3. If multiple candidates exist, keep only the highest-precedence directory, report the conflict, and leave siblings unchanged.
4. If none exists and notes must be created, default to `<workspace>/safari/` only after brief consent.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd. An existing `~/safari/` may be read; otherwise ask before creating data.
6. Keep the selected `<state_root>` fixed for the whole invocation.

Use the selected `<state_root>` for every state path in this skill. Outside this section, every skill-state path uses `<state_root>/...`. Skill resources stay under `references/`. Do not treat the literal string `<state_root>` as a filesystem path. Do not write passwords, cookies, full history exports, Keychain material, or raw credential blobs into state files. Do not write learned preferences into `SKILL.md`.

Default note files (create on first authorized write):

| File | Purpose |
| --- | --- |
| `<state_root>/memory.md` | Activation defaults, preferred control mode, guardrails |
| `<state_root>/permissions.md` | Automation, Develop menu, screenshot preflight state |
| `<state_root>/sessions.md` | Real-session vs WebDriver notes and target tabs |
| `<state_root>/snippets.md` | Known-good AppleScript and shell patterns |
| `<state_root>/recipes.md` | High-value task recipes (read, click, fill, capture) |
| `<state_root>/incidents.md` | Permission failures, blocked JS, repeat breakages |

Load `references/memory-template.md` for templates. Load `references/setup.md` only when onboarding or `<state_root>` is empty.

## When to load

- Control the user's real Safari session (open tabs, cookies, login state)
- Run Safari-specific `safaridriver` / WebDriver / BiDi isolation
- Preflight Apple Events, Screen Recording, or JavaScript-from-automation
- Screenshot-verify layout, focus, or post-action page state
- Hand off when the need becomes generic multi-browser automation (`playwright`)

## Workflow

1. Classify: real AppleScript session vs isolated WebDriver vs permission-only debug.
2. Resolve `<state_root>` only when notes or prior permission state matter; otherwise stay stateless.
3. Run the lowest-risk read probe before click, type, or screenshot.
4. One action → one verification (re-read title/URL/DOM or screenshot).
5. Re-open `references/sources.md` before restating version-sensitive WebDriver/Safari claims.
6. Keep the description trigger-focused: real Safari / safaridriver / permissions — not generic browser QA.

| Need | Load |
| --- | --- |
| Architecture, rules, traps, security | `references/domain.md` |
| Onboarding and activation defaults | `references/setup.md` |
| State file templates | `references/memory-template.md` |
| Permissions and preflight probes | `references/preflight-and-permissions.md` |
| Real-session AppleScript commands | `references/applescript-control.md` |
| `safaridriver`, WebDriver, BiDi | `references/webdriver-and-bidi.md` |
| Screenshot feedback loop | `references/screenshot-and-visual-loop.md` |
| Failure ladder and recovery | `references/troubleshooting.md` |
| Verified official sources | `references/sources.md` |

## Minimum viable defaults

1. **Pick the control surface first** — AppleScript for live tabs/cookies; `safaridriver` for isolated automation. Do not blur them.
2. **Preflight read before mutate** — e.g. `osascript -e 'tell application "Safari" to get name of front window'`.
3. **Verify after every action** — command exit 0 is not proof of visible Safari state.
4. **Treat real Safari as high-trust** — ask before activate, switch tab, type, click, copy page data, or capture screens that may show personal content.
5. **Verify focus before keystrokes** — prefer DOM input with read-back over blind `System Events` typing.
6. **Route adjacencies** — deep AppleScript → `applescript`; macOS permissions/focus → `macos`; generic automation → `playwright`; WebAuthn → `passkey`; iPhone/iPad → `ios`.

## Failure branches

| Condition | Action |
| --- | --- |
| AppleScript no response | Check Automation permission for **this** terminal app; retry simplest probe; launch Safari if needed |
| `do JavaScript` blocked | Confirm normal web tab (not internal UI); resolve Develop/automation JS path; fall back to tab metadata |
| `safaridriver` fails | `safaridriver --enable`; start `safaridriver -p 0`; add `--diagnose` only after simple start fails |
| Typing wrong place | Halt keystrokes; re-activate Safari; verify tab + focused element; switch to DOM input |
| Screenshot mismatch | Confirm front window; re-capture after bringing Safari forward; check focus steal |
| Task needs logged-in real tabs | Prefer AppleScript mode; do not promise WebDriver inherits daily tabs |

## Safety defaults

- macOS + Safari required (`osascript`, `safaridriver`, `screencapture`). Document `darwin` honestly; do not fake portability.
- No undeclared network from this skill. Page navigation only when the user authorized that target.
- Do not request passwords, raw Keychain exports, or copied credential material.
- Prefer dedicated Safari profile or WebDriver for risky/repetitive automation over daily browsing profile.
- Keep writes inside resolved `<state_root>/` with consent; do not commit runtime memory into the package.
- Load at most one deep reference per step; keep always-on defaults in this file only.
