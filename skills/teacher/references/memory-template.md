# Memory write destinations

Use this file only when persisting durable teaching state under the resolved `<state_root>`. Write plain local notes; never store credentials, safeguarding disclosures, diagnoses, or minors' contact/identity numbers.

## Boxes index (`memory.md`)

Keep `## Boxes` as the index of optional files. Each line names a relative path inside `<state_root>/` and the condition that opens it. Treat the list as dynamic.

## Due table (`memory.md`)

Use `## Due` for review dates: interventions, observation targets, rubric norming, guardian follow-ups, and cadence rows accepted from Configuration preferences.

## Destination map

| Durable result | Destination | Format notes |
|---|---|---|
| Declared preferences | `config.yaml` | Keys from `references/configuration.md` |
| Observations and indexes | `memory.md` | Include `## Boxes` and `## Due` |
| Class roster / accommodations | `classes/<class-id>.md` | Adjustment + trigger only; no diagnosis |
| Recontactable adults | `contacts/contacts.md` | One row per person; `Key` = lower-case email |
| Multi-week work | `projects/<project>.md` | Milestones and decisions |
| Shared locale/timezone | `profile.yaml` | Shared universals only |
| Reusable artifacts | `artifacts/<yyyy-mm-dd>-<slug>.md` | Plan, rubric, comment bank, run sheet; note what changed on reuse |

## Write rules

1. Update or remove only rows this skill wrote, matched on the box identity key.
2. Name every write or deletion in one line as it happens.
3. Prefer pointers (`env:…`, `keychain:…`, `1password:…`) over secret values.
4. If legacy data sits at `~/teacher/` or `~/clawic/teacher/`, migrate into `<state_root>/` and report the move in one line.
