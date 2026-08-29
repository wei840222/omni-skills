# Output Gates

Before shipping a build, a capability, or a code change that touches the platform:

- Which of the five layers does this belong to, and does the fix act on that layer?
- Every new Info.plist purpose string written in the user's language and describing the real use?
- New capability applied in all three places, and to every target that uses it (Rule 3)?
- Anything added to launch measured against the 400 ms budget on the oldest supported device (Rule 6)?
- Any new persistence: protection class chosen, and does background code need it before first unlock (Rule 7)?
- Any store-facing change checked against the guideline that governs it — purchases, account deletion, login options, privacy labels (Rule 8)?
- Does the change work when the permission is denied, the network is absent, and the background task never ran?
- Is this destructive to user data (a migration, a keychain wipe, a container reset)? Then it names exactly what is lost and ships behind an explicit confirmation, avoiding copy-paste blocks.
- Did anything durable come out of this — an app or identifier, a device, an SDK, a release, a rejection, a baseline, a platform fact, an artifact? Then it is written to its box in `<state_root>/memory-template.md`, with its `## Boxes` line, in this same turn.
