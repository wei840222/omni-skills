---
name: playwright
description: >
  Automate, test, and debug browsers with Playwright: locators, auto-waiting,
  traces, CI sharding, storageState auth, request mocking, visual diffs, and
  Playwright MCP control. Use when a test is flaky, times out, or fails only in
  CI/headless; when strict-mode locators match the wrong node; when waits become
  sleeps or networkidle never settles; for login setup, uploads/downloads,
  iframes, popups, accessibility checks, JS-rendered scraping, or porting from
  Cypress/Puppeteer/Selenium. Prefer `cypress` or `puppeteer` to maintain those
  suites, and `http` when a plain request already answers the need.
metadata:
  version: "1.0.4"
  openclaw: '{"emoji":"🎭","requires":{"bins":["node","npx"]}}'
  related-skills: '{"cypress":"Maintain or migrate an existing Cypress suite rather than Playwright-first work.","puppeteer":"Maintain Puppeteer automation outside the Playwright runner.","http":"Plain HTTP/API checks that do not need a real browser."}'
---

# Playwright

Agent guidance for **Playwright Test and browser automation**: durable locators,
web-first waits, isolation, traces, CI browsers, and MCP-driven live control.
Preserve useful intent from the original package; this entrypoint is the router.

Runtime artifacts (specs, traces, reports, snapshots, `storageState`) stay in the
repository or temp dirs — never inside preference state.

## When to load

- Writing or repairing Playwright specs, fixtures, `playwright.config.*`, or one-off scripts
- Failures: timeout, strict mode violation, flaky click, green local / red CI or headless-only
- Login reuse, uploads/downloads, iframes, popups/dialogs, device emulation
- Visual snapshots, accessibility checks, traces, sharding, suite wall-time cuts
- Live browser control via Playwright MCP, or extracting JS-rendered page data
- Porting Cypress / Puppeteer / Selenium habits into Playwright

Prefer other skills when the ask is mainly:

- Keeping a Cypress suite healthy → `cypress`
- Keeping Puppeteer scripts healthy → `puppeteer`
- API-only verification a fetch already covers → `http`

## State location

Optional operator preferences and memory may exist in `<workspace>/playwright/`,
`<workspace>/memory/playwright/`, or `~/playwright/`. Before the first state read
or write, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in that order.
3. If multiple candidates exist, use only the highest-precedence path and report duplicates — never merge silently.
4. If none exists and preferences must be saved, create `<workspace>/playwright/` only with user consent.

Use `<state_root>/config.yaml` and `<state_root>/memory.md` for declared preferences
only. Keep credentials, `storageState`, tokens, traces, videos, reports, and
snapshots out of `<state_root>/`; place those in gitignored repo paths or system temp.
Legacy paths such as `~/Clawic/data/playwright/` are migration sources only — copy
with user consent; do not auto-delete.

## Routing

Keep `SKILL.md` as the progressive-disclosure router; load the smallest relevant file:

| Situation | Load |
|---|---|
| First-use preferences / memory | `references/setup.md` |
| Config, projects, webServer, tags | `references/config.md` |
| CLI toolkit | `references/commands.md` |
| Locators / strict mode | `references/selectors.md` |
| Actionability and waits | `references/waiting.md` |
| What deserves an E2E, assert outcomes | `references/testing.md` |
| Fixtures, page objects, test data | `references/fixtures.md` |
| Auth / storageState / worker accounts | `references/auth.md` |
| Trace, headed repro, timeout triage | `references/debugging.md` |
| Local green / CI red, retries | `references/flake.md` |
| Browser install, channels, engines | `references/browsers.md` |
| CI image pin, artifacts, sharding | `references/ci-cd.md` |
| Contexts, popups, dialogs, permissions | `references/contexts.md` |
| route / HAR mock and replay | `references/network.md` |
| Upload, download, drag-drop | `references/files.md` |
| Screenshot diffs | `references/visual.md` |
| axe + keyboard a11y | `references/accessibility.md` |
| Suite wall time | `references/performance.md` |
| Playwright MCP live control | `references/mcp.md` |
| JS-rendered extraction | `references/scraping.md` |
| Cypress/Puppeteer/Selenium port | `references/migration.md` |
| Gate 6 sources | `references/sources.md` |

## Core rules

1. **Locate by what the user perceives.** Prefer role/label/text → test id → CSS/XPath. `getByRole('button', { name: 'Submit' })` survives class renames; bare `.nth()` is last resort when position is the behavior under test.
2. **Assert instead of sleeping.** Replace `waitForTimeout` with web-first assertions that poll until the expect timeout. Prefer explicit UI-state assertions over `networkidle` for SPA readiness.
3. **Budget timeouts; do not inflate globals.** Defaults: test 30s, expect 5s, action/navigation inherit the test ceiling, `webServer` 60s. Raise one slow assertion, not the suite default.
4. **One test, one fresh context, one owned account.** Contexts reset cookies/storage, not your database. Index worker accounts by `parallelIndex`.
5. **Capture before rewrite.** Use `trace: 'on-first-retry'` (or `--trace on`) and open the DOM snapshot before changing locators.
6. **Retries hide cost.** Keep limited retries while driving flaky count down; measure with `--repeat-each` before rewriting.
7. **Mock what you do not own; seed via API.** Click the UI only for the behavior under test unless the integration itself is the subject.
8. **Production and destructive flows are opt-in.** Real payments, deletions, or outbound mail need explicit session consent. Treat `storageState` as credentials — gitignore and never write into shared/synced preference folders.
9. **Pin browsers to the Playwright version.** CI image tags and cache keys must match installed `@playwright/test` exactly.

## Quick failure map

| Signature | First move |
|---|---|
| `strict mode violation: resolved to N elements` | Narrow with `.filter({ hasText })` or parent chain → `references/selectors.md` |
| `Timeout ... waiting for locator` | Locator never matched; trace it — do not raise timeout first → `references/debugging.md` |
| `element is not visible` / intercepts pointer | Overlay/animation/disabled; `force: true` hides the bug → `references/waiting.md` |
| Needs `waitForTimeout` to pass | Assert the state you were sleeping for → `references/waiting.md` |
| Green local, red CI/headless | Viewport, workers, timezone, animations, browser build → `references/flake.md`, `references/ci-cd.md` |
| Passes alone, fails in suite | Shared account/data or leaked storage → `references/auth.md` |
| Login every test | Setup project + `storageState` → `references/auth.md` |
| Snapshot differs by machine | Generate where CI runs; pin browser/OS → `references/visual.md` |

## Minimal patterns

Web-first assertion (no sleep):

```ts
await expect(page.getByRole('heading', { name: 'Dashboard' })).toBeVisible();
```

Strict-mode fix:

```ts
await page.getByRole('button', { name: 'Submit' }).click();
```

Reuse auth once:

```ts
// setup project writes storageState; tests load it via project dependencies
await page.context().storageState({ path: 'playwright/.auth/user.json' });
```

Reproduce with a trace:

```bash
npx playwright test path/to/spec.ts --headed --trace on
npx playwright show-trace test-results/**/trace.zip
```

## Safety

- Use placeholders for secrets; keep `storageState` / HAR with cookies out of git.
- Default automation targets local or staging; production mutations need explicit consent.
- Prefer placeholders in examples (`<BASE_URL>`, `<USER_EMAIL>`).
- Keep preference state free of credentials and run artifacts.

## Output gates

Before claiming a fix is done:

- No new `waitForTimeout` / `networkidle` readiness hacks without a documented exception
- Strict-mode violations resolved with specific locators, not blind `.first()`
- Assertions target user-visible outcomes
- CI config keeps `trace: 'on-first-retry'` (or equivalent) and uploads artifacts
- Headless/CI path uses version-pinned browsers
