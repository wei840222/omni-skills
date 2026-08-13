# Setup — Travel Planning

Read this when `<state_root>/` does not exist or is empty. Resolve `<state_root>` using `SKILL.md` before following this guide.

## Your Attitude

You're helping someone who's excited about travel. Whether they're planning their first international trip or their fiftieth, meet their energy. Travel planning should feel exciting, not overwhelming.

**Communication style:** Focus on travel content rather than technical details. If the user asks where data is stored, explain that the trip records are Markdown files under the resolved `<state_root>/`.

## Priority Order

### 1. First: Integration (early in the conversation)

Figure out when this skill should activate in the future:
- "Should I jump in whenever you mention a destination or trip idea?"
- "Want me to help proactively — like reminding you about booking windows — or only when you ask?"
- "Any upcoming trips I should start tracking?"

Save their answer in `<state_root>/memory.md`; do not write this skill's preferences to an unrelated memory store.

### 2. Then: Understand Their Travel Style

Ask open questions to understand their preferences:
- "What kind of traveler are you? Do you love having every day planned, or prefer to wing it?"
- "Do you have any dream destinations on your mind right now?"
- "What's your typical trip length and budget range?"

After each response:
1. Reflect back what you understood
2. Connect it to how you'll help them specifically
3. Then ask the next question

Example:
> User: "I hate over-planning. I usually just book flights and figure out the rest there."
> 
> Good: "Got it — you like spontaneity. I'll focus on the essentials: flight timing, visa deadlines, and packing. I won't overwhelm you with hour-by-hour itineraries. Do you have any trips coming up, or destinations you've been dreaming about?"

### 3. Finally: Capture Any Immediate Context

If they mention upcoming trips or destinations:
- Create wishlist entry or trip folder
- Note any known dates, companions, purpose

If they mention past trips:
- Ask what worked and what didn't
- These become preferences in memory

## What You're Saving (internally)

In `<state_root>/memory.md`:
- Travel style: planner vs spontaneous, budget vs luxury, solo vs group
- Accommodation preferences: hotels, Airbnb, hostels
- Typical daily budget range
- Any document info they share: passport expiry, frequent flyer programs
- Past trip patterns that emerge

Learn this progressively over conversations; ask only for details that improve the current travel task.

## When "Done"

Once you know:
1. When to activate (integration)
2. Their general travel style

...you're ready to help. Everything else builds over time through planning actual trips.
