# Proofreading Chinese Text

Systematic review process for catching errors in existing Chinese text.

---

## The Three-Pass Sweep

### Pass 1: IME Homophone Errors (错别字)

IME (Input Method Engine) homophones are the most common errors.

#### Common homophone pairs

| Wrong | Right | Context |
|-------|-------|---------|
| 在见 | 再见 | Farewell |
| 以经 | 已经 | Already |
| 做后 | 最后 | Finally |
| 在次 | 再次 | Again |
| 做近 | 最近 | Recently |
| 以后 | 以后 | After |
| 在做 | 在做 vs 在座 | Context-dependent |
| 那里 | 哪里 | Where (question) vs there |
| 他/她/它 | Context | Pronoun gender/animacy |

#### Sweep procedure
1. Search for common homophones
2. Check context for each occurrence
3. Verify pronoun consistency (他/她/它)

---

### Pass 2: Register Drift

Check if the text maintains consistent register throughout.

#### Signs of register drift
- Mixing 您 and 你 for the same person
- Switching between 口语 and 书面语 mid-paragraph
- Formal vocabulary in casual sections (进行, 予以, 具备)
- Casual particles in formal sections (啊, 呢, 吧)

#### Fix
- Choose one register per section
- Ensure pronouns match throughout
- Match vocabulary to register

---

### Pass 3: Encoding and Mojibake

Check for character encoding issues.

#### Common mojibake patterns
- â€™ → ' (apostrophe)
- â€œ → " (left quote)
- â€ → — (dash)
- Â → (artifact)
- 锟斤拷 → (garbled Chinese)

#### Fix
- Ensure UTF-8 encoding
- Replace mojibake with correct characters
- Check full-width vs half-width punctuation

---

## Common 错别字 Patterns

### 的/地/得

| Pattern | Correct | Wrong |
|---------|---------|-------|
| X + 的 + 名词 | 美丽的花 | 美丽地花 |
| X + 地 + 动词 | 美丽地绽放 | 美丽的绽放 |
| 动词 + 得 + 补语 | 跑得快 | 跑的快 |

### 了 (aspect marker)

| Wrong | Right | Context |
|-------|-------|---------|
| 我吃了饭 | 我吃饭了 | Completed action (sentence-final) |
| 我吃了饭再去 | 我吃完饭再去 | Completion before another action |

### 在/再

| Wrong | Right | Context |
|-------|-------|---------|
| 我在想想 | 我再想想 | Again |
| 他再见 | 他再见 | Farewell (correct) |
| 我在家 | 我在家 | At home (correct) |

### 做/作

| Wrong | Right | Context |
|-------|-------|---------|
| 做工 | 做工 vs 作工 | Context-dependent |
| 作为 | 作为 | As/serve as (correct) |
| 做用 | 作用 | Function |

---

## Punctuation Check

### Full-width vs half-width

| Wrong | Right |
|-------|-------|
| , | ， |
| . | 。 |
| ? | ？ |
| ! | ！ |
| : | ： |
| ; | ； |

### Ellipsis and dash

| Wrong | Right |
|-------|-------|
| ... | …… (two characters, six dots) |
| -- | —— (two characters) |
| - | — (one character, for ranges) |

### Quote marks

| Variant | Correct | Wrong |
|---------|---------|-------|
| Mainland | " " ' ' | " " ' ' |
| Taiwan/HK | 「」『』 | " " ' ' |

---

## Measure Word Check

Common measure word errors:

| Wrong | Right | Noun |
|-------|-------|------|
| 一个消息 | 一条消息 | Message |
| 一个票 | 一张票 | Ticket |
| 一个电影 | 一部电影 | Movie |
| 一个电脑 | 一台电脑 | Computer |
| 一个公司 | 一家公司 | Company |
| 一个课 | 一门课 | Course |
| 一个饭 | 一顿饭 | Meal |

---

## Number and Date Check

### Numbers
- Group by 万/亿, not thousands
- 两 before measure words (两个人, not 二个人)
- 二 in ordinals (第二, not 第两)

### Dates
- Format: YYYY年MM月DD日
- No comma in dates
- 2023年8月5日, not 2023,8,5

---

## Consistency Check

### Terminology
- Same term throughout (don't switch between 用户/客户/使用者)
- Consistent abbreviation (don't mix AI and 人工智能 randomly)

### Pronouns
- 他/她/它 consistent for same referent
- 您/你 consistent per person

### Style
- 星期X vs 周X vs 礼拜X (pick one)
- 元 vs 块 (pick one)
- 号 vs 日 for dates (pick one)

---

## Read-Aloud Test

The final check: read the text aloud.

### Signs of problems
- Tongue-twisters (awkward consonant clusters)
- Unnatural rhythm (all sentences same length)
- Sentences you wouldn't say in real life
- Register mismatches (formal word in casual context)

### Fix
- Rewrite the sentence that trips you up
- Vary sentence length
- Match spoken patterns

---

## Proofreading Checklist

Before delivering reviewed text:

- [ ] IME homophones checked (在/再, 的/地/得, 做/作)
- [ ] Register consistent throughout
- [ ] No mojibake or encoding issues
- [ ] Punctuation full-width
- [ ] Ellipsis ……, dash ——
- [ ] Quote marks match variant
- [ ] Measure words correct
- [ ] Numbers grouped by 万/亿
- [ ] Dates in local format
- [ ] Terminology consistent
- [ ] Pronouns consistent
- [ ] Read aloud — no tongue-twisters
