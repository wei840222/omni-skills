#!/usr/bin/env python3
"""Snapshot every current skill into three chunked routing representations."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess

import yaml

from generate_bm25_prompts import compile_queries

COLLECTIONS = ("name-description", "full", "full-references")


def content_hash(value) -> str:
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def chunk_text(text: str, size: int = 6000, overlap: int = 400) -> list[str]:
    if size < 2 or overlap < 0 or overlap >= size // 2:
        raise ValueError("Chunk overlap must be nonnegative and less than half the chunk size")
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + size, len(text))
        # Byte-level BPE cannot have more tokens than UTF-8 bytes. Leave room
        # for the skill prefix below and the embedding service's 8192-token cap.
        bounded = text[start:end].encode("utf-8")[:7500].decode("utf-8", errors="ignore")
        end = start + len(bounded)
        if end < len(text):
            boundary = text.rfind("\n", start + size // 2, end)
            if boundary > start:
                end = boundary
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end == len(text):
            break
        start = max(start + 1, end - overlap)
    return chunks


def prepare(root: Path, chunk_size: int = 6000, overlap: int = 400):
    documents = {collection: [] for collection in COLLECTIONS}
    skill_files = sorted((root / "skills").glob("*/SKILL.md"))
    if not skill_files:
        raise ValueError("No skills/*/SKILL.md found")
    source_files = {}
    for entrypoint in skill_files:
        slug = entrypoint.parent.name
        full_text = entrypoint.read_text(encoding="utf-8")
        if not full_text.startswith("---"):
            raise ValueError(f"Missing YAML frontmatter: {slug}")
        sections = full_text.split("---", 2)
        if len(sections) != 3:
            raise ValueError(f"Unclosed YAML frontmatter: {slug}")
        metadata = yaml.safe_load(sections[1])
        if not isinstance(metadata, dict) or not isinstance(metadata.get("description"), str):
            raise ValueError(f"Invalid skill description: {slug}")
        nd = f"{metadata.get('name', slug)}\n{metadata['description']}"
        documents["name-description"].append({"id": f"{slug}/name-description", "skill": slug, "path": str(entrypoint.relative_to(root)), "text": nd})
        references = sorted((entrypoint.parent / "references").rglob("*.md"))
        for source in [entrypoint, *references]:
            relative = str(source.relative_to(root))
            text = full_text if source == entrypoint else source.read_text(encoding="utf-8")
            source_files[relative] = hashlib.sha256(text.encode()).hexdigest()
            chunks = chunk_text(text, chunk_size, overlap)
            for index, chunk in enumerate(chunks):
                document = {"id": f"{relative}#{index}", "skill": slug, "path": relative, "text": f"Skill: {slug}\n{chunk}"}
                documents["full-references"].append(document)
                if source == entrypoint:
                    documents["full"].append(document)
    queries = compile_queries(root)
    for prompt_file in sorted((root / "skills").glob("*/test-prompts.json")):
        source_files[str(prompt_file.relative_to(root))] = hashlib.sha256(prompt_file.read_bytes()).hexdigest()
    git = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    manifest = {
        "schema_version": 2,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "source_git_commit": git,
        "skill_count": len(skill_files),
        "query_count": len(queries),
        "document_count_by_collection": {key: len(value) for key, value in documents.items()},
        "corpus_hash": content_hash(documents),
        "queries_hash": content_hash(queries),
        "source_files": source_files,
        "chunk_size_chars": chunk_size,
        "chunk_overlap_chars": overlap,
        "protocol": "All current skills; original natural prompts for every pipeline; single owning-skill label from author test prompts. No answer-conditioned keyword generation. Chunk max pooling per skill.",
    }
    output = root / "experiments" / "datasets"
    output.mkdir(parents=True, exist_ok=True)
    for filename, data in [("documents.json", documents), ("benchmark_queries.json", queries), ("manifest.json", manifest)]:
        temporary = output / (filename + ".tmp")
        temporary.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        temporary.replace(output / filename)
    return manifest


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--chunk-size", type=int, default=6000)
    parser.add_argument("--overlap", type=int, default=400)
    args = parser.parse_args()
    manifest = prepare(args.root, args.chunk_size, args.overlap)
    print(json.dumps({key: manifest[key] for key in ("skill_count", "query_count", "document_count_by_collection", "corpus_hash", "queries_hash")}, indent=2))


if __name__ == "__main__":
    main()
