# MQTT best practices

Load this file when implementing or reviewing broker/client configuration. Prefer cited pages in `references/sources.md` over memorized option names when versions matter.

## Security traps

- Default Mosquitto allows anonymous connections on many stock configs — bots scan constantly; always configure authentication for non-lab listeners.
- TLS is mandatory for external or untrusted-path access — otherwise usernames/passwords and payloads travel in plaintext.
- Duplicate client IDs cause connection fights — both clients repeatedly disconnect each other; assign stable unique IDs per device or process instance.
- ACLs should restrict topic access — one compromised device must not read or write all topics.
- Bind intentionally: `listener 1883 0.0.0.0` exposes all interfaces; use `127.0.0.1` (or a private NIC) for local-only brokers.

## QoS misunderstandings

- Effective QoS is the minimum of publisher and subscriber — brokers downgrade when the subscriber requests lower.
- QoS 1 may duplicate messages — handlers and side effects must be idempotent.
- QoS 2 has significant overhead — only use when duplicates would cause real harm (for example non-idempotent commands).
- QoS applies per message — mixing levels on the same topic is allowed when intentional.

## Topic design pitfalls

- Starting with `/` creates an empty first level — prefer `home/temp` rather than `/home/temp`.
- Wildcards only work in subscriptions — publishing requires exact topics; do not publish to `home/+/temperature`.
- `#` matches everything including nested levels — `home/#` receives `home/a/b/c/d`.
- Some brokers limit topic depth or fan-out — verify before designing deep hierarchies.

## Connection and session management

- Persistent sessions (MQTT 3.1.1 clean session false; MQTT 5 clean start false with session expiry) preserve subscriptions and may queue messages while disconnected — backlog can surprise operators after long outages.
- Keep-alive too long delays dead-client detection — 60s is a common reasonable default.
- Reconnection logic is a client responsibility — many libraries require explicit reconnect and resubscribe configuration.
- Last will / testament only fires on unexpected disconnect paths the broker detects — a clean disconnect typically omits the will.

## Retained message traps

- Retained messages persist until explicitly cleared — old payloads confuse new subscribers.
- Clear retained state with an empty payload published with the retain flag on brokers that follow this convention — confirm against current broker docs.
- Birth/will presence pattern: publish retained "online" on connect; configure will to publish "offline" (often retained) so late joiners see last known presence.

## Mosquitto specifics

- `persistence true` (with a writable persistence location) survives restarts for retained messages and durable session state when configured correctly.
- Queue ceilings such as `max_queued_messages` reduce the chance that one slow subscriber exhausts broker memory.
- Separate listeners for local plaintext lab traffic versus TLS external traffic; do not copy public-bind examples into production without ACLs and auth.

## Debugging

- `mosquitto_sub -v` shows topic with message — essential for lab debugging.
- Subscribing to `#` sees all traffic — never leave this in production without extreme ACL isolation; it leaks everything.
- `$SYS/#` exposes broker metrics — client counts, bytes, subscriptions; treat as sensitive.
- Retained messages can survive "the fix" — explicitly clear bad retained keys after remediation.

## Cognitive-load notes (Freud)

- Lead with the exposure and auth decision before option catalogs.
- Do not open with long "don't forget" blacklists; encode failures next to the positive rule (auth, TLS, unique client ID, ACL).
- Load this reference only when implementing or reviewing config; keep the SKILL.md router short.
