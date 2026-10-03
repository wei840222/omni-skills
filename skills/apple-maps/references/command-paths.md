# Command Paths - Apple Maps (macOS)

Use this order for deterministic command selection.

## Priority Order

1. `open` with Apple Maps URLs (primary and preferred)
2. `shortcuts run` for user-owned shortcut automations
3. `osascript` as last-mile fallback (activate app and assist UI workflows)

## Probe Pattern

Run lightweight checks before first operation:

```bash
command -v open
command -v shortcuts
command -v osascript
```

## URL Launch Pattern

Use `open -a Maps` with explicit HTTPS Maps URLs:

```bash
open -a Maps "https://maps.apple.com/?q=coffee+near+me"
open -a Maps "https://maps.apple.com/?ll=50.894967,4.341626&q=Atomium"
open -a Maps "https://maps.apple.com/?daddr=San+Francisco&dirflg=d&t=h"
open -a Maps "https://maps.apple.com/?saddr=Cupertino&daddr=San+Francisco&dirflg=r"
```

## URL Parameter Rules

Derived from Apple Map Links guidance:

- `q` — query string treated like Maps search input; can also label a pin when used with `ll`
- `near` — bias search near a place or `latitude,longitude`
- `ll` — map center as `latitude,longitude`
- `z` — zoom level
- `saddr` / `daddr` — route origin and destination; `daddr` is required for directions; omit `saddr` to start from the device location ("from here")
- `dirflg` — transport type: `d` driving, `w` walking, `r` transit
- `t` — map type when needed (for example `h` hybrid)

## Selection Rules

- Use the first available path in priority order.
- If `open` is available, prefer URL workflows over UI scripting.
- If using `shortcuts run`, require an existing shortcut name and confirm expected output.
- If only `osascript` is usable, clearly state reduced reliability and request confirmation before proceeding.

## Notes on Scriptability

- Apple Maps has limited direct AppleScript command coverage for deterministic search actions.
- Use URL-based invocation as the stable default and keep UI scripting as a fallback only.
