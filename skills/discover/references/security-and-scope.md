## Security and privacy

**Data that leaves your machine:**
- topic names, query variants, and source lookups needed to discover new information

**Data that stays local:**
- discovery preferences and activation rules in `<state_root>/memory.md`
- active interest watchlists and heartbeat state in `<state_root>/watchlist.md` and `<state_root>/heartbeat-state.md`
- dated findings in `<state_root>/findings/`

**This skill does:**
- keep recurring loops explicit and user-approved
- treat repetition as noise until novelty-test passes
- keep secrets and credentials out of local discovery memory
- require consent before contacting third parties, buying services, or making commitments
- leave package `SKILL.md` unchanged at runtime

## Scope

This skill covers:
- local discovery state in `<state_root>/`
- durable curiosity turned into a visible watchlist with explicit novelty rules
- heartbeat only for approved tracks with a quiet no-change path

This skill leaves out:
- treating generic summaries as discoveries
- monitoring topics that lack recurrence approval
- silent scope expansion
- turning discovery into external action without approval
