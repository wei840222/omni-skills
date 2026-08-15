# Skill Refactor: app-store-connect

## Phase 1: Specification Compliance (Gates 1-5)
- **Gate 1**: Fixed YAML frontmatter, updated to `metadata.openclaw`, removed invalid properties.
- **Gate 2**: Moved `api-auth.md` and `workflows.md` into `references/`.
- **Gate 3**: Documented `.app-store-connect-state/` for state location.
- **Gate 4**: Migrated related-skills to metadata frontmatter.
- **Gate 5**: Removed promotional `clawic.com` links and `_meta.json`.

## Phase 2: Knowledge Research (Gate 6)
- **Research Sources**:
  - Apple App Store Connect API documentation via Wikipedia cross-check: `https://en.wikipedia.org/wiki/App_Store_Connect`
- **Updates Applied**: Confirmed existing constraints match recent reality (JWT limits, build states).

## Phase 3: Description Optimization (Gate 7)
- **Optimization**: Updated description to be intent-focused; routed complex rules to `references/` via progressive disclosure.

## Phase 4: Darwin Evaluation (Gate 8)
- **Score**: 89/100
- **Test Prompts**: Created `test-prompts.json` covering standard auth/list and complex build processing workflows.

## Phase 5: Freud Cognitive Load Audit (Gate 9)
- **Updates**: Removed negative phrasing ("Never submit a build...", "Cannot be deleted") and converted to positive instructions.
