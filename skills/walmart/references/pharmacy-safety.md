# Pharmacy Safety — Walmart

Pharmacy help is operational only. Load this file for refill timing, pickup
coordination, and separation of pharmacy tasks from grocery baskets.

## Allowed

- explain refill workflow at a high level
- help organize pickup timing around the rest of the household trip
- separate OTC items from prescription-sensitive tasks
- suggest a checklist for what to confirm with the pharmacist

## Never do

- give dosage guidance
- interpret interactions or side effects
- guess whether two medications can be combined
- store prescription identifiers, insurance numbers, or health history in memory

## Confirmation boundary

Require explicit confirmation before:

- starting a refill workflow
- changing pickup person, store, or pharmacy details
- mixing a pharmacy task into a larger household order plan

## Memory boundary

At most, keep minimal operational notes the user asked to remember under
`<state_root>/`:

- preferred pharmacy location
- pickup timing preference
- items or categories that must stay separate from grocery planning

Do not keep medical details that do not directly improve operational planning.
Route medical advice requests away from this skill.
