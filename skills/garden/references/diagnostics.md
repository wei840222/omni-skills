# Problem Diagnosis

## Integrated Pest Management (IPM) Framework

Follow the EPA four-tier IPM approach when diagnosing problems. It applies to home gardens and selects controls by effectiveness and risk. [EPA, Integrated Pest Management Principles](https://www.epa.gov/safepestcontrol/integrated-pest-management-ipm-principles)

1. **Set Action Thresholds** — One pest doesn't mean control is needed. Determine when pest populations become an economic threat.
2. **Monitor and Identify** — Accurately identify the organism and assess whether control is needed before taking action.
3. **Prevention** — Use cultural methods first: crop rotation, resistant varieties, pest-free rootstock, clean tools.
4. **Control** — If prevention fails, evaluate controls by effectiveness and risk:
   - Choose less-risky, effective controls first, such as targeted chemicals or mechanical methods.
   - Escalate only when monitoring and thresholds support the change; use pesticide products according to their labels and local guidance.

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

## Common Symptoms → Questions to Investigate

### Yellow Leaves

| Pattern | Likely Cause | Check |
|---------|--------------|-------|
| Lower leaves first | Nutrient, moisture, or age-related factors | When was the plant fertilized and watered? |
| Between veins (interveinal) | Nutrient availability or root-zone factors | Is a soil test available? |
| All over, plus wilting | Root-zone moisture or drainage factors | What is the soil moisture and drainage? |
| Spots with yellow halo | Disease, injury, or environmental factors | Was there recent rain, humidity, or damage? |
| New growth yellow | Nutrient availability or root-zone factors | Is a soil test available? |

### Wilting

| Pattern | Likely Cause | Check |
|---------|--------------|-------|
| Midday only, recovers evening | Heat or water-demand factors | Check temperature and soil moisture |
| Constant, soil is wet | Root-zone or drainage factors | Check drainage and roots before treating |
| Constant, soil is dry | Water availability factors | Check soil moisture and irrigation |
| Sudden, one side of plant | Local injury, root, or vascular factors | Inspect without assuming a diagnosis |
| Progressive from bottom | Disease, root-zone, or age factors | Check history and consider local diagnosis support |

### Spots & Discoloration

| Pattern | Likely Cause | Treatment |
|---------|--------------|-----------|
| Brown spots, concentric rings | Disease or injury patterns | Document symptoms; seek local diagnosis before treatment |
| Black spots on roses | Disease or environmental patterns | Improve airflow and seek local diagnosis before treatment |
| White powder on leaves | Fungal or environmental patterns | Improve airflow and seek local diagnosis before treatment |
| Rust-colored spots underside | Disease patterns | Document symptoms and seek local diagnosis before treatment |
| Mosaic pattern, distortion | Virus, pest, or nutrient patterns | Seek local diagnosis before treatment |

### Pest Identification

| Signs | Pest | IPM Response |
|-------|------|--------|
| Sticky residue, tiny insects | Sap-feeding insects may be present | Identify the organism and apply IPM thresholds |
| Silver trails, holes | Mollusc or chewing-pest damage may be present | Identify the organism and apply IPM thresholds |
| Webbing under leaves | Mites or other arthropods may be present | Identify the organism and apply IPM thresholds |
| Holes in leaves, green caterpillars | Chewing insects may be present | Identify the organism and apply IPM thresholds |
| Wilting despite water, grubs in soil | Root-zone pests or disease may be present | Identify the cause before selecting control |

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
