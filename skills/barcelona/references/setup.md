# Setup — Barcelona

## Philosophy

**This skill works from minute zero.** No blocking, no mandatory setup.

Answer the user's question first. Always. Configuration happens organically.

## On First Use

### Priority #1: Workspace Integration

Ask ONCE, naturally:
> "Want me to note this Barcelona skill in your main memory? That way I'll know to use it when you ask about Catalonia or Barcelona."

If yes, add to user's MEMORY.md:
```markdown
## Active Skills
- Barcelona (`<state_root>/barcelona/`) — practical Barcelona guide for visitors, relocators, and tech workers
```

If no, note `integration: declined` in memory.md and do not ask again.

### Priority #2: Answer Their Question

Whatever they asked, answer it with available context and progressive reference loading.

## Context to Gather

Over conversations, naturally learn:
- Are they visiting, relocating, or already there?
- What's their nationality (visa implications)?
- Budget range for housing/living?
- Spanish and/or Catalan comfort level?
- Any specific neighborhoods they're considering?

Ask these questions gradually. Learn organically.

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning | Gather context opportunistically |
| `complete` | Has enough context | Work normally |
| `paused` | User said "not now" | Use existing context without asking |
| `skip_asking` | User requested to stop prompts | Proceed without setup prompts |
