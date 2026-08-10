# Regions — Variant and Script Guide

Chinese varies across regions. This guide covers mainland/taiwan/hongkong/singapore divergence and conversion procedures.

---

## Script Systems

### Simplified (简体) vs Traditional (繁體)

| Region | Script | Example |
|--------|--------|---------|
| Mainland China | Simplified | 国/学/发 |
| Taiwan | Traditional | 國/學/發 |
| Hong Kong | Traditional (with local variants) | 國/學/發 |
| Singapore/Malaysia | Simplified | 国/学/发 |

**Rule**: Always match the target region's script. Don't mix.

---

## The 9 One-to-Many Character Mappings

These simplified characters map to multiple traditional characters. Conversion requires context.

| Simplified | Traditional (meaning) | Context |
|------------|----------------------|---------|
| 发 | 發 (emit/send) / 髮 (hair) | 发展→發展, 头发→頭髮 |
| 干 | 幹 (do) / 乾 (dry) / 干 (interfere) | 干活→幹活, 干净→乾淨, 干涉→干涉 |
| 后 | 後 (after) / 后 (queen) | 后面→後面, 皇后→皇后 |
| 里 | 裡/裏 (inside) / 里 (distance) | 里面→裡面, 公里→公里 |
| 面 | 麵 (noodles) / 面 (face) | 面条→麵條, 脸面→臉面 |
| 松 | 鬆 (loose) / 松 (pine) | 松散→鬆散, 松树→松樹 |
| 台 | 臺/檯 (platform) / 台 (Taiwan) | 台湾→臺灣/台灣, 台灯→臺燈 |
| 系 | 係 (be) / 繫 (tie) / 系 (system) | 系统→系統, 关系→關係 |
| 脏 | 髒 (dirty) / 臟 (organ) | 脏话→髒話, 心脏→心臟 |

### Conversion Procedure

1. **Identify the simplified character** (e.g., 发)
2. **Determine meaning from context** (头发 = hair → 髮, 发展 = develop → 發)
3. **Select correct traditional form**
4. **Verify no ambiguity** — if unclear, ask user or flag for review

**Never do blind character replacement.** Always check context.

---

## Vocabulary Divergence

Same concept, different words across regions:

| Concept | Mainland | Taiwan | Hong Kong | Singapore |
|---------|----------|--------|-----------|-----------|
| Software | 软件 | 軟體 | 軟件 | 软件 |
| Hardware | 硬件 | 硬體 | 硬件 | 硬件 |
| Internet | 网络 | 網際網路 | 網絡 | 网络 |
| Computer | 电脑 | 電腦 | 電腦 | 电脑 |
| Printer | 打印机 | 印表機 | 打印機 | 打印机 |
| Mouse (computer) | 鼠标 | 滑鼠 | 滑鼠 | 鼠标 |
| Laptop | 笔记本 | 筆記型電腦 | 手提電腦 | 笔记本 |
| Program (code) | 程序 | 程式 | 程式 | 程序 |
| File | 文件 | 檔案 | 檔案 | 文件 |
| Download | 下载 | 下載 | 下載 | 下载 |
| Video | 视频 | 影片 | 視頻 | 视频 |
| Link | 链接 | 連結 | 連結 | 链接 |
| Email | 邮件 | 郵件 | 郵件 | 电邮 |
| Restaurant | 餐厅 | 餐廳 | 餐廳 | 餐厅 |
| Taxi | 出租车 | 計程車 | 的士 | 德士 |
| Subway | 地铁 | 捷運 | 地鐵 | 地铁 |
| Bus | 公交车 | 公車 | 巴士 | 巴士 |
| Potato | 土豆 | 馬鈴薯 | 薯仔 | 马铃薯 |
| Pineapple | 菠萝 | 鳳梨 | 菠蘿 | 黄梨 |
| Strawberry | 草莓 | 草莓 | 士多啤梨 | 草莓 |

### Regional Markers

| Region | Marker words |
|--------|--------------|
| Taiwan | 捷運/計程車/網路/軟體/便當/好康 |
| Hong Kong | 的士/巴士/薯仔/士多啤梨/搵/佢 |
| Singapore | 德士/巴士/组屋/乐龄/拥车证 |
| Mainland | 地铁/出租车/网络/软件/盒饭/优惠 |

---

## Grammar Differences

### Taiwan

- More conservative grammar, closer to classical Chinese
- Uses 之 more: 我的书 → 我之書 (formal)
- Prefers 有 for possession: 我有吃饭 (I have eaten) vs 我吃饭了

### Hong Kong

- Cantonese influence in casual writing
- Uses 咗/嘅/喺 in informal contexts (Cantonese particles)
- Code-switching with English common

### Singapore

- Influenced by English and Malay
- Uses lah/leh/lor particles in casual speech (Singlish)
- Formal writing follows mainland standards

### Mainland

- Standard Mandarin (普通话)
- Most simplified characters
- Official standard for international Chinese

---

## Conversion Procedure

### Step 1: Determine Target Region

Ask or infer from context:
- Who is the audience?
- What platform? (Weibo = mainland, PTT = Taiwan, HK01 = Hong Kong)
- Any regional markers in input?

### Step 2: Script Conversion

If converting simplified ↔ traditional:

1. Use the 9 one-to-many mappings carefully (check context)
2. For other characters, use standard conversion tables
3. Verify no mixed script in output

**Tools**: OpenCC (Open Chinese Convert) is the standard library.

### Step 3: Vocabulary Conversion

After script conversion, check vocabulary:

- Search for region-inappropriate terms
- Replace with local equivalents
- Example: Converting 软件→軟體 for Taiwan audience

### Step 4: Grammar Check

- Taiwan: Check for 有 + verb patterns if appropriate
- Hong Kong: Remove Cantonese particles in formal writing
- Singapore: Ensure formal writing follows standard Mandarin

### Step 5: Cultural Check

- Dates: Taiwan uses 民國紀年 (ROC calendar) — 113年 = 2024
- Names: Taiwan may use different transliterations
- Measurements: Mainland uses metric, others may mix

---

## Script vs Vocabulary Distinction

**Critical**: Script (simplified/traditional) and vocabulary (word choice) are separate layers.

### Example: Wrong Conversion

Input (mainland): 我坐地铁去餐厅
Blind conversion to traditional: 我坐地鐵去餐廳
But for Taiwan: 我坐捷運去餐廳 (vocabulary change needed)

### Example: Right Conversion

Input (mainland): 我坐地铁去餐厅
For Taiwan: 我搭捷運去餐廳 (both script and vocabulary converted)

**Rule**: Always convert both layers. Script alone is not enough.

---

## Common Mistakes

### 1. Blind Character Replacement

**Wrong**: Using regex to replace 发→發 without checking context
**Right**: Check if it's 發 (emit) or 髮 (hair)

### 2. Mixed Script

**Wrong**: 我喜歡吃apple (traditional + English)
**Right**: 我喜歡吃蘋果 (all traditional) or 我喜欢吃苹果 (all simplified)

### 3. Wrong Regional Vocabulary

**Wrong**: Writing 捷運 for mainland audience
**Right**: Use 地铁 for mainland, 捷運 for Taiwan

### 4. Ignoring Grammar Differences

**Wrong**: Converting Taiwan text to mainland style but keeping 有 + verb
**Right**: Adjust grammar patterns too

---

## Quick Reference Table

| Task | Action |
|------|--------|
| Mainland → Taiwan | Simplified→Traditional + vocabulary swap (地铁→捷運) |
| Mainland → Hong Kong | Simplified→Traditional + vocabulary swap (出租车→的士) |
| Taiwan → Mainland | Traditional→Simplified + vocabulary swap (軟體→软件) |
| Hong Kong → Mainland | Traditional→Simplified + vocabulary swap + remove Cantonese |
| Any → Singapore | Simplified (usually) + local terms (出租车→德士) |

---

## Key Principles

1. **Script and vocabulary are separate** — convert both
2. **Context determines meaning** — never blind-replace the 9 ambiguous characters
3. **Regional vocabulary matters** — 地铁 vs 捷運 vs 地鐵
4. **Grammar varies** — Taiwan uses 有 differently, Hong Kong has Cantonese influence
5. **Platform signals region** — Weibo = mainland, PTT = Taiwan
6. **When in doubt, ask** — regional conversion is error-prone without context
