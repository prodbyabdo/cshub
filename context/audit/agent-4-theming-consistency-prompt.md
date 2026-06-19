# Agent 4 Prompt: Theming, Consistency, Anti-Patterns, Content Risk

You are Agent 4 for the CS Hub deep audit.

## Scope
Audit theming consistency, design-token use, hard-coded colors, visual drift between sibling pages, AI-slop anti-patterns, inline style sprawl, content structure consistency, and obvious content risk.

Public scope includes root public HTML pages, subject pages, `resources.html`, `cs-wiki.html`, and `wiki/**`.

Exclude `.git`, `node_modules`, `.tmp`, `scratch`, `contentforwiki`, `temp_chat_*`, and unrelated/generated artifacts unless publicly linked.

## Output
Do not edit production files. Return structured findings to the coordinator. Use this format:

```md
## Agent 4 Results

### Coverage Summary
- ...

### Findings

#### A4-###
- Severity:
- Category: Theming / Anti-Pattern / Content
- Location:
- Evidence:
- Impact:
- Recommendation:
- Verification:
- Status: open
```

## Checks
- Missing or inconsistent shared CSS references.
- Hard-coded colors where tokens exist.
- Inline style overuse.
- Inconsistent page structure between sibling subject pages.
- Generic dark-card/neon patterns where they reduce clarity or consistency.
- Gradient text, over-rounded cards, repeated card-grid layouts, decorative clutter.
- Theme drift between Calculus, DBMS, English, Intro Programming, Resources, Wiki.
- Obvious content stubs, mismatched labels, dead placeholders, or pages that promise unavailable material.

## Suggested Commands
- Search for `style="`, hex colors, `linear-gradient`, `border-radius`, `<style`, repeated CSS variables.
- Compare sibling page headers, nav actions, tab structures, and resource links.

Before finishing, do not penalize the project simply for having a dark academic theme. Focus on inconsistency, maintainability, and user-facing clarity.
