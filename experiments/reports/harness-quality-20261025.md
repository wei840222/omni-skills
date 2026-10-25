# Skill-harness 對齊實驗結果（2026-10-25）

本輪決策是**保留現行 current-max／候選池 6／無命中片段**。技能身分融合、較大的候選池及命中片段，都沒有在事前凍結的規則下優於基線。沒有形成 production 修補，也沒有調整正式 runtime。

完整數據、逐題預測及 24 份任務原始碼收錄於 [JSON 報告](harness-quality-20261025.json)；互動檢視使用 [harness_quality_mo.py](../notebooks/harness_quality_mo.py)。原始向量、模型快取及完整 checkpoints 保留在本機 ignored run `experiments/datasets/harness-quality-20261025/`，其指紋記錄於報告。

## 方法及適用範圍

這是對齊實際安裝版 harness 與 host Decision 的受控離線實驗，不是前一輪 `rerank-3` 的 Top-1 benchmark，也不是某篇論文的逐項重製。

- 公開目錄 963 技能；既有 2,554 題先做結構及來源核對。在修正前快照中，原作者全部標記 pass，但只有 85 題附 evidence，不能把其餘 2,469 題當作已獨立驗證。
- 新 pilot 180 題、36 個 intent families，依家族分 dev 120／holdout 60。最終 AI silver labels 為 175 題 resolved；holdout 納入 55 題／11 families，f32 的五題全部 uncertain，排除於主要指標。
- Primary AI、AGY 九批盲審及來源裁決在觀察變體前完成。這是 silver，不是 human gold；來源及裁決仍可能有錯。最終 SQL 替代技能跨兩個 split 共用，不能聲稱所有技能身分在 holdout 完全未見。
- Embedding 固定 `text-embedding-3-small`／1536；expansion 為 `gemini-3.5-flash-lite`，Decision 請求 `jev-latest`、實際回報 `jev-1.14.0`。
- 使用隔離 QMD 的三集合查詢、實際安裝版候選政策與 host public Decision facade。權重 3／2／1、skill gate 0.4、最終注入 cap 6、Decision timeout 8 秒保持固定。每題原始 hitlists 擷取一次，各變體共用。
- 私人經驗及關係圖未匯入，明列 unavailable；沒有匯出真實私密對話。SDK mock-fetch seam 不涵蓋正式 DNS、dispatcher、Gateway、resident working set 等邊界，因此不宣稱 production 完全等價。

主指標是 **family-macro best-acceptable-set F1**：先把預測技能集合與每個完整可接受集合比較，取最佳 F1，再依 intent family 等權平均。它懲罰不必要的多選，不能與舊的 owning-skill Top-1 百分比直接相減。

事前採用條件包括 F1 至少增加 3 個百分點、配對 family bootstrap 95% CI 下界大於零、沒有新增 no-skill false positive，以及完整性、延遲、token、timeout 和預算檢查。延遲及 token p95 比率上限為基線的 1.25 倍。沒有在看 holdout 後降低門檻或改標籤。

## Development：五組已完成配置

120 題均完成；各配置沒有 unavailable、timeout 或 error。合法空候選池另列為 skipped-empty-pool。

| 配置 | Family F1 | Exact set | No-skill FP（20 題） | Selector service p95 ms | Input tokens p95 |
| --- | ---: | ---: | ---: | ---: | ---: |
| current-max／6／無片段 | 81.12% | 58.33% | 1 | 315.38 | 2,853.35 |
| skill-identity-sum／6／無片段 | 76.33% | 50.00% | 2 | 314.70 | 3,022.40 |
| current-max／10／無片段 | 77.37% | 50.00% | 3 | 328.66 | 4,291.35 |
| current-max／20／無片段 | 77.07% | 49.17% | 2 | 316.92 | 7,495.95 |
| current-max／6／命中片段 | 79.50% | 56.67% | 3 | 291.58 | 3,386.10 |

Identity-sum 相對基線的 F1 差異為 −4.78 個百分點，配對 family bootstrap 95% CI 為 [−8.69, −1.25]。擴大候選池的 token p95 約為 1.50／2.63 倍，且沒有改善選取品質。

因此各階段保留原基線。依事前規則，從已完成的非基線中選最高 F1 的命中片段版本，作唯一的**診斷用 holdout 對照**，並非建議採用。片段預算是整個 map 2,048 UTF-8 bytes、每候選 320 bytes，取實際 SDK bestChunk；不是任意截取技能正文。

## Holdout：唯一一次凍結比較

`challenger-config.json` SHA 為 `de334db2e2ca7d7ad03a892bccb1c2486e4388c1c31ae22179d6e83f42bbb66f`。它在 12:57:52 UTC 凍結，raw capture 於 12:58:02 UTC 啟動。兩個版本各完成相同 60 題，主要計分使用其中 55 題。

| 指標 | 現行基線 | 命中片段 |
| --- | ---: | ---: |
| Family F1 | 74.73% | 73.88% |
| Precision | 67.94% | 66.52% |
| Recall | 90.91% | 90.91% |
| Exact set | 47.27% | 43.64% |
| No-skill FP | 2／5 | 2／5 |
| Selector service p95 | 269.25 ms | 276.94 ms |
| Input tokens p95 | 2,752.85 | 3,251.90 |

F1 差異 −0.85 個百分點；10,000 次配對 family bootstrap、固定 seed 20261025，95% CI 為 [−2.30, +0.24] 個百分點。CI 跨零，不能聲稱片段已被證明普遍有害；結果也沒有提供採用所需的改善證據。

兩者 FP 總數相同，但基線為 p151／p152，片段版為 p152／p155：修復一題又新增一題，仍未通過事前的 no-new-FP 條件。最終決策保持基線。

## 對話上下文確實有傳入

20 題多輪追問均把公開合成的前文送入 `conversation_context`；其餘 160 題是獨立任務。各比較版本使用相同前文。

例如 p178 的最新訊息為「Does it run on the server?」，前文討論 SvelteKit effect 與 server rendering。實際 Jev 回報 svelte 0.93、web 0.30、frontend 0.11、server 0.05、home-server 0.02、roblox 0.01，最後只選 svelte。這與使用者核對的 payload／結果一致。

基線在 holdout 的分項如下：

| 類型 | Resolved 題數 | Family F1 | Exact set |
| --- | ---: | ---: | ---: |
| 單一技能 | 20 | 91.67% | 75.00% |
| 合理替代技能 | 15 | 42.00% | 0.00% |
| 多技能共需 | 10 | 84.67% | 30.00% |
| 無需技能 | 5 | 60.00% | 60.00% |
| 多輪追問 | 5 | 100.00% | 100.00% |

多輪 holdout 只有 Svelte 一個家族的五題，不能外推為一般長對話準確率。整體差異也不能歸因於漏傳前文。依最佳可接受集合分類，基線 29 題 exact-set 不符中，28 題含額外技能、3 題有漏選（兩者可以重疊）。目前更值得研究的是重疊技能與多選，而不是直接擴大候選池。

## 12 組實際任務：primary 與 supplement 分開

使用 12 題事前凍結的 TypeScript、JavaScript、SQLite、CSV、資料彙總、Bash、regex、NDJSON 任務。先執行真實 query＋兩臂 Decision，再派 24 個全新 native worker，每臂僅生成一次。Worker 只收到公開題目、所選 SKILL.md 全文及公開 reference allowlist；不提供 variant 名稱、隱藏 grader、另一臂輸出或修正回饋。主代理檢視 24 份原始碼後，才在受限本機環境驗收。

**凍結 primary 結果：兩臂各 10／12；10 組同時通過，沒有單臂勝出。**

t05、t12 共四份產物只得到 `bounded-execution-or-contract`，沒有進入語義案例：SQLite authorizer 未允許 `typeof`；Python AST 未允許公開題目未禁止的 `text.split("\n")`，restricted builtins 又缺少 `RecursionError`。獨立 reviewer 核對後接受此診斷，不能把這四次拒絕直接當作語義答案錯誤。

因此另存一個明確標記的 **post-observation supplementary check**：只對這四份已鎖 hash 的原產物，允許 SQL `typeof`、已審查的 `text.split("\n")` 及 `RecursionError`。原案例、預期值、時間／記憶體限制均保留，沒有修改解答、重跑模型或改寫原 grader。四份補充驗證全部通過。

原 primary 10／12 保持不變，不合併寫成 primary 12／12；補充結果也不作採用依據。這些任務很小、每臂只有一次生成，且大多數兩臂選到相同技能。沒有 no-harness control，不能據此證明載入技能相較不載入有因果增益，也不能代表全庫執行品質。Native model 的精確身分及 token 用量未由介面提供，報告保留 unknown。

## 費用、失敗及驗證

全 run ledger 共 1,320 次實體請求，含 probe、dev、holdout、任務路由及失敗：

| Provider | Attempts | 已知 billed tokens | 依宣告單價換算 USD |
| --- | ---: | ---: | ---: |
| Jev | 923 | 2,387,507 input | 0.100275294 |
| Embedding | 199 | 25,123 | 0.00050246 |
| Expansion | 198 | 224,644 | 未宣告單價 |

另有一次 expansion transport-error 用量未知，75,291 tokens 預留未釋放。失敗時間約 15 秒，與原 timeout 一致；因 transport 沒保留底層例外，不能斷言具體網路或 provider 原因。原失敗目錄、帳本及快取保留，人工核對後以相同條件做一次明確 recovery。Recovery 實際 36 次新請求、零 cache hit；首個 intent fingerprint 與前次不同，因此沒有聲稱重用了前次成功請求。

Jev 明顯低於 US$2 停止上限。此金額是依本輪宣告單價換算，不是帳戶帳單；不含 expansion、AGY 或 native worker 費用。AGY 九批共回報 770,123 input／174,355 output tokens，低於使用者核准的 250,000 output 上限。

Cache 的服務耗時及 billed tokens 沿用原始觀測；不把本機 cache lookup 當成模型服務時間。共用 query 與 selector 費用分開，不能把各配置重複列出的 shared-query 費用再相加。Query＋selector 的相加時間是重建值，不是實測冷啟動 Gateway 延遲。

驗證包括 Python 99 tests、Node 78 tests；原始六個 benchmark／embedding 檔案 hash、8,678 份公開 SKILL／reference 及 23 個 M1 凍結項目均保持一致。來源、dev 決策、holdout 及 M4 工具分別經獨立 reviewer 檢查。Reviewer 找出的 collector 檔名錯配已修正並有回歸測試；本輪 24 份產物的實際檔名均符合 frozen contract，不受該缺陷影響。

## 對技能庫與 harness 的判斷

現行路由能在受控環境重現，多輪上下文也正常送入；本輪證據支持保留目前流程，沒有支持上述三種改動。它沒有證明 harness 相對不用 harness 提高多少準確率，更沒有證明所有 963 個技能的任務品質。

技能庫的結構與來源可追溯，但作者測試的 evidence 稀少、適用範圍重疊及已確認的 Avalanche 領域錯題，表示品質仍需要來源裁決與真實任務驗收。Avalanche 三題已修正；SKILL／reference 語料未因本輪消融改寫。少量來源的版本新鮮度仍是限制，不能從結構通過推論內容全部正確。

後續若另開研究，優先檢查「每個候選各自有幫助」的 predicate 與「完成任務所需的最小技能集合」是否目標一致，並為替代／重疊技能建立更清楚的邊界。再以新的獨立案例驗證多選控制，加入 no-harness control 及更廣的多輪家族。本輪不使用已看過的 holdout 繼續調參，也不把這些後續假設直接改進正式環境。
