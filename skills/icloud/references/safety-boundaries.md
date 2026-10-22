# Safety boundaries — iCloud

Non-negotiable execution boundaries for agent runs.

## Execution boundaries

- Collect Apple credentials and 2FA codes only through local interactive prompts.
- Require explicit confirmation before risky write operations.
- Keep logs and `<state_root>/` files free of secrets.
- Report success only after a post-action read-back.

## Confirmation template for risky actions

Before execution, state:

- target (`device_id` or exact Drive path / album+asset),
- operation effect,
- expected result,
- rollback note.

Then require explicit user confirmation.

## Minimum verification standard

- One pre-action read snapshot.
- One post-action read verification.
- One concise operation result line (success, or failure cause).
