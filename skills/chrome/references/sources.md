# Verified sources (Gate 6)

Retrieval window for this refactor: 2026-10-10. Re-open these pages before restating version-sensitive CDP or MV3 claims.

## Agent Skills package format

- **Agent Skills specification** — frontmatter and resource layout via https://agentskills.io/specification
- **Document index** — https://agentskills.io/llms.txt
- **Reference validator package** — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Chrome DevTools Protocol

- **Protocol viewer (endpoints, scope, multi-client)** — https://chromedevtools.github.io/devtools-protocol/
- **Tip-of-tree Page domain / captureScreenshot** — https://chromedevtools.github.io/devtools-protocol/tot/Page/#method-captureScreenshot
- **Fetch domain** — https://chromedevtools.github.io/devtools-protocol/tot/Fetch/
- **Network domain** — https://chromedevtools.github.io/devtools-protocol/tot/Network/
- **devtools-protocol definitions repo** — https://github.com/ChromeDevTools/devtools-protocol
- **browser_protocol.json (machine-readable)** — https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/master/json/browser_protocol.json
- **js_protocol.json (Runtime, etc.)** — https://raw.githubusercontent.com/ChromeDevTools/devtools-protocol/master/json/js_protocol.json

## Chrome extensions

- **MV3 migration hub** — https://developer.chrome.com/docs/extensions/develop/migrate
- **Extension service workers** — https://developer.chrome.com/docs/extensions/develop/concepts/service-workers
- **chrome.storage** — https://developer.chrome.com/docs/extensions/reference/api/storage
- **Manifest file format** — https://developer.chrome.com/docs/extensions/reference/manifest

## Web platform security / performance

- **Secure contexts** — https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts
- **Mixed content** — https://developer.mozilla.org/en-US/docs/Web/Security/Mixed_content
- **CORS guide** — https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CORS
- **performance.memory (non-standard)** — https://developer.mozilla.org/en-US/docs/Web/API/Performance/memory

## Fragile claims

- Do not assert `Page.captureScreenshot` supports `scale`; tip-of-tree params use `fromSurface` / clip / format — DPI via Emulation `deviceScaleFactor`.
- Do not teach `Network.setRequestInterception` as the current intercept API; use Fetch.
- Do not quote fixed CDP compatibility guarantees; the viewer states CDP is not a supported public third-party API and may change with Chromium.
- `performance.memory` availability is implementation-specific; always feature-detect.
