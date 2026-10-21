---
name: face
description: >
  Shortlist AI-generated human faces from Generated Photos for agent avatars,
  profile pictures, and group images with gender, age-look, pose, race, hair,
  eye, and emotion filters, plus transparent previews when present. Use when
  the user wants a human face, avatar shortlist, profile face, transparent
  avatar, or reusable Generated Photos detail link. Prefer `agent` for persona
  and voice, `stock-images` for non-face placeholders, and `image-generation`
  for custom prompt-based faces.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"👤","requires":{"bins":["curl","python3"]}}'
  related-skills: '{"agent":"Persona, voice, and identity writing after a face is chosen.","stock-images":"Generic placeholders and non-face stock/avatar seeds instead of Generated Photos faces.","image-generation":"Prompt-based generative faces when a library shortlist is not enough.","image":"Compress or convert the chosen avatar file after selection.","image-edit":"Crop, mask, or background edits on an already chosen face asset."}'
---

# Face

Give an agent, persona, group, or chat surface a human-looking face quickly by
shortlisting Generated Photos gallery results and waiting for an explicit pick.

## State location

Chosen-face memory may exist in `<workspace>/face/`,
`<workspace>/memory/face/`, or `~/face/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/face/`, `<workspace>/memory/face/`, `~/face/`.
3. If none exists and durable avatar memory must be created, default to
   `<workspace>/face/` only with user consent.
4. If more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/face/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Host-shared identity files such as workspace `IDENTITY.md` are outside
`<state_root>` and need separate consent.

```text
<state_root>/
└── chosen-face.md    # Optional approved detail URL and notes
```

## When to use

- Need 3–6 human face options for an agent avatar or profile image
- Filter by gender and optional gallery facets already exposed by the site
- Prefer transparent preview when the page embeds one
- Persist an approved detail-page link for reuse

Route elsewhere when:

- Defining persona/voice → `agent`
- Generic placeholders / non-face stock → `stock-images`
- Prompted generative art → `image-generation`
- Pixel edits on a chosen file → `image-edit` / `image`

## Core workflow

1. Confirm gender (and any extra filters the user named).
2. Open a stable listing URL; start from
   `https://generated.photos/faces/beautified/{gender}/young-adult`.
3. Extract cards from HTML before opening a browser.
4. Present 3–6 numbered options with detail link, preview, and transparent
   preview when available.
5. Wait for an explicit choice. Do not auto-apply an avatar.
6. After approval, keep the detail-page URL (not only the CDN preview) and
   optionally store it under `<state_root>/chosen-face.md`.

Load references only when needed:

- `references/filters.md` — build or narrow gallery filter paths
- `references/extraction.md` — HTML extractor, transparent pairing, 429 backoff,
  detail-page preview notes
- `references/sources.md` — product pages, API boundaries, and license terms

## Response shape

```text
I found 4 options for your agent face.

1. Option A
   Detail: https://generated.photos/face/...
   Preview: https://images.generated.photos/...
   Transparent: https://images.generated.photos/...   # omit if absent

2. Option B
   ...

Tell me which one you want and I will prepare it as the avatar.
```

## Execution targets

- **Filter fidelity**: Follow listing links the current page emits; do not invent
  deeper URL combinations from memory.
- **Background handling**: Prefer embedded transparent CDN URLs when present;
  do not invent a public background route parameter.
- **Option limit**: Return 3–6 faces.
- **Link persistence**: Save the `/face/...` detail URL for reuse.
- **User consent**: Change or store an avatar only after explicit approval.
- **Rate limits**: On HTTP 429, back off and report the failure honestly; do not
  fabricate options.

## External endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| `https://generated.photos` | Filter path segments and face detail page GETs | Browse/filter faces and open detail pages |
| `https://images.generated.photos` | Image GETs only | Preview and transparent preview retrieval |

No credentials are required for gallery HTML browsing. Paid REST API access is
out of scope for this skill; see `references/sources.md`.
