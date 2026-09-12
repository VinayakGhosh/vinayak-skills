# Onboarding

Use this mode when the developer is new to the repository or lacks a trustworthy system map.

## Outcome

The developer can explain the repository's purpose, name its major pieces, trace one important journey, and choose a useful next topic. File coverage is not the goal.

## Orientation ladder

Move from context toward implementation:

1. **Purpose:** What real problem does the repository solve?
2. **Actors:** Which people or systems interact with it?
3. **Major pieces:** Which applications, services, packages, jobs, or stores carry distinct responsibilities?
4. **Journeys:** What are the one to three most important input-to-output flows?
5. **Concepts:** Which domain ideas make those journeys work?
6. **Code:** Which small anchors implement the selected concept?
7. **Tests:** Which behaviors and important rules do they protect?

Before presenting the orientation, inspect the README, architecture documentation, manifests, top-level structure, entry points, and representative tests. Validate documentation against implementation where practical.

Start with purpose, a compact system map, an ordered learning path, and the evidence status of any uncertain claim. Use the orientation ladder as the roadmap and follow the [shared mentor loop](../SKILL.md#mentor-loop). Move one rung at a time in a guided session; a concise overview may combine early rungs when the user asked for a quick answer.

Order topics for learning value: product purpose and vocabulary, the main successful flow, data and boundaries, important failure or security rules, secondary behavior, then operations and deployment. Change the order when the user's immediate task requires a different foundation.
