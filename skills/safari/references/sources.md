# Verified sources (Gate 6)

Retrieval window for this refactor: 2026-10-11. Re-open these pages before restating version-sensitive Safari, WebDriver, or Agent Skills claims.

## Agent Skills package format

- **Agent Skills specification** — https://agentskills.io/specification
- **Document index** — https://agentskills.io/llms.txt
- **Best practices for skill creators** — https://agentskills.io/skill-creation/best-practices
- **Optimizing skill descriptions** — https://agentskills.io/skill-creation/optimizing-descriptions
- **Reference validator package** — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Safari WebDriver / WebKit

- **Testing with WebDriver in Safari (Apple Developer)** — https://developer.apple.com/documentation/webkit/testing-with-webdriver-in-safari
- **About WebDriver for Safari (Apple Developer)** — https://developer.apple.com/documentation/webkit/about_webdriver_for_safari
- **WebDriver support in Safari 10 (WebKit blog)** — https://webkit.org/blog/6900/webdriver-support-in-safari-10/
- **Safari developer tools hub** — https://developer.apple.com/documentation/safari-developer-tools

## macOS automation boundaries

- Apple Events / Automation permission is **per controlling app** (Terminal vs iTerm vs other hosts do not share approval).
- Screen Recording is separate from Automation; presence of `screencapture` does not prove permission.
- `safaridriver` sessions are automation sessions; do not treat them as automatic control of the user's already-open daily tabs unless that exact setup was verified.

## Fragile claims

- Do not claim WebDriver automatically shares cookies, tabs, or login state with the visible Safari UI.
- Do not teach blind `System Events` keystrokes without focus verification.
- Do not assert cross-platform Safari control; this skill is `darwin`-only.
- Do not invent BiDi flag matrices from memory; confirm against current `safaridriver` help and Apple WebDriver docs for the installed macOS/Safari version.
