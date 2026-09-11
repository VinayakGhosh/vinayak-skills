# Skill organization

Each direct child of a category is one installable skill. Its folder name and
the `name` in `SKILL.md` must match and use lowercase hyphen-case.

| Category | Purpose |
| --- | --- |
| `engineering/` | Software delivery, code quality, architecture, and developer tooling |
| `productivity/` | General workflows that are useful beyond codebases |

## Skill anatomy

Only `SKILL.md` is required:

```text
skill-name/
|-- SKILL.md                 # Required instructions and YAML frontmatter
|-- agents/openai.yaml       # Optional Codex UI and invocation metadata
|-- scripts/                 # Repeatable deterministic helpers
|-- references/              # Detail loaded only on relevant branches
`-- assets/                  # Templates or files used in generated output
```

Create optional directories only when they have a real caller. Keep shared
purpose and constraints in `SKILL.md`; move substantial branch-specific detail
behind an explicit pointer to `references/`.

## Invocation

- Model-invoked skills are discoverable from a precise frontmatter description.
- Explicit-only skills set `policy.allow_implicit_invocation: false` in
  `agents/openai.yaml` and rely on the person to invoke them.
- When explicit-only skills become hard to remember, add a small explicit-only
  router skill that explains which one fits each situation.

Descriptions are context pointers. Name what the skill does and the distinct
conditions that should activate it; avoid broad catch-all wording.
