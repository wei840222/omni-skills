# Launch and Profiles

## OS Launch Paths

Use the platform's normal launch path first:

| OS | Typical launch path |
|----|---------------------|
| macOS | `open -a "Brave Browser"` |
| Windows | Start menu entry or Brave executable under `Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe` |
| Linux | `brave-browser` or the desktop launcher |

If the app path is unclear, confirm the installed channel before adding flags.

## Profile Strategy

Keep purpose separate:
- daily profile for normal browsing and logins
- test profile for site debugging and extension isolation
- automation profile for Playwright, Puppeteer, or DevTools work

Test risky flags or questionable extensions in a dedicated test profile before affecting the daily profile.

## Safe Launch Questions

Lock these before running commands:
- which profile should open
- whether private-window behavior matters
- whether the user wants persistent changes or a disposable session
- whether remote debugging is part of the task

## Temporary Profile Pattern

When debugging without touching the daily setup, prefer a clean disposable profile.

Good uses:
- checking whether a site failure is profile-specific
- testing if an extension causes the issue
- isolating automation from personal cookies

Use a persistent profile when the task requires an existing login or saved browser state.

## Launch Flags Discipline

Use the fewest flags needed for the task.

Common safe categories:
- profile selection flags
- remote-debugging flags only when automation is explicitly approved
- temporary user-data-dir for isolation

Apply one flag at a time during diagnosis to prevent overlapping effects from creating fake "Brave problems."
