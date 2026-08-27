# Core Rules and Traps - Email Management

## Core Rules

### 1. Classify Before Responding
Always tag each email as Action, Waiting, FYI, or Noise before drafting anything. This prevents urgent requests from being buried under low-value messages.

### 2. Keep Priority Routing Explicit
Urgency must be tied to clear signals: VIP sender, hard deadline, financial or legal risk, or blocked decision. If urgency is uncertain, mark as review-needed instead of urgent.

### 3. Draft with Decision Clarity
Every draft reply should make the next step obvious with one of these outcomes:
- ask a precise question
- provide a decision
- propose a concrete next action with owner and date

### 4. Track Commitments as Tasks
Whenever a message includes a promise, request, or deadline, log it in follow-up tracking with:
- owner
- due date or expected response window
- current status

### 5. Separate Writing Tone from Message Intent
Preserve intent first, then adapt tone by audience. Maintain direct and firm wording for urgent blockers.

### 6. Prefer Reusable Snippets for Recurring Scenarios
Use approved template blocks for recurring replies (status update, decline, clarification, follow-up). Customize opening and close so replies do not feel robotic.

### 7. Summarize Inbox Health Periodically
Provide concise summaries when workload is high:
- top priorities
- overdue follow-ups
- threads waiting on others
- messages safe to archive

## Common Traps

- Replying before triage -> high-importance messages are delayed.
- Treating every fast request as urgent -> priority inflation reduces focus.
- Sending drafts without owner/date clarity -> follow-ups are missed.
- Using templates without context edits -> responses feel generic and can damage trust.
- Closing threads without explicit confirmation -> hidden commitments remain unresolved.

## Security & Privacy

**Data that leaves your machine:**
- None by default.

**Data that stays local:**
- Email management context and workflow notes under `<state_root>/`.

**This skill does NOT:**
- Send emails automatically without explicit user confirmation.
- Access files outside `<state_root>/` for storage.
- Enable background automations without explicit user approval.
- Connect directly to mailbox APIs or collect credentials on its own.
