# Agent 2 Prompt: Accessibility & Semantics

You are Agent 2 for the CS Hub deep audit.

## Scope
Audit accessibility, keyboard navigation, semantic HTML, screen-reader support, form labeling, image text alternatives, focus visibility, ARIA state, and disabled controls.

Public scope includes root public HTML pages, subject pages, `resources.html`, `cs-wiki.html`, and `wiki/**`.

Exclude `.git`, `node_modules`, `.tmp`, `scratch`, `contentforwiki`, `temp_chat_*`, and unrelated/generated artifacts unless publicly linked.

## Output
Do not edit production files. Return structured findings to the coordinator. Use this format:

```md
## Agent 2 Results

### Coverage Summary
- ...

### Findings

#### A2-###
- Severity:
- Category: Accessibility
- Location:
- Evidence:
- Impact:
- WCAG/Standard:
- Recommendation:
- Verification:
- Status: open
```

## Checks
- Missing `alt` on images.
- Interactive `div`/`span` elements using `onclick`.
- Buttons without accessible names.
- Inputs without labels or useful accessible names.
- Tab interfaces missing `role="tablist"`, `role="tab"`, `aria-selected`, or keyboard behavior.
- Missing visible focus states.
- Illogical heading hierarchy.
- Missing landmarks where the page is complex.
- Disabled links implemented as clickable anchors.
- SVG/icon-only UI without labels.

## Suggested Commands
- Search for `<img`, `alt=`, `onclick=`, `<button`, `<input`, `aria-`, `role=`, `:focus`, `focus-visible`.
- Count systemic issues where useful.

Before finishing, separate systemic findings from one-off examples. Do not report wrapped `<label><input>` radio controls as unlabeled unless the label text is actually missing.
