# Vinayak Skills

A personal repository for reusable agent skills. The layout is inspired by
[mattpocock/skills](https://github.com/mattpocock/skills), with a smaller
authoring-focused core so publishing machinery can be added only when needed.

## Create a skill

Start a draft in `skills/in-progress/`:

```bash
python scripts/new_skill.py my-skill
```

Choose a stable category when the scope is already clear:

```bash
python scripts/new_skill.py my-skill --category engineering
python scripts/new_skill.py my-skill --category productivity
python scripts/new_skill.py my-skill --category misc
```

Add optional resource directories only when the workflow needs them:

```bash
python scripts/new_skill.py my-skill --resources scripts,references
```

Use `--explicit-only` for a skill that should run only when a person invokes it.
Otherwise, skills are discoverable by the model by default.

The command creates:

```text
skills/<category>/<skill-name>/
|-- SKILL.md
`-- agents/
    `-- openai.yaml
```

A skill may later add `scripts/`, `references/`, or `assets/` when those files
provide concrete value.

## Finish and validate

Replace every `TODO` in the generated skill, keep its description precise about
when it applies, and then run:

```bash
python scripts/validate_skills.py
```

The validator checks every `SKILL.md`, folder naming, unfinished placeholders,
and the essential Codex metadata. Move a completed draft from `in-progress` to
`engineering`, `productivity`, or `misc` before publishing it.

See [skills/README.md](skills/README.md) for category and invocation guidance.
