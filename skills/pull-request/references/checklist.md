# Pull Request Checklist

## Before Writing Any Code

- [ ] **Read CONTRIBUTING.md** — Understand project's specific requirements
- [ ] **Check issue policy** — Does this project require issues first, or accept direct PRs?
- [ ] **Search for duplicates** — Existing PRs or recently-closed attempts
- [ ] **Project accepts PRs** — Check activity, response times, any "not accepting contributions" notice
- [ ] **AI policy** — Search CONTRIBUTING.md for "AI", "bot", "automated" mentions
- [ ] **DCO/CLA** — Check if signing is required

## Scope Validation

- [ ] **Small enough** — Under 5 files and 200 lines? If not, needs discussion first
- [ ] **Verify public interfaces are unchanged** — Public interfaces unchanged? If changed, needs discussion
- [ ] **Leave Auth, crypto, permissions alone** — Auth, crypto, permissions left alone?
- [ ] **Leave License, CoC, README philosophy unchanged** — License, CoC, README philosophy unchanged?
- [ ] **Verify project is actively accepting changes** — Project not in release freeze or code lockdown?

## Before Committing

- [ ] **Tests pass** — Run project's test command (check package.json, Makefile, etc.)
- [ ] **Linting passes** — Use project's config, not your IDE defaults
- [ ] **Build succeeds** — If applicable
- [ ] **If can't run checks** — Note this explicitly in PR description
- [ ] **Remove debug code** — `console.log`, `print()`, `debugger`, `TODO: remove`
- [ ] **Remove or explain commented code** — Delete or explain
- [ ] **Ensure diff is surgical and focused** — Diff is surgical
- [ ] **Matches project style** — Check configs: `.editorconfig`, `.prettierrc`, `.eslintrc`

## Branch Hygiene

- [ ] **Rebased on target** — No merge conflicts
- [ ] **Branch name** — Follows project convention if any
- [ ] **Target branch correct** — Check default branch, not assuming `main`

## Commits

- [ ] **Message format** — Matches project requirements (conventional commits, etc.)
- [ ] **Atomic commits** — Each is one logical change
- [ ] **Squash WIP commits** — Squashed before pushing
- [ ] **DCO sign-off** — If required: `git commit -s`

## Dependencies (If Any)

- [ ] **Justified** — Truly necessary
- [ ] **Maintained** — Active development
- [ ] **License compatible** — Check against project
- [ ] **Security clean** — No known vulnerabilities
- [ ] **Size reasonable** — Not adding 500KB for one function

## Tests

- [ ] **New tests for new code** — Coverage doesn't decrease
- [ ] **Regression test for bugs** — Would have caught this bug
- [ ] **Edge cases** — null, empty, invalid input

## Documentation

- [ ] **README updated** — If behavior changed
- [ ] **API docs updated** — If interfaces changed
- [ ] **CHANGELOG entry** — If project requires it

## Security

- [ ] **Replace secrets with `<PLACEHOLDER>`** — Not even "example" keys; use `<PLACEHOLDER>`
- [ ] **Remove unsafe patterns** — eval(), exec(), verify=False, debug=True
- [ ] **Input validation** — User input is sanitized

## AI-Assisted PR Requirements

- [ ] **Marked as AI-assisted** — In title or description
- [ ] **Testing level noted** — untested / lightly tested / fully tested
- [ ] **Prompts included** — If available and helpful
- [ ] **Understanding confirmed** — "I reviewed this and understand it"
- [ ] **Human linked** — Who directed this contribution

## PR Description

- [ ] **Links issue** — `Fixes #123` or `Closes #456` (if issue exists)
- [ ] **Explains what** — Summary of changes
- [ ] **Explains why** — Reasoning behind approach
- [ ] **Testing done** — How you verified it works
- [ ] **Screenshots** — For UI changes
- [ ] **Breaking changes** — Explicitly called out
- [ ] **Uses template** — If project has one

## After Opening

- [ ] **Monitor CI** — Fix failures promptly
- [ ] **Respond to feedback** — Within 48h
- [ ] **If can't continue** — Close with handoff message
