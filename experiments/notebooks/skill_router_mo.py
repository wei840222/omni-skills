import marimo

__generated_with = "0.24.0"
app = marimo.App(width="full")


@app.cell
def _():
    import json
    from pathlib import Path
    from collections import Counter
    import marimo as mo
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    return Counter, Path, json, mo, pd, plt, sns


@app.cell
def _(Path, json, mo):
    _result_path = Path(__file__).resolve().parent.parent / "datasets" / "routing_benchmark_results.json"
    mo.stop(not _result_path.exists(), mo.md("""
    # 技能路由實驗

    尚未找到實際結果。請在 `experiments/` 依序執行：

    ```bash
    uv run python scripts/prepare_experiment_datasets.py
    uv run python scripts/generate_bm25_prompts.py
    uv run python scripts/generate_embeddings.py --embed-model text-embedding-3-small --dimension 1536
    uv run python scripts/run_routing_evaluation.py --embed-model text-embedding-3-small --dimension 1536
    ```

    筆記本只顯示量測結果，不會呼叫模型或產生替代數字。
    """))
    benchmark = json.loads(_result_path.read_text(encoding="utf-8"))
    cases = benchmark["detailed_cases"]
    metadata = benchmark["metadata"]
    mo.stop(not cases, mo.md("結果檔沒有案例，請重新執行完整評測。"))
    return benchmark, cases, metadata


@app.cell
def _(benchmark, cases, json, metadata, mo, pd):
    _skill_count = metadata.get("skill_count", len({_c["skill"] for _c in cases}))
    mo.vstack([
        mo.md(f"""
        # 完整技能庫路由評測

        **{_skill_count:,} 個技能 · {len(cases):,} 題 · {len(benchmark['metrics_by_pipeline'])} 種語料表示**

        Embedding：`{metadata.get('embedding_model', '未記錄')}` · 維度：`{metadata.get('dimension', '未記錄')}` · Rerank：`{metadata.get('rerank_model', '未記錄')}`

        Corpus：`{metadata.get('corpus_hash', '未記錄')}`

        所有路徑使用原始問題；正解只供計分，舊的 `bm25_prompt` 不參與檢索。
        標籤來自各技能自身測試題，不代表獨立盲測或唯一可接受的技能。
        """),
        mo.accordion({"執行版本、模型與量測規則": mo.md("```json\n" + json.dumps(metadata, ensure_ascii=False, indent=2) + "\n```")}),
        mo.md("### 本次測試問題"),
        mo.ui.table(pd.DataFrame([{"Query ID": _c["query_id"], "Target skill": _c["skill"], "Original query": _c["natural_prompt"]} for _c in cases]), page_size=8),
    ])
    return


@app.cell
def _(benchmark, mo, pd, plt, sns):
    _rows = []
    for _collection, _pipelines in benchmark["metrics_by_pipeline"].items():
        for _pipeline, _m in _pipelines.items():
            _rows.append({"Collection": _collection, "Pipeline": _pipeline, "Hit@1 (%)": _m["hit@1"], "Hit@3 (%)": _m["hit@3"], "Hit@5 (%)": _m["hit@5"], "MRR@10": _m["mrr@10"], "Stage ms (mean, embedding excluded)": _m.get("retrieval_latency_ms_mean"), "Rerank service ms (mean)": _m.get("service_latency_ms_mean")})
    metrics_table = pd.DataFrame(_rows)
    sns.set_theme(style="whitegrid")
    _fig, _axes = plt.subplots(1, 2, figsize=(16, 5))
    for _ax, _metric in zip(_axes, ["Hit@1 (%)", "MRR@10"]):
        sns.barplot(data=metrics_table, x="Pipeline", y=_metric, hue="Collection", ax=_ax)
        _ax.tick_params(axis="x", rotation=20)
        _ax.set_title(_metric + " by collection")
        _ax.set_ylim(0, 105 if _metric.startswith("Hit") else 1.05)
    _fig.tight_layout()
    mo.vstack([mo.md("""
    ### 四種路由方式的實際結果

    BM25 使用原始問題的詞彙檢索；Vector 對技能切塊取最高餘弦相似度；
    Hybrid RRF 融合兩者名次；Hybrid + Rerank 由設定的遠端模型重排候選。
    Hit@K 是正解出現在前 K 名的比例，MRR@10 是前十名內的倒數名次平均。
    """), mo.ui.table(metrics_table, page_size=12), _fig])
    return (metrics_table,)


@app.cell
def _(benchmark, mo):
    collection_choice = mo.ui.dropdown(options=list(benchmark["metrics_by_pipeline"]), value=list(benchmark["metrics_by_pipeline"])[0], label="案例語料")
    pipeline_choice = mo.ui.dropdown(options={"BM25": "bm25", "Vector": "vector", "Hybrid RRF": "hybrid", "Hybrid + Rerank": "rerank"}, value="Vector", label="診斷路徑")
    mo.hstack([collection_choice, pipeline_choice], justify="start")
    return collection_choice, pipeline_choice


@app.cell
def _(cases, mo, pd, pipeline_choice, plt):
    _records, _examples = [], []
    for _before, _after in [("name-description", "full"), ("full", "full-references")]:
        _counts = {"Unchanged correct": 0, "Rescue": 0, "Regression": 0, "Unchanged incorrect": 0}
        for _case in cases:
            _old = _case["rankings"][_before][pipeline_choice.value]
            _new = _case["rankings"][_after][pipeline_choice.value]
            _old_ok = bool(_old) and _old[0] == _case["skill"]
            _new_ok = bool(_new) and _new[0] == _case["skill"]
            _status = "Unchanged correct" if _old_ok and _new_ok else "Rescue" if not _old_ok and _new_ok else "Regression" if _old_ok and not _new_ok else "Unchanged incorrect"
            _counts[_status] += 1
            if _status in ("Rescue", "Regression"):
                _examples.append({"Transition": f"{_before} -> {_after}", "Status": _status, "Query ID": _case["query_id"], "Target skill": _case["skill"], "Before top-1": _old[0] if _old else None, "After top-1": _new[0] if _new else None, "Original query": _case["natural_prompt"]})
        _records.append({"Transition": f"{_before} -> {_after}", **_counts})
    _df = pd.DataFrame(_records).set_index("Transition")
    _fig, _ax = plt.subplots(figsize=(12, 4))
    _df.plot.barh(stacked=True, color=["#2ecc71", "#3498db", "#e74c3c", "#95a5a6"], ax=_ax)
    _ax.set_title("Top-1 transitions: " + pipeline_choice.value)
    _ax.set_xlabel("Queries")
    _ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.2), ncol=4)
    _fig.tight_layout()
    mo.vstack([mo.md("### 語料擴展後的救援與退步\n每一階段分別比較擴展前後的 Top-1；排名變化本身不證明失敗原因。"), _fig, mo.ui.table(_df.reset_index(), page_size=2), mo.ui.table(pd.DataFrame(_examples), page_size=8)])
    return


@app.cell
def _(Counter, cases, collection_choice, mo, pd, pipeline_choice, plt):
    _errors, _intruders = [], Counter()
    for _case in cases:
        _ranking = _case["rankings"][collection_choice.value][pipeline_choice.value]
        if not _ranking or _ranking[0] != _case["skill"]:
            _prediction = _ranking[0] if _ranking else "(no result)"
            _intruders[_prediction] += 1
            _errors.append({"Query ID": _case["query_id"], "Target skill": _case["skill"], "Predicted skill": _prediction, "Target rank": str(_ranking.index(_case["skill"]) + 1) if _case["skill"] in _ranking else ">" + str(len(_ranking)), "Original query": _case["natural_prompt"]})
    _top = pd.DataFrame(_intruders.most_common(15), columns=["Predicted skill", "Incorrect top-1 count"])
    _items = [mo.md(f"### 誤派技能與錯誤案例\n`{collection_choice.value}` / `{pipeline_choice.value}`：**{len(_errors):,}** 題 Top-1 未命中。")]
    if not _top.empty:
        _fig, _ax = plt.subplots(figsize=(12, 5))
        _ax.barh(_top["Predicted skill"][::-1], _top["Incorrect top-1 count"][::-1], color="#e67e22")
        _ax.set_title("Most frequent incorrect top-1 predictions")
        _ax.set_xlabel("Queries")
        _fig.tight_layout()
        _items.extend([_fig, mo.ui.table(_top, page_size=8)])
    _items.append(mo.ui.table(pd.DataFrame(_errors), page_size=8))
    mo.vstack(_items)
    return


@app.cell
def _(cases, collection_choice, mo, pd, plt, sns):
    _rows, _hard = [], []
    for _case in cases:
        _length = len(_case["natural_prompt"].split())
        _bucket = "Short (<=15 words)" if _length <= 15 else "Medium (16-35 words)" if _length <= 35 else "Long (>35 words)"
        _all_missed = True
        for _pipeline, _ranking in _case["rankings"][collection_choice.value].items():
            _hit = bool(_ranking) and _ranking[0] == _case["skill"]
            _all_missed = _all_missed and not _hit
            _rows.append({"Query length": _bucket, "Pipeline": _pipeline, "Hit@1 (%)": 100 * _hit})
        if _all_missed:
            _hard.append({"Query ID": _case["query_id"], "Target skill": _case["skill"], "Original query": _case["natural_prompt"]})
    _length_df = pd.DataFrame(_rows).groupby(["Query length", "Pipeline"], as_index=False)["Hit@1 (%)"].mean()
    _fig, _ax = plt.subplots(figsize=(12, 4))
    sns.barplot(data=_length_df, x="Query length", y="Hit@1 (%)", hue="Pipeline", ax=_ax)
    _ax.set_title("Accuracy by query length: " + collection_choice.value)
    _ax.set_ylim(0, 105)
    _fig.tight_layout()
    mo.vstack([mo.md("### 問題長度與共同失敗案例\n長度以空白分詞計算；中文等無空白的語言不適合據此比較語意複雜度。"), _fig, mo.md(f"在 `{collection_choice.value}` 中，四種路徑皆 Top-1 未命中：**{len(_hard):,}** 題。"), mo.ui.table(pd.DataFrame(_hard), page_size=8)])
    return


@app.cell
def _(cases, json, metadata, metrics_table, mo, pd, plt, sns):
    _timing = []
    for _case in cases:
        for _collection, _pipelines in _case.get("latency_ms", {}).items():
            for _pipeline, _value in _pipelines.items():
                _service = _case.get("service_latency_ms", {}).get(_collection, {}).get(_pipeline, 0.0)
                _timing.append({"Collection": _collection, "Pipeline": _pipeline, "Stage ms (embedding excluded)": _value, "Rerank service ms": _service})
    _items = [mo.md("""
    ### 實際延遲與準確率

    Stage 是本輪各路徑的處理時間；rerank 路徑包含模型服務時間，向量矩陣的批次耗時按題數攤提。
    Rerank service 是模型請求量測，請同時查看執行紀錄中的快取命中數。
    查詢 embedding 的批次 API 時間另列於下方，未混入 Stage。
    這些數字不能直接當成單筆冷啟動的端到端延遲。
    """)]
    if _timing:
        _summary = pd.DataFrame(_timing).groupby(["Collection", "Pipeline"])[["Stage ms (embedding excluded)", "Rerank service ms"]].agg(["mean", "median", lambda _x: _x.quantile(0.95)])
        _summary.columns = [" ".join(_parts).replace("<lambda_0>", "p95") for _parts in _summary.columns]
        _items.append(mo.ui.table(_summary.reset_index(), page_size=12))
    _plot = metrics_table.dropna(subset=["Stage ms (mean, embedding excluded)"]).copy()
    if not _plot.empty:
        _fig, _ax = plt.subplots(figsize=(12, 5))
        sns.scatterplot(data=_plot, x="Stage ms (mean, embedding excluded)", y="Hit@1 (%)", hue="Pipeline", style="Collection", s=140, ax=_ax)
        _ax.set_title("Measured stage time vs accuracy (embedding excluded)")
        _fig.tight_layout()
        _items.append(_fig)
    _embedding_info = metadata.get("embedding_api_timing", metadata.get("api_timing", {}))
    _items.append(mo.md("Embedding API 紀錄：\n```json\n" + json.dumps(_embedding_info, ensure_ascii=False, indent=2) + "\n```"))
    mo.vstack(_items)
    return


if __name__ == "__main__":
    app.run()
