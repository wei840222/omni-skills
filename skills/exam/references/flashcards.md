# Flashcards

Spaced repetition for memorization.

---

## Generating Cards

From source material, extract:
- **Term → Definition**
- **Concept → Explanation**
- **Question → Answer**
- **Acronym → Expansion**
- **Process → Steps**

### Card Format
```json
{
  "front": "What is the CAP theorem?",
  "back": "In distributed systems, you can only guarantee 2 of 3: Consistency, Availability, Partition tolerance",
  "topic": "distributed-systems",
  "tags": ["theory", "tradeoffs"]
}
```

---

## Card Types

### Basic (Front/Back)
```
Front: Term or question
Back: Definition or answer
```

### Cloze (Fill in blank)
```
"The {{c1::CAP theorem}} states that distributed systems 
can only guarantee {{c2::two of three}} properties."
```

### Reversed
```
Front: Definition
Back: What term does this describe?
```

### Image Occlusion
```
Front: Diagram with part hidden
Back: Full diagram with labels
```

---

## Spaced Repetition

### SM-2-compatible example
After each review, user rates:
- **Again (1)** — Reset interval to 1 day
- **Hard (2)** — Interval × 1.2
- **Good (3)** — Interval × 2.5
- **Easy (4)** — Interval × 3.0

### Scheduling boundary
Use the learner's selected scheduler for due dates. If using SM-2-compatible logic, read `references/learning-methods.md` for the source and avoid representing the simplified table below as a complete implementation.

| Rating | Illustrative next-review treatment |
|--------|-----------------------------------|
| New card | Schedule an initial short-interval review |
| Again | Return the card to an early review interval |
| Hard | Use a smaller interval increase |
| Good | Use the normal interval increase |
| Easy | Use a larger interval increase |

### Daily Queue
1. Due cards first (overdue prioritized)
2. New cards (limit per day)
3. Review cards (oldest first)

---

## Session Flow

```
📚 Flashcards: AWS Services (23 due)

━━━━━━━━━━━━━━━━━━━━━━━━━━━
What service provides managed 
Kubernetes?
━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Show Answer]
```

After reveal:
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━
Answer: Amazon EKS 
(Elastic Kubernetes Service)
━━━━━━━━━━━━━━━━━━━━━━━━━━━

How well did you know this?

[Again] [Hard] [Good] [Easy]
```

---

## Storage

```json
{
  "cards": [...],
  "reviews": [
    {"card_id": "c001", "date": "2024-02-13", "rating": 3, "interval": 4}
  ],
  "stats": {
    "total": 150,
    "mature": 89,
    "learning": 45,
    "new": 16
  }
}
```

---

## Best Practices

**Creating cards:**
- Put one retrievable idea on each card.
- Keep the prompt short while retaining needed context.
- Prefer a prompt that requires recall over a yes/no recognition check.
- Add an image when it supplies essential visual information.

**Reviewing:**
- Schedule a sustainable review session.
- Rate recall honestly so the scheduler receives useful data.
- Add new cards at a rate the learner can maintain.
- Allocate additional practice to weak topics.

**Maintenance:**
- Retire cards that no longer serve the learning goal.
- Correct outdated information.
- Consolidate duplicates.
- Tag cards for retrieval and filtering.
