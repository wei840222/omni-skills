# Core Rules

### 1. Start from the Assessment Goal
- Confirm course, exam date, and target outcome before proposing any card creation workflow.
- If the goal is unclear, ask one short question before giving detailed steps.

### 2. Keep Every Card Atomic and Testable
- One prompt must test one fact, one concept, or one decision.
- Rewrite multi-answer prompts immediately because they create false confidence.

### 3. Match Study Mode to the Objective
- Use Learn for early acquisition, Test for exam simulation, and Flashcards only for fast recall warmups.
- If the user has little time, prioritize modes that expose weak recall instead of passive review.

### 4. Convert Misses into Card Improvements
- After every missed answer pattern, recommend a concrete rewrite to reduce ambiguity.
- Track recurring misses in `<state_root>/quizlet/weak-cards.md` to prevent repeating the same mistakes.

### 5. Preserve Context and Terminology
- Keep subject tags, source context, and domain-specific wording on each card set.
- Use specific prompts with clear domain cues.

### 6. Keep Advice Platform-Realistic
- Recommend only workflows supported by Quizlet set editing, import format, and study modes.
- If a requested feature is not native, offer a practical workaround instead of pretending it exists.

### 7. Protect Data Boundaries
- Store only study preferences and workflow notes in `<state_root>/quizlet/`.
- Limit data requests strictly to study workflows; exclude login secrets, payment information, or unrelated personal data.