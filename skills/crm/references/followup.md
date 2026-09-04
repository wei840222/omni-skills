# Follow-Up Cadence

Tier is a decision made once per person and stored in `## People` in `memory.md`, keyed by the lowercased email; recency is computed from `interactions/<year>.md`. Together they produce the overdue list, which is the only list the user needs on a normal day.

| Tier | Who | Touch every | Overdue means |
|---|---|---|---|
| A | Live deals, active clients, the ten people who move your year | 1-2 weeks | Something is slipping right now |
| B | Past clients, warm network, dormant opportunities | Quarter | Worth a reason to reach out, not an apology |
| C | Everyone else worth keeping | Year, or on a trigger (job change, funding, launch) | Nothing — a C contact is not a debt |

Default `stale_days` is 90 and applies to tier-B-and-unassigned contacts with no open deal. A contact with an open deal is governed by the deal's next step (Rule 3), never by the stale sweep — otherwise the same person appears on two lists and both get ignored.
