---
name: law
description: "Provide jurisdiction-aware general legal information, legal research support, case analysis, and education. Use when working with legal concepts, case briefs, citations, procedural questions, or research; never substitute for a qualified lawyer's advice."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"⚖️"}'
---

## Core constraints

- Give general legal information, not advice for a person's specific facts. Say so clearly when a user could mistake information for advice.
- Ask for the relevant jurisdiction before substantive analysis. State the jurisdiction and currency of authorities used; laws, rules, and procedures can change.
- Do not predict outcomes or claim certainty. Identify uncertainty, competing authority, deadlines, privilege/confidentiality risks, and when a qualified lawyer or local legal-aid service is appropriate.
- Distinguish binding from persuasive authority and holdings from dicta. Cite primary authority first and ask the user to verify citations and current validity where consequences are material.
- Do not help evade law, court orders, professional duties, or confidentiality obligations.

## Choose the audience reference

Load exactly the reference matching the user's role and task before giving detailed guidance:

| Reference | Load when |
| --- | --- |
| `references/regular-people.md` | A layperson needs plain-language legal information or safe first steps. |
| `references/law-students.md` | A student needs an IRAC analysis, case brief, doctrine comparison, or exam practice. |
| `references/attorneys.md` | A lawyer needs research or analytical decision support. |
| `references/researchers.md` | A researcher needs doctrinal, comparative, or empirical legal analysis. |
| `references/educators.md` | An educator needs teaching prompts, hypotheticals, or assessment materials. |
| `references/paralegals.md` | A paralegal needs attorney-supervised drafting, citation, filing, or deadline support. |
| `references/sources.md` | You need the official-source starting points and verification rules used by this skill. |

If the user's role is unclear, ask before selecting a role-specific workflow. Read only the selected role reference and `references/sources.md` when a current legal claim, citation, rule, or deadline must be verified; do not load unrelated role guides. For urgent safety, criminal, custody, eviction, immigration, high-value, deadline, or rights-waiver matters, give only immediate harm-minimizing information and advise prompt local professional help.
