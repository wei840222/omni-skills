# Core Rules


### 1. Treat Mail.app as the Unified Account Layer
- Assume provider sync is already configured in Apple Mail and operate on that local unified mailbox layer.
- Use Apple Mail's existing sync configuration instead of direct OAuth inside this skill unless user explicitly asks for setup help.

### 2. Detect Command Path Before Every Operation
- Probe command paths in strict order: `osascript`, then `shortcuts`, then `sqlite3` for read-only indexed lookup.
- If no safe path is available, stop and report the exact blocker instead of guessing.

### 3. Default to Dry-Run for Write Intents
- For compose, reply, move, archive, and delete workflows, first produce a dry-run preview with impacted messages and fields.
- Require explicit user confirmation before executing live changes from the dry-run summary.

### 4. Enforce High-Risk Confirmation Gates
- Require explicit confirmation for send, delete, bulk move, bulk archive, forwarding, and reply-all expansions.
- If external recipients are added or recipient count changes, require a second confirmation.

### 5. Use Operation IDs and Idempotency
- Generate a unique operation ID for every write workflow and include it in local operation logs.
- Before send, verify there is no prior successful send with the same operation context.

### 6. Read First, Write Once, Verify Immediately
- Resolve message identity with at least two fields (message ID plus sender or date) before any write action.
- After every write, run read-back verification and report final mailbox state.

### 7. Keep Exposure Minimal and Local-First
- Use only required fields for the requested task and avoid broad mailbox exports by default.
- Keep message bodies and attachments local, routing them only to the explicit destination defined by the user.
