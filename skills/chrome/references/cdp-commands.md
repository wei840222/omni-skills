# Core CDP commands

Parameter names below were checked against tip-of-tree `browser_protocol.json` / `js_protocol.json` during this refactor. Re-open the protocol viewer before asserting new fields.

## Domain enablement

- `Runtime.enable` — start execution-context reporting (`executionContextCreated`).
- `Page.enable` — page domain notifications.
- `Network.enable` — network events; optional buffer size params for payload retention.

Call these **before** evaluate/navigate/body reads.

## Navigation and evaluate

- `Page.navigate` — required `url`; optional referrer, frameId, transitionType.
- `Runtime.evaluate` — run expression in a context; wait for the response with the same command `id`.

## Screenshot

`Page.captureScreenshot` parameters include:

- `format` (png/jpeg/webp)
- `quality` (jpeg)
- `clip` (Viewport)
- `fromSurface` (boolean; capture from surface rather than view; defaults true in recent protocol)
- `captureBeyondViewport`
- `optimizeForSpeed`

There is **no** `scale` parameter on `Page.captureScreenshot`. For high-DPI / Retina-like output:

1. Keep `fromSurface: true` when surface capture is desired.
2. Use `Emulation.setDeviceMetricsOverride` with an appropriate `deviceScaleFactor` (and width/height/mobile as needed).
3. Then capture.

Docs: https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-captureScreenshot

## Network body

1. `Network.enable`
2. Observe `Network.responseReceived` and `Network.loadingFinished` (body is not inline on responseReceived).
3. `Network.getResponseBody` with `requestId` → `{ body, base64Encoded }`.

## Blocking without full intercept

`Network.setBlockedURLs` accepts URL patterns (`urls` and/or `urlPatterns`). Apply **before** navigation you want blocked.
