# Document roles

Read this guide after classifying a document when its role affects whether a claim should be rewritten, preserved, or linked.

## Current references

README files, architecture guides, runbooks, and user-facing technical references should describe supported present behavior. Replace stale claims when current evidence is sufficient. When evidence conflicts, state the uncertainty near the claim and identify the next useful source or owner rather than guessing.

## Plans and proposals

Plans record an intended path at a particular time. Keep their original scope, assumptions, and alternatives legible. Add a short outcome or status note that says what was implemented, deferred, abandoned, or superseded, with links to the relevant implementation, decision, or follow-up plan. Do not recast an old plan as if it described the current system.

## Decisions and ADRs

Decisions preserve the reasoning for a choice. Correct factual errors that obstruct reading, but retain the decision and its historical rationale. If the decision no longer governs the system, record its successor or deprecation according to the repository's conventions. A changed implementation alone does not establish that the decision was reversed.

## Investigations, bug reports, and incident records

Preserve observed symptoms, environment, timeline, diagnosis, mitigation, and lessons. Add later evidence that confirms, refines, or disputes the finding. Link the fix, regression, or follow-up investigation. Keep time-bound statements time-bound rather than upgrading them to a general claim.

## Agent and developer instructions

Instructions carry rules, ownership boundaries, and workflow expectations. Reconcile factual context that is directly supported by the repository, while preserving policy and authority boundaries. Ask before changing a behavioral rule, approval requirement, or developer workflow unless the user has specifically requested that policy change.

## Cross-document relationships

Use relative links when they resolve a reader's next question. Name the relationship in the surrounding text and link to the specific section when practical. Prefer a small number of maintained links over a broad, speculative graph. If related documents make incompatible claims, preserve both records and describe the conflict or the evidence that establishes a successor.
