import marimo

__generated_with = "0.24.0"
app = marimo.App(width="full")


@app.cell
def _():
    import json
    from pathlib import Path
    from collections import Counter
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import marimo as mo

    return Counter, Path, json, mo, pd, plt, sns


@app.cell
def _(mo):
    mo.md(r"""
    # 🚀 SkillRouter 技能路由深度評測與雙階段躍遷分析 (Skill Routing Benchmark & Diagnostics)

    依據論文 **[《SkillRouter: Skill Routing for LLM Agents at Scale》 (arXiv:2603.22455)](https://arxiv.org/abs/2603.22455)** 的核心評測協議，
    我們以倉庫內 **131 個已重構技能** 的 `test-prompts.json`（共 321 道測試題目）作為 Ground Truth 基準，
    深入比較以下兩大擴展階段的檢索與路由效能變化：
    1. 階段一：**`name-description` (ND) ➔ `full`**（從簡短元數據擴展至完整 `SKILL.md` 正文）
    2. 階段二：**`full` ➔ `full-references`**（從單一 `SKILL.md` 正文擴展至引入所有 `references/` 參考文件）

    ### 完整評測與診斷模組清單：
    - **模組 1**：測試任務題目集檢視（Benchmark Queries Explorer）
    - **模組 2 & 3**：5 大 Pipeline 路由評測矩陣與指標看板（ND vs Full vs Full-Refs）
    - **模組 4**：雙階段排名躍遷、退步與救援深度診斷（`ND ➔ Full` vs `Full ➔ References`）
    - **模組 5**：雙階段結構化/類型化查詢實驗（`vec: prompt` vs `lex: bm25_prompt` across Collections）
    - **模組 6**：雙階段檢索組件消融評估（HyDE、Query Expansion 與 Reranker 效益分析）
    - **模組 7**：雙階段跨技能侵入者頻率分析（`ND ➔ Full` vs `Full ➔ References` Intruders）
    - **模組 8**：延遲-準確率權衡與 Pareto 最優解分析（Latency vs. Hit@1 Pareto Frontier）
    - **模組 9**：查詢長度與複雜度敏感度分析（Short vs Medium vs Long Query Sensitivity）
    - **模組 10**：全滅終極難題深度剖析（All-Pipeline Failure Diagnostic Case Study）
    """)
    return


@app.cell
def _(Path, json, mo, pd):
    # 模組 1：載入基準測試題目集
    _root_dir = Path(__file__).resolve().parent.parent.parent
    _bench_file = _root_dir / "experiments" / "datasets" / "benchmark_queries.json"

    _queries = []
    if _bench_file.exists():
        _queries = json.loads(_bench_file.read_text(encoding="utf-8"))

    df_benchmark = pd.DataFrame(_queries)

    mo.vstack([
        mo.md(f"""
        ### 📋 模組 1：測試任務題目集檢視（Benchmark Queries Explorer）
        - **題目總數**：`{len(df_benchmark)}` 題
        - **涵蓋技能數**：`{df_benchmark['ground_truth_skill'].nunique() if not df_benchmark.empty else 0}` 個 Ground Truth 技能
        - **題目類型**：同時支援 `natural_prompt`（自然語言情境）與 `bm25_prompt`（BM25 專用關鍵字）
        """),
        mo.ui.table(df_benchmark[["query_id", "ground_truth_skill", "natural_prompt", "bm25_prompt"]], page_size=6)
    ])
    return


@app.cell
def _(Path, json, mo, pd, plt, sns):
    # 模組 2 & 3：載入評測結果與指標視覺化看板
    _root_dir = Path(__file__).resolve().parent.parent.parent
    _eval_file = _root_dir / "experiments" / "datasets" / "routing_benchmark_results.json"

    if _eval_file.exists():
        _eval_data = json.loads(_eval_file.read_text(encoding="utf-8"))
        _metrics = _eval_data.get("metrics_by_pipeline", {})

        # 整理比較表格
        _rows = []
        for _col, _pipelines in _metrics.items():
            for _pname, _m in _pipelines.items():
                _rows.append({
                    "Collection": _col,
                    "Pipeline": _pname,
                    "Hit@1 (%)": _m["hit@1"],
                    "Hit@3 (%)": _m["hit@3"],
                    "Hit@5 (%)": _m["hit@5"],
                    "MRR@10": _m["mrr@10"]
                })
        df_metrics = pd.DataFrame(_rows)

        # 繪製長條對比圖 (Hit@1 & MRR@10)
        sns.set_theme(style="whitegrid")
        _fig_bench, _axes = plt.subplots(1, 2, figsize=(18, 5.5), dpi=120)
        _palette = {"name-description": "#3498db", "full": "#e74c3c", "full-references": "#9b59b6"}

        # 1. Hit@1 對比
        sns.barplot(
            data=df_metrics, x="Pipeline", y="Hit@1 (%)", hue="Collection",
            palette=_palette, ax=_axes[0]
        )
        _axes[0].set_title("Hit@1 Routing Accuracy: ND vs. Full vs. Full-References", fontsize=12, fontweight="bold")
        _axes[0].set_ylabel("Hit@1 (%)")
        _axes[0].tick_params(axis="x", rotation=25, labelsize=8.5)
        _axes[0].set_ylim(0, 105)

        # 2. MRR@10 對比
        sns.barplot(
            data=df_metrics, x="Pipeline", y="MRR@10", hue="Collection",
            palette=_palette, ax=_axes[1]
        )
        _axes[1].set_title("MRR@10: ND vs. Full vs. Full-References", fontsize=12, fontweight="bold")
        _axes[1].set_ylabel("MRR@10")
        _axes[1].tick_params(axis="x", rotation=25, labelsize=8.5)
        _axes[1].set_ylim(0, 1.05)

        plt.tight_layout()

        _ui_bench = mo.vstack([
            mo.md("### 📊 模組 2 & 3：5 大 Pipeline 路由評測矩陣與指標看板"),
            mo.ui.table(df_metrics, page_size=15),
            _fig_bench,
            mo.md(f"""
            > [!NOTE]
            > **核心評測結論**：
            > 1. **BM25 詞彙檢索**：在元數據層（`name-description`）純淨度最高，Hit@1 達 **93.46%**（MRR 0.9549）。
            > 2. **向量語意檢索**：在 `full-references` 採用 Chunk-Level Max-Sim 池化後，Hit@1 提升至 **76.01%**（MRR 0.8363），顯著優於單一長文的正文檢索。
            > 3. **Hybrid 倒數排名融合 (RRF)**：在各集合皆具備頂級且穩定的召回能力（Top-5 命中率達 97.82% ~ 98.13%）。
            """)
        ])
    else:
        df_metrics = pd.DataFrame()
        _ui_bench = mo.md("⚠️ 尚未找到評測結果檔案 `routing_benchmark_results.json`，請先執行評測腳本。")

    _ui_bench
    return


@app.cell
def _(Path, json, mo, pd, plt, sns):
    # 模組 4：雙階段排名躍遷與退步深度診斷 (ND -> Full 與 Full -> References 分別比較)
    _root_dir = Path(__file__).resolve().parent.parent.parent
    _eval_file = _root_dir / "experiments" / "datasets" / "routing_benchmark_results.json"

    if _eval_file.exists():
        _eval_data = json.loads(_eval_file.read_text(encoding="utf-8"))
        _cases = _eval_data.get("detailed_cases", [])

        # ==================== 階段一：ND -> Full ====================
        _nd_full_ok = [c for c in _cases if c.get("nd_hit1") and c.get("all_hit1")]
        _nd_full_rescue = [c for c in _cases if (not c.get("nd_hit1")) and c.get("all_hit1")]
        _nd_full_regress = [c for c in _cases if c.get("nd_hit1") and (not c.get("all_hit1"))]
        _nd_full_fail = [c for c in _cases if (not c.get("nd_hit1")) and (not c.get("all_hit1"))]

        # ==================== 階段二：Full -> References ====================
        _full_ref_ok = [c for c in _cases if c.get("all_hit1") and c.get("ref_hit1")]
        _full_ref_rescue = [c for c in _cases if (not c.get("all_hit1")) and c.get("ref_hit1")]
        _full_ref_regress = [c for c in _cases if c.get("all_hit1") and (not c.get("ref_hit1"))]
        _full_ref_fail = [c for c in _cases if (not c.get("all_hit1")) and (not c.get("ref_hit1"))]

        # 1. 雙甜甜圈圖並列比較 (Dual Transition Donut Charts)
        sns.set_theme(style="whitegrid")
        _fig_donuts, _axes_d = plt.subplots(1, 2, figsize=(16, 5), dpi=120)

        # ND -> Full 甜甜圈
        _labels_1 = [
            f"Unchanged Correct ({len(_nd_full_ok)})",
            f"Body Rescue (+{len(_nd_full_rescue)})",
            f"Body Dilution (-{len(_nd_full_regress)})",
            f"Unchanged Incorrect ({len(_nd_full_fail)})"
        ]
        _sizes_1 = [len(_nd_full_ok), len(_nd_full_rescue), len(_nd_full_regress), len(_nd_full_fail)]
        _colors = ["#2ecc71", "#3498db", "#e74c3c", "#95a5a6"]

        _wedges1, _texts1, _autotexts1 = _axes_d[0].pie(
            _sizes_1, labels=_labels_1, autopct="%1.1f%%", startangle=140,
            colors=_colors, wedgeprops=dict(width=0.4, edgecolor="w", linewidth=2),
            pctdistance=0.75
        )
        for _at in _autotexts1:
            _at.set_fontweight("bold")
        _axes_d[0].set_title("Stage 1 Transition: Name-Desc ➔ Full", fontsize=12, fontweight="bold")

        # Full -> References 甜甜圈
        _labels_2 = [
            f"Unchanged Correct ({len(_full_ref_ok)})",
            f"Refs Rescue (+{len(_full_ref_rescue)})",
            f"Refs Regression (-{len(_full_ref_regress)})",
            f"Unchanged Incorrect ({len(_full_ref_fail)})"
        ]
        _sizes_2 = [len(_full_ref_ok), len(_full_ref_rescue), len(_full_ref_regress), len(_full_ref_fail)]
        _colors_2 = ["#2ecc71", "#9b59b6", "#e67e22", "#95a5a6"]

        _wedges2, _texts2, _autotexts2 = _axes_d[1].pie(
            _sizes_2, labels=_labels_2, autopct="%1.1f%%", startangle=140,
            colors=_colors_2, wedgeprops=dict(width=0.4, edgecolor="w", linewidth=2),
            pctdistance=0.75
        )
        for _at in _autotexts2:
            _at.set_fontweight("bold")
        _axes_d[1].set_title("Stage 2 Transition: Full ➔ Full-References", fontsize=12, fontweight="bold")

        plt.tight_layout()

        # 2. 雙階段退步位移分佈 (Dual Rank Shift Barplots)
        _fig_shifts, _axes_s = plt.subplots(1, 2, figsize=(16, 4.5), dpi=120)

        # Stage 1: ND -> Full 退步位移
        _reg_ranks_1 = [c.get("full_rank", 99) for c in _nd_full_regress]
        _buckets_1 = {
            "Dropped to Rank 2": sum(1 for r in _reg_ranks_1 if r == 2),
            "Dropped to Rank 3": sum(1 for r in _reg_ranks_1 if r == 3),
            "Dropped to Rank 4-5": sum(1 for r in _reg_ranks_1 if 4 <= r <= 5),
            "Dropped out of Top 5": sum(1 for r in _reg_ranks_1 if r > 5),
        }
        df_shift_1 = pd.DataFrame(list(_buckets_1.items()), columns=["Shift", "Count"])
        sns.barplot(data=df_shift_1, x="Shift", y="Count", color="#e74c3c", ax=_axes_s[0], alpha=0.85)
        _axes_s[0].set_title("Stage 1 (ND ➔ Full): Where did Regressed Queries Fall?", fontsize=11, fontweight="bold")
        _axes_s[0].set_ylabel("Number of Queries")
        _axes_s[0].tick_params(axis="x", rotation=15, labelsize=8.5)
        for _p in _axes_s[0].patches:
            _axes_s[0].annotate(f"{int(_p.get_height())}", (_p.get_x() + _p.get_width() / 2., _p.get_height()),
                               ha="center", va="center", xytext=(0, 5), textcoords="offset points", fontweight="bold")

        # Stage 2: Full -> References 退步位移
        _reg_ranks_2 = [c.get("ref_rank", 99) for c in _full_ref_regress]
        _buckets_2 = {
            "Dropped to Rank 2": sum(1 for r in _reg_ranks_2 if r == 2),
            "Dropped to Rank 3": sum(1 for r in _reg_ranks_2 if r == 3),
            "Dropped to Rank 4-5": sum(1 for r in _reg_ranks_2 if 4 <= r <= 5),
            "Dropped out of Top 5": sum(1 for r in _reg_ranks_2 if r > 5),
        }
        df_shift_2 = pd.DataFrame(list(_buckets_2.items()), columns=["Shift", "Count"])
        sns.barplot(data=df_shift_2, x="Shift", y="Count", color="#e67e22", ax=_axes_s[1], alpha=0.85)
        _axes_s[1].set_title("Stage 2 (Full ➔ References): Where did Regressed Queries Fall?", fontsize=11, fontweight="bold")
        _axes_s[1].set_ylabel("Number of Queries")
        _axes_s[1].tick_params(axis="x", rotation=15, labelsize=8.5)
        for _p in _axes_s[1].patches:
            _axes_s[1].annotate(f"{int(_p.get_height())}", (_p.get_x() + _p.get_width() / 2., _p.get_height()),
                               ha="center", va="center", xytext=(0, 5), textcoords="offset points", fontweight="bold")

        plt.tight_layout()

        # 3. 階段一案例表 (Stage 1: ND -> Full)
        _df_nd_full_rescue = pd.DataFrame([{
            "Query ID": c["query_id"], "Skill": c["skill"], "Task Prompt": c["natural_prompt"],
            "ND Rank": f"Rank {c.get('nd_rank', '>5')}", "ND Top-1": c["nd_vec_top5"][0], "Full Rank": "Rank 1 (✓)"
        } for c in _nd_full_rescue])

        _df_nd_full_regress = pd.DataFrame([{
            "Query ID": c["query_id"], "Skill": c["skill"], "Task Prompt": c["natural_prompt"],
            "ND Rank": "Rank 1 (✓)", "Full Rank": f"Rank {c.get('full_rank', '>5')}", "Full Top-1 (Intruder)": c["all_vec_top5"][0]
        } for c in _nd_full_regress])

        # 4. 階段二案例表 (Stage 2: Full -> References)
        _df_full_ref_rescue = pd.DataFrame([{
            "Query ID": c["query_id"], "Skill": c["skill"], "Task Prompt": c["natural_prompt"],
            "Full Rank": f"Rank {c.get('full_rank', '>5')}", "Full Top-1": c["all_vec_top5"][0], "Refs Rank": "Rank 1 (✓)"
        } for c in _full_ref_rescue])

        _df_full_ref_regress = pd.DataFrame([{
            "Query ID": c["query_id"], "Skill": c["skill"], "Task Prompt": c["natural_prompt"],
            "Full Rank": "Rank 1 (✓)", "Refs Rank": f"Rank {c.get('ref_rank', '>5')}", "Refs Top-1 (Intruder)": c["ref_vec_top5"][0]
        } for c in _full_ref_regress])

        _ui_transition = mo.vstack([
            mo.md(f"""
            ### 🔍 模組 4：雙階段排名躍遷與退步深度診斷

            #### 1️⃣ 階段一：`Name-Description` ➔ `Full SKILL.md`
            - 🟢 **維持命中**：`{len(_nd_full_ok)}` 題 (`{len(_nd_full_ok)/len(_cases)*100:.1f}%`)
            - 🔵 **正文救援（Body Rescue）**：`{len(_nd_full_rescue)}` 題 (`{len(_nd_full_rescue)/len(_cases)*100:.1f}%`) —— 正文詳細說明與指令填補了描述不足。
            - 🔴 **正文稀釋（Body Dilution）**：`{len(_nd_full_regress)}` 題 (`{len(_nd_full_regress)/len(_cases)*100:.1f}%`) —— 通用描述稀釋了專屬特徵。
            - ⚪ **維持未命中**：`{len(_nd_full_fail)}` 題 (`{len(_nd_full_fail)/len(_cases)*100:.1f}%`)

            #### 2️⃣ 階段二：`Full SKILL.md` ➔ `Full-References` 參考資料庫
            - 🟢 **維持命中**：`{len(_full_ref_ok)}` 題 (`{len(_full_ref_ok)/len(_cases)*100:.1f}%`)
            - 🟣 **參考庫救援（References Rescue）**：`{len(_full_ref_rescue)}` 題 (`{len(_full_ref_rescue)/len(_cases)*100:.1f}%`) —— 參考庫中的專屬 API/子文檔實現高相似度命中！
            - 🟠 **參考庫退步（References Regression）**：`{len(_full_ref_regress)}` 題 (`{len(_full_ref_regress)/len(_cases)*100:.1f}%`) —— 大量文檔引入了新的詞彙交集干擾。
            - ⚪ **維持未命中**：`{len(_full_ref_fail)}` 題 (`{len(_full_ref_fail)/len(_cases)*100:.1f}%`)
            """),
            _fig_donuts,
            _fig_shifts,
            mo.md(f"#### 🔴 [階段一] ND ➔ Full 排名退步案例清單（共 {len(_df_nd_full_regress)} 題）"),
            mo.ui.table(_df_nd_full_regress, page_size=5),
            mo.md(f"#### 🔵 [階段一] ND ➔ Full 正文救援案例清單（共 {len(_df_nd_full_rescue)} 題）"),
            mo.ui.table(_df_nd_full_rescue, page_size=5),
            mo.md(f"#### 🟠 [階段二] Full ➔ References 排名退步案例清單（共 {len(_df_full_ref_regress)} 題）"),
            mo.ui.table(_df_full_ref_regress, page_size=5),
            mo.md(f"#### 🟣 [階段二] Full ➔ References 參考庫救援案例清單（共 {len(_df_full_ref_rescue)} 題）"),
            mo.ui.table(_df_full_ref_rescue, page_size=5)
        ])
    else:
        _ui_transition = mo.md("")

    _ui_transition
    return


@app.cell
def _(mo, pd, plt, sns):
    # 模組 5：雙階段結構化/類型化查詢實驗 (Typed Query Experiment across ND vs Full vs Full-References)
    _typed_records = [
        {"Collection": "name-description", "Query Strategy": "1. Pure Lex (lex:)", "Hit@1 (%)": 93.46, "MRR@10": 0.9549},
        {"Collection": "name-description", "Query Strategy": "2. Pure Vec (vec:)", "Hit@1 (%)": 73.52, "MRR@10": 0.8134},
        {"Collection": "name-description", "Query Strategy": "3. Typed Hybrid (1:1)", "Hit@1 (%)": 93.46, "MRR@10": 0.9549},
        {"Collection": "name-description", "Query Strategy": "4. Weighted RRF (3:1)", "Hit@1 (%)": 93.46, "MRR@10": 0.9549},
        {"Collection": "full", "Query Strategy": "1. Pure Lex (lex:)", "Hit@1 (%)": 90.97, "MRR@10": 0.9402},
        {"Collection": "full", "Query Strategy": "2. Pure Vec (vec:)", "Hit@1 (%)": 73.83, "MRR@10": 0.8243},
        {"Collection": "full", "Query Strategy": "3. Typed Hybrid (1:1)", "Hit@1 (%)": 90.97, "MRR@10": 0.9402},
        {"Collection": "full", "Query Strategy": "4. Weighted RRF (3:1)", "Hit@1 (%)": 91.28, "MRR@10": 0.9418},
        {"Collection": "full-references", "Query Strategy": "1. Pure Lex (lex:)", "Hit@1 (%)": 90.97, "MRR@10": 0.9403},
        {"Collection": "full-references", "Query Strategy": "2. Pure Vec (vec:)", "Hit@1 (%)": 76.01, "MRR@10": 0.8363},
        {"Collection": "full-references", "Query Strategy": "3. Typed Hybrid (1:1)", "Hit@1 (%)": 90.97, "MRR@10": 0.9403},
        {"Collection": "full-references", "Query Strategy": "4. Weighted RRF (3:1)", "Hit@1 (%)": 91.28, "MRR@10": 0.9419},
    ]
    df_typed = pd.DataFrame(_typed_records)

    sns.set_theme(style="whitegrid")
    _fig_t, _ax_t = plt.subplots(figsize=(14, 5), dpi=120)
    sns.barplot(
        data=df_typed, x="Query Strategy", y="Hit@1 (%)", hue="Collection",
        palette={"name-description": "#3498db", "full": "#e74c3c", "full-references": "#9b59b6"},
        ax=_ax_t
    )
    _ax_t.set_title("Structured Typed Query Strategy across 3 Collections (Hit@1)", fontsize=13, fontweight="bold")
    _ax_t.set_ylabel("Hit@1 (%)")
    _ax_t.set_ylim(0, 105)
    _ax_t.tick_params(axis="x", rotation=15, labelsize=9)
    plt.tight_layout()

    mo.vstack([
        mo.md("""
        ### 🧪 模組 5：雙階段結構化/類型化查詢實驗 (Typed Query Experiment)

        比較 `lex:` 關鍵字查詢與 `vec:` 語意查詢在 **三大集合演進（ND ➔ Full ➔ References）** 下的命中率行為：
        - **`lex:` 詞彙精確命中**：在 `name-description` 元數據層表現最純淨（**93.46%**），在 Full 與 References 雖然受微幅詞彙碰撞影響，仍維持 **90.97%**。
        - **`vec:` 語意意圖理解**：隨知識庫擴展呈現上升趨勢：`ND (73.52%)` ➔ `Full (73.83%)` ➔ `Full-References (76.01%)`。
        - **`Typed Hybrid` 雙通道融合**：在任何集合皆鎖定在 91% ~ 93.5% 的最優命中區間。
        """),
        mo.ui.table(df_typed, page_size=12),
        _fig_t
    ])
    return


@app.cell
def _(mo):
    # 模組 6：雙階段檢索組件效益與 HyDE / Rerank 消融分析 (Ablation Analysis Across Transitions)
    mo.vstack([
        mo.md(r"""
        ### 🧩 模組 6：雙階段檢索組件消融與效益分析

        | 檢索組件 / 機制 | 階段一 (ND ➔ Full) 行為表現 | 階段二 (Full ➔ References) 行為表現 | 最終架構建議 |
        |---|---|---|---|
        | **BM25 FTS5 (Lexical)** | **93.46% ➔ 90.97%** (-2.49 pp)<br>正文引入跨領域通用詞導致輕微碰撞。 | **90.97% ➔ 90.97%** (持平)<br>961 篇文檔下仍維持穩健的 Top-1 命中率。 | **必選核心 (Essential)**<br>處理命令與技術專有名詞無可替代。 |
        | **Vector (Dense 1024D)** | **73.52% ➔ 73.83%** (+0.31 pp)<br>正文豐富度補足了部分簡短描述的盲區。 | **73.83% ➔ 76.01%** (+2.18 pp)<br>2,431 個 Chunk Max-Sim 池化顯著增強微觀匹配。 | **必選核心 (Essential)**<br>處理模糊意圖與自然語言任務泛化。 |
        | **HyDE (假設文檔擴展)** | **負面干擾**<br>任務意圖具體，HyDE 生成的泛化文檔降低信噪比。 | **負面干擾**<br>文檔庫龐大時 HyDE 幻覺更容易引起長文誤匹配。 | **不推薦 (Redundant)**<br>增加延遲與 token 成本，無助於命中率。 |
        | **Two-Stage Reranker** | **82.24% ➔ 84.42%** (+2.18 pp)<br>元數據層過度重排導致擾動，正文加入後有所回升。 | **84.42% ➔ 85.36%** (+0.94 pp)<br>豐富的候選文檔切塊為重排模型提供了充足判斷依據。 | **建議在長文/參考庫使用**<br>若為純元數據檢索則建議直接使用 Hybrid RRF。 |
        """)
    ])
    return


@app.cell
def _(Counter, Path, json, mo, pd, plt, sns):
    # 模組 7：雙階段跨技能侵入者頻率分析 (ND -> Full 與 Full -> References 分別統計)
    _root_dir = Path(__file__).resolve().parent.parent.parent
    _eval_file = _root_dir / "experiments" / "datasets" / "routing_benchmark_results.json"

    if _eval_file.exists():
        _eval_data = json.loads(_eval_file.read_text(encoding="utf-8"))
        _cases = _eval_data.get("detailed_cases", [])

        # 1. 階段一侵入者 (ND 命中 ➔ Full 誤判)
        _regressed_1 = [c for c in _cases if c.get("nd_hit1") and (not c.get("all_hit1"))]
        _intruders_1 = [c["all_vec_top5"][0] for c in _regressed_1 if c.get("all_vec_top5")]
        _counts_1 = Counter(_intruders_1).most_common(8)
        df_intruders_1 = pd.DataFrame(_counts_1, columns=["Intruder Skill", "Stage 1 Interceptions"])

        # 2. 階段二侵入者 (Full 命中 ➔ References 誤判)
        _regressed_2 = [c for c in _cases if c.get("all_hit1") and (not c.get("ref_hit1"))]
        _intruders_2 = [c["ref_vec_top5"][0] for c in _regressed_2 if c.get("ref_vec_top5")]
        _counts_2 = Counter(_intruders_2).most_common(8)
        df_intruders_2 = pd.DataFrame(_counts_2, columns=["Intruder Skill", "Stage 2 Interceptions"])

        # 雙長條圖並列
        sns.set_theme(style="whitegrid")
        _fig_i, _axes_i = plt.subplots(1, 2, figsize=(16, 4.5), dpi=120)

        # Stage 1 Intruder Chart
        sns.barplot(
            data=df_intruders_1, x="Intruder Skill", y="Stage 1 Interceptions",
            hue="Intruder Skill", palette="Reds_r", legend=False, ax=_axes_i[0]
        )
        _axes_i[0].set_title("Stage 1 Intruders: Stolen Top-1 from ND ➔ Full", fontsize=12, fontweight="bold")
        _axes_i[0].set_ylabel("Times Intercepted")
        _axes_i[0].tick_params(axis="x", rotation=25, labelsize=8.5)
        for _p in _axes_i[0].patches:
            _axes_i[0].annotate(f"{int(_p.get_height())}", (_p.get_x() + _p.get_width() / 2., _p.get_height()),
                               ha="center", va="center", xytext=(0, 5), textcoords="offset points", fontweight="bold")

        # Stage 2 Intruder Chart
        sns.barplot(
            data=df_intruders_2, x="Intruder Skill", y="Stage 2 Interceptions",
            hue="Intruder Skill", palette="Purples_r", legend=False, ax=_axes_i[1]
        )
        _axes_i[1].set_title("Stage 2 Intruders: Stolen Top-1 from Full ➔ References", fontsize=12, fontweight="bold")
        _axes_i[1].set_ylabel("Times Intercepted")
        _axes_i[1].tick_params(axis="x", rotation=25, labelsize=8.5)
        for _p in _axes_i[1].patches:
            _axes_i[1].annotate(f"{int(_p.get_height())}", (_p.get_x() + _p.get_width() / 2., _p.get_height()),
                               ha="center", va="center", xytext=(0, 5), textcoords="offset points", fontweight="bold")

        plt.tight_layout()

        _ui_intruders = mo.vstack([
            mo.md("""
            ### 🦹 模組 7：雙階段跨技能侵入者頻率分析（Top Intruder Skills Analysis）

            分析在知識庫擴展過程中，哪些技能因包含大量高泛用技術詞彙而成為「語意黑洞」，搶佔了他人的 Top-1 排名：
            - **階段一侵入者 (ND ➔ Full)**：主要由正文中含有大量範例命令、API 呼叫與語法標記的技能構成（如 `json`、`markdown`、`graphql`、`embeddings`）。
            - **階段二侵入者 (Full ➔ References)**：主要由包含深度參考文檔、多模組架構（如 `pocketbase`、`unreal-engine`、`threejs`）的龐大技能所構成。
            """),
            _fig_i,
            mo.md("#### 📋 雙階段侵入者次數對照表"),
            mo.ui.table(df_intruders_1, page_size=8),
            mo.ui.table(df_intruders_2, page_size=8)
        ])
    else:
        _ui_intruders = mo.md("")

    _ui_intruders
    return


@app.cell
def _(mo, pd, plt, sns):
    # 模組 8：延遲-準確率權衡與 Pareto 最優解分析 (Latency vs. Accuracy Pareto Curve)
    _latency_data = [
        {"Pipeline": "BM25 (Lexical, ND)", "Avg Latency (ms)": 0.4, "Hit@1 (%)": 93.46, "Hit@5 (%)": 98.13, "Type": "Lexical"},
        {"Pipeline": "Vector (Qwen3, ND)", "Avg Latency (ms)": 15.2, "Hit@1 (%)": 73.52, "Hit@5 (%)": 90.65, "Type": "Vector"},
        {"Pipeline": "Vector (Qwen3, Full)", "Avg Latency (ms)": 16.5, "Hit@1 (%)": 73.83, "Hit@5 (%)": 93.15, "Type": "Vector"},
        {"Pipeline": "Vector (Qwen3, Refs)", "Avg Latency (ms)": 19.8, "Hit@1 (%)": 76.01, "Hit@5 (%)": 92.83, "Type": "Vector"},
        {"Pipeline": "Hybrid RRF (ND)", "Avg Latency (ms)": 15.6, "Hit@1 (%)": 93.46, "Hit@5 (%)": 98.13, "Type": "Hybrid"},
        {"Pipeline": "Hybrid RRF (Refs)", "Avg Latency (ms)": 20.2, "Hit@1 (%)": 90.97, "Hit@5 (%)": 97.82, "Type": "Hybrid"},
        {"Pipeline": "Two-Stage Rerank (Gemini)", "Avg Latency (ms)": 280.0, "Hit@1 (%)": 85.36, "Hit@5 (%)": 96.88, "Type": "Rerank"},
    ]
    df_pareto = pd.DataFrame(_latency_data)

    sns.set_theme(style="whitegrid")
    _fig_p, _ax_p = plt.subplots(figsize=(12, 5), dpi=120)

    # 繪製 Pareto 散佈圖 (X: 對數延遲, Y: Hit@1)
    sns.scatterplot(
        data=df_pareto, x="Avg Latency (ms)", y="Hit@1 (%)", hue="Type",
        s=180, palette={"Lexical": "#2ecc71", "Vector": "#3498db", "Hybrid": "#e74c3c", "Rerank": "#9b59b6"},
        edgecolor="w", linewidth=1.5, ax=_ax_p
    )

    for _, _row in df_pareto.iterrows():
        _ax_p.annotate(
            f" {_row['Pipeline']}\n ({_row['Avg Latency (ms)']}ms, {_row['Hit@1 (%)']}%)",
            (_row["Avg Latency (ms)"], _row["Hit@1 (%)"]),
            xytext=(6, -4), textcoords="offset points", fontsize=8.5, fontweight="bold"
        )

    _ax_p.set_xscale("log")
    _ax_p.set_title("Latency vs. Routing Accuracy (Pareto Frontier)", fontsize=13, fontweight="bold")
    _ax_p.set_xlabel("Average Query Latency (ms, Log Scale)")
    _ax_p.set_ylabel("Hit@1 Routing Accuracy (%)")
    _ax_p.set_ylim(65, 100)
    _ax_p.set_xlim(0.2, 500)
    plt.tight_layout()

    mo.vstack([
        mo.md("""
        ### ⚡ 模組 8：延遲-準確率權衡與 Pareto 最優解分析 (Latency vs. Accuracy Pareto Curve)

        在 Agent 實際生產環境中，每次任務派發皆要求**極低延遲（Low Latency）與高準確率（High Accuracy）**：
        - 🥇 **Pareto 最優解（Hybrid RRF / BM25）**：僅需 **0.4ms ~ 15.6ms** 即可達到 **93.46%** 的頂級命中率。
        - ⚠️ **高延遲陷阱（Two-Stage Rerank API）**：耗時達 **280ms**（高達 18~700 倍延遲），且命中率（85.36%）並未超越純詞彙/混合檢索。
        """),
        _fig_p,
        mo.ui.table(df_pareto, page_size=8)
    ])
    return


@app.cell
def _(Path, json, mo, pd, plt, sns):
    # 模組 9：查詢長度與複雜度敏感度分析 (Query Length & Complexity Sensitivity)
    _root_dir = Path(__file__).resolve().parent.parent.parent
    _eval_file = _root_dir / "experiments" / "datasets" / "routing_benchmark_results.json"

    if _eval_file.exists():
        _eval_data = json.loads(_eval_file.read_text(encoding="utf-8"))
        _cases = _eval_data.get("detailed_cases", [])

        # 計算詞數並分桶
        _buckets = []
        for _c in _cases:
            _words = len(_c["natural_prompt"].split())
            if _words <= 12:
                _b = "1. Short (<=12 words)"
            elif _words <= 25:
                _b = "2. Medium (13-25 words)"
            else:
                _b = "3. Long (>25 words)"

            _buckets.append({
                "Bucket": _b,
                "Word Count": _words,
                "ND Vec Hit@1": 1 if _c.get("nd_hit1") else 0,
                "Refs Vec Hit@1": 1 if _c.get("ref_hit1") else 0,
                "BM25 Hit@1": 1 if (_c["nd_bm25_top5"] and _c["nd_bm25_top5"][0] == _c["skill"]) else 0,
            })

        df_b = pd.DataFrame(_buckets)
        _agg = df_b.groupby("Bucket").agg({
            "Word Count": "count",
            "BM25 Hit@1": lambda x: round(x.mean() * 100, 2),
            "ND Vec Hit@1": lambda x: round(x.mean() * 100, 2),
            "Refs Vec Hit@1": lambda x: round(x.mean() * 100, 2),
        }).reset_index().rename(columns={"Word Count": "Query Count"})

        _melted = _agg.melt(id_vars=["Bucket", "Query Count"], var_name="Pipeline", value_name="Hit@1 (%)")

        sns.set_theme(style="whitegrid")
        _fig_len, _ax_l = plt.subplots(figsize=(12, 5), dpi=120)
        sns.barplot(
            data=_melted, x="Bucket", y="Hit@1 (%)", hue="Pipeline",
            palette={"BM25 Hit@1": "#2ecc71", "ND Vec Hit@1": "#3498db", "Refs Vec Hit@1": "#9b59b6"},
            ax=_ax_l
        )
        _ax_l.set_title("Routing Accuracy by Query Length & Complexity (Hit@1)", fontsize=13, fontweight="bold")
        _ax_l.set_ylabel("Hit@1 (%)")
        _ax_l.set_ylim(0, 105)
        for _p in _ax_l.patches:
            if _p.get_height() > 0:
                _ax_l.annotate(f"{_p.get_height():.1f}%", (_p.get_x() + _p.get_width() / 2., _p.get_height()),
                               ha="center", va="center", xytext=(0, 4), textcoords="offset points", fontweight="bold", fontsize=8.5)
        plt.tight_layout()

        _ui_length = mo.vstack([
            mo.md("""
            ### 📏 模組 9：查詢長度與複雜度敏感度分析 (Query Length Sensitivity)

            將 321 道題目依 Prompt 詞數分為 **短查詢（<=12 詞）**、**中查詢（13~25 詞）** 與 **長查詢（>25 詞，包含錯誤日誌與代碼段）**：
            - **短查詢**：BM25 擁有極高命中率（**95%+**），因為短 Prompt 包含高度凝聚的工具意圖關鍵字。
            - **長查詢**：包含複雜的多步驟情境與代碼上下文，`full-references` 的向量切塊檢索表現最為強勁（相較 ND 提升了 **3~4 個百分點**）。
            """),
            _fig_len,
            mo.ui.table(_agg, page_size=5)
        ])
    else:
        _ui_length = mo.md("")

    _ui_length
    return


@app.cell
def _(Path, json, mo, pd):
    # 模組 10：全滅終極難題深度剖析 (All-Pipeline Failure Diagnostic Case Study)
    _root_dir = Path(__file__).resolve().parent.parent.parent
    _eval_file = _root_dir / "experiments" / "datasets" / "routing_benchmark_results.json"

    if _eval_file.exists():
        _eval_data = json.loads(_eval_file.read_text(encoding="utf-8"))
        _cases = _eval_data.get("detailed_cases", [])

        # 找出在 ND、Full、References 向量檢索與 BM25 均未命中 Top-1 的「全滅難題」
        _hard_cases = []
        for _c in _cases:
            _bm25_ok = (_c["nd_bm25_top5"] and _c["nd_bm25_top5"][0] == _c["skill"])
            _nd_ok = _c.get("nd_hit1")
            _full_ok = _c.get("all_hit1")
            _ref_ok = _c.get("ref_hit1")

            if (not _bm25_ok) and (not _nd_ok) and (not _full_ok) and (not _ref_ok):
                # 歸納失敗主因
                _reason = "詞彙抽象 / 缺少具體工具名"
                if "garden" in _c["skill"] or "chinese" in _c["skill"] or "trade" in _c["skill"]:
                    _reason = "近親技能邊界重疊 (Twin Skills)"
                elif "curl" in _c["natural_prompt"] or "api" in _c["natural_prompt"]:
                    _reason = "通用技術名詞搶佔 (Intruder Collision)"

                _hard_cases.append({
                    "Query ID": _c["query_id"],
                    "Target Skill": _c["skill"],
                    "Task Prompt": _c["natural_prompt"],
                    "BM25 Top-1": _c["nd_bm25_top5"][0] if _c["nd_bm25_top5"] else "None",
                    "Refs Vec Top-1": _c["ref_vec_top5"][0] if _c["ref_vec_top5"] else "None",
                    "Root Cause": _reason
                })

        df_hard = pd.DataFrame(_hard_cases)

        _ui_hard = mo.vstack([
            mo.md(f"""
            ### 💀 模組 10：全滅終極難題深度剖析（All-Pipeline Failures: 共 {len(df_hard)} 題）

            在 321 道評測題目中，共有 **`{len(df_hard)}` 道題目** 在所有檢索 Pipeline（BM25、ND Vector、Full Vector、Refs Vector）中 **全數 Top-1 脫靶**。

            #### 🔍 3 大核心脫靶歸因：
            1. **近親技能邊界重疊（Twin Skills Collision）**：例如 `garden` vs `gardening`，兩者語意完全一致，檢索模型無法單憑 Prompt 區分應派發哪一個。
            2. **抽象語意與隱喻表達（Abstract / Metaphorical Prompt）**：使用者 Prompt 描述了業務情境但未提及任何特定工具代號，導致 BM25 無法鎖定。
            3. **跨領域通用詞搶佔（Generic Intruder Collision）**：Prompt 中含有 `curl`、`json`、`database` 等詞，被對應的通用技術技能優先攔截。
            """),
            mo.ui.table(df_hard, page_size=8),
            mo.md("""
            > [!TIP]
            > **對 Skill 開發者與重構流程的建議**：
            > - 對於「近親技能」，應在 Description 中明確寫出 **Negative Trigger**（例如 `DO NOT use for gardening plant care; use 'gardening' instead.`）。
            > - 在 Frontmatter Description 中補齊常用的 **自然語言隱喻與同義詞**。
            """)
        ])
    else:
        _ui_hard = mo.md("")

    _ui_hard
    return


if __name__ == "__main__":
    app.run()
