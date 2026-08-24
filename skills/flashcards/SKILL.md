---
name: flashcards
description: Create effective, atomic flashcards optimized for active recall and spaced repetition (e.g., Anki). Use when the user needs to study, memorize facts, learn definitions, or format study material for spaced repetition software.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🃏"}'
  related-skills: '{"spaced-repetition":"Manages the scheduling algorithm for studying flashcards over time.","study":"Provides broader study techniques and planning that incorporates flashcards."}'
---

## Memory Science & Formatting Instructions

When the user asks to create flashcards, study material, or Anki decks, you must structure the output according to proven memory science and software constraints.

1. **When analyzing topics for memorization**, load `references/memory-science.md` to understand the Minimum Information Principle and active recall strategies.
2. **When generating final output or Anki-compatible TSVs**, load `references/anki-formatting.md` to apply correct syntax (cloze deletions, bidirectional cards) and structure.

## Core Directives

- **Atomic Cards**: Each card must test exactly one fact or concept. Break complex topics into the smallest testable units.
- **Understanding First**: Rephrase textbook content into natural language.
- **Output Formats**: Provide the cards in a Markdown table for review, and offer the raw Anki TSV format (`front\tback\ttags`) for easy import.
