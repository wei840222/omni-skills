# Migration — Legacy Parking State

## Legacy path

Older Clawic-era notes may exist only at:

```text
~/Clawic/data/parking/
```

Typical contents:

- `memory.md`
- `favorites.md`
- `cities.md`
- `findings.md`
- `sessions/`
- `archive/`

## Cutover procedure

1. Resolve the portable `<state_root>` using the rules in `SKILL.md`.
2. If legacy notes exist and the portable root is empty, propose a
   copy → validate → cutover plan.
3. Wait for explicit user confirmation before copying or deleting anything.
4. After cutover, keep the portable root fixed for the invocation and treat the
   legacy path as read-only archival unless the user asks to remove it.
5. Never write the literal string `<state_root>` to disk.

## Validation checklist

- Favorites retain facility names, cities, and evidence notes
- City provider order and traps survive without inventing new operators
- Vehicle height / EV / plate-storage boundaries remain intact
- No payment card numbers, passwords, or full booking receipts are copied
