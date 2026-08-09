---
name: chinese
description: Write native-quality Mandarin Chinese for any context — WeChat messages, business emails, social media posts, formal documents, or casual chat. Use when composing Chinese text that must sound authentic (not translated or AI-generated), when choosing between 你/您, simplified/traditional, or mainland/Taiwan vocabulary, when fixing grammar (的/地/得, measure words, particles), or when calibrating register, slang, and punctuation. Not for translating existing source text (use `translate`), Traditional-only output (use `traditional-chinese`), or travel planning (use `china`).
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"🇨🇳"}'
  related-skills: '{"china":"Travelling in the country these texts are read in.","japanese":"The same problem in the neighbouring language.","traditional-chinese":"Traditional-only writing for Taiwan and Hong Kong readers.","translate":"Bound to an existing source text in another language.","writing":"The craft of prose itself, once the language question is settled."}'
---

## State location

Chinese state may exist in `<workspace>/chinese/`, `<workspace>/memory/chinese/`, or `~/chinese/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise inspect all three candidate directories in this order:
   `<workspace>/chinese/`, `<workspace>/memory/chinese/`, `~/chinese/`.
3. If two or three candidate directories exist, tell the user that multiple state copies were detected. Use only the highest-precedence existing directory; do not merge, cross-read, or cross-write the others.
4. If none exists and the user asks to save a preference, create `<workspace>/chinese/` as `<state_root>`.

Use the selected `<state_root>` for every state operation in this skill.

**Optional preferences.** Read `<state_root>/config.yaml` and `<state_root>/memory.md` only after the resolver selects an existing state root, or after the user explicitly asks to save a preference. Keep all state in those two files; the skill neither creates nor edits host-shared contact or project records. Use `references/memory-template.md` only when saving an approved preference. State is local plain text: store language decisions and style preferences, never credentials, account identifiers, or content that belongs in another system.

Model-written Chinese is almost always grammatical and almost always wrong at the register: one notch too formal, particle-free, and structured like an English essay wearing Chinese words. The job is to put back what a native adds without thinking — the 语气词, the fragment, the right 量词, the 全角 comma — and to take out what English pushed in: 进行 + verb, 一个 as an article, a 30-character attributive stacked before 的. Produce the Chinese first; explain in English only when asked. Work from defaults immediately: start writing in the assumed variant and register, adjusting only when the user states a preference. The one exception to silence is script — while `variant` is unset, state which variant and script you are writing in before writing it (Rule 2). That is a statement, not a question. Precedence for any value: `config.yaml` → `<workspace>/profile.yaml` (shared universals: locale, timezone) → the Configuration table default.

## Before Writing — Decision Sequence

Resolve these in order before producing any Chinese text:

1. **Channel** → What platform or context? (WeChat / email / 小红书 / document / …) → Sets default register and emoji density.
2. **Audience** → Who reads this? → Check `## Recipients` for existing address form; if new, pick from the Register Ladder.
3. **Variant & script** → Mainland simplified? Taiwan traditional? → When the request and state provide no preference, label and write Mainland Simplified Chinese; otherwise state and apply the selected variant before writing (Rule 2). Load `references/regions.md` for vocabulary divergence.
4. **Register rung** → Which of the five rungs? → Lock it for the entire text; mid-text drift is the most visible failure.
5. **Slang appetite** → How much internet language? → From config or default `light`. Load `references/slang.md` when using any term.
6. **Write** → Produce the Chinese.
7. **Output Gates** → Run the checklist below before delivering.

### Fact boundary

Keep every clause grounded in the request. When a name, date, price, result, personal reaction, work arrangement, or comparative claim is missing, use a visible `[placeholder]` or omit it. This applies to titles, hooks, softeners, calls to action, and conventional business boilerplate as well as the body. For an unspecified first-person experience, produce a neutral placeholder draft: each scene-setting, reaction, recommendation, and promise must come from the user or remain a placeholder.

## When To Use

- Writing original Chinese: messages, emails, posts, captions, documents, scripts, marketing copy, product names
- Repairing Chinese that reads wrong — too formal, textbook, translated, or recognisably AI — including text the user did not write
- Deciding the frame before the words: 你 or 您, 口语 or 书面语, simplified or traditional, mainland or Taiwan or Hong Kong vocabulary, how much slang
- Mechanics a non-native gets wrong: 的/地/得, 了, 把/被, measure words, full-width punctuation, 万/亿 numbers, dates, names, titles, addresses
- Pragmatics: refusing without saying no, apologising at the right weight, accepting a compliment, asking a favour, giving face in a group chat
- Act-as by default — this skill writes the Chinese. It advises instead when the user is learning and asks why; then the Chinese still comes first and the explanation follows it
- Not for translating a source text that already exists (`translate` — that job is bound to a source and this one is not), Traditional-only output (`traditional-chinese`), or travelling in China (`china`)

## Quick Reference

| Situation | Play | Depth |
|---|---|---|
| "Make this sound less like AI wrote it" | Run the tell sweep before touching style: openers, 四字格 parallelism, uniform paragraphs, zero particles | `references/ai-tells.md` |
| WeChat message, group chat, reply to a boss | Drop the final 。, match 哈哈哈 length, open directly with the message content | `references/chat.md` |
| Work email, 通知, 汇报, addressing a title | 尊敬的X总 → 结论先行 → 此致 敬礼; 王总 not 王总经理 | `references/business.md` |
| 小红书, 公众号, 微博, 抖音, B站, 知乎 post | Each platform is a different register with a different title mechanic | `references/social-media.md` |
| Simplified or traditional; mainland, Taiwan, HK, Singapore | Vocabulary diverges more than the glyphs do (Rule 2) | `references/regions.md` |
| Is this slang still alive? Which slang for this reader? | Date the term, then match the audience's age band (Rule 9) | `references/slang.md` |
| 的/地/得, 了, 把, 被, 是…的, word order, 量词 | The rule, the test, and the sentence rewritten | `references/grammar.md` |
| 全角 vs 半角, 《》「」"", ……, ——, spacing around Latin | Full-width always; the half-width comma is the loudest tell (Rule 8) | `references/punctuation.md` |
| Numbers, money, dates, phone, address, a person's name or title | Group by four; 两 before a measure word; big-to-small addresses | `references/numbers-and-names.md` |
| A 成语 or 俗语 — is it right, is it too much? | Frequency ceiling plus the twelve most-misused 成语 | `references/idioms.md` |
| 请假条, 辞职信, 简历, 邀请函, 感谢信, 合同 clause, 公文 | Fixed skeletons; 请示 and 报告 are different documents | `references/documents.md` |
| 论文, 摘要, 关键词, 术语, 参考文献 | 本文 not 我; 200-300 字 abstract; GB/T 7714 citations | `references/academic.md` |
| Something to be said aloud: call, voice note, toast, presentation | Spoken Chinese is shorter, more particled, and repeats the topic | `references/speaking.md` |
| Refusing, apologising, thanking, complimenting, asking a favour | The refusal ladder; 不好意思 vs 对不起 vs 抱歉 | `references/etiquette.md` |
| Checking someone else's Chinese, or hunting 错别字 and mojibake | IME homophone sweep, then register drift, then encoding | `references/proofreading.md` |
| Which 你/您 and how casual, for this person or this channel | The Register Ladder below; save the decision only if the user asks | `references/register.md` |
| Anything else in Chinese | Write it at the register the channel implies, then state the two assumptions you made — audience and formality — so the user can correct one | — |

Coverage map: `references/register.md` formality and address form · `references/chat.md` WeChat and messaging · `references/business.md` workplace and email · `references/social-media.md` platform voices · `references/documents.md` formal paperwork · `references/academic.md` research and technical writing · `references/speaking.md` spoken scripts · `references/etiquette.md` politeness and face · `references/grammar.md` the mechanics that break · `references/punctuation.md` typography · `references/numbers-and-names.md` numbers, dates, names, addresses · `references/idioms.md` 成语 and 俗语 · `references/slang.md` internet language and its shelf life · `references/regions.md` variants and scripts · `references/ai-tells.md` machine fingerprints · `references/proofreading.md` reviewing existing Chinese.

## Core Rules

1. **Register comes from the relationship and the channel, not the topic alone.** Decide before the first character; the Register Ladder below is the table. 您 is a prudent default for a customer, official, or first contact where the relationship is unknown; 你 fits established peers and most colleagues. Keep the established form unless the relationship changes. Address a group as 大家 or 各位 rather than 您们. Save a recipient-specific choice only after the user asks to retain it.
2. **Variant and script are one decision, taken before writing and stated out loud when unset.** A glyph converter is not a variant converter: it produces 繁體字 carrying mainland vocabulary, which a Taiwanese reader spots in one line (視頻 for 影片, 軟件 for 軟體). It also guesses wrong on the one-to-many mappings, where one simplified character maps to several traditional ones — 发 → 發/髮, 干 → 幹/乾/干, 后 → 後/后, 里 → 裡/里, 面 → 麵/面, 只 → 隻/只, 云 → 雲/云, 松 → 鬆/松, 台 → 臺/檯/颱/台. Convert the vocabulary and re-read those characters by hand (`references/regions.md`).
3. **Numbers group by four, not by three.** 万 = 10⁴, 亿 = 10⁸. Convert by dividing: `value ÷ 10,000` → 万, `value ÷ 100,000,000` → 亿. So 1,200,000 → 120万 and 3,500,000,000 → 35亿; "3.5 billion" written as 三十五亿 is right and as 3.5十亿 is not Chinese. A seven-digit comma-grouped figure in Chinese prose is a translation artefact. Before a measure word the number two is 两 (两个人, 两天), while 二 stays in ordinals and compounds (第二, 十二, 二十). Full table in `references/numbers-and-names.md`.
4. **Use particles when the register calls for them, not as a quota.** In casual text, place 啊/呀 to soften, 呢 to hand back the turn, 吧 to propose or hedge, 嘛 to mark the obvious, 啦 to close, 哦/噢 to acknowledge, and 呗 to shrug. Omit them from formal documents unless the document's genre calls for one (`references/register.md`).
5. **Cut the attributive at about twelve characters before 的.** Chinese stacks every modifier ahead of the noun, so an English relative clause moved across in place forces the reader to hold the whole modifier in memory before learning what it modifies. Working threshold: past ~12 characters, break it into its own clause and let the noun arrive first — 我昨天在楼下咖啡店遇到的那个人 becomes 那个人，我昨天在楼下咖啡店遇到的. 余光中's essays on 欧化中文 are the standard treatment; this is their operational form, and the full table of Europeanised patterns with their rewrites is in `references/grammar.md`.
6. **Delete 进行/作出/给予/予以 plus a noun and put the verb back.** 进行讨论 → 讨论, 作出决定 → 决定, 给予支持 → 支持, 予以考虑 → 考虑. Each deletion removes two characters and one degree of bureaucratic distance. Same family: 一个 used as an English indefinite article, 们 stacked on a noun already marked plural (三个学生们), 性/化 suffixes on words that do not need them (可行性方案 → 可行的方案), and 被 on anything that is not adverse (被讨论 is un-Chinese; 被表扬 has been naturalised and is fine).
7. **的/地/得 are decided by what follows them, not by how they sound.** Formula: `X的 + 名词` · `X地 + 动词` · `动词/形容词得 + 补语`. Worked: 高兴**的**孩子 (noun follows) · 高兴**地**说 (verb follows) · 说**得**很高兴 (complement follows). This is the single most common 错别字 in native writing too, so an error here does not read as foreign — it reads as careless, which for a 公文 or a resume is worse (`references/grammar.md`).
8. **Use the target variant's punctuation and the channel's established style.** In normal Chinese prose, use full-width ，。、；：？！; use 、 for list items rather than clauses; use …… for an ellipsis and —— for a dash. Use 《》 for titles when the genre calls for book-title marks. Mainland writing commonly uses “”, while Taiwan and Hong Kong commonly use 「」; preserve the publication's house style when it differs. Apply `latin_spacing` consistently (`references/punctuation.md`).
9. **Treat slang as current only with audience evidence.** Match `slang_appetite`, region, platform, and the reader's own language. When a term's currency or meaning is uncertain, use plain language rather than guessing; `references/slang.md` gives a verification procedure.

## AI Tells In Chinese

The fingerprints that make a Chinese reader screenshot a text as 机翻 or AI. Sweep for these before style: they are structural, so no amount of vocabulary polish removes them.

| Tell | Why it reads machine | Do instead |
|---|---|---|
| 首先…其次…再次…最后 | Essay scaffolding pasted into a message nobody asked to be structured | Say the thing; if order matters, 先…然后… or nothing at all |
| 总之 / 综上所述 / 总的来说 | A summary of four sentences the reader just read | Delete. If a conclusion is needed, put it first (`references/business.md`) |
| 值得注意的是 / 需要注意的是 | Textbook hedge with no speaker behind it | 注意 + the thing, or just the thing |
| 随着…的发展 / 在…方面 / 在…的情况下 | Translated English prepositional frames | Rebuild as topic-comment: put the topic first, bare |
| 希望以上内容对您有所帮助 | Customer-service boilerplate on a personal message | Nothing, or 有问题再问我 |
| Every paragraph the same length, every sentence balanced | Natural Chinese varies wildly: a three-character line next to a forty-character one | Break the rhythm on purpose; leave one fragment |
| 四字格 stacked three or more in a row | 精益求精、锐意进取、开拓创新 is 公文 filler, not writing | One at most, and only where it earns its place (`references/idioms.md`) |
| Zero 语气词 in a casual message (Rule 4) | The single most reliable signal | Add where the feeling is, not everywhere |
| Bolded key terms and emoji headings in a chat message | Nobody formats a WeChat message | Plain text; line breaks are the only formatting chat has |
| 我们可以看到 / 让我们一起 | Lecture voice from a first-person plural nobody appointed | Drop the frame, keep the observation |
| Perfect 。 at the end of every chat line | Chat drops the final period; keeping it reads as cold or final (`references/chat.md`) | End on the last character, or a particle |
| An English idiom carried across literally | 一石二鸟 exists; "touch base" and "circle back" have no Chinese and produce nonsense | Name the action: 再对一下 |
| Anything else that feels off but parses | Read it aloud; the sentence a native would not say aloud is the one to rewrite | `references/proofreading.md` |

## The Register Ladder

Five rungs. Pick by the relationship, then keep it for the whole text — mid-text drift is more visible than starting one rung wrong.

| Rung | Who / where | Address | Particles | Sample opener |
|---|---|---|---|---|
| 极正式 | 公文, 合同, official notice, court, 学术论文 | 贵方 / 各位 / no second person at all | none | 兹通知如下： |
| 正式 | External email, a client, a professor, an older stranger | 您 | none, or 呢 in a question | 王总您好，打扰了。 |
| 客气 | New colleague, a peer at another company, a shop | 你 with 请/麻烦 | 吧, 呢 | 你好，麻烦问一下 |
| 日常 | Colleagues, friends, group chats, most 小红书 copy | 你 | 啊, 呢, 吧, 嘛 | 在忙吗？想问个事儿 |
| 亲近 | Close friends, family, same-age group chat | 你 plus nicknames | all of them, plus slang | 诶你看这个 |

Defaults when nothing is known: 客气 in writing to a person, 日常 on social copy, 正式 in email. `formality` overrides; a stated preference for one person overrides both for the current work and may be saved in `## Recipients` on the user's request.

## Word Choice: Safe → Native

The model reaches for the dictionary word. A native reaches for the specific one. Left column is not wrong — it is *flat*, which is what reads as machine.

| Flat | Native, casual | Native, formal | Note |
|---|---|---|---|
| 很好 | 太好了 / 绝了 / 牛 | 非常好 / 十分理想 | 绝了 and 牛 carry age signal (`references/slang.md`) |
| 不好 | 太差了 / 拉垮 / 坑 | 不理想 / 有待改进 | 坑 means it wasted your money or time specifically |
| 很多 | 超多 / 一堆 / 一大把 | 大量 / 众多 | 一堆 implies untidy volume |
| 非常 | 超 / 巨 / 特别 / 贼 (northern) | 十分 / 极为 | 贼 marks the writer as northern |
| 我认为 | 我觉得 / 我感觉 | 本文认为 / 笔者认为 | 我认为 in a 论文 is a register error (`references/academic.md`) |
| 是的 | 对 / 嗯 / 是啊 | 是的 | Bare 是的 in chat reads clipped |
| 谢谢你 | 谢啦 / 多谢 / 麻烦你了 | 感谢您的支持 | 麻烦你了 thanks for effort, not for a gift |
| 对不起 | 不好意思 | 抱歉 / 深表歉意 | Weight ladder in `references/etiquette.md` |
| 一个人 | 有个人 | 一位 + role | 位 is the polite measure word for people |
| 个 (any noun) | the specific 量词 | the specific 量词 | 一条消息, 一张票, 一部电影, 一台电脑, 一家公司, 一门课, 一顿饭 |
| 进行讨论 | 聊聊 / 说一下 | 讨论 | Rule 6 |
| 现在 | 这会儿 / 眼下 | 目前 / 当前 | 这会儿 is spoken and northern-leaning |
| 因为…所以… | just the two clauses | 由于…因此… | Chinese does not need both halves; keeping both is textbook |
| 我不同意 | 我觉得不太行 / 这个可能有点难 | 恐怕难以认同 | Direct disagreement is a register decision, not a default (`references/etiquette.md`) |

## Output Gates

Before delivering any Chinese text, run each check. If any fails, fix before delivery.

**GATE A — Variant & Script (Rule 2)**
- [ ] Variant and script settled and consistent end to end
- [ ] No mixed-variant vocabulary
- [ ] Every one-to-many character checked (发→發/髮, 干→幹/乾/干, etc.)

**GATE B — Register (Rule 1)**
- [ ] One register for the whole text
- [ ] Address form matches `## Recipients` row if one exists
- [ ] Address form unchanged from previous messages to that person

**GATE C — Punctuation & Typography (Rule 8)**
- [ ] Punctuation full-width throughout
- [ ] Ellipsis ……, dash ——, titles in 《》
- [ ] Quotes matching the variant
- [ ] `latin_spacing` applied uniformly

**GATE D — Numbers & Names (Rule 3)**
- [ ] Numbers grouped by 万/亿
- [ ] 两 before measure words
- [ ] Dates and money in the local shape

**GATE E — AI-Tell Sweep**
- [ ] No opener scaffolding (首先/其次/最後)
- [ ] No 值得注意的是 / 需要注意的是
- [ ] Paragraph lengths vary (not uniform)
- [ ] No stacked 四字格 (≥3 in a row)
- [ ] Casual text has 语气词 (not zero)

**GATE F — Grammar (Rules 6, 7)**
- [ ] 的/地/得 checked at every occurrence
- [ ] Every 个 that should be a specific 量词 replaced

**GATE G — Slang & Idioms (Rule 9)**
- [ ] Every slang term datable and within `slang_appetite`
- [ ] Every 成语 checked for actual meaning, not parts

**GATE H — Final Read**
- [ ] Read once aloud in the target register: is there a sentence a native would not say out loud?

**GATE I — Persist**
- [ ] If the user asked to retain a durable preference, record it using `references/memory-template.md`; otherwise complete the writing task without state changes.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; save a preference in `<state_root>/config.yaml` only when the user asks to retain it.

| Variable | Type | Default | Effect |
|---|---|---|---|
| variant | mainland \| taiwan \| hongkong \| singapore | mainland | Vocabulary set, slang source, punctuation defaults and every example in `references/regions.md`; while unset, name the assumed variant before writing (Rule 2) |
| script | simplified \| traditional \| from-variant | from-variant | Overrides the script the variant implies, for the case of simplified text for a Taiwanese reader or the reverse |
| formality | casual \| neutral \| formal \| auto | auto | Default rung on the Register Ladder when the channel does not settle it; `auto` reads it from the channel |
| address_form | 你 \| 您 \| auto | auto | Second person used when no `## Recipients` row exists; a row for a person always wins (Rule 1) |
| slang_appetite | none \| light \| current \| heavy | light | How much internet language enters output; `none` for official channels or a 50+ audience, `heavy` only when the user has shown they write that way (`references/slang.md`) |
| pinyin_gloss | none \| new-words \| all | none | Whether output carries pinyin and an English gloss — set to `new-words` when the user is learning, `none` when they are native |
| default_channel | wechat \| xiaohongshu \| weibo \| gongzhonghao \| douyin \| zhihu \| email \| document \| none | none | Channel assumed when a request does not name one; picks the style box and the platform conventions in `references/social-media.md` |
| latin_spacing | bool | true | Whether a half-width space separates Han from Latin letters and digits; applied to every occurrence or none (Rule 8) |
| crude_ok | bool | false | Whether 卧槽-tier and 牛逼-tier words may appear at all |
| emoji_density | none \| sparse \| native \| heavy | sparse | Emoji and 表情包 per paragraph in chat and social copy; `native` matches the platform norm, which on 小红书 is far higher than on WeChat |

Preference areas — customizable dimensions; apply a stated preference to the current work and save it only when the user asks:

- **Voice** — how blunt, how warm, sentence length, whether fragments are welcome, self-reference (我 / 本人 / 笔者 / 小编), and signature sign-offs — affects every piece and may be saved as an approved preference
- **Conventions** — quote-mark style, whether 星期六 or 周六 or 礼拜六, 元 or 块, 号 or 日, half-width digits in Chinese text, paragraph indent (首行缩进两字) or blank-line separation — affects `references/punctuation.md` and `references/numbers-and-names.md`
- **Platform** — which channels the user writes on, their audience age band and region, account type and its limits, whether a piece is read on a phone — affects `references/social-media.md` and `emoji_density`
- **Relationships** — a standing address form and register for a named person or group; save it in `## Recipients` only on the user's request
- **Risk posture** — appetite for crude words, sensitive topics, direct disagreement, and humour that could be misread by a superior — affects `references/etiquette.md`
- **Cadence** — slang re-calibration, native review, glossary consolidation, and review after a platform changes its rules; perform these only when the user requests them
- **Output register** — Chinese only, Chinese plus back-translation, Chinese plus pinyin, whether alternatives are offered by default, how much of the reasoning to show — affects the shape of every answer

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| 呵呵 as friendly laughter | On the mainland it has meant dismissal or contempt for over a decade; sending it to a colleague reads as an insult | 哈哈 / 哈哈哈, matched in length to theirs (`references/chat.md`) |
| The 🙂 emoji, or 微笑 from the WeChat set | Read as passive-aggressive by most users under about 40; the older generation still means it warmly, which is exactly why it lands badly | 😄, 😂, or a 表情包 (`references/chat.md`) |
| Opening a message with 在吗 | Puts the reader on the hook before they know the cost; widely resented | Ask the thing in the first message, with the context |
| A 。 at the end of every chat line | Chat punctuation is minimal; a final period reads as cold, angry, or conversation-ending | End on the last character or a particle; keep 。 for paragraphs |
| Machine-converting simplified to traditional | Vocabulary stays mainland and the one-to-many characters break: the converter emits 頭發 for 头发 and leaves 干杯 as 干杯, where 頭髮 and 乾杯 are the right forms | Convert vocabulary too, then re-read the nine characters in Rule 2 (`references/regions.md`) |
| 二个, 二点钟 | Before a measure word the number is 两 | 两个, 两点钟 (Rule 3) |
| Overusing 您 with a peer | Reads as sarcasm or as putting distance in on purpose | 你 for peers; 您 only up the ladder or on first contact (Rule 1) |
| 亲 as a friendly opener | It is Taobao seller voice; outside e-commerce it reads as a sales script | The person's name, or nothing |
| Adding 哥/姐 to a name without checking | 哥 attached to some given names collides with a product or a meme — 伟哥 is the brand name of Viagra | Use 姓 + 哥/姐 (王哥), or the title (`references/numbers-and-names.md`) |
| Stacking 成语 to sound educated | Three in a paragraph reads as 公文 filler or as a student showing off | One per paragraph at most, and only where a plain phrase would be longer (`references/idioms.md`) |
| Reaching for slang to sound young | A dead meme dates the writer more precisely than plain language ever could | Date the term first (Rule 9) |
| Half-width ,.?! inside Chinese text | The most visible non-native mark, and it survives every style edit | Full-width throughout (Rule 8) |
| 谢谢你的来信 / 期待您的回复 as email frames | Direct calques of English business letters; Chinese email has its own skeleton | 您好 → the point → 此致 敬礼 or 顺颂商祺 (`references/business.md`) |
| 加油 as the answer to any difficulty | Fine for exams and matches, hollow after bad news | Name the specific thing: 有事随时说 / 需要我做什么 |
| Writing ... instead of …… | Three ASCII dots are a Latin ellipsis; Chinese uses two ellipsis characters | …… (Rule 8) |
| Using 、 to join two clauses | 、 lists items inside one clause and nothing else | ，between clauses, 、inside a list |
| A term, name or register decision that should be reused | It may be re-decided differently in later work | Ask whether to save it, then record it in `<state_root>/memory.md` or `<state_root>/config.yaml` only with approval (`references/memory-template.md`) |

## Where Experts Disagree

- **儿化 in writing.** Northern writers put it in (这儿, 一会儿, 玩儿) and hear its absence as stiff; southern and Taiwanese readers see it as Beijing affectation. The decidable version is the audience, not taste: write it when the reader is northern or the voice is deliberately Beijing, drop it in anything national or formal.
- **Han-Latin spacing.** No national standard requires a space between Chinese characters and Latin words or digits; the dominant web typography convention adds one. Publishers split. Pick with `latin_spacing` and be uniform — mixed spacing looks like a merge conflict, which is worse than either choice.
- **Loanwords and English acronyms.** Mainland technical and office writing carries English acronyms untranslated (PPT, KPI, OKR, APP); Taiwanese writing translates more of them (簡報); purists in both markets object to all of it. Frontier: acronyms the audience uses at work stay in English, consumer-facing copy translates them.
- **欧化中文.** 余光中 and 思果 treat 进行 + noun, long pre-nominal attributives and 被 overuse as damage to be reversed; descriptive linguists point out that a century of translation has naturalised much of it and that some structures now carry meaning nothing else does. Both agree the stacked attributive is unreadable; the argument is over the rest. Rules 5 and 6 take the prescriptive side because the failure mode here is machine-flavoured text, and that is precisely what the prescriptive rules delete.
- **TA for gender-neutral third person.** Written 他 covers mixed and unknown gender by convention; TA (Latin letters) is common online and in HR writing, and reads as internet register or as awkward in print. Brand decision per channel, never a default the writer picks mid-document.
