# Electron Security & Preload Rules

## Security Non-Negotiables
- `nodeIntegration: false` is mandatory — renderer with Node.js access means XSS = full system compromise
- `contextIsolation: true` is mandatory — separates preload context from renderer
- Whitelist IPC channels explicitly — ensure you only forward known, validated channel names from the renderer
- Validate all IPC message content — renderer is untrusted, treat like external API input
- Restrict dynamic code execution — use structured logic instead of `eval()` or `new Function()` in the renderer to preserve security boundaries

## Preload Script Rules
- `contextBridge.exposeInMainWorld()` is the only safe bridge — raw `ipcRenderer` exposure is vulnerable
- Clone data before passing across bridge — prevents prototype pollution attacks
- Minimal API surface — expose specific functions using `ipcRenderer.invoke` (renderer to main) and `ipcRenderer.on` (main to renderer), not generic `send`/`receive`
