import marimo

__generated_with = "0.24.0"
app = marimo.App(width="full")


@app.cell
def _():
    import json
    import sqlite3
    from pathlib import Path
    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    import pandas as pd
    import seaborn as sns
    from sklearn.decomposition import PCA
    import sqlite_vec
    import marimo as mo

    return PCA, Path, json, mo, np, pd, plt, sns, sqlite3, sqlite_vec


@app.cell
def _(mo):
    mo.md(r"""
    # 🔬 SkillRouter 實驗：技能向量分佈與 PCA 3D 視覺化

    本筆記本從專案本地的 `experiments/.qmd/index.sqlite` 提取以下兩個技能集合的 1536 維 Embedding 向量：
    - **`skills-nd`**：僅包含 Name + Description（元數據）
    - **`skills-all-field`**：包含完整 `SKILL.md` 正文

    透過 **PCA 降維至 3 維空間**，直觀比較「加入完整 Body」後技能向量在語意空間中的分佈漂移與聚合特性。
    """)
    return


@app.cell
def _(Path, json, mo, np, pd, sqlite3, sqlite_vec):
    # 定位 index.sqlite 路徑
    _root_dir = Path(__file__).resolve().parent.parent.parent
    _db_path = _root_dir / "experiments" / ".qmd" / "index.sqlite"

    if not _db_path.exists():
        # Fallback 到當前工作目錄的相對路徑
        _db_path = Path("experiments/.qmd/index.sqlite").resolve()

    _conn = sqlite3.connect(str(_db_path))
    _conn.enable_load_extension(True)
    sqlite_vec.load(_conn)
    _conn.enable_load_extension(False)

    _cursor = _conn.cursor()
    _rows = _cursor.execute("""
        SELECT 
            d.collection,
            d.path,
            d.title,
            vv.hash_seq,
            vec_to_json(vv.embedding)
        FROM documents d
        JOIN content_vectors cv ON cv.hash = d.hash
        JOIN vectors_vec vv ON vv.hash_seq = cv.hash || '_' || cv.seq
        WHERE d.active = 1
    """).fetchall()

    _records = []
    for _col, _path, _title, _hseq, _emb_json in _rows:
        _emb = json.loads(_emb_json)
        # 提取技能 slug 名稱 (例如 aave/SKILL.md -> aave)
        _slug = _path.split("/")[0] if "/" in _path else _path.replace(".md", "")
        _records.append({
            "collection": _col,
            "path": _path,
            "slug": _slug,
            "title": _title,
            "hash_seq": _hseq,
            "embedding": np.array(_emb, dtype=np.float32)
        })

    df_raw = pd.DataFrame(_records)
    _conn.close()

    mo.md(f"""
    ✅ **成功載入向量資料**
    - 資料庫路徑：`{_db_path}`
    - 總向量數量：`{len(df_raw)}` 筆
    - `skills-nd` 筆數：`{(df_raw['collection'] == 'skills-nd').sum()}`
    - `skills-all-field` 筆數：`{(df_raw['collection'] == 'skills-all-field').sum()}`
    - 向量維度：`1536`
    """)
    return (df_raw,)


@app.cell
def _(PCA, df_raw, mo, np):
    # 進行 PCA 降維至 3 維
    X = np.stack(df_raw["embedding"].values)

    pca = PCA(n_components=3, random_state=42)
    X_3d = pca.fit_transform(X)

    df_pca = df_raw.copy()
    df_pca["PC1"] = X_3d[:, 0]
    df_pca["PC2"] = X_3d[:, 1]
    df_pca["PC3"] = X_3d[:, 2]

    var_ratio = pca.explained_variance_ratio_
    total_var = np.sum(var_ratio) * 100

    # 統一三張 3D 圖表的座標軸邊界以利視覺對比
    axis_limits = {
        "x": (float(df_pca["PC1"].min() * 1.15), float(df_pca["PC1"].max() * 1.15)),
        "y": (float(df_pca["PC2"].min() * 1.15), float(df_pca["PC2"].max() * 1.15)),
        "z": (float(df_pca["PC3"].min() * 1.15), float(df_pca["PC3"].max() * 1.15)),
    }

    sample_slugs = [
        "zendesk", "graphql", "embeddings", "meilisearch",
        "marriage", "drawing", "cfo", "stock-market",
        "android", "real-estate-agent"
    ]

    mo.md(f"""
    ### 📊 PCA 降維統計
    - **PC1 解釋變異量**: `{var_ratio[0]*100:.2f}%`
    - **PC2 解釋變異量**: `{var_ratio[1]*100:.2f}%`
    - **PC3 解釋變異量**: `{var_ratio[2]*100:.2f}%`
    - **前 3 主成分累計解釋變異**: `{total_var:.2f}%`
    """)
    return axis_limits, df_pca, sample_slugs


@app.cell
def _(axis_limits, df_pca, mo, plt, sample_slugs, sns):
    # 1. skills-nd 單獨 3D 圖
    sns.set_theme(style="whitegrid")
    _fig_nd = plt.figure(figsize=(11, 8), dpi=120)
    _ax_nd = _fig_nd.add_subplot(111, projection="3d")

    _nd = df_pca[df_pca["collection"] == "skills-nd"]

    _ax_nd.scatter(
        _nd["PC1"], _nd["PC2"], _nd["PC3"],
        c="#3498db", label="skills-nd (Name+Description Only)",
        alpha=0.85, edgecolors="w", s=55, marker="o"
    )

    for _slug in sample_slugs:
        _sub = _nd[_nd["slug"] == _slug]
        if not _sub.empty:
            _r = _sub.iloc[0]
            _ax_nd.text(
                _r["PC1"], _r["PC2"], _r["PC3"],
                f" {_slug}", fontsize=8.5, fontweight="bold", color="#1b4f72"
            )

    _ax_nd.set_title("3D PCA: skills-nd (Name + Description Only)", fontsize=13, pad=18, fontweight="bold")
    _ax_nd.set_xlabel("PC1 (11.10%)", labelpad=8)
    _ax_nd.set_ylabel("PC2 (3.92%)", labelpad=8)
    _ax_nd.set_zlabel("PC3 (3.54%)", labelpad=8)
    _ax_nd.set_xlim(axis_limits["x"])
    _ax_nd.set_ylim(axis_limits["y"])
    _ax_nd.set_zlim(axis_limits["z"])
    _ax_nd.legend(loc="upper right", frameon=True)
    plt.tight_layout()

    mo.vstack([
        mo.md("### 1️⃣ `skills-nd` 集合 3D 向量空間分佈（僅 Name + Description）"),
        _fig_nd
    ])
    return


@app.cell
def _(axis_limits, df_pca, mo, plt, sample_slugs, sns):
    # 2. skills-all-field 單獨 3D 圖
    sns.set_theme(style="whitegrid")
    _fig_all = plt.figure(figsize=(11, 8), dpi=120)
    _ax_all = _fig_all.add_subplot(111, projection="3d")

    _all_f = df_pca[df_pca["collection"] == "skills-all-field"]

    _ax_all.scatter(
        _all_f["PC1"], _all_f["PC2"], _all_f["PC3"],
        c="#e74c3c", label="skills-all-field (Full SKILL.md Body)",
        alpha=0.85, edgecolors="w", s=55, marker="^"
    )

    for _slug in sample_slugs:
        _sub = _all_f[_all_f["slug"] == _slug]
        if not _sub.empty:
            _r = _sub.iloc[0]
            _ax_all.text(
                _r["PC1"], _r["PC2"], _r["PC3"],
                f" {_slug}", fontsize=8.5, fontweight="bold", color="#78281f"
            )

    _ax_all.set_title("3D PCA: skills-all-field (Full SKILL.md Body)", fontsize=13, pad=18, fontweight="bold")
    _ax_all.set_xlabel("PC1 (11.10%)", labelpad=8)
    _ax_all.set_ylabel("PC2 (3.92%)", labelpad=8)
    _ax_all.set_zlabel("PC3 (3.54%)", labelpad=8)
    _ax_all.set_xlim(axis_limits["x"])
    _ax_all.set_ylim(axis_limits["y"])
    _ax_all.set_zlim(axis_limits["z"])
    _ax_all.legend(loc="upper right", frameon=True)
    plt.tight_layout()

    mo.vstack([
        mo.md("### 2️⃣ `skills-all-field` 集合 3D 向量空間分佈（完整 SKILL.md 正文）"),
        _fig_all
    ])
    return


@app.cell
def _(axis_limits, df_pca, mo, pd, plt, sample_slugs, sns):
    # 3. skills-nd vs skills-all-field 綜合對比 3D 圖 (含漂移向量連線)
    sns.set_theme(style="whitegrid")
    _fig_cmp = plt.figure(figsize=(12, 9), dpi=120)
    _ax_cmp = _fig_cmp.add_subplot(111, projection="3d")

    _nd = df_pca[df_pca["collection"] == "skills-nd"]
    _all_f = df_pca[df_pca["collection"] == "skills-all-field"]

    _ax_cmp.scatter(
        _nd["PC1"], _nd["PC2"], _nd["PC3"],
        c="#3498db", label="skills-nd (Name+Desc only)",
        alpha=0.8, edgecolors="w", s=50, marker="o"
    )
    _ax_cmp.scatter(
        _all_f["PC1"], _all_f["PC2"], _all_f["PC3"],
        c="#e74c3c", label="skills-all-field (Full Body)",
        alpha=0.8, edgecolors="w", s=50, marker="^"
    )

    # 連接同技能兩點的漂移向量
    _merged = pd.merge(
        _nd[["slug", "PC1", "PC2", "PC3"]],
        _all_f[["slug", "PC1", "PC2", "PC3"]],
        on="slug",
        suffixes=("_nd", "_all")
    )

    for _, _row in _merged.iterrows():
        _ax_cmp.plot(
            [_row["PC1_nd"], _row["PC1_all"]],
            [_row["PC2_nd"], _row["PC2_all"]],
            [_row["PC3_nd"], _row["PC3_all"]],
            color="gray", alpha=0.25, linestyle="--", linewidth=0.8
        )

    for _slug in sample_slugs:
        _sub = _merged[_merged["slug"] == _slug]
        if not _sub.empty:
            _r = _sub.iloc[0]
            _ax_cmp.text(
                _r["PC1_all"], _r["PC2_all"], _r["PC3_all"],
                f" {_slug}", fontsize=8.5, fontweight="bold", color="#2c3e50"
            )

    _ax_cmp.set_title("3D PCA: Semantic Drift Vectors (skills-nd -> skills-all-field)", fontsize=14, pad=20, fontweight="bold")
    _ax_cmp.set_xlabel("PC1 (11.10%)", labelpad=8)
    _ax_cmp.set_ylabel("PC2 (3.92%)", labelpad=8)
    _ax_cmp.set_zlabel("PC3 (3.54%)", labelpad=8)
    _ax_cmp.set_xlim(axis_limits["x"])
    _ax_cmp.set_ylim(axis_limits["y"])
    _ax_cmp.set_zlim(axis_limits["z"])
    _ax_cmp.legend(loc="upper right", frameon=True)
    plt.tight_layout()

    mo.vstack([
        mo.md("### 3️⃣ 綜合對照：`skills-nd` vs `skills-all-field` 向量偏移 (Semantic Drift)"),
        _fig_cmp
    ])
    return


@app.cell
def _(df_pca, mo, np, pd, plt, sns):
    # 2D 投影與分佈對比 (Pairwise 2D Projections)
    fig2, axes = plt.subplots(1, 3, figsize=(18, 5), dpi=100)

    pairs = [("PC1", "PC2"), ("PC1", "PC3"), ("PC2", "PC3")]
    palette = {"skills-nd": "#3498db", "skills-all-field": "#e74c3c"}

    for idx, (px, py) in enumerate(pairs):
        sns.scatterplot(
            data=df_pca, x=px, y=py, hue="collection",
            palette=palette, alpha=0.7, ax=axes[idx], s=40
        )
        sns.kdeplot(
            data=df_pca, x=px, y=py, hue="collection",
            palette=palette, alpha=0.3, ax=axes[idx], levels=4
        )
        axes[idx].set_title(f"{px} vs {py}", fontweight="bold")

    plt.tight_layout()

    # 計算向量漂移距離 (Cosine & Euclidean Distance)
    _nd = df_pca[df_pca["collection"] == "skills-nd"].set_index("slug")
    _all = df_pca[df_pca["collection"] == "skills-all-field"].set_index("slug")

    common_slugs = _nd.index.intersection(_all.index)
    dist_records = []

    for s in common_slugs:
        v_nd = _nd.loc[s, "embedding"]
        v_all = _all.loc[s, "embedding"]
        if isinstance(v_nd, pd.Series): v_nd = v_nd.iloc[0]
        if isinstance(v_all, pd.Series): v_all = v_all.iloc[0]

        # Cosine distance
        dot = np.dot(v_nd, v_all)
        norm_nd = np.linalg.norm(v_nd)
        norm_all = np.linalg.norm(v_all)
        cos_sim = dot / (norm_nd * norm_all) if (norm_nd * norm_all) > 0 else 0
        cos_dist = 1.0 - cos_sim

        # Euclidean distance
        euc_dist = np.linalg.norm(v_nd - v_all)

        dist_records.append({
            "Skill": s,
            "Cosine Distance": cos_dist,
            "Cosine Similarity": cos_sim,
            "Euclidean Distance": euc_dist
        })

    df_dist = pd.DataFrame(dist_records).sort_values(by="Cosine Distance", ascending=False)

    mo.vstack([
        mo.md("### 📈 2D 投影與核密度估計（KDE）"),
        fig2,
        mo.md("### 🔍 技能漂移程度排行（Top 10 漂移最大 vs 最小）"),
        mo.hstack([
            mo.vstack([mo.md("**漂移最大（Body 帶來最多全新語意資訊）：**"), mo.ui.table(df_dist.head(10))]),
            mo.vstack([mo.md("**漂移最小（Description 與 Body 高度一致）：**"), mo.ui.table(df_dist.tail(10))])
        ])
    ])
    return


@app.cell
def _(mo):
    mo.md(r"""
    ---
    # 🚀 SkillRouter 路由評測實驗：ND vs. All-Field 在 5 大檢索架構下的表現

    依據論文 **《SkillRouter: Skill Routing for LLM Agents at Scale》 (arXiv:2603.22455)** 的核心評測協議，
    我們以倉庫內 **131 個已重構技能** 的 `test-prompts.json`（共 321 道測試題目）作為 Ground Truth 基準，
    評測以下 **5 種檢索路由 Pipeline** 在 `skills-nd` 與 `skills-all-field` 上的效果：

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
            palette={"skills-nd": "#3498db", "skills-all-field": "#e74c3c"},
            ax=_axes[0]
        )
        _axes[0].set_title("Hit@1 Routing Accuracy: ND vs. All-Field", fontsize=13, fontweight="bold")
        _axes[0].set_ylabel("Hit@1 (%)")
        _axes[0].tick_params(axis="x", rotation=25, labelsize=9)
        _axes[0].set_ylim(0, 105)

        # 2. MRR@10 對比
        sns.barplot(
            data=df_metrics, x="Pipeline", y="MRR@10", hue="Collection",
            palette={"skills-nd": "#3498db", "skills-all-field": "#e74c3c"},
            ax=_axes[1]
        )
        _axes[1].set_title("MRR@10 (Mean Reciprocal Rank): ND vs. All-Field", fontsize=13, fontweight="bold")
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
            > 2. **Body Rescue 正文救援效應**：共有 **{len(_rescued)} 道題目**在純 ND 描述中檢索失敗（Top-1 誤判），但在引入完整 Body 後成功命中正確技能！
            """)
        ])
    else:
        df_metrics = pd.DataFrame()
        _ui_bench = mo.md("⚠️ 尚未找到評測結果檔案 `routing_benchmark_results.json`，請先執行評測腳本。")

    _ui_bench
    return


@app.cell
def _(Path, json, mo, pd):
    # 模組 4：Body Rescue 案例深度下鑽
    _root_dir = Path(__file__).resolve().parent.parent.parent
    _eval_file = _root_dir / "experiments" / "datasets" / "routing_benchmark_results.json"

    if _eval_file.exists():
        _eval_data = json.loads(_eval_file.read_text(encoding="utf-8"))
        _cases = _eval_data["detailed_cases"]
        _rescued_cases = [c for c in _cases if c.get("is_rescued_by_body")]

        _case_rows = []
        for c in _rescued_cases:
            _case_rows.append({
                "Query ID": c["query_id"],
                "Target Skill": c["skill"],
                "Task Prompt": c["natural_prompt"],
                "ND Top-1 (Misrouted)": c["nd_vec_top5"][0] if c["nd_vec_top5"] else "None",
                "All-Field Top-1 (Rescued)": c["all_vec_top5"][0] if c["all_vec_top5"] else "None"
            })

        df_rescue = pd.DataFrame(_case_rows)

        _ui_rescue = mo.vstack([
            mo.md(f"### 🔍 模組 4：正文救援個案下鑽（Body Rescue Cases: 共 {len(df_rescue)} 題）"),
            mo.md("以下展示「僅看 Name+Description 時路由錯誤，但加入 SKILL.md Body 後成功命中」的典型案例："),
            mo.ui.table(df_rescue, page_size=8)
        ])
    else:
        _ui_rescue = mo.md("")

    _ui_rescue
    return


if __name__ == "__main__":
    app.run()
