#!/usr/bin/env python3
"""Create a new skill in this repository."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


CATEGORIES = ("engineering", "productivity", "misc", "in-progress")
RESOURCE_TYPES = ("scripts", "references", "assets")
MAX_NAME_LENGTH = 64


def normalize_name(raw_name: str) -> str:
    """Normalize a proposed skill name to lowercase hyphen-case."""
    name = re.sub(r"[^a-z0-9]+", "-", raw_name.strip().lower())
    return re.sub(r"-{2,}", "-", name).strip("-")


def parse_resources(raw_resources: str) -> list[str]:
    resources = [item.strip() for item in raw_resources.split(",") if item.strip()]
    invalid = sorted(set(resources) - set(RESOURCE_TYPES))
    if invalid:
        allowed = ", ".join(RESOURCE_TYPES)
        raise ValueError(f"unknown resource type(s): {', '.join(invalid)}; allowed: {allowed}")
    return list(dict.fromkeys(resources))


def skill_markdown(name: str, title: str) -> str:
    return f'''---
name: {name}
description: "[TODO: Say what this skill does and the distinct conditions that should activate it.]"
---

# {title}

[TODO: Add the non-obvious guidance, workflow, constraints, and completion criteria this skill needs.]
'''


def openai_yaml(name: str, title: str, explicit_only: bool) -> str:
    implicit = "false" if explicit_only else "true"
    display_name = json.dumps(title)
    short_description = json.dumps("[TODO: Describe this skill for the UI]")
    default_prompt = json.dumps(f"Use ${name} to complete the requested workflow.")
    return f'''interface:
  display_name: {display_name}
  short_description: {short_description}
  default_prompt: {default_prompt}

policy:
  allow_implicit_invocation: {implicit}
'''


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Create a new skill draft.")
    parser.add_argument("name", help="Skill name; normalized to lowercase hyphen-case")
    parser.add_argument(
        "--category",
        choices=CATEGORIES,
        default="in-progress",
        help="Destination category (default: in-progress)",
    )
    parser.add_argument(
        "--resources",
        default="",
        help="Comma-separated optional directories: scripts,references,assets",
    )
    parser.add_argument(
        "--explicit-only",
        action="store_true",
        help="Disable automatic model invocation in agents/openai.yaml",
    )
    parser.add_argument(
        "--root",
        type=Path,
        help=argparse.SUPPRESS,
    )
    return parser


def main() -> int:
    args = build_parser().parse_args()
    name = normalize_name(args.name)
    if not name:
        print("error: the skill name must contain a letter or digit", file=sys.stderr)
        return 1
    if len(name) > MAX_NAME_LENGTH:
        print(f"error: normalized name exceeds {MAX_NAME_LENGTH} characters", file=sys.stderr)
        return 1

    try:
        resources = parse_resources(args.resources)
    except ValueError as error:
        print(f"error: {error}", file=sys.stderr)
        return 1

    repo_root = args.root.resolve() if args.root else Path(__file__).resolve().parents[1]
    skill_dir = repo_root / "skills" / args.category / name
    if skill_dir.exists():
        print(f"error: skill directory already exists: {skill_dir}", file=sys.stderr)
        return 1

    title = " ".join(part.capitalize() for part in name.split("-"))
    (skill_dir / "agents").mkdir(parents=True)
    (skill_dir / "SKILL.md").write_text(skill_markdown(name, title), encoding="utf-8")
    (skill_dir / "agents" / "openai.yaml").write_text(
        openai_yaml(name, title, args.explicit_only), encoding="utf-8"
    )
    for resource in resources:
        (skill_dir / resource).mkdir()

    if name != args.name:
        print(f"Normalized '{args.name}' to '{name}'.")
    print(f"Created {skill_dir}")
    print("Replace the TODOs, add only needed resources, then run:")
    print("  python scripts/validate_skills.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
