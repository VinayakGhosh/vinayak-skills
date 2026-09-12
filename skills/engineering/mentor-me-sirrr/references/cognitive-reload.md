# Cognitive Reload

Use this mode when the developer wants to understand changes that have already happened or rebuild a previously held mental model.

## Establish the change range

Identify and state the comparison being reviewed. It may be:

- uncommitted or staged changes against the current base;
- one commit or a commit range;
- a branch compared with its merge base;
- a pull request;
- changes since a date or prior learning session;
- a user-provided change description when repository evidence is unavailable.

Use Git and repository evidence without modifying the checkout. Ask one focused question when multiple plausible baselines would produce meaningfully different reloads. Separate observed changes from claims in commit messages or descriptions.

## Reload ladder

Scale the ladder to the change:

1. **Before and after:** What behavior changed, in everyday language?
2. **Reason:** What problem does the new behavior solve? Mark historical motivation as inferred unless evidence supports it.
3. **System position:** Which actors, components, or boundaries participate?
4. **Flow:** How does data or control travel through the changed path?
5. **Consequences:** Which users, callers, stored data, operations, or failure paths are affected?
6. **Implementation:** Which focused code anchors carry the change?
7. **Verification:** Which tests or checks support the claimed behavior, and what remains unverified?
8. **Judgment:** For large changes, what trade-offs and likely failure modes should the developer understand?

Begin with a change map rather than a file-by-file diff recital. Group edits by behavior or responsibility. A renamed helper and its test usually belong to one concept; unrelated changes remain separate topics.

For a guided reload, use the reload ladder as the roadmap and follow the [shared mentor loop](../SKILL.md#mentor-loop). Mark the reload complete when the requested changed behavior and relevant code or test anchors have been explored, then follow the [shared closing guidance](../SKILL.md#finish-or-pause).
