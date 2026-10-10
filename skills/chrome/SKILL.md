---
name: chrome
description: >
  Debug and automate Chromium via Chrome DevTools Protocol (CDP), Manifest V3
  extensions, and Chrome-only diagnostics: target discovery, domain enablement,
  screenshots, network body fetch, Fetch interception, service-worker state,
  and secure-context checks. Use for raw CDP clients, extension MV3 pitfalls,
  remote-debugging endpoints, or Chrome-vs-Edge detection. Prefer `playwright`
  or `puppeteer` for product browser automation; `cypress` for that suite;
  `web`/`javascript` for page code without DevTools.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🌐"}'
  related-skills: '{"playwright":"Primary browser test/automation runner with locators, traces, and CI sharding.","puppeteer":"Chrome/Chromium automation library when staying on the Puppeteer API.","cypress":"Maintain an existing Cypress suite rather than raw CDP.","web":"General web delivery, DOM, and frontend traps outside DevTools.","javascript":"Language-only JS patterns without Chrome protocol or extension APIs."}'
---

# Chrome

Own **Chrome/Chromium protocol and extension diagnostics**: connect to the right target, enable domains before commands, capture reliable screenshots, inspect network bodies, intercept with Fetch (not legacy Network interception), and keep MV3 extension state durable. This skill does not replace Playwright/Puppeteer product runners.

## State location

Chrome diagnostic notes may exist in `<workspace>/chrome/`, `<workspace>/memory/chrome/`, or `~/chrome/`.
Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one; resolve it to an absolute directory.
2. Otherwise use the first existing directory in this order:
   `<workspace>/chrome/`, `<workspace>/memory/chrome/`, `~/chrome/`.
3. If multiple candidates exist, keep only the highest-precedence directory, report the conflict, and leave siblings unchanged.
4. If none exists and notes must be created, default to `<workspace>/chrome/` only after brief consent.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd. An existing `~/chrome/` may be read; otherwise ask before creating data.
6. Keep the selected `<state_root>` fixed for the whole invocation.

Use the selected `<state_root>` for every state path in this skill. Outside this section, every skill-state path uses `<state_root>/...`. Skill resources stay under `references/`. Never treat the literal string `<state_root>` as a filesystem path. Never write cookies, CDP auth tokens, extension secrets, or full user profiles into state files. Never write learned preferences into `SKILL.md`.

Default note file: `<state_root>/memory.md` (create on first authorized write). Load `references/state.md` for the template.

## Workflow

1. Classify the ask: CDP connect/target, screenshot/network debug, request intercept/block, MV3 extension, context detection, or security (mixed content/CORS/secure context).
2. Resolve `<state_root>` only when notes or prior endpoints matter; otherwise stay stateless.
3. Apply the minimum viable CDP/MV3 defaults below, then load only the matching reference.
4. Prefer supported runners (`playwright`, `puppeteer`) when the user needs product automation rather than raw protocol work.
5. Re-check tip-of-tree CDP and Chrome docs for version-sensitive commands before asserting parameter names.

| Need | Load |
| --- | --- |
| Defaults, checklist, common traps | `references/domain.md` |
| HTTP discovery endpoints, WebSocket targets, multi-client notes | `references/cdp-connect.md` |
| Domain enable, evaluate, screenshot, network body | `references/cdp-commands.md` |
| Fetch pause/fail/fulfill vs blocked URLs | `references/network-intercept.md` |
| MV3 permissions, service workers, storage | `references/extensions-mv3.md` |
| Chrome-vs-other, extension context types | `references/context-detect.md` |
| Mixed content, CORS, secure context | `references/security.md` |
| Preference template under `<state_root>` | `references/state.md` |
| Verified specs and fragile claims | `references/sources.md` |

## Minimum viable CDP session

1. Launch or attach with remote debugging (example port `9222`).
2. `GET /json/list` (or `/json`) and pick the target's `webSocketDebuggerUrl` — do not guess `ws://localhost:9222/devtools/browser` when a page target is required.
3. Open the WebSocket; send commands with monotonically increasing `id`; wait for matching responses (CDP is async).
4. Call `Runtime.enable` and `Page.enable` (and `Network.enable` when observing traffic) **before** `Runtime.evaluate`, `Page.navigate`, or body fetches.
5. For screenshots: `Page.captureScreenshot` with `fromSurface: true` when capturing the surface; for high-DPI layout use `Emulation.setDeviceMetricsOverride` `deviceScaleFactor` (there is **no** `scale` on `Page.captureScreenshot` in current tip-of-tree).
6. For response bodies: handle `Network.responseReceived` / `loadingFinished`, then `Network.getResponseBody` with `requestId`.
7. For interception: enable **`Fetch`** (`Fetch.enable` → `requestPaused` → `continueRequest` / `failRequest` / `fulfillRequest`). Do not teach removed `Network.setRequestInterception` as current API.

## Failure branches

| Condition | Action |
| --- | --- |
| Commands hang or return empty | Confirm domain `*.enable` ran; match response `id`; ensure target WebSocket still open |
| Connected but wrong document | Re-list `/json/list`; attach to page target `webSocketDebuggerUrl`, not an unrelated worker/browser root |
| Fuzzy / low-res screenshot on Retina | Set `fromSurface: true`; set `deviceScaleFactor` via Emulation; do not invent a `scale` param on captureScreenshot |
| `getResponseBody` fails | Wait until `loadingFinished`; use the same `requestId`; enable Network with adequate buffers before heavy body retention |
| Intercept API missing | Migrate to Fetch domain; fail with `errorReason` such as `BlockedByClient` |
| MV3 background "forgets" state | Persist with `chrome.storage`; use `chrome.alarms` instead of long `setInterval`; avoid relying on global vars across worker restarts |
| Content script cannot see page globals | `chrome.scripting.executeScript` into page world, or `postMessage` bridge |
| Page APIs throw without gesture / http | Check `window.isSecureContext`; fix mixed content; diagnose CORS from Network panel, not only `TypeError` text |

## Safety defaults

- Treat CDP as a **trusted, high-privilege** local debug channel — not a public browser API. Prefer Puppeteer/Playwright/ChromeDriver for third-party product automation when possible.
- Never exfiltrate profile data, cookies, or extension secrets from a debugging session.
- Do not invent CDP parameter matrices from memory; re-open `references/sources.md` and tip-of-tree protocol docs when claims are version-sensitive.
- Keep writes inside `<state_root>/` with consent; never commit runtime memory into the package.
- Load at most one deep reference per step; keep always-on defaults in this file only.
