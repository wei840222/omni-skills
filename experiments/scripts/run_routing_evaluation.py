#!/usr/bin/env python3
"""Measure fair BM25, dense, RRF, and configured remote-reranker routing."""

import argparse
from collections import defaultdict
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import sqlite3
import time

import numpy as np
import pandas as pd

from generate_embeddings import ResponseCache, bounded_results, load_settings, post_json, rerank_order
from prepare_experiment_datasets import COLLECTIONS, content_hash

PIPELINES = {"bm25": "BM25", "vector": "Vector", "hybrid": "Hybrid RRF", "rerank": "Hybrid + Rerank"}


def compute_metrics(results):
    total = len(results)
    if not total:
        raise ValueError("Cannot evaluate an empty benchmark")
    output = {f"hit@{cutoff}": round(100 * sum(item["ground_truth"] in item["retrieved"][:cutoff] for item in results) / total, 4) for cutoff in (1, 3, 5)}
    output["mrr@10"] = round(sum(1 / (item["retrieved"][:10].index(item["ground_truth"]) + 1) if item["ground_truth"] in item["retrieved"][:10] else 0 for item in results) / total, 6)
    return output


def rrf_fusion(ranked_lists, k=60, top_k=10):
    scores = defaultdict(float)
    for ranking in ranked_lists:
        for rank, skill in enumerate(dict.fromkeys(ranking), 1):
            scores[skill] += 1 / (k + rank)
    return sorted(scores, key=lambda skill: (-scores[skill], skill))[:top_k]


def rank_pipelines(bm25, vector):
    return {"bm25": bm25[:10], "vector": vector[:10], "hybrid": rrf_fusion([bm25, vector])}


def normalize(matrix):
    matrix = np.asarray(matrix, dtype=np.float32)
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    if not np.isfinite(matrix).all() or np.any(norms == 0):
        raise ValueError("Embedding matrix contains zero or nonfinite vectors")
    return matrix / norms


def build_fts(documents):
    connection = sqlite3.connect(":memory:")
    connection.execute("CREATE VIRTUAL TABLE fts USING fts5(text, skill UNINDEXED, tokenize='unicode61')")
    connection.executemany("INSERT INTO fts(text, skill) VALUES (?, ?)", [(item["text"], item["skill"]) for item in documents])
    return connection


def bm25_search_fts(connection, query, top_k=25):
    tokens = list(dict.fromkeys(re.findall(r"[\w-]+", query.lower())))
    if not tokens:
        return []
    expression = " OR ".join('"' + token.replace('"', '""') + '"' for token in tokens)
    cursor = connection.execute("SELECT skill FROM fts WHERE fts MATCH ? ORDER BY bm25(fts), rowid", (expression,))
    ranking = []
    seen = set()
    for (skill,) in cursor:
        if skill not in seen:
            ranking.append(skill)
            seen.add(skill)
        if len(ranking) == top_k:
            break
    cursor.close()
    return ranking


def request_rerank(settings, query, candidates, texts):
    response, duration = post_json(settings.rerank_url, {"model": settings.rerank_model, "query": query, "documents": texts}, settings.rerank_key)
    return {"ranking": rerank_order(response, candidates), "service_ms": duration}


def summarize_timing(values):
    return {"mean": round(float(np.mean(values)), 4), "p50": round(float(np.percentile(values, 50)), 4), "p95": round(float(np.percentile(values, 95)), 4)}


def evaluate(root, settings, workers=12, query_limit=None):
    if workers < 1:
        raise ValueError("Workers must be positive")
    folder = root / "experiments" / "datasets"
    documents = json.loads((folder / "documents.json").read_text())
    all_queries = json.loads((folder / "benchmark_queries.json").read_text())
    manifest = json.loads((folder / "manifest.json").read_text())
    embedding_info = json.loads((folder / "embedding_manifest.json").read_text())
    if content_hash(documents) != manifest["corpus_hash"] or content_hash(all_queries) != manifest["queries_hash"]:
        raise ValueError("Dataset no longer matches manifest")
    if any(embedding_info[key] != manifest[key] for key in ("corpus_hash", "queries_hash")) or embedding_info["config_fingerprint"] != settings.fingerprint:
        raise ValueError("Embedding artifact does not match dataset/model; regenerate embeddings")
    if query_limit is not None and query_limit < 1:
        raise ValueError("Query limit must be positive")
    queries = all_queries[:query_limit] if query_limit else all_queries
    with np.load(folder / "embeddings.npz", allow_pickle=False) as vectors:
        if vectors["query_ids"].tolist() != [query["query_id"] for query in all_queries]:
            raise ValueError("Query embedding IDs/order do not match benchmark")
        query_vectors = normalize(vectors["query_vectors"][:len(queries)])
        query_api_times = vectors["query_embedding_api_batch_ms_per_item"][:len(queries)].tolist()
        matrices = {collection: normalize(vectors[collection + "__vectors"]) for collection in COLLECTIONS}
        for collection in COLLECTIONS:
            if vectors[collection + "__ids"].tolist() != [item["id"] for item in documents[collection]]:
                raise ValueError(f"Document embedding IDs/order mismatch: {collection}")
    cases = [{"query_id": query["query_id"], "skill": query["ground_truth_skill"], "natural_prompt": query["natural_prompt"], "rankings": {}, "latency_ms": {}, "service_latency_ms": {}, "rerank_cache_hit": {}} for query in queries]
    cache = ResponseCache(folder / ".cache" / "responses.sqlite")
    current_run_service_calls = 0
    run_started = time.perf_counter()
    try:
        for collection in COLLECTIONS:
            collection_documents = documents[collection]
            slugs = np.asarray([item["skill"] for item in collection_documents])
            unique_skills = np.unique(slugs)
            order = np.argsort(slugs, kind="stable")
            ordered_skills = slugs[order]
            starts = np.r_[0, np.flatnonzero(ordered_skills[1:] != ordered_skills[:-1]) + 1]
            started = time.perf_counter()
            similarities = query_vectors @ matrices[collection].T
            skill_scores = np.maximum.reduceat(similarities[:, order], starts, axis=1)
            ranked_indices = np.argsort(-skill_scores, axis=1, kind="stable")[:, :25]
            dense_rankings = [[str(unique_skills[index]) for index in row] for row in ranked_indices]
            dense_ms_per_query = (time.perf_counter() - started) * 1000 / len(queries)
            skill_chunks = {str(skill): np.flatnonzero(slugs == skill) for skill in unique_skills}
            fts = build_fts(collection_documents)
            tasks = []
            for index, query in enumerate(queries):
                started = time.perf_counter()
                lexical = bm25_search_fts(fts, query["natural_prompt"])
                lexical_ms = (time.perf_counter() - started) * 1000
                started = time.perf_counter()
                rankings = rank_pipelines(lexical, dense_rankings[index])
                fusion_ms = (time.perf_counter() - started) * 1000
                hybrid_ms = lexical_ms + dense_ms_per_query + fusion_ms
                cases[index]["rankings"][collection] = rankings
                cases[index]["latency_ms"][collection] = {"bm25": lexical_ms, "vector": dense_ms_per_query, "hybrid": hybrid_ms}
                cases[index]["service_latency_ms"][collection] = {"query_embedding_batch_per_item": query_api_times[index]}
                candidates = rankings["hybrid"]
                texts = []
                for candidate in candidates:
                    indices = skill_chunks[candidate]
                    best_chunk = int(indices[np.argmax(similarities[index, indices])])
                    texts.append(collection_documents[best_chunk]["text"])
                key = content_hash({"protocol": 2, "endpoint": settings.rerank_url, "model": settings.rerank_model, "query": query["natural_prompt"], "candidates": candidates, "texts": texts})
                cached = cache.get(key)
                if cached is not None:
                    if set(cached["ranking"]) != set(candidates) or len(cached["ranking"]) != len(candidates):
                        raise ValueError("Rerank cache candidate mismatch")
                    rankings["rerank"] = cached["ranking"]
                    cases[index]["service_latency_ms"][collection]["rerank"] = cached["service_ms"]
                    cases[index]["latency_ms"][collection]["rerank"] = hybrid_ms + cached["service_ms"]
                    cases[index]["rerank_cache_hit"][collection] = True
                else:
                    tasks.append((index, key, candidates, texts))
            fts.close()
            print(f"{collection}: {len(collection_documents)} chunks, {len(queries)} queries; {len(tasks)} rerank requests missing", flush=True)
            request_task = lambda job: request_rerank(settings, queries[job[0]]["natural_prompt"], job[2], job[3])
            for completed, ((index, key, _, _), response) in enumerate(bounded_results(request_task, tasks, workers), 1):
                cache.put(key, response)
                current_run_service_calls += 1
                cases[index]["rankings"][collection]["rerank"] = response["ranking"]
                cases[index]["service_latency_ms"][collection]["rerank"] = response["service_ms"]
                cases[index]["latency_ms"][collection]["rerank"] = cases[index]["latency_ms"][collection]["hybrid"] + response["service_ms"]
                cases[index]["rerank_cache_hit"][collection] = False
                if completed % 50 == 0 or completed == len(tasks):
                    print(f"{collection}: reranked {completed}/{len(tasks)}", flush=True)
            del similarities
    finally:
        cache.close()
    metrics = {}
    for collection in COLLECTIONS:
        metrics[collection] = {}
        for pipeline, label in PIPELINES.items():
            evaluation = [{"ground_truth": case["skill"], "retrieved": case["rankings"][collection][pipeline]} for case in cases]
            statistics = compute_metrics(evaluation)
            timings = [case["latency_ms"][collection][pipeline] for case in cases]
            statistics["retrieval_latency_ms_mean"] = summarize_timing(timings)["mean"]
            statistics["retrieval_latency_ms_p50"] = summarize_timing(timings)["p50"]
            statistics["retrieval_latency_ms_p95"] = summarize_timing(timings)["p95"]
            statistics["service_latency_ms_mean"] = round(float(np.mean([case["service_latency_ms"][collection]["rerank"] for case in cases])), 4) if pipeline == "rerank" else 0.0
            metrics[collection][label] = statistics
    for case in cases:
        case["nd_vec_top5"] = case["rankings"]["name-description"]["vector"][:5]
        case["nd_bm25_top5"] = case["rankings"]["name-description"]["bm25"][:5]
        case["all_vec_top5"] = case["rankings"]["full"]["vector"][:5]
        case["ref_vec_top5"] = case["rankings"]["full-references"]["vector"][:5]
        for key, collection in [("nd_hit1", "name-description"), ("all_hit1", "full"), ("ref_hit1", "full-references")]:
            ranking = case["rankings"][collection]["vector"]
            case[key] = bool(ranking and ranking[0] == case["skill"])
    metadata = {key: value for key, value in manifest.items() if key != "source_files"}
    metadata.update({
        "created_at": datetime.now(timezone.utc).isoformat(),
        "query_count": len(queries),
        "total_query_count": len(all_queries),
        "partial_run": len(queries) != len(all_queries),
        "embedding_model": settings.embed_model,
        "embedding_api_timing": {
            "model": settings.embed_model,
            "dimension": settings.dimension,
            "observed_models": embedding_info.get("observed_models", []),
            "query_api_batch_ms_per_item": summarize_timing(query_api_times),
            "generation_run_request_count": len(embedding_info["api_timing"]["current_run_requests"]),
            "method": embedding_info["api_timing"]["query_per_item_timing"],
        },
        "rerank_model": settings.rerank_model,
        "dimension": settings.dimension,
        "rerank_candidate_count": 10,
        "rrf_k": 60,
        "current_run_rerank_service_calls": current_run_service_calls,
        "rerank_cached_observation_count": sum(
            case["rerank_cache_hit"][collection]
            for case in cases for collection in COLLECTIONS
        ),
        "evaluation_wall_seconds": round(time.perf_counter() - run_started, 3),
        "code_sha256": {
            str(Path("experiments/scripts") / source.name): hashlib.sha256(source.read_bytes()).hexdigest()
            for source in sorted(Path(__file__).resolve().parent.glob("*.py"))
        },
        "timing_method": (
            "Dense retrieval uses actual batched matrix/pooling/sort wall time divided by queries. "
            "BM25/fusion measured per query. Rerank service wall time includes network and bounded retries, "
            "reused original observations when cached; stage sums exclude candidate-context assembly and query embedding. "
            "API query embedding batching time is separately recorded and is not single-query end-to-end latency."
        ),
        "rerank_context": (
            "For each of the top ten RRF skills, rerank the chunk with maximum query-vector similarity; "
            "same natural query, no expected answer or ground truth used."
        ),
    })
    output = {"metadata": metadata, "metrics_by_pipeline": metrics, "detailed_cases": cases}
    filename = "routing_benchmark_smoke_results.json" if query_limit else "routing_benchmark_results.json"
    temporary = folder / (filename + ".tmp")
    temporary.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n")
    temporary.replace(folder / filename)
    for collection in COLLECTIONS:
        print(f"\n{collection}\n{pd.DataFrame(metrics[collection]).T.to_string()}", flush=True)
    print(f"Saved {filename}; partial_run={metadata['partial_run']}", flush=True)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--config", type=Path, default=Path("~/.config/qmd/index.yml"))
    parser.add_argument("--embed-model")
    parser.add_argument("--dimension", type=int)
    parser.add_argument("--workers", type=int, default=12)
    parser.add_argument("--limit-queries", type=int, help="Smoke test; writes a separate results file")
    args = parser.parse_args()
    settings = load_settings(args.config, args.embed_model, args.dimension)
    evaluate(args.root, settings, args.workers, args.limit_queries)


if __name__ == "__main__":
    main()
