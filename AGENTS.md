# Agent instructions

This repository contains reusable agent skills. Read `skills/README.md` before
creating, moving, or substantially editing one.

- Use the `skill-creator` and `writing-for-agents` skills when they are available.
- Put each skill at `skills/<category>/<skill-name>/SKILL.md`.
- Keep `SKILL.md` focused on guidance that changes agent behavior; disclose
  conditional detail through clearly routed files in `references/`.
- Add `scripts/`, `references/`, and `assets/` only when the skill actually uses
  them.
- Preserve user intent and authorization boundaries in every workflow.
- Run `python scripts/validate_skills.py` after changing skill files.
