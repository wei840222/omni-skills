# 技能庫品質與 skill-harness 選取改善計畫

- 日期：2026-10-25
- 深度：L3；跨資料集、實驗程式與 harness，預期跨多個工作階段。
- 狀態：M0、M1 已完成驗收；180 題最終 silver labels／hash manifest 已凍結（175 題可評分、5 題 uncertain）。M2 的 dev raw capture 與兩種融合比較已完成；current-max F1 81.12%、skill-identity-sum 76.33%，依規則保留 current-max。pool10 已執行，pool20 正在執行，尚未評保留集。
- 本次授權：使用者於 2026-10-25 指示「照你的計劃完成吧」，核准 M0–M4 執行與 Antigravity CLI（`agy`）獨立複核。Jev 按前述討論設 US$2 停止預算；正式 runtime 維持只讀，合併 main／部署不在此次授權。
- 計畫類型：act-as；後續由 agent 依里程碑執行。
- 時程：無指定截止日。
- 唯一計畫檔：本檔。既有 productivity 專案頁保留為歷史與決策來源。

## 目標與完成定義

建立可信的技能選取評測，找出是否值得修改 harness 的候選融合、候選數量及 Decision 證據輸入，交付有實驗支持的候選修補或明確保留現況的決策。

完成時應能回答：

1. 哪些錯誤來自測試標籤、技能適用邊界、候選漏失或最後選取？
2. 在固定資料與模型下，skill identity 融合、較大的候選池、命中片段各自有沒有改善？
3. 改善需要多少額外 token、延遲與模型請求；是否符合事前凍結的門檻？
4. 少量可離線驗收的任務是否得到正確產物，而非僅觀察到技能被選入？

可接受的結案結果包含「沒有足夠證據優於現況」。不得為得到正面結論調整標籤、刪除難題或事後降低門檻。

## 風險決策

**最危險的假設**：能在隔離環境忠實重播目前 harness 的資料身分、檢索、候選政策與 host Decision 語義，且評測標籤足以判斷選擇是否合理。若不成立，後續分數無法用來決定線上改動。

先在 **M0 的五個公開案例與本地 fixture** 驗證整合可行性；在 **M1** 凍結標籤與評測契約後才比較效果。M0 是可行性 spike，不是品質改善證明。

失敗預演：若數週後仍無可信結論，最可能是錯把自帶題目的 owning skill 當成唯一正解，或把替代的離線模型／流程冒充目前 harness。M0／M1 必須先排除這兩種混淆。

## 已知基線與證據界線

- omni-skills 的已提交實驗版本：`05baf79c`；技能資料來源 revision 另由既有 manifest 記錄，不與實驗程式版本混用。
- 當前 harness 原始碼：`da00386`，已包含 host Decision API。開始執行前重新確認 HEAD 與 dirty state。
- 既有實驗：963 技能、2,554 題，embedding 為 `text-embedding-3-small`／1536 維，末段使用 `rerank-3`。
- 按現有標籤，Full＋Rerank 命中 1,705 題，Refs＋Rerank 命中 1,699 題，不能憑六題差異決定全面採用其中一種表示。
- 已確認至少一組領域錯配：區塊鏈 `avalanche` 的測試卻問滑雪雪崩。`cv`／`resume` 等重疊案例需核對並標示可接受選擇。
- 目前 harness 是三集合檢索、候選池、統一 Decision；本次 `rerank-3` 實驗不等同該流程。最後 Decision 目前沒有 QMD 命中正文片段。
- 外層融合使用含 collection/path 的 hit ID，再對技能取最大值。3／2／1 權重與直接候選上限六個時，若有六個不同技能的 meta hits，meta 第六名分數仍高於 body 第一名。這是結構性條件推論，尚未量出真實效能損失。
- Runtime 的選入、讀取與經驗重用不等於任務成功；歷史混合版本資料不能當新版 Decision 的準確率。Resident 的精確 build 尚待可觀察證據核實。

## 範圍

納入：

- 測試資料一致性檢查、已確認錯配修正、可接受多標籤／多技能／無技能案例。
- 在既有 experiments 中建立 harness 對齊的隔離重播與報表。
- 候選融合、候選池與注入上限解耦、Decision 命中片段三項獨立消融。
- 通過實驗後的 feature branch 候選修補、回歸驗證、少量任務產物驗證。

界線：

- 首輪使用公開技能與新寫的公開案例。私密 runtime 僅參考已核對的摘要與案例類型，不直接匯出原始對話。
- 使用者於 2026-10-25 補充授權：需要較重的編譯／區塊鏈技能測試時可用 `ssh wei-workspace`。已唯讀確認可連線、Linux x86_64／8 核及 Python、Node、uv、Cargo、Go 的 PATH 入口；入口存在不代表版本或依賴已驗證。僅在實際任務需要時建立專屬實驗目錄，記錄遠端工具版本與產物 hash；本次不因此增加鏈上交易或部署。
- 不操作正式 Gateway、正式 QMD 索引、經驗卡、關係圖、credentials 或線上門檻。
- 不重開既有固定觀察窗、name-match 移除研究、關係問法 A/B、通用評測服務或版本追蹤服務。
- 既有關係圖重建與 Review CRUD／confidence TODO 維持獨立；本計畫不重建正式圖。
- 原本 2,554 題全量結果保留作歷史基線；未完成語義核對的題目不作選出勝出配置的主要依據。
- 本計畫的執行完成不包含合併、發布或部署。若有勝出修補，再提出具體部署與回復方案，依當次授權執行。

## 里程碑與驗收

後續里程碑只定成果與驗收；M0 通過後再細化下一階段，不先假設未知整合都能成立。

| 里程碑 | 可交付成果與可觀察驗收 | 估計投入 | 依賴／狀態 |
| --- | --- | --- | --- |
| M0：凍結證據與重播可行性 | baseline manifest、隔離方式與回復檢查、五案例重播紀錄；明確決定可沿用、需 adapter 或阻擋。通過條件見下節。 | 2–3 小時；spike 硬上限 3 小時 | 完成；`m0-acceptance.json`，25／30 外送、五例完整 query replay（四例呼叫 Decision、空池一例略過） |
| M1：修正標籤並凍結契約 | 全 2,554 題結構／身分檢查清單、已確認缺陷修正 diff、180 題 AI 雙方複核 pilot（silver labels）、固定 dev／holdout、評分與成本契約。 | 6–12 小時 | 完成；九批 AGY 及最終 source gate ACCEPT，`m1-freeze.json`／`m1-silver-labels.json` |
| M2：候選融合與候選池消融 | 在固定 raw hitlists 下，分別比較 current max 與 skill-level fusion，以及候選六／十／二十個；最終注入 cap 固定。交付召回、誤載、成本差異與選擇理由。 | 4–8 小時 | 進行中；融合比較保留 current-max，pool10 完成、pool20 執行中 |
| M3：Decision 命中片段 A/B | 固定 M2 選定候選池與同一 Decision model，比較現行 metadata＋association payload（無命中片段）與加入有界命中片段；交付逐題差異、選取品質、耗時與 token 報表。 | 4–8 小時 | M2；待執行 |
| M4：保留集、回歸與交付決策 | 凍結配置後一次評保留集；通過時形成候選修補與回歸結果，再用 12 個可離線驗收任務檢查實際產物。交付採用／不採用決策及文件，不宣稱代表全庫任務品質。 | 2–4 小時 | M3；待執行 |

**初估總投入：18–35 小時，跨多個工作階段**，不含等待人工裁決或服務恢復。高端由標籤分歧、host 重播 adapter 及 SDK／索引版本差異驅動。這是未校準初估；M0 後重估剩餘工作。若需超過區間或擴大語料／外送資料範圍，先更新本計畫。

### M0 詳細步驟

1. **建立基線與資料身分清單。**
   - 記錄兩個 repo 的 HEAD、lockfile／模型設定指紋、原始實驗 manifest 與結果雜湊。
   - 核對公開 963 技能與目標 agent winning skill 身分的交集、重名 precedence、內容 hash 差異；不把同名視為同版本。
   - 產出 `baseline-manifest.json` 與差異摘要。清楚區分公開 963 語料重播和實際 runtime inventory，不宣稱兩者相同。
   - Done-check：舊結果與資料未覆寫；每個比較均有明確 catalog、query、code、model 身分。

2. **建立隔離與回復證明。**
   - 在獨立 feature worktree／實驗 profile 中工作；正式安裝目錄只讀。
   - 測試輸出使用新的 run directory，與原始 baseline／正式索引分開。
   - 證明刪除實驗產物或還原 feature diff 後，基線 hash 不變且同一 fixture 的候選與 payload 可重新產生。這是隔離回復，不是回復正式資料庫。
   - 若需要索引快照，先確定資料是否公開、是否能重用既有向量；無法重用時先列新增 embedding 請求估算，不直接重建全庫。
   - Done-check：正式資料無寫入路徑；回復後基線 hash 與 fixture 結果相符。

3. **五個公開案例驗證真實流程。**
   - 以 source tests／現有 SDK 為基礎驗證 currentUserMessage、公開合成 conversation、QMD context、候選門檻與統一 Decision 的資料流。
   - 核對三集合與 name／experience／graph 候選來源。無法取得相同資料者標為 controlled fixture／unavailable，不能靜默關掉後稱 production-equivalent。
   - 驗證 host Decision route、batch schema、候選身分與回答對齊、timeout／空結果路徑，以及可重用的 cache key。
   - 不以 `rerank-3` 或 plugin compatibility route 靜默替代 host Decision。Host 無法隔離重播時交付阻擋與可行替案，由下一個決策點選擇。
   - 模型探測上限提案：五個公開案例、最多 30 個實驗端可觀察的新增外送模型請求，包含 embedding、expansion、Decision 及 client retry。取得啟動授權後，以外送前計數實作此限制；無法攔截 SDK retry 或尚未設定各 provider 的成本／token 上限時，只能執行零模型 fixture，不啟動付費 probe。
   - 若 host／provider 內部請求數或費用無法觀察，明列未知；請求數上限不是保證金額上限。
   - Done-check：五案例有完整階段紀錄且輸入／候選／payload 可對照目前原始碼；或產出明確的 blocked decision，停止擴大實驗。

### M0 驗證點

同時滿足下列條件才進入 M1：

- 能辨認並凍結語料、程式、模型及查詢身分。
- 原始基線與正式資料保持可核對，隔離回復檢查通過。
- 能忠實重播所宣稱的管線範圍，或已明確限縮結論的適用範圍。
- 已產生下一里程碑的實際題數、模型請求／token 估算及上限；不能帶著未定預算自動跑全量。

## M1 評測契約草案

### 資料與標籤

- 全量 2,554 題先查結構、唯一 ID、存在的技能、內容／標籤身分差異；領域疑似錯配只作標註核對候選，不自動重貼正解。
- 先修已確認的 `avalanche` 錯配；保留修正理由與前後對照，不把舊分數與新標籤分數直接相減。
- Pilot 預計 180 題：單一明確技能 60、合理替代技能 40、多技能任務 30、無需技能 30、多輪追問 20。這是可檢驗規模提案，不宣稱代表實際流量分布。
- 依技能家族與近義改寫群組劃分 dev 120／holdout 60；同組不得跨 split。標籤在看變體輸出前核對；無法裁決的案例保留為 uncertain，不放進主要決策分數。
- 每題記錄公開來源、類型、conversation、`acceptable_sets`、理由、審查狀態與 split；替代選擇以不同集合表示，多技能共需以同一集合表示，無技能為空集合。
- 標籤、expected 與評測理由只供計分，不能送進檢索／expansion／Decision。
- 選題不能依變體是否能命中來保留或刪除；既有自帶題目與獨立新案例分開報表。

### Antigravity 獨立複核

- 使用者指定 `antigravity-cli` skill 與 `agy` CLI；主代理先標註，Antigravity 在新的工作階段作盲審。記錄實際回傳模型、輸入雜湊與輸出，不自動更換模型或切換其他 CLI。
- 盲審輸入僅含公開 task／合成 conversation、無語義提示的案例 ID，以及固定版本的完整公開技能目錄與可核對技能內容；不提供主代理答案、owning-skill／原測試檔名、檢索排名或變體結果。兩方分別輸出 `acceptable_sets`、來源依據與不確定性。
- 收到獨立答案後才比對；保留兩份原始標註與分歧紀錄。只能根據事前凍結的準則與技能內容裁決，無法裁決者保留 `uncertain`，不為提高分數反覆詢問模型或刪題。
- AI 共識一律稱 silver labels，不能宣稱為人工核對或 human gold。報告同時列出納入、排除、不確定案例數與分歧率，揭露困難案例未納入主要分數的限制。
- 標籤與評分契約須在看變體輸出前凍結；holdout 標註可先審查，但不得用其變體結果調參。未建立 180 題資料前，計畫審查不算完成標籤複核。
- Antigravity 複核費用／配額與 Jev 分開記錄；全輪標註派工、批次大小、重試及用量上限須在 M1 啟動前固定。本輪只派一次計畫審查，不批量建立或審查案例。

### 指標與採用規則

- 候選階段：any-relevant coverage，以及是否完整包含至少一個 acceptable set 的 Recall@K；另外呈現 gate 前後的候選損失。
- 選取階段：對 acceptable sets 計算集合 precision／recall／F1、完整可接受集合命中率、無技能誤載數。
- 效率：實驗端可見模型請求、輸入大小／token、p50／p95、timeout／unavailable、cache 命中與沿用觀測。批次攤提不能冒充單筆端到端耗時。
- M1 凍結一個主要指標、成本／延遲上限及比較程序，再看變體結果。建議主要指標為 family-macro set-F1，並以 paired family bootstrap 描述不確定性；小樣本不以微小差異宣稱普遍改善。
- 該契約須寫明 family 定義、空集合、多個 acceptable sets 的計分方式、uncertain 的分母與公開數量，以及「支持改善」的事前判定規則；這些欄位未定案就不開始變體比較。
- 標註覆蓋率定義為 resolved／total，與選取品質分開呈現；主要品質指標明列已裁決分母。若呈現含 uncertain 的全體成功率上下界，僅針對已定義的二元成功事件計算，不把 uncertain 當成已知錯誤，也不把 resolved-correct／total 稱為標註覆蓋率。
- 推薦變體須在未用於調參的保留集支持改善，無新增無技能誤載，通過既有功能與新缺陷回歸，且符合事前凍結的資源上限。
- 若保留集證據不足、品質退步或超出資源上限，結案保留 baseline；不能在看結果後改門檻或繼續反覆使用同一 holdout 調參。

## 實驗隔離原則

- M2 融合實驗：固定 query、raw retrieval hitlists、模型與 gates，只改融合單位；候選內容可以因介入而改變。
- M2 pool 實驗：固定融合規則與原始 hitlists，只改可供 selector 評估的候選數；最後注入 cap 不變。
- M3 snippet 實驗：固定相同候選池、同一 Decision model 與政策，保留現有 metadata、conversation 與 association context，只增補作為 reference data 的命中片段。每候選的片段與總 payload budget 在執行前凍結。
- 經驗、圖與 conversation 能力已存在；其狀態／來源必須固定或明確分層，不與三項主要介入同時變動。
- M0 的五個 probe 不得使用 holdout 案例或同一家族；holdout 可先凍結獨立標註，但其檢索／expansion／Decision 結果只在 M4 配置凍結後產生與分析。
- Dev／holdout 的 query 與結果產物分開記錄；允許共用與答案無關的固定公開語料向量。共用 cache 必須以完整 query／context／模型／受測 payload／政策身分正確區分；禁止標籤、評測理由或用 holdout 結果調整的設定流入模型輸入。快取本身不等於資料洩漏，不要求為隔離而重付全庫 embedding 費用。
- M4 的 12 個任務在執行前凍結預期產物、可離線檢驗的斷言、每任務 turn／模型請求上限與停止條件；無法自動驗收者報為未驗收，不以技能被選入代替任務成功。
- 本計畫不訓練新 embedding／reranker，不新增獨立常駐評測服務，也不以調低線上門檻代替改善證據。

## 無人值守的預算與停止契約

- 本輪 Jev 停止預算為 US$2；全 run 共用 ledger，設定 47,000,000 輸入 token（公開牌價 US$1.974，保留餘額），每個實體請求／retry 外送前先預留 65,536 token，回應後按付費 usage 結算。M0 另加最多 30 次外送的階段限制，仍須同時扣全 run ledger，不是額外費用池。查詢展開、embedding、Antigravity 及任務主模型另列 request／token 額度；公開牌價不是帳戶實收保證。
- 新 run 使用外送前的請求／token 預留與實際 usage ledger，計入 client retry 與並行中的請求；輸入超限、剩餘額度不足或連續兩次 provider 錯誤時停止新增請求，保存可續跑狀態，不自動切模型或擴額。
- 完成一次批次後核對用量再啟動下一批。缺少帳戶費率、付費 token 或 host 內部可觀察性時，明列未知；無法證明符合已核准上限的付費路徑不自動開跑。
- 先前送出的請求無法撤銷其費用；停止機制限制後續外送，不能保證 provider 內部重試或尚未回報費用為零。M0 的零模型隔離檢查可先做，付費 probe 與後續里程碑須各自符合預算契約。

## 授權、不可逆成本與回復

- 使用者已授權依計畫完成實驗、標註複核與範圍內候選修補；進度與已發生模型請求以本檔及 run ledger 為準。不含正式合併或部署。
- 後續公開資料與 feature worktree 內的實驗／修補，可在使用者核准具體執行範圍與預算後進行；既有授權在其範圍內延續，不逐步重問。
- M0–M4 的主要檔案操作可由新 run directory 與 Git diff 回復；回復檢查在 M0、候選修補回復在 M4 驗證。
- 新增模型推論已發生的費用無法回復，以事前請求／token 上限、快取、少量 probe 與有界並行控制。沿用既有服務，不自動切換 provider 或升級模型。
- 原始私密會話、憑證、完整 live config 不進公開 repo，也不作本輪外送資料。若未來需要這些資料，先另列具體來源、用途與邊界。
- 正式部署、credential 變更、正式圖／索引重建、刪除 runtime、合併到 main 不在本計畫執行授權內。勝出後需先完成可審查的部署／回復方案，再取得對應授權。

## 狀態、偏差與交接

| 項目 | 狀態／證據 |
| --- | --- |
| 計畫交付 | 已寫入；2026-10-25 獨立 plan-review：OKAY，無重大阻擋；後續契約待決項保留於 M1 |
| Antigravity 獨立審查 | 已透過 `agy --print` 完成一次；原始結論 CLARIFY。已補盲審／silver-label、覆蓋率、holdout 使用時點、預算停止與任務斷言契約；全快取禁用及覆蓋率公式未照單採用，採納說明見 `../reviews/2026-10-25-agy-plan-review/review.md`。未對修訂版再送模型 |
| 實驗與修補 M0–M4 | M0、M1 通過；M2 融合比較完成、pool 實驗進行中；M3、M4 尚未執行，未實作線上候選修補 |
| 已發生偏差 | AGY 初次 `--print` 引數失敗未進模型；改用官方 stream-json 後第一批已有有效 terminal SUCCESS，但 CLI 沒自行結束。保留原始輸出並修正 terminal 後程序清理，再以明確 recovery 匯入成功批次，不重跑。其後共完成五批／100 題；回報 output 合計 101,650 超過原訂 100,000，driver 已停止後續四批。使用者其後明確同意提高至 250,000；授權原文與 prepare／freeze hash 存於 `execution.budget-amendment.json`，以第二次 recovery 匯入五批後接續四批。所有舊 marker、原始回應及 usage 均保留。 |
| M1 來源複核 | 最終 source gate ACCEPT 完整 180 題。AGY 九次 review，770,123 input／174,355 output；全部低於修訂額度，未重跑成功批次。80 次讀檔嘗試中 67 次成功、13 次不存在；成功 bytes 與公開快照相同，來源根目錄偏差已揭露。197 筆引文為 137 逐字、44 Markdown 格式差異、16 省略／串接改寫；保留原文並補來源。第八批 free-text 串接 draft／final，依官方 schema 欄位與最後 finish 參數一致的 `structured_output` 解析，未新增該批模型呼叫。 |
| M1 最終凍結 | labels SHA `3fca29489297cd536b322707944167736792080e2b0114677ff9d8b5b5b71538`；freeze SHA `c19b7fa44a798794d7e263bb8dc2f0d8e275258eac077f5f6bde9c5b980d14f8`。相對 primary 20 題裁決變更；175／180 resolved、35／36 家族可評分。holdout 55／60、11／12 家族；f32 全部 uncertain。SQL 有效替代跨 split 共用，不能宣稱最終技能身分完全未見。最終 silver snapshot 另存 `experiments/fixtures/harness_silver_annotations.json`，不是 human gold。 |
| 已完成資料修正 | `a760c6f6` 單獨提交 Avalanche 三題領域修正；重新檢查官方來源、JSON-RPC batch 與實際離線 Python controls 通過。公開 SKILL／references 語料與歷史結果未改寫。 |
| 消融／任務準備 | `harness_ablation_protocol.json` 已在看變體結果前凍結階段選擇、命中片段 2048／320 UTF-8 bytes 及保留集使用規則。12 題任務／驗收器已凍結，7 tests 包含正負控制通過；真正 24 次 paired outputs 尚未執行。 |
| M2 真實觀測 | 120 題 raw capture 完成，361 次外送（含一個額外 embedding）、零失敗，所有原始清單保存。current-max/pool6/none：family-macro set-F1 0.81115079、exact 0.58333333、recall 0.92083333、no-skill FP 1／20。identity-sum/pool6/none：F1 0.76333333、FP 2／20；paired family bootstrap delta −0.04781746，95% CI [−0.08694444, −0.0125]，新增 FP p149，故不採用此融合介入。來源 `development/*-summary.json` 與 `m2-fusion-comparison.json`。 |
| 重播工具修正 | source gate 先拒絕 policy hash 形狀混用、endpoint 配對缺漏、cache billing metadata 不一致；修正與 regression tests 通過後接受。120 題 raw 及 386 個既有 cache payload／ledger usage 獨立核對無差異。另修 stdin UTF-8 跨 buffer 解碼；第一次 selector 在 preflight 即停止、零模型請求。保留舊準備檔，重建後證明兩個融合各 120 題的 model-input objects 完全相同，raw hash 未改；同樣修正 summary 的內嵌 Node hashing reader。未變更標籤、評分規則或比較門檻。 |
| Jev 批次預算 | 進入 pool20 前全 run 476 次 Jev／1,045,194 input tokens，公開牌價 US$0.043898148；unknown usage 0。US$2 停止上限維持。其他 provider／AGY 用量分列，不把此數字當成所有服務的帳戶實收。 |
| 模型與預算決策 | Jev 全 run 47M 付費輸入 token／US$1.974 公開牌價；M0 另限 30 外送。持久化 ledger 8 tests、受控 fetch 9 tests 及 host 13 tests 通過；M0 共 25 次外送：embedding 6 次／9,266 tokens、expansion 5 次／5,682 tokens、Jev 14 次／26,133 input tokens（US$0.001097586 公開牌價） |
| 政策／正式 runtime 變更 | 無 |

連續兩個步驟偏離預期輸出、需要更換模型／語料範圍、預算或工時超出本計畫時，先記錄原因並重排剩餘里程碑，不連續補丁式往下推。閒置超過七天時，先重核 HEAD、基線 hash 與 M0 最大風險。

本檔是工作交付物，不另建個人偏好或 outcome 記憶庫；長期記憶遵循 Hindsight 單一來源規則。計畫執行狀態與偏差只維護在本檔，結案後保留可追溯結果，不自動刪除交付物。

### 2026-10-25 執行紀錄

- Canonical run：`experiments/datasets/harness-quality-20261025/`；資料與模型 cache 均 Git ignored，既有 baseline 不覆寫。
- `baseline-manifest.json`、`baseline-restore-check.json`、`dataset-audit.json` 已產生；963 技能／2,554 題／9,641 來源 hash 均一致，六個基線輸入前後 hash 不變。作者 `pass=true` 不是獨立驗證；85 題有 evidence、2,469 題未附 evidence；avalanche 三題仍待 M1 語義修正。
- 五個 live allowlist 均含公開 963 技能；meta/body 各 962 份與公開快照一致，唯一同名差異為 `triage`。此處不宣稱完整 references／resident build／atomic snapshot 身分已驗證。
- 本輪固定 `text-embedding-3-small`／1536，與 plugin 實際配置一致；QMD YAML 的 Voyage 4／1024 僅記為不同預設，不改設定也不跟隨換模型。
- 真實 installed skill-harness consumer → host public Decision facade → registry／TypeSafe provider 的 11 個離線測試通過；五個 synthetic 案例只驗資料流，不是品質結果。最終 syscall 審查為零網路、零正式 config/runtime/`.env` 讀取。
- Host adapter 的受控 HTTP 注入使用 SDK mock-fetch seam，因此跳過 DNS／dispatcher；不宣稱驗證正式網路 SSRF。最初探索僅攔 global fetch 時可能嘗試 synthetic loopback socket，已修正並以底層 socket/DNS deny 及 syscall 檢查驗證後續流程；無外部模型請求。
- 隔離 QMD 正在檢查精確公開文件向量重用；TTL cache 只有 23 筆，不能據此承諾全庫零新增 embedding。優先從正式索引唯讀抽取與已知公開內容／title／hash／chunk 完全匹配的向量，不複製整個私人 DB。
- 受控 transport 初次 review 的三項缺陷（Request header、alias cache、錯誤答案 cache）已修正並通過重新審查；host → ledger → fake native 整合已由父代理重跑 13 tests 通過。
- `qmd-preflight.json` 發現 10 個公開 triage 缺口後，以一次受雙 ledger 控制的 embedding 請求補足，回報 8,933 tokens。`qmd-build.json` 驗證 963 技能／9,641 文件／10,443 vector rows、needsEmbedding=0、errors=0；432 次為本地 cache 回放，不是外送請求。source generation 1009→1011 另有紀錄，未覆寫舊 preflight。
- `m0-host-probes.json` 的五公開案例均經真實 host public facade 成功、回報 jev-1.14.0、legacyCalls=0；含對話、合成 experience／relation 與無需技能案例。這是受控候選 fixture，不代表 QMD 召回或生產準確率。Jev 付費 usage 共 10,367 tokens，公開牌價 US$0.000435414；embedding US$0.00017866，兩者分帳。
- 查詢展開沿用 QMD 原始 payload，不添加 max_tokens；依已核對官方 Gemini 3.5 Flash-Lite 的 65,536 output-token 上限預留，避免為節費暗改受測行為。實際 provider usage 與帳戶價格仍按 ledger 分開記錄。
- `m0-query-probes.json` 五例完整 managed query replay 通過；每例均保留三集合原始 top40 hitlists、相同 raw query、rerank=false，所有模型回應經消費端驗證。四例呼叫 host，無需技能案例因空候選池略過 host，不能寫成五例均呼叫 Decision。
- `m0-acceptance.json` 已逐項核對並再 hash 六個原始輸入，皆未變；global／probe ledger 逐筆對帳相符，共 25 次且全為 completed、無 unknown usage。獨立 source-review ACCEPT，範圍只限公開隔離流程，不是 production 等價或品質增益。
- M1 primary package：180 案／36 families，類型 60 single、40 alternatives、30 multi、30 no-skill、20 followup；dev120／holdout60，主可接受技能身分跨 split 無交集，M0 五技能不在 holdout。初標 6 案 uncertain，不能提前當成雙方共識。
- 在盲審／變體觀測前補了 10 題「提到技能名但只是 literal copy／pick」負樣本；可靠性契約補明 unavailable 不能當正確空選擇，合法空池 skip 才可正常計分。原採用數值門檻未降低。
- `m1-pre-review-freeze.json` 固定 cases／primary annotations／contract／metrics 雜湊；Antigravity 收到的只含 opaque cases、完整963技能目錄與公開來源，不含初標、family、split、排名或變體結果。上限九批各20案、無自動重試、每批5分鐘；可觀察額度 input4M/output100k，限制不冒充 provider 帳單硬上限。
- 尚待：Antigravity 盲審、分歧處理與 final silver-label freeze、已知 avalanche 問題修正、M2–M4。不得將 M0 成功或初標凍結當成完成整體實驗。

**Next action：**依凍結輸入執行九批 Antigravity 盲審，核對回應與引用、處理分歧並凍結 final silver labels，再進入 M2；整個 run 持續共用 Jev US$2 停止額度。

## 依據

- 本次分析與逐題結果：`/home/wei/Documents/Gitea/wei840222/omni-skills/experiments/datasets/routing_benchmark_results.json`。
- 實驗定義：`/home/wei/Documents/Gitea/wei840222/omni-skills/experiments/README.md`。
- 候選融合與上限：`/home/wei/.openclaw/extensions/skill-harness/src/qmd/skill-index.ts`、`src/hooks/index.ts`。
- Decision state：`/home/wei/.openclaw/extensions/skill-harness/src/classification/selection-batch.ts`。
- 既有實驗、結案與獨立 TODO：`/home/wei/productivity/projects/ai/skill-harness.md`；本計畫不複製私人原始 runtime。
- 規劃流程：`/home/wei/Documents/Gitea/wei840222/Yumi/skills/plan/SKILL.md` 及其 `references/long-horizon.md`、`references/risk.md`。

- 模型價格／上限核對（2026-10-25）：[TypeSafe Models](https://docs.typesafe.ai/models)、[TypeSafe System One usage](https://docs.typesafe.ai/api/system-one)、[Gemini 3.5 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite)、[text-embedding-3-small](https://developers.openai.com/api/docs/models/text-embedding-3-small)。
