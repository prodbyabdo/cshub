# Agent 1 Prompt: Links, Routing, Site Inventory

You are Agent 1 for the CS Hub deep audit.

## Scope
Audit public site routing, links, page inventory, missing files, missing assets, empty/stub pages, unsafe external links, and navigation consistency.

Public scope includes root public HTML pages, subject pages, `resources.html`, `cs-wiki.html`, and `wiki/**`.

Exclude `.git`, `node_modules`, `.tmp`, `scratch`, `contentforwiki`, `temp_chat_*`, and unrelated/generated artifacts unless publicly linked.

## Output
Do not edit production files. Return structured findings to the coordinator. Use this format:

```md
## Agent 1 Results

### Inventory Summary
- ...

### Findings

#### A1-###
- Severity:
- Category: Links / Routing / Assets
- Location:
- Evidence:
- Impact:
- Recommendation:
- Verification:
- Status: open
```

## Checks
- Canonical public page inventory.
- Local `href`, `src`, stylesheet, script, favicon, image, and asset validation.
- Broken or missing targets.
- Empty or 0-byte public pages.
- Stub pages that claim "Coming Soon".
- `target="_blank"` links missing `rel="noopener noreferrer"`.
- Links to `#` used as disabled or fake navigation.
- Public pages that link to excluded/generated/scratch files.

## Suggested Commands
- `rg --files -g "*.html" -g "*.css" -g "*.js"`
- Search for `href=`, `src=`, `target="_blank"`, `href="#"`.
- Use PowerShell `Test-Path` for local target validation.

Before finishing, deduplicate link/asset findings and include line numbers.
