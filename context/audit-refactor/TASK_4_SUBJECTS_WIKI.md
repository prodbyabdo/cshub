# Task 4 — Subject Content Pages & Wiki

**Agent scope**: 10 subject HTML files + CS Wiki + wiki subpages
**Branch**: `audit-refactor`
**Dependencies**: `assets/css/global.css`, `assets/js/deeplink.js`, `assets/js/tabs.js` (read-only)

> [!CAUTION]
> Do NOT touch any file outside your scope. Other agents own other files.

---

## Files Owned

### Subject Content Pages (8 active + 2 preview)
```
year1sem1compapp.html          — Computer Applications
year1sem1introcs.html          — Introduction to Computer Science
year1sem2compmain.html         — Computer Maintenance
year1sem2english.html          — English for Specific Purpose
year1sem2filemgmt.html         — File Management
year1sem2introdbms.html        — Introduction to Databases
year1sem2introprog.html        — Principles of Programming (largest: ~3000 lines)
year1sem2programmingjava.html  — Programming with Java
year1sem2introprog_preview.html — Preview version (may be stale)
year1-preview.html             — Preview version (may be stale)
```

### Wiki Pages
```
cs-wiki.html                   — Wiki article (Computer)
wiki/wiki.css                  — Wiki shared stylesheet
wiki/programming.html          — Programming category page
wiki/*.html                    — All auto-generated wiki pages
```

---

## Checklist

### 4.1 — Link Shared Assets (all subject pages)
For each subject page:
- [ ] Add `<link rel="stylesheet" href="assets/css/global.css">` in `<head>` BEFORE inline `<style>`
- [ ] Add `<link rel="icon" href="assets/online.png" type="image/png">`
- [ ] Add `<meta name="description" content="...">` — use subject-specific text:
  - `year1sem2introprog.html`: `"Principles of Programming — COM126 course summary, Java tutorials, practice exams, and an embedded compiler."`
  - `year1sem2introdbms.html`: `"Introduction to Databases — DBMS course summary, exam practice, and answer sheets."`
  - `year1sem2english.html`: `"English for Specific Purpose II — Course resources and materials."`
  - `year1sem2compmain.html`: `"Computer Maintenance — Hardware-focused course materials."`
  - `year1sem2filemgmt.html`: `"File Management — Course resources and study materials."`
  - `year1sem2programmingjava.html`: `"Programming with Java — Advanced Java course resources."`
  - `year1sem1compapp.html`: `"Computer Applications — COM-111 course resources."`
  - `year1sem1introcs.html`: `"Introduction to Computer Science — COM115 course materials and tutorials."`
- [ ] Replace inline deep-linking `<script>` with: `<script src="assets/js/deeplink.js" defer></script>`
- [ ] Replace inline `openTab()` / `printFullPdf()` / `printCurrentTab()` with: `<script src="assets/js/tabs.js"></script>`

### 4.2 — CSS Deduplication (all subject pages)
Remove from each file's `<style>` block (now in `global.css`):
- [ ] `:root { ... }` — REMOVE entirely
- [ ] `* { box-sizing }` — REMOVE
- [ ] `body { ... }` base styles — REMOVE (keep page-specific overrides)
- [ ] `.container` — REMOVE if matches global
- [ ] `.nav-back` / `.nav-back:hover` — REMOVE
- [ ] `header` — REMOVE if matches global
- [ ] `h1`, `h2`, `h3`, `h4`, `.subtitle` — REMOVE if matches global
- [ ] `.section-title` — REMOVE
- [ ] `.tabs`, `.tab-btn`, `.tab-content` — REMOVE
- [ ] `@keyframes fadeIn` — REMOVE
- [ ] `.card`, `.card-title`, `.blue-glow`, `.red-glow`, `.green-glow`, `.gold-glow`, `.purple-glow` — REMOVE
- [ ] `.dot`, `.dot-*` — REMOVE
- [ ] `.def` — REMOVE
- [ ] `.clean`, `.clean li`, `.clean li::before` — REMOVE
- [ ] `.grid-2`, `.grid-3` — REMOVE
- [ ] `.sheet` table styles — REMOVE
- [ ] `.print-btn`, `.header-actions`, `.tab-print-actions` — REMOVE
- [ ] `code`, `pre` styles — REMOVE
- [ ] `.question-card`, `.question-text`, `.options` — REMOVE
- [ ] `.yt-link`, `.yt-icon` — REMOVE
- [ ] `.lang-block` — REMOVE
- [ ] `.study-*` classes — REMOVE (all in global)
- [ ] Print `@media print` rules — REMOVE base rules; keep page-specific tab-print logic

**KEEP as page-specific**:
- Answer grid / exam-specific layout (`.answer-grid`, `.answer-table`)
- Java compiler iframe styles
- Any page-unique interactive components

### 4.3 — Accessibility Fixes

#### `year1sem2introprog.html` (largest, most complex):
- [ ] Tab buttons already use `<button>` — good. Add `role="tablist"` to `.tabs` container
- [ ] Add `role="tab"` to each `.tab-btn`
- [ ] Add `role="tabpanel"` to each `.tab-content`
- [ ] Java Compiler iframe: add `title="Java Compiler — JDoodle"` or equivalent
- [ ] Any `<table>` elements: wrap in `<div class="table-wrap">` for mobile overflow
- [ ] Ensure all heading hierarchy is correct (single `<h1>`, then `<h2>`, etc.)

#### `year1sem2introdbms.html`:
- [ ] Same tab/ARIA fixes as introprog
- [ ] Check `aria-label` attribute usage (this was the only file with existing ARIA — verify it's correct)
- [ ] Wrap tables in `.table-wrap`

#### All subject pages:
- [ ] Ensure every `<iframe>` has a `title` attribute
- [ ] Ensure `<img>` tags have `alt` text (may not have many images)
- [ ] Search input fields: add `aria-label` if no visible `<label>`
- [ ] Interactive `<div>` elements → convert to `<button>` or add `role="button" tabindex="0"`

### 4.4 — Wiki Pages

#### `cs-wiki.html`:
- [ ] This page has its OWN full `<style>` block duplicating wiki tokens. Replace the `:root` and base styles with a link to `global.css`
- [ ] Add `<link rel="stylesheet" href="assets/css/global.css">` in `<head>`
- [ ] Add `<link rel="icon" href="assets/online.png" type="image/png">`
- [ ] Add `<meta name="description" content="Computer — CS Wiki article covering the history, types, and components of computers.">`
- [ ] Remove inline deep-linking script, add `<script src="assets/js/deeplink.js" defer></script>`
- [ ] Fix `line-height: 1.7` → standardize to `1.6` (matches global)
- [ ] Keep wiki-specific CSS (infobox, TOC, wiki-header, etc.) inline or move to `wiki/wiki.css`

#### `wiki/wiki.css`:
- [ ] Update `:root` tokens to match global (accent `#00ff88`, etc.) — verify they already do
- [ ] Remove any rules that are now in `global.css` (`.nav-back`, base `body` styles, etc.)
- [ ] Keep wiki-specific: `.stub-section`, `.link-grid`, `.link-card`, header gradient styles

#### `wiki/*.html` (auto-generated pages):
- [ ] These are generated by `fetch_wiki.py` — do NOT manually edit them
- [ ] Instead, note any issues that need to be fixed in the Python script (for later)
- [ ] Verify they link to `wiki/wiki.css` (they should already)

### 4.5 — Table Overflow Fix
The audit identified tables with `min-width: 620px` causing horizontal scroll on mobile:
- [ ] In `year1sem2introprog.html`: find `.answer-table` or tables with `min-width` and wrap in `<div class="table-wrap">`
- [ ] In `year1sem2introdbms.html`: same treatment for `.sheet` tables
- [ ] Remove any `min-width` on tables where possible (let them shrink naturally)

### 4.6 — Preview Files
- [ ] `year1sem2introprog_preview.html` and `year1-preview.html` — check if these are stale/unused
- [ ] If stale: leave them alone (don't delete on a refactor branch, just note in progress)
- [ ] If active: apply the same treatment as their parent files

### 4.7 — Verify
- [ ] Open `year1sem2introprog.html` — all 5 tabs work, print buttons work, Java compiler loads
- [ ] Open `year1sem2introdbms.html` — tabs work, tables don't overflow on mobile
- [ ] Open `cs-wiki.html` — infobox renders, article content displays
- [ ] Open a wiki subpage (e.g., `wiki/programming.html`) — link grid renders
- [ ] Check mobile (375px) on introprog — tabs wrap, tables scroll, content readable
- [ ] Print introprog "Course Summary" tab — clean print output

---

## File Ownership
```
OWNS:
  year1sem1compapp.html
  year1sem1introcs.html
  year1sem2compmain.html
  year1sem2english.html
  year1sem2filemgmt.html
  year1sem2introdbms.html
  year1sem2introprog.html
  year1sem2programmingjava.html
  year1sem2introprog_preview.html
  year1-preview.html
  cs-wiki.html
  wiki/wiki.css
  wiki/programming.html
  wiki/*.html (read-only — auto-generated, note issues only)

DO NOT TOUCH:
  index.html, year1-4.html (Agent 1)
  resources.html (Agent 2)
  year1sem*calc*.html, unit_circle_trig.html (Agent 3)
  assets/** (foundation — read-only)
```
