# Network block and Fetch interception

## Block list

Use `Network.setBlockedURLs` when you only need to prevent loads matching patterns. Set patterns before `Page.navigate`.

## Full interception (current)

Legacy `Network.setRequestInterception` is **not** the modern teaching path. Use the **Fetch** domain:

1. `Fetch.enable` (optional `patterns`, `handleAuthRequests`)
2. Handle `Fetch.requestPaused`
3. Respond with exactly one of:
   - `Fetch.continueRequest`
   - `Fetch.failRequest` (`errorReason`, e.g. `BlockedByClient`)
   - `Fetch.fulfillRequest` (synthetic status/headers/body)
4. Optional: `Fetch.getResponseBody` when paused at the response stage
5. `Fetch.continueWithAuth` when `authRequired` and auth handling was enabled

If a guide still says `Network.setRequestInterception`, rewrite it to Fetch before shipping automation advice.

Protocol references:

- https://chromedevtools.github.io/devtools-protocol/tot/Fetch/
- https://chromedevtools.github.io/devtools-protocol/tot/Network/#method-setBlockedURLs
