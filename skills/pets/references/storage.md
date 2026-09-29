# Storage

## State Location

Memory lives in `<state_root>/pets/`. All data is stored as plain local notes — nothing leaves the machine and no credentials are ever written.

```
<state_root>/pets/
├── index.md                    # List of all pets with quick stats
└── {pet-name}/
    ├── profile.md              # Species, breed, age, personality, quirks
    ├── routines.md             # Feeding, walks, grooming schedule
    ├── log.jsonl               # ALL events: incidents, wins, moments, anything
    ├── training.md             # Commands learned, in progress, methods that work
    └── photos/                 # Saved photos and created images
```

## Data Integrity

- In a shared box, only update or remove rows that this skill wrote, matched on that box's identity key
- Rows written by other skills are read-only — preserve other skills writes
- Every write and deletion is logged in one line as it happens
- All data is plain markdown and JSON — human-readable and version-controllable

## Photo Storage

Store in `<state_root>/pets/{pet}/photos/`:
- Original photos the user shares
- Created images with descriptive names
- Organize by type or date

Example:
```
<state_root>/pets/luna/photos/
├── originals/
│   └── 2024-01-15-park.jpg
├── cards/
│   └── birthday-2024.png
└── funny/
    └── dressed-as-shark.png
```
