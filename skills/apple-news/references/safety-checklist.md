# Safety checklist

Apply this checklist before opening links or running a Shortcut.

## Before execution

1. Confirm the exact action: launch News.app, open one link, open a set of links, or run a Shortcut.
2. Verify that every link uses `https://apple.news/...`.
3. Preview each target URL and identify whether it contains sensitive context.
4. For a Shortcut, confirm its exact name and expected side effects.
5. For multiple links, show the count and obtain two explicit confirmations.

## After execution

1. Report the command that ran and its result.
2. Confirm that the requested app, URL, or Shortcut outcome matches the user's intent.
3. When the observed result differs, load `troubleshooting.md` and present the corrected next step.

## Default boundary

Open one link at a time unless the user explicitly confirms a larger set. Record confirmed multi-link and Shortcut preferences in `<state_root>` only after the user approves the persistent write.
