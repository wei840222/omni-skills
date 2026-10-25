import marimo

__generated_with = "0.24.0"
app = marimo.App(width="full")


@app.cell
def _():
    import hashlib
    import importlib.util
    import json
    from decimal import Decimal
    from pathlib import Path

    import marimo as mo
    import matplotlib.pyplot as plt
    import pandas as pd

    return Decimal, Path, hashlib, importlib, json, mo, pd, plt


@app.cell
def _(Path, hashlib, importlib, json):
    experiment_root = Path(__file__).resolve().parent.parent
    run_dir = experiment_root / "datasets" / "harness-quality-20261025"
    load_issues = []
    artifact_inventory = []

    def read_artifact(path, required=False):
        if not path.is_file():
            if required:
                load_issues.append({"Artifact": str(path.relative_to(experiment_root)), "問題": "缺少檔案"})
            return None
        try:
            content = path.read_bytes()
            value = json.loads(content)
        except (OSError, ValueError) as error:
            load_issues.append({"Artifact": str(path.relative_to(experiment_root)), "問題": str(error)})
            return None
        artifact_inventory.append({"Artifact": str(path.relative_to(experiment_root)), "SHA256": hashlib.sha256(content).hexdigest()})
        return value

    _export = read_artifact(experiment_root / "reports" / "harness-quality-20261025.json") or {}
    pilot = read_artifact(experiment_root / "fixtures" / "harness_pilot_cases.json", required=True) or {}
    silver = read_artifact(run_dir / "m1-silver-labels.json") or read_artifact(experiment_root / "fixtures" / "harness_silver_annotations.json", required=True) or {}
    frozen_config = read_artifact(run_dir / "challenger-config.json") or _export.get("challenger_config", {})
    summaries = {}
    comparisons = []
    for _phase in ("development", "holdout"):
        for _path in sorted((run_dir / _phase).glob("*-summary.json")):
            _summary = read_artifact(_path)
            if isinstance(_summary, dict) and "variant" in _summary:
                summaries[f"{_phase} / {_summary['variant']}"] = _summary
            elif _summary is not None:
                load_issues.append({"Artifact": str(_path.relative_to(experiment_root)), "問題": "缺少 variant；不可計分"})
        for _path in sorted((run_dir / _phase).glob("*comparison.json")):
            _comparison = read_artifact(_path)
            if isinstance(_comparison, dict):
                _entries = _comparison.get("comparisons_to_original_baseline")
                if _entries is None:
                    _entries = {_comparison.get("challenger", _path.stem): _comparison}
                for _entry in _entries.values():
                    comparisons.append({"phase": _phase, "source": _path.name, **_entry})
    if not summaries:
        summaries = _export.get("summaries", {})
    if not comparisons:
        comparisons = _export.get("comparisons", [])
    task_report = read_artifact(run_dir / "task-results.json") or _export.get("task_results")
    task_supplement = read_artifact(run_dir / "task-results-supplement.json") or _export.get("task_supplement")
    labels_by_id = {_row["id"]: _row for _row in silver.get("annotations", [])}
    cases_by_id = {_row["id"]: _row for _row in pilot.get("cases", [])}
    _spec = importlib.util.spec_from_file_location("harness_metrics", experiment_root / "scripts" / "harness_metrics.py")
    _metrics = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(_metrics)
    best_set_score = _metrics.best_set_score
    return (
        artifact_inventory,
        best_set_score,
        cases_by_id,
        comparisons,
        frozen_config,
        labels_by_id,
        load_issues,
        pilot,
        run_dir,
        silver,
        summaries,
        task_report,
        task_supplement,
    )


@app.cell
def _(frozen_config, load_issues, mo, pd, pilot, silver, summaries):
    _coverage = []
    for _phase in ("development", "holdout"):
        _labels = [_row for _row in silver.get("annotations", []) if _row.get("split") == _phase]
        _coverage.append({"階段": _phase, "標記案例": len(_labels), "Resolved": sum(not _row.get("uncertain", True) for _row in _labels), "Uncertain（排除主指標）": sum(_row.get("uncertain", True) for _row in _labels), "已讀 summary": sum(_key.startswith(_phase + " / ") for _key in summaries)})
    _items = [mo.md(f"""
    # Skill harness 品質實驗

    公開技能目錄 **{pilot.get('public_catalog_skill_count', '未記錄')}** 個技能；pilot **{len(pilot.get('cases', []))}** 題。
    這是獨立 AI 標記、來源裁決後凍結的 **silver labels，非 human gold**。
    主指標為 **family-macro set F1**：各題與完整 acceptable sets 比較，再先平均同一 family、最後等權平均 family。
    舊 notebook 的 owning-skill Top-1 衡量不同問題，不能直接當成本實驗的基準。

    development 選擇：`{frozen_config.get('developmentDecision', {}).get('decision', '尚未凍結')}`。
    holdout 僅檢查事前凍結的 diagnostic contender；不據此再調參，也不代表 production 改善。
    本頁只讀本機 artifacts，不呼叫模型；執行後若有新結果，請重新執行載入 cell 或重開 notebook。
    """), mo.ui.table(pd.DataFrame(_coverage), selection=None)]
    for _phase in ("development", "holdout"):
        if not any(_key.startswith(_phase + " / ") for _key in summaries):
            _items.append(mo.callout(mo.md(f"`{_phase}` 尚無 summary。先由既有執行流程完成 capture、selector 與 `scripts/summarize_harness_variants.py` 彙整；本頁不啟動實驗。"), kind="warn"))
    if load_issues:
        _items.extend([mo.md("### 載入問題\n修復檔案或完成寫入後，重新執行載入 cell。"), mo.ui.table(pd.DataFrame(load_issues), selection=None)])
    mo.vstack(_items)
    return


@app.cell
def _(mo, pd, plt, summaries):
    metric_rows = []
    for _key, _summary in summaries.items():
        _metrics = _summary.get("metrics", {})
        _macro = _metrics.get("family_macro", {})
        _coverage = _metrics.get("coverage", {})
        _fp = _metrics.get("no_skill_false_positive", {})
        metric_rows.append({"階段 / Variant": _key, "狀態": _summary.get("status"), "證據": _summary.get("evidence_status"), "Family set F1": _macro.get("f1"), "Precision": _macro.get("precision"), "Recall": _macro.get("recall"), "Exact set": _macro.get("exact"), "Resolved / Total": f"{_coverage.get('resolved_cases', '?')} / {_coverage.get('total_cases', '?')}", "Resolved families": _coverage.get("resolved_families"), "No-skill FP / Total": f"{_fp.get('count', '?')} / {_fp.get('total', '?')}", "執行失敗": _metrics.get("reliability", {}).get("failure_count")})
    _items = [mo.md("## 路由結果\nUncertain 不進入主指標；執行失敗與空候選池分別保留。Exact set 要求整組技能完全相等。")]
    if metric_rows:
        _items.append(mo.ui.table(pd.DataFrame(metric_rows), selection=None, page_size=10))
        _plot_rows = [_row for _row in metric_rows if _row["Family set F1"] is not None]
        if _plot_rows:
            _fig, _ax = plt.subplots(figsize=(12, max(3, len(_plot_rows) * 0.45)))
            _ax.barh([_row["階段 / Variant"] for _row in _plot_rows][::-1], [_row["Family set F1"] for _row in _plot_rows][::-1])
            _ax.set(xlim=(0, 1), xlabel="Family-macro set F1", title="Measured routing quality")
            _fig.tight_layout()
            _items.append(_fig)
    mo.vstack(_items)
    return


@app.cell
def _(comparisons, mo, pd):
    _rows, _checks = [], []
    for _comparison in comparisons:
        _interval = _comparison.get("paired_family_bootstrap", {})
        _adoption = _comparison.get("adoption") or {}
        _rows.append({"階段": _comparison["phase"], "來源": _comparison["source"], "Baseline": _comparison.get("baseline"), "Challenger": _comparison.get("challenger"), "Δ family F1": _comparison.get("family_macro_f1_delta"), "CI lower": _interval.get("lower"), "CI upper": _interval.get("upper"), "Confidence": _interval.get("confidence"), "Families": _interval.get("families"), "Replicates": _interval.get("replicates"), "採用判定": _adoption.get("decision", "尚無充分證據"), "新增 no-skill FP": ", ".join(_comparison.get("new_no_skill_false_positive_ids", []))})
        for _name, _passed in _adoption.get("checks", _comparison.get("checks", {})).items():
            _checks.append({"階段": _comparison["phase"], "來源": _comparison["source"], "Challenger": _comparison.get("challenger"), "Gate": _name, "通過": _passed})
    _items = [mo.md("## 配對比較與決策\n區間來自同一 intent family 的配對 bootstrap；採用判定直接讀取凍結規則產生的 report。Development 的比較供選擇使用，不是獨立 holdout 結論。")]
    if _rows:
        _items.append(mo.ui.table(pd.DataFrame(_rows), selection=None, page_size=10))
    else:
        _items.append(mo.md("尚無 comparison report。完成同階段的配對 summary 後，再由 summary 工具產生比較。"))
    if _checks:
        _items.append(mo.accordion({"採用條件明細": mo.ui.table(pd.DataFrame(_checks), selection=None, page_size=12)}))
    mo.vstack(_items)
    return


@app.cell
def _(Decimal, mo, pd, summaries):
    _rows, _query_rows = [], []
    for _key, _summary in summaries.items():
        _resource = _summary.get("resources", {})
        _tokens = _resource.get("selector_actual_new_billed_input_tokens")
        _price = _resource.get("jev_usd_per_million")
        _actual_usd = str(Decimal(_tokens) * Decimal(_price) / 1_000_000) if _tokens is not None and _price is not None else None
        _rows.append({"階段 / Variant": _key, "Selector service p95 ms": _resource.get("selector_latency_p95_ms"), "Selector input tokens p95": _resource.get("selector_input_tokens_p95"), "有 service 觀測 / 應觀測": f"{_resource.get('service_observations', '?')} / {_resource.get('service_required', '?')}", "空池跳過": _resource.get("skipped_empty_pools"), "新外送 selector tokens": _tokens, "按宣告單價換算 USD": _actual_usd, "Jev USD / 1M": _price, "Shared query p95 ms": _resource.get("shared_query_latency_p95_ms"), "Budget OK": _resource.get("budget", {}).get("ok"), "Hard timeout OK": _resource.get("hard_timeout_ok")})
        for _provider, _usage in _resource.get("shared_query_by_provider", {}).items():
            _query_rows.append({"階段 / Variant": _key, "Provider": _provider, **_usage})
    _items = [mo.md("""
    ## 延遲與費用

    Selector p95 使用原始 service observations；cache 的本機 wall time 另列於案例診斷。
    費用 gate 使用 selector input tokens p95、共用宣告單價；金額是按該單價換算，非供應商帳單。
    「新外送」只計該 variant checkpoint 中的 remote selector 請求；共用 query observations 可在多個 variant 重複出現，**不能跨列加總成總支出**。
    Shared query + selector 為重建時間，不是冷啟動端到端 gateway latency。
    Expansion 無宣告單價時保留空值，不視為零費用。
    """)]
    if _rows:
        _items.append(mo.ui.table(pd.DataFrame(_rows), selection=None, page_size=10))
    if _query_rows:
        _items.append(mo.accordion({"共用 query provider 觀測（重用、不可重複加總）": mo.ui.table(pd.DataFrame(_query_rows), selection=None, page_size=10)}))
    mo.vstack(_items)
    return


@app.cell
def _(mo, summaries):
    diagnostic_choice = mo.ui.dropdown(options=list(summaries), value=next(iter(summaries), None), label="診斷 Variant")
    mo.vstack([mo.md("## 案例與候選階段診斷\n以下是凍結 silver 標記與模型輸出的離線比較，不參與推論。Uncertain 顯示標記狀態與原因，F1 留空。"), diagnostic_choice])
    return (diagnostic_choice,)


@app.cell
def _(
    best_set_score,
    cases_by_id,
    diagnostic_choice,
    labels_by_id,
    mo,
    pd,
    summaries,
):
    _summary = summaries.get(diagnostic_choice.value, {})
    _diagnostics, _uncertain = [], []
    for _record in _summary.get("records", []):
        _id = _record["id"]
        _label = labels_by_id.get(_id, {})
        _prediction = _record.get("prediction", {})
        _skills = _prediction.get("skills", [])
        _score = None
        if _label and not _label.get("uncertain", True):
            _score = best_set_score(_skills, _label["acceptable_sets"])["f1"] if _prediction.get("status") in ("completed", "skipped-empty-pool") else 0.0
        _stages = _record.get("candidate_coverage_stages", {})
        _diagnostics.append({"ID": _id, "Family": _label.get("family_id"), "Type": _label.get("type"), "問題": cases_by_id.get(_id, {}).get("latest"), "狀態": _prediction.get("status"), "Uncertain": _label.get("uncertain", True), "Set F1": _score, "Acceptable sets（silver）": str(_label.get("acceptable_sets", [])), "Selected skills": ", ".join(_skills), "候選": ", ".join(_record.get("candidates", [])), "Pool complete": _stages.get("after_pool", {}).get("complete_set"), "Gate complete": _stages.get("semantic_gate", {}).get("complete_set"), "Union complete": _stages.get("union_candidates", {}).get("complete_set"), "Selector service ms": _record.get("selector_original_service_ms"), "Selector local wall ms": _record.get("selector_local_wall_ms"), "Transport": _record.get("selector_transport_source"), "Reconstructed query + selector ms": _record.get("reconstructed_shared_query_plus_selector_ms")})
    for _label in labels_by_id.values():
        if _label.get("uncertain"):
            _uncertain.append({"ID": _label["id"], "Split": _label.get("split"), "Family": _label.get("family_id"), "排除原因": _label.get("uncertainty_reason")})
    _items = []
    if _diagnostics:
        _items.append(mo.ui.table(pd.DataFrame(_diagnostics).sort_values("Set F1", na_position="last"), selection=None, page_size=8))
    else:
        _items.append(mo.md("選擇已有 records 的 summary；未完成 capture 時不顯示替代案例。"))
    if _summary.get("stage_coverage"):
        _items.append(mo.accordion({"各候選階段的 family-macro coverage": mo.ui.table(pd.DataFrame([{"Stage": _stage, **_values} for _stage, _values in _summary["stage_coverage"].items()]), selection=None)}))
    if _uncertain:
        _items.extend([mo.md("### 全部 uncertain 排除明細"), mo.ui.table(pd.DataFrame(_uncertain), selection=None)])
    mo.vstack(_items)
    return


@app.cell
def _(mo, pd, task_report):
    _items = [mo.md("## 實際任務的配對結果\n這組有界任務比較 baseline 與 frozen challenger。沒有 no-harness control，不能據此宣稱 harness 相對無 harness 的因果增益；也不能直接推廣到 production。")]
    if not isinstance(task_report, dict) or not task_report.get("pairs"):
        _items.append(mo.callout(mo.md("尚無實際配對 task report。完成獨立任務執行與 grader 後，將 `task-results.json` 寫入本次 run 目錄；路由 F1 不會代替任務成功率。"), kind="warn"))
    else:
        _rows = []
        for _pair in task_report["pairs"]:
            _row = {"ID": _pair.get("id"), "Task": _pair.get("task")}
            for _arm in ("baseline", "challenger"):
                _result = _pair.get(_arm, {})
                for _field in ("status", "success", "artifact_sha256"):
                    _row[f"{_arm} {_field}"] = _result.get(_field)
            _rows.append(_row)
        _items.extend([mo.md(f"Report 狀態：`{task_report.get('status', '未記錄')}` · **{len(_rows)}** 組配對。只顯示實際結果，不讀取隱藏 grader/oracle。"), mo.ui.table(pd.DataFrame(_rows), selection=None, page_size=12)])
        _complete = [row for row in task_report["pairs"] if all(type(row.get(arm, {}).get("success")) is bool for arm in ("baseline", "challenger"))]
        if _complete:
            _items.append(mo.ui.table(pd.DataFrame([{"Arm": arm, "已計分配對": len(_complete), "Success": sum(row[arm]["success"] for row in _complete), "Success rate": sum(row[arm]["success"] for row in _complete) / len(_complete)} for arm in ("baseline", "challenger")]), selection=None))
        if task_report.get("limitations"):
            _items.append(mo.md("\n".join("- " + str(item) for item in task_report["limitations"])))
    mo.vstack(_items)
    return


@app.cell
def _(artifact_inventory, frozen_config, json, mo, pd, run_dir, silver):
    _config = {key: frozen_config.get(key) for key in ("status", "frozenAt", "baseline", "challenger")}
    _pins = {key: silver.get(key) for key in ("dataset_id", "annotation_version", "rubric_version", "annotation_origin", "frozen_at_utc", "cases_sha256", "contract_sha256", "protocol_sha256")}
    mo.accordion({"資料來源與凍結識別": mo.vstack([mo.md(f"Run 目錄：`{run_dir}`\n\n此頁呈現 summary 工具的結果；下列 SHA256 為本次讀取的檔案指紋，並非重新驗證所有原始 checkpoints。"), mo.md("```json\n" + json.dumps({"labels": _pins, "frozen_config": _config}, ensure_ascii=False, indent=2) + "\n```"), mo.ui.table(pd.DataFrame(artifact_inventory), selection=None, page_size=10)])})
    return


@app.cell
def _(best_set_score, cases_by_id, labels_by_id, mo, pd, summaries):
    _groups = {}
    for _key, _summary in summaries.items():
        for _record in _summary.get("records", []):
            _label = labels_by_id.get(_record["id"], {})
            if _label.get("uncertain") or not _label.get("acceptable_sets"):
                continue
            _group = _groups.setdefault((_key, _label.get("type")), {"families": {}, "cases": 0, "context": 0})
            _prediction = _record.get("prediction", {})
            _score = best_set_score(_prediction.get("skills", []), _label["acceptable_sets"])
            if _prediction.get("status") not in {"completed", "skipped-empty-pool"}:
                _score = dict.fromkeys(("f1", "precision", "recall", "exact"), 0.0)
            _group["families"].setdefault(_label["family_id"], []).append(_score)
            _group["cases"] += 1
            _group["context"] += bool(cases_by_id.get(_record["id"], {}).get("conversation"))
    _rows = []
    for (_key, _kind), _group in _groups.items():
        _row = {"階段 / Variant": _key, "類型": _kind, "可評分題數": _group["cases"], "Intent families": len(_group["families"]), "有對話前文": _group["context"]}
        for _metric in ("f1", "precision", "recall", "exact"):
            _family_values = [sum(_s[_metric] for _s in _scores) / len(_scores) for _scores in _group["families"].values()]
            _row[_metric] = sum(_family_values) / len(_family_values)
        _rows.append(_row)
    mo.vstack([mo.md("## 單輪與多輪分項\n多輪案例的公開合成前文有傳入 host Decision 的 conversation_context。其餘案例是獨立任務；各變體使用相同前文。下表排除 uncertain，按 intent family 平均；holdout 的 followup 僅一個家族、五題，不能外推為一般長對話準確率。"), mo.ui.table(pd.DataFrame(_rows), selection=None, page_size=10)])
    return


@app.cell
def _(mo, pd, task_supplement):
    _items = [mo.md("## 任務驗收器的相容性補充\n原始凍結成績保留為兩臂各 10／12；t05 與 t12 的四份產物被執行限制攔截，未進入語義測試，不能直接歸為答案錯誤。獨立 source reviewer 核對公開題目後，另以最小 API 相容調整驗證同一批產物；沒有重跑模型或修改解答。補充成績與主要結果分開，也不作為採用依據。")]
    if task_supplement:
        _rows = [{"ID": _row["id"], "Arm": _row["arm"], "補充語義案例通過": _row["passed"], "Artifact SHA256": _row["artifact_sha256"]} for _row in task_supplement.get("results", [])]
        _items.append(mo.ui.table(pd.DataFrame(_rows), selection=None))
        _items.append(mo.md("相容性變更僅包含 SQL typeof、已審查的 text.split(newline) 與 RecursionError；原案例、預期值及資源限制保留。此環境仍不是 OS sandbox。"))
    else:
        _items.append(mo.md("尚無相容性補充結果。"))
    mo.vstack(_items)
    return


if __name__ == "__main__":
    app.run()
