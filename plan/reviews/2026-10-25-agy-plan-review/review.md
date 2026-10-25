# Antigravity 計畫審查與主代理採納紀錄

本輪僅審查原始計畫與未來 AI 標註流程；未執行 M0–M4，也未建立或複核 180 題案例。

## 呼叫與證據界線

- 使用已安裝的 `antigravity-cli` skill，實際呼叫一次 `agy --print`；未指定模型、未自動 retry／續問。
- CLI 回傳狀態：SUCCESS；回報 turns：1；耗時：20.411647582 秒。
- CLI 回報 usage：`{"input_tokens": 14609, "output_tokens": 1664, "thinking_tokens": 0, "cache_read_tokens": 0, "total_tokens": 16273}`。這不是 Jev 用量或已核實帳單；回傳未提供模型名稱或實付金額。
- 完整請求、回應與輸入 SHA-256 分別保存在本目錄 `request.txt`、`response.json`、`manifest.json`。
- 審查以附加計畫為唯一證據，禁止工具／檔案／網路存取。這是派工邊界，不是對工具禁用的 runtime 強制保證；回傳沒有完整工具事件供獨立驗證。
- CLI stderr 說明 `--disable-slash-commands` 下 `--mode plan` 不生效，因此不把此旗標當作唯讀模式證明。未使用 `--dangerously-skip-permissions`；日後同類純文字審查可省略無效 mode 組合。
- skill 所載 `agy version` 在本機不支援；以本機 `agy --help` 核對此次實際使用旗標，未更新 CLI 或設定。

## 主代理採納與保留

1. 採納獨立盲審、silver labels、分歧／uncertain 保留、標註覆蓋率揭露，以及在變體輸出前凍結標籤與評分的要求。
2. 採納 M0 probe 不接觸 holdout、M4 才執行其檢索／Decision、各 provider 分帳與外送前停止契約、12 任務的事前斷言與 turn 上限。這些目前是待實作驗收條件，不代表預算已核准或控制器已實作。
3. 不採納全面禁止 dev／holdout 共用固定語料 embedding 的要求。與答案無關、版本固定的公開技能向量可重用；有關 query／context／payload／政策的 cache 身分及答案洩漏才需分別核對。
4. 修正 reviewer 的覆蓋率命名：resolved／total 才是標註覆蓋率；resolved-correct／total 不能冒充此指標。全體二元成功率可另報含 uncertain 的上下界，主要品質指標須明列分母與限制。
5. 保留 reviewer 原始 CLARIFY，不改寫成 ACCEPT。主代理已將合理要求寫回唯一計畫；未對修訂版重送另一付費請求，亦不把計畫審查視為實驗啟動授權。

## Antigravity 原始回覆

# 獨立計畫審查報告：技能庫品質與 skill-harness 選取改善計畫

## Result
**CLARIFY（附條件修正後可進行 M0）**

本計畫結構嚴謹，在隔離原則、不可逆成本控管與漸進里程碑設計上具備良好工程標準。然而，計畫在「AI 獨立標籤審查機制」、「不確定案例（Uncertain Cases）計分隔離性」、「付費 API 請求與金額防護上限（Circuit Breakers）」以及「保留集（Holdout）資訊外洩防護」上存在關鍵缺口，需在進入 M0 執行前明確補充補正。

---

## Evidence

1. **標籤審查與真值假設缺乏無人化防護**：
   - 引用〈M1 評測契約草案：資料與標籤〉，計畫提及「180 題人工核對 pilot」。依據指引，此 180 題目前並不存在，且若引入 AI 輔助審查，產出的共識僅為「白銀標籤（Silver Labels）」，計畫未定義 AI 獨立盲審流程（Blind Review Protocol）。
   - 計畫指出「無法裁決的案例保留為 uncertain，不放進主要決策分數」。若僅將難題移出分母，會導致「不確定性覆蓋率（Uncertainty Coverage）」被隱蔽，產生人為拉高準確率的統計偏差。
2. **評測外洩與資料隔離界線**：
   - 引用〈M1 評測契約草案：資料與標籤〉，提及依技能家族與近義群組劃分 dev 120／holdout 60。但未明確規定在多輪意圖擴展（Intent Expansion）、QMD 檢索與 Decision 測試中，Holdout 案例是否能被任何前期 probe 觀察或快取污染。
3. **付費調用與無人執行預算未落實實體熔斷**：
   - 引用〈M0 詳細步驟：3〉，僅提及「模型探測建議上限……最多 30 個實驗端可觀察的新增外送模型請求……請求數上限不是保證金額上限」。
   - 目前系統未實作任何硬性金額或 runtime cap；後續 360 個 Decision batch 與潛在 360 個 QMD intent expansion 若處於無人值守執行，欠缺非同步終止與停損機制。
4. **離線重播保真度（Offline Replay Fidelity）邊界**：
   - 引用〈已知基線與證據界線〉及〈M0 詳細步驟：3〉，當前 harness 的三集合檢索、name/experience/graph 候選與 host Decision API 在離線沙盒中難以保證 100% 同構。計畫雖提出 controlled fixture 標記，但對差異造成的決策漂移缺乏量化校準程序。

---

## Changes (None)

*(本審查為純讀取審查，未建立、編輯或變更任何檔案與環境產物)*

---

## Decisions

為確保後續實驗可信度與成本可控，提出以下具體決策與補正要求：

### 1. 增訂「Antigravity 無人化 AI 標籤獨立盲審協議 (AI-Label-Review Protocol)」
在 M1 建置 180 題 pilot 時，若採用 Antigravity (agy) 進行無人標籤審查，必須嚴格執行以下流程：
1. **雙盲輸入（Blind Pass）**：獨立審查代理人（agy）在初次評估時，**只能接觸公開任務／對話輸入（User Message & Conversation Context）與公開技能庫定義（SKILL.md 元資料與正文）**，**嚴格遮蔽**第一標註者（Primary Annotator）的標籤、預期結果與推論理由。
2. **獨立產出與比對（Disagreement Recording）**：agy 依語義獨立產出建議的 `acceptable_sets` 與判斷依據。完成後才與第一標註者交叉對比，系統自動記錄分歧項目（Disagreements）。
3. **銀標識標與不確定案例保留（Silver Labels & Uncertainty Tracking）**：
   - 雙方一致者僅標記為「AI 共識白銀標籤（Consensus Silver Labels）」，不可宣稱為人類黃金真值（Human Gold）。
   - 雙方分歧或模型標註信心不足之案例，**強制維持 `uncertain` 標記**。
   - **禁止直接從分母剔除難題**：評測報告必須強制同時公布：
     $$\text{Full-Set Coverage} = \frac{\text{Resolved Correct}}{\text{Total (including uncertain)}}$$
     以及標註爭議比例（Uncertainty Coverage %）。評測指標與主要決策契約必須在接觸任何 M2/M3 變體結果前永久凍結。

### 2. 嚴格隔離 Holdout 集（防範 Evaluation Leakage）
1. 嚴格鎖定 Dev (120) 與 Holdout (60) 的邊界，禁止共用同組近義改寫。
2. **檢索與特徵快取隔離**：Dev 實驗過程產生的動態 embedding、intent expansion 與關聯快取，不得在 Holdout 評測時被複用，防止資訊經由快取隱性滲透。
3. Holdout 僅能在 M4 終審階段單次執行（One-shot Evaluation），禁止依據 Holdout 結果反覆微調超參數。

### 3. 明確離線重播保真度與替代路線
若 M0 發現 host Decision API 無法完全隔離重播，必須明確回報「環境不可同構」，限制評測結論僅限於「特定 Adapter 條件下的相對排序」，不得直接推論線上生產環境之絕對表現。

---

## Unresolved

下列事項在進入無人化或正式執行前仍屬未決狀態，需在授權前補齊規格：

1. **無人執行實體停損與預算硬上限（Budget & Stop Conditions）**：
   - 目前全案缺乏 runtime 硬性金額截斷（Hard Dollar/Token Cap）。無人值守運作時，若遇 client retry 風暴或大量 context expansion，費用將不受控。
   - **必備停損條件**：
     - M0 嚴格限制可觀察請求 $\le 30$ 次。
     - M1–M3 批次執行前，必須設定明確的單次實驗批次計數器（Batch Counter）與異常中斷點（例如連續 2 次網路異常或單一批次輸入超過預期 token 閾值即終止退出）。
2. **批次模型費用計算標準未核定**：
   - 計畫依據之每百萬 token 報價僅為情境參考，尚未獨立驗證；且 Gemini expansion、動態 embedding 與主模型重審成本尚未納入閉環預算表。
3. **12 個沙盒驗收任務的自動判定準則**：
   - M4 提及 12 個可離線驗收任務，但缺乏機器可判讀的斷言（Assertions）與產物評估腳本規格，無人值守下無法自動完成驗收判定。
