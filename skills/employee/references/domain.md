# Domain Knowledge & Traps

## Scope

This skill manages **virtual AI employees inside a workspace**: registry,
memory, autonomy ladder, and task routing. It is not a human hiring desk,
fictional roleplay engine, or full AI-company control plane.

| Ask | Prefer instead |
|-----|----------------|
| Hire a freelancer / contractor with milestones | `hiring` |
| Source or interview human candidates | `recruiter` |
| Lead a human team (1:1, PIP, feedback) | `management` / `chro` |
| Fictional character scene | `roleplay` |
| Org-chart / multi-agent company runtime | `paperclip` |

## Traps

| Trap | Why it fails | Do instead |
|------|--------------|------------|
| Generalist employee ("handles everything") | No clear permissions or success criteria | One narrow role per employee |
| Instant autonomy on day one | External side effects before trust exists | Start at shadow or draft-only |
| Skipping memory load | Repeats corrected mistakes | Load `memory/context.md` before every task |
| Auto-routing urgent/confidential work | Wrong blast radius | Keep with main agent unless user assigns |
| Treating placeholders as paths | Writes to literal `<state_root>` / `<workspace>` | Resolve real paths first |
| Merging duplicate state roots | Silent data divergence | Pick highest-precedence root; report duplicates |
| Retiring without confirmation | Hard-to-reverse archive | Confirm, then archive under `<state_root>/archive/` |
| Using this skill for human HR actions | Wrong legal/process surface | Hand off to `hiring` / `recruiter` / `chro` |

## Operating invariants

- Registry status gates routing: only `active` employees receive work.
- Autonomy level gates external effects; review requires human approval first.
- Escalation text must include reason plus enough context for the main agent.
- Linked skill paths must point at real workspace packages the host can load.
