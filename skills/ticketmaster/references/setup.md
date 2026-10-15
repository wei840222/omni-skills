# Ticketmaster Setup

## API key

1. Create a Ticketmaster Developer account and register an application.
2. Copy the Discovery API consumer key.
3. Export it for the current shell:

```bash
export TM_API_KEY="your-ticketmaster-key"
```

Keep the key in the environment. Do not write it into skill memory, screenshots,
or committed examples.

## Resolve state location first

Before creating files, resolve `<state_root>` with the State location rules in
`SKILL.md`. Then substitute the real filesystem path into the commands below.
Never create a directory literally named `<state_root>`.

## Create local working memory

```bash
mkdir -p /absolute/path/to/<state_root>/logs
cp /path/to/installed/ticketmaster/assets/data-templates.md /absolute/path/to/<state_root>/memory.md
touch /absolute/path/to/<state_root>/queries.md
```

If the skill is already installed locally, copy the structure from
`assets/data-templates.md` into the resolved `<state_root>/memory.md`. See
`references/setup-memory.md` for status values.

## Smoke test the API

```bash
curl --get "https://app.ticketmaster.com/discovery/v2/events.json" \
  --data-urlencode "apikey=***" \
  --data-urlencode "keyword=test" \
  --data-urlencode "size=1"
```

Expected result: JSON with `_embedded.events` or an empty but valid search
result payload. Auth failures usually mean `TM_API_KEY` is missing or wrong.

## Smoke test the helper

```bash
chmod +x /path/to/installed/ticketmaster/assets/ticketmaster.sh
/path/to/installed/ticketmaster/assets/ticketmaster.sh events "metallica" --size 1
```

If `jq` is installed, output is pretty-printed. Otherwise the helper prints raw
JSON.

## Suggested first defaults

Add these to `<state_root>/memory.md` after the first successful request:

- default locale
- default country or market
- common city filters
- preferred sort order
