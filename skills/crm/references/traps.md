# Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Designing the schema before using it | Fields invented in advance encode a process nobody has run yet, and half of them stay empty forever | Minimum record for two weeks, add a field only when a real question needs it (`references/schema.md`) |
| Importing the whole list on day one | 4,000 unqualified rows make every future query a filtering exercise and every count meaningless | Import what you would actually contact this quarter; archive the rest outside the CRM (`references/import.md`) |
| Stage = how the seller feels | Optimism migrates upward, so the pipeline inflates exactly when it needs to be honest | Verifiable exit criteria per stage (`references/pipeline.md`) |
| Using the tool's default win probabilities | They are seeded constants, not your history; a 60% "Proposal" you close at 25% overstates the quarter by 2.4× | Compute stage conversion from your own closed deals (`references/metrics.md`) |
| Keeping lost deals as "on hold" | The pipeline never shrinks, so coverage looks fine while nothing is really live | Close it lost with a reason; reopen a new deal if it comes back — that also measures resurrection honestly |
| Two status fields (lifecycle stage and deal stage) | They drift within a week and every report has to say which one it used | One field owns the truth; the other is derived or deleted (`references/schema.md`) |
| Merging duplicates by keeping the newest record | The newest is usually the emptiest — the import that created it had three columns | Merge into the richest record, field by field; oldest `created` wins for provenance (`references/hygiene.md`) |
| Enrichment before dedupe | You pay per record to enrich the same person four times, and the copies now disagree | Dedupe, then enrich the survivors (`references/automation.md`) |
| Automating follow-up on stale data | Bounces and "Dear [FIRST_NAME]" tell the recipient exactly how they are stored | Bounce sweep and merge pass before any automation is switched on (`references/hygiene.md`) |
| Deleting a contact on request and calling it done | The address survives in exports, backups, the mail tool and the warehouse, so the next campaign contacts them again | Suppress first, then delete across every copy, and keep the suppression hash forever (`references/privacy.md`) |
| Notes that say "had a call, went well" | Unsearchable and undecidable six months later — nobody can act on it | One line of substance: what they said, what changed, what is next (Rule 5) |
| Migrating by importing a CSV into the new tool | Activity history, ids and relations do not travel in a contacts CSV; the timeline is what made the CRM worth anything | Export every object, map ids, run both read-only for one cycle (`references/import.md`) |
| Buying a CRM to fix adoption | The team stopped using the last one for a reason the new UI does not address | Cut fields and reduce the update to one minute; migrate only after that works (`references/adoption.md`) |
