import marimo

__generated_with = "0.24.0"
app = marimo.App(width="full")


@app.cell(hide_code=True)
def _():
    import hashlib
    import importlib.util
    from pathlib import Path
    from time import perf_counter

    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from matplotlib.collections import LineCollection, PolyCollection
    from matplotlib.patches import FancyArrowPatch

    return (
        FancyArrowPatch,
        LineCollection,
        Path,
        PolyCollection,
        hashlib,
        importlib,
        mo,
        np,
        pd,
        perf_counter,
        plt,
    )


@app.cell(hide_code=True)
def _(Path, hashlib, importlib, mo, pd, perf_counter):
    experiment_root = Path(__file__).resolve().parent.parent
    graph_path = experiment_root.parent / "ontology" / "graph.jsonl"
    mo.stop(not graph_path.is_file(), mo.md("# 技能關聯分布\n找不到 `ontology/graph.jsonl`；請先建立技能圖，再重新執行本頁。"))
    _spec = importlib.util.spec_from_file_location("ontology_analysis", experiment_root / "scripts" / "ontology_analysis.py")
    graph_tools = importlib.util.module_from_spec(_spec)
    _spec.loader.exec_module(graph_tools)
    _start = perf_counter()
    _before = graph_path.read_bytes()
    try:
        entities, relations, operation_count = graph_tools.read_graph(graph_path)
    except (OSError, ValueError) as _error:
        mo.stop(True, mo.md(f"# 技能關聯分布\n圖資料無法重播，請修正來源後重新執行。\n\n```text\n{_error}\n```"))
    mo.stop(graph_path.read_bytes() != _before, mo.md("讀取期間 graph.jsonl 有更新，請重新執行本頁。"))
    graph_sha256 = hashlib.sha256(_before).hexdigest()
    analysis_result = graph_tools.analyze_graph(entities, relations)
    graph_summary = analysis_result["summary"]
    nodes_df = pd.DataFrame(analysis_result["nodes"])
    edges_df = pd.DataFrame(analysis_result["edges"])
    read_ms = 1000 * (perf_counter() - _start)
    mo.stop(not entities, mo.md("# 技能關聯分布\n操作日誌目前沒有有效技能節點，請先匯入技能。"))
    return (
        edges_df,
        entities,
        graph_sha256,
        graph_summary,
        graph_tools,
        nodes_df,
        operation_count,
        read_ms,
        relations,
    )


@app.cell(hide_code=True)
def _(graph_sha256, graph_summary, mo, operation_count, read_ms):
    mo.vstack([
        mo.md(f"""
        # 技能關聯分布

        **{graph_summary['node_count']:,} 個技能 · {graph_summary['edge_count']:,} 條有向關聯 · {operation_count:,} 筆歷史操作**

        先依序重播 `ontology/graph.jsonl`，再分析目前有效的節點與邊；撤回的歷史關係不計入分布。
        每條箭頭由宣告關聯的技能指向目標技能，理由保留作者原文。

        - 平均入度／出度：**{graph_summary['average_degree']:.2f}**。
        - 有反向宣告的邊：**{graph_summary['reciprocal_edges']:,}／{graph_summary['edge_count']:,}（{graph_summary['reciprocity']:.1%}）**，對應 **{graph_summary['reciprocal_pairs']:,} 組雙向配對**。
        - 完全沒有 incoming 或 outgoing 的孤立技能：**{graph_summary['isolated_count']:,}**。
        - 有向圖密度：**{graph_summary['density']:.3%}**，分母為 N × (N − 1)，不含自我關聯。

        關聯數不是品質分數，沒有邊也不表示無關；有幫助的技能多選可以接受，應避免的是明顯無關的載入。
        """),
        mo.accordion({"來源與讀取時間": mo.md(f"Graph SHA256：`{graph_sha256}`\n\n本次讀取、重播與統計：{read_ms:.1f} ms。不呼叫 embedding、分類或 rerank 模型。")}),
    ])
    return


@app.cell(hide_code=True)
def _(mo, nodes_df, np, plt):
    _bounds = [0, 1, 2, 4, 6, 11, 21, float("inf")]
    _labels = ["0", "1", "2-3", "4-5", "6-10", "11-20", "21+"]
    _fig, _axes = plt.subplots(1, 2, figsize=(15, 4))
    for _ax, _column, _title, _color in zip(_axes, ["in_degree", "out_degree"], ["Incoming degree", "Outgoing degree"], ["#167c80", "#bd6b27"]):
        _counts, _ = np.histogram(nodes_df[_column], bins=_bounds)
        _ax.bar(_labels, _counts, color=_color)
        _ax.set(title=_title, xlabel="Directed degree", ylabel="Skills")
        for _index, _count in enumerate(_counts):
            _ax.text(_index, _count, str(_count), ha="center", va="bottom", fontsize=9)
    _fig.tight_layout()
    mo.vstack([mo.md("## 入度與出度\n入度是被多少技能指向；出度是自己宣告了多少目標。兩邊平均相同，但分布可能差很多。"), _fig])
    return


@app.cell(hide_code=True)
def _(mo, nodes_df, plt):
    _fig, _axes = plt.subplots(1, 2, figsize=(15, 6))
    for _ax, _column, _title, _color in zip(_axes, ["in_degree", "out_degree"], ["Most referenced skills (incoming)", "Most declared targets (outgoing)"], ["#167c80", "#bd6b27"]):
        _top = nodes_df.sort_values([_column, "name"], ascending=[False, True]).head(15).iloc[::-1]
        _ax.barh(_top["name"], _top[_column], color=_color)
        _ax.set(title=_title, xlabel="Directed edges")
    _fig.tight_layout()
    _most_referenced = nodes_df.sort_values(["in_degree", "name"], ascending=[False, True]).iloc[0]
    _max_out = int(nodes_df["out_degree"].max())
    _max_out_names = ", ".join(nodes_df.loc[nodes_df["out_degree"] == _max_out, "name"].sort_values())
    _mode_out = int(nodes_df["out_degree"].mode().iloc[0])
    _mode_count = int((nodes_df["out_degree"] == _mode_out).sum())
    _zero_out = int((nodes_df["out_degree"] == 0).sum())
    _incoming_only = int((nodes_df["role"] == "incoming_only").sum())
    mo.vstack([mo.md(f"""
    ## 關聯集中在哪些技能

    - 出度最常見是 **{_mode_out} 條**，共有 **{_mode_count:,} 個技能**；出度最高為 **{_max_out} 條**，是 `{_max_out_names}`。
    - 入度最高是 **{_most_referenced['name']}（{_most_referenced['in_degree']} 次）**。入度較集中，代表一些技能被多個作者拿來作關聯目標；不等於它在每個任務都適用。
    - 沒有 outgoing 的 **{_zero_out:,} 個技能**中，**{_incoming_only:,} 個**仍有 incoming。單看自己是否宣告關聯，會漏掉其他技能對它的引用。

    這是作者宣告的引用與連結分布，不是使用量、任務重要性或路由準確率排名。
    """), _fig])
    return


@app.cell(hide_code=True)
def _(graph_summary, mo, pd, plt):
    _roles = graph_summary["roles"]
    _fig, _ax = plt.subplots(figsize=(12, 3))
    _ax.barh(["Both incoming and outgoing", "Incoming only", "Outgoing only", "Isolated"], [_roles["both"], _roles["incoming_only"], _roles["outgoing_only"], _roles["isolated"]], color=["#167c80", "#3d73b1", "#bd6b27", "#8b939e"])
    _ax.invert_yaxis()
    _ax.set(title="Node connectivity roles", xlabel="Skills")
    _fig.tight_layout()
    _components = pd.DataFrame([
        {"分量": "弱連通（忽略箭頭方向）", "數量": graph_summary["weak_component_count"], "最大分量技能數": graph_summary["largest_weak_component"]},
        {"分量": "強連通（沿箭頭彼此可達）", "數量": graph_summary["strong_component_count"], "最大分量技能數": graph_summary["largest_strong_component"]},
    ])
    mo.vstack([mo.md(f"""
        ## 圖的連通結構

        最大弱連通分量有 **{graph_summary['largest_weak_component']:,}** 個技能，表示忽略方向時它們能連成一片。
        最大強連通分量有 **{graph_summary['largest_strong_component']:,}** 個技能，表示其中任兩點都存在依箭頭方向往返的路徑。
        這些路徑只是結構統計，不代表應沿路載入全部技能，也不代表已驗證的依賴。
        """), _fig, mo.ui.table(_components, selection=None)] )
    return


@app.cell(hide_code=True)
def _(entities, graph_tools, perf_counter, relations):
    _start = perf_counter()
    graph_positions = graph_tools.graph_layout(entities, relations)
    layout_ms = 1000 * (perf_counter() - _start)
    return graph_positions, layout_ms


@app.cell(hide_code=True)
def _(FancyArrowPatch, LineCollection, PolyCollection, np, plt):
    def draw_relation_graph(entity_map, relation_rows, layout, node_rows, visible_ids=None, selected=None, title="Directed skill relations"):
        ids = sorted(entity_map if visible_ids is None else visible_ids)
        rows = {row["id"]: row for row in node_rows}
        colors = {"both": "#167c80", "incoming_only": "#3d73b1", "outgoing_only": "#bd6b27", "isolated": "#8b939e"}
        labels = {"both": "Both", "incoming_only": "Incoming only", "outgoing_only": "Outgoing only", "isolated": "Isolated"}
        fig, ax = plt.subplots(figsize=(16, 10))
        coords = np.array([layout[node] for node in ids])
        span = max(float(np.ptp(coords[:, 0])), float(np.ptp(coords[:, 1])), 1.0)
        pairs = {(edge["from"], edge["to"]) for edge in relation_rows}
        if len(relation_rows) > 250:
            segments, heads = [], []
            for edge in relation_rows:
                start, end = np.array(layout[edge["from"]]), np.array(layout[edge["to"]])
                delta = end - start
                length = float(np.linalg.norm(delta))
                if length < 1e-10:
                    continue
                direction = delta / length
                normal = np.array([-direction[1], direction[0]])
                gap = min(span * 0.006, length * 0.2)
                head_length = min(span * 0.009, length * 0.25)
                tip = end - direction * gap
                base = tip - direction * head_length
                segments.append([start + direction * gap, base])
                heads.append([tip, base + normal * head_length * 0.4, base - normal * head_length * 0.4])
            ax.add_collection(LineCollection(segments, colors="#667d86", linewidths=0.35, alpha=0.22, zorder=1))
            ax.add_collection(PolyCollection(heads, facecolors="#667d86", edgecolors="none", alpha=0.38, zorder=2))
        else:
            for edge in relation_rows:
                source, target = edge["from"], edge["to"]
                color = "#bd6b27" if source == selected else "#3d73b1" if target == selected else "#667d86"
                curve = 0.15 if (target, source) in pairs else 0.0
                ax.add_patch(FancyArrowPatch(layout[source], layout[target], arrowstyle="-|>", mutation_scale=13, shrinkA=10, shrinkB=10, connectionstyle=f"arc3,rad={curve}", color=color, alpha=0.75, linewidth=1.0, zorder=1))
        for role, color in colors.items():
            members = [node for node in ids if rows[node]["role"] == role]
            if members:
                xy = np.array([layout[node] for node in members])
                sizes = [12 + 8 * np.sqrt(rows[node]["total_degree"]) for node in members]
                ax.scatter(xy[:, 0], xy[:, 1], s=sizes, c=color, label=f"{labels[role]} ({len(members)})", edgecolors="white", linewidths=0.35, zorder=3)
        if selected is not None:
            ax.scatter(*layout[selected], s=180, facecolors="none", edgecolors="#202b32", linewidths=2, zorder=4)
        labelled = ids if len(ids) <= 50 else sorted(ids, key=lambda node: (-rows[node]["total_degree"], rows[node]["name"]))[:20]
        if selected is not None and selected not in labelled:
            labelled.append(selected)
        for node in labelled:
            ax.annotate(rows[node]["name"], layout[node], xytext=(4, 4), textcoords="offset points", fontsize=8, color="#26333a", zorder=5)
        ax.set_xlim(coords[:, 0].min() - span * 0.08, coords[:, 0].max() + span * 0.08)
        ax.set_ylim(coords[:, 1].min() - span * 0.08, coords[:, 1].max() + span * 0.08)
        ax.set_aspect("equal")
        ax.set_title(title)
        ax.axis("off")
        ax.legend(loc="upper left", frameon=False, fontsize=9)
        fig.tight_layout()
        return fig

    return (draw_relation_graph,)


@app.cell(hide_code=True)
def _(
    draw_relation_graph,
    entities,
    graph_positions,
    layout_ms,
    mo,
    nodes_df,
    relations,
):
    _fig = draw_relation_graph(entities, relations, graph_positions, nodes_df.to_dict("records"), title=f"Full directed graph: {len(entities)} skills / {len(relations)} edges")
    mo.vstack([mo.md(f"""
        ## 技能有向全圖

        每個點是一個技能；箭頭由來源指向目標。點的大小依入度＋出度，顏色依 incoming／outgoing 的連結角色。
        全部節點與邊均顯示；為避免重疊，只標出總度數最高的 20 個名稱。孤立技能排在右側獨立區域。

        使用固定種子的力導向配置，本次配置耗時 **{layout_ms:.0f} ms**。位置只方便看結構，距離不是語義相似度；互動選擇不會重新計算全圖配置。
        """), _fig])
    return


@app.cell(hide_code=True)
def _(entities, mo):
    _options = {entity["properties"]["name"]: identity for identity, entity in sorted(entities.items(), key=lambda item: item[1]["properties"]["name"])}
    skill_choice = mo.ui.dropdown(options=_options, value="aws" if "aws" in _options else next(iter(_options)), searchable=True, label="搜尋技能")
    direction_choice = mo.ui.dropdown(options={"雙向": "both", "只看自己指向誰": "outgoing", "只看誰指向自己": "incoming"}, value="雙向", label="關聯方向")
    mo.hstack([skill_choice, direction_choice], justify="start", wrap=True)
    return direction_choice, skill_choice


@app.cell(hide_code=True)
def _(
    direction_choice,
    draw_relation_graph,
    entities,
    graph_tools,
    mo,
    nodes_df,
    np,
    pd,
    relations,
    skill_choice,
):
    selected_ids, selected_relations = graph_tools.select_neighborhood(entities, relations, skill_choice.value, direction_choice.value)
    _row = nodes_df.set_index("id").loc[skill_choice.value]
    _neighbors = sorted(selected_ids - {skill_choice.value}, key=lambda node: entities[node]["properties"]["name"])
    _local_positions = {skill_choice.value: (0.0, 0.0)}
    for _index, _node in enumerate(_neighbors):
        _angle = 2 * np.pi * _index / max(len(_neighbors), 1)
        _local_positions[_node] = (float(np.cos(_angle)), float(np.sin(_angle)))
    _fig = draw_relation_graph(entities, selected_relations, _local_positions, nodes_df.to_dict("records"), visible_ids=selected_ids, selected=skill_choice.value, title=f"{_row['name']}: {direction_choice.value} / {len(selected_ids)} skills / {len(selected_relations)} edges")
    _rows = [{"來源": entities[edge["from"]]["properties"]["name"], "目標": entities[edge["to"]]["properties"]["name"], "類型": edge["rel"], "原始理由": edge["properties"]["reason"]} for edge in selected_relations]
    _items = [mo.md(f"""
        ## 單一技能與一跳關聯

        **{_row['name']}**：全圖入度 **{_row['in_degree']}**、出度 **{_row['out_degree']}**。
        目前顯示 **{len(selected_ids)} 個節點、{len(selected_relations)} 條關係**，只取符合所選方向的 incident edges，不加入鄰居之間的其他關係。
        橘色箭頭是自己指向目標，藍色是其他技能指向自己；雙向宣告用分開的弧線表示。
        超過 50 個節點時只顯示部分名稱，節點、箭頭及下方完整理由表不截斷。
        """), _fig]
    if _rows:
        _items.append(mo.ui.table(pd.DataFrame(_rows), page_size=10, selection=None))
    else:
        _items.append(mo.md("這個方向目前沒有宣告關係；這不表示此技能無用，或與其他技能已被證明無關。"))
    mo.vstack(_items)
    return


@app.cell(hide_code=True)
def _(edges_df, mo, nodes_df):
    mo.vstack([
        mo.md("## 完整節點與邊資料\n可搜尋、排序與分頁查看。未出現在關聯中的技能仍保留在節點表。"),
        mo.accordion({
            "全部技能與入／出度": mo.ui.table(nodes_df, page_size=15, selection=None),
            "孤立技能": mo.ui.table(nodes_df.loc[nodes_df["role"] == "isolated"], page_size=15, selection=None),
            "全部有向關聯與理由": mo.ui.table(edges_df, page_size=15, selection=None),
        }),
    ])
    return


if __name__ == "__main__":
    app.run()
