# Where The Data Lives

One default per situation, with the trigger for leaving it. Costs and limits change: verify before committing.

| Situation | Default | Move when |
|---|---|---|
| One person, under ~200 contacts, no team | Markdown or JSON files in `<state_root>/crm/db/` | Queries stop being greppable, or two devices start conflicting |
| One person, needs real queries or history | SQLite, one file, one table per entity | Someone else needs to write to it concurrently |
| Small team, wants a UI and shared writes | A hosted CRM with a real export (Attio, Pipedrive, Folk) | Never for volume alone — move only for a capability you can name |
| Already living in Notion or Airtable | Stay there; a database with a relation field is a CRM | Relations get slow, or you need automated dedupe |
| Enterprise process, admin, integrations mandated | Salesforce or HubSpot | — |
| Only need "who do I know and when did we last talk" | The shared contacts box plus `interactions/<year>.md` | A deal appears with a value and a date attached |

Lock-in test before adopting anything: can you export contacts, companies, deals, *and* activity history, with ids intact, without paying? A CRM you cannot leave is a CRM that no longer has to earn you.

Verify export paths with the vendor docs listed in `references/sources.md` before committing.
