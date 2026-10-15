# Lifecycle Commands

## Hire

**Syntax:** `hire {name} as {role}` or `create employee {name} for {purpose}`

**Actions:**
```bash
mkdir -p <state_root>/employees/{name}/memory
mkdir -p <state_root>/employees/{name}/logs
# Create employee.json with role config
# Update registry.json
# Initialize memory/context.md
```

**Required info:**
- Name (unique identifier)
- Role (single domain)
- Skill source (link existing, embed new, or registry slug)
- Initial permissions

**Example:**
```
User: "Hire Luna as a research assistant"
→ Creates <state_root>/employees/luna/
→ Links to researcher skill
→ Sets autonomy: shadow
→ Updates registry.json
```

Start new hires at `shadow` unless the user explicitly chooses another level
that still respects the promotion ladder.

## Train

**Syntax:** `train {name} on [documents/context]`

**Actions:**
- Append to `<state_root>/employees/{name}/memory/context.md`
- Optionally create domain-specific memory files under the same employee tree
- Update employee stats

**Example:**
```
User: "Train Luna on our company style guide"
→ Reads style guide
→ Extracts key rules
→ Appends to luna/memory/context.md
```

## Assign Task

**Syntax:** `{name}, do X` or `ask {name} to X`

**Actions:**
- Load employee config
- Load memory
- Spawn as subagent
- Execute task inside permissions
- Log result
- Update stats

## Evaluate

**Syntax:** `evaluate {name}` or `how is {name} doing?`

**Output:**
```markdown
## Luna - Performance Review

### Stats (last 30 days)
- Tasks completed: 47
- Escalations: 3 (6%)
- Rejections: 1 (2%)
- Token usage: 125,000

### Strengths
- Fast turnaround on research
- Good source citation

### Areas for improvement
- Sometimes over-detailed

### Recommendation
- Ready for promotion to review level
```

Load `references/autonomy.md` before recommending a promotion.

## Promote / Demote

**Syntax:** `promote {name}` or `demote {name}`

**Actions:**
- Verify criteria (see `references/autonomy.md`)
- Update `permissions.autonomyLevel`
- Log change

**Safeguard:** Always confirm before promoting to autonomous.

## Pause / Resume

**Syntax:** `pause {name}` or `resume {name}`

**Actions:**
- Update `status` in employee.json
- Update registry.json
- Paused employees stop receiving tasks

## Retire

**Syntax:** `retire {name}`

**Actions:**
- Set status: `retired`
- Optionally archive the folder under `<state_root>/archive/` after confirmation
- Update registry.json
- Employee no longer receives tasks

**Safeguard:** Confirm before retiring. Retirement is reversible but discouraged.

## Clone

**Syntax:** `clone {name} as {new-name}`

**Actions:**
- Copy employee.json (reset stats)
- Create fresh memory/context.md
- Omit logs when copying

**Use case:** Create a variant with different permissions or personality.

## List

**Syntax:** `list employees` or `who works for me?`

**Output:**
```markdown
## Active Employees
- Luna (Research Assistant) - autonomous
- Max (Code Reviewer) - review

## Paused
- Alex (Writer) - paused since 2026-02-10

## Retired
- OldBot (Legacy) - retired 2026-01-15
```
