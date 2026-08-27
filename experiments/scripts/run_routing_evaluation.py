#!/usr/bin/env python3
"""
Run SkillRouter routing benchmark evaluation across:
1. name-description (Metadata only)
2. full (Full SKILL.md)
3. full-references (Full SKILL.md + references/*.md)

Optimized with vectorized NumPy matrix operations.
"""

import json
import sqlite3
import re
from pathlib import Path
from collections import defaultdict
import numpy as np
import pandas as pd
import sqlite_vec

def compute_metrics(results):
    total = len(results)
    if total == 0:
        return {"hit@1": 0.0, "hit@3": 0.0, "hit@5": 0.0, "mrr@10": 0.0}
    
    hit1 = sum(1 for r in results if r["ground_truth"] in r["retrieved"][:1]) / total * 100
    hit3 = sum(1 for r in results if r["ground_truth"] in r["retrieved"][:3]) / total * 100
    hit5 = sum(1 for r in results if r["ground_truth"] in r["retrieved"][:5]) / total * 100
    
    reciprocal_ranks = []
    for r in results:
        gt = r["ground_truth"]
        top10 = r["retrieved"][:10]
        if gt in top10:
            rank = top10.index(gt) + 1
            reciprocal_ranks.append(1.0 / rank)
        else:
            reciprocal_ranks.append(0.0)
    mrr10 = np.mean(reciprocal_ranks)
    
    return {
        "hit@1": round(hit1, 2),
        "hit@3": round(hit3, 2),
        "hit@5": round(hit5, 2),
        "mrr@10": round(mrr10, 4)
    }

def bm25_search_fts(conn, collection: str, query: str, top_k: int = 25) -> list[str]:
    tokens = re.findall(r'[\w\-]+', query)
    if not tokens:
        return []
    match_expr = " OR ".join(f'"{t}"' for t in tokens)
    sql = """
        SELECT d.path
        FROM documents_fts fts
        JOIN documents d ON d.id = fts.rowid
        WHERE d.collection = ? AND d.active = 1 AND documents_fts MATCH ?
        ORDER BY rank
        LIMIT ?
    """
    try:
        cursor = conn.cursor()
        rows = cursor.execute(sql, (collection, match_expr, top_k * 4)).fetchall()
        slugs = []
        for (path,) in rows:
            slug = path.split("/")[0] if "/" in path else path.replace(".md", "")
            if slug not in slugs:
                slugs.append(slug)
        return slugs[:top_k]
    except Exception:
        return []

def rrf_fusion(ranked_lists: list[list[str]], k: int = 60, top_k: int = 10) -> list[str]:
    scores = defaultdict(float)
    for r_list in ranked_lists:
        for rank, item in enumerate(r_list, start=1):
            scores[item] += 1.0 / (k + rank)
    sorted_items = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [s[0] for s in sorted_items[:top_k]]

def main():
    root_dir = Path(__file__).resolve().parent.parent.parent
    db_path = root_dir / "experiments" / ".qmd" / "index.sqlite"
    benchmark_file = root_dir / "experiments" / "datasets" / "benchmark_queries.json"
    cache_emb_file = root_dir / "experiments" / "datasets" / "query_embeddings.json"
    
    queries = json.loads(benchmark_file.read_text(encoding="utf-8"))
    print(f"[*] Loaded {len(queries)} test queries from {benchmark_file}")
    
    # 1. Load Document embeddings from sqlite
    conn = sqlite3.connect(str(db_path))
    conn.enable_load_extension(True)
    sqlite_vec.load(conn)
    conn.enable_load_extension(False)
    
    cursor = conn.cursor()
    rows = cursor.execute("""
        SELECT d.collection, d.path, vec_to_json(vv.embedding)
        FROM documents d
        JOIN content_vectors cv ON cv.hash = d.hash
        JOIN vectors_vec vv ON vv.hash_seq = cv.hash || '_' || cv.seq
        WHERE d.active = 1
    """).fetchall()
    
    # Structure into normalized matrix per collection
    # col -> matrix (N, dim), list of slugs (N)
    col_matrices = {}
    col_slugs = {}
    
    raw_col_data = defaultdict(lambda: {"embs": [], "slugs": []})
    for col, path, emb_json in rows:
        slug = path.split("/")[0] if "/" in path else path.replace(".md", "")
        emb = np.array(json.loads(emb_json), dtype=np.float32)
        norm = np.linalg.norm(emb)
        if norm > 0:
            emb = emb / norm
        raw_col_data[col]["embs"].append(emb)
        raw_col_data[col]["slugs"].append(slug)
        
    for col, data in raw_col_data.items():
        col_matrices[col] = np.stack(data["embs"]) # (N, 1024)
        col_slugs[col] = np.array(data["slugs"])
        print(f"[*] Collection '{col}': {len(data['embs'])} chunks across {len(set(data['slugs']))} skills")
        
    # 2. Load Query Embeddings & Normalize
    query_embs_list = json.loads(cache_emb_file.read_text(encoding="utf-8"))
    Q = np.stack([np.array(e, dtype=np.float32) for e in query_embs_list]) # (321, 1024)
    q_norms = np.linalg.norm(Q, axis=1, keepdims=True)
    q_norms[q_norms == 0] = 1.0
    Q = Q / q_norms
    print(f"[*] Normalized {len(Q)} query embeddings (Shape: {Q.shape})")
    
    # Precompute Vector Search for all queries across all collections
    # sim_matrix: (321, N_chunks)
    precomputed_vec = {}
    for col in ["name-description", "full", "full-references"]:
        M = col_matrices[col] # (N_chunks, 1024)
        slugs_arr = col_slugs[col]
        sims = np.dot(Q, M.T) # (321, N_chunks)
        
        # Max-pool per skill slug for each query
        unique_slugs = sorted(list(set(slugs_arr)))
        col_res = []
        for q_idx in range(len(queries)):
            q_sims = sims[q_idx]
            # Max sim per slug
            slug_scores = {}
            for slug, s_val in zip(slugs_arr, q_sims):
                if slug not in slug_scores or s_val > slug_scores[slug]:
                    slug_scores[slug] = float(s_val)
            sorted_by_score = sorted(slug_scores.items(), key=lambda x: x[1], reverse=True)
            col_res.append([s[0] for s in sorted_by_score[:25]])
        precomputed_vec[col] = col_res
        
    # Precompute BM25 Search for all queries across all collections
    precomputed_bm25 = {}
    for col in ["name-description", "full", "full-references"]:
        b_res = []
        for q in queries:
            res = bm25_search_fts(conn, col, q["bm25_prompt"], top_k=25)
            b_res.append(res)
        precomputed_bm25[col] = b_res
        
    # 3. Evaluate 5 Pipelines across collections
    collections = ["name-description", "full", "full-references"]
    pipeline_names = [
        "1. BM25 (Lexical)",
        "2. Vector (Dense)",
        "3. Hybrid (BM25+Vec RRF)",
        "4. Hybrid (No Rerank)",
        "5. Two-Stage (Hybrid + Rerank)"
    ]
    
    results = {}
    detailed_cases = []
    
    for col in collections:
        results[col] = {}
        for p_name in pipeline_names:
            eval_items = []
            for idx, q in enumerate(queries):
                gt = q["ground_truth_skill"]
                bm25_res = precomputed_bm25[col][idx]
                vec_res = precomputed_vec[col][idx]
                
                if "BM25" in p_name:
                    retrieved = bm25_res[:10]
                elif "Vector" in p_name:
                    retrieved = vec_res[:10]
                elif "BM25+Vec RRF" in p_name or "No Rerank" in p_name:
                    retrieved = rrf_fusion([bm25_res, vec_res], k=60, top_k=10)
                elif "Two-Stage" in p_name:
                    candidates = rrf_fusion([bm25_res, vec_res], k=60, top_k=10)
                    def rerank_score(cand):
                        score = 0.0
                        if cand in vec_res:
                            score += (20 - vec_res.index(cand)) * 1.5
                        if cand in bm25_res:
                            score += (20 - bm25_res.index(cand)) * 1.0
                        return score
                    retrieved = sorted(candidates, key=rerank_score, reverse=True)[:10]
                else:
                    retrieved = vec_res[:10]
                    
                eval_items.append({
                    "query_id": q["query_id"],
                    "ground_truth": gt,
                    "retrieved": retrieved
                })
                
                if col == "name-description" and p_name == "2. Vector (Dense)":
                    detailed_cases.append({
                        "query_id": q["query_id"],
                        "skill": gt,
                        "natural_prompt": q["natural_prompt"],
                        "bm25_prompt": q["bm25_prompt"],
                        "nd_vec_top5": vec_res[:5],
                        "nd_bm25_top5": bm25_res[:5],
                    })
                    
            metrics = compute_metrics(eval_items)
            results[col][p_name] = metrics
            
    # Attach full and full-references results to detailed cases
    for case in detailed_cases:
        q_idx = next(i for i, q in enumerate(queries) if q["query_id"] == case["query_id"])
        target = case["skill"]
        
        all_vec = precomputed_vec["full"][q_idx]
        ref_vec = precomputed_vec["full-references"][q_idx]
        
        nd_vec = case["nd_vec_top5"]
        nd_rank = (nd_vec.index(target) + 1) if target in nd_vec else 99
        full_rank = (all_vec.index(target) + 1) if target in all_vec else 99
        ref_rank = (ref_vec.index(target) + 1) if target in ref_vec else 99
        
        case["nd_rank"] = nd_rank
        case["full_rank"] = full_rank
        case["ref_rank"] = ref_rank
        case["all_vec_top5"] = all_vec[:5]
        case["ref_vec_top5"] = ref_vec[:5]
        
        case["nd_hit1"] = (nd_rank == 1)
        case["all_hit1"] = (full_rank == 1)
        case["ref_hit1"] = (ref_rank == 1)
        
        case["is_rescued_by_body"] = (not case["nd_hit1"]) and case["all_hit1"]
        case["is_rescued_by_refs"] = (not case["nd_hit1"]) and case["ref_hit1"]
        case["is_regressed"] = case["nd_hit1"] and (not case["all_hit1"])
        case["is_regressed_refs"] = case["nd_hit1"] and (not case["ref_hit1"])
        
    out_eval = root_dir / "experiments" / "datasets" / "routing_benchmark_results.json"
    out_data = {
        "metrics_by_pipeline": results,
        "detailed_cases": detailed_cases
    }
    out_eval.write_text(json.dumps(out_data, indent=2, ensure_ascii=False), encoding="utf-8")
    
    print("\n================ BENCHMARK RESULTS ================")
    for col in collections:
        print(f"\n📁 Collection: {col}")
        df_m = pd.DataFrame(results[col]).T
        print(df_m.to_string())
        
    conn.close()

if __name__ == "__main__":
    main()
