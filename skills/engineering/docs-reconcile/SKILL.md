---
name: docs-reconcile
description: Reconcile repository Markdown with current code, tests, configuration, and history when documentation, plans, or investigations may be stale or contradictory.
---

# Docs Reconcile

Bring repository-owned Markdown back into a useful relationship with the codebase. The outcome is durable context: a reader can tell what the system does now, what was intended, what happened before, and which claims still need evidence.

Treat **reconcile** as evidence-led maintenance. Preserve useful history while making current material accurate and navigable.

## Scope and authority

1. Establish the requested document set and the comparison boundary: the working tree, branch, commit, release, issue, or incident that makes the documents stale. For a repository-wide request, inventory repository-owned Markdown and state any excluded areas.
2. Skip generated, vendored, and third-party files unless the request includes them. Follow related documents only when they help resolve or expose a claim within scope.
3. Apply evidence-backed edits within the requested scope. Ask before deleting documents, broadly restructuring documentation, or changing instructions that govern agents or developers.
4. Keep code fixes, test changes, and external verification as separate work unless the user also authorizes them.

## Reconciliation loop

1. **Classify.** Identify each document's role: current reference, plan, decision, investigation, incident record, or agent instruction. Read [references/document-roles.md](references/document-roles.md) when the role changes how it should be maintained.
2. **Trace.** Break relevant statements into claims and gather the smallest useful evidence from implementation, configuration, tests, version history, issue links, and—when needed—deployment evidence. Record the source while working so each material edit remains explainable.
3. **Separate.** Label a claim by what it represents:
   - **Observed implementation:** behavior demonstrated by current code, configuration, or executed checks.
   - **Intended behavior:** an explicit requirement, approved decision, or maintained contract.
   - **Historical finding:** a time-bound plan, diagnosis, incident fact, or past decision.
   - **Unresolved:** a contradiction or gap that needs more evidence.
4. **Reconcile.** Update current-reference documents to match supported current behavior. Preserve plans and investigations as historical records, then add concise status, successor, or follow-up context. Link related documents with a precise relationship such as `implemented by`, `superseded by`, or `follow-up investigation`.
5. **Surface conflicts.** When code, tests, and intended behavior disagree, describe the disagreement with its evidence. A current implementation can be defective; do not silently rewrite an intended contract to match it.
6. **Verify.** Re-read every changed claim against its source, check local links and commands, and run proportionate safe checks when the claim depends on behavior. Say whether a result was inspected or executed.

## Freshness and context

- Follow existing status, ownership, and indexing conventions. Add a compact evidence or status note only where it makes a historical or disputed document easier to use, including relevant source links and an available Git revision.
- Treat “last reviewed” as a record of scope and evidence, not proof that an entire document is current. Mark unreviewed or unresolved material locally.
- Keep durable diagnostic value: symptoms, root cause, failed assumptions, diagnostic steps, decision rationale, and links to later work.
- Use an existing documentation index when one exists. Create a new index only when the requested collection needs one to remain navigable.

## Completion

Finish with a concise reconciliation report that states:

- documents reviewed and changed, plus excluded or unreviewed areas;
- the evidence and checks that support the material updates;
- links or status changes that connect historical and current context; and
- unresolved contradictions, assumptions, and follow-up work.

Persist that report only when the user asks for it or the repository already has a place for such records.
