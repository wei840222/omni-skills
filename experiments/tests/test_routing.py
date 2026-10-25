"""Regression tests for fair queries, cache identity, and pipeline ranking."""

import json
from pathlib import Path
import sys
import tempfile
import unittest
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from generate_bm25_prompts import compile_queries
from generate_embeddings import ModelSettings, embedding_batch, embedding_key, generate, rerank_order
from prepare_experiment_datasets import chunk_text, prepare
from run_routing_evaluation import compute_metrics, evaluate, rank_pipelines


class RoutingRegressionTests(unittest.TestCase):
    def test_queries_ignore_answer_conditioned_keywords(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            skill = root / "skills" / "garden"
            skill.mkdir(parents=True)
            (skill / "SKILL.md").write_text("---\nname: garden\ndescription: plants\n---\n")
            source = json.dumps([{"id": 7, "prompt": "My leaves are yellow", "bm25_prompt": "garden secret answer", "expected": "diagnose"}])
            (skill / "test-prompts.json").write_text(source)
            queries = compile_queries(root)
            self.assertEqual(queries[0]["natural_prompt"], "My leaves are yellow")
            self.assertNotIn("bm25_prompt", queries[0])
            self.assertEqual((skill / "test-prompts.json").read_text(), source)

    def test_hybrid_really_combines_both_rankings(self):
        rankings = rank_pipelines(["lexical", "shared"], ["semantic", "shared"])
        self.assertEqual(rankings["bm25"][0], "lexical")
        self.assertEqual(rankings["vector"][0], "semantic")
        self.assertEqual(rankings["hybrid"][0], "shared")

    def test_embedding_cache_keys_include_model_role_and_content(self):
        base = embedding_key("hello", "model-a", 1024, "query", "https://example.invalid")
        for text, model, dimension, role in [("new", "model-a", 1024, "query"), ("hello", "model-b", 1024, "query"), ("hello", "model-a", 512, "query"), ("hello", "model-a", 1024, "document")]:
            self.assertNotEqual(base, embedding_key(text, model, dimension, role, "https://example.invalid"))

    def test_rerank_uses_response_indices_not_candidate_order(self):
        response = {"results": [{"index": 2, "relevance_score": 0.9}, {"index": 0, "relevance_score": 0.8}, {"index": 1, "relevance_score": 0.1}]}
        self.assertEqual(rerank_order(response, ["a", "b", "c"]), ["c", "a", "b"])
        with self.assertRaises(ValueError):
            rerank_order({"results": [{"index": 99}]}, ["a"])
        for score in [None, float("nan"), float("inf")]:
            with self.assertRaises(ValueError):
                rerank_order({"results": [{"index": 0, "relevance_score": score}]}, ["a"])

    def test_metrics_respect_rank_ten_cutoff(self):
        actual = compute_metrics([{"ground_truth": "a", "retrieved": ["a"]}, {"ground_truth": "b", "retrieved": ["a", "b"]}, {"ground_truth": "missing", "retrieved": ["a"]}])
        self.assertAlmostEqual(actual["hit@1"], 100 / 3, places=2)
        self.assertAlmostEqual(actual["hit@3"], 200 / 3, places=2)
        self.assertEqual(actual["mrr@10"], 0.5)

    def test_embedding_response_rejects_a_different_model(self):
        settings = ModelSettings("https://example.invalid/embeddings", "requested", 2, "", "https://example.invalid/rerank", "rerank", "")
        with patch("generate_embeddings.post_json", return_value=({"model": "wrong", "data": [{"index": 0, "embedding": [1, 0]}]}, 1)):
            with self.assertRaises(ValueError):
                embedding_batch(settings, ["hello"], "query")

    def test_unicode_chunks_stay_below_service_token_limit(self):
        chunks = chunk_text("測試" * 9000)
        self.assertTrue(all(len(chunk.encode("utf-8")) <= 7500 for chunk in chunks))
        with self.assertRaises(ValueError):
            chunk_text("abc", size=100, overlap=90)

    def test_small_run_saves_aligned_artifacts_and_resumes_reranking(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            for slug in ["garden", "database"]:
                skill = root / "skills" / slug
                skill.mkdir(parents=True)
                (skill / "SKILL.md").write_text(f"---\nname: {slug}\ndescription: Work on {slug}\n---\nHelp with {slug}.")
                (skill / "test-prompts.json").write_text(json.dumps([{"id": 1, "prompt": f"Help with {slug}", "bm25_prompt": "wrong answer"}]))
            with patch("prepare_experiment_datasets.subprocess.run", return_value=SimpleNamespace(stdout="source-sha\n")):
                manifest = prepare(root)
            self.assertEqual(manifest["skill_count"], 2)
            settings = ModelSettings("https://example.invalid/embeddings", "small", 2, "", "https://example.invalid/rerank", "rerank", "")

            def embed_response(url, payload, key):
                vectors = [{"index": index, "embedding": [1, 0] if "garden" in text else [0, 1]} for index, text in enumerate(payload["input"])]
                return {"model": "small", "data": vectors}, 10

            with patch("generate_embeddings.post_json", side_effect=embed_response):
                generate(root, settings, workers=1, batch_size=2)

            def rerank_response(url, payload, key):
                count = len(payload["documents"])
                return {"results": [{"index": index, "relevance_score": float(index)} for index in reversed(range(count))]}, 20

            with patch("run_routing_evaluation.post_json", side_effect=rerank_response):
                first = evaluate(root, settings, workers=1)
            with patch("run_routing_evaluation.post_json", side_effect=AssertionError("cached rerank should not call network")):
                resumed = evaluate(root, settings, workers=1)
            self.assertEqual(len(first["detailed_cases"]), 2)
            self.assertEqual(resumed["metadata"]["current_run_rerank_service_calls"], 0)
            self.assertEqual(resumed["metadata"]["rerank_cached_observation_count"], 6)
            self.assertEqual(set(first["metrics_by_pipeline"]["full"]), {"BM25", "Vector", "Hybrid RRF", "Hybrid + Rerank"})
            with patch("generate_embeddings.post_json", side_effect=AssertionError("model cache must avoid requests")):
                generate(root, settings, workers=1, batch_size=2)


if __name__ == "__main__":
    unittest.main()
