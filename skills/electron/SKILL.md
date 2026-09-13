---
name: electron
description: Build Electron desktop applications with secure architecture. Use when setting up contextIsolation/preload bridges, hardening IPC, packaging installers, rebuilding native modules, or debugging main/renderer freezes.
metadata:
  version: "1.1.0"
  openclaw: "{\"emoji\":\"⚡\",\"requires\":{\"bins\":[\"npm\"]}}"
---

## When to Use

- Hardening Electron `webPreferences`, preload scripts, or IPC boundaries
- Packaging macOS/Windows installers, code signing, or ASAR distribution questions
- Rebuilding native modules after an Electron upgrade
- Debugging main-process freezes, white-flash startup, or renderer DevTools issues
- Not for general Node.js language craft (`javascript` / `nodejs`) or non-Electron desktop frameworks

This skill is stateless and does not store local configuration or persistent user state.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Security non-negotiables, preload, IPC whitelist | `references/security.md` | First setup or any renderer↔main bridge work |
| Architecture traps, UtilityProcess, native modules, packaging, debug | `references/architecture.md` | Performance, packaging, platform, or freeze issues |
| Official sources | `references/sources.md` | Verify current Electron guidance |

## Core Rules

1. Keep `nodeIntegration: false` and `contextIsolation: true` — renderer is untrusted.
2. Expose only a minimal preload API through `contextBridge.exposeInMainWorld`; prefer `invoke`/`handle` over generic send/receive.
3. Whitelist and validate IPC channels/payloads; never forward arbitrary renderer channel names.
4. Do not block the main process; offload CPU-heavy work to `UtilityProcess` instead of hidden `BrowserWindow`s.
5. Rebuild native modules for Electron's Node ABI after upgrades; prefer N-API modules when choosing native deps.
6. Treat ASAR as an archive, not encryption — keep secrets in env vars or an external credential store.

## Operations

For security and preload details, load [Security & Preload Rules](references/security.md).

For architecture, native modules, packaging, platform caveats, performance, and debugging, load [Architecture & Debugging](references/architecture.md).
