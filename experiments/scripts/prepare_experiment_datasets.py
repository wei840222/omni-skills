#!/usr/bin/env python3
"""
Prepare datasets for SkillRouter replication experiments.

Reads all refactored skills listed in CHANGELOG.md and generates two datasets in `experiments/datasets/`:
1. `name-description`: Contains only skill name + description (metadata-only).
2. `full`: Contains the full SKILL.md file.
"""

import os
import re
import sys
import yaml
from pathlib import Path

def parse_changelog_skills(changelog_path: Path) -> list[str]:
    if not changelog_path.exists():
        raise FileNotFoundError(f"Changelog not found: {changelog_path}")
    
    skills = []
    seen = set()
    for line in changelog_path.read_text(encoding="utf-8").splitlines():
        match = re.match(r"^\|\s*([a-zA-Z0-9_\-]+)\s*\|", line)
        if match:
            slug = match.group(1).strip()
            if slug not in ("Skill", "----------------------------") and slug not in seen:
                skills.append(slug)
                seen.add(slug)
    return skills

def extract_frontmatter(content: str) -> tuple[dict, str]:
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            fm_text = parts[1]
            body = parts[2].strip()
            try:
                data = yaml.safe_load(fm_text) or {}
                return data, body
            except yaml.YAMLError:
                pass
    return {}, content

def main():
    root_dir = Path(__file__).resolve().parent.parent.parent
    changelog_path = root_dir / "CHANGELOG.md"
    skills_dir = root_dir / "skills"
    
    exp_dir = root_dir / "experiments" / "datasets"
    nd_dir = exp_dir / "name-description"
    full_dir = exp_dir / "full"
    
    nd_dir.mkdir(parents=True, exist_ok=True)
    full_dir.mkdir(parents=True, exist_ok=True)
    
    skills = parse_changelog_skills(changelog_path)
    print(f"[*] Found {len(skills)} refactored skills in CHANGELOG.md")
    
    processed = 0
    missing = []
    
    for slug in skills:
        src_file = skills_dir / slug / "SKILL.md"
        if not src_file.exists():
            missing.append(slug)
            continue
        
        full_content = src_file.read_text(encoding="utf-8")
        fm_data, _ = extract_frontmatter(full_content)
        
        name = fm_data.get("name", slug)
        desc = fm_data.get("description", "").strip()
        
        # 1. Dataset 1: Name + Description only (name-description)
        target_nd_dir = nd_dir / slug
        target_nd_dir.mkdir(parents=True, exist_ok=True)
        nd_file = target_nd_dir / "SKILL.md"
        
        # Format clean markdown with frontmatter and body description
        nd_content = (
            f"---\n"
            f"name: {name}\n"
            f"description: >-\n"
            f"  {desc}\n"
            f"---\n\n"
            f"# {name}\n\n"
            f"{desc}\n"
        )
        nd_file.write_text(nd_content, encoding="utf-8")
        
        # 2. Dataset 2: Full SKILL.md (full)
        target_full_dir = full_dir / slug
        target_full_dir.mkdir(parents=True, exist_ok=True)
        all_file = target_full_dir / "SKILL.md"
        all_file.write_text(full_content, encoding="utf-8")
        
        processed += 1
    
    print(f"[✓] Successfully prepared {processed} skills in:")
    print(f"    - Name-Description dataset: {nd_dir}")
    print(f"    - Full dataset: {full_dir}")
    
    if missing:
        print(f"[!] Warning: {len(missing)} skills were not found in {skills_dir}: {missing}")

if __name__ == "__main__":
    main()
