# Changelog

## Merged Skill Refactors

This table is the canonical record of skill refactor pull requests merged into `local`. It is used by the refactor workflow and automation when selecting the next skill.

| Skill | PR | Date | Darwin Score |
|-------|----|------|--------------|
| garden | #1 | 2026-08-04 | 85/100 |
| photography | #4 | 2026-08-04 | 80.2/100 |
| statistics | #3 | 2026-08-04 | 82.3/100 |
| cgo | #5 | 2026-08-04 | 82/100 |
| groq-api | #6 | 2026-08-04 | 81.2/100 |
| flutter | #7 | 2026-08-04 | 89/100 |
| stock-market | #9 | 2026-08-04 | 80.1/100 |
| cardano | #10 | 2026-08-04 | 82/100 |
| software-architect | #11 | 2026-08-04 | 81/100 |
| sydney | #12 | 2026-08-04 | 83/100 |
| financial-literacy | #13 | 2026-08-05 | 82.3/100 |
| chinese | #16 | 2026-08-05 | 80.3/100 |
| redis-store | #17 | 2026-08-05 | 84.7/100 |
| golf | #18 | 2026-08-05 | ~75 |
| galician | #20 | 2026-08-05 | 82/100 |
| macau | #19 | 2026-08-05 | 82/100 |
| six-thinking-hats | #21 | 2026-08-05 | Not recorded |
| pay | TBD | 2026-08-10 | 94/100 |
| home-renovation | #22 | 2026-08-05 | 85/100 |
| sell | #23 | 2026-08-06 | ~82/100 |
| passwords | #25 | 2026-08-06 | 82/100 |
| deploy | #26 | 2026-08-07 | ~82/100 |
| academy | #28 | 2026-08-08 | 84.7/100 |
| aave | #27 | 2026-08-08 | 82.6/100 |
| accountant | #29 | 2026-08-08 | 84.7/100 |
| welsh | #31 | 2026-08-08 | 84.7/100 |

## Updating This Changelog

For every skill-refactor pull request:

1. Complete and validate all refactor phases.
2. Create the pull request targeting `local`.
3. After GitHub assigns the pull request number, add a row on the same branch with the skill name, PR number, date, and final Darwin score.
4. Commit and push the `CHANGELOG.md` update so it lands with the pull request when merged.
