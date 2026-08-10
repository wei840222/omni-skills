## Climate Configuration

### USDA Hardiness Zone

USDA released an updated Plant Hardiness Zone Map in 2023. It uses 1991–2020 observations from 13,412 weather stations and represents 30-year average annual extreme minimum temperature. The map is a planting-hardiness input, not a complete local forecast or a standalone climate-change indicator. [USDA ARS, 2023](https://www.ars.usda.gov/news-events/news/research-news/2023/usda-unveils-updated-plant-hardiness-zone-map/)

**Action:** Verify your current zone at [planthardiness.ars.usda.gov](https://planthardiness.ars.usda.gov/). Update `<state_root>/climate.md` if your zone changed.

### Setup `<state_root>/climate.md`

After the user chooses climate tracking, create `<state_root>/climate.md` from this placeholder template and fill it only with user-provided or user-approved local data:

```markdown
# Climate Profile

## Location
- **USDA Zone:** [zone]
- **Latitude:** [latitude, optional]
- **Elevation:** [elevation, optional]

## Frost Dates
- **Last spring frost:** [local average date]
- **First fall frost:** [local average date]
- **Growing season:** [local estimate]

## Temperature Ranges
- **Record low:** [local value, optional]
- **Typical winter low:** [local range, optional]
- **Summer high:** [local range, optional]

## Precipitation
- **Annual:** [local average, optional]
- **Dry season:** [local months, optional]
- **Wet season:** [local months, optional]
- **Irrigation notes:** [user-approved observations]

## Microclimate Notes
- [user-approved sun, wind, drainage, or frost observations]

## Alert Thresholds
- **Frost alert:** [user-selected threshold]
- **Heat alert:** [user-selected threshold]
- **Wind alert:** [user-selected threshold]
```

## Seasonal Planting Windows

Based on frost dates, calculate:

| Category | Start After | End Before |
|----------|-------------|------------|
| Tender annuals (tomato, pepper) | Last frost + 2 weeks | First frost |
| Hardy annuals (lettuce, peas) | 4 weeks before last frost | 6 weeks before first frost |
| Cool season crops | Fall: 8 weeks before first frost | Spring: 6 weeks after last frost |

## Climate-Aware Recommendations

When user asks "what can I plant now?":

1. Check current date against frost dates
2. Calculate weeks until/since frost events
3. Filter plant suggestions by timing
4. Note microclimate exceptions ("bed-3 runs cold, wait extra week")

## Alert Triggers

When user reports weather:

**"Frost tonight"**
1. List tender plants currently in ground
2. Suggest protection methods:
   - Cover with frost cloth
   - Harvest mature produce
   - Move containers indoors
3. Note affected zones (especially frost pockets)

**"Heat wave coming"**
1. Check soil moisture and follow the plant's care needs
2. Consider shade cloth for sensitive plants
3. Harvest cool-season crops before bolting
4. Early morning watering preferred

**"Storm warning"**
1. Stake/secure tall plants
2. Harvest ripe produce
3. Check drainage in problem areas
4. Secure garden structures

## Zone-Specific Climate and Weather Impact

After tracking consent, attach user-approved microclimate observations to the relevant zone and significant weather observations to `<state_root>/log/YYYY-MM.md` using the asset templates.
