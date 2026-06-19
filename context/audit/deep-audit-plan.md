# 4-Agent Deep Public Site Audit Plan

## Summary
Run a static and manual deep audit of the public CS Hub site only. Exclude `.git`, `node_modules`, `.tmp`, `scratch`, `contentforwiki`, `temp_chat_*`, and unrelated/generated artifacts unless they are directly linked from public pages.

Coordination files:
- `context/audit/deep-audit-progress.md`
- `context/audit/deep-audit-errors.md`

Agent prompt files:
- `context/audit/agent-1-links-routing-prompt.md`
- `context/audit/agent-2-accessibility-prompt.md`
- `context/audit/agent-3-responsive-performance-prompt.md`
- `context/audit/agent-4-theming-consistency-prompt.md`

## Agent Split
- Agent 1: Links, routing, public page inventory, missing files, missing assets, stubs, unsafe external links.
- Agent 2: Accessibility, semantics, keyboard support, labels, alt text, ARIA, focus, disabled controls.
- Agent 3: Responsive layout, mobile overflow, performance, heavy assets, blocking scripts, MathJax, repeated inline CSS/JS.
- Agent 4: Theming, design consistency, anti-patterns, content structure drift, hard-coded colors, inline style sprawl.

## Shared Rules
- Audit only public site files: root public HTML pages, subject pages, `resources.html`, `cs-wiki.html`, and `wiki/**`.
- Do not edit production HTML/CSS/JS during the audit.
- Use severity labels: `P0 Blocking`, `P1 Major`, `P2 Minor`, `P3 Polish`.
- Include file path and line number for every finding.
- Deduplicate findings before reporting.
- Mark uncertain findings as `needs confirm`, not as facts.

## Execution Flow
1. Agent 1 builds the public-page inventory so the audit scope is explicit.
2. Agents 1-4 audit in parallel across their assigned dimensions.
3. Consolidate returned findings into `deep-audit-errors.md`.
4. Update coverage and completion status in `deep-audit-progress.md`.
5. Produce a final score table, top P0/P1 findings, systemic patterns, positive findings, and prioritized next actions.

## Verification Plan
- Static local link and asset checks for public pages.
- Static accessibility checks for missing `alt`, non-semantic controls, unlabeled inputs, missing focus states, and absent tab ARIA.
- Static responsive checks for `100vh`, `overflow:hidden`, fixed widths, missing mobile constraints, and horizontal overflow risks.
- Static performance checks for large remote image grids, MathJax/script loading, missing lazy loading, duplicated inline CSS/JS, and missing shared assets.
- Manual consistency review across sibling subject pages and main navigation flows.

## Assumptions
- Scope is public site only.
- Depth is static + manual.
- Audit files live under `context/audit/`.
- This audit does not implement fixes.
