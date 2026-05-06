# Task 3 — Calculus Pages

**Agent scope**: 19 calculus HTML files + `unit_circle_trig.html` + `assets/css/math-style.css`
**Branch**: `audit-refactor`
**Dependencies**: `assets/css/global.css`, `assets/js/deeplink.js`, `assets/js/tabs.js` (read-only)

> [!CAUTION]
> Do NOT touch any file outside your scope. Other agents own other files.

---

## Files Owned (20 files)

```
year1sem1calclaws.html
year1sem1calcsolutions.html
year1sem2calc2.html            ← Calc 2 index/hub
year1sem2calc2lec1.html
year1sem2calc2lec1sol.html
year1sem2calc2lec2.html
year1sem2calc2lec2sol.html
year1sem2calc2lec3.html
year1sem2calc2lec3sol.html
year1sem2calc2lec4.html
year1sem2calc2lec4sol.html
year1sem2calc2lec5.html
year1sem2calc2lec5sol.html
year1sem2calc2lec6.html
year1sem2calc2lec6sol.html
year1sem2calc2lec7.html
year1sem2calc2lec7sol.html
year1sem2calc2lec8.html
year1sem2calc2lec8sol.html
unit_circle_trig.html
```

**May also create**: `assets/css/math-style.css` (if extracting math-specific shared CSS)

---

## Checklist

### 3.1 — Create `assets/css/math-style.css`
Extract shared math/calc-specific CSS from the lecture pages into a new shared file. These pages share:
- [ ] Desktop sidebar layout (`.desktop-sidebar`, `.content-with-sidebar`, grid layout)
- [ ] `.formula-box`, `.theorem`, `.important` blocks
- [ ] MathJax container overrides
- [ ] Solution-linking styles (`.solution-link-card`)
- [ ] PDF download link styles (`.pdf-download`)
- [ ] Day/section navigator styles
- [ ] Lecture-specific `.card` extensions

Study 2-3 lecture files to identify the exact shared patterns, then extract.

### 3.2 — Link Shared Assets (all 20 files)
For each file:
- [ ] Add `<link rel="stylesheet" href="assets/css/global.css">` in `<head>`
- [ ] Add `<link rel="stylesheet" href="assets/css/math-style.css">` in `<head>` (after global)
- [ ] Add `<link rel="icon" href="assets/online.png" type="image/png">`
- [ ] Add `<meta name="description" content="...">` (use subject-specific text):
  - Lecture pages: `"Calculus 2 — Lecture N notes, formulas, and worked examples for CS & IT students."`
  - Solution pages: `"Calculus 2 — Lecture N solutions and worked problems."`
  - `year1sem2calc2.html`: `"Calculus 2 course hub — All lectures, solutions, and formula sheets."`
  - `year1sem1calclaws.html`: `"Calculus 1 — Laws, rules, and formula reference sheet."`
  - `year1sem1calcsolutions.html`: `"Calculus 1 — Exam solutions and worked problems."`
  - `unit_circle_trig.html`: `"Unit circle and trigonometry reference — visual guide."`
- [ ] Replace inline deep-linking script with: `<script src="assets/js/deeplink.js" defer></script>`
- [ ] For files that have `openTab()` / `printFullPdf()` / `printCurrentTab()` functions defined inline, replace with: `<script src="assets/js/tabs.js"></script>` (loaded BEFORE page-specific scripts)

### 3.3 — CSS Deduplication (all 20 files)
From each file's `<style>` block, REMOVE rules now covered by `global.css`:
- [ ] `:root { ... }` — REMOVE
- [ ] `* { box-sizing }` — REMOVE
- [ ] `body { ... }` base styles — REMOVE (keep page-specific overrides like padding-bottom for sidebar layout)
- [ ] `.container` — REMOVE if matches global; keep if has different max-width or padding
- [ ] `.nav-back` / `.nav-back:hover` — REMOVE
- [ ] `h1`, `.subtitle` — REMOVE if matches global; keep if has page-specific sizing
- [ ] `h2`, `h3`, `h4` — REMOVE
- [ ] `.tabs`, `.tab-btn`, `.tab-content` — REMOVE
- [ ] `@keyframes fadeIn` — REMOVE
- [ ] `.card`, `.card-title` — REMOVE base; keep glow variants if not in global
- [ ] `.dot`, `.dot-*` — REMOVE
- [ ] `.def` — REMOVE
- [ ] `.section-title` — REMOVE
- [ ] `.print-btn`, `.header-actions`, `.tab-print-actions` — REMOVE
- [ ] `.sheet` table styles — REMOVE
- [ ] `code`, `pre` — REMOVE
- [ ] Print `@media print` rules — REMOVE base; keep page-specific tab printing rules

**KEEP as page-specific**:
- Desktop sidebar layout (until moved to `math-style.css`)
- Formula/theorem boxes (until moved to `math-style.css`)
- MathJax-specific overrides
- Any page-unique layout rules

### 3.4 — Accessibility Fixes (all 20 files)

#### Semantic HTML:
- [ ] Ensure all `<img>` tags have `alt` text (check for PDF preview images, MathJax screenshots, etc.)
- [ ] If any `<div>` elements are used as buttons (e.g., `<div onclick="...">`) → change to `<button>`
- [ ] Sidebar navigation links should use `<nav>` wrapper with `aria-label="Lecture navigation"`

#### Tables:
- [ ] Wrap any `<table>` elements in `<div class="table-wrap">` for mobile overflow handling (the `.table-wrap` class is in global.css)
- [ ] Ensure tables have `<thead>` with proper `<th>` elements

#### PDF iframes:
- [ ] Any `<iframe>` embedding PDFs should have a `title` attribute: `title="PDF: Lecture N slides"`
- [ ] Ensure the mobile PDF download link fallback exists (from previous work sessions)

### 3.5 — Navigation Consistency
- [ ] Verify all "Back to" links point to the correct parent page:
  - Lecture/solution pages → `year1sem2calc2.html`
  - `year1sem2calc2.html` → `year1.html`
  - `year1sem1calclaws.html` → `year1.html`
  - `year1sem1calcsolutions.html` → `year1.html`
  - `unit_circle_trig.html` → `year1sem2calc2.html` or `year1.html`
- [ ] Verify all solution-link cards from lectures point to the correct `*sol.html` file
- [ ] Verify all "Back to Lectures" links from solutions point to the correct `*lecN.html` file

### 3.6 — Verify
- [ ] Open `year1sem2calc2.html` (hub page) — all lecture links work
- [ ] Open 2-3 lecture pages — tabs work, MathJax renders, sidebar nav works
- [ ] Open a solution page — verify formulas render
- [ ] Check mobile (375px) — sidebar collapses, content readable
- [ ] Print a lecture page — verify print CSS works

---

## File Ownership
```
OWNS:
  year1sem1calclaws.html
  year1sem1calcsolutions.html
  year1sem2calc2.html
  year1sem2calc2lec1.html through year1sem2calc2lec8.html
  year1sem2calc2lec1sol.html through year1sem2calc2lec8sol.html
  unit_circle_trig.html
  assets/css/math-style.css (NEW — may create)

DO NOT TOUCH:
  index.html, year1-4.html (Agent 1)
  resources.html (Agent 2)
  introprog, introdbms, english, etc. (Agent 4)
  assets/css/global.css, assets/js/* (foundation — read-only)
```
