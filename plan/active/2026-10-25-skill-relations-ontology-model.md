# Skill related-skills ontology 建模提案

- 日期：2026-10-25。
- 狀態：設計經 ontology_log_design_gate plan-review OKAY；依使用者新指示完成初始 catalog 匯入，尚未實作增量同步器、分類或 runtime adapter。
- 本輪範圍：專案根目錄 ontology/schema.yaml 與 ontology/graph.jsonl，僅初始資料；不改技能 metadata、凍結實驗、harness runtime 或正式 graph，不呼叫付費模型。
- 原專案：`/home/wei/Documents/Gitea/wei840222/omni-skills`；盤點 HEAD `4896704b9c9eed9117777e324c6ecd293cd68e9d`。
- 本檔是唯一計畫。使用者最新決定取代初版快照與獨立評估實體方案。

## 最新決策及主要風險

採 **Skill 節點＋單一有向關係邊＋追加操作日誌 graph.jsonl**。作者宣告與分類放同一邊，不另建 RelationAssessment／Assertion；不建立每代完整快照目錄或 current pointer。

同一 catalog 的有序 `(from, to)` 最多一條有效邊，反向獨立。類型改變不改變邏輯邊身分。歷史由操作日誌與 Git 保存。

最大風險：裸 relate 是新增，不是 upsert。更新需 unrelate 舊 triple，再 relate 完整新值，整批發布。這是可重播的 append-only operation log，不宣稱原 CLI 有資料庫 WAL 的交易或斷電復原保證。

## 盤點

| 項目 | 數量 |
| --- | ---: |
| Skill／可解析 frontmatter | 963／963 |
| 有 related-skills／缺欄位 | 778／185 |
| 有向宣告／不同 target | 3,862／715 |
| reciprocal pairs／其中有向邊 | 392／784 |
| 只有單向宣告的邊／孤立技能 | 3,078／43 |
| 解析錯誤、重複 key、缺失 target、歧義、自我關聯 | 全部 0 |

778 個欄位皆為 JSON string，內層非空 object。963 個 name 唯一且等於目錄名；code 與 coding 不合併。185 個缺欄位者中 142 個仍有 incoming；缺欄位不代表無關。

## 精簡模型

Skill entity：

```json
{"id":"github:wei840222/omni-skills:aws","type":"Skill","properties":{"name":"aws","source_path":"skills/aws/SKILL.md"}}
```

ID 不含 SHA 或本機絕對路徑，內容更新仍是同一技能；catalog 不同則 namespace 不同。改名需新 ID 或顯式 mapping，不靠 fuzzy 猜測。保留全部 963 個節點。

關係操作：

```json
{"op":"relate","from":"github:wei840222/omni-skills:aws","rel":"related","to":"github:wei840222/omni-skills:terraform","properties":{"reason":"HCL authoring, state surgery, module design"}}
```

ID 格式為 `<provider>:<repository>:<skill>`，共同來源契約由 schema 的 sources 按 provider／repository 分組，schema 不再綁單一 catalog。這是使用者指定的邏輯來源識別，不宣稱目前 Git remote 使用 GitHub transport。各檔 SHA／related-skills presence 的 manifest 屬後續同步器選項。邊不重複 origin、source_path、yaml_field、inner_json_key，由 from 節點與 to 還原。同步器須檢查 target key 與目標名稱一致；未來別名需明確修訂契約，不默默丟掉原值。

aws → terraform 與反向獨立；後者理由為 `provider-specific AWS resource design and IAM once the plan/state problem is clear`。不補反向、不跨 hop 推論。完整 reason 保留，YAML 原 bytes 從固定 Git 來源取得。

Predicate 沿用 related、depends_on、composes_with、similar_to、conflicts_with、specializes；目前全部 related，不呼叫分類模型。依使用者最新核准，不存 classification_status、verification_status，也不新增 status。rel 表達關係種類，reason 保留理由；分類／審核尚無對應流程，不預建狀態機。未來真有流程再定義必要欄位；分類不是驗證，不觸發依賴閉包／互斥／自動共同載入。

Reason 或端點內容改變，舊分類失效或重審；無差異同步不清除既有分類。一條邊只有一個當前主要 predicate，完整 reason 保留其他語義。

## 日誌與重播契約

| 既有操作 | 既有 reader 的效果 |
| --- | --- |
| create | 按 entity.id 寫實體；本 writer 只對新節點使用 |
| update | 按 id 淺層合併 properties，不更新邊或清除 property |
| delete | 移除實體，不連帶清除 incident edges |
| relate | 新增邊，不自動覆蓋 pair／triple |
| unrelate | 移除所有相同 from／rel／to 的有效邊 |

不新增自訂 upsert／transaction op。更新理由／類型／分類，先對該 pair 所有舊 predicate 追加 unrelate，再 relate 完整新值，即使類型未變也先撤回。移除關聯只追加 unrelate；刪除節點先撤回 incident edges 再 delete，整批發布。未來 property 清除不能把 null 當成現有 update 的刪除功能。

重播完成後每個有序 pair 至多一條有效邊，歷史多筆 relate 不算重複有效邊。無差異同步零追加，只追加必要 delta。移除宣告只表示當前沒有宣告，不等於已證明無關。

## 發布、歷史與復原

目前已建立兩個初始資料檔：

```text
ontology/schema.yaml
ontology/graph.jsonl
```

下列為後續完整同步器的選項，本輪未建立：

```text
ontology/manifest.json
tools/skill_relations.py
```

SKILL.md 為作者資料來源，graph 為狀態與操作歷史。Manifest 記共同契約、最近同步來源 revision、SHA／presence 等稽核資料，不是提交指標。

發布流程：單一 writer lock → 嚴格重播目前 log → 計算 delta → 記憶體驗證 old log＋完整 batch → 同目錄暫存檔寫 old bytes＋new lines → 原子 rename 發布 graph。既有 byte prefix 不變，邏輯只追加；實體 I/O 是 copy＋atomic replace，不是逐行原地 append，也不是保留歷代快照。此規模先採簡單可靠方式。

Reader 看到舊檔或完整新檔，不會看到 unrelate／relate 中間狀態。通用 append_op 不提供此保證，不直接用於多筆更新。發布前失敗不動 graph；manifest 後寫失敗以 graph 為準。Manifest 帶 graph byte length＋hash，使用前核對，不匹配即拒用，重新核對來源後重建；兩個檔案 rename 不構成跨檔交易。

Malformed JSON、未知 op、無效型別整體拒收，不靜默跳過錯誤；外部工具留下壞尾端先停同步，不自動截短日誌。未發布暫存檔不影響正式檔。MVP 不承諾斷電 durability；需要時再加入 file／directory fsync 並實測。

依檔案順序重播，不依 timestamp 排序。正常更新保留全部歷史。回復狀態時比較指定 Git 版本或已驗證整批邊界與目前狀態，產生補償操作追加發布，不截短正式 log。任意 line prefix 可能落在 batch 中間，僅供診斷；合法邊界以已驗證版本／同步結果 byte length＋hash 識別。

來源、圖、manifest 一起留下可追溯 Git commit。未 commit 的中間日誌不保證能對應當時來源 bytes。MVP 不 compaction 或自製交易協定；過大時先量測重播成本，再另規劃歷史壓縮。

## 驗證與 harness 邊界

嚴格驗證已知型別／predicate、唯一 ID、欄位型別、非空 reason、端點可解析、無自我邊、pair 唯一。related 允許環，392 reciprocal pairs 不能被無環約束拒收。安全解析 YAML／JSON 並拒絕重複 key；缺失、空 map、解析錯誤分開。

首次有效圖 963 nodes／3,862 edges，方向／target／reason 逐條一致，初始 create＋relate 共 4,825 records；後續 records 包含歷史，不再等於有效節點邊總數。用 load_graph 完整 properties 驗收，get_related 省略 properties 不能判定無損。

Ontology CLI create／relate 沒有 pre-write validation，validate_graph 未完整強制未知型別／scalar 型別，validate CLI 不保證錯誤時非零退出。薄的 domain 同步器補上述契約，不能宣稱 CLI 原有保證。

Harness source 基準 `/home/wei/.openclaw/extensions/skill-harness` HEAD `009b121a26501d23d2474e47b010c73c6bc0c972`，package 2026.10.7；只讀 source，未讀正式 graph 或驗證 Gateway build。

- Harness 已 replay 此格式；import writer 已 unrelate＋relate 與 atomic publication，reader 不強制 pair 唯一。
- Runtime ID 綁 name／realpath／frontmatter-body fingerprint（排除 related-skills），不能直接用 catalog ID。Runtime 邊要求 source: author-import、verification_status: unverified、formatVersion: 1；後續 adapter 才映射，精簡 catalog profile 不直接匯入。
- Runtime metadata 移除不自動撤回 imported edge；catalog 刪除政策不代表授權改正式 graph。保留既有 locking／ownership／備份，不另建 runtime graph。
- import 分類分數、當回合 relation 參考分數、skill 入選分數不同；格式變更不自動改選取政策。

品質準則：必要技能覆蓋與明顯無關載入優先；有幫助的多選可接受。超出原標籤集合不直接當無關，數量／F1／exact match 為輔助，不修改凍結資料或用已看過 holdout 調參。

## 分階段計畫

| 階段 | 產物及 done-check | 初估 |
| --- | --- | --- |
| P0：契約及隔離 spike | 約 10 個實際案例；節點 update、理由更新、換類型、反向不變、刪除清邊、分類失效。證明裸 relate 重複，正確 batch 後 pair 唯一；舊 reader 可讀完整 properties。測原子發布與 manifest mismatch 拒用 | 0.5–1 小時 |
| P1：全目錄增量同步 | 首次 963／3,862、理由完全一致，第二次零追加；來源／內容／關聯刪除只出必要 delta；未變更分類不清除，每次保持舊 log byte prefix | 2–3 小時 |
| P2：查詢與歷史驗收 | incoming／outgoing／both 帶理由查詢；整批歷史重播與補償回復、並行 writer 不丟更新、發布前故障不變、manifest 過期偵測、壞 log 拒收。來源及六個 baseline hash 不變 | 1–2 小時 |
| P3：可選 runtime adapter | public fixtures 驗證 identity／properties／六類型／ownership／歷史，不碰正式 graph；政策改動另開實驗 | 另估 2–4 小時 |

完整 MVP 初估 3.5–6 小時，待 spike 校準；無 embedding／Jev／AGY 費用。P3 不綁 MVP；本輪僅先交付初始資料，P0–P2 增量／故障／歷史驗收未完成。

P0 記錄原 repo experiments/datasets/ 六個 baseline 實際 hash：manifest.json、benchmark_queries.json、documents.json、embedding_manifest.json、embeddings.npz、routing_benchmark_results.json，不沿用舊值。

## 證據與複核

- 原 repo ontology.py:67 replay、120 create、201 relate；create/entity 與 relate/from/rel/to/properties 是實際 wire 格式。
- skills/aws/SKILL.md:6、skills/terraform/SKILL.md:14 為反向不同理由；code 與 coding 是不同 identity。
- Harness relation-graph.ts:113 replay，appendImportedRelations 為 unrelate／relate 與原子發布；relation-import.ts、related.ts、classification/selection-batch.ts 為分類／選取界線。
- 本版獨立 ontology_log_design_gate 判定 OKAY：單邊更新、追加重播與原子發布契約成立，無重大阻礙。這是設計複核，不代表 P0／P2 故障及並行驗收已通過。
- 主代理以實際 ontology.load_graph 作純記憶體驗證：裸 relate 會重複；unrelate＋relate 更新正向理由／類型且保留反向；update 淺層合併。兩段 JSON 範例可解析，git diff --check 通過。未建立／讀取 graph 檔案。

## 本輪初始匯入驗收

- 輸入：目前 worktree 的 skills/*/SKILL.md，共 963 份；與原 repo 最新來源逐檔 SHA 相同。
- Schema：精簡 Skill 欄位、六個既有 predicate；YAML anchor 共用關係規格，初始資料僅使用 related。共同來源欄位在 schema 指定一次，不在節點／邊重複。
- Graph：963 create＋3,862 relate＝4,825 筆；778 個技能宣告 outgoing，185 個缺欄位，節點全部保留。
- 全量逐條核對所有 entity、方向、target、reason、分類／驗證狀態、pair 唯一與端點；固定排序再次建構得到完全相同 bytes。
- 實際 ontology.load_graph／validate_graph 通過，無驗證錯誤；另外自行檢查 CLI 未完整強制的欄位／pair 約束。
- Graph SHA256：fba52cb89f46785a56ce8e3d857ad04d591bfce2a1dada28da418449c31c5fec。
- 來源 corpus SHA256：831d9a28de20612c0ccf84c794fba862b3720fb7f422b60a19de2d145857979c（相對路徑→各檔 SHA 的 sorted canonical JSON 雜湊）。
- git diff --exit-code HEAD -- skills experiments/datasets 通過；ontology/ 內恰有使用者要求的兩個檔案。
- 初始匯入獨立 ontology_bootstrap_review（source-review／ponytail-review）ACCEPT，無必修項；全量實體／邊與 schema 核對通過。Leaf 僅靜態核對 reader 相容性，實際 load_graph／validate_graph 由主代理執行通過。

本輪交付：初始資料已驗收並通過 review，納入目前分支提交。未來完整同步器從 P0 做起，不直接重建正式圖或付費分類。

## 2026-10-26：圖分布分析筆記本

使用者追加分析與有箭頭的技能圖，隨後指定沿用 experiments/notebooks/skill_router_mo.py 的 marimo 方式，不做獨立網頁。原先 HTML 工作在寫檔前停止；本次只新增 notebook、分析 helper、相關測試及使用說明，原始 graph/schema 不改。

- Notebook：experiments/notebooks/ontology_graph_mo.py，沿用現有 uv、marimo、matplotlib、numpy、pandas，不新增依賴。
- Helper：experiments/scripts/ontology_analysis.py。依既有 create/update/delete/relate/unrelate 語義重播有效圖，再算有向入／出度、reciprocity、強弱連通與孤立技能；不把歷史操作筆數當有效邊數。
- 視覺：分布圖、熱門 incoming／outgoing、連結角色、963 節點／3,862 箭頭全圖，以及搜尋技能與方向篩選的一跳圖、原始理由表。完整資料可搜尋／分頁；只限制密集圖的名稱標籤，不截斷點或邊。
- 固定種子的 NumPy force layout 約 4 秒，獨立 cell 計算一次，方向切換不重算；位置不是語義距離，關聯數不代表品質或路由準確率。
- 實際分析：平均入／出度 4.0104；reciprocal pairs 392、其中有向邊 784（20.3004%）；弱連通 44 個、最大 920；強連通 479 個、最大 423；孤立 43。角色 both 573、incoming-only 142、outgoing-only 205。
- 強連通的 479／423 已由主代理以另一個 forward/backward reachability 演算法獨立核對，不只採信 helper 的 Kosaraju 結果。
- 分析只描述宣告結構；有幫助的多選可接受，不能由缺邊、度數或可達路徑推導是否應載入。

驗證：

- uv sync --locked 完成；8 個新增 focused tests 通過，Python 全套 107 tests 通過。
- uv run marimo check notebooks 通過。新 notebook 的 Python app 完整執行；router/vector apps 在此 worktree 缺少 ignored datasets，只驗證到既有缺資料提示，不宣稱已重跑其圖表或評測。
- 實際 marimo live kernel 全部 12 cells idle、無 cell errors；透過 code-mode 切換 aws outgoing（5）、incoming（8）、孤立 analyze（1 node／0 edges），結果與來源逐條一致，並確認全圖 layout 物件與耗時未變。最後恢復 aws／both。
- 目視檢查 live cell 實際輸出的全圖與一跳 PNG 表示；圖在 notebook 內顯示，未新增專案圖片／HTML 產物。Orca browser 已顯示摘要／分布與表格；後續 desktop browser sharing 中斷，未宣稱完成所有 viewport 或完整 browser console 無錯誤。Editor console 的既有 language-server initialization timeout 不屬於 notebook cell error。
- Node 全套未通過：既有 QMD 整合遇到 vectors_vec 表缺失及已不存在的 @wei840222/qmd@2026.10.19 dist 路徑；相關 source/tests 未修改，沒有跳過測試或改低門檻。本次不修 runtime 或重建凍結資料。
- graph.jsonl SHA 仍為 fba52cb89f46785a56ce8e3d857ad04d591bfce2a1dada28da418449c31c5fec，schema／graph 與原 repo 相同。此 worktree 缺少六個 ignored baseline，不能用它做逐檔 baseline 對比；本輪未重建它們。
- 獨立 ontology_notebook_review（source-review／ponytail-review）ACCEPT；靜態核對重播、方向、分母、圖說與測試。Live execution 及測試由主代理負責。

交付：保留本機 marimo session 供查看，README 加入開啟命令。完整增量同步器與 runtime adapter 仍是另一期工作。

## 2026-10-26：來源命名空間與移除狀態欄位

使用者核准 ID 改為 github:wei840222/omni-skills:<skill>，並明確指示這次刪除舊紀錄、直接重建 graph.jsonl；此一次性重建優先於原先 append-only 預設，舊檔仍在 Git 歷史。一般未來更新的 operation-log 語義保持不變。

- Schema 升為 version 2，改以 identity 格式與 sources map 表示多來源；不增加重複的節點／邊來源欄位。
- 重建後仍為 963 個節點、3,862 條有向邊、4,825 筆初始操作。名稱、source_path、關係類型、方向及每個 reason 均保持一致。
- 依使用者選擇，邊 properties 只保留 reason；不存分類狀態、驗證狀態或 status。所有關係仍是參考主張，不自動當執行約束。
- 分析表、圖標籤及技能選單以完整 ID 區分多來源同名技能，單一來源無歧義時仍顯示簡短名稱。選中技能同時顯示完整 ID。
- 新增無 status、多來源同名互連案例，確認不合併節點、不覆蓋下拉選項、不混淆方向，並保持舊 ontology 操作語義相容。
- 新 graph SHA256：1e9b604009589177f7191b00683ef50e3f6ee19f7d508f5a20b49389620ab790。舊 SHA 僅是上方歷史驗收紀錄，不代表目前圖檔。

驗收：10 個 focused tests、Python 全套 109 tests、marimo check 與 ontology notebook app 均通過。原生 ontology reader／schema validator 也通過。主代理逐一比對舊版節點屬性、3862 個 reason／類型／方向及所有現有 SKILL.md metadata；除了核准的 ID／狀態移除，資料完全一致。Live kernel 12 cells idle，完整讀入新 SHA 與新 ID，所有選項覆蓋 963 個 ID，並切換至 github:wei840222/omni-skills:bluetooth 驗證局部圖。獨立 ontology_identity_review（source-review／ponytail-review）ACCEPT，未發現必修問題。

本次不新增資料來源、不改正式 harness runtime，也不呼叫 embedding／rerank／分類服務。既有 QMD Node 環境問題未因此變更，也不重跑不相關的 Node 檢查。重建與 notebook 更新納入目前分支提交。
