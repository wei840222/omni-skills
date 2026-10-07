# Keys broker setup

Install and verify the local broker before the first authenticated call.

## Requirements

| Requirement | Detail |
|-------------|--------|
| OS | macOS, or Linux desktop with a keyring (GNOME Keyring / KWallet via libsecret) |
| Shell | bash 4.0+ (associative arrays) |
| Binaries | `curl`, `jq`, and the installed `keys-broker` wrapper |
| Keychain | macOS Keychain Access / `security`; Linux `secret-tool` (package often `libsecret-tools`) |

Unsupported environments return structured errors from the broker: Docker (`.dockerenv` / cgroup), WSL (`microsoft` in `/proc/version`), and Linux without `DBUS_SESSION_BUS_ADDRESS`.

## Install onto PATH

From the skill package root (directory that contains `SKILL.md`):

```bash
install -m 0755 scripts/keys-broker.sh "${HOME}/.local/bin/keys-broker"
# Ensure ~/.local/bin is on PATH for interactive and agent shells
case ":$PATH:" in
  *":$HOME/.local/bin:"*) ;;
  *) echo 'export PATH="$HOME/.local/bin:$PATH"' >> "${HOME}/.bashrc" ;;
esac
hash -r 2>/dev/null || true
```

Re-run `install` after editing `scripts/keys-broker.sh` (for example after extending `ALLOWED_URLS`).

## Verify

```bash
command -v keys-broker
keys-broker ping
# {"ok":true,"status":"running"}

keys-broker services
# {"ok":true,"services":["openai","anthropic","stripe","github"]}
# order may vary; names must match ALLOWED_URLS keys
```

If `ping` works but `call` fails with keyring errors, fix the environment (desktop session / unlock keyring) before storing secrets.

## Trust boundary

```
Agent  --JSON call-->  keys-broker  --allowlist + keychain-->  HTTPS API
  ^                         |
  |                         +-- response JSON only (no raw key)
  +-------- ok/status/body -+
```

- The agent supplies `service`, `url`, `method`, and optional JSON `body`.
- The broker rejects non-HTTPS URLs and URLs outside the per-service regex allowlist.
- The bearer token is read from the OS keychain (`keys:<service>`) and written only to a mode-0600 temp header file for curl (`-H @file`), then deleted.
- The agent must not run `security … -w` / `secret-tool lookup` just to "check" a key into context; existence checks that print secrets belong in the user's local terminal, not in agent logs.

## Dependency install hints

```bash
# Debian/Ubuntu example
sudo apt-get update && sudo apt-get install -y curl jq libsecret-tools

# macOS: curl/jq via Xcode CLT or Homebrew; security(1) is built-in
```

Official references for the underlying tools:

- Apple Keychain Services overview: https://developer.apple.com/documentation/security/keychain_services
- `security` CLI summary: https://ss64.com/mac/security.html
- `secret-tool` man page: https://manpages.debian.org/bookworm/libsecret-tools/secret-tool.1.en.html
- libsecret project: https://wiki.gnome.org/Projects/Libsecret
- curl man page: https://curl.se/docs/manpage.html
