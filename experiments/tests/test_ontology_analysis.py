import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "ontology_analysis.py"
SPEC = importlib.util.spec_from_file_location("ontology_analysis", SCRIPT)
analysis = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(analysis)


def create(name):
    return {"op": "create", "entity": {"id": name, "type": "Skill", "properties": {"name": name, "source_path": f"skills/{name}/SKILL.md"}}}


def relate(source, target, reason="reason", relation="related"):
    return {"op": "relate", "from": source, "rel": relation, "to": target, "properties": {"reason": reason, "classification_status": "not_classified", "verification_status": "unverified"}}


class OntologyAnalysisTests(unittest.TestCase):
    def load(self, records):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "graph.jsonl"
            path.write_text("".join(json.dumps(record) + "\n" for record in records))
            return analysis.read_graph(path)

    def fixture(self):
        return self.load([*[create(name) for name in "abcd"], relate("a", "b"), relate("b", "a"), relate("c", "a")])

    def test_replay_updates_entity_and_replaces_relation_without_losing_reverse(self):
        records = [create("a"), create("b"), relate("a", "b", "old"), relate("b", "a", "reverse"),
                   {"op": "update", "id": "a", "properties": {"source_path": "skills/new-a/SKILL.md"}},
                   {"op": "unrelate", "from": "a", "rel": "related", "to": "b"},
                   relate("a", "b", "new", "composes_with")]
        entities, edges, count = self.load(records)
        self.assertEqual(count, 7)
        self.assertEqual(entities["a"]["properties"]["source_path"], "skills/new-a/SKILL.md")
        self.assertEqual({(edge["from"], edge["to"]): (edge["rel"], edge["properties"]["reason"]) for edge in edges},
                         {("a", "b"): ("composes_with", "new"), ("b", "a"): ("related", "reverse")})

    def test_metrics_distinguish_reciprocal_edges_components_and_direction(self):
        entities, edges, _ = self.fixture()
        result = analysis.analyze_graph(entities, edges)
        summary = result["summary"]
        self.assertEqual((summary["node_count"], summary["edge_count"]), (4, 3))
        self.assertEqual((summary["reciprocal_pairs"], summary["reciprocal_edges"]), (1, 2))
        self.assertAlmostEqual(summary["reciprocity"], 2 / 3)
        self.assertAlmostEqual(summary["density"], 3 / 12)
        self.assertEqual(summary["weak_component_sizes"], [3, 1])
        self.assertEqual(summary["strong_component_sizes"], [2, 1, 1])
        self.assertEqual(summary["roles"], {"both": 2, "incoming_only": 0, "outgoing_only": 1, "isolated": 1})
        rows = {row["id"]: row for row in result["nodes"]}
        self.assertEqual((rows["a"]["in_degree"], rows["a"]["out_degree"]), (2, 1))

    def test_duplicate_ordered_pair_is_rejected_even_with_different_predicate(self):
        with self.assertRaises(ValueError):
            self.load([create("a"), create("b"), relate("a", "b"), relate("a", "b", relation="composes_with")])

    def test_delete_requires_explicit_edge_removal(self):
        with self.assertRaises(ValueError):
            self.load([create("a"), create("b"), relate("a", "b"), {"op": "delete", "id": "b"}])
        entities, edges, _ = self.load([create("a"), create("b"), relate("a", "b"),
                                      {"op": "unrelate", "from": "a", "rel": "related", "to": "b"}, {"op": "delete", "id": "b"}])
        self.assertEqual(set(entities), {"a"})
        self.assertEqual(edges, [])

    def test_unknown_operations_and_invalid_endpoints_are_rejected(self):
        for records in [[{"op": "surprise"}], [create("a"), relate("a", "missing")], [create("a"), relate("a", "a")]]:
            with self.subTest(records=records), self.assertRaises(ValueError):
                self.load(records)

    def test_neighborhood_filter_obeys_arrow_direction(self):
        entities, edges, _ = self.fixture()
        selected, outgoing = analysis.select_neighborhood(entities, edges, "a", "outgoing")
        self.assertEqual(selected, {"a", "b"})
        self.assertEqual([(edge["from"], edge["to"]) for edge in outgoing], [("a", "b")])
        selected, incoming = analysis.select_neighborhood(entities, edges, "a", "incoming")
        self.assertEqual(selected, {"a", "b", "c"})
        self.assertEqual({(edge["from"], edge["to"]) for edge in incoming}, {("b", "a"), ("c", "a")})
        selected, isolated = analysis.select_neighborhood(entities, edges, "d", "both")
        self.assertEqual((selected, isolated), ({"d"}, []))

    def test_empty_graph_has_zero_counts(self):
        entities, edges, count = self.load([])
        summary = analysis.analyze_graph(entities, edges)["summary"]
        self.assertEqual((count, summary["node_count"], summary["edge_count"], summary["density"], summary["reciprocity"]), (0, 0, 0, 0, 0))

    def test_multiple_sources_keep_same_named_skills_distinct_without_status(self):
        first = create("github:wei840222/omni-skills:bluetooth")
        second = create("github:another/skills:bluetooth")
        for record in [first, second]:
            record["entity"]["properties"] = {"name": "bluetooth", "source_path": "skills/bluetooth/SKILL.md"}
        edge = {"op": "relate", "from": first["entity"]["id"], "rel": "related", "to": second["entity"]["id"], "properties": {"reason": "Complementary Bluetooth guidance."}}
        entities, edges, _ = self.load([first, second, edge])
        result = analysis.analyze_graph(entities, edges)
        self.assertEqual((result["summary"]["node_count"], result["summary"]["edge_count"]), (2, 1))
        labels = analysis.skill_labels(entities)
        self.assertEqual(len(set(labels.values())), 2)
        self.assertIn(first["entity"]["id"], labels[first["entity"]["id"]])
        self.assertIn(second["entity"]["id"], labels[second["entity"]["id"]])
        self.assertEqual({row["display_name"] for row in result["nodes"]}, set(labels.values()))
        self.assertEqual(result["edges"][0]["source"], labels[first["entity"]["id"]])
        self.assertEqual(result["edges"][0]["target"], labels[second["entity"]["id"]])
        self.assertEqual(edges[0]["properties"], {"reason": "Complementary Bluetooth guidance."})

    def test_single_source_keeps_short_skill_labels(self):
        entities, _, _ = self.fixture()
        self.assertEqual(analysis.skill_labels(entities), {name: name for name in "abcd"})

    def test_replay_preserves_existing_ontology_overwrite_and_noop_semantics(self):
        replacement = create("a")
        replacement["entity"]["properties"]["name"] = "renamed-a"
        edge = relate("a", "b")
        edge["timestamp"] = "2026-10-26T00:00:00Z"
        entities, edges, count = self.load([
            create("a"), replacement, create("b"),
            {"op": "update", "id": "missing", "properties": {"name": "ignored"}},
            {"op": "delete", "id": "missing"},
            {"op": "update", "id": "a", "properties": {"source_path": "skills/renamed-a/SKILL.md"}, "timestamp": "2026-10-26T00:00:00Z"},
            edge,
        ])
        self.assertEqual(count, 7)
        self.assertEqual(entities["a"]["properties"]["name"], "renamed-a")
        self.assertEqual(entities["a"]["updated"], "2026-10-26T00:00:00Z")
        self.assertEqual(set(edges[0]), {"from", "rel", "to", "properties"})


if __name__ == "__main__":
    unittest.main()
