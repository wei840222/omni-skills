# Common Traps and Recoveries

| Trap | Symptom | Recovery |
|------|---------|----------|
| One shared file for every subject | Topics collide; continuity breaks | Create `topics/<slug>/` namespaces from `assets/topic-template.md` |
| Auto-edit AGENTS without consent | Unexpected routing / user surprise | Generate snippet only; user pastes manually (`activation-routing.md`) |
| New lessons before any review queue | Fast forgetting; fake progress | Seed reviews after first loops; serve review-before-new |
| Long lectures instead of micro-loops | Low engagement | Split into 60–90s loops from `lesson-loop.md` |
| Streak pressure without comeback | Churn after one miss | Apply grace miss + comeback loop (`retention-ops.md`) |
| XP without mastery evidence | Score looks good, skill is shallow | Gate XP on clean passes and checkpoint quality (`progression.md`) |
| Mixing live state into `assets/` | Templates overwritten | Keep live files only under `<state_root>/` |
