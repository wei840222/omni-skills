#!/usr/bin/env python3
"""
Generate BM25-friendly keyword prompts for test-prompts.json across all refactored skills.
Uses bifrost (Gemini 3.1 Flash) via OpenAI-compatible endpoint.
"""

import json
import os
import re
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

API_URL = "https://bifrost.home-infra.weii.cloud/openai/v1/chat/completions"
MODEL = "gemini-3.1-flash-lite-agy"

def get_refactored_skills(changelog_path: Path) -> list[str]:
    skills = []
    seen = set()
    for line in changelog_path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*([a-zA-Z0-9_\-]+)\s*\|", line)
        if m:
            slug = m.group(1).strip()
            if slug not in ("Skill", "----------------------------") and slug not in seen:
                skills.append(slug)
                seen.add(slug)
    return skills

def call_gemini_keywords(skill_slug: str, desc: str, prompt: str) -> str:
    system_prompt = (
        "You are an expert in Information Retrieval (BM25 keyword search). "
        "Your task is to generate 3 to 6 concise, highly discriminative BM25 search keywords "
        "that an agent or user would query to find the tool/skill needed to solve the task.\n"
        "Rules:\n"
        "- Output ONLY the space-separated keywords without any prefix, punctuation, or markdown.\n"
        "- Match the language of the task prompt (English or Traditional Chinese).\n"
        "- Focus on functional verbs, core domain entities, and tool capabilities."
    )
    user_content = f"Skill: {skill_slug}\nDescription: {desc}\nTask Prompt: {prompt}\n\nBM25 Keywords:"

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content}
        ],
        "temperature": 0.2
    }

    req = urllib.request.Request(
        API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY', '')}"
        }
    )

    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            keywords = data["choices"][0]["message"]["content"].strip()
            # Clean up any surrounding quotes or backticks
            keywords = re.sub(r"^[`'\"]+|[`'\"]+$", "", keywords).strip()
            return keywords
    except Exception as e:
        print(f"Error calling API for {skill_slug}: {e}", file=sys.stderr)
        return ""

def process_skill(slug: str, root_dir: Path) -> int:
    skill_dir = root_dir / "skills" / slug
    tp_file = skill_dir / "test-prompts.json"
    skill_file = skill_dir / "SKILL.md"

    if not tp_file.exists() or not skill_file.exists():
        return 0

    desc = ""
    try:
        content = skill_file.read_text(encoding="utf-8")
        if "description:" in content:
            desc_match = re.search(r"description:\s*(?:>-\s*)?(.*?)(?:\n[a-z0-9_\-]+:|\n---)", content, re.DOTALL)
            if desc_match:
                desc = desc_match.group(1).strip()
    except Exception:
        pass

    try:
        prompts_data = json.loads(tp_file.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"Error reading {tp_file}: {e}", file=sys.stderr)
        return 0

    updated = 0
    for item in prompts_data:
        if "prompt" in item:
            # Generate or update bm25_prompt
            prompt_text = item["prompt"]
            if not item.get("bm25_prompt"):
                kw = call_gemini_keywords(slug, desc, prompt_text)
                if kw:
                    item["bm25_prompt"] = kw
                    updated += 1

    if updated > 0:
        tp_file.write_text(json.dumps(prompts_data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    return updated

def main():
    root_dir = Path(__file__).resolve().parent.parent.parent
    changelog_path = root_dir / "CHANGELOG.md"
    skills = get_refactored_skills(changelog_path)

    print(f"[*] Processing {len(skills)} skills for BM25 keyword generation...")
    total_updated = 0

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {executor.submit(process_skill, s, root_dir): s for s in skills}
        for future in as_completed(futures):
            s = futures[future]
            try:
                count = future.result()
                if count > 0:
                    print(f"  [✓] {s}: added {count} bm25 prompts")
                    total_updated += count
            except Exception as e:
                print(f"  [✗] {s} error: {e}", file=sys.stderr)

    print(f"\n[✓] Completed! Total BM25 keyword prompts generated: {total_updated}")

    # Compile consolidated benchmark dataset
    benchmark_items = []
    for slug in skills:
        tp_file = root_dir / "skills" / slug / "test-prompts.json"
        if tp_file.exists():
            try:
                data = json.loads(tp_file.read_text(encoding="utf-8"))
                for idx, item in enumerate(data):
                    benchmark_items.append({
                        "query_id": f"{slug}_{item.get('id', idx+1)}",
                        "ground_truth_skill": slug,
                        "natural_prompt": item.get("prompt", ""),
                        "bm25_prompt": item.get("bm25_prompt", item.get("prompt", "")),
                        "expected": item.get("expected", "")
                    })
            except Exception:
                pass

    dataset_out = root_dir / "experiments" / "datasets" / "benchmark_queries.json"
    dataset_out.parent.mkdir(parents=True, exist_ok=True)
    dataset_out.write_text(json.dumps(benchmark_items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"[✓] Compiled consolidated benchmark dataset ({len(benchmark_items)} queries) to: {dataset_out}")

if __name__ == "__main__":
    main()
