# Memory setup — Taxi

Create directories only after `<state_root>` is resolved with the State location
rules in `SKILL.md`, and only when durable preferences or trip logs must persist.

## Templates

Copy the needed sections from `assets/taxi-data-templates.md` into:

- `<state_root>/memory.md` — preferences, saved addresses, special needs
- `<state_root>/trips.md` — trip history and monthly summaries
- `<state_root>/accounts.md` — app accounts, ratings, credits (no secrets)
- `<state_root>/promos.md` — active codes with expiry and stacking notes

## Safety for stored data

- Payment fields may store a card nickname or last four digits only
- Keep full card numbers, CVVs, PINs, one-time codes, and account passwords out of every state file
- Mask home addresses in exported or shared logs when the user asks
- Treat referral codes and promo terms as ephemeral; re-check before applying
