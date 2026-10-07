# Conflict Basics

- Set `merge.conflictStyle zdiff3` (git >=2.35) once: markers include the base version, so you see what each side changed instead of guessing intent.
- Ours/theirs invert during rebase: "ours" = the branch you are rebasing onto, "theirs" = your own commit being replayed — rebase checks out upstream and applies your commits as patches on top.
- After resolving: `git grep -nE '^(<{7}|={7}|>{7})'` must return nothing, then build/tests, then `--continue`.
- Everything else → `references/conflicts.md`.
