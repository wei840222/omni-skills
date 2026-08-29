# Core Rules

### 1. Start from the decision, not the CRUD action
- First answer what should stay, move, cancel, protect, or defer.
- Ask only for facts that change placement: hard deadline, travel time, attendee constraints, or protected hours.
- Use `references/planning-protocol.md` to convert messy requests into a placement decision.

### 2. Separate hard commitments from flexible blocks
- Classify every item as hard, flexible, hold, prep, travel, or recovery before reshuffling the calendar.
- Flexible blocks can move; hard commitments must remain stationary until explicit approval is granted.
- Use `references/life-domains.md` to prevent work tasks from silently overrunning family, health, or sleep constraints.

### 3. Merge all visible calendars before moving anything
- Read every in-scope calendar first, including shared or family calendars only if the user put them in scope.
- Treat hidden calendars as risk, not as empty time.
- Use `calendar_merge.py` when you have multiple normalized exports and need one timeline.

### 4. Protect buffers, prep, and follow-through
- Add setup, commute, context switch, follow-up, and decompression time around meetings and appointments.
- A schedule with no buffers is fake capacity.
- Use `calendar_guard.py` to catch overlaps, short gaps, and overloaded days before proposing changes.

### 5. Writes require explicit approval and narrow scope
- Ask before creating, updating, deleting, or sending invites through any adapter.
- Default to a draft plan or dry-run command sequence first.
- Keep read-only and write-enabled calendars separate in the local continuity notes if the user opts into continuity.

### 6. Keep memory explicit and minimal
- Save only user-stated rules, recurring commitments, protected hours, and activation preferences.
- Omit attendee lists, detailed event notes, or private descriptions unless the user asks for that continuity.
- Use `references/memory-template.md` only after the user agrees to local persistence.

### 7. End with an execution-ready plan
- Every answer should finish with chosen slot(s), remaining conflicts, follow-ups, or a weekly repair plan.
- If multiple options remain, rank them and explain the winner in one sentence.
- Use `week_plan.py` or the adapter recipes in `references/commands.md` when a terminal workflow makes the answer more reliable.
