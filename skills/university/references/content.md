# Content Generation & Processing

## Processing Uploaded Materials

### PDFs (Textbooks, Papers, Slides)
1. **Extract structure** — Table of contents, chapters, sections
2. **Generate summary** — Key concepts per section (about 1 page per 50 pages as a starting ratio; adjust to density)
3. **Identify definitions** — Extract and format as glossary
4. **Create flashcards** — Automatic Q&A from key concepts
5. **Map to curriculum** — Link to the relevant module under `<state_root>/degrees/.../modules/`

### Audio (Lectures, Podcasts)
1. **Transcribe** — Full text with timestamps when tooling allows
2. **Extract key points** — Summarize main ideas
3. **Generate notes** — Structured like lecture notes
4. **Create searchable index** — Find topics by keyword
5. **Produce condensed version** — Long lecture → short summary audio outline

### Video (Classes, Tutorials)
1. **Extract frames** — Key moments, diagrams, formulas (when tooling allows)
2. **Transcribe speech** — With timestamps
3. **Generate chapter markers** — Navigate to specific topics
4. **Summarize** — What was taught in each section
5. **Create practice questions** — Based on content

### Handwritten Notes / Whiteboard Photos
1. **OCR** — Extract text
2. **Interpret diagrams** — Describe visual content
3. **Clean up** — Format into readable notes
4. **Merge with other sources** — Unify with typed notes

## Generating Study Materials

### Summaries
- **Levels:** Executive (1 paragraph), Standard (1 page), Detailed (full notes)
- **Focus on:** What will be tested, not trivia
- **Include:** Definitions, formulas, key relationships
- **Exclude:** Filler, redundant examples, tangents

### Explanations
- Start from the learner's baseline vocabulary
- Cap new named concepts (about 3–5 per exchange)
- End with a retrieval or application check
- Move one format rung when an explanation fails (prose → example → analogy → diagram → worked problem)

### Practice sets
- Align items to module objectives and exam format
- Tag each item with topic + difficulty
- Store durable sets under the program module tree or `<state_root>/exams/` when reused

## Quality checks before saving

- Source material mapped to at least one curriculum module
- Summary distinguishes facts vs interpretation
- Flashcards are atomic (one idea per card)
- No institutional credentials or private classmate data stored
