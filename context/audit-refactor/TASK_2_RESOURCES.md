# Task 2 — Resources Library

**Agent scope**: `resources.html` (single file, 317 KB, 4732 lines)
**Branch**: `audit-refactor`
**Dependencies**: `assets/css/global.css`, `assets/js/deeplink.js` (already created, read-only)

> [!CAUTION]
> Do NOT touch any file outside your scope. Other agents own other files.

---

## Checklist

### 2.1 — Link Shared Assets
- [ ] Add `<link rel="stylesheet" href="assets/css/global.css">` in `<head>` BEFORE the inline `<style>` block
- [ ] Add `<link rel="icon" href="assets/online.png" type="image/png">` in `<head>`
- [ ] Add `<meta name="description" content="Curated CS video tutorials and resources — categorized by subject for CS & IT students.">`
- [ ] Replace the deep-linking `<script>` IIFE at bottom (lines 4682-4727) with: `<script src="assets/js/deeplink.js" defer></script>`

### 2.2 — Fix Accent Color Mismatch
- [ ] Line 20: Change `--accent-color: #00c288;` → `--accent-color: #00ff88;`
- [ ] Line 21: Change `--accent-dim: rgba(0, 194, 136, 0.08);` → `--accent-dim: rgba(0, 255, 136, 0.1);`

### 2.3 — CSS Deduplication
Remove from inline `<style>` (these are now in `global.css`):
- [ ] `:root { ... }` — REMOVE (but keep `--sidebar-width: 280px;` as page-specific, inline it below body or keep a small `:root` with just that)
- [ ] `* { box-sizing }` — REMOVE
- [ ] `@keyframes fadeIn` — REMOVE

**KEEP as page-specific** (these are unique to resources layout):
- `body` (flex column, 100vh, overflow hidden — specific to this layout)
- `.top-nav`, `.page-title` — page-specific
- `.layout`, `.sidebar`, `.sidebar-group`, `.sidebar-title`, `.nav-item` — page-specific
- `.content`, `.content-section` — page-specific
- `.resource-grid`, `.resource-card`, `.resource-empty` — page-specific
- `.badge`, `.badge-neutral`, `.badge-row`, `.play-btn` — page-specific
- `.resource-thumbnail`, `.play-overlay`, `.resource-info` — page-specific
- `.mobile-*` (menu, drawer, bottom-nav, chips) — page-specific
- All `@media` blocks — page-specific

### 2.4 — Replace Inline Styles with CSS Classes
This is the biggest cleanup. There are ~100 channel links with identical inline styles.

- [ ] The `.channel-link` class already exists in `global.css`. Find all channel link `<a>` tags that have this pattern:
  ```html
  <a href="..." target="_blank"
     style="font-size:0.78rem;color:var(--text-secondary);text-decoration:none;margin-top:8px;display:inline-block;font-family:var(--font-mono);opacity:0.7;transition:opacity 0.2s;"
     onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.7'">
  ```
  Replace with:
  ```html
  <a href="..." target="_blank" rel="noopener noreferrer" class="channel-link">
  ```
  The `onmouseover`/`onmouseout` are replaced by the CSS `:hover` rule in `.channel-link`.

- [ ] Count: There should be roughly 80-100 of these. Use find-and-replace carefully:
  - Search: `style="font-size:0.78rem;color:var(--text-secondary);text-decoration:none;margin-top:8px;display:inline-block;font-family:var(--font-mono);opacity:0.7;transition:opacity 0.2s;" onmouseover="this.style.opacity='1'" onmouseout="this.style.opacity='0.7'"`
  - Replace: `class="channel-link" rel="noopener noreferrer"`

### 2.5 — Accessibility Fixes

#### Semantic HTML:
- [ ] Change `<div class="nav-item" onclick="showSection(...)">` → `<button class="nav-item" type="button" onclick="showSection(...)">`
  - There are 14 of these in the sidebar (lines 612-629)
- [ ] Change the sidebar `<aside class="sidebar">` — add `role="navigation"` and `aria-label="Topic navigation"`
- [ ] Change `<main class="content">` — already `<main>`, good. Add `aria-label="Resource content"`
- [ ] Mobile menu button (line 601): add `aria-label="Open topic menu"` and `aria-expanded="false"`
- [ ] Close drawer button (line 591): add `aria-label="Close menu"`
- [ ] Mobile drawer (line 588): add `aria-hidden="true"` (JS should toggle this when opened/closed)

#### Images — add `alt` text:
- [ ] Every `<img src="https://img.youtube.com/vi/..." loading="lazy">` needs an `alt` attribute
- [ ] Use the video title from the `<h3>` in the same card. Example:
  ```html
  <img src="https://img.youtube.com/vi/NtfbWkxJTHw/mqdefault.jpg" loading="lazy"
       alt="Thumbnail: How to Learn to Code - 8 Hard Truths">
  ```
- [ ] There are roughly 100 images. For each one, copy the `<h3>` text as the alt value prefixed with "Thumbnail: "

### 2.6 — Content Fixes
- [ ] **Misplaced video**: Line ~784-797 has "Integrated Rate Laws - Zero, First, & Second Order Reactions - Chemical Kinetics" in the **Intro to CS** section. This is a chemistry video. Move it to the **Calculus** section, or remove it entirely.
- [ ] **Empty href**: Line ~737 has `<a href="" target="_blank" ...>↗ Code.org</a>`. Fix the href to the correct YouTube channel URL, or remove the link if unknown.
- [ ] **Nested badge-row**: Several cards have `<div class="badge-row"><span class="badge-row">...</span></div>` — a `.badge-row` inside a `.badge-row`. Simplify to just one wrapping `<div class="badge-row">`.

### 2.7 — Mobile Drawer JS Update
In the `toggleMobileMenu()` function (~line 4590 area), update to toggle ARIA:
```javascript
function toggleMobileMenu() {
    var drawer = document.getElementById('mobileDrawer');
    var overlay = document.getElementById('mobile-overlay');
    var btn = document.querySelector('.mobile-menu-btn');
    drawer.classList.toggle('show');
    overlay.classList.toggle('show');
    var isOpen = drawer.classList.contains('show');
    drawer.setAttribute('aria-hidden', !isOpen);
    if (btn) btn.setAttribute('aria-expanded', isOpen);
}
```

### 2.8 — Verify
- [ ] Open resources.html in browser — all sections load, accent color is green #00ff88
- [ ] Click through all 14 sidebar topics — each section shows
- [ ] Check mobile (375px) — bottom chips work, drawer opens/closes
- [ ] Check that channel links still hover correctly (opacity change via CSS)
- [ ] Keyboard-tab through — focus indicators visible
- [ ] Right-click → View Source — no more inline `onmouseover`/`onmouseout`

---

## File Ownership
```
OWNS:
  resources.html

DO NOT TOUCH:
  index.html, year1-4.html (Agent 1)
  year1sem2calc*.html, year1sem1calc*.html (Agent 3)
  year1sem2introprog.html, introdbms, english, etc. (Agent 4)
  assets/** (foundation — read-only)
```
