1. **Pre-Commit Validation**
   - Run `uvx --from skills-ref agentskills validate skills/booking/` to ensure the skill is valid.

2. **PR Submission**
   - Use the `submit` tool to create the PR.

3. **Changelog Update**
   - Wait for the PR number to be generated.
   - Update `CHANGELOG.md` with `sed` using the actual PR number: `sed -i '56i| booking | #<PR_NUMBER> | '"$(date +%Y-%m-%d)"' | 85 |' CHANGELOG.md`.

4. **Commit Changelog**
   - Commit the changes to `CHANGELOG.md` using `git commit -am "docs(booking): update CHANGELOG.md for PR #<PR_NUMBER>"`.

5. **Pre-Commit Action**
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.

6. **Final Submit**
   - Complete the task using the `done` tool.
