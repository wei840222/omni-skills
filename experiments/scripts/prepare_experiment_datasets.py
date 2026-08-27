#!/usr/bin/env python3
"""
Prepare datasets for SkillRouter replication experiments.

Reads all refactored skills listed in CHANGELOG.md and generates three datasets in `experiments/datasets/`:
1. `name-description`: Contains only skill name + description (metadata-only).
2. `full`: Contains the full SKILL.md file.
3. `full-references`: Contains the full SKILL.md file plus all files under `references/`.
"""

import os
import re
import sys
import shutil
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
    ref_dir = exp_dir / "full-references"
    
    nd_dir.mkdir(parents=True, exist_ok=True)
    full_dir.mkdir(parents=True, exist_ok=True)
    ref_dir.mkdir(parents=True, exist_ok=True)
    
    skills = parse_changelog_skills(changelog_path)
    print(f"[*] Found {len(skills)} refactored skills in CHANGELOG.md")
    
    processed = 0
    missing = []
    
    for slug in skills:
        src_skill_dir = skills_dir / slug
        src_file = src_skill_dir / "SKILL.md"
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
        
        # 3. Dataset 3: Full SKILL.md + references (full-references)
        target_ref_dir = ref_dir / slug
        target_ref_dir.mkdir(parents=True, exist_ok=True)
        ref_skill_file = target_ref_dir / "SKILL.md"
        ref_skill_file.write_text(full_content, encoding="utf-8")
        
        src_refs = src_skill_dir / "references"
        target_refs = target_ref_dir / "references"
        if src_refs.exists() and src_refs.is_dir():
            if target_refs.exists():
                shutil.rmtree(target_refs)
            shutil.copytree(src_refs, target_refs)
            
        processed += 1
    
    print(f"[✓] Successfully prepared {processed} skills in:")
    print(f"    - Name-Description dataset: {nd_dir}")
    print(f"    - Full dataset: {full_dir}")
    print(f"    - Full + References dataset: {ref_dir}")
    
    if missing:
        print(f"[!] Warning: {len(missing)} skills were not found in {skills_dir}: {missing}")

if __name__ == "__main__":
    main()
