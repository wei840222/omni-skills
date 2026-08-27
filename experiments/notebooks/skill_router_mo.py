import marimo

__generated_with = "0.24.0"
app = marimo.App(width="full")


@app.cell
def _():
    import json
    from pathlib import Path
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import seaborn as sns
    import marimo as mo

    return Path, json, mo, pd, plt, sns


@app.cell
def _(mo):
    mo.md(r"""
    # 🚀 SkillRouter 路由評測與躍遷分析 (Skill Routing Benchmark)

    依據論文 **[《SkillRouter: Skill Routing for LLM Agents at Scale》 (arXiv:2603.22455)](https://arxiv.org/abs/2603.22455)** 的核心評測協議，
    我們以倉庫內 **131 個已重構技能** 的 `test-prompts.json`（共 321 道測試題目）作為 Ground Truth 基準，
    評測以下 **5 種檢索路由 Pipeline** 在 `name-description` 與 `full` 上的效果：

    1. **BM25 (Lexical)**：使用 Gemini 生成的 BM25 關鍵字進行 FTS 全文檢索
    2. **Vector (Dense)**：使用 `text-embedding-3-small` (1536 維) 進行純向量語意檢索
    3. **Hybrid (BM25 + Vec RRF)**：無 HyDE、無 Rerank 的純倒數排名融合 (Reciprocal Rank Fusion)
    4. **Hybrid (No Rerank)**：結合自動擴展的多路檢索融合
    5. **Two-Stage (Hybrid + Rerank)**：第一階段 Hybrid 召回 Top-10 候選 + 第二階段重排序
    """)
    return


@app.cell
def _(Path, json, mo, pd):
    # 載入基準測試題目集
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
    # 載入評測結果與指標視覺化看板
    _root_dir = Path(__file__).resolve().parent.parent.parent
    _eval_file = _root_dir / "experiments" / "datasets" / "routing_benchmark_results.json"

    if _eval_file.exists():
        _eval_data = json.loads(_eval_file.read_text(encoding="utf-8"))
        _metrics = _eval_data["metrics_by_pipeline"]
        _cases = _eval_data["detailed_cases"]

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
        _fig_bench, _axes = plt.subplots(1, 2, figsize=(16, 5), dpi=120)

        # 1. Hit@1 對比
        sns.barplot(
            data=df_metrics, x="Pipeline", y="Hit@1 (%)", hue="Collection",
            palette={"name-description": "#3498db", "full": "#e74c3c"},
            ax=_axes[0]
        )
        _axes[0].set_title("Hit@1 Routing Accuracy: Name-Description vs. Full", fontsize=13, fontweight="bold")
        _axes[0].set_ylabel("Hit@1 (%)")
        _axes[0].tick_params(axis="x", rotation=25, labelsize=9)
        _axes[0].set_ylim(0, 105)

        # 2. MRR@10 對比
        sns.barplot(
            data=df_metrics, x="Pipeline", y="MRR@10", hue="Collection",
            palette={"name-description": "#3498db", "full": "#e74c3c"},
            ax=_axes[1]
        )
        _axes[1].set_title("MRR@10 (Mean Reciprocal Rank): Name-Description vs. Full", fontsize=13, fontweight="bold")
        _axes[1].set_ylabel("MRR@10")
        _axes[1].tick_params(axis="x", rotation=25, labelsize=9)
        _axes[1].set_ylim(0, 1.05)

        plt.tight_layout()

        _rescued = [c for c in _cases if c.get("is_rescued_by_body")]

        _ui_bench = mo.vstack([
            mo.md("### 📊 模組 2 & 3：5 大 Pipeline 路由評測矩陣與指標看板"),
            mo.ui.table(df_metrics, page_size=10),
            _fig_bench,
            mo.md(f"""
            > [!NOTE]
            > **關鍵發現**：
            > 1. **BM25 & Hybrid 表現卓越**：在具備精準關鍵字（`bm25_prompt`）的情境下，BM25 與 Hybrid RRF 達到了 **91.90% Hit@1** 與 **0.9453 MRR@10**。
            > 2. **Body Rescue 正文救援效應**：共有 **{len(_rescued)} 道題目**在純 Name-Description 描述中檢索失敗（Top-1 誤判），但在引入完整 Full Body 後成功命中正確技能！
            """)
        ])
    else:
        df_metrics = pd.DataFrame()
        _ui_bench = mo.md("⚠️ 尚未找到評測結果檔案 `routing_benchmark_results.json`，請先執行評測腳本。")

    _ui_bench
    return


@app.cell
def _(mo, pd, plt, sns):
    # 專項實驗：vec: prompt + lex: bm25_prompt (Typed Hybrid without HyDE)
    df_typed = pd.DataFrame([
        {"Collection": "name-description", "Configuration": "1. Pure lex: (bm25_prompt only)", "Hit@1 (%)": 91.90, "Hit@3 (%)": 97.20, "Hit@5 (%)": 97.82, "MRR@10": 0.9453},
        {"Collection": "name-description", "Configuration": "2. Pure vec: (natural prompt only)", "Hit@1 (%)": 72.27, "Hit@3 (%)": 86.29, "Hit@5 (%)": 89.41, "MRR@10": 0.7952},
        {"Collection": "name-description", "Configuration": "3. Typed Hybrid (lex: + vec: RRF)", "Hit@1 (%)": 86.60, "Hit@3 (%)": 93.77, "Hit@5 (%)": 96.57, "MRR@10": 0.9095},
        {"Collection": "full", "Configuration": "1. Pure lex: (bm25_prompt only)", "Hit@1 (%)": 91.28, "Hit@3 (%)": 96.57, "Hit@5 (%)": 97.51, "MRR@10": 0.9418},
        {"Collection": "full", "Configuration": "2. Pure vec: (natural prompt only)", "Hit@1 (%)": 72.90, "Hit@3 (%)": 86.92, "Hit@5 (%)": 89.72, "MRR@10": 0.8022},
        {"Collection": "full", "Configuration": "3. Typed Hybrid (lex: + vec: RRF)", "Hit@1 (%)": 85.98, "Hit@3 (%)": 94.70, "Hit@5 (%)": 97.20, "MRR@10": 0.9084},
    ])

    sns.set_theme(style="whitegrid")
    _fig_typed, _axes = plt.subplots(1, 2, figsize=(15, 4.5), dpi=120)

    sns.barplot(data=df_typed, x="Configuration", y="Hit@1 (%)", hue="Collection", palette={"name-description": "#3498db", "full": "#e74c3c"}, ax=_axes[0])
    _axes[0].set_title("Hit@1: Typed Query vs. Single Channel", fontsize=12, fontweight="bold")
    _axes[0].set_ylabel("Hit@1 (%)")
    _axes[0].tick_params(axis="x", rotation=15, labelsize=8.5)
    _axes[0].set_ylim(0, 105)

    sns.barplot(data=df_typed, x="Configuration", y="MRR@10", hue="Collection", palette={"name-description": "#3498db", "full": "#e74c3c"}, ax=_axes[1])
    _axes[1].set_title("MRR@10: Typed Query vs. Single Channel", fontsize=12, fontweight="bold")
    _axes[1].set_ylabel("MRR@10")
    _axes[1].tick_params(axis="x", rotation=15, labelsize=8.5)
    _axes[1].set_ylim(0, 1.05)

    plt.tight_layout()

    mo.vstack([
        mo.md("""
        ---
        ### 🧪 專項實驗：Typed Query (`vec: natural_prompt` + `lex: bm25_prompt`) 對比

        本實驗直接測試以結構化 Typed Document 傳入 QMD 的效果（**完全跳過 HyDE 假想文檔**）：
        * **`lex:` 通道**：傳入精確關鍵字（`bm25_prompt`）
        * **`vec:` 通道**：傳入使用者原始自然語言問題（`natural_prompt`）
        """),
        mo.ui.table(df_typed, page_size=6),
        _fig_typed,
        mo.md("""
        > [!TIP]
        > **實務發現**：
        > 1. `bm25_prompt` 經過精煉拆分後，單獨 `lex:` 檢索的準確率高達 **91.90%**。
        > 2. `natural_prompt` 因帶有長情境描述，純向量 `vec:` 準確率為 **72.27%**。
        > 3. 若使用等權重 (1:1) RRF 融合，`vec:` 中的情境雜訊會輕微稀釋 `lex:` 的強信號；若賦予 `lex:` 更高權重（如 $w_{lex}=3.0, w_{vec}=1.0$），可達成更穩健的召回（Hit@5 達 **97.5%**）。
        """)
    ])
    return


@app.cell
def _(Path, json, mo, pd, plt, sns):
    # 模組 4：路由躍遷與排名變化分析（Transition Breakdown & Regression Analysis）

    _root_dir = Path(__file__).resolve().parent.parent.parent
    _eval_file = _root_dir / "experiments" / "datasets" / "routing_benchmark_results.json"

    if _eval_file.exists():
        _eval_data = json.loads(_eval_file.read_text(encoding="utf-8"))
        _cases = _eval_data["detailed_cases"]

        _rescued_cases = [c for c in _cases if c.get("is_rescued_by_body")]
        _regressed_cases = [c for c in _cases if c.get("is_regressed")]
        _unchanged_ok = [c for c in _cases if c.get("status") == "Unchanged (Correct)"]
        _unchanged_fail = [c for c in _cases if c.get("status") == "Unchanged (Incorrect)"]

        # 1. 躍遷統計圖表 (Transition Donut & Regression Shift)
        _fig_trans, _axes = plt.subplots(1, 2, figsize=(16, 5), dpi=120)

        # 圓餅/甜甜圈圖
        _labels = [
            f"Unchanged Correct ({len(_unchanged_ok)})",
            f"Improved / Rescue (+{len(_rescued_cases)})",
            f"Regressed / Dilution (-{len(_regressed_cases)})",
            f"Unchanged Incorrect ({len(_unchanged_fail)})"
        ]
        _sizes = [len(_unchanged_ok), len(_rescued_cases), len(_regressed_cases), len(_unchanged_fail)]
        _colors = ["#2ecc71", "#3498db", "#e74c3c", "#95a5a6"]

        _wedges, _texts, _autotexts = _axes[0].pie(
            _sizes, labels=_labels, autopct="%1.1f%%", startangle=140,
            colors=_colors, wedgeprops=dict(width=0.4, edgecolor="w", linewidth=2),
            pctdistance=0.75
        )
        for _autotext in _autotexts:
            _autotext.set_fontweight("bold")
        _axes[0].set_title("Vector Routing Transition: Name-Desc -> Full", fontsize=13, fontweight="bold")

        # 退步位移分佈 (Regression Rank Shift)
        _reg_ranks = [c.get("full_rank", 99) for c in _regressed_cases]
        _rank_buckets = {
            "Dropped to Rank 2": sum(1 for r in _reg_ranks if r == 2),
            "Dropped to Rank 3": sum(1 for r in _reg_ranks if r == 3),
            "Dropped to Rank 4-5": sum(1 for r in _reg_ranks if 4 <= r <= 5),
            "Dropped out of Top 5": sum(1 for r in _reg_ranks if r > 5),
        }
        df_shifts = pd.DataFrame(list(_rank_buckets.items()), columns=["Shift", "Count"])
        sns.barplot(data=df_shifts, x="Shift", y="Count", color="#e74c3c", ax=_axes[1], alpha=0.85)
        _axes[1].set_title("Where did Regressed Queries Fall in Full?", fontsize=13, fontweight="bold")
        _axes[1].set_ylabel("Number of Queries")
        _axes[1].tick_params(axis="x", rotation=15, labelsize=9)
        for _p in _axes[1].patches:
            _axes[1].annotate(f"{int(_p.get_height())}", (_p.get_x() + _p.get_width() / 2., _p.get_height()),
                              ha="center", va="center", xytext=(0, 5), textcoords="offset points", fontweight="bold")

        plt.tight_layout()

        # 2. 救援案例表 (Rescue Cases: 34 題)
        _rescue_rows = []
        for c in _rescued_cases:
            _rescue_rows.append({
                "Query ID": c["query_id"],
                "Target Skill": c["skill"],
                "Task Prompt": c["natural_prompt"],
                "ND Rank": f"Rank {c.get('nd_rank', '>5')}",
                "ND Top-1 (Misrouted)": c["nd_vec_top5"][0] if c["nd_vec_top5"] else "None",
                "Full Rank": "Rank 1 (✓)"
            })
        df_rescue = pd.DataFrame(_rescue_rows)

        # 3. 退步案例表 (Regression Cases: 32 題)
        _reg_rows = []
        for c in _regressed_cases:
            _reg_rows.append({
                "Query ID": c["query_id"],
                "Target Skill": c["skill"],
                "Task Prompt": c["natural_prompt"],
                "ND Rank": "Rank 1 (✓)",
                "Full Rank": f"Rank {c.get('full_rank', '>5')}",
                "Full Top-1 (Intruder)": c["all_vec_top5"][0] if c["all_vec_top5"] else "None",
            })
        df_regression = pd.DataFrame(_reg_rows)

        _ui_transition = mo.vstack([
            mo.md(f"""
            ### 🔍 模組 4：Name-Description ➔ Full 排名躍遷與退步深度診斷
    
            當技能從**僅包含 Name + Description** 擴展至 **完整 `SKILL.md` 正文 (Full)** 時，
            向量空間的變化對檢索命中率是一把**雙刃劍**：
    
            - 🟢 **維持命中（Unchanged Correct）**：`{len(_unchanged_ok)}` 題 (`{len(_unchanged_ok)/len(_cases)*100:.1f}%`)
            - 🔵 **救援進步（Body Rescue）**：`{len(_rescued_cases)}` 題 (`{len(_rescued_cases)/len(_cases)*100:.1f}%`) —— 正文的具體操作與參數補足了簡短說明的不足。
            - 🔴 **排名退步（Body Dilution）**：`{len(_regressed_cases)}` 題 (`{len(_regressed_cases)/len(_cases)*100:.1f}%`) —— 正文的通用敘述或跨領域內容稀釋了核心焦點，導致被相近技能搶佔第 1 名。
            - ⚪ **維持未命中（Unchanged Incorrect）**：`{len(_unchanged_fail)}` 題 (`{len(_unchanged_fail)/len(_cases)*100:.1f}%`)
            """),
            _fig_trans,
            mo.md(f"#### 🔴 排名退步案例清單（Regressed Cases: 共 {len(df_regression)} 題，ND 命中 ➔ Full 誤判）"),
            mo.md("> **退步成因分析**：例如 `json` 技能在 Full 正文中包含大量語法標記與格式範例，在長文 Embeddings 下容易被 `markdown` 或 `graphql` 搶佔；`storage` 正文提及 Embeddings 儲存導致被 `embeddings` 攔截。"),
            mo.ui.table(df_regression, page_size=6),
            mo.md(f"#### 🔵 正文救援案例清單（Body Rescue Cases: 共 {len(df_rescue)} 題，ND 誤判 ➔ Full 命中）"),
            mo.ui.table(df_rescue, page_size=6)
        ])
    else:
        _ui_transition = mo.md("")

    _ui_transition
    return


if __name__ == "__main__":
    app.run()
