# Chrome domain defaults

## Always-on checklist

1. Discover targets with `GET /json/list` (or `/json`) before opening a WebSocket.
2. Use the target's `webSocketDebuggerUrl`; browser-root and page targets differ.
3. Enable domains before dependent commands (`Runtime`, `Page`, `Network`, `Fetch` as needed).
4. Treat CDP as async: every command needs a unique `id` and a matching response.
5. Prefer Playwright/Puppeteer for product automation; use this skill for protocol/extension diagnostics.

## Common traps

| Trap | Correct path |
| --- | --- |
| Hard-code `ws://localhost:9222/devtools/browser` for page work | List targets; attach to the page entry |
| Call `Page.navigate` / `Runtime.evaluate` before enable | `Page.enable` / `Runtime.enable` first |
| Expect body on `Network.responseReceived` | Follow with `Network.getResponseBody` after load finishes |
| Teach `Network.setRequestInterception` as current API | Use **Fetch** domain (`enable` → `requestPaused` → continue/fail/fulfill) |
| Assume `Page.captureScreenshot` has `scale` | Use `fromSurface`; set DPI via `Emulation.setDeviceMetricsOverride.deviceScaleFactor` |
| MV3 globals across events | `chrome.storage.*` + `chrome.alarms`; workers are ephemeral |
| Content script reads `window.appState` | Inject into page world or bridge with `postMessage` |

## Routing

- Flaky E2E / locators / traces → `playwright`
- Existing Puppeteer scripts → `puppeteer`
- Cypress suite → `cypress`
- Page JS without DevTools → `javascript` / `web`
