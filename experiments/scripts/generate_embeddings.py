#!/usr/bin/env python3
"""Generate resumable document/query embeddings using external QMD model settings."""

import argparse
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import dataclass, field
from datetime import datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path
import sqlite3
import time
import urllib.error
import urllib.request

import numpy as np
import yaml

from prepare_experiment_datasets import COLLECTIONS, content_hash


@dataclass(frozen=True)
class ModelSettings:
    embed_url: str
    embed_model: str
    dimension: int
    embed_key: str = field(repr=False)
    rerank_url: str
    rerank_model: str
    rerank_key: str = field(repr=False)

    @property
    def fingerprint(self):
        return content_hash({"embed_url": self.embed_url, "embed_model": self.embed_model, "dimension": self.dimension})


def resolve_key(value):
    if value is None:
        return ""
    if not isinstance(value, str):
        raise ValueError("API key setting must be a string")
    if value.startswith("env:"):
        name = value[4:]
        if name not in os.environ:
            raise ValueError("API key environment variable is unset")
        return os.environ[name]
    expanded = os.path.expandvars(value)
    if "$" in expanded:
        raise ValueError("API key environment variable is unset")
    return expanded


def load_settings(config: Path, embed_model=None, dimension=None) -> ModelSettings:
    settings = yaml.safe_load(config.expanduser().read_text(encoding="utf-8"))
    models = settings.get("models", {})
    embed_url = str(models.get("embed_api_url", "")).rstrip("/")
    if not embed_url.endswith("/embeddings"):
        embed_url += "/embeddings"
    result = ModelSettings(
        embed_url=embed_url,
        embed_model=embed_model or models.get("embed_api_model", ""),
        dimension=int(dimension or models.get("embed_dimension", 1024)),
        embed_key=resolve_key(models.get("embed_api_key", "")),
        rerank_url=str(models.get("rerank_api_url", "")),
        rerank_model=str(models.get("rerank_api_model", "")),
        rerank_key=resolve_key(models.get("rerank_api_key", "")),
    )
    if not result.embed_url.startswith(("https://", "http://")) or not result.embed_model or result.dimension < 1:
        raise ValueError("QMD embedding URL/model/dimension is missing or invalid")
    if not result.rerank_url.startswith(("https://", "http://")) or not result.rerank_model:
        raise ValueError("QMD rerank URL/model is missing or invalid")
    return result


def embedding_key(text, model, dimension, role, endpoint):
    return content_hash({"text": text, "model": model, "dimension": dimension, "role": role, "endpoint": endpoint, "protocol": 2})


def post_json(url, payload, key, timeout=120):
    headers = {"Content-Type": "application/json"}
    if key:
        headers["Authorization"] = f"Bearer {key}"
    request = urllib.request.Request(url, data=json.dumps(payload).encode(), headers=headers)
    started = time.perf_counter()
    for attempt in range(2):
        try:
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return json.loads(response.read()), (time.perf_counter() - started) * 1000
        except urllib.error.HTTPError as error:
            if error.code not in (408, 429, 500, 502, 503, 504) or attempt == 1:
                raise RuntimeError(f"Remote model request failed (HTTP {error.code}); response body omitted") from None
        except (urllib.error.URLError, TimeoutError):
            if attempt == 1:
                raise RuntimeError("Remote model request failed after bounded retries; connection details omitted") from None
        time.sleep(2 ** attempt)
    raise RuntimeError("Remote model request failed")


def bounded_results(function, jobs, workers):
    """Submit only the active window; stop scheduling after the first error."""
    iterator = iter(jobs)
    pool = ThreadPoolExecutor(max_workers=workers)
    pending = {}
    try:
        for _ in range(workers):
            job = next(iterator, None)
            if job is not None:
                pending[pool.submit(function, job)] = job
        while pending:
            completed, _ = wait(pending, return_when=FIRST_COMPLETED)
            for future in completed:
                job = pending.pop(future)
                yield job, future.result()
                next_job = next(iterator, None)
                if next_job is not None:
                    pending[pool.submit(function, next_job)] = next_job
    finally:
        for future in pending:
            future.cancel()
        pool.shutdown(wait=True, cancel_futures=True)


class ResponseCache:
    """Content-addressed responses; writes occur only in the coordinating thread."""

    def __init__(self, path):
        path.parent.mkdir(parents=True, exist_ok=True)
        self.connection = sqlite3.connect(path)
        self.connection.execute("CREATE TABLE IF NOT EXISTS responses (key TEXT PRIMARY KEY, payload TEXT NOT NULL)")
        self.connection.commit()

    def get(self, key):
        row = self.connection.execute("SELECT payload FROM responses WHERE key = ?", (key,)).fetchone()
        return json.loads(row[0]) if row else None

    def put(self, key, value):
        self.connection.execute("INSERT OR REPLACE INTO responses VALUES (?, ?)", (key, json.dumps(value)))
        self.connection.commit()

    def close(self):
        self.connection.close()


def validate_vector(vector, dimension):
    array = np.asarray(vector, dtype=np.float32)
    if array.shape != (dimension,) or not np.isfinite(array).all() or np.linalg.norm(array) == 0:
        raise ValueError("Embedding response/cache has invalid dimensions or nonfinite/zero values")
    return array


def embedding_batch(settings, texts, role):
    payload = {"model": settings.embed_model, "input": texts}
    if "voyage" in settings.embed_model.lower():
        payload.update({"output_dimension": settings.dimension, "input_type": role})
    else:
        payload["dimensions"] = settings.dimension
    response, duration = post_json(settings.embed_url, payload, settings.embed_key)
    served_model = response.get("model")
    if served_model is not None and str(served_model).split("/")[-1] != settings.embed_model.split("/")[-1]:
        raise ValueError("Embedding response model differs from requested model")
    rows = response.get("data")
    if not isinstance(rows, list) or len(rows) != len(texts):
        raise ValueError("Embedding response count does not match request")
    indices = [row.get("index") for row in rows]
    if sorted(indices) != list(range(len(texts))):
        raise ValueError("Embedding response indices are invalid")
    rows.sort(key=lambda row: row["index"])
    vectors = [validate_vector(row["embedding"], settings.dimension).tolist() for row in rows]
    return vectors, duration, served_model


def rerank_order(response, candidates):
    results = response.get("results")
    if not isinstance(results, list):
        raise ValueError("Rerank response is missing results")
    indices = [item.get("index") for item in results]
    if any(type(index) is not int or index < 0 or index >= len(candidates) for index in indices):
        raise ValueError("Rerank response index is outside candidate range")
    if len(indices) != len(candidates) or len(set(indices)) != len(indices):
        raise ValueError("Rerank response must contain every candidate exactly once")
    if any(type(result.get("relevance_score")) not in (int, float) or not math.isfinite(result["relevance_score"]) for result in results):
        raise ValueError("Rerank response must provide a finite relevance_score per candidate")
    results = sorted(results, key=lambda item: item["relevance_score"], reverse=True)
    return [candidates[item["index"]] for item in results]


def generate(root, settings, workers=4, batch_size=32):
    if workers < 1 or batch_size < 1:
        raise ValueError("Workers and batch size must be positive")
    folder = root / "experiments" / "datasets"
    documents = json.loads((folder / "documents.json").read_text())
    queries = json.loads((folder / "benchmark_queries.json").read_text())
    manifest = json.loads((folder / "manifest.json").read_text())
    if content_hash(documents) != manifest["corpus_hash"] or content_hash(queries) != manifest["queries_hash"]:
        raise ValueError("Dataset differs from manifest; run prepare_experiment_datasets.py")
    cache = ResponseCache(folder / ".cache" / "responses.sqlite")
    entries = {}
    for collection in COLLECTIONS:
        for document in documents[collection]:
            key = embedding_key(document["text"], settings.embed_model, settings.dimension, "document", settings.embed_url)
            entries[key] = (document["text"], "document")
    for query in queries:
        key = embedding_key(query["natural_prompt"], settings.embed_model, settings.dimension, "query", settings.embed_url)
        entries[key] = (query["natural_prompt"], "query")
    found = {}
    missing = {"document": [], "query": []}
    for key, (text, role) in entries.items():
        cached = cache.get(key)
        if cached:
            validate_vector(cached["vector"], settings.dimension)
            found[key] = cached
        else:
            missing[role].append((key, text))
    batches = [(role, entries[start:start + batch_size]) for role, entries in missing.items() for start in range(0, len(entries), batch_size)]
    print(f"Embedding {len(entries)} unique inputs: {len(found)} cached, {sum(map(len, missing.values()))} missing; model={settings.embed_model}, dimension={settings.dimension}", flush=True)
    run_requests = []
    try:
        request_batch = lambda job: embedding_batch(settings, [text for _, text in job[1]], job[0])
        for completed, ((role, batch), (vectors, duration, served_model)) in enumerate(bounded_results(request_batch, batches, workers), 1):
            run_requests.append({"role": role, "count": len(batch), "duration_ms": duration, "served_model": served_model})
            for (key, _), vector in zip(batch, vectors):
                cached = {"vector": vector, "api_batch_ms_per_item": duration / len(batch), "batch_size": len(batch), "served_model": served_model}
                cache.put(key, cached)
                found[key] = cached
            print(f"Embedded batch {completed}/{len(batches)} ({len(found)}/{len(entries)} inputs)", flush=True)
        arrays = {}
        for collection in COLLECTIONS:
            records = documents[collection]
            arrays[collection + "__vectors"] = np.stack([found[embedding_key(item["text"], settings.embed_model, settings.dimension, "document", settings.embed_url)]["vector"] for item in records]).astype(np.float32)
            for key, field in [("skills", "skill"), ("paths", "path"), ("ids", "id")]:
                arrays[collection + "__" + key] = np.asarray([item[field] for item in records], dtype=str)
        arrays["query_vectors"] = np.stack([found[embedding_key(query["natural_prompt"], settings.embed_model, settings.dimension, "query", settings.embed_url)]["vector"] for query in queries]).astype(np.float32)
        arrays["query_ids"] = np.asarray([query["query_id"] for query in queries], dtype=str)
        arrays["query_embedding_api_batch_ms_per_item"] = np.asarray([found[embedding_key(query["natural_prompt"], settings.embed_model, settings.dimension, "query", settings.embed_url)]["api_batch_ms_per_item"] for query in queries])
        with (folder / "embeddings.npz.tmp").open("wb") as output:
            np.savez_compressed(output, **arrays)
        (folder / "embeddings.npz.tmp").replace(folder / "embeddings.npz")
        info = {
            "schema_version": 2,
            "created_at": datetime.now(timezone.utc).isoformat(),
            "model": settings.embed_model,
            "observed_models": sorted({entry["served_model"] for entry in found.values() if entry.get("served_model")}),
            "dimension": settings.dimension,
            "corpus_hash": manifest["corpus_hash"],
            "queries_hash": manifest["queries_hash"],
            "config_fingerprint": settings.fingerprint,
            "document_count_by_collection": manifest["document_count_by_collection"],
            "query_count": len(queries),
            "api_timing": {
                "current_run_requests": run_requests,
                "query_per_item_timing": "API batch wall time divided by batch size; cached original service observations, not single-query end-to-end latency",
            },
        }
        (folder / "embedding_manifest.json").write_text(json.dumps(info, indent=2) + "\n")
    finally:
        cache.close()
    print("Saved embeddings.npz and embedding_manifest.json", flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--config", type=Path, default=Path("~/.config/qmd/index.yml"))
    parser.add_argument("--embed-model")
    parser.add_argument("--dimension", type=int)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--batch-size", type=int, default=32)
    args = parser.parse_args()
    settings = load_settings(args.config, args.embed_model, args.dimension)
    generate(args.root, settings, args.workers, args.batch_size)


if __name__ == "__main__":
    main()
