#!/usr/bin/env python3
"""Validate every skill in this repository without third-party dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_PATTERN = re.compile(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|\Z)", re.DOTALL)
FIELD_PATTERN = re.compile(r"^([a-zA-Z0-9_-]+):\s*(.*?)\s*$")
MAX_NAME_LENGTH = 64


def unquote(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def top_level_fields(frontmatter: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for line in frontmatter.splitlines():
        if line.startswith((" ", "\t")):
            continue
        match = FIELD_PATTERN.match(line)
        if match:
            fields[match.group(1)] = unquote(match.group(2).strip())
    return fields


def validate_skill(skill_md: Path) -> list[str]:
    errors: list[str] = []
    content = skill_md.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(content)
    if not match:
        return ["missing or malformed YAML frontmatter"]

    fields = top_level_fields(match.group(1))
    name = fields.get("name", "")
    description = fields.get("description", "")

    if not name:
        errors.append("frontmatter is missing name")
    elif not NAME_PATTERN.fullmatch(name) or len(name) > MAX_NAME_LENGTH:
        errors.append("name must be lowercase hyphen-case and at most 64 characters")
    elif name != skill_md.parent.name:
        errors.append(f"name '{name}' does not match folder '{skill_md.parent.name}'")

    if not description:
        errors.append("frontmatter is missing description")
    elif "TODO" in description:
        errors.append("description still contains TODO")
    elif "<" in description or ">" in description:
        errors.append("description cannot contain angle brackets")
    elif len(description) > 1024:
        errors.append("description exceeds 1024 characters")

    if re.search(r"\[TODO:[^\]]*\]", content):
        errors.append("instructions still contain a TODO placeholder")

    metadata = skill_md.parent / "agents" / "openai.yaml"
    if metadata.exists():
        metadata_text = metadata.read_text(encoding="utf-8")
        if "TODO" in metadata_text:
            errors.append("agents/openai.yaml still contains a TODO placeholder")
        prompt_match = re.search(r"^\s*default_prompt:\s*[\"']?(.*?)[\"']?\s*$", metadata_text, re.MULTILINE)
        if prompt_match and f"${name}" not in prompt_match.group(1):
            errors.append(f"agents/openai.yaml default_prompt must mention ${name}")
        policy_match = re.search(
            r"^\s*allow_implicit_invocation:\s*(\S+)\s*$", metadata_text, re.MULTILINE
        )
        if policy_match and policy_match.group(1).lower() not in {"true", "false"}:
            errors.append("allow_implicit_invocation must be true or false")

    return errors


def main() -> int:
    repo_root = Path(__file__).resolve().parents[1]
    skills_root = repo_root / "skills"
    skill_files = sorted(skills_root.glob("*/*/SKILL.md"))
    if not skill_files:
        print("No skills found. The repository scaffold is valid and ready.")
        return 0

    failure_count = 0
    for skill_md in skill_files:
        relative_path = skill_md.parent.relative_to(repo_root)
        errors = validate_skill(skill_md)
        if errors:
            failure_count += 1
            print(f"FAIL {relative_path}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK   {relative_path}")

    if failure_count:
        print(f"\n{failure_count} skill(s) failed validation.")
        return 1

    print(f"\nValidated {len(skill_files)} skill(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
