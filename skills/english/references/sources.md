# Sources and claim audit

Material claims used by this skill. Prefer primary style authorities; Wikipedia used only as a routing summary where primary pages block automated fetch. Re-check before quoting hard institutional cutoffs.

## Agent format

| Claim | Source | URL |
|---|---|---|
| Skill directory + string metadata map | Agent Skills Specification | https://agentskills.io/specification |

## Serial comma

| Claim | Source | URL |
|---|---|---|
| Serial comma required in APA series | APA Style — Serial comma | https://apastyle.apa.org/style-grammar-guidelines/punctuation/serial-comma |
| Chicago supports serial comma practice | CMOS Shop Talk / Q&A on commas | https://www.chicagomanualofstyle.org/qanda/data/faq/topics/Commas/faq0018.html |
| Background and house-style split | Serial comma (overview) | https://en.wikipedia.org/wiki/Serial_comma |
| Some UK news styles omit | Guardian and Observer style guide (C) | https://www.theguardian.com/guardian-observer-style-guide-c |

**Operational default:** `oxford_comma: true` because absence can create ambiguity; override for a house style that forbids it.

## Spelling systems

| Claim | Source | URL |
|---|---|---|
| Oxford spelling pairs British vocabulary with -ize | Oxford spelling (overview) | https://en.wikipedia.org/wiki/Oxford_spelling |
| OED spelling information | Oxford English Dictionary — spelling | https://www.oed.com/information/understanding-entries/spelling |
| US/UK spelling axes | American and British English spelling differences | https://en.wikipedia.org/wiki/American_and_British_English_spelling_differences |

**Operational default:** general British audiences → *-ise* unless user/house asks for Oxford *-ize*.

## Plain language

| Claim | Source | URL |
|---|---|---|
| Concise, simple wording guidance | Plainlanguage.gov guidelines | https://www.plainlanguage.gov/guidelines/concise/ |
| Simple words and phrases | Plainlanguage.gov — simple words | https://www.plainlanguage.gov/guidelines/words/use-simple-words-phrases/ |

## Learner levels

| Claim | Source | URL |
|---|---|---|
| CEFR level descriptions exist as shared reference | Council of Europe CEFR resources | https://www.coe.int/en/web/common-european-framework-reference-languages/level-descriptions |
| CEFR overview | CEFR (overview) | https://en.wikipedia.org/wiki/Common_European_Framework_of_Reference_for_Languages |
| CEFR companion volume (PDF) | Council of Europe | https://rm.coe.int/common-european-framework-of-reference-for-languages-learning-teaching/16809ea0d4 |

**Qualification:** CEFR bands in `practice.md` are planning vocabulary, not an automated score. Claims about post-B2 returns are goal-dependent (collocation/precision often dominate; accent goals vary).

## Pronunciation / intelligibility

| Claim | Source | URL |
|---|---|---|
| Intelligibility-oriented priorities are the operational overlap of accent-reduction and ELF debates | Skill position + CEFR communication aims | (see CEFR links above; pair with user goals) |

**Qualification:** Do not claim a single orthodoxy for "reduce accent" vs "keep identity"; prioritize stress/rhythm for comprehension.

## British understatement

| Claim | Source | URL |
|---|---|---|
| Indirect professional disagreement is culturally variable | Operational caution in `business.md` | n/a — pragmatic tendency, not a universal decoder |

**Qualification:** Tables are tendencies; always read relationship and prior turns.

## Slang freshness

| Claim | Source | URL |
|---|---|---|
| Slang ages; dated slang is high-risk in careful prose | Operational policy in `idioms.md` | n/a — no universal 3–5 year expiry law retained |

**Qualification:** Original absolute "dates in ~3–5 years" removed; use freshness tags and plain wording when unsure.

## Contraction and sentence-length thresholds

| Claim | Source | URL |
|---|---|---|
| Operational cadence thresholds (contraction density, 14–20 word mean at neutral) | Skill house rules for anti-AI-cadence editing | n/a — editorial heuristics aligned with plain-language pressure, not a single laboratory law |

**Qualification:** Treat Core Rules 2–3 as editable house thresholds via `max_sentence_words` and register bands, not as universal linguistic constants.

## US government style (optional typography)

| Claim | Source | URL |
|---|---|---|
| GPO Style Manual (PDF) | U.S. Government Publishing Office | https://www.govinfo.gov/content/pkg/GPO-STYLEMANUAL-2016/pdf/GPO-STYLEMANUAL-2016.pdf |
