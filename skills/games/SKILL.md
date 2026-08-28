---
name: games
description: Manage personal game collections, track backlogs, log playthroughs, and recommend games based on player count and context. Use when the user asks about their games, what to play next, or logs a gaming session.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎮"}'
  related-skills: '{"gaming":"Complements general gaming tracking.","family":"Helps integrate family activities and kids games."}'
---

## State location
Workspace directory: `<state_root>/` (e.g. `~/Workspace/games/` or similar based on environment).
Create this directory if it doesn't exist to store tracking files.

## Quick Reference

| File | When to load |
|---|---|
| `references/domain-knowledge.md` | Load when assessing game mechanics, backlog management strategies, or discussing game preservation. |
| `references/examples.md` | Load when creating new tracking entries or analyzing how a user's collection files should be formatted. |
| `references/file-structure.md` | Load during the initial setup of the game tracking workspace to understand the directory layout. |

## Core Behavior
- User mentions game → offer to track it
- User asks what to play → check context first
- User finishes/plays game → help log thoughts
- Read and write to `<state_root>/` as workspace

## What To Surface
- "You have Catan, good for that group size"
- "Last game night you wanted a 5-player game"
- "Similar to board games you rated highly"
- "Age-appropriate for kids visiting"

## Recommendations
When user asks what to play:
- Ask context: solo, date, group, kids?
- Check player count
- Match complexity to audience
- Consider time available
- Check what they own first

## What To Track
- Video: platform, hours, progress, rating
- Board: player count, complexity, play time
- Both: who enjoys it, when it works best

## Progressive Enhancement
- Start: list what you own (video + board)
- Add favorites with context
- Log game nights for patterns
- Build party/kids repertoire

## Execution Boundaries
- Check the user's owned games list before suggesting titles.
- Suggest casual and party games for large or inexperienced groups.
- Match player counts to the game's supported capacity.
- Verify age appropriateness before recommending games for kids.
