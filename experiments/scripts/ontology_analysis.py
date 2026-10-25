"""Read and analyze the authored skill relation log without changing its source.

Relations are directed declarations, not verified relevance or quality labels.
The force layout is a display arrangement, not a semantic distance measure.
"""

from collections import Counter
from copy import deepcopy
import json
from pathlib import Path

import numpy as np


RELATION_TYPES = frozenset({
    "related", "depends_on", "composes_with", "similar_to", "conflicts_with",
    "specializes",
})


def _text(value, label):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty string")
    return value


def _validate_graph(entities, relations):
    """Validate the final state; keep all original entity/relation fields."""
    for entity_id, entity in entities.items():
        _text(entity_id, "entity id")
        if not isinstance(entity, dict) or entity.get("id") != entity_id:
            raise ValueError(f"entity {entity_id!r} has an inconsistent id")
        if entity.get("type") != "Skill":
            raise ValueError(f"entity {entity_id!r} must have type Skill")
        properties = entity.get("properties")
        if not isinstance(properties, dict):
            raise ValueError(f"entity {entity_id!r} must have properties")
        _text(properties.get("name"), f"entity {entity_id!r} name")
        _text(properties.get("source_path"), f"entity {entity_id!r} source_path")
    seen = set()
    for edge in relations:
        if not isinstance(edge, dict):
            raise ValueError("relation must be an object")
        source = _text(edge.get("from"), "relation from")
        target = _text(edge.get("to"), "relation to")
        if source not in entities or target not in entities:
            raise ValueError(f"relation {source!r} -> {target!r} has an unresolved endpoint")
        if source == target:
            raise ValueError(f"self relation on {source!r} is not allowed")
        if not isinstance(edge.get("rel"), str) or edge["rel"] not in RELATION_TYPES:
            raise ValueError(f"unknown relation type {edge.get('rel')!r}")
        pair = (source, target)
        if pair in seen:
            raise ValueError(f"duplicate ordered relation pair {source!r} -> {target!r}")
        seen.add(pair)
        properties = edge.get("properties")
        if not isinstance(properties, dict):
            raise ValueError(f"relation {source!r} -> {target!r} must have properties")
        _text(properties.get("reason"), f"relation {source!r} -> {target!r} reason")


def read_graph(path: Path):
    """Replay a JSONL operation log and return entities, relations, op count.

    Create replaces an identity; missing update/delete targets are ignored.
    Relate appends a declaration; unrelate removes its exact directed triple. The
    final graph is validated after replay, so a removed historical declaration
    does not affect the current analysis.
    """
    path = Path(path)
    entities, relations = {}, []
    operation_count = 0
    with path.open(encoding="utf-8") as stream:
        for line_number, line in enumerate(stream, 1):
            if not line.strip():
                continue
            try:
                record = json.loads(line)
                if not isinstance(record, dict):
                    raise ValueError("operation must be an object")
                operation_count += 1
                operation = record.get("op")
                if operation == "create":
                    entity = record.get("entity")
                    if not isinstance(entity, dict):
                        raise ValueError("create requires an entity object")
                    entity_id = _text(entity.get("id"), "create entity id")
                    entities[entity_id] = deepcopy(entity)
                elif operation == "update":
                    entity_id = _text(record.get("id"), "update id")
                    if entity_id not in entities:
                        continue
                    properties = record.get("properties", {})
                    if not isinstance(properties, dict):
                        raise ValueError("update requires a properties object")
                    old_properties = entities[entity_id].get("properties", {})
                    if not isinstance(old_properties, dict):
                        raise ValueError(f"entity {entity_id!r} properties must be an object")
                    entities[entity_id]["properties"] = {**old_properties, **deepcopy(properties)}
                    entities[entity_id]["updated"] = record.get("timestamp")
                elif operation == "delete":
                    entity_id = _text(record.get("id"), "delete id")
                    entities.pop(entity_id, None)
                elif operation in {"relate", "unrelate"}:
                    source = _text(record.get("from"), "relation from")
                    relation_type = _text(record.get("rel"), "relation type")
                    target = _text(record.get("to"), "relation to")
                    if operation == "relate":
                        # Keep append semantics: duplicate pairs must be visible
                        # to final validation rather than silently overwritten.
                        relations.append({"from": source, "rel": relation_type, "to": target,
                                          "properties": deepcopy(record.get("properties", {}))})
                    else:
                        triple = (source, relation_type, target)
                        relations = [edge for edge in relations
                                     if (edge["from"], edge["rel"], edge["to"]) != triple]
                else:
                    raise ValueError(f"unknown operation {operation!r}")
            except (ValueError, TypeError, KeyError) as error:
                raise ValueError(f"{path}:{line_number}: {error}") from error
    try:
        _validate_graph(entities, relations)
    except ValueError as error:
        raise ValueError(f"{path}: final graph: {error}") from error
    return entities, relations, operation_count


def _components(adjacency):
    """Connected components of an undirected adjacency mapping."""
    remaining = set(adjacency)
    groups = []
    for root in sorted(adjacency):
        if root not in remaining:
            continue
        remaining.remove(root)
        group, stack = [], [root]
        while stack:
            node = stack.pop()
            group.append(node)
            for neighbor in adjacency[node]:
                if neighbor in remaining:
                    remaining.remove(neighbor)
                    stack.append(neighbor)
        groups.append(sorted(group))
    return sorted(groups, key=lambda group: (-len(group), group))


def _strong_components(outgoing, incoming):
    """Iterative Kosaraju traversal, including isolated nodes."""
    visited, finished = set(), []
    for root in sorted(outgoing):
        if root in visited:
            continue
        visited.add(root)
        stack = [(root, iter(sorted(outgoing[root])))]
        while stack:
            node, neighbors = stack[-1]
            neighbor = next(neighbors, None)
            if neighbor is None:
                finished.append(node)
                stack.pop()
            elif neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, iter(sorted(outgoing[neighbor]))))
    visited.clear()
    groups = []
    for root in reversed(finished):
        if root in visited:
            continue
        visited.add(root)
        group, stack = [], [root]
        while stack:
            node = stack.pop()
            group.append(node)
            for neighbor in sorted(incoming[node]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        groups.append(sorted(group))
    return sorted(groups, key=lambda group: (-len(group), group))


def analyze_graph(entities, relations):
    """Return directed graph metrics and deterministic node/edge table rows."""
    _validate_graph(entities, relations)
    outgoing = {node: set() for node in entities}
    incoming = {node: set() for node in entities}
    for edge in relations:
        outgoing[edge["from"]].add(edge["to"])
        incoming[edge["to"]].add(edge["from"])
    weak = _components({node: outgoing[node] | incoming[node] for node in entities})
    strong = _strong_components(outgoing, incoming)
    weak_index = {node: index for index, group in enumerate(weak) for node in group}
    strong_index = {node: index for index, group in enumerate(strong) for node in group}
    roles = Counter({"both": 0, "incoming_only": 0, "outgoing_only": 0, "isolated": 0})
    nodes = []
    for node in sorted(entities, key=lambda key: (entities[key]["properties"]["name"].casefold(),
                                                  entities[key]["properties"]["name"], key)):
        in_degree, out_degree = len(incoming[node]), len(outgoing[node])
        role = ("both" if in_degree and out_degree else "incoming_only" if in_degree
                else "outgoing_only" if out_degree else "isolated")
        roles[role] += 1
        nodes.append({
            "id": node, "name": entities[node]["properties"]["name"],
            "source_path": entities[node]["properties"]["source_path"],
            "in_degree": in_degree, "out_degree": out_degree,
            "total_degree": in_degree + out_degree, "role": role,
            "weak_component": weak_index[node], "strong_component": strong_index[node],
        })
    pairs = {(edge["from"], edge["to"]) for edge in relations}
    reciprocal_edges = sum((target, source) in pairs for source, target in pairs)
    edges = [{
        "source": entities[edge["from"]]["properties"]["name"],
        "target": entities[edge["to"]]["properties"]["name"],
        "source_id": edge["from"], "target_id": edge["to"],
        "relation_type": edge["rel"], "reason": edge["properties"]["reason"],
        "reciprocal": (edge["to"], edge["from"]) in pairs,
    } for edge in relations]
    edges.sort(key=lambda edge: (edge["source"].casefold(), edge["source"], edge["source_id"],
                                 edge["target"].casefold(), edge["target"], edge["target_id"],
                                 edge["relation_type"]))
    n, m = len(entities), len(relations)
    summary = {
        "node_count": n, "edge_count": m,
        "density": m / (n * (n - 1)) if n > 1 else 0,
        "average_degree": m / n if n else 0,
        "reciprocal_pairs": reciprocal_edges // 2,
        "reciprocal_edges": reciprocal_edges,
        "reciprocity": reciprocal_edges / m if m else 0,
        "isolated_count": roles["isolated"],
        "weak_component_count": len(weak), "largest_weak_component": len(weak[0]) if weak else 0,
        "strong_component_count": len(strong), "largest_strong_component": len(strong[0]) if strong else 0,
        "roles": dict(roles), "weak_component_sizes": [len(group) for group in weak],
        "strong_component_sizes": [len(group) for group in strong],
    }
    return {"summary": summary, "nodes": nodes, "edges": edges}


def select_neighborhood(entities, relations, skill_id, direction):
    """Select one-hop incident declarations, retaining an isolated selection."""
    if skill_id not in entities:
        raise ValueError(f"unknown skill id {skill_id!r}")
    if direction not in {"incoming", "outgoing", "both"}:
        raise ValueError(f"unknown neighborhood direction {direction!r}")
    selected = {skill_id}
    edges = []
    for edge in relations:
        if ((direction in {"outgoing", "both"} and edge["from"] == skill_id)
                or (direction in {"incoming", "both"} and edge["to"] == skill_id)):
            edges.append(edge)
            selected.update((edge["from"], edge["to"]))
    return selected, edges


def graph_layout(entities, relations):
    """Deterministic seeded force coordinates; isolates use a separate compact grid.

    Computes 120 NumPy-vectorized iterations once, rather than during interactive
    filtering. Reciprocal declarations share one undirected layout spring.
    Neither the coordinates nor their distances imply semantic similarity.
    """
    _validate_graph(entities, relations)
    if not entities:
        return {}
    linked = {edge[endpoint] for edge in relations for endpoint in ("from", "to")}
    active = sorted(linked)
    isolated = sorted(set(entities) - linked)
    coordinates = {}
    if active:
        count = len(active)
        index = {node: position for position, node in enumerate(active)}
        pairs = sorted({tuple(sorted((index[edge["from"]], index[edge["to"]]))) for edge in relations})
        source = np.array([pair[0] for pair in pairs], dtype=int)
        target = np.array([pair[1] for pair in pairs], dtype=int)
        positions = np.random.default_rng(20261026).uniform(-1, 1, (count, 2))
        ideal_distance = np.sqrt(4 / count)
        for iteration in range(120):
            delta = positions[:, None, :] - positions[None, :, :]
            squared_distance = np.maximum(np.sum(delta * delta, axis=2), 1e-8)
            displacement = np.sum(delta * (ideal_distance**2 / squared_distance)[:, :, None], axis=1)
            spring_delta = positions[source] - positions[target]
            spring_distance = np.maximum(np.linalg.norm(spring_delta, axis=1), 1e-8)
            attraction = spring_delta * (spring_distance / ideal_distance)[:, None]
            np.add.at(displacement, source, -attraction)
            np.add.at(displacement, target, attraction)
            displacement -= positions * 0.02
            length = np.maximum(np.linalg.norm(displacement, axis=1), 1e-8)
            temperature = 0.14 * (1 - iteration / 120)
            positions += displacement * (np.minimum(length, temperature) / length)[:, None]
        positions -= positions.mean(axis=0)
        positions /= max(float(np.abs(positions).max()), 1e-8)
        coordinates.update({node: (float(point[0]), float(point[1]))
                            for node, point in zip(active, positions)})
    if isolated:
        columns = int(np.ceil(np.sqrt(len(isolated))))
        rows = int(np.ceil(len(isolated) / columns))
        spacing = 0.12 if active else 1 / max(columns, rows, 1)
        start_x = max(point[0] for point in coordinates.values()) + 0.3 if active else -(columns - 1) * spacing / 2
        for index, node in enumerate(isolated):
            coordinates[node] = (float(start_x + (index % columns) * spacing),
                                 float(((rows - 1) / 2 - index // columns) * spacing))
    return {node: coordinates[node] for node in sorted(coordinates)}
