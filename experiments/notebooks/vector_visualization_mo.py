import marimo

__generated_with = "0.24.0"
app = marimo.App(width="full")


@app.cell
def _():
    import json
    from pathlib import Path
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import seaborn as sns
    from sklearn.decomposition import PCA

    return PCA, Path, json, mo, np, pd, plt, sns


@app.cell
def _(Path, json, mo, np, pd):
    _data_dir = Path(__file__).resolve().parent.parent / "datasets"
    _required = [_data_dir / "embeddings.npz", _data_dir / "embedding_manifest.json"]
    mo.stop(not all(_path.exists() for _path in _required), mo.md("""
    # 技能向量空間

    尚未找到本次 embedding 產物。請在 `experiments/` 執行：

    ```bash
    uv run python scripts/prepare_experiment_datasets.py
    uv run python scripts/generate_bm25_prompts.py
    uv run python scripts/generate_embeddings.py --embed-model text-embedding-3-small --dimension 1536
    ```

    筆記本讀取實際向量，不需要舊 QMD SQLite schema，也不會呼叫模型。
    """))
    embedding_metadata = json.loads(_required[1].read_text(encoding="utf-8"))
    _records = []
    vectors_by_collection, skills_by_collection = {}, {}
    with np.load(_required[0], allow_pickle=False) as _archive:
        for _collection in ["name-description", "full", "full-references"]:
            _vectors = np.asarray(_archive[_collection + "__vectors"], dtype=np.float32)
            _skills = _archive[_collection + "__skills"].astype(str)
            _paths = _archive[_collection + "__paths"].astype(str)
            if len(_vectors) != len(_skills) or len(_vectors) != len(_paths):
                raise ValueError(f"Embedding artifact rows do not align: {_collection}")
            if not np.isfinite(_vectors).all():
                raise ValueError(f"Non-finite embedding values: {_collection}")
            _norms = np.linalg.norm(_vectors, axis=1, keepdims=True)
            if np.any(_norms == 0):
                raise ValueError(f"Zero-length embedding: {_collection}")
            _vectors = _vectors / _norms
            vectors_by_collection[_collection], skills_by_collection[_collection] = _vectors, _skills
            for _index, (_skill, _path) in enumerate(zip(_skills, _paths)):
                _records.append({"collection": _collection, "skill": _skill, "path": _path, "vector_index": _index})
    df_chunks = pd.DataFrame(_records)
    mo.stop(df_chunks.empty, mo.md("Embedding 產物沒有切塊資料，請重新產生。"))
    return (
        df_chunks,
        embedding_metadata,
        skills_by_collection,
        vectors_by_collection,
    )


@app.cell
def _(df_chunks, embedding_metadata, json, mo, vectors_by_collection):
    _counts = df_chunks.groupby("collection").agg(Skills=("skill", "nunique"), Chunks=("skill", "size")).reset_index()
    mo.vstack([
        mo.md(f"""
        # 完整技能庫的向量與語意診斷

        模型：`{embedding_metadata.get('model', '未記錄')}` · 實際維度：**{next(iter(vectors_by_collection.values())).shape[1]}** · 查詢數：**{embedding_metadata.get('query_count', '未記錄')}**

        Corpus：`{embedding_metadata.get('corpus_hash', '未記錄')}`

        `name-description` 僅含名稱與描述；`full` 使用完整 SKILL.md 切塊；`full-references` 再加入參考文件。
        距離和相似度均在原始單位化向量空間計算。PCA 僅供視覺投影，圖上遠近不能直接代表路由準確率。
        """),
        mo.ui.table(_counts, page_size=3),
        mo.accordion({"Embedding 版本與 API 量測": mo.md("```json\n" + json.dumps(embedding_metadata, ensure_ascii=False, indent=2) + "\n```")}),
    ])
    return


@app.cell
def _(PCA, df_chunks, mo, np, vectors_by_collection):
    _matrix = np.concatenate([vectors_by_collection[_c] for _c in ["name-description", "full", "full-references"]])
    _components = min(3, _matrix.shape[0], _matrix.shape[1])
    mo.stop(_components < 2, mo.md("至少需要兩筆向量才能呈現 PCA 投影。"))
    _pca = PCA(n_components=_components, random_state=42)
    _coords = _pca.fit_transform(_matrix)
    df_projection = df_chunks.copy()
    df_projection["PC1"], df_projection["PC2"] = _coords[:, 0], _coords[:, 1]
    df_projection["PC3"] = _coords[:, 2] if _components == 3 else 0.0
    pca_variance = _pca.explained_variance_ratio_
    mo.md(f"### PCA 投影\n前 {_components} 個主成分保留 **{100 * pca_variance.sum():.2f}%** 變異，其餘資訊未顯示在圖中。")
    return (df_projection,)


@app.cell
def _(df_projection, mo, plt, sns):
    sns.set_theme(style="whitegrid")
    _palette = {"name-description": "#3498db", "full": "#e74c3c", "full-references": "#9b59b6"}
    _fig = plt.figure(figsize=(17, 5))
    for _index, (_collection, _color) in enumerate(_palette.items(), 1):
        _ax = _fig.add_subplot(1, 3, _index, projection="3d")
        _subset = df_projection[df_projection["collection"] == _collection]
        _ax.scatter(_subset["PC1"], _subset["PC2"], _subset["PC3"], s=8, alpha=0.4, color=_color)
        _ax.set_title(_collection + f" ({len(_subset):,} chunks)")
        for _name, _setter in [("PC1", _ax.set_xlim), ("PC2", _ax.set_ylim), ("PC3", _ax.set_zlim)]:
            _low, _high = df_projection[_name].min(), df_projection[_name].max()
            _margin = max((_high - _low) * 0.05, 0.001)
            _setter(_low - _margin, _high + _margin)
        _ax.set_xlabel("PC1")
        _ax.set_ylabel("PC2")
        _ax.set_zlabel("PC3")
    _fig.tight_layout()
    mo.vstack([mo.md("### 三種語料的共同 PCA 座標"), _fig])
    return


@app.cell
def _(df_projection, mo, plt, sns):
    _fig, _axes = plt.subplots(1, 3, figsize=(17, 5))
    for _ax, (_x, _y) in zip(_axes, [("PC1", "PC2"), ("PC1", "PC3"), ("PC2", "PC3")]):
        sns.scatterplot(data=df_projection, x=_x, y=_y, hue="collection", alpha=0.25, s=8, ax=_ax)
        _ax.set_title(_x + " vs " + _y)
    _fig.tight_layout()
    mo.vstack([mo.md("### 二維投影\n每點代表一個切塊；切塊較多的技能會出現較多點，不代表較高的路由權重。"), _fig])
    return


@app.cell
def _(np, pd, skills_by_collection, vectors_by_collection):
    centroids, _records = {}, []
    for _collection, _vectors in vectors_by_collection.items():
        _skills = skills_by_collection[_collection]
        for _skill in sorted(set(_skills)):
            _subset = _vectors[_skills == _skill]
            _center = _subset.mean(axis=0)
            _norm = np.linalg.norm(_center)
            if _norm == 0:
                raise ValueError(f"Zero-length skill centroid: {_collection}/{_skill}")
            _center = _center / _norm
            centroids[(_collection, _skill)] = _center
            _distance = np.linalg.norm(_subset - _center, axis=1)
            _records.append({"Collection": _collection, "Skill": _skill, "Chunks": len(_subset), "Mean radius": float(_distance.mean()), "Max radius": float(_distance.max()), "Cosine spread": float(1 - (_subset @ _center).mean())})
    df_radius = pd.DataFrame(_records)
    _drifts = []
    for _skill in sorted(set(skills_by_collection["name-description"])):
        _nd, _full, _refs = [centroids[(_c, _skill)] for _c in ["name-description", "full", "full-references"]]
        _drifts.append({"Skill": _skill, "ND -> Full cosine distance": float(1 - np.clip(_nd @ _full, -1, 1)), "Full -> Refs cosine distance": float(1 - np.clip(_full @ _refs, -1, 1)), "ND -> Refs cosine distance": float(1 - np.clip(_nd @ _refs, -1, 1))})
    df_drift = pd.DataFrame(_drifts)
    return centroids, df_drift, df_radius


@app.cell
def _(df_drift, mo, plt):
    _fig, _axes = plt.subplots(1, 2, figsize=(16, 5))
    for _ax, _column in zip(_axes, ["ND -> Full cosine distance", "Full -> Refs cosine distance"]):
        _top = df_drift.nlargest(12, _column).sort_values(_column)
        _ax.barh(_top["Skill"], _top[_column], color="#9b59b6")
        _ax.set_title(_column + " (original embedding space)")
        _ax.set_xlabel("Cosine distance between normalized centroids")
    _fig.tight_layout()
    mo.vstack([mo.md("### 語料擴展造成的向量變化\n距離取原始向量空間內，單位化技能質心的餘弦距離。較大變化不等同於品質改善或退步。"), _fig, mo.ui.table(df_drift.sort_values("ND -> Full cosine distance", ascending=False), page_size=10)])
    return


@app.cell
def _(df_radius, mo, plt):
    _refs = df_radius[df_radius["Collection"] == "full-references"]
    _multi = _refs[_refs["Chunks"] > 1]
    _items = [mo.md("### 切塊分散程度\n比較單位化切塊與其單位化質心。單一切塊的半徑為零；半徑只描述表示分散，不能單獨判斷技能邊界。")]
    if not _multi.empty:
        _fig, _axes = plt.subplots(1, 2, figsize=(16, 5))
        for _ax, _subset, _title in [(_axes[0], _multi.nlargest(12, "Mean radius"), "Largest mean chunk radius"), (_axes[1], _multi.nsmallest(12, "Mean radius"), "Smallest mean chunk radius (multi-chunk)")]:
            _subset = _subset.sort_values("Mean radius")
            _ax.barh(_subset["Skill"], _subset["Mean radius"], color="#3498db")
            _ax.set_title(_title)
            _ax.set_xlabel("Mean Euclidean distance")
        _fig.tight_layout()
        _items.append(_fig)
    _items.append(mo.ui.table(_refs.sort_values("Mean radius", ascending=False), page_size=10))
    mo.vstack(_items)
    return


@app.cell
def _(mo, skills_by_collection):
    skill_choice = mo.ui.dropdown(options=sorted(set(skills_by_collection["name-description"])), value=sorted(set(skills_by_collection["name-description"]))[0], label="查看技能近鄰", searchable=True)
    skill_choice
    return (skill_choice,)


@app.cell
def _(centroids, mo, np, pd, plt, skill_choice, skills_by_collection, sns):
    _skills = sorted(set(skills_by_collection["name-description"]))
    _matrix = np.stack([centroids[("name-description", _skill)] for _skill in _skills])
    _similarity = np.clip(_matrix @ _matrix.T, -1, 1)
    _i, _j = np.triu_indices(len(_skills), k=1)
    _order = np.argsort(-_similarity[_i, _j], kind="stable")[:30]
    _pairs = pd.DataFrame([{"Skill A": _skills[_i[_k]], "Skill B": _skills[_j[_k]], "Cosine similarity": float(_similarity[_i[_k], _j[_k]])} for _k in _order])
    _selected = _skills.index(skill_choice.value)
    _nearest = [_index for _index in np.argsort(-_similarity[_selected], kind="stable") if _index != _selected][:20]
    _neighbors = pd.DataFrame({"Skill": [_skills[_index] for _index in _nearest], "Cosine similarity": [_similarity[_selected, _index] for _index in _nearest]})
    _subset_ids = [_selected] + _nearest[:14]
    _fig, _ax = plt.subplots(figsize=(11, 9))
    sns.heatmap(_similarity[np.ix_(_subset_ids, _subset_ids)], xticklabels=[_skills[_k] for _k in _subset_ids], yticklabels=[_skills[_k] for _k in _subset_ids], vmin=-1, vmax=1, cmap="vlag", ax=_ax)
    _ax.set_title("Metadata cosine similarity: selected skill and nearest neighbors")
    _fig.tight_layout()
    mo.vstack([mo.md("### 技能近鄰與相似度熱圖\n比較名稱與描述的向量；相似度不是實測誤派率，實際混淆請看路由評測筆記本。"), mo.hstack([mo.ui.table(_neighbors, page_size=10), mo.ui.table(_pairs, page_size=10)]), _fig])
    return


if __name__ == "__main__":
    app.run()
