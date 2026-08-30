# Operation patterns

## Launch News.app

1. Confirm the request is to launch News.app.
2. Run `open /System/Applications/News.app`.
3. Report the command result. If it fails, load `troubleshooting.md`.

## Open one Apple News link

1. Confirm that the target begins with `https://apple.news/`.
2. Preview the exact URL.
3. Run `open "<link>"`.
4. Report that macOS received the request and ask the user to confirm the intended article opened if the runtime cannot observe the app.

## Topic search

1. Confirm the topic and source scope.
2. Use a confirmed, user-owned Shortcut when one exists.
3. Otherwise, request one Apple News link or a source constraint.
4. Present any candidate links before opening one.

## Multiple links

1. List every candidate with an index and source.
2. Ask the user to select one or explicitly approve the full set.
3. Restate the count and targets, then obtain a second explicit confirmation.
4. Open only the confirmed links and report each attempted command.

## Failure recovery

If a command fails, identify the failed prerequisite or URL, load `troubleshooting.md`, and offer its next actionable step. End the operation after the safe paths are exhausted.
