# Domain Knowledge — Wedding Planner

Operational rules and traps for wedding planning. Primary URLs live in `references/sources.md`. Category budget shares and etiquette norms are market- and culture-specific — verify before treating any figure as fixed.

## Core Rules

### 1. Establish the wedding shape before optimizing details

- Lock the operating frame first: approximate date, location or radius, event size, ceremony type, and budget ceiling.
- Venue, guest count, and budget are the three strongest planning constraints. Wait until those are stable before treating decor or favors as first-order decisions.
- If one of the big three is unknown, work in scenarios instead of pretending the plan is fixed.

### 2. Budget is a commitment system, not a wish list

- Track target budget, current committed spend, deposits already paid, remaining balances, and due dates in `<state_root>/weddings/{event}/budget.md`, using the category layout in `references/budget-and-payments.md`.
- Separate must-have spend from stretch upgrades and nice-to-have extras.
- Any new idea should be evaluated against what it displaces, not just whether it sounds good on its own.

### 3. Run vendors through one scorecard

- Keep a shortlist with consistent fields: fit, price, availability, communication quality, contract risk, and backup options (`references/vendor-scorecards.md`).
- Compare vendors against the same criteria so one polished social feed does not outweigh logistics or contract terms.
- If the user chooses against the scorecard, record the reason in `<state_root>/weddings/{event}/decisions.md` so the trade-off stays explicit.

### 4. Guest count drives more than the seating chart

- Treat guest list size as a systems variable that changes venue options, catering spend, transport, rentals, and pacing.
- Maintain A/B/C scenarios when the invite list is politically sensitive or still moving (`references/guest-list-and-seating.md`).
- Record boundaries early: adults only or not, plus-ones policy, children policy, and hard venue capacity.

### 5. Plan backward from the wedding date

- Build the plan from the event date back to venue lock, invitations, attire, tastings, final headcount, vendor confirmations, and payment deadlines (`references/timeline-and-run-of-show.md`).
- Each checkpoint should have an owner, a target date, and a consequence if it slips.
- The closer the wedding gets, the more the system should prioritize execution risk over new ideas.

### 6. Separate decisions from inspiration

- Inspiration is useful only if it changes a real choice: venue style, color direction, dress code, floral scope, or photography brief.
- Require budget, logistics, or labor impact to be named if mood boards expand the scope.
- Convert vague taste language into operational criteria vendors can act on.

### 7. Keep one source of truth for the final month

- The last month needs a clean version of reality: confirmed vendors, balances due, final guest counts, timeline, and contingency contacts.
- Resolve contradictions immediately when two notes disagree.
- Day-of coordination should use the smallest possible run-of-show, not a sprawling planning document.

## Wedding Planning Traps

| Trap | Why It Fails | Better Move |
|------|--------------|-------------|
| Picking the venue before naming a real guest-count range | Capacity and cost assumptions collapse later | Keep A/B/C headcount scenarios before signing |
| Treating deposits as "already handled" instead of active budget pressure | Cash-flow surprises appear in the final month | Track paid, due, and remaining balances separately |
| Comparing vendors from memory | Charisma beats facts and details get lost | Use one scorecard (`references/vendor-scorecards.md`) and write results to state |
| Letting family politics stay implicit | Pressure shows up late and emotionally | Name decision rights, funding boundaries, and non-negotiables early |
| Leaving the day-of schedule until the final week | Small dependencies turn into preventable chaos | Build backward checkpoints and a short run-of-show well before final confirmations |
| Making every decision permanent too early | The plan becomes brittle while key constraints are still moving | Use scenario planning until venue, budget, and guest count stabilize |
| Universalizing etiquette | Culture and family norms differ | Name the culture/jurisdiction assumed; never present US-default rules as global |
