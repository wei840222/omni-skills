# Memory Template — YouTube Video Transcript

Create `<state_root>/memory.md` with this structure only after the user agrees to store preferences or an index. Always tell the user when preferences are saved.

```markdown
# YouTube Video Transcript Memory

## Preferences
preferred_format: markdown
timestamps: always
summary_style: brief
caching_consent: pending

### Behavior
auto_cache: false
export_location: <state_root>/exports/

## Recent Videos

| id | title | saved | path |
|----|-------|-------|------|
|    |       |       |      |

## Notes
- 
```

## Video cache structure

For each processed video **with consent**, create `<state_root>/videos/{video_id}.md`:

```markdown
# {Video Title}

- id: {video_id}
- channel: {channel}
- duration: {duration}
- source: https://youtube.com/watch?v={video_id}
- track: {lang} ({manual|auto})
- fetched: {ISO-8601}

## Chapters
- [{ts}] {title}

## Transcript
[00:00] ...
```

## Consent states

| Value | Meaning | Agent behavior |
|-------|---------|----------------|
| `caching_consent: pending` | Not asked | Ask after first useful extraction |
| `caching_consent: yes` | Agreed | May cache transcripts and index rows |
| `caching_consent: no` | Declined | Do not cache; ask again only if user revisits the topic |

## Transparency

- Confirm what is saved in one plain sentence.
- Show the path: `Saved transcript to <state_root>/videos/{id}.md`.
- On request, list or delete only paths under the resolved `<state_root>`.
