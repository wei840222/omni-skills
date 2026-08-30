# Command paths

Use `open` as the supported command path. It launches News.app by absolute path and hands Apple News URLs to the macOS-registered handler.

## Probe before the first command

```bash
command -v open
test -d /System/Applications/News.app && echo "News.app present"
```

If either probe fails, explain the failed prerequisite and follow `troubleshooting.md`.

## Launch News.app

```bash
open /System/Applications/News.app
```

## Open an Apple News link

After confirming the exact `https://apple.news/...` URL, run:

```bash
open "https://apple.news/AhCs4Rmk1REaKltNwpS4APQ"
```

This asks macOS to use the registered handler for the URL. Confirm the result rather than asserting that News.app received the article; a user can change URL associations.

## Shortcut path

Use this path only for a user-owned Shortcut whose name and side effects the user has confirmed:

```bash
shortcuts list
shortcuts run "<user-shortcut-name>"
```

`shortcuts` is optional. When it is unavailable or the named Shortcut is absent, ask for one Apple News link or source constraint instead.
