# Memory destinations

Only load this file to decide where durable writes go.

| Artifact | Destination | Threshold |
|---|---|---|
| Person row | shared `contacts.md` | any keepable person |
| Person detail | `<contacts_root>/<name>.md` | more than one row of detail |
| Interaction line | person file or `interactions/YYYY.md` under state root | every real touch |
| Open loop | `memory.md` → `## Open Loops` | promise, favor, intro, send-X |
| Dates | person file + optional `## Dates` index | known birthday/anniversary/loss |
| Suppression | `do-not-surface.md` | death, estrangement, explicit request |
| Config | `config.yaml` | stated preference |
| Due hygiene | `memory.md` → `## Due` | roster_review cadence |
| Boxes index | `memory.md` → `## Boxes` | every extra file created |

## Boxes line shape

`- path/relative/to/state | read when <condition>`

Create the `## Boxes` line in the same turn as the file.
