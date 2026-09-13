---
name: electron
description: Build Electron desktop applications following secure architecture principles. Use this when the user needs help with Electron context isolation, IPC communication, packaging, or native module builds.
metadata:
  version: '1.0.0'
  openclaw: "{\"emoji\": \"\u26A1\", \"requires\": {\"bins\": [\"npm\"]}}"
---

## Core References

When working on Electron applications, load these references as needed:
- `references/security.md` - Read when setting up `webPreferences`, preload scripts, or IPC communication to ensure secure boundaries.
- `references/architecture.md` - Read when debugging performance, building native modules, or configuring packaging tools (like electron-builder or Squirrel).

## State location

This skill is stateless and does not store local configuration or persistent memory.
