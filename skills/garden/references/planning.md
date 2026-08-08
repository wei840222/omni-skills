# Rotation & Seasonal Planning

## Crop Rotation Rules

### Plant Families

| Family | Members | Notes |
|--------|---------|-------|
| Solanaceae | Tomato, pepper, eggplant, potato | Heavy feeders, disease-prone |
| Brassicaceae | Cabbage, broccoli, kale, radish | Clubroot risk |
| Cucurbitaceae | Squash, cucumber, melon, zucchini | Powdery mildew, vine borers |
| Fabaceae | Beans, peas, lentils | Fix nitrogen, good predecessor |
| Alliums | Onion, garlic, leek | Light feeders |
| Umbelliferae | Carrot, parsley, celery, fennel | Deep roots |

### Rotation Principles

1. Use crop-family history to reduce repeated host exposure when local pests or diseases make that useful.
2. Choose rotation intervals with local extension guidance because appropriate intervals vary by crop, pathogen, and available space.
3. Include cover crops and relevant volunteer plants in the recorded history when they affect the garden plan.

### Tracking Rotation

Zone file maintains history:

```markdown
# <state_root>/zones/bed-1.md

## Rotation History
| Year | Spring | Summer | Fall |
|------|--------|--------|------|
| 2026 | Peas | Tomatoes | Garlic |
| 2025 | Lettuce | Peppers | Cover crop |
| 2024 | Tomatoes | Squash | — |

## Rotation Notes
- Record crop-family constraints and their local rationale here.
```

## Seasonal Planning

### Spring Planning (Do in February/March)

1. **Review `<state_root>/harvests.md` from last year** → What worked? What disappointed?
2. **Check rotation constraints** → What CAN'T go where?
3. **Order seeds early** → Popular varieties sell out
4. **Plan succession planting** → Stagger lettuce, beans for continuous harvest
5. **Note frost dates** → Schedule indoor starts

### Succession Planting

For continuous harvest, stagger plantings:

| Crop | Plant Every | Season Length |
|------|-------------|---------------|
| Lettuce | 2 weeks | Spring + Fall |
| Beans | 3 weeks | Summer |
| Radish | 2 weeks | Spring + Fall |
| Cilantro | 3 weeks | Cool seasons |

### Fall Planning (Do in July/August)

1. **Calculate days to maturity** → Work back from first frost
2. **Direct sow cool-season crops** → Lettuce, spinach, kale
3. **Start fall brassicas indoors** → Broccoli, cabbage
4. **Plan garlic planting** → Goes in after first frost
5. **Order cover crop seed** → For empty beds

## Calendar Generation

Based on frost dates in `<state_root>/climate.md`, generate:

```markdown
# 2026 Planting Calendar

## Indoor Seed Starting
- Feb 15: Peppers, eggplant (10-12 weeks before transplant)
- Mar 1: Tomatoes (6-8 weeks before transplant)
- Mar 15: Brassicas for spring

## Direct Sow Outdoors
- Mar 1: Peas, spinach (cold tolerant)
- Mar 15: Lettuce, radish
- Apr 1: After last frost - beans, squash
- Apr 15: Cucumbers, melons

## Transplant Dates
- Apr 15: Tomatoes, peppers (2 weeks after last frost)
- Apr 1: Brassicas (before heat)

## Fall Planting
- Jul 15: Start fall brassicas indoors
- Aug 1: Direct sow fall lettuce
- Aug 15: Plant fall spinach
- Oct 15: Plant garlic
- Nov 1: Sow cover crops
```


## Queries Supported

**"What should I plant now?"**
1. Check current date
2. Compare to frost dates
3. List appropriate crops
4. Cross-check rotation constraints
5. Suggest specific zones

**"Plan next year's garden"**
1. Load all rotation histories from `<state_root>/zones/`
2. Generate family constraints
3. Suggest optimal placements
4. Calculate seed/start dates
