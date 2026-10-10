# CDP connect and target discovery

When Chromium/Chrome starts with `--remote-debugging-port=<port>` (example `9222`), it exposes a local HTTP server for discovery and WebSocket CDP sessions.

## HTTP endpoints

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/json/version` | GET | Browser version metadata and browser-level WebSocket URL |
| `/json` or `/json/list` | GET | Inspectable targets (pages, workers, tabs) with per-target `webSocketDebuggerUrl` |
| `/json/new?{url}` | PUT | Create a new page/tab target (PUT required) |
| `/json/activate/{targetId}` | GET | Foreground a target |
| `/json/close/{targetId}` | GET | Close a target |
| `/json/protocol` | GET | Full protocol schema JSON |
| `/devtools/browser/{guid}` | WS | Browser-level connection |
| `/devtools/page/{targetId}` | WS | Page/target connection |

Source: Chrome DevTools Protocol viewer endpoint documentation
https://chromedevtools.github.io/devtools-protocol/

## Practice

1. `curl -s http://127.0.0.1:9222/json/list`
2. Select the target whose URL/title matches the work.
3. Open that object's `webSocketDebuggerUrl`.
4. If port was `0`, read the chosen port from stderr or the profile `DevToolsActivePort` file.
5. Multiple simultaneous clients are supported on modern Chrome; a disconnect may emit `Inspector.detached`.

## Trust boundary

CDP is high-privilege and intended for trusted local tooling. It is not a stable public web API. Product automation should prefer Puppeteer, Playwright, ChromeDriver, or other supported wrappers when they fit.
