# Chrome extensions (Manifest V3)

Official orientation:

- MV3 intro / migration hub: https://developer.chrome.com/docs/extensions/develop/migrate
- Service workers: https://developer.chrome.com/docs/extensions/develop/concepts/service-workers
- `storage` API: https://developer.chrome.com/docs/extensions/reference/api/storage
- Manifest format: https://developer.chrome.com/docs/extensions/reference/manifest

## Permissions

- `permissions` — extension APIs
- `host_permissions` — hosts/URLs
- Prefer tight host patterns over broad `http://*/*` unless the product truly needs it

## Service worker lifetime

MV3 background is a **service worker** that may restart between events—persist anything you need next time.

- Persist with `chrome.storage.local` / `session` / `sync` as appropriate (APIs are async — always await).
- Schedule with `chrome.alarms` instead of long-lived `setInterval`.
- Handle storage quota errors (`QUOTA_EXCEEDED` class failures) explicitly.

## Content scripts vs page world

Content scripts are isolated from page JavaScript. To touch page globals:

- `chrome.scripting.executeScript` with a function in the page world, or
- explicit `window.postMessage` / custom-event bridges

## Action API

Prefer `chrome.action` (MV3) over deprecated `chrome.browserAction` (MV2). Guard `chrome.runtime.getManifest()` in try/catch when probing contexts.
