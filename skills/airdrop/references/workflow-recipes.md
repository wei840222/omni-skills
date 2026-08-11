# Workflow Recipes - AirDrop

Use these patterns when the user wants nearby local delivery from the agent.

Before running a recipe, resolve `<state_root>` with `SKILL.md`, then replace both variables with actual absolute paths.

```bash
skill_root="/absolute/path/to/skills/airdrop"
state_root="/absolute/path/to/resolved/airdrop-state"
```

## Direct Mode: Share One File

```bash
"$skill_root/scripts/airdrop-send.sh" ./dist/release-notes.pdf
```

Best for:
- one PDF
- one ZIP
- one screenshot
- one installer file

## Direct Mode: Share Multiple Files

```bash
"$skill_root/scripts/airdrop-send.sh" ./build/app.dmg ./build/checksums.txt
```

Use this when the recipient needs a small fixed bundle and no extra packaging.

## Curate Then Share

When the source is noisy, reduce it first:

```bash
mkdir -p "$state_root/staging/review-bundle"
cp ./output/final-review.pdf "$state_root/staging/review-bundle/"
cp ./output/diff-summary.txt "$state_root/staging/review-bundle/"
zip -r "$state_root/staging/review-bundle.zip" "$state_root/staging/review-bundle"
"$skill_root/scripts/airdrop-send.sh" "$state_root/staging/review-bundle.zip"
```

Use this for:
- review packages
- debug bundles
- selected screenshots
- only-approved exports

## Text Needs a File First

If the user says "AirDrop this summary", stage it first:

```bash
mkdir -p "$state_root/staging"
printf '%s\n' "summary text here" > "$state_root/staging/session-summary.txt"
"$skill_root/scripts/airdrop-send.sh" "$state_root/staging/session-summary.txt"
```

Do not claim chat text can be AirDropped directly without a shareable item.

## Shortcut Fallback Mode

If the user already has a Shortcut that accepts file input:

```bash
"$skill_root/scripts/airdrop-send.sh" --shortcut "Send via AirDrop" ./exports/demo.mp4
```

Use this when:
- they prefer Shortcuts automation
- `swift` is unavailable
- the Shortcut performs pre-share transforms first

## Report State Correctly

Good:
- "AirDrop chooser launched for 2 files."
- "The handoff is ready; pick the nearby device in macOS."

Bad:
- "The file was delivered."
- "The device received it." 

Delivery is only confirmed after the user sees the device-side result.
