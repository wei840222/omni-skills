# Troubleshooting

## News.app probe fails

**Symptom:** `/System/Applications/News.app` is absent or `open` is unavailable.

1. Report which probe failed.
2. Ask the user to confirm that News.app is installed and that the session is running on macOS.
3. Resume with `open /System/Applications/News.app` after the prerequisite is available.

## Apple News link is invalid or opens unexpectedly

**Symptom:** The target is not an `https://apple.news/...` URL, or macOS opens an unexpected handler or article.

1. Show the exact URL that was received.
2. Request a replacement Apple News URL when the target is malformed or mismatched.
3. For a valid URL with an unexpected handler, explain that macOS URL associations control the destination and ask the user to choose whether to update that association or continue with the current handler.

## Shortcut is unavailable

**Symptom:** `shortcuts` is absent, `shortcuts list` cannot find the named Shortcut, or the run command fails.

1. Run `shortcuts list` when the command is available.
2. Confirm the exact Shortcut name and its expected effects.
3. Continue with a direct Apple News link or source constraint when the Shortcut cannot run.

## Persistent-state path is unclear

**Symptom:** More than one state candidate exists, or no workspace path is available.

1. Use the highest-precedence existing candidate from the State location resolver.
2. Tell the user when lower-precedence copies exist; keep them unchanged.
3. When no state root can be resolved and a write is requested, ask the user or host for an explicit state path.
