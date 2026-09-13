# Electron Architecture & Debugging

## Architecture Traps
- `webPreferences` locked after window creation — can't enable nodeIntegration later
- Blocking main process freezes ALL windows — async everything, use `UtilityProcess` for CPU-intensive tasks instead of hidden background windows
- Each BrowserWindow is separate renderer process — can't share JS variables directly
- `show: false` then `ready-to-show` — prevents white flash, looks more native

## Native Module Pain
- Pre-built native modules won't work — must rebuild for Electron's specific Node version
- `electron-rebuild` after every Electron upgrade — version mismatch = runtime crash
- N-API modules more stable — survive Electron upgrades better than nan-based

## Packaging Pitfalls
- Dev dependencies included by default — production builds bloat without explicit exclusion
- Code signing required for macOS auto-update — unsigned apps can't use Squirrel
- Windows notifications require `app.setAppUserModelId()` — silent failure without it
- ASAR is an archive format, not encryption — securely store secrets in environment variables or external credential stores instead of the ASAR bundle

## Platform-Specific Issues
- CORS blocks `file://` protocol — use custom protocol (`app://`) or local server
- Windows needs NSIS or Squirrel for auto-update — installer format matters
- macOS universal binary needs `--universal` flag — ships both Intel and ARM

## Memory and Performance
- Unclosed windows leak memory — call `win.destroy()` explicitly when done
- Lazy load heavy modules — startup time directly affects perceived quality
- `backgroundThrottling: false` if timers matter when minimized

## Debugging
- Main process: `--inspect` flag, connect via `chrome://inspect`
- Renderer: `webContents.openDevTools()` or keyboard shortcut
- `electron-log` for persistent logs — console.log vanishes on restart
