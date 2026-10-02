# macOS command reference

Load this file when executing commands on Darwin or diagnosing Homebrew,
Keychain, launchd, TCC, defaults, files, clipboard, screenshots, power,
networksetup, SIP, unified logging, or `open`/`osascript`.

## BSD vs GNU commands

- `sed -i` requires an extension argument: `sed -i '' 's/a/b/' file` — empty string skips backup; GNU sed treats the extension as optional.
- `find` lacks `-printf` — use `-exec stat -f ... {} +` or `xargs` with `stat -f`.
- `date` format flags differ: `date -j -f '%Y-%m-%d' '2024-01-15' '+%s'` — `-j` prevents setting the clock.
- `grep -P` (Perl regex) is absent — use `grep -E` or install GNU grep (`ggrep`) via Homebrew.
- `xargs` defaults to `/usr/bin/echo` — always pass the target command explicitly.
- `readlink -f` is missing — use `realpath` or `python3 -c "import os; print(os.path.realpath('path'))"`.

## Homebrew paths

- Apple Silicon: `/opt/homebrew/bin`, `/opt/homebrew/lib`
- Intel: `/usr/local/bin`, `/usr/local/lib`
- Architecture: `uname -m` → `arm64` or `x86_64`
- Shell init often needs `eval "$(/opt/homebrew/bin/brew shellenv)"` in `~/.zprofile`
- Rosetta / x86 under arm64: `arch -x86_64 /bin/bash` then install or run Intel-only tools

## Keychain (secrets)

- Store: `security add-generic-password -a "$USER" -s "<SERVICE_NAME>" -w "<SECRET_VALUE>" -U`
- Retrieve: `security find-generic-password -a "$USER" -s "<SERVICE_NAME>" -w`
- `-U` updates an existing item; without it, duplicates error
- First access may prompt; authorize permanently only for trusted automation identities
- Delete: `security delete-generic-password -a "$USER" -s "<SERVICE_NAME>"`
- Prefer Keychain over plaintext env files committed to disk

## launchd (services)

- User agents: `~/Library/LaunchAgents/` — run as the logged-in user
- System daemons: `/Library/LaunchDaemons/` — boot-time, typically root
- Modern control: `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/<PLIST_LABEL>.plist` and `launchctl bootout ...` (older `load`/`unload -w` still appear in many guides)
- Unload/bootout before editing a loaded plist — live edits are ignored
- Status: `launchctl print gui/$(id -u)/<PLIST_LABEL>` or `launchctl list | grep <name>`
- Logs: `log show --predicate 'subsystem == "<subsystem>"' --last 1h`

## Privacy permissions (TCC)

- Automation often fails silently without Full Disk Access, Automation (AppleEvents), or Screen Recording
- Grant under System Settings → Privacy & Security for each app binary (Terminal ≠ iTerm ≠ script runner)
- Reset category: `tccutil reset AppleEvents` (and other services as needed)
- Inspecting `TCC.db` may itself require Full Disk Access; treat DB contents as sensitive
- Do not ship TCC dumps or raw permission tables in git

## defaults (preferences)

- Read: `defaults read <bundle-id> <key>`
- Write: `defaults write <bundle-id> <key> -bool true`
- Delete: `defaults delete <bundle-id> <key>`
- Restart the target app after changes when UI state is cached (`killall Finder`)
- Bundle ID: `osascript -e 'id of app "App Name"'`
- Export domain XML: `defaults export <bundle-id> -`

## File operations

- `ditto` preserves resource forks and metadata — prefer over `cp -R` for app bundles
- Create DMG: `hdiutil create -volname "Name" -srcfolder ./folder -ov -format UDZO output.dmg`
- Attach: `hdiutil attach image.dmg` — note the mount point
- Detach: `hdiutil detach /Volumes/Name`
- Extended attributes: `xattr -l file`, clear all `xattr -c file`
- Quarantine removal (only when the binary is trusted): `xattr -d com.apple.quarantine app.app`

## Clipboard

- Copy text: `printf '%s' 'text' | pbcopy`
- Paste: `pbpaste`
- File to clipboard: `pbcopy < file.txt`
- Prefer plain text unless RTF is required (`pbpaste -Prefer rtf`)

## Screenshots and screen

- Interactive region: `screencapture -i output.png`
- Window: `screencapture -w output.png`
- Clipboard: `screencapture -c`
- Quiet: `screencapture -x output.png`
- Screen Recording permission is required for many capture paths

## Process and power

- Keep awake while a command runs: `caffeinate -i <command>`
- Timed assertion: `caffeinate -t 3600`
- Why not sleeping: `pmset -g assertions`
- View power settings: `pmset -g`
- Frontmost app name: `osascript -e 'tell application "System Events" to get name of first process whose frontmost is true'`

## Network helpers

- Hardware ports: `networksetup -listallhardwareports`
- IPv4 on interface: `ipconfig getifaddr en0` (Wi-Fi is often `en0` on laptops, not guaranteed)
- DNS config: `scutil --dns | grep nameserver`
- Flush local DNS cache: `sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder`
- HTTP proxy: `networksetup -getwebproxy "Wi-Fi"`

## System Integrity Protection

- Status: `csrutil status`
- Disable only from Recovery and only for temporary debugging; re-enable afterward
- Protected paths include `/System`, `/usr` (except `/usr/local`), `/sbin`, `/bin`
- Root cannot freely mutate SIP-protected paths — design automations around this boundary

## Unified logging

- Live stream: `log stream --predicate 'process == "processname"'`
- Recent search: `log show --last 1h --predicate 'eventMessage contains "error"'`
- Subsystem filter: `log show --predicate 'subsystem == "com.apple.example"' --last 1h`
- Collect archive: `log collect --output ./logs.logarchive`

## open / AppleScript / Spotlight

- URL: `open 'https://example.com'`
- App by name: `open -a 'Safari'`
- File with app: `open -a 'TextEdit' file.txt`
- AppleScript one-liner: `osascript -e 'tell application "Finder" to get name of home'`
- Spotlight name query: `mdfind "kMDItemDisplayName == 'filename.txt'"` — often faster than recursive `find` on indexed volumes
