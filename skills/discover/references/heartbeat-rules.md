# Heartbeat Rules - Discover

Use heartbeat to revisit approved discovery topics without turning the system into noise.

## Source of truth

Keep the workspace `HEARTBEAT.md` snippet minimal.
Treat this file as the stable contract for recurring discovery behavior.
Store mutable state only in `<state_root>/heartbeat-state.md`.

## Start of every heartbeat

1. Ensure `<state_root>/heartbeat-state.md` exists.
2. Read `<state_root>/watchlist.md` and keep only topics marked `Heartbeat: active`.
3. Read the last lens used and the last material discovery marker.
4. Skip any topic that no longer has a clear reason or novelty bar.

## For each active topic

1. Restate why the topic matters now.
2. Choose one fresh lens not used last time:
   - direct
   - contrarian
   - operator
   - geographic
   - regulatory
   - stakeholder
   - practical next-step
3. Do a light pass first. Deepen only if the signal looks promising.
4. Apply `references/novelty-test.md`.

## If the finding is new

- Append one dated entry to `<state_root>/findings/{topic}.md`
- State what changed, why it matters now, and one next move
- Update `last_material_discovery_at` and `last_angle_used`

## If nothing changed

- Update `last_angle_used`
- Set `last_heartbeat_result: HEARTBEAT_OK`
- Return `HEARTBEAT_OK`

## Safety rules

- Most heartbeat runs should bypass action
- Log only high-value novel findings
- Keep topic scope strictly bounded
- Retain existing heartbeat topics only during execution
- Restrict external action to discovery and logging
- If the topic is becoming vague, pause it instead of improvising
