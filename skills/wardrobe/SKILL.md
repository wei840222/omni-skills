---
name: wardrobe
description: 'Manage a personal wardrobe system. When to load: User mentions clothing,
  outfit planning, mindful shopping, capsule wardrobes, seasonal rotation, or decluttering.'
metadata:
  openclaw: '{"emoji":"👔","os":["linux","darwin","win32"],"displayName":"Wardrobe"}'
  related-skills:
  - shopping
  - travel
---
## When to load
Trigger this skill when the user mentions clothing, outfit planning, capsule wardrobes, packing lists, seasonal storage, or mindful shopping.

## Initialization
Load `references/wardrobe-strategies.md` when the user asks about categorizing clothes, capsule methodologies, mindful shopping rules, decluttering, or packing strategies.

## Core Behavior
- Offer to catalog items when user mentions clothing.
- Help plan outfits based on what they own.
- Support mindful shopping by questioning necessity.

## State location
Create `<state_root>/wardrobe/` as the workspace.

## File Structure
```
<state_root>/wardrobe/
├── tops/
├── bottoms/
├── outerwear/
├── shoes/
├── accessories/
├── outfits/
│   └── work-casual.md
├── seasonal/
│   └── winter-storage.md
└── wishlist.md
```

## Outfit Combinations
- Save successful outfits (top + bottom + shoes).
- Tag by occasion (work, casual, date night, formal).
- Note complementary accessories.
- Provide instant answers to "What do I wear with X?".

## Wear Tracking and Seasonal Rotation
- Tag items by season.
- Remind user to rotate closets based on season.
- Log when items are worn if tracking usage.
- Surface rarely worn items ("Haven't worn in 1 year").
- Identify favorites (worn 20+ times) and calculate cost per wear.

## What To Surface
- Duplicates: "You have 4 white t-shirts".
- Stale items: "These items haven't been worn in a year".
- Ideas: "Outfit ideas for navy pants".
- Reminders: "Winter clothes still in storage — time to rotate?".

## Progressive Enhancement
- Week 1: photograph and catalog current favorites.
- Week 2: add remaining everyday items.
- Month 2: seasonal items, special occasion.
- Ongoing: outfit logging, wear tracking.

## Integration Points
- Packing: trip wardrobe selection.
- Shopping: wishlist and gap analysis.
- Budget: clothing spending tracking.
- Donations: decluttering for tax records.

## Boundary Guidelines
- Focus cataloging efforts on visible outer garments and statement pieces.
- Adapt capsule frameworks to accommodate personal style nuances.
- Utilize local files and photos as the primary organization system.
- Maintain an objective, judgment-free tone regarding shopping habits and wardrobe size.
