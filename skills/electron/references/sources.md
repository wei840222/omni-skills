# Sources — electron skill

Gate 6 research anchors. Prefer primary Electron docs; re-verify before citing version-specific defaults.

## Security model and preload

- [Security Tutorial](https://www.electronjs.org/docs/latest/tutorial/security) — `nodeIntegration`, `contextIsolation`, and renderer trust boundaries
- [contextBridge](https://www.electronjs.org/docs/latest/api/context-bridge) — only safe exposure path into the renderer
- [ipcMain](https://www.electronjs.org/docs/latest/api/ipc-main) — main-process handlers (`handle` / `on`)
- [ipcRenderer](https://www.electronjs.org/docs/latest/api/ipc-renderer) — preload-side `invoke` / `on` patterns

## Process model and windows

- [UtilityProcess](https://www.electronjs.org/docs/latest/api/utility-process) — preferred path for CPU-heavy work instead of hidden `BrowserWindow`
- [BrowserWindow](https://www.electronjs.org/docs/latest/api/browser-window) — `webPreferences` lock-after-create, `ready-to-show`, throttling

## Native modules and packaging

- [Using Native Node Modules](https://www.electronjs.org/docs/latest/tutorial/using-native-node-modules) — rebuild for Electron's Node ABI; N-API stability
- [ASAR Archives](https://www.electronjs.org/docs/latest/tutorial/asar-archives) — archive format, not encryption; keep secrets out of the bundle
- [Application Distribution](https://www.electronjs.org/docs/latest/tutorial/application-distribution) — packaging and platform installer expectations
