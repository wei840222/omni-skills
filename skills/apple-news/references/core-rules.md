# Core rules

1. Launch News.app with `open /System/Applications/News.app` after verifying that the command and app path are available.
2. For article reads, accept `https://apple.news/...` URLs, preview the exact target, and invoke `open "<link>"`.
3. For topic discovery without an Apple News link, use a confirmed user-owned Shortcut. Otherwise request one source constraint or reference link.
4. Preview every URL or Shortcut name before execution. Ask for explicit confirmation when the request includes sensitive context.
5. For multiple links, list the targets and obtain two explicit confirmations before commands run.
6. Report command results and load `troubleshooting.md` when the result differs from the requested outcome.
7. Send only the URL or Shortcut inputs necessary for the requested operation. Persist reusable local preferences only after the user approves the write.
