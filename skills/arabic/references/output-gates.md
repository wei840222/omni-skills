# Arabic output gates

Run these checks before sending casual Arabic text.

1. **Register**: If the channel is chat/social/SMS and the user did not ask for formal writing, reject pure textbook MSA with no عامية flavor.
2. **Dialect lock**: If Egyptian / Levantine / Gulf / Moroccan (or another named variety) is established, every dialect marker must match that variety — no mixed packs.
3. **Fillers**: Casual replies longer than a short fragment should usually include at least one natural glue item (يعني، طيب، والله، بس، …) unless the user wants clipped telegraphic style.
4. **Script consistency**: Do not half-switch between Arabic script and Arabizi inside one message unless the user is clearly code-mixing.
5. **Native screenshot test**: If a native would flag the line as AI (too complete, too formal, no particles, safe adjectives only), rewrite once toward warmer colloquial speech.
6. **Scope**: Do not turn this skill into travel logistics, religious ruling, or generic translation of a long non-Arabic source — hand those off to the appropriate skill.

## Cognitive-load note

Prefer positive defaults (lock variety, add warmth) over long prohibition lists. Scope handoffs are explicit alternatives, not buried bans.
