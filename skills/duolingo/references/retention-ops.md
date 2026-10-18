# Multi-Topic Retention Operations

Retention must work for one or many active topics.

## Daily planner

At session start:

1. choose topic from the rotation policy
2. serve one fast win
3. serve one review item when due (review-before-new)
4. queue the next due action

## Rotation policies

| Policy | Use when | Example |
|--------|----------|---------|
| Alternating days | two balanced priorities | Mon english, Tue cooking |
| Weighted split | one primary topic | 70% english, 30% cooking |
| Daily stack | short sessions available | english loop then cooking loop |

## Review queue rules

- Schedule reviews from misses and low-confidence passes.
- Each topic keeps its own queue in `topics/<slug>/queue.md`.
- The daily planner should include at least one review before new content when a review is due.

## Comeback triggers

- Day 1 miss: lightweight reminder and one easy loop.
- Day 3 miss: restart with a guided recap.
- Day 7 miss: rebuild momentum with a mini-checkpoint.

## Weekly reset

Weekly operations:

- archive completed queue items
- rebalance topic rotation
- review checkpoint outcomes
- adjust next-week loop targets
