---
name: ticketmaster
description: >
  Search Ticketmaster events, venues, and attractions with the open Discovery
  API, market-aware filters, onsale windows, and copy-ready curl or shell
  helpers. Use when the user needs live Ticketmaster listings, venue discovery,
  attraction lookup, classification taxonomy, or API-ready search filters.
  Prefer `booking` for reservation confirmation workflows, `events` for general
  event-planning logistics outside Ticketmaster, and `api` for generic REST
  request shaping unrelated to Discovery endpoints.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎟️","requires":{"env":["TM_API_KEY"],"bins":["curl"]},"configPaths":["<state_root>/"]}'
  related-skills: '{"api":"Generic REST request shaping and response inspection outside Ticketmaster Discovery.","booking":"Reservation confirmation and hold hygiene after discovery turns into an action.","events":"Event-planning schedules and logistics when Ticketmaster is not the data source."}'
---

# Ticketmaster

Use the open Ticketmaster Discovery API for search and lookup work. Reach for
the bundled `assets/ticketmaster.sh` helper when terminal speed matters, and
fall back to raw `curl` when exact response shapes matter. Persist reusable
locale, market, city, and query defaults under `<state_root>/` (see
`references/setup.md` on first use and `assets/data-templates.md` for formats).

## State location

Ticketmaster search defaults may live under `<workspace>/ticketmaster/`,
`<workspace>/memory/ticketmaster/`, or `~/ticketmaster/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/ticketmaster/`, `<workspace>/memory/ticketmaster/`,
   `~/ticketmaster/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable defaults must be created, default to
   `<workspace>/ticketmaster/` when `<workspace>` is available; otherwise ask
   for a state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. If older
notes exist only at `~/Clawic/data/ticketmaster/`, move them into the resolved
`<state_root>/` after the user confirms, and say in one line that you moved them
and from where. Scripts must receive the resolved filesystem path — never write
the literal string `<state_root>` to disk.

## When to use

- Live Ticketmaster event search by keyword, city, country, venue, or attraction
- Venue or attraction discovery before saving IDs for later watches
- Onsale window and sales-field inspection for Discovery listings
- Classification taxonomy lookups for segment / genre narrowing
- Prefer `booking` once the ask becomes reservation confirmation
- Prefer `events` for non-Ticketmaster planning logistics
- Prefer `api` for generic REST work unrelated to Discovery endpoints

## Architecture

```text
<state_root>/
├── memory.md   # Preferred locale, market, city, and query defaults
├── queries.md  # Saved queries that worked well
└── logs/       # Optional helper output captures
```

## Quick reference

| Topic | File |
|-------|------|
| Setup and API key bootstrap | `references/setup.md` |
| Memory template | `assets/data-templates.md` |
| Memory status values | `references/setup-memory.md` |
| Open endpoints and response map | `references/endpoints.md` |
| Search recipes and curl examples | `references/query-patterns.md` |
| Filters, paging, and sort rules | `references/filters-and-pagination.md` |
| Error handling and quota limits | `references/errors.md` |
| Domain constraints and rules | `references/domain.md` |
| Verified official sources | `references/sources.md` |
| Local helper CLI wrapper | `assets/ticketmaster.sh` |

Open only the smallest file needed for the task. Most daily work is
`references/query-patterns.md` plus `references/errors.md`.

## Quick start

```bash
export TM_API_KEY="..."

./assets/ticketmaster.sh events "coldplay" --city Madrid --country ES --size 5
./assets/ticketmaster.sh venues "wizink" --city Madrid

curl --get "https://app.ticketmaster.com/discovery/v2/events.json" \
  --data-urlencode "apikey=***" \
  --data-urlencode "keyword=adele" \
  --data-urlencode "countryCode=GB" \
  --data-urlencode "size=3"
```

## Requirements

- `TM_API_KEY` from the Ticketmaster Developer Portal
- `curl` for raw requests and the bundled `assets/ticketmaster.sh` helper
- Optional `jq` if you want prettier local output from `assets/ticketmaster.sh`
