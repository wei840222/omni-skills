# Configuration

Store declared preferences in `<state_root>/config.yaml` after State location resolution and named consent for first create.

| Variable | Type | Default | Effect |
|---|---|---|---|
| variety | en-US \| en-GB \| en-AU \| en-CA \| en-IE \| en-IN \| en-NZ | en-US | Spelling, vocabulary, punctuation, date/number format, collective-noun agreement |
| spelling_system | american \| british-ise \| oxford-ize \| canadian \| australian | follows `variety` | Overrides spelling axis alone (British vocabulary + -ize is Oxford) |
| register_default | casual \| neutral \| professional \| formal | neutral | Starting rung when the channel gives no signal |
| first_language | text | none | Selects interference row in `learners.md` and minimal pairs in `pronunciation.md` |
| oxford_comma | bool | true | Serial comma in generated lists; absence can create ambiguity, presence rarely does |
| correction_mode | silent \| inline-marked \| explained | silent | How corrections are shown; `practice.md` often uses `explained` |
| max_sentence_words | number (12–40) | 25 | Hard ceiling before split; professional/formal rungs may raise toward 35 |
| banned_words | list | none | Never emit, any register |
| voice_file | path under `<state_root>/` | none | Long-form sample of the user's English |
| review_cadence | off \| weekly \| monthly | off | Creates `## Due` rows for error journal and vocabulary review |

Preference areas (record when the user states them): conventions (title case, dash habit, list punctuation); variety detail (rejected regional words, deliberate mixes); output register (diff vs full text, emoji/profanity tolerance); restrictions (inclusive-language rules, banned jargon); learning focus; correction posture; cadence for reviews and practice sessions.
