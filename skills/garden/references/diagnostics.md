# Problem Diagnosis

## Integrated Pest Management (IPM) Framework

Follow the EPA/USDA four-tier IPM approach when diagnosing problems:

1. **Set Action Thresholds** — One pest doesn't mean control is needed. Determine when pest populations become an economic threat.
2. **Monitor and Identify** — Not all insects are harmful. Accurately identify pests before taking action. Less than 1% of insect species are considered harmful (USDA).
3. **Prevention** — Use cultural methods first: crop rotation, resistant varieties, pest-free rootstock, clean tools.
4. **Control** — If prevention fails, evaluate controls by effectiveness and risk:
   - **First:** Biological control (predators, parasitoids, pathogens)
   - **Second:** Mechanical control (trapping, weeding, row covers)
   - **Third:** Targeted chemicals (pheromones to disrupt mating)
   - **Last resort:** Broadcast spraying of pesticides

### Biological Control Agents

- **Predators:** Lady beetles eat aphids; predatory mites eat thrips and scales
- **Parasitoids:** Tiny parasitic wasps lay eggs in host insects
- **Pathogens:** Beneficial nematodes, Bt (Bacillus thuringiensis) for caterpillars

**Habitat for beneficials:** Plant marigolds, provide habitat for beneficial insects, bats, and birds. This is the most cost-effective long-term pest control strategy (USDA).

## Diagnostic Flow

When user reports a problem:

1. **Identify the symptom** (yellow leaves, spots, wilting, pests visible)
2. **Check plant history** → `<state_root>/plants/{name}.md` for past issues
3. **Check zone conditions** → `<state_root>/zones/{zone}.md` for environmental factors
4. **Cross-reference patterns** → same issue in multiple plants?
5. **Identify the pest/disease** accurately before recommending treatment
6. **Assess action threshold** — is intervention needed?
7. **Recommend IPM-appropriate treatment** starting with least-risk options
8. **Log the diagnosis** in `<state_root>/plants/{name}.md`

## Common Symptoms → Causes

### Yellow Leaves

| Pattern | Likely Cause | Check |
|---------|--------------|-------|
| Lower leaves first | Nitrogen deficiency | When last fertilized? |
| Between veins (interveinal) | Iron/magnesium deficiency | Soil pH? |
| All over, plus wilting | Overwatering | Soil moisture? Drainage? |
| Spots with yellow halo | Fungal infection | Recent rain/humidity? |
| New growth yellow | pH lock-out | Soil test needed |

### Wilting

| Pattern | Likely Cause | Check |
|---------|--------------|-------|
| Midday only, recovers evening | Heat stress | Normal for hot days |
| Constant, soil is wet | Root rot | Drainage, reduce water |
| Constant, soil is dry | Underwatering | Increase frequency |
| Sudden, one side of plant | Bacterial wilt | Inspect stem, may be fatal |
| Progressive from bottom | Fusarium/Verticillium | Check rotation history |

### Spots & Discoloration

| Pattern | Likely Cause | Treatment |
|---------|--------------|-----------|
| Brown spots, concentric rings | Early blight | Remove affected leaves, fungicide |
| Black spots on roses | Black spot fungus | Improve air circulation, fungicide |
| White powder on leaves | Powdery mildew | Baking soda spray, improve airflow |
| Rust-colored spots underside | Rust fungus | Remove affected parts, avoid wetting leaves |
| Mosaic pattern, distortion | Virus | Remove plant, control aphids |

### Pest Identification

| Signs | Pest | IPM Response |
|-------|------|--------|
| Sticky residue, tiny insects | Aphids | Spray off with water; encourage ladybugs; neem if threshold exceeded |
| Silver trails, holes | Slugs/snails | Beer traps, diatomaceous earth, handpick at dusk |
| Webbing under leaves | Spider mites | Increase humidity; predatory mites; neem if severe |
| Holes in leaves, green caterpillars | Caterpillars | Handpick; Bt spray; row covers for prevention |
| Wilting despite water, grubs in soil | Root pests | Beneficial nematodes; crop rotation next season |

## Questions to Ask

When diagnosing, gather:

1. **Which plant(s)?** → Load plant history
2. **When did it start?** → Correlate with weather/activity
3. **Affected area?** → All leaves, new growth, old growth, one side?
4. **Recent changes?** → New fertilizer, moved, weather event?
5. **Photo?** → If available, visual diagnosis

## Logging Diagnoses

Update plant's health log:

```markdown
## Health Log
| Date | Issue | Treatment | Outcome |
|------|-------|-----------|---------|
| 2026-06-20 | Yellow lower leaves | Applied nitrogen fertilizer | Improved in 1 week |
| 2026-07-05 | Aphids | Neem spray x3 days | Cleared |
| 2026-07-20 | Blossom end rot | Consistent watering + calcium | No new affected fruit |
```

## Pattern Recognition

After logging issues:

- Same plant, recurring problem → Note variety weakness
- Same zone, multiple plants → Environmental issue
- Same pest, every year → Add to spring prevention checklist
- Same timing → Correlate with climate events

## Prevention Reminders

Based on history, suggest preventive actions:

"Last year aphids appeared in June. Consider:
- Inspect new growth weekly starting late May
- Plant nasturtiums as trap crop
- Encourage ladybugs"
