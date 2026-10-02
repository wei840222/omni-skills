---
name: macos
description: >
  Apply macOS-specific system administration, BSD/GNU CLI traps, Homebrew path
  differences, Keychain secrets, launchd agents, TCC privacy permissions, and
  automation with defaults/osascript. Use on Darwin hosts for sed -i, Keychain,
  LaunchAgents, SIP, screenshots, or networksetup. Prefer `linux` for non-Darwin
  hosts, `bash` for shell syntax depth, and `network` for non-radio L3/DNS work.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🍎","os":["darwin"]}'
  related-skills: '{"backups":"Cross-system backup retention and restore policy beyond local macOS copy tools.","bash":"Shell scripting syntax and safety beyond macOS BSD utility traps.","linux":"Non-Darwin host triage, systemd, and Linux package/firewall workflows.","network":"Layer-3 reachability, DNS, routing, and TLS diagnosis beyond macOS interface helpers.","windows":"Windows host traps and Credential Manager when the target is not Darwin."}'
---

# macOS

Domain guidance for **Apple Darwin hosts**: BSD vs GNU CLI differences, Homebrew
layout, Keychain, launchd, TCC privacy gates, defaults, and local automation.
This skill is **stateless** — it does not store credentials or host inventories
in the package.

## When to load

- Scripts fail on macOS because of BSD `sed`/`find`/`date`/`xargs`/`readlink`
- Storing or reading secrets via Keychain (`security`) instead of plaintext files
- Creating or debugging user LaunchAgents / system LaunchDaemons
- Automation blocked by TCC (Full Disk Access, Automation, Screen Recording)
- Homebrew path / arch (`arm64` vs `x86_64`) confusion
- Local ops: `defaults`, `pbcopy`/`pbpaste`, `screencapture`, `caffeinate`, `open`

Prefer other skills when the ask is mainly:

- Non-macOS Linux hosts / systemd → `linux`
- Shell language craft (arrays, set -euo, quoting depth) → `bash`
- DNS/routing/TLS outside macOS helpers → `network`
- Windows Credential Manager / WinRM → `windows`
- Backup retention policy across systems → `backups`

## Routing

Keep `SKILL.md` as the router; load supporting references only when needed:

- **BSD/GNU traps, Homebrew, Keychain, launchd, TCC, defaults, files, clipboard, screenshots, power, network helpers, SIP, logs, open/osascript** → `references/macos-commands.md`
- **Gate 6 primary sources** → `references/sources.md`

## Core rules

1. **Assume BSD userland** — `sed -i` needs an extension arg (`sed -i '' ...`); `find -printf`, `grep -P`, and `readlink -f` are missing or different; prefer `realpath` or explicit `stat -f`.
2. **Never hardcode secrets** — use Keychain (`security add/find-generic-password`) or env/keychain pointers; examples use placeholders only.
3. **TCC fails silent** — Full Disk Access, Automation, and Screen Recording are per-app; grant Terminal and iTerm separately; do not treat empty output as success.
4. **launchd edits need unload** — unload before editing a loaded plist; prefer `~/Library/LaunchAgents/` for user agents.
5. **Respect SIP** — `/System`, `/usr` (except `/usr/local`), `/sbin`, `/bin` stay protected; design around SIP instead of disabling it.
6. **Name the arch** — Apple Silicon Homebrew is `/opt/homebrew`; Intel is `/usr/local`; check `uname -m` before blaming PATH.

## Safety

- Never commit real Keychain passwords, `.p12`/API tokens, or TCC database dumps into the skill tree or git.
- Use placeholders such as `<SERVICE_NAME>`, `<SECRET_VALUE>`, `<PLIST_LABEL>`.
- Do not recommend disabling SIP except as a temporary Recovery-mode debug step with explicit restore.
