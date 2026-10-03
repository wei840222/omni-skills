# Gate 6 sources (verified at handoff)

Primary documentation used to check locators, auto-waiting, traces, auth, CI browsers, and MCP claims. Re-open the live page before restating defaults or flag names.

| Topic | Source | URL | Takeaway used in skill |
| --- | --- | --- | --- |
| Docs home | Playwright documentation | https://playwright.dev/docs/intro | Entry map for Test, library, and release notes. |
| Locators | Locators | https://playwright.dev/docs/locators | User-facing locators first; strict mode; filtering. |
| Auto-waiting | Actionability | https://playwright.dev/docs/actionability | Built-in actionability checks; avoid manual sleeps. |
| Assertions | Assertions | https://playwright.dev/docs/test-assertions | Web-first assertions re-poll until timeout. |
| Timeouts | Timeouts | https://playwright.dev/docs/test-timeouts | Test/expect/action timeout relationship. |
| Auth | Authentication | https://playwright.dev/docs/auth | setup projects and `storageState` reuse. |
| Traces | Trace viewer | https://playwright.dev/docs/trace-viewer-intro | `on-first-retry`, show-trace workflow. |
| CI | CI introduction | https://playwright.dev/docs/ci-intro | Official CI images and browser install. |
| Browsers | Browsers | https://playwright.dev/docs/browsers | Version-locked browser installs and channels. |
| Network | Network | https://playwright.dev/docs/network | `route`, HAR, and mocking guidance. |
| Best practices | Best practices | https://playwright.dev/docs/best-practices | Testing pyramid habits Playwright documents. |
| MCP | Playwright MCP | https://github.com/microsoft/playwright-mcp | Snapshot-driven MCP browser control package. |
| Agent Skills format | Agent Skills specification | https://agentskills.io/specification | Frontmatter, progressive disclosure, package layout. |
| Reference validator | agentskills / skills-ref | https://github.com/agentskills/agentskills/tree/main/skills-ref | `uvx --from skills-ref agentskills validate skills/playwright`. |

## Operational notes retained (not live measurements)

- Default test timeout 30s and expect timeout 5s follow Playwright Test docs at handoff time; always re-check the timeouts page before changing project defaults.
- Official Microsoft Playwright container tags must match the installed `@playwright/test` version exactly.
- `networkidle` remains discouraged for SPA readiness in current docs; prefer explicit UI assertions.

Handoff verification date: 2026-10-03 (local takeover of Jules session 13287972543154995167).
