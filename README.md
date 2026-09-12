# Vinayak Skills

Reusable agent skills for learning codebases, understanding software changes,
and working with coding agents more effectively. The repository uses the open
`SKILL.md` format and can be installed with the
[Skills CLI](https://github.com/vercel-labs/skills) for compatible agents such
as Codex, Claude Code, Cursor, and OpenCode.

Install the available skills into the current project:

```bash
npx skills@latest add VinayakGhosh/vinayak-skills
```

## Included skills

### Mentor Me Sirrr

Patient, junior-friendly codebase mentoring that explains what code does, why
it exists, where it fits in the wider system, and how its behavior is verified.
It supports repository onboarding, implementation mentoring, system deep dives,
and cognitive reloads. Longer learning sessions follow a focused, evidence-led
roadmap and can include optional teach-backs or visuals where they clarify a
relationship.

### Docs Reconcile

Evidence-led maintenance for repository Markdown that has drifted from the
codebase. It refreshes current references, preserves plans and investigations
as historical records, identifies contradictions between documentation and
implementation, and links related context with clear status.

## Install options

Install a specific skill into the current project:

```bash
npx skills@latest add VinayakGhosh/vinayak-skills \
  --skill mentor-me-sirrr
```

Replace `mentor-me-sirrr` with `docs-reconcile` to install Docs Reconcile.

Install globally for the current user:

```bash
npx skills@latest add VinayakGhosh/vinayak-skills \
  --skill mentor-me-sirrr \
  --global
```

Install all available skills globally for Codex:

```bash
npx skills@latest add VinayakGhosh/vinayak-skills \
  --agent codex \
  --global
```

List the repository's available skills without installing:

```bash
npx skills@latest add VinayakGhosh/vinayak-skills --list
```

## Usage

### Repository onboarding

```text
Use mentor-me-sirrr to onboard me to this repository. Start with what the
system does and how its major pieces work together, then let me choose where
to go deeper.
```

### Learn while making a change

```text
Use mentor-me-sirrr while implementing this change. Explain the important
decisions in junior-friendly language and connect them to the wider system.
```

### System deep dive

```text
Use mentor-me-sirrr to explain how authentication works in this repository.
Show me the main flow, relevant code, tests, and likely failure points.
```

### Cognitive reload

```text
Use mentor-me-sirrr to give me a cognitive reload of the changes on this
branch compared with main. Explain what changed, why, how the flow works now,
and what the tests prove.
```

### Optional teach-back

```text
Use mentor-me-sirrr to test my understanding of the component we just
explored. Ask one question at a time and help me correct any gaps.
```

### Documentation reconciliation

```text
Use docs-reconcile to review the repository's planning and architecture
Markdown after this branch. Update evidence-backed current context, preserve
historical findings, and report any contradictions that need a code decision.
```

## Privacy and permissions

Mentor Me Sirrr keeps learning progress in the current conversation by
default. Persistent progress is optional and requires the user to approve both
the write and its location.

Repository exploration remains read-only for onboarding, reviews, and
explanations. The skill edits product code only when the user explicitly asks
for implementation or modification. Private repository details must not be
sent to a public diagram renderer without explicit permission.

## Repository layout

```text
skills/
  engineering/
    mentor-me-sirrr/
    docs-reconcile/
scripts/
  new_skill.py
  validate_skills.py
LICENSE
```

Installable skills live at `skills/<category>/<skill-name>`. Each skill keeps
its shared behavior in `SKILL.md` and places conditional detail in focused
references.

## Authoring and validation

Create a skill in one of the maintained categories:

```bash
python scripts/new_skill.py my-skill --category engineering
python scripts/new_skill.py my-skill --category productivity
```

After editing a skill, validate the repository:

```bash
python scripts/validate_skills.py
```

See [`skills/README.md`](skills/README.md) for the repository's skill structure
and invocation guidance.

## Update installed skills

Update Mentor Me Sirrr:

```bash
npx skills@latest update mentor-me-sirrr --global
```

Update Docs Reconcile:

```bash
npx skills@latest update docs-reconcile --global
```

You can also reinstall a specific skill from this repository:

```bash
npx skills@latest add VinayakGhosh/vinayak-skills \
  --skill <skill-name> \
  --global
```

Replace `<skill-name>` with `mentor-me-sirrr` or `docs-reconcile`.

## Acknowledgements

Mentor Me Sirrr adapts teaching and cognitive-reload ideas from
[`TheMovingTargets/agent-skills`](https://github.com/TheMovingTargets/agent-skills).
The applicable upstream MIT notice is preserved in the Mentor Me Sirrr skill's
[`LICENSE`](skills/engineering/mentor-me-sirrr/LICENSE).

## License

This repository is licensed under the [MIT License](LICENSE).
