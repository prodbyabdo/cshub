# Iteration 2 — Theme Extraction to Shared Assets

> **Prerequisite:** Iteration 1 complete and working on `year1sem2calc2.html`.

## Goal
Extract the theme system (CSS tokens + toggle JS) into shared asset files so **all calc pages** get the Manuscript toggle automatically. Aligns with the [Unify Math Assets KI plan](/knowledge/unify_math_assets/artifacts/implementation_plan.md).

---

## New File Structure

```
cshub-main/
└── assets/
    ├── css/
    │   └── math-style.css     ← shared styles + theme tokens
    └── js/
        └── math-scripts.js    ← shared scripts incl. theme toggle
```

---

## Target HTML Files (20+ pages)

From the Unify Math Assets KI:

| File | Action |
|---|---|
| `year1sem2calc2.html` | Replace `<style>` → `<link>`, move toggle btn JS → external |
| `year1sem2calc2lec1.html` | Extract + link |
| `year1sem2calc2lec2.html` | Extract + link |
| `year1sem2calc2lec3.html` | Extract + link |
| `year1sem2calc2lec4.html` | Extract + link |
| `year1sem2calc2lec5.html` | Extract + link |
| `year1sem2calc2lec6.html` | Extract + link |
| `year1sem2calc2lec[1-6]sol.html` | Extract + link (×6) |
| `calculus_laws.html` | Extract + link |
| `calculus_solutions.html` | Extract + link |
| `year1sem1calclaws.html` | Extract + link |
| `year1sem1calcsolutions.html` | Extract + link |
| `calc2_mock_exam.html` | Extract + link |

---

## Step-by-Step

### Step 1 — Create `assets/css/math-style.css`

Move into this file:
- **Everything** from Iteration 1's `<style>` block (fully tokenized)
- `:root` Terminal tokens
- `[data-theme="manuscript"]` Manuscript tokens
- All manuscript-specific overrides
- Print media query

The file becomes the single source of truth for all math page styling.

### Step 2 — Create `assets/js/math-scripts.js`

Move into this file:
- Theme toggle IIFE (from Iteration 1)
- Reading progress bar listener (already in the KI plan)
- Card reveal IntersectionObserver (currently in `year1sem2calc2.html`)
- Hash scroll handler (currently in `year1sem2calc2.html`)

```js
// math-scripts.js
// 1. Anti-flash theme restore (runs immediately)
(function () {
  const saved = localStorage.getItem('calc2-theme');
  if (saved === 'manuscript') {
    document.documentElement.setAttribute('data-theme', 'manuscript');
  }
})();

// 2. DOM-ready functionality
document.addEventListener('DOMContentLoaded', function () {
  // Theme toggle button
  const btn = document.getElementById('theme-toggle');
  if (btn) { /* toggle logic */ }

  // Card reveal animation
  const cards = document.querySelectorAll('.lec-card');
  if (cards.length) { /* IntersectionObserver */ }

  // Hash scroll
  /* handleHash() */

  // Progress bar (if element exists)
  const bar = document.getElementById('progress-bar');
  if (bar) { /* scroll listener */ }
});
```

> [!NOTE]
> All features guard with `if (element)` so the single script works safely on pages that don't have every element (e.g., lecture pages have no `.lec-card` grid).

### Step 3 — Add toggle button to shared `<header>` template

Each page's header needs the button. Two options:

| Option | Pros | Cons |
|---|---|---|
| **A** — Manually add to each HTML file | Simple, no build step | Repetitive across 20 files |
| **B** — JS-inject the button via `math-scripts.js` | Single change point | Button appears after DOM parse |

**Recommendation: Option B** — inject via JS in `math-scripts.js`:

```js
// Auto-inject theme toggle into any page using math-style.css
const header = document.querySelector('header');
if (header && !document.getElementById('theme-toggle')) {
  const btn = document.createElement('button');
  btn.id = 'theme-toggle';
  btn.className = 'print-btn no-print';
  btn.style.marginLeft = '10px';
  header.appendChild(btn);
}
```

This means **zero HTML changes** to the 20 target files beyond adding the `<link>` and `<script>` tags.

### Step 4 — Anti-flash inline script in each `<head>`

Each HTML file gets one tiny inline `<script>` at the top of `<body>` (before stylesheet renders) to prevent theme flash:

```html
<script>
  if (localStorage.getItem('calc2-theme') === 'manuscript')
    document.documentElement.setAttribute('data-theme','manuscript');
</script>
```

This is the only new inline content per file (5 lines).

### Step 5 — Replace `<style>` and `<script>` blocks

For each target file:

```diff
- <style> ... 350 lines ... </style>
+ <link rel="stylesheet" href="assets/css/math-style.css">

  <body>
+ <script>if(localStorage.getItem('calc2-theme')==='manuscript')document.documentElement.setAttribute('data-theme','manuscript');</script>

- <script> ... inline JS ... </script>
+ <script src="assets/js/math-scripts.js"></script>
```

> [!WARNING]
> Lecture sub-pages are in subdirectories (e.g., `year1sem2calc2lec1.html` may be at root level). Verify all relative paths for `assets/` resolve correctly from each file's location before replacing.

---

## Verification Checklist (per file)

- [ ] Page renders identically in Terminal mode
- [ ] Manuscript toggle works and persists
- [ ] No theme flash on load
- [ ] Print styles still produce black-on-white output
- [ ] MathJax renders correctly in both themes
- [ ] Mobile layout unchanged

---

## Effort Estimate

| Task | Time |
|---|---|
| Create `math-style.css` | 30 min |
| Create `math-scripts.js` | 30 min |
| Update `year1sem2calc2.html` | 15 min |
| Update 19 remaining lecture files | ~2 hrs (batch find/replace) |
| Testing | 30 min |
| **Total** | **~3.5 hrs** |

---

## Outcome
- Single source of truth for all calc page styling
- Theme toggle available on every lecture and solutions page
- Future theme additions only require editing `math-style.css`
- Reduces per-page HTML by ~350 lines each
