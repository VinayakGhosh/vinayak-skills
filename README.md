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

Patient, junior-friendly codebase mentoring that explains not only what code
does, but why it exists, where it fits in the wider system, and how the behavior
is verified.

Use it for:

- onboarding to an unfamiliar repository;
- learning while implementing a requested change;
- understanding a component, workflow, or architecture decision;
- taking a cognitive reload of completed changes;
- translating technical jargon into plain language without hiding the correct
  terminology;
- optional teach-backs and longer learning paths;
- charts, mind maps, and flow diagrams when relationships are easier to learn
  visually.

The skill adapts its depth to the task. Small changes receive a compact
explanation, while larger changes include system context, data or control flow,
trade-offs, failure behavior, code anchors, and tests.

Install only Mentor Me Sirrr:

```bash
npx skills@latest add VinayakGhosh/vinayak-skills \
  --skill mentor-me-sirrr
```

## Install options

Install into the current project:

```bash
npx skills@latest add VinayakGhosh/vinayak-skills \
  --skill mentor-me-sirrr
```

Install globally for the current user:

```bash
npx skills@latest add VinayakGhosh/vinayak-skills \
  --skill mentor-me-sirrr \
  --global
```

Install globally for Codex:

```bash
npx skills@latest add VinayakGhosh/vinayak-skills \
  --skill mentor-me-sirrr \
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
      SKILL.md
      LICENSE
      agents/
        openai.yaml
      references/
  productivity/
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

Update an installed copy:

```bash
npx skills@latest update mentor-me-sirrr --global
```

You can also reinstall it from this repository:

```bash
npx skills@latest add VinayakGhosh/vinayak-skills \
  --skill mentor-me-sirrr \
  --global
```

## Acknowledgements

Mentor Me Sirrr adapts teaching and cognitive-reload ideas from
[`TheMovingTargets/agent-skills`](https://github.com/TheMovingTargets/agent-skills).
The applicable upstream MIT notice is preserved in the skill's
[`LICENSE`](skills/engineering/mentor-me-sirrr/LICENSE).

## License

This repository is licensed under the [MIT License](LICENSE).
