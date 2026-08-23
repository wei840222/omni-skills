# Pull Request Practices

Use this reference after repository-specific guidance. Repository policy is authoritative when it differs from general guidance.

## Focus and reviewability

- Submit one coherent concern at a time, with a title and description that explain both the change and its reason.
- Review the full diff before submission; remove debugging artifacts and unrelated reformatting.
- Add or update tests for changed behavior, then report the exact commands and outcomes in the pull request.

## Repository policy and automation

- Read `CONTRIBUTING.md` and any pull-request template before proposing work.
- Check required status checks and workflow results before requesting review. Use the repository's branch and commit conventions.
- For API, authentication, security, or governance changes, start with the repository's required discussion process rather than assuming direct pull-request submission is acceptable.

## Sources

- GitHub Docs, *About pull requests* — https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
- GitHub Docs, *About protected branches* — https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches
- GitHub Docs, *Contributing to projects* — https://docs.github.com/en/get-started/exploring-projects-on-github/contributing-to-open-source
