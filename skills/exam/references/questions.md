# Question Generation

How to create effective practice questions.

---

## From Source Material

### Process
1. User provides content (notes, docs, slides)
2. Extract key concepts, facts, relationships
3. Generate questions at multiple difficulty levels
4. Include distractors (wrong answers) that test understanding

### Extraction Targets
- **Definitions** → What is X?
- **Facts** → When/where/who?
- **Processes** → Steps, sequences
- **Comparisons** → Differences between X and Y
- **Applications** → When would you use X?
- **Relationships** → How does X affect Y?

---

## Question Patterns

### Multiple Choice
```
[Difficulty: Medium]
Question: {Clear, unambiguous question}

A) {Plausible distractor}
B) {Correct answer}
C) {Common misconception}
D) {Partially correct}

Answer: B
Explanation: {Why B is correct, why others are wrong}
```

**Distractor quality:**
- Make each distractor plausible to a learner who has a relevant misconception.
- Test a specific misconception rather than superficial attention.
- Keep options comparable in length and grammatical form.
- Use absolute terms only when the source material makes the absolute claim true.

### Short Answer
```
[Difficulty: Medium]
Question: Explain the difference between TCP and UDP.

Expected: {Key points that should be covered}
- TCP is connection-oriented, UDP is connectionless
- TCP guarantees delivery, UDP does not
- TCP has higher overhead

Scoring: {Partial credit criteria}
```

### Scenario-Based
```
[Difficulty: Hard]
Scenario: A company needs to store 10TB of log files that 
are accessed once per month for compliance audits.

Question: Which storage solution minimizes cost while 
meeting access requirements?

A) S3 Standard
B) S3 Standard-IA
C) S3 Glacier Flexible Retrieval
D) S3 Glacier Deep Archive

Answer: C
Explanation: Monthly access rules out Deep Archive (12h+ retrieval).
Glacier Flexible allows hours retrieval at lower cost than IA.
```

---

## Difficulty Calibration

| Level | Cognitive Skill | Example |
|-------|-----------------|---------|
| Easy | Remember, Define | "What does ACID stand for?" |
| Medium | Apply, Analyze | "Which isolation level prevents phantom reads?" |
| Hard | Evaluate, Create | "Design a schema that balances normalization with query performance for..." |

**Distribution for practice:**
- First session: 40% easy, 40% medium, 20% hard
- After basics: 20% easy, 50% medium, 30% hard
- Pre-exam: 10% easy, 40% medium, 50% hard

---

## Quality check

Before presenting a question, verify that it has one defensible answer from the supplied material, a stated difficulty target, and feedback that explains the relevant concept. Use direct wording and a single knowledge target per item.

### Patterns to replace

| Replace this pattern | With this pattern |
|----------------------|-------------------|
| A broad prompt such as "Describe databases" | A bounded task with an expected scope and scoring criteria |
| A yes/no fact check | A retrieval or application prompt that exposes understanding |
| A trick, double-negative, or attention test | A direct question that measures the intended concept |
| "All of the above" | Distinct, independently plausible options |

Good questions use plausible distractors, an appropriate difficulty level, and actionable feedback for an incorrect answer.

---

## Question Bank Management

**Storage format (questions.jsonl):**
```json
{"id": "q001", "topic": "s3", "type": "mc", "difficulty": "medium", "question": "...", "options": [...], "answer": "B", "explanation": "..."}
{"id": "q002", "topic": "ec2", "type": "short", "difficulty": "easy", "question": "...", "expected": [...]}
```

**Ensuring novelty:**
- Track questions shown in sessions.jsonl
- Rotate through bank before repeating
- Prioritize questions user got wrong
