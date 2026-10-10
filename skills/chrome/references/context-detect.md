# Context detection helpers

These are practical heuristics, not normative Chrome guarantees. Re-test on the target browser build when behavior matters.

## Chrome vs other Chromium browsers

`window.chrome` alone is insufficient (Edge/Brave/Opera may expose chrome-like objects). Combine vendor and UA checks carefully; prefer feature detection for the API you need rather than brand sniffing when possible.

## Extension contexts

| Signal | Likely context |
| --- | --- |
| `chrome.runtime.id` present | Extension content script / extension page |
| `chrome.runtime.getManifest` usable | Extension extension-page / service worker / popup |
| Page without extension runtime | Ordinary web page |

## Performance memory

`performance.memory` is **non-standard** and not universally available. Always guard:

```js
if ('memory' in performance) {
  // performance.memory.usedJSHeapSize ...
}
```

MDN: https://developer.mozilla.org/en-US/docs/Web/API/Performance/memory

## Marks and observers

Use `performance.mark` / `measure` for spans; disconnect observers and clear marks when done to avoid leaks. `PerformanceObserver` entry types such as `measure`, `paint`, `largest-contentful-paint` help flag long tasks/frames; treat 16.67ms only as a 60fps rule of thumb, not a Chrome SLA.
