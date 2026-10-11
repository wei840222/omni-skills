# Official sources (verify before quoting)

Open these live pages when recommending plans, quotas, or vendor-specific
steps. Orientation numbers in `references/services.md` are not a substitute for
the current public page.

## Plans and storage

- Apple iCloud+ overview — https://www.apple.com/icloud/
- Apple iCloud+ plans / storage help — https://support.apple.com/en-us/108038
- Google One plans — https://one.google.com/about/plans
- Google Drive storage settings — https://drive.google.com/settings/storage
- Dropbox plans — https://www.dropbox.com/plans
- Microsoft OneDrive / Microsoft 365 plan comparison — https://www.microsoft.com/en-us/microsoft-365/onedrive/compare-onedrive-plans

## Exports and account tools

- iCloud web — https://www.icloud.com
- Google Takeout — https://takeout.google.com
- Dropbox web — https://www.dropbox.com
- OneDrive web — https://onedrive.live.com

## Research notes (this refactor)

- Apple iCloud marketing page reachable HTTP 200 (2026-10-11); public copy still
  surfaces 5 GB free and paid iCloud+ steps including 50 GB / 200 GB / 2 TB class
  tiers — re-check support article before stating a local-currency price.
- Google One plans page reachable; free tier remains 15 GB shared across Drive,
  Gmail, and Photos in public materials; paid steps include 100 GB and 2 TB
  classes — confirm live SKU before quoting.
- Dropbox `/plans` reachable HTTP 200; free baseline remains very small (2 GB
  class) with device limits on free; Plus pricing is market-specific — always
  open the live plans page in the user region.
- Microsoft plan comparison pages may bot-block some automated fetches (HTTP
  403 observed from datacenter IPs); use an interactive browser or the signed-in
  account storage UI when a precise OneDrive price is required.

When a fetch is blocked, say the price is unverified and point the user at the
official URL rather than inventing a number.
