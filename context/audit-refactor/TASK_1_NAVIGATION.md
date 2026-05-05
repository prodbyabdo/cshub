# Task 1 — Navigation Shell Pages

**Agent scope**: `index.html`, `year1.html`, `year2.html`, `year3.html`, `year4.html`
**Branch**: `audit-refactor`
**Dependencies**: `assets/css/global.css`, `assets/js/deeplink.js` (already created)

> [!CAUTION]
> Do NOT touch any file outside your scope. Other agents own other files.

---

## Checklist

### 1.1 — Link Shared Assets
For each file in scope:
- [ ] Add `<link rel="stylesheet" href="assets/css/global.css">` in `<head>` (BEFORE any `<style>` block)
- [ ] Add `<link rel="icon" href="assets/online.png" type="image/png">` (missing on year pages)
- [ ] Replace the inline deep-linking `<script>` block (the ~45-line IIFE at bottom) with: `<script src="assets/js/deeplink.js" defer></script>`
- [ ] Keep only page-specific CSS in the remaining `<style>` block. Remove any rules that now exist in `global.css`

### 1.2 — CSS Deduplication (per file)

#### `index.html`
The following are in `global.css` and should be REMOVED from inline `<style>`:
- `:root { ... }` block (lines 15-26) — REMOVE entirely
- `body { ... }` — REMOVE (global covers it), BUT keep `min-height: 100vh; display: flex; flex-direction: column;` as page-specific
- `.nav-back` / `.nav-back:hover` — REMOVE
- `h1` — KEEP (this page uses gradient text + 4rem size, different from global)
- `.subtitle` — KEEP (has `text-transform: uppercase; letter-spacing: 2px;` specific to home)
- `footer` — KEEP (page-specific)
- `a.link` — KEEP (page-specific)

**KEEP as page-specific**: `.container` (flex layout), `.grid`, `.card`, `.card-icon`, `.card-title`, `.card-desc`, `footer`, `a.link`, all `@media` blocks. These have index-specific values.

#### `year1.html`
Remove from inline `<style>`:
- `:root { ... }` block — REMOVE
- `* { box-sizing }` — REMOVE (in global)
- `body { ... }` — REMOVE base, keep `min-height: 100vh`
- `.nav-back` / `.nav-back:hover` — REMOVE
- `h1` — KEEP (gradient text, 3.5rem, differs from global)
- `.subtitle` — KEEP (has `letter-spacing: 1px`)
- `@keyframes fadeIn` — REMOVE (in global)

**KEEP as page-specific**: `.view-section`, `.semester-prompts`, `.semester-btn`, `.subjects-header`, `.back-to-semesters`, `.search-box`, `.search-input`, `.grid`, `.subject-card`, `.stretched-link`, `.subject-code`, `.subject-name`, `.card-actions`, `.btn`, `.btn-primary`, `.btn-secondary`, `.btn-disabled`, `.empty-search`

#### `year2.html`, `year3.html`, `year4.html`
These are placeholder pages (~3.4 KB each). Remove:
- `:root` block — REMOVE
- `body`, `.container`, `h1`, `.subtitle`, `.nav-back` — REMOVE (all in global)
- Keep any page-specific content styles

### 1.3 — Accessibility Fixes

#### All 5 files:
- [ ] Add `<meta name="description" content="...">` to `<head>`:
  - `index.html`: `"CS Hub — A student-built study platform for CS & IT undergraduates. Course notes, video tutorials, and a CS wiki."`
  - `year1.html`: `"Year 1 CS & IT curriculum — Semester 1 and 2 subjects including Calculus, Programming, Databases, and more."`
  - `year2-4.html`: `"Year N CS & IT curriculum — Coming soon."`
- [ ] Add `<link rel="icon" href="assets/online.png" type="image/png">` where missing

#### `index.html`:
- [ ] The `<a>` tag on line 199 (inline style, "made by: prodbyabdo") → move inline style to a CSS class `.author-link`
- [ ] Footer link should have `rel="noopener noreferrer"`

#### `year1.html`:
- [ ] Change `<div class="semester-btn" onclick="openSemester('sem1')">` → `<button class="semester-btn" onclick="openSemester('sem1')" type="button">`
  - Do this for BOTH semester buttons (lines 328, 332)
- [ ] Change `<div class="nav-item" ...>` elements → won't apply here (that's resources.html scope)
- [ ] Fix `.nav-back` from `position: absolute` → remove position rule, use normal flow with `margin-bottom`
- [ ] Search input: add `<label>` element (visually hidden) for the search input, or add `aria-label="Search subjects"`
- [ ] Disabled buttons (`<a href="#" class="btn btn-disabled">`) → add `aria-disabled="true"` and `tabindex="-1"`

### 1.4 — Typography / Design Fixes

#### `index.html`:
- [ ] REMOVE gradient text on `h1` (the `background: linear-gradient(...); background-clip: text; -webkit-text-fill-color: transparent;`). Replace with `color: var(--text-primary);`

#### `year1.html`:
- [ ] REMOVE gradient text on `h1` — same fix as index.html
- [ ] Fix `.btn-primary` and `.btn-secondary` — they're currently identical. Make `.btn-secondary` use a lighter style:
  ```css
  .btn-secondary {
      background: rgba(255, 255, 255, 0.05);
      color: var(--text-secondary);
      border-color: var(--border-color);
  }
  ```

### 1.5 — Verify
- [ ] Open each page in browser — visual check, no broken styles
- [ ] Check that tab navigation, search, semester switching all still work
- [ ] Keyboard-tab through year1.html — verify focus indicators appear
- [ ] Check mobile at 375px width — verify layout isn't broken

---

## File Ownership (DO NOT EDIT other files)
```
OWNS:
  index.html
  year1.html
  year2.html
  year3.html
  year4.html

DO NOT TOUCH:
  resources.html (Agent 2)
  year1sem2calc*.html, year1sem1calc*.html, unit_circle*.html (Agent 3)
  year1sem2introprog.html, year1sem2introdbms.html, year1sem2english.html,
  year1sem2programmingjava.html, year1sem2filemgmt.html, year1sem2compmain.html,
  year1sem1compapp.html, year1sem1introcs.html, cs-wiki.html, wiki/** (Agent 4)
  assets/** (foundation — already created, read-only for agents)
```
