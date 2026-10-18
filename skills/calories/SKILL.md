---
name: calories
description: >
  Track calories, macros, and weight trends from meal photos, text logs, and
  nutrition labels. Use when the user logs a meal or drink, keeps a food diary,
  asks how many calories something has, wants a cut/bulk/maintenance or protein
  target, asks for TDEE or measured maintenance calories, reads a food label,
  asks whether to eat back workout burn, or asks why the scale stalled or jumped
  overnight. Covers TDEE calibration from the user's own logs, restaurant and
  alcohol estimates, plateaus and water weight, smart-scale body-fat readings,
  GLP-1/medical guardrails, and eating-disorder safety. Prefer `dietitian` or
  `meal-planner` for menus, `nutrition` for micronutrients, `gym` for training
  programming, `fasting` for eating windows, and `water` for fluid-only tracking.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🍎","requires":{"config":["<state_root>/calories/"]}}'
  related-skills: '{"dietitian":"Turn calorie/macro targets into meal plans and timing.","nutrition":"Micronutrients and broader dietary adequacy beyond calories and macros.","gym":"Training programming for a cut, bulk, or recomposition.","fasting":"Eating-window and fast tracking when time-restricted eating is the ask.","water":"Fluid intake and hydration advice when the user is not logging food calories.","meal-planner":"Menu construction and shopping lists once targets already exist."}'
---

## State location

Calories preferences, food library, daily logs, and memory are persistent user state. Resolve one `<state_root>` before any read or write:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order: `<workspace>/calories/`, `<workspace>/memory/calories/`, `~/calories/`.
3. If several candidates exist, use only the highest-precedence directory, report the split copies, and do not merge or cross-write.
4. If none exists and the user wants durable calorie-tracking state, create `<workspace>/calories/` when `<workspace>` is available; otherwise ask for a state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the rest of the invocation.

Use the selected `<state_root>` for every calories state path under `<state_root>/calories/` (`config.yaml`, `memory.md`, `library.md`, `log.md`). Legacy `~/Clawic/data/calories/`, `~/clawic/calories/`, and bare `~/calories/` copies are migration sources only — move them into the resolved `<state_root>/calories/` when the user asks, and say in one line that you moved them and from where. Skill resources stay under `references/` and `assets/`; never treat the literal string `<state_root>` as a filesystem directory name.

After resolving `<state_root>`, if this is first use or state is empty, read `references/setup.md`. File formats live in `assets/data-templates.md`.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/calories/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| units | metric \| imperial | metric | Converts bodyweight, portions, and every formula input/output (kg↔lb, cm↔in) |
| energy_unit | kcal \| kJ | kcal | All energy figures; kJ = kcal × 4.184 (`references/labels.md` for kJ-labeled countries) |
| summary_cadence | per_meal \| daily \| weekly \| none | per_meal | When running totals are reported back to the user |
| clarify_style | ask_once \| assume | ask_once | Ask the single clarifying question, or estimate silently and state the assumption that moves the number most |

Preference areas to record as the user reveals them:

- **logging medium** — photo-first, text-first, or label-first; affects which path in `references/estimation.md` opens by default
- **goal style** — casual logging vs coached (weekly trend reviews, proactive check-ins); affects prompting intensity everywhere
- **food conventions** — home cuisine, staple dishes, recurring restaurants; affects portion defaults and library seeding
- **data of record** — an external tracker the user also logs in; affects whether totals mirror its database entries or this skill's estimates
- **restrictions** — vegetarian/vegan, allergies, religious rules; affects protein-source assumptions and meal defaults
- **weigh-in ritual** — scale owned or not, daily vs 3-4×/week tolerance, cycle-aligned comparisons; affects the protocol and averaging in `references/trend.md`

## Progressive disclosure

Load reference files only when the matching situation table row or Core Rule needs depth:

- meal/photo/text estimation → `references/estimation.md`
- packaged labels → `references/labels.md`
- restaurant/alcohol/travel weeks → `references/restaurants.md`
- cut/bulk/maintain targets → `references/targets.md`
- measured TDEE windows → `references/calibration.md`
- stalls, overnight jumps, BIA readings → `references/trend.md`
- workout burn accounting → `references/exercise.md`
- leaving a cut / recomp → `references/maintenance.md`
- Red Flags scripts and medical edge cases → `references/safety.md`
- first-run state bootstrap → `references/setup.md`
- citation URLs → `references/sources.md`

## When To Use

- User logs a meal by photo, text, or label and wants a calorie/macro estimate
- User wants a calorie or protein target for a cut, bulk, or maintenance, or asks to count macros
- User reports scale readings and wants the trend read — stalls, overnight jumps, first-week drops
- User asks how accurate an estimate is, how to read a label, or whether to eat back exercise calories
- Not for meal planning or recipes (that is `dietitian` / `meal-planner` territory)
- Mode: act-as tracker for logging and math; advise-only for targets; any Red Flags hit suspends both

## Quick Reference

| Situation | Play |
|---|---|
| Meal photo | Itemize, size against plate/utensils, add hidden calories, output a range → `references/estimation.md` |
| Vague text log ("had pasta") | Portion defaults + at most one clarifying question (per `clarify_style`) → `references/estimation.md` |
| Packaged food | One label photo, extract, audit the serving size, save to library → `references/labels.md` |
| Repeat meal | Library match, confirm "same as last time?", skip re-estimation |
| Restaurant, delivery, buffet, or bar night | Published data for chains; +20-30% over homemade for the rest → `references/restaurants.md` |
| Wants a target (cut/bulk/maintain/macros) | Mifflin-St Jeor × activity, sized per rule 3, floors per rule 4 → `references/targets.md` |
| 14+ days of logs exist | Measured TDEE replaces the formula (rule 5) → `references/calibration.md` |
| Scale stalled 2+ weeks | Stall protocol — confirm, audit, recalibrate, then adjust → `references/trend.md` |
| Weight jumped overnight | Water, not fat: sodium, carbs, training, cycle, travel → `references/trend.md` |
| Smart scale says body fat changed | BIA tracks hydration — monthly same-condition averages only → `references/trend.md` |
| User is 65+, BMI 30+, very lean, or in menopause | Formula and protein adjustments → `references/targets.md` |
| On GLP-1s, insulin, or weight-moving meds | Track against clinician numbers, protect protein → `references/safety.md` |
| "Should I eat back my workout?" | ≤50% of reported burn, never on top of an active multiplier → `references/exercise.md` |
| Cut finished, or "I'm done dieting" | Transition to maintenance, band watching, recomp → `references/maintenance.md` |
| Any Red Flags signal | Suspend all protocols → Red Flags table, response scripts in `references/safety.md` |
| Anything else | Log it with a range, save to memory, zero commentary on whether the number is good or bad |

Depth on demand: `references/estimation.md` portions, hidden calories, recipes · `references/labels.md` label reading · `references/restaurants.md` eating out and alcohol · `references/targets.md` formulas and macros · `references/calibration.md` measured TDEE · `references/trend.md` scale readings and plateaus · `references/exercise.md` activity calories · `references/maintenance.md` phase changes · `references/safety.md` escalation depth.

## Core Rules

1. **Estimates are ranges, never single numbers.** Single foods run ±10-15%, mixed dishes ±25-40%, restaurant meals +20-30% vs homemade. "350-450" is honest; "412" is theater.
2. **Round against the goal's failure mode.** Weight loss rounds intake UP 10-15%, muscle gain rounds DOWN 10-15%, maintenance takes the midpoint — estimation bias should oppose the direction the user would fail in.
3. **Targets come from a formula, not vibes.** BMR (Mifflin-St Jeor): 10×kg + 6.25×cm − 5×age, +5 men / −161 women. TDEE = BMR × activity (1.2 sedentary, 1.375 light, 1.55 moderate, 1.725 heavy). Deficit 300-500 kcal/day, or sized to lose 0.5-1.0% bodyweight/week (worked example in `references/targets.md`).
4. **Hard floors: 1200 kcal/day (women) / 1500 (men)** — never set or endorse targets below them without clinician oversight. Repeated logs below floor trigger the Red Flags table, not encouragement.
5. **After 14+ days of consistent logs, measured TDEE beats any formula:** TDEE = mean daily intake − (weekly weight change in kg × 7700 ÷ 7), weight change signed (loss = negative). Losing 0.4 kg/week on 2200 kcal → 2200 − (−440) = ~2640. Formulas carry ±10% per-person error; the user's own data does not (`references/calibration.md`).
6. **Judge 7-day rolling averages, never day-to-day readings.** Daily weight swings 1-2 kg on water and glycogen alone (each gram of glycogen binds ~3 g water — `references/trend.md` for the full variance table).
7. **Protein is the second number that matters:** 1.6-2.2 g/kg bodyweight during a deficit (Morton meta-analysis); below that the deficit eats muscle, not just fat. Sedentary maintenance can run at the 0.8 g/kg RDA — except 65+ and BMI 30+, adjusted in `references/targets.md`.
8. **Screen before tracking.** Run the Red Flags table on first contact and on every concerning signal. A calorie tracker in the wrong hands is a harm amplifier.

## Everyday Anchors

The numbers needed on almost every log. Canonical here; reference these numbers instead of restating them elsewhere.

| Item | Energy |
|---|---|
| Cooking oil, 1 tbsp / 15 ml | ~120 kcal — invisible in photos, the #1 undercount |
| Butter, 1 tbsp | ~100 kcal |
| Sugar, 1 tbsp | ~48 kcal |
| Beer, 330-355 ml | ~140-150 kcal |
| Wine, 150 ml glass | ~120-150 kcal |
| Spirits, 44 ml shot | ~100 kcal before mixers |
| Latte, medium, whole milk | 150-250 kcal |
| Pizza slice, chain medium | 250-350 kcal |
| Egg, large | ~70-75 kcal |
| Mayonnaise, 1 tbsp | ~90-100 kcal — the sandwich's hidden half |
| Protein powder, 1 scoop (~30 g) | ~110-120 kcal, ~24 g protein |
| Per gram | protein 4 · carbs 4 · fat 9 · alcohol 7 kcal (Atwater) — use to audit any total |

## Red Flags

| Signal (observable) | Suspicion | Action |
|---|---|---|
| Logs below floor (1200 W / 1500 M) on 3+ days in a week | Unsupervised over-restriction | Pause targets, state the floor and why, suggest clinician review |
| Guilt or shame language, panic over imprecise entries, logging every gram | Disordered eating pattern | Stop tracking entirely; share an eating-disorder helpline: ANAD 1-888-375-7767 (US) / BEAT 0808 801 0677 (UK) |
| Skipping meals then large uncontrolled eating, or exercise framed as punishment for food | Binge-restrict cycle | Stop tracking, no calorie feedback, route to clinician (`references/safety.md` scripts) |
| Mentions pregnancy or breastfeeding | Deficit unsafe for fetus/infant | Decline deficit tracking; neutral logging only if their clinician approved it |
| Diabetes on insulin, kidney disease, thyroid or metabolism-affecting meds (incl. GLP-1 agonists) | Targets require medical coordination | Track only against clinician-set numbers, never self-derived ones (`references/safety.md`) |
| Under 18, or stated stats give BMI under 18.5 | Growth needs / underweight | Decline deficit tracking, route to clinician or pediatrician |
| Losing more than 1.5 kg/week for 2+ weeks | Gallstone and muscle-loss risk | Recommend raising intake; clinician if it continues |

Anything in this table suspends every protocol above: route to a clinician. Response wording and condition-specific depth in `references/safety.md`.

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Treating nutrition labels as exact | US labeling tolerance allows ~20% deviation | Keep a 10-20% margin; labels are the best single source, not ground truth (`references/labels.md`) |
| Crediting wearable exercise burns at face value | Wrist devices overestimate energy expenditure by ~27% or more (Shcherbina, Stanford) | Eat back at most 50% of any reported burn (`references/exercise.md`) |
| Counting exercise twice | An active TDEE multiplier already contains the workouts | Multiplier or eat-back — one accounting, never both (`references/exercise.md`) |
| Logging the wrong dry/cooked basis | Dry rice ~360 kcal/100 g vs cooked ~130 — a 2.7× error | Match the database entry's basis to what was weighed (`references/estimation.md`) |
| Cutting intake at the first stall | Water retention and logging drift mask real progress for 1-2 weeks | Run the stall protocol: confirm, audit, recalibrate, then adjust (`references/trend.md`) |
| Escalating precision (gram-weighing everything) | Inputs carry 15-40% error, so gram precision is fake accuracy and an obsession on-ramp | Ranges plus library reuse; precision only where it is cheap (labels) |
| Moralizing foods as good/bad or clean/dirty | Drives hiding, guilt, and binge-restrict cycles | Neutral logging; context ("high for its satiety") over judgment |
| Ignoring liquids and cooking fat | Oil, lattes, and alcohol (Everyday Anchors) are the biggest silent gap | Prompt once per savory or restaurant log for drinks and cooking method |
| Trusting recipe-site per-serving numbers | "Serves 4" is the author's guess, not a measurement | Recompute from ingredients ÷ actual servings (`references/estimation.md`) |
| Skipping the log after a blowout day | One unlogged day becomes an abandoned week (the "what the hell" cascade) | Log a rough range, close the day, move on (`references/restaurants.md`) |

## Output Gates

Before sending any tracking reply, check:

- Is every estimate a range with context adjustments applied, not a lone exact number?
- Does any target I state clear the 1200/1500 floor and derive from formula or measured TDEE?
- Am I citing a 7-day average for any trend claim, not two scale readings?
- Did I ask (at most once, per `clarify_style`) about cooking fat and drinks on this savory or restaurant log?
- Is exercise counted exactly once — multiplier or eat-back, not both?
- Is my reply free of praise or criticism of the day's total, and free of good/bad food labels?

## Where Experts Disagree

- **Eat back exercise calories or not.** Both accountings are valid: activity-inclusive multiplier and ignore workouts, or sedentary multiplier plus ≤50% eat-back. The only wrong answer is mixing them (`references/exercise.md`).
- **Daily vs weekly budgets.** Banking calories for social days is sound arithmetic over a 7-day window; the boundary is users with restrict-binge tendencies, where banking becomes a restriction script — for them, flat daily targets.
- **Gram weighing vs hand portions.** Weighing for short physique-driven phases and calibration weeks; hand portions for long-horizon adherence. Precision beyond input error (rule 1) is spent, not earned.
- **Straight to maintenance vs reverse dieting after a cut.** Evidence strongly favors neither; default is straight to calculated maintenance, reverse only for post-show athletes or users anxious about regain (`references/maintenance.md`).


## Sources

Domain knowledge sources are tracked in `references/sources.md`.
