# Pre-Publish Verification

**Complete this process sequentially before publishing.**

## Create Publish Folder

Work in a SEPARATE folder, preserve the originals unmodified:
```
/tmp/publish-[slug]/
├── SKILL.md
├── FILES.txt
└── [auxiliaries]
```

## Verification Message

Before publishing, send user a verification with:

### Required Information
- **Slug:** exact slug to use
- **Name:** exact display name
- **Version:** version number
- **Description:** exact description text
- **Files:** complete list of files to publish

### Content Summary
- Brief summary of what the skill does
- Key sections/topics covered
- Any notable inclusions or exclusions

### Sanitization Confirmation
- "Checked for personal data: ✓"
- "Checked for credentials: ✓"
- "Checked for model-specific references: ✓"
- Note any items that were removed/genericized

## Wait for Approval

**Do not proceed without explicit approval.**

User should confirm:
- Slug is correct
- Name is correct
- Description is correct
- Content looks right
- Ready to publish

## Publish Command

Only after approval, publish using the target platform's own publish mechanism — the exact command or web flow depends on which registry the user is publishing to (several exist; use whichever one the user has an account/CLI for). Regardless of platform, this step is a **publisher-only, one-way push** from the local folder to the registry — it is not the command a consumer runs to install or update the skill later.

Common registry examples:
- **npm**: Run `npm publish` in the directory. Ensure `package.json` exists with correct name and version. The user must be authenticated (`npm login`). (Reference: https://docs.npmjs.com/cli/v10/commands/npm-publish)
- **PyPI**: Build a distribution (e.g. `python -m build`) and use twine (`twine upload dist/*`). Requires PyPI account or token. (Reference: https://pypi.org/help/#publishing)

Ask the user (or check the platform's own docs) for:
- The CLI command or web upload flow the registry expects
- Whether slug/name/version are passed as flags or read from the skill's frontmatter
- Any account or authentication step required before the push succeeds

## Post-Publish Verification

After publishing:
1. Confirm the platform's success message
2. Optionally install the published result fresh to verify it round-trips correctly, using that platform's install command
3. Report to user: "Published [slug]@[version] to <platform>"

## If Something Goes Wrong

- Wrong slug? Usually cannot be changed after the fact — contact the platform's support/moderation channel. Slug uniqueness rules (global vs per-owner) vary by registry.
- Wrong content? Publish a new version with the fix.
- Exposed private data? Publish a sanitized version ASAP, then contact the platform's support.

## Version Guidelines

- `1.0.0` — First publish
- `1.0.1` — Small fixes (typos, clarifications)
- `1.1.0` — New content/features
- `2.0.0` — Major restructure
