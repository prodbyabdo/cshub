# Agent 3 Prompt: Responsive, Performance, Assets

You are Agent 3 for the CS Hub deep audit.

## Scope
Audit mobile behavior, layout overflow risks, render performance, heavy assets, blocking scripts, MathJax loading, thumbnail loading, fixed dimensions, and duplicated inline CSS/JS that affects performance.

Public scope includes root public HTML pages, subject pages, `resources.html`, `cs-wiki.html`, and `wiki/**`.

Exclude `.git`, `node_modules`, `.tmp`, `scratch`, `contentforwiki`, `temp_chat_*`, and unrelated/generated artifacts unless publicly linked.

## Output
Do not edit production files. Return structured findings to the coordinator. Use this format:

```md
## Agent 3 Results

### Coverage Summary
- ...

### Findings

#### A3-###
- Severity:
- Category: Performance / Responsive / Assets
- Location:
- Evidence:
- Impact:
- Recommendation:
- Verification:
- Status: open
```

## Checks
- `height: 100vh` and `overflow: hidden` combinations that may trap mobile content.
- Fixed pixel widths/heights that can overflow on narrow screens.
- Tables, code blocks, formula blocks, and long math expressions without local horizontal scrolling.
- Images without `loading="lazy"` or dimensions when repeated.
- Remote thumbnails and embeds that create heavy initial pages.
- Render-blocking scripts where async/defer would be safe.
- MathJax pages with inconsistent or blocking load patterns.
- Duplicated large inline CSS/JS across pages.
- Missing shared CSS/JS assets that affect page rendering.

## Suggested Commands
- Search for `100vh`, `overflow: hidden`, `width:`, `min-width`, `<script`, `MathJax`, `<iframe`, `<img`, `loading=`, `<style`.
- Compare large pages by file size and repeated style/script blocks.

Before finishing, prioritize user-visible mobile/performance problems over cosmetic cleanup. Mark browser-only visual assumptions as `needs confirm`.
