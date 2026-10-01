# Memory and inventory templates

Use this file when initializing or updating durable VPS state. Paths are under the resolved `<state_root>` unless a shared inventory path is explicitly configured.

## Suggested layout

```text
<state_root>/
|-- config.yaml           # declared preferences (see configuration.md)
|-- memory.md             # observations, ## Boxes index, ## Due, ## Hosts
|-- changes/
|   `-- <year>.md         # dated operational events
`-- artifacts/            # recovery runbooks, cutover plans, decision notes
```

Shared (optional, host-wide):

- servers inventory — one row per host keyed by `Name` + `Provider`; update in place, never duplicate
- domains inventory — registrar, expiry, where a name points (migration is DNS as much as compute)
- finances / profile — currency, locale, country universals when the host already keeps them

## `memory.md` sections

- **`## Boxes`** — dynamic index of per-box note paths; the index *is* the file list
- **`## Hosts`** — VPS-only attributes inventory has no column for (image, snapshot policy, private-network membership, what it serves), keyed by the same `Name`
- **`## Due`** — restore drills, certificate/provider renewals, spend reviews, reboot windows

## Write rules

- Declarations in `config.yaml` win over observations in `memory.md`
- Observations never overwrite declarations; record disagreement as an observation
- No live credentials under any of these paths
- When a session creates, rebuilds, resizes, discovers, or destroys a host — or opens/closes ports, sets snapshot policy, times a restore, or records spend — update inventory + `changes/<year>.md` before the session ends
