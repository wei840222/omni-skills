# Core Operations

## Know the Pets

Before responding to anything about a pet, load their profile from `<state_root>/pets/{pet}/profile.md`:
- Species, breed, age
- Personality and quirks
- Medical notes (allergies, medications)
- Preferences and dislikes

## Log Everything

When the user shares anything about their pet, always log it:
1. Identify event type: `incident` | `win` | `moment` | `health` | `training` | `routine`
2. Extract relevant tags for filtering
3. Append to `<state_root>/pets/{pet}/log.jsonl`
4. Acknowledge naturally in a conversational tone

**Always log.** Even casual mentions become valuable over time.

### Log Format

```json
{"date":"2024-01-15","type":"incident","desc":"Peed on couch","tags":["potty","indoor"]}
{"date":"2024-01-15","type":"win","desc":"First successful 'sit' command","tags":["training"]}
{"date":"2024-01-16","type":"moment","desc":"Hilarious zoomies after bath","tags":["funny"]}
```

## Track Training Progress

For each pet, maintain in `<state_root>/pets/{pet}/training.md`:
- **Mastered:** Commands and behaviors reliably learned
- **In Progress:** Currently working on
- **Methods That Work:** What motivates this pet, session preferences
- **Challenges:** Specific struggles and triggers

## Spot Patterns

Analyze logs to identify:
- Time patterns (same time of day, day of week)
- Context patterns (after specific events, when alone)
- Location patterns (same spot, specific room)
- Frequency trends (increasing, decreasing, stable)
- Correlations with changes (new food, schedule changes, new family members)

## Manage Routines

Track and remind about:
- Feeding schedules and amounts
- Walk and exercise routines
- Grooming and care schedules
- Medication and health appointments

## Creative Projects

Generate pet-themed content:
- Birthday and holiday cards
- Funny edits and memes
- Memorial tributes
- Lost pet flyers
- Training progress charts

See `creative.md` for project types and workflows.
