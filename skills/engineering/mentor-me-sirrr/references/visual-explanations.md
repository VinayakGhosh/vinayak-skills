# Visual Explanations

Use a visual when it reduces the effort needed to understand three or more relationships, a branching decision, state changes, or an ordered interaction. A two-part fact usually needs only prose.

## Choose the smallest useful form

| Need | Preferred form |
| --- | --- |
| Repository areas or concept hierarchy | Mind map or tree |
| Runtime pieces and dependencies | Flow diagram |
| Request, event, or call order | Sequence diagram |
| Lifecycle or allowed transitions | State diagram |
| Decision logic | Flowchart |
| Exact mappings or comparisons | Table |

Use the best format supported by the current environment. Mermaid or a compact text diagram is sufficient when a rendered visualization is unavailable. Never send private repository details to a public rendering service without explicit permission.

## Keep it teachable

- Show one concept per visual and normally use four to six nodes.
- Put domain concepts in labels before filenames.
- Keep labels short and explain the important relationships in prose.
- Show the successful path first; add failure branches only when they are the lesson.
- After the concept is understood, map nodes to relevant files, functions, and tests.
- Include only relationships supported by repository evidence and label meaningful inference.

If the learner remains confused, redraw the smallest relevant relationship instead of adding a larger diagram. The prose explanation must still communicate the core idea when the visual cannot render.
