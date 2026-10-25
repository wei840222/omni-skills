#!/usr/bin/env python3
"""Compile original test prompts without answer-conditioned keyword generation.

The historical filename is retained for the documented command. This script
never calls a model and never modifies skill packages.
"""

import argparse
import json
from pathlib import Path


def compile_queries(root: Path) -> list[dict]:
    queries = []
    seen = set()
    for entrypoint in sorted((root / "skills").glob("*/SKILL.md")):
        slug = entrypoint.parent.name
        prompt_file = entrypoint.parent / "test-prompts.json"
        if not prompt_file.exists():
            raise ValueError(f"Missing test prompts: {slug}")
        records = json.loads(prompt_file.read_text(encoding="utf-8"))
        if not isinstance(records, list) or not records:
            raise ValueError(f"Expected nonempty test prompt list: {slug}")
        for index, item in enumerate(records, start=1):
            if not isinstance(item, dict) or not isinstance(item.get("prompt"), str) or not item["prompt"].strip():
                raise ValueError(f"Invalid prompt: {slug} item {index}")
            query_id = f"{slug}_{item.get('id', index)}"
            if query_id in seen:
                raise ValueError(f"Duplicate query ID: {query_id}")
            seen.add(query_id)
            queries.append({
                "query_id": query_id,
                "ground_truth_skill": slug,
                "natural_prompt": item["prompt"],
                "expected": item.get("expected", ""),
            })
    if not queries:
        raise ValueError("No test prompts found")
    return queries


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    args = parser.parse_args()
    output = args.root / "experiments" / "datasets" / "benchmark_queries.json"
    output.parent.mkdir(parents=True, exist_ok=True)
    queries = compile_queries(args.root)
    output.write_text(json.dumps(queries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Compiled {len(queries)} original queries; legacy bm25_prompt ignored; skill files unchanged.")


if __name__ == "__main__":
    main()
