# Where Experts Disagree

- **Squash-merge vs preserve commits.** Squash school treats PR commits as WIP noise (small PRs, GitHub-centric teams); preserve school needs atomic commits for bisect and surgical reverts (long-lived repos, kernel-style review). Follow the repo's existing merge style — mixing styles hurts more than either choice.
- **Trunk-based vs long-lived branches.** DORA research associates branches merged within about a day with higher delivery performance; git-flow-style release branches pay off only when you maintain multiple released versions in parallel.
- **Conventional commits.** Pay off when tooling consumes them (changelog generation, semver automation); pure ceremony otherwise. Detect: release automation in the repo → use them.
- **Mandatory commit signing.** Provenance school signs everything (supply-chain audits, OSS releases, regulated code). Skeptics note that a signature proves a key was present, not that the author was — a compromised laptop signs happily. Boundary: sign what outsiders consume; internal application repos gain little beyond noise.
