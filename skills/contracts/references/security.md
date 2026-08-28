# Security & Privacy Requirements

## Storage Rules

### Local-Only by Default

```
✅ REQUIRED
├── All contracts in <state_root>/ (user-controlled)
├── Metadata in local files only
├── No cloud sync unless user explicitly enables
└── No network transmission of contract content

⚠️ SECURITY CONSTRAINTS
├── Keep files strictly on the local filesystem
├── Keep contract text within local storage only
├── Sanitize logs to exclude contract content
├── Use only local extraction tools
```

### File Permissions

- Contracts folder: `chmod 700` (owner-only access)
- Individual files: inherit from folder
- Backups: warn if unencrypted backup detected

---

## Data Sensitivity

### What Contracts Contain

| Data Type | Sensitivity | Handling |
|-----------|-------------|----------|
| Names | Medium | Extract, don't expose in logs |
| Addresses | High | Extract, minimize storage |
| SSN / Tax IDs | **Critical** | Flag, skip extraction |
| Bank accounts | **Critical** | Flag, skip extraction |
| Salaries | High | Extract with caution |
| Signatures | High | Skip processing |

### GDPR Considerations (EU)

- **Data minimization** — Only extract necessary metadata
- **Right to erasure** — Support full deletion on request
- **No automated decisions** — Provide raw text only for user interpretation
- **Retention awareness** — Require explicit user consent prior to deletion

---

## Legal Boundaries

### The Skill MUST FOLLOW these strict boundaries:

1. **Provide factual extraction only** — Present clauses as written; defer interpretation of "fair" or "standard" to the user
2. **Remain neutral** — Present the information objectively and instruct the user to make signing decisions independently
3. **Present facts without assessment** — Highlight specific clauses without assigning a risk score
4. **Extract specific data only** — Output the contract's actual contents rather than comparing against industry norms
5. **State the written terms** — List the terms of the agreement without forecasting future events or dispute outcomes
6. **Preserve original text** — Keep all legal language exactly as written in the source document

### The Skill CAN:

1. ✅ Extract factual data (dates, amounts, parties)
2. ✅ Track deadlines and send reminders
3. ✅ Organize and search contracts
4. ✅ Show specific clauses when asked
5. ✅ Flag items for review ("this has an arbitration clause")
6. ✅ Aggregate costs across contracts

### Mandatory Disclaimers

When user asks legal questions:

> "I can show you the relevant clause, but for interpretation or advice, please consult a qualified attorney."

When flagging unusual terms:

> "This clause may be worth reviewing with a lawyer before signing."

---

## Confidentiality

### NDA-Aware Handling

- Treat ALL contracts as potentially confidential
- Expose counterparty names only upon explicit user request
- Keep all contract snippets strictly within the skill context
- If contract references NDA, flag as extra-sensitive

### Attorney-Client Privilege

- If contract folder contains legal correspondence, treat as privileged
- Skip analysis and summarization for legal advice documents
- Safest approach: treat lawyer emails as opaque files

---

## Incident Response

### If Contract Exposed Accidentally

1. Assess what was exposed calmly
2. Identify affected parties
3. Consider notification obligations
4. Document the incident
5. Review and tighten access controls

### If User Requests Cloud Sync

- Warn about risks explicitly
- Recommend encryption before sync
- Require manual opt-in before enabling
- Log that user acknowledged risks
