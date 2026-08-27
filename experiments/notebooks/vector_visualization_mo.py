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
    # 🔬 技能向量空間與語意分佈分析 (Vector Space Visualization)

    本筆記本從專案本地的 `experiments/.qmd/index.sqlite` 提取以下兩個技能集合的 1536 維 Embedding 向量：
    - **`name-description`**：僅包含 Name + Description（元數據）
    - **`full`**：包含完整 `SKILL.md` 正文

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
    - `name-description` 筆數：`{(df_raw['collection'] == 'name-description').sum()}`
    - `full` 筆數：`{(df_raw['collection'] == 'full').sum()}`
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
    # 1. name-description 單獨 3D 圖
    sns.set_theme(style="whitegrid")
    _fig_nd = plt.figure(figsize=(11, 8), dpi=120)
    _ax_nd = _fig_nd.add_subplot(111, projection="3d")

    _nd = df_pca[df_pca["collection"] == "name-description"]

    _ax_nd.scatter(
        _nd["PC1"], _nd["PC2"], _nd["PC3"],
        c="#3498db", label="name-description (Name+Description Only)",
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

    _ax_nd.set_title("3D PCA: name-description (Name + Description Only)", fontsize=13, pad=18, fontweight="bold")
    _ax_nd.set_xlabel("PC1 (11.10%)", labelpad=8)
    _ax_nd.set_ylabel("PC2 (3.92%)", labelpad=8)
    _ax_nd.set_zlabel("PC3 (3.54%)", labelpad=8)
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
    _ax_full.set_xlabel("PC1 (11.10%)", labelpad=8)
    _ax_full.set_ylabel("PC2 (3.92%)", labelpad=8)
    _ax_full.set_zlabel("PC3 (3.54%)", labelpad=8)
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
def _(axis_limits, df_pca, mo, pd, plt, sample_slugs, sns):
    # 3. name-description vs full 綜合對比 3D 圖 (含漂移向量連線)
    sns.set_theme(style="whitegrid")
    _fig_cmp = plt.figure(figsize=(12, 9), dpi=120)
    _ax_cmp = _fig_cmp.add_subplot(111, projection="3d")

    _nd = df_pca[df_pca["collection"] == "name-description"]
    _full = df_pca[df_pca["collection"] == "full"]

    _ax_cmp.scatter(
        _nd["PC1"], _nd["PC2"], _nd["PC3"],
        c="#3498db", label="name-description (Name+Desc only)",
        alpha=0.8, edgecolors="w", s=50, marker="o"
    )
    _ax_cmp.scatter(
        _full["PC1"], _full["PC2"], _full["PC3"],
        c="#e74c3c", label="full (Full Body)",
        alpha=0.8, edgecolors="w", s=50, marker="^"
    )

    # 連接同技能兩點的漂移向量
    _merged = pd.merge(
        _nd[["slug", "PC1", "PC2", "PC3"]],
        _full[["slug", "PC1", "PC2", "PC3"]],
        on="slug",
        suffixes=("_nd", "_full")
    )

    for _, _row in _merged.iterrows():
        _ax_cmp.plot(
            [_row["PC1_nd"], _row["PC1_full"]],
            [_row["PC2_nd"], _row["PC2_full"]],
            [_row["PC3_nd"], _row["PC3_full"]],
            color="gray", alpha=0.25, linestyle="--", linewidth=0.8
        )

    for _slug in sample_slugs:
        _sub = _merged[_merged["slug"] == _slug]
        if not _sub.empty:
            _r = _sub.iloc[0]
            _ax_cmp.text(
                _r["PC1_full"], _r["PC2_full"], _r["PC3_full"],
                f" {_slug}", fontsize=8.5, fontweight="bold", color="#2c3e50"
            )

    _ax_cmp.set_title("3D PCA: Semantic Drift Vectors (name-description -> full)", fontsize=14, pad=20, fontweight="bold")
    _ax_cmp.set_xlabel("PC1 (11.10%)", labelpad=8)
    _ax_cmp.set_ylabel("PC2 (3.92%)", labelpad=8)
    _ax_cmp.set_zlabel("PC3 (3.54%)", labelpad=8)
    _ax_cmp.set_xlim(axis_limits["x"])
    _ax_cmp.set_ylim(axis_limits["y"])
    _ax_cmp.set_zlim(axis_limits["z"])
    _ax_cmp.legend(loc="upper right", frameon=True)
    plt.tight_layout()

    mo.vstack([
        mo.md("### 3️⃣ 綜合對照：`name-description` vs `full` 向量偏移 (Semantic Drift)"),
        _fig_cmp
    ])
    return


@app.cell
def _(df_pca, mo, np, pd, plt, sns):
    # 2D 投影與分佈對比 (Pairwise 2D Projections)
    fig2, axes = plt.subplots(1, 3, figsize=(18, 5), dpi=100)

    pairs = [("PC1", "PC2"), ("PC1", "PC3"), ("PC2", "PC3")]
    palette = {"name-description": "#3498db", "full": "#e74c3c"}

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
    _nd = df_pca[df_pca["collection"] == "name-description"].set_index("slug")
    _full = df_pca[df_pca["collection"] == "full"].set_index("slug")

    common_slugs = _nd.index.intersection(_full.index)
    dist_records = []

    for s in common_slugs:
        v_nd = _nd.loc[s, "embedding"]
        v_full = _full.loc[s, "embedding"]
        if isinstance(v_nd, pd.Series): v_nd = v_nd.iloc[0]
        if isinstance(v_full, pd.Series): v_full = v_full.iloc[0]

        # Cosine distance
        dot = np.dot(v_nd, v_full)
        norm_nd = np.linalg.norm(v_nd)
        norm_full = np.linalg.norm(v_full)
        cos_sim = dot / (norm_nd * norm_full) if (norm_nd * norm_full) > 0 else 0
        cos_dist = 1.0 - cos_sim

        # Euclidean distance
        euc_dist = np.linalg.norm(v_nd - v_full)

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


if __name__ == "__main__":
    app.run()
