# Anki Formatting Guidelines

## Import and Structure

- **TSV import format**: `front\tback\ttag1 tag2` — tabs separate fields, spaces separate tags.
- **Tags for organization**: Use hierarchical tags `subject::topic::subtopic` for filtered study.

## Card Types

- **Bidirectional cards**: For definitions, create both term→definition AND definition→term to prevent recognition-only learning.
- **Cloze deletion syntax**: `{{c1::answer}}` for a single deletion, `{{c1::first}} and {{c2::second}}` for multiple deletions on different cards.
- **Image occlusion**: Use for diagrams, maps, and anatomical images by hiding labels and revealing them on the flip.

## Best Practices for Card Design

- **Too much text on back**: Keep answers under 20 words. Long answers provide a weak recall signal.
- **Orphan cards**: Cards without context fail. Include source or chapter information in tags.
- **Copy-paste from textbook**: Rephrase in your own words. Understanding must precede memorization.
- **Skipping hard cards**: Difficulty means you need it most. Always create a simplified replacement card when suspending a difficult card.

## Spaced Repetition Best Practices

- **New cards/day**: Target 10-20 for sustainable learning. More causes review pile-up.
- **Review intervals**: Trust the algorithm. Allow the algorithm to automatically handle all card rescheduling.
- **Again vs Hard**: Use "Again" for complete failure (resets interval). Use "Hard" if you struggled but eventually recalled the answer.
- **Leeches**: Cards failed 8+ times (leeches) usually need rewriting, not more repetition.

## References
- Anki Software: https://en.wikipedia.org/wiki/Anki
