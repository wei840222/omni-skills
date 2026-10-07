# Varieties

`variety` selects spelling, vocabulary, punctuation, quote-period order, date/number defaults, and collective-noun agreement. One variety end-to-end (Core Rule 5).

## Supported codes

| Code | Label | Spelling default | Notes |
|---|---|---|---|
| en-US | American | american | Default when unset |
| en-GB | British | british-ise | General UK audience; Oxford *-ize* only if `spelling_system: oxford-ize` |
| en-AU | Australian | australian | Mostly British lexis + local vocabulary |
| en-CA | Canadian | canadian | Mixed US/UK; prefer Canadian dictionary forms |
| en-IE | Irish | british-ise | British-leaning with local vocabulary |
| en-IN | Indian | british-ise | British-leaning; respect local institutional forms |
| en-NZ | New Zealand | british-ise | British-leaning with local vocabulary |

## Spelling axes (sweep in one pass)

| Axis | american | british-ise | oxford-ize | canadian | australian |
|---|---|---|---|---|---|
| -or / -our | color | colour | colour | colour (many) | colour |
| -ize / -ise | organize | organise | organize | organize (many) | organise (many) |
| -er / -re | center | centre | centre | centre | centre |
| -og / -ogue | catalog | catalogue | catalogue | catalogue | catalogue |
| -ense / -ence | defense | defence | defence | defence | defence |
| double l (travel+) | traveling | travelling | travelling | travelling | travelling |

Oxford spelling = British vocabulary + *-ize*. It is valid; it becomes an error only when mixed with American forms such as *center* or *color* in the same document.

## Lexis splits (examples)

| en-US | en-GB / many others | Domain |
|---|---|---|
| apartment | flat | housing |
| elevator | lift | buildings |
| truck | lorry | transport |
| faucet | tap | fixtures |
| cookie | biscuit | food (sense differs) |
| pants | trousers | clothing |
| soccer | football | sport (audience-sensitive) |
| vacation | holiday | time off |

## Grammar / usage splits

| Point | en-US tendency | en-GB tendency |
|---|---|---|
| past participle of get | gotten (and got) | got |
| weekend preposition | on the weekend | at the weekend |
| collective nouns | mostly singular agreement | often plural agreement (*the team are*) |
| present perfect vs past | simple past common with recent past + time | present perfect more common |
| shall | rare outside legal | more productive in offers/suggestions (formal) |

## Dates, quotes, punctuation defaults

| Point | en-US | en-GB |
|---|---|---|
| short date order | month/day/year — ambiguous forms banned in shared docs | day/month/year — prefer `2026-10-07` or `7 October 2026` for cross-border |
| quote vs period | periods/commas inside closing quotes (editorial US) | often logical punctuation outside unless part of quote |
| serial comma | usually on in book/academic US | house-dependent; many UK news styles omit |

When a document mixes varieties, pick one `variety`, state it, and sweep spelling + lexis + dates + quotes in a single pass. Deliberate mixes belong in `config.yaml` variety detail, not silent inconsistency.

Sources for contested points: `sources.md`.
