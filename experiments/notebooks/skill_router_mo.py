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
    評測以下 **5 種檢索路由 Pipeline** 在三大知識集合上的效果：
    1. **`name-description`**：僅包含 Name + Description（元數據）
    2. **`full`**：包含完整 `SKILL.md` 正文
    3. **`full-references`**：包含完整 `SKILL.md` 正文以及 `references/` 目錄下的所有參考文件

    ### 評測的 5 大檢索路由 Pipeline：
    1. **BM25 (Lexical)**：使用 Gemini 提煉的 BM25 關鍵字進行 SQLite FTS5 全文檢索
    2. **Vector (Dense)**：使用本地 `Qwen3-Embedding-0.6B` (1024 維) 進行純向量語意檢索
    3. **Hybrid (BM25 + Vec RRF)**：無 HyDE、無 Rerank 的純倒數排名融合 (Reciprocal Rank Fusion)
    4. **Hybrid (No Rerank)**：結合多通道擴展檢索融合
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
        _metrics = _eval_data.get("metrics_by_pipeline", {})
        _cases = _eval_data.get("detailed_cases", [])

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

        _rescued = [c for c in _cases if c.get("is_rescued_by_body")]

        _ui_bench = mo.vstack([
            mo.md("### 📊 模組 2 & 3：5 大 Pipeline 路由評測矩陣與指標看板"),
            mo.ui.table(df_metrics, page_size=15),
            _fig_bench,
            mo.md(f"""
            > [!NOTE]
            > **關鍵發現**：
            > 1. **BM25 & Hybrid 表現卓越**：在具備精準關鍵字（`bm25_prompt`）的情境下，BM25 與 Hybrid RRF 達到了 **91.90% Hit@1** 與 **0.9453 MRR@10**。
            > 2. **向量檢索在元數據層（`name-description`）表現最為精準**：`Qwen3-Embedding 1024D` 在 ND 上達到 **73.52% Hit@1**，而在包含大量長文正文與參考文件的集合中，純向量因語意稀釋而下滑。
            """)
        ])
    else:
        df_metrics = pd.DataFrame()
        _ui_bench = mo.md("⚠️ 尚未找到評測結果檔案 `routing_benchmark_results.json`，請先執行評測腳本。")

    _ui_bench
    return


@app.cell
def _(Path, json, mo, pd, plt, sns):
    # 模組 4：路由躍遷與排名變化分析（Transition Breakdown & Regression Analysis）
    _root_dir = Path(__file__).resolve().parent.parent.parent
    _eval_file = _root_dir / "experiments" / "datasets" / "routing_benchmark_results.json"

    if _eval_file.exists():
        _eval_data = json.loads(_eval_file.read_text(encoding="utf-8"))
        _cases = _eval_data.get("detailed_cases", [])

        _rescued_cases = [c for c in _cases if c.get("is_rescued_by_body")]
        _regressed_cases = [c for c in _cases if c.get("is_regressed")]
        _unchanged_ok = [c for c in _cases if c.get("status") == "Unchanged (Correct)"]
        _unchanged_fail = [c for c in _cases if c.get("status") == "Unchanged (Incorrect)"]

        # 1. 躍遷統計圖表 (Transition Donut & Regression Shift)
        _fig_trans, _axes = plt.subplots(1, 2, figsize=(16, 5), dpi=120)

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

        # 2. 救援案例表
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

        # 3. 退步案例表
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
            ### 🔍 模組 4：排名躍遷與退步深度診斷
            
            - 🟢 **維持命中（Unchanged Correct）**：`{len(_unchanged_ok)}` 題 (`{len(_unchanged_ok)/len(_cases)*100:.1f}%`)
            - 🔵 **救援進步（Body Rescue）**：`{len(_rescued_cases)}` 題 (`{len(_rescued_cases)/len(_cases)*100:.1f}%`)
            - 🔴 **排名退步（Body Dilution）**：`{len(_regressed_cases)}` 題 (`{len(_regressed_cases)/len(_cases)*100:.1f}%`)
            - ⚪ **維持未命中（Unchanged Incorrect）**：`{len(_unchanged_fail)}` 題 (`{len(_unchanged_fail)/len(_cases)*100:.1f}%`)
            """),
            _fig_trans,
            mo.md(f"#### 🔴 排名退步案例清單（Regressed Cases: 共 {len(df_regression)} 題）"),
            mo.ui.table(df_regression, page_size=6),
            mo.md(f"#### 🔵 正文救援案例清單（Body Rescue Cases: 共 {len(df_rescue)} 題）"),
            mo.ui.table(df_rescue, page_size=6)
        ])
    else:
        _ui_transition = mo.md("")

    _ui_transition
    return


if __name__ == "__main__":
    app.run()
