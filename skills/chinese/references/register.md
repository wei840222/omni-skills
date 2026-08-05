# Register and Formality Guide

The Register Ladder in detail: choosing and maintaining formality levels.

---

## The Five Rungs

### 极正式 (Extremely Formal)

**Who/where:** 公文, 合同, official notice, court, 学术论文

**Address:** 贵方 / 各位 / no second person at all

**Particles:** None

**Characteristics:**
- Third-person or passive voice
- No personal pronouns
- Formulaic openings (兹通知如下, 鉴于)
- Rigid structure

**Example:**
> 兹通知如下：各部门应于本月二十五日前提交季度报告。

---

### 正式 (Formal)

**Who/where:** External email, a client, a professor, an older stranger

**Address:** 您

**Particles:** None, or 呢 in questions

**Characteristics:**
- Polite but personal
- 您 consistently
- Standard business phrases (感谢您的支持, 此致敬礼)

**Example:**
> 王总您好，打扰了。关于上周讨论的项目，想跟您确认一下进度。

---

### 客气 (Polite)

**Who/where:** New colleague, a peer at another company, a shop

**Address:** 你 with 请/麻烦

**Particles:** 吧, 呢

**Characteristics:**
- Friendly but respectful
- 请/麻烦 for requests
- Not overly familiar

**Example:**
> 你好，麻烦问一下，这个文件应该发给谁？

---

### 日常 (Casual)

**Who/where:** Colleagues, friends, group chats, most 小红书 copy

**Address:** 你

**Particles:** 啊, 呢, 吧, 嘛

**Characteristics:**
- Natural spoken Chinese
- Particles present
- Fragments OK

**Example:**
> 在忙吗？想问个事儿，周末有空吗？

---

### 亲近 (Intimate)

**Who/where:** Close friends, family, same-age group chat

**Address:** 你 plus nicknames

**Particles:** All of them, plus slang

**Characteristics:**
- Very casual
- Nicknames, inside jokes
- Slang acceptable

**Example:**
> 诶你看这个，笑死我了哈哈哈

---

## 你 vs 您 Decision Rules

### Use 您 when:
- Age gap (they're significantly older)
- Status gap (client, superior, official)
- First contact with stranger
- Formal context (business email, official letter)
- Showing respect deliberately

### Use 你 when:
- Same age or younger
- Peer relationship
- Established relationship (after switching from 您)
- Casual context (chat, social media)
- Group setting with mixed ages (default to 你 for group)

### The asymmetry
- **您 → 你**: A warming gesture the senior party offers. Accept it gracefully.
- **你 → 您**: Reads as cold anger or sarcasm. Avoid this shift.

### Recording the choice
When you first address someone, record their 你/您 preference in `## Recipients`:

```
| key | display_name | address_form | notes |
|-----|-------------|--------------|-------|
| @王总 | 王建国 | 您 | 客户，第一次见面用您 |
| @小李 | 李明 | 你 | 同事，同组 |
```

---

## Mid-Text Drift Prevention

Once you pick a register, maintain it throughout the text.

### Signs of drift
- Starting with 您, switching to 你 mid-paragraph
- Formal opening, casual closing
- Mixing 口语 particles in formal sections
- Using 进行 in casual chat

### Prevention
1. **Decide before writing** — check `## Recipients` or channel default
2. **Consistency check** — before delivering, scan for pronoun shifts
3. **Read aloud** — drift sounds jarring

---

## Default Registers

When nothing is known:

| Context | Default register |
|---------|-----------------|
| Writing to a person | 客气 |
| Social media copy | 日常 |
| Email | 正式 |
| Group chat | 日常 |
| Document | 正式 or 极正式 |

Override with:
- `formality` config variable
- `## Recipients` row for that person
- User's stated preference

---

## Register and Channel

Different channels imply different registers:

| Channel | Typical register |
|---------|-----------------|
| WeChat (boss) | 正式 or 客气 |
| WeChat (colleague) | 日常 |
| WeChat (friend) | 日常 or 亲近 |
| Email (external) | 正式 |
| Email (internal) | 客气 or 日常 |
| 小红书 | 日常 |
| 公众号 | 客气 or 正式 |
| 公文 | 极正式 |
| 合同 | 极正式 |

---

## Age and Register

| Age gap | Register |
|---------|----------|
| 20+ years older | 您 |
| 10-20 years older | 您 (first contact), may shift to 你 |
| Same age | 你 |
| 10+ years younger | 你 |

Exception: Formal contexts override age (a 25-year-old CEO gets 您 from older employees in meetings).

---

## Regional Differences

### Mainland
- 您 used more frequently
- Title + 姓 (王总, 李老师) common

### Taiwan
- 你 more common even in semi-formal
- 先生/女士 preferred over titles

### Hong Kong
- Mix of Mandarin and Cantonese register
- 你/您 similar to Taiwan

---

## Common Mistakes

1. **Inconsistent 你/您** — switching mid-conversation
2. **Wrong default** — using 你 with a client, 您 with a close friend
3. **Not recording the choice** — re-deciding every time
4. **Drift** — starting formal, ending casual
5. **Over-formal in chat** — 您 in a friend group
6. **Under-formal in email** — 你 with a new client
