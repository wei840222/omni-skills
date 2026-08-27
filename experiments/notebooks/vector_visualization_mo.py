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
    import scipy.cluster.hierarchy as sch
    import sqlite_vec
    import marimo as mo

    return PCA, Path, json, mo, np, pd, plt, sns, sqlite3, sqlite_vec


@app.cell
def _(mo):
    mo.md(r"""
    # 🔬 技能向量空間、語意幾何與混淆分群分析 (Vector Space & Semantic Diagnostics)

    本筆記本從專案本地的 `experiments/.qmd/index.sqlite` 提取以下三個技能集合的 1024 維 Qwen3 Embedding 向量：
    - **`name-description` (ND)**：僅包含 Name + Description（元數據）
    - **`full`**：包含完整 `SKILL.md` 正文
    - **`full-references`**：包含完整 `SKILL.md` 正文以及 `references/` 目錄下的所有參考文件

    ### 完整分析模組清單：
    - **模組 1 ~ 3**：單一集合 3D 空間分佈（ND / Full / Full-References）
    - **模組 4**：三大集合 3D 綜合對照（Multi-Collection Semantic Comparison）
    - **模組 5**：2D 投影與核密度估計（Pairwise 2D KDE）
    - **模組 6**：雙階段語意漂移深度分析（ND ➔ Full ➔ References 空間位移軌跡）
    - **模組 7**：技能語意覆蓋半徑與離散度分析（Skill Semantic Radius & Volume）
    - **模組 8**：131 個技能近親混淆熱力圖與近親對排行（Skill-to-Skill Confusion Heatmap）
    """)
    return


@app.cell
def _(Path, json, mo, np, pd, sqlite3, sqlite_vec):
    # 定位 index.sqlite 路徑
    _root_dir = Path(__file__).resolve().parent.parent.parent
    _db_path = _root_dir / "experiments" / ".qmd" / "index.sqlite"

    if not _db_path.exists():
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
    ✅ **成功載入向量資料庫**
    - 資料庫路徑：`{_db_path}`
    - 總向量數量：`{len(df_raw)}` 筆
    - `name-description` 筆數：`{(df_raw['collection'] == 'name-description').sum()}`
    - `full` 筆數：`{(df_raw['collection'] == 'full').sum()}`
    - `full-references` 筆數：`{(df_raw['collection'] == 'full-references').sum()}`
    - 向量維度：`1024` (Qwen3-Embedding-0.6B)
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
    ### 📊 PCA 降維統計 (Qwen3-Embedding 1024D)
    - **PC1 解釋變異量**: `{var_ratio[0]*100:.2f}%`
    - **PC2 解釋變異量**: `{var_ratio[1]*100:.2f}%`
    - **PC3 解釋變異量**: `{var_ratio[2]*100:.2f}%`
    - **前 3 主成分累計解釋變異**: `{total_var:.2f}%`
    """)
    return axis_limits, df_pca, sample_slugs


@app.cell
def _(axis_limits, df_pca, mo, plt, sample_slugs, sns):
    # 1. name-description 單獨 3D 圖
    sns.set_theme(style="whitegrid")
    _fig_nd = plt.figure(figsize=(11, 8), dpi=120)
    _ax_nd = _fig_nd.add_subplot(111, projection="3d")

    _nd = df_pca[df_pca["collection"] == "name-description"]

    _ax_nd.scatter(
        _nd["PC1"], _nd["PC2"], _nd["PC3"],
        c="#3498db", label="name-description (Name+Desc Only)",
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

    _ax_nd.set_title("3D PCA: name-description (Metadata Only)", fontsize=13, pad=18, fontweight="bold")
    _ax_nd.set_xlim(axis_limits["x"])
    _ax_nd.set_ylim(axis_limits["y"])
    _ax_nd.set_zlim(axis_limits["z"])
    _ax_nd.legend(loc="upper right", frameon=True)
    plt.tight_layout()

    mo.vstack([
        mo.md("### 1️⃣ `name-description` 集合 3D 向量空間分佈（僅 Name + Description）"),
        _fig_nd
    ])
    return


@app.cell
def _(axis_limits, df_pca, mo, plt, sample_slugs, sns):
    # 2. full 單獨 3D 圖
    sns.set_theme(style="whitegrid")
    _fig_full = plt.figure(figsize=(11, 8), dpi=120)
    _ax_full = _fig_full.add_subplot(111, projection="3d")

    _full = df_pca[df_pca["collection"] == "full"]

    _ax_full.scatter(
        _full["PC1"], _full["PC2"], _full["PC3"],
        c="#e74c3c", label="full (Full SKILL.md Body)",
        alpha=0.85, edgecolors="w", s=55, marker="^"
    )

    for _slug in sample_slugs:
        _sub = _full[_full["slug"] == _slug]
        if not _sub.empty:
            _r = _sub.iloc[0]
            _ax_full.text(
                _r["PC1"], _r["PC2"], _r["PC3"],
                f" {_slug}", fontsize=8.5, fontweight="bold", color="#78281f"
            )

    _ax_full.set_title("3D PCA: full (Full SKILL.md Body)", fontsize=13, pad=18, fontweight="bold")
    _ax_full.set_xlim(axis_limits["x"])
    _ax_full.set_ylim(axis_limits["y"])
    _ax_full.set_zlim(axis_limits["z"])
    _ax_full.legend(loc="upper right", frameon=True)
    plt.tight_layout()

    mo.vstack([
        mo.md("### 2️⃣ `full` 集合 3D 向量空間分佈（完整 SKILL.md 正文）"),
        _fig_full
    ])
    return


@app.cell
def _(axis_limits, df_pca, mo, plt, sample_slugs, sns):
    # 3. full-references 單獨 3D 圖
    sns.set_theme(style="whitegrid")
    _fig_ref = plt.figure(figsize=(11, 8), dpi=120)
    _ax_ref = _fig_ref.add_subplot(111, projection="3d")

    _ref = df_pca[df_pca["collection"] == "full-references"]

    _ax_ref.scatter(
        _ref["PC1"], _ref["PC2"], _ref["PC3"],
        c="#9b59b6", label="full-references (SKILL.md + references/*.md)",
        alpha=0.65, edgecolors="w", s=40, marker="s"
    )

    for _slug in sample_slugs:
        _sub = _ref[_ref["slug"] == _slug]
        if not _sub.empty:
            _r = _sub.iloc[0]
            _ax_ref.text(
                _r["PC1"], _r["PC2"], _r["PC3"],
                f" {_slug}", fontsize=8.5, fontweight="bold", color="#4a235a"
            )

    _ax_ref.set_title("3D PCA: full-references (Full Body + All References)", fontsize=13, pad=18, fontweight="bold")
    _ax_ref.set_xlim(axis_limits["x"])
    _ax_ref.set_ylim(axis_limits["y"])
    _ax_ref.set_zlim(axis_limits["z"])
    _ax_ref.legend(loc="upper right", frameon=True)
    plt.tight_layout()

    mo.vstack([
        mo.md("### 3️⃣ `full-references` 集合 3D 向量空間分佈（SKILL.md + references 目錄）"),
        _fig_ref
    ])
    return


@app.cell
def _(axis_limits, df_pca, mo, plt, sns):
    # 4. 三大集合綜合對照 3D 圖
    sns.set_theme(style="whitegrid")
    _fig_cmp = plt.figure(figsize=(12, 9), dpi=120)
    _ax_cmp = _fig_cmp.add_subplot(111, projection="3d")

    _nd = df_pca[df_pca["collection"] == "name-description"]
    _full = df_pca[df_pca["collection"] == "full"]
    _ref = df_pca[df_pca["collection"] == "full-references"]

    _ax_cmp.scatter(_nd["PC1"], _nd["PC2"], _nd["PC3"], c="#3498db", label="name-description", alpha=0.7, edgecolors="w", s=45, marker="o")
    _ax_cmp.scatter(_full["PC1"], _full["PC2"], _full["PC3"], c="#e74c3c", label="full", alpha=0.7, edgecolors="w", s=45, marker="^")
    _ax_cmp.scatter(_ref["PC1"], _ref["PC2"], _ref["PC3"], c="#9b59b6", label="full-references", alpha=0.4, edgecolors="w", s=30, marker="s")

    _ax_cmp.set_title("3D PCA: Multi-Collection Semantic Comparison", fontsize=14, pad=20, fontweight="bold")
    _ax_cmp.set_xlim(axis_limits["x"])
    _ax_cmp.set_ylim(axis_limits["y"])
    _ax_cmp.set_zlim(axis_limits["z"])
    _ax_cmp.legend(loc="upper right", frameon=True)
    plt.tight_layout()

    mo.vstack([
        mo.md("### 4️⃣ 三大集合綜合對照：`name-description` vs `full` vs `full-references`"),
        _fig_cmp
    ])
    return


@app.cell
def _(df_pca, mo, plt, sns):
    # 5. 2D 投影與分佈對比 (Pairwise 2D Projections)
    fig2, axes = plt.subplots(1, 3, figsize=(18, 5), dpi=100)

    pairs = [("PC1", "PC2"), ("PC1", "PC3"), ("PC2", "PC3")]
    palette = {"name-description": "#3498db", "full": "#e74c3c", "full-references": "#9b59b6"}

    for idx, (px, py) in enumerate(pairs):
        sns.scatterplot(
            data=df_pca, x=px, y=py, hue="collection",
            palette=palette, alpha=0.6, ax=axes[idx], s=35
        )
        sns.kdeplot(
            data=df_pca, x=px, y=py, hue="collection",
            palette=palette, alpha=0.25, ax=axes[idx], levels=3
        )
        axes[idx].set_title(f"{px} vs {py}", fontweight="bold")

    plt.tight_layout()

    mo.vstack([
        mo.md("### 5️⃣ 2D 投影與核密度估計（KDE）"),
        fig2
    ])
    return


@app.cell
def _(df_pca, mo, np, pd, plt, sample_slugs, sns):
    # 6. 語意漂移分析 (Semantic Drift Analysis: ND -> Full & ND -> Full-References)
    _nd_df = df_pca[df_pca["collection"] == "name-description"].set_index("slug")
    _full_df = df_pca[df_pca["collection"] == "full"]
    _ref_df = df_pca[df_pca["collection"] == "full-references"]

    _skills = sorted(list(_nd_df.index))
    _drift_records = []

    for _s in _skills:
        _nd_row = _nd_df.loc[_s]
        _nd_vec = _nd_row["embedding"]
        _nd_norm = np.linalg.norm(_nd_vec)
        _nd_p1, _nd_p2, _nd_p3 = _nd_row["PC1"], _nd_row["PC2"], _nd_row["PC3"]

        # Full 聚類質心
        _f_sub = _full_df[_full_df["slug"] == _s]
        if not _f_sub.empty:
            _f_embs = np.stack(_f_sub["embedding"].values)
            _f_mean_emb = np.mean(_f_embs, axis=0)
            _f_norm = np.linalg.norm(_f_mean_emb)
            _f_p1, _f_p2, _f_p3 = _f_sub["PC1"].mean(), _f_sub["PC2"].mean(), _f_sub["PC3"].mean()
            _cos_sim_full = float(np.dot(_nd_vec, _f_mean_emb) / (_nd_norm * _f_norm)) if _nd_norm * _f_norm > 0 else 1.0
            _pca_dist_full = float(np.sqrt((_nd_p1 - _f_p1)**2 + (_nd_p2 - _f_p2)**2 + (_nd_p3 - _f_p3)**2))
        else:
            _cos_sim_full, _pca_dist_full = 1.0, 0.0
            _f_p1, _f_p2, _f_p3 = _nd_p1, _nd_p2, _nd_p3

        # Full-References 聚類質心
        _r_sub = _ref_df[_ref_df["slug"] == _s]
        if not _r_sub.empty:
            _r_embs = np.stack(_r_sub["embedding"].values)
            _r_mean_emb = np.mean(_r_embs, axis=0)
            _r_norm = np.linalg.norm(_r_mean_emb)
            _r_p1, _r_p2, _r_p3 = _r_sub["PC1"].mean(), _r_sub["PC2"].mean(), _r_sub["PC3"].mean()
            _cos_sim_ref = float(np.dot(_nd_vec, _r_mean_emb) / (_nd_norm * _r_norm)) if _nd_norm * _r_norm > 0 else 1.0
            _pca_dist_ref = float(np.sqrt((_nd_p1 - _r_p1)**2 + (_nd_p2 - _r_p2)**2 + (_nd_p3 - _r_p3)**2))
        else:
            _cos_sim_ref, _pca_dist_ref = _cos_sim_full, _pca_dist_full
            _r_p1, _r_p2, _r_p3 = _f_p1, _f_p2, _f_p3

        _drift_records.append({
            "Skill": _s,
            "ND->Full CosSim": round(_cos_sim_full, 4),
            "ND->Full Drift (PCA)": round(_pca_dist_full, 4),
            "ND->Refs CosSim": round(_cos_sim_ref, 4),
            "ND->Refs Drift (PCA)": round(_pca_dist_ref, 4),
            "ND_PC1": _nd_p1, "ND_PC2": _nd_p2, "ND_PC3": _nd_p3,
            "Full_PC1": _f_p1, "Full_PC2": _f_p2, "Full_PC3": _f_p3,
            "Ref_PC1": _r_p1, "Ref_PC2": _r_p2, "Ref_PC3": _r_p3,
        })

    df_drift = pd.DataFrame(_drift_records)

    # 繪製語意漂移軌跡圖 (3D Drift Trajectory)
    sns.set_theme(style="whitegrid")
    _fig_drift = plt.figure(figsize=(14, 8), dpi=120)
    _ax_d = _fig_drift.add_subplot(111, projection="3d")

    # 繪製樣本技能的漂移向量
    for _slug in sample_slugs:
        _sub_d = df_drift[df_drift["Skill"] == _slug]
        if not _sub_d.empty:
            _r = _sub_d.iloc[0]
            # 點: ND(藍), Full(紅), Refs(紫)
            _ax_d.scatter(_r["ND_PC1"], _r["ND_PC2"], _r["ND_PC3"], c="#3498db", s=50, marker="o")
            _ax_d.scatter(_r["Full_PC1"], _r["Full_PC2"], _r["Full_PC3"], c="#e74c3c", s=50, marker="^")
            _ax_d.scatter(_r["Ref_PC1"], _r["Ref_PC2"], _r["Ref_PC3"], c="#9b59b6", s=50, marker="s")
            # 軌跡線 ND -> Full
            _ax_d.plot([_r["ND_PC1"], _r["Full_PC1"]], [_r["ND_PC2"], _r["Full_PC2"]], [_r["ND_PC3"], _r["Full_PC3"]],
                       color="#e67e22", linestyle="--", linewidth=1.5, alpha=0.8)
            # 軌跡線 Full -> Refs
            _ax_d.plot([_r["Full_PC1"], _r["Ref_PC1"]], [_r["Full_PC2"], _r["Ref_PC2"]], [_r["Full_PC3"], _r["Ref_PC3"]],
                       color="#8e44ad", linestyle=":", linewidth=1.5, alpha=0.8)
            _ax_d.text(_r["ND_PC1"], _r["ND_PC2"], _r["ND_PC3"], f" {_slug}", fontsize=8.5, fontweight="bold", color="#1a5276")

    _ax_d.set_title("3D Semantic Drift Vectors: ND ➔ Full ➔ References", fontsize=13, pad=18, fontweight="bold")
    plt.tight_layout()

    # 排行榜：漂移最大 vs 最穩定
    _top_drift_full = df_drift.sort_values(by="ND->Full Drift (PCA)", ascending=False).head(8)
    _top_stable_full = df_drift.sort_values(by="ND->Full Drift (PCA)", ascending=True).head(8)

    mo.vstack([
        mo.md("""
        ### 6️⃣ 語意漂移深度分析（Semantic Drift Analysis）

        當技能從簡短元數據擴展為完整文檔及參考資料庫時，向量質心會發生**語意空間位移（Semantic Drift）**：
        - 🟠 **橘色虛線**：`Name-Description` ➔ `Full SKILL.md` 的空間位移
        - 🟣 **紫色點線**：`Full SKILL.md` ➔ `Full-References` 參考資料庫的進一步位移
        """),
        _fig_drift,
        mo.md("#### 🚀 語意漂移最大 Top 8 技能（正文大幅擴充了領域概念與專有名詞）"),
        mo.ui.table(_top_drift_full[["Skill", "ND->Full CosSim", "ND->Full Drift (PCA)", "ND->Refs CosSim", "ND->Refs Drift (PCA)"]], page_size=8),
        mo.md("#### 🛡️ 最穩定 Top 8 技能（正文與 Name-Description 核心語意高度一致）"),
        mo.ui.table(_top_stable_full[["Skill", "ND->Full CosSim", "ND->Full Drift (PCA)", "ND->Refs CosSim", "ND->Refs Drift (PCA)"]], page_size=8),
        mo.md("#### 📋 131 個技能完整語意漂移數據瀏覽器"),
        mo.ui.table(df_drift[["Skill", "ND->Full CosSim", "ND->Full Drift (PCA)", "ND->Refs CosSim", "ND->Refs Drift (PCA)"]], page_size=10)
    ])
    return


@app.cell
def _(df_pca, mo, np, pd, plt, sns):
    # 7. 技能語意覆蓋半徑與離散度分析 (Skill Semantic Radius / Spread in full-references)
    _ref_data = df_pca[df_pca["collection"] == "full-references"]
    _skills = _ref_data["slug"].unique()

    _radius_records = []
    for _s in _skills:
        _sub = _ref_data[_ref_data["slug"] == _s]
        _n_chunks = len(_sub)
        if _n_chunks > 1:
            _embs = np.stack(_sub["embedding"].values)
            # 歸一化
            _norms = np.linalg.norm(_embs, axis=1, keepdims=True)
            _norms[_norms == 0] = 1.0
            _normed = _embs / _norms

            # 質心與迴轉半徑 (Radius of Gyration)
            _centroid = np.mean(_normed, axis=0)
            _centroid_norm = np.linalg.norm(_centroid)
            if _centroid_norm > 0:
                _centroid = _centroid / _centroid_norm

            # 計算各 Chunk 離質心的平均歐氏距離與餘弦距離
            _dists_euclid = np.linalg.norm(_normed - _centroid, axis=1)
            _mean_radius = float(np.mean(_dists_euclid))
            _max_radius = float(np.max(_dists_euclid))
            _cos_sims = np.dot(_normed, _centroid)
            _mean_cos_spread = float(1.0 - np.mean(_cos_sims))
        else:
            _n_chunks = 1
            _mean_radius, _max_radius, _mean_cos_spread = 0.0, 0.0, 0.0

        _radius_records.append({
            "Skill": _s,
            "Chunk Count": _n_chunks,
            "Semantic Radius (Mean)": round(_mean_radius, 4),
            "Max Radius": round(_max_radius, 4),
            "Cosine Spread (1-CosSim)": round(_mean_cos_spread, 4)
        })

    df_radius = pd.DataFrame(_radius_records)

    # 繪製覆蓋半徑分析圖 (Top Broad vs Top Focused)
    _top_broad = df_radius[df_radius["Chunk Count"] > 2].sort_values(by="Semantic Radius (Mean)", ascending=False).head(10)
    _top_focused = df_radius[df_radius["Chunk Count"] > 2].sort_values(by="Semantic Radius (Mean)", ascending=True).head(10)

    sns.set_theme(style="whitegrid")
    _fig_rad, _axes_r = plt.subplots(1, 2, figsize=(16, 5), dpi=120)

    # 1. 巨無霸型技能 (Top Broad)
    sns.barplot(
        data=_top_broad, x="Semantic Radius (Mean)", y="Skill",
        hue="Skill", palette="magma", legend=False, ax=_axes_r[0]
    )
    _axes_r[0].set_title("Top 10 Broadest Skills (Large Semantic Volume)", fontsize=12, fontweight="bold")
    _axes_r[0].set_xlabel("Mean Semantic Radius (Gyration)")

    # 2. 超專精聚焦型技能 (Top Focused)
    sns.barplot(
        data=_top_focused, x="Semantic Radius (Mean)", y="Skill",
        hue="Skill", palette="crest", legend=False, ax=_axes_r[1]
    )
    _axes_r[1].set_title("Top 10 Most Focused Skills (Compact Semantic Ball)", fontsize=12, fontweight="bold")
    _axes_r[1].set_xlabel("Mean Semantic Radius (Gyration)")

    plt.tight_layout()

    mo.vstack([
        mo.md("""
        ### 🌐 模組 7：技能語意覆蓋半徑與幾何體積分析 (Skill Semantic Volume & Radius)

        在 `full-references` 資料庫中，每個技能由數個至數十個 Chunk 構成。
        透過計算每個技能所有 Chunk 相對於其幾何質心的**迴轉半徑（Radius of Gyration）**與**餘弦離散度（Cosine Spread）**：
        - **🌐 巨無霸型技能（Broad / High-Variance）**：覆蓋半徑極大（如 `unreal-engine`、`pocketbase`、`threejs`），具備多子模組與複雜 API，容易成為跨領域侵入者。
        - **🎯 超專精聚焦型技能（Compact / Focused）**：所有 Chunk 緊密環繞於同一語意焦點，邊界清晰（如 `grammar`、`find`、`regex`）。
        """),
        _fig_rad,
        mo.md("#### 📋 131 個技能語意半徑與切塊統計表"),
        mo.ui.table(df_radius.sort_values(by="Semantic Radius (Mean)", ascending=False), page_size=8)
    ])
    return


@app.cell
def _(df_pca, mo, np, pd, plt, sns):
    # 8. 131 個技能近親混淆熱力圖與階層分群 (Skill Confusion Heatmap & Closest Pairs)
    _nd_df = df_pca[df_pca["collection"] == "name-description"].set_index("slug")
    _skills = sorted(list(_nd_df.index))

    # 提取 131 個技能的 1024D 歸一化向量
    _mat = np.stack([_nd_df.loc[_s, "embedding"] for _s in _skills])
    _norms = np.linalg.norm(_mat, axis=1, keepdims=True)
    _norms[_norms == 0] = 1.0
    _normed_mat = _mat / _norms

    # 計算 131 x 131 兩兩餘弦相似度矩陣
    _cos_sim_matrix = np.dot(_normed_mat, _normed_mat.T)
    _cos_sim_matrix = np.clip(_cos_sim_matrix, -1.0, 1.0)

    # 找出除了對角線外，最相似的 Top 15 技能近親對 (Closest Skill Pairs)
    _pairs = []
    _n = len(_skills)
    for _i in range(_n):
        for _j in range(_i + 1, _n):
            _sim = float(_cos_sim_matrix[_i, _j])
            _pairs.append({
                "Skill A": _skills[_i],
                "Skill B": _skills[_j],
                "Cosine Similarity": round(_sim, 4),
                "Confusion Risk": "🔴 High Risk (>0.80)" if _sim >= 0.80 else ("🟠 Moderate (>0.70)" if _sim >= 0.70 else "🟢 Low")
            })

    df_pairs = pd.DataFrame(_pairs).sort_values(by="Cosine Similarity", ascending=False)
    _top15_pairs = df_pairs.head(15)

    # 繪製最相似 Top 15 技能近親對水平條形圖
    sns.set_theme(style="whitegrid")
    _fig_pairs, _ax_p = plt.subplots(figsize=(12, 5), dpi=120)
    _top15_plot = _top15_pairs.copy()
    _top15_plot["Pair"] = _top15_plot["Skill A"] + "  ↔  " + _top15_plot["Skill B"]

    sns.barplot(
        data=_top15_plot, x="Cosine Similarity", y="Pair",
        hue="Pair", palette="flare", legend=False, ax=_ax_p
    )
    _ax_p.set_title("Top 15 Closest / Most Confusable Skill Pairs (Name-Description Cosine Similarity)", fontsize=12, fontweight="bold")
    _ax_p.set_xlabel("Cosine Similarity (1024D Qwen3 Embedding)")
    _ax_p.set_xlim(0.65, 0.95)
    for _p in _ax_p.patches:
        _ax_p.annotate(f"{_p.get_width():.4f}", (_p.get_width(), _p.get_y() + _p.get_height() / 2.),
                       ha="left", va="center", xytext=(4, 0), textcoords="offset points", fontweight="bold", fontsize=8.5)
    plt.tight_layout()

    mo.vstack([
        mo.md("""
        ### 🔥 模組 8：131 個技能近親混淆熱力圖與最相似技能對排行 (Skill Confusion Analysis)

        評估在 1024 維語意空間中，哪些技能因為**功能領域相近、術語重疊**而處於高度混淆風險區（Cosine Similarity > 0.75）：
        """),
        _fig_pairs,
        mo.md("#### 📋 最易混淆 Top 15 技能近親對排行榜（架構優化與 Prompt 重點區隔對象）"),
        mo.ui.table(_top15_pairs, page_size=8)
    ])
    return


if __name__ == "__main__":
    app.run()
