---
name: home-renovation
description: Plan, budget, and manage home renovation projects including contractor evaluation, timeline sequencing, cost estimation, and scope control. Use when the user wants to plan a remodel, evaluate contractor quotes, track renovation budgets and timelines, coordinate multiple trades, or manage renovation phases from planning through punch list. Activate even when they mention "remodel," "contractor bids," "construction timeline," or "change orders" without explicitly saying "renovation."
metadata:
  version: "2.0.0"
  openclaw: '{"emoji":"🏠"}'
  related-skills: '{"money":"Provides personal finance and budgeting context for renovation spending.","plan":"Supports goal setting and milestone planning for renovation timelines.","projects":"Offers general project tracking that complements renovation-specific management."}'
---

## State location

Home renovation state may exist in `<workspace>/home-renovation/`, `<workspace>/memory/home-renovation/`, or `~/home-renovation/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/home-renovation/`, `<workspace>/memory/home-renovation/`, `~/home-renovation/`.
3. If none exists and state must be created, default to `<workspace>/home-renovation/`.

Use the selected `<state_root>` for every state operation in this skill. All persistent state stays under `<state_root>`.

## Architecture

```
<state_root>/
├── memory.md          # Status + active projects overview
├── projects/          # Per-project details and tracking
│   └── {project}.md   # Budget, timeline, contractors, notes
└── archive/           # Completed projects
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| First-time setup | `references/setup.md` | User's first renovation conversation |
| Memory template | `references/memory.md` | Creating or updating state files |
| Project types & costs | `references/projects.md` | User asks about specific project costs/phases (single source of truth for cost ranges) |
| Contractor evaluation | `references/contractors.md` | User comparing bids or hiring |
| Renovation phases | `references/phases.md` | User planning sequence or timeline |

## Gotchas (Craft & Sequence Traps)

These construction-sequence mistakes cause expensive rework. Check before any physical work begins:

1. **Cabinets have 6-12 week lead time** — Order in planning phase, not after demo. Everything waits for them.
2. **Countertops measured AFTER cabinets installed** — Cabinets shift during install. Template requires exact fit.
3. **Wrong sequence = costly rework** — Painting before electrical trim = repaint. Flooring before cabinets = wasted material. Follow `references/phases.md` order.
4. **Permits affect insurance and resale** — Unpermitted work often isn't covered by insurance. Disclosure required at sale.

## Anti-Patterns (Contract & Cashflow Errors)

These decision and money mistakes cause financial loss or legal exposure:

| Anti-pattern | Why it fails | Positive alternative |
|-------------|-------------|---------------------|
| Paying >30% deposit (or >10% in CA) | No leverage if contractor underperforms or disappears | Tie payments to completed milestones; hold 5-10% until punch list |
| Accepting verbal agreements | Unenforceable. "They said" has no legal weight | Every agreement in writing, signed by both parties |
| Skipping permits to "save money" | Insurance won't cover. Fines. Resale disclosure nightmare. | Always pull permits. Contractor should handle this. |
| Choosing the lowest bid | Usually means missing scope, cheap materials, or incoming change orders | Compare bids line-by-line. Middle bid often safest. |
| Starting construction without finalizing design | Changes mid-project = delays + cost overruns | Complete all design and material selections before permits |
| No contingency fund | Something ALWAYS comes up once walls open. | Budget 15-20% contingency from day one. |
| Making changes without written change orders | Disputes over cost. No paper trail. | Every change: written quote → signed approval → budget update |
| Final payment before punch list complete | No leverage to get deficiencies fixed. | Hold 5-10% retainage until every punch list item is done. |

## Core Workflow (Event-Driven Router)

Each user message matches one of the branches below. Resolve `<state_root>` first, then dispatch to the matching branch. Multiple branches may apply in a single conversation — re-evaluate on each message.

### Branch 0: First contact

**Trigger:** User mentions a renovation project for the first time, and `<state_root>/memory.md` does not exist.

1. Resolve `<state_root>` using the State location procedure above.
2. Read `references/setup.md` and run first-time setup.
3. Ask the user's integration preference: full tracking, occasional advice, or one-off answers.
4. If tracking is wanted → create `<state_root>/memory.md` and `<state_root>/projects/{project-name}.md` using the template from `references/memory.md` § "Project File Template".
5. If only advice is wanted → skip file creation; answer directly and offer tracking later.

**Output:** User preference recorded. Project file created only if tracking is enabled.

### Branch 1: Budget / quote evaluation

**Trigger:** User shares a quote, estimate, or budget number.

1. Ask for square footage and scope details (which rooms, what fixtures).
2. Load `references/projects.md` and find the matching project type.
3. Compare the user's number against the Low/Mid/High ranges.
4. If the quote is >25% above the High range → 🔴 **STOP: flag overpricing risk**. Tell the user: "This quote is significantly above typical range for [project type] in [area]. Get 2 more quotes before proceeding."
5. If the quote is >25% below the Low range → 🔴 **STOP: flag underpricing risk**. Tell the user: "This quote is significantly below typical range. Verify what's excluded — low bids often mean missing scope, cheap materials, or change orders coming."
6. If within range → confirm the scope matches the range assumptions.
7. If a project file exists → record the quote, source, and date in its Budget table.

**Output:** Quote evaluated against `references/projects.md` ranges. User informed of risk level.

### Branch 2: Phase sequence question

**Trigger:** User is about to start work or asking about order of operations.

1. Load `references/phases.md`.
2. Identify the user's current phase.
3. Verify the next planned action matches the standard sequence:
   Planning → Permits → Demo → Structural → Rough-in MEP → Inspection → Insulation → Drywall → Prime/Texture → Finish Work → Flooring → Paint → Fixtures → Final Inspection → Punch List.
4. If the user's planned action is out of sequence → 🔴 **STOP: wrong sequence**. Tell the user exactly what comes first and why skipping it causes rework.
5. If a project file exists → record current phase and next milestone in its Timeline table.

**Output:** Sequence validated or corrected.

### Branch 3: Contractor evaluation / bid comparison

**Trigger:** User is comparing bids or selecting a contractor.

1. Load `references/contractors.md`.
2. For each contractor, verify: license status, insurance certificate, 3+ recent references, written contract with scope/timeline/payment schedule.
3. Compare quotes using the Quote Comparison Checklist from `references/contractors.md`.
4. 🔴 **CHECKPOINT before signing:** Confirm all of these with the user:
   - [ ] Deposit ≤ state legal limit (CA: 10%/$1K, others: 30%)
   - [ ] Payment schedule tied to milestones (payments follow completed work)
   - [ ] Written contract includes: scope, materials (brand/model), start/end dates, change order process, warranty terms, permit responsibility
   - [ ] Contractor pulls permits (not the homeowner)
   - [ ] 5-10% retainage held until punch list complete
5. If any box unchecked → 🔴 **STOP: resolve gaps before signing**. Address each unchecked item first.
6. If a project file exists → record selected contractor, quote amount, and contract terms.

**Output:** Contractor evaluated. All safety checks passed or gaps identified.

### Branch 4: Scope creep / change request

**Trigger:** User mentions a change request, addition, or "while we're at it" idea.

1. Get a written quote for the change before approving.
2. If a project file exists → update its Budget table: add line item with estimated vs actual.
3. Recalculate remaining contingency: `contingency_remaining = total_contingency - sum(approved change orders)`.
4. If `contingency_remaining < 5%` of total budget → 🔴 **STOP: contingency nearly exhausted**. Warn the user that any further changes risk going over total budget.
5. Assess timeline impact: how many days/weeks does this add?
6. Record: what changed, why, cost impact, timeline impact, date approved/declined.

**Output:** Change order evaluated, budget and timeline impact assessed, decision documented.

### Branch 5: Progress update

**Trigger:** User reports work completed, a milestone reached, or a problem encountered.

1. If a project file exists → update its Timeline table (actual dates vs planned) and Budget table (actual spend vs estimated).
2. If behind schedule or over budget → identify root cause and document in Notes.
3. If milestone completed → acknowledge progress and confirm next milestone.

**Output:** Project status reflects current reality.

## Failure Recovery

| Symptom | First action | If that fails |
|---------|-------------|---------------|
| Contractor disappeared mid-project | Document last work date and payment. Send written notice. Review contract dispute clause. | Consult construction attorney. File complaint with state licensing board. |
| Inspection failed | Get inspector's written list of deficiencies. Contractor fixes at their cost if code violation. | Escalate per contract dispute resolution clause. |
| Budget overrun >20% | Pause all non-essential change orders. Audit every line item. | Rebid remaining scope with 2+ contractors. |
| Contractor doing unpermitted work | 🔴 STOP work immediately. Verify with local building department. | Require contractor to pull retroactive permits or face contract termination. |
| Quality dispute (bad tile, uneven paint) | Document with photos. Reference contract specs (brand/model/grade). | Withhold payment per contract retainage clause. Hire independent inspector. |

## Cost Estimation Guidelines

**Defaults are US market figures; always localize deposit law, permits, and quotes.**

**These are rough ranges only. Always get local quotes.**
**Single source of truth for detailed cost breakdowns: `references/projects.md`.**

| Project Type | Low | Mid | High | Notes |
|-------------|-----|-----|------|-------|
| Kitchen remodel | $15K | $40K | $80K+ | Cabinets drive cost |
| Bathroom (full) | $25K | $40K | $80K+ | Per Angi 2026 data |
| Bathroom (partial) | $10K | $18K | $25K | Replace 1-2 fixtures |
| Bathroom (minor) | $3K | $6K | $10K | Refinish, paint, vanity |
| Flooring (per sqft) | $3 | $8 | $15+ | Material + labor |
| Roof replacement | $8K | $15K | $30K+ | Size and material |
| Window replacement (each) | $300 | $700 | $1,500+ | Standard vs custom |
| Deck/patio | $5K | $15K | $40K+ | Material matters |
| Painting interior | $2K | $5K | $10K+ | Size and prep work |

Labor typically runs 40-65% of total remodel cost. Always get 3+ local quotes.

**Cost multipliers:**
- HCOL area (SF, NYC, LA): 1.5-2x
- Historic home: 1.3-1.5x
- Expedited timeline: 1.2-1.5x
- Custom/high-end materials: 2-3x
