# Sandbox Testing

Isolated environment for safe single-skill trials.

## Setup

Prefer a disposable directory the host already allows. Example pattern (replace the install command with the user's actual skill manager):

```bash
# Create an isolated test folder under a temp path the host permits
mkdir -p /tmp/skill-test/<slug>
# Copy or install the candidate package into that folder only
# Do not install into the live agent skill path until the user approves
```

If the runtime supports sub-agents, prefer spawning one with **only** the candidate skill loaded rather than mutating the main session.

## Running tests

**Option 1: Sub-agent isolation (recommended)**

Spawn a sub-agent instructed to:

- Load ONLY the candidate skill package
- Ignore unrelated workspace skills and prior chat state
- Run the agreed test tasks
- Return activation notes, outputs, failures, and token/cost signals

**Option 2: Manual static review**

- Read `SKILL.md` and routed references
- Trace the happy path and failure path
- Flag credentials, destructive defaults, and unclear triggers

## Test tasks

Define 2–3 realistic prompts the user would actually ask:

- What would I try first if this skill were installed?
- What edge case would break it?
- Does the description match when the skill should load?

## What to observe

- Does it activate for the intended prompts?
- Are instructions concrete enough to execute without guessing?
- Does it conflict with an already-installed skill?
- Is token cost acceptable for the value delivered?
- Is output quality good enough to keep?

## Credentials and failures

- **Needs credentials:** ask for disposable test credentials, or skip auth-dependent paths and mark them untested.
- **Candidate missing:** verify the package path or registry name with the user's skill manager; do not invent a catalog URL.
- **Mid-run failure:** let the isolated runner exit cleanly; capture logs; adjust the task; retry once.
- **Many auxiliary files:** load `SKILL.md` first; open references only when the trial path requires them.

## Cleanup

```bash
rm -rf /tmp/skill-test/<slug>
```

Remove only the disposable trial directory. Do not delete the user's live skill install or `<state_root>` notes without explicit approval.

## Graduating to real use

Only after a successful sandbox trial:

1. User explicitly approves install
2. Install into the real skill location via the user's manager (`skill-finder` / `skill-manager` as appropriate)
3. Smoke-test once in the real context
4. Optionally append a dated note under `<state_root>/trials.md`
