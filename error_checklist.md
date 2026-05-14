# Error Checklist — Theme Toggle Implementation

Use this after completing each iteration. Work through every section before marking done.

---

## Section 1 — Theme Flash (Critical)

| # | Check | Pass? |
|---|---|---|
| 1.1 | Hard-refresh the page with Manuscript saved in localStorage. Does the page load in **Terminal** before flipping to Manuscript? | ❌ = flash bug |
| 1.2 | Is the anti-flash inline `<script>` placed as the **first child of `<body>`** (not deferred, not at bottom)? | Must be yes |
| 1.3 | Open DevTools → Network → Disable cache, reload. Manuscript should render with no white/black flash. | |

**Fix if failing:** Move the anti-flash snippet earlier, or switch to placing it in `<head>` after the stylesheet `<link>`.

---

## Section 2 — Terminal Theme Visual Regression

The Terminal theme must be **pixel-identical** to what it was before changes.

| # | Check | Expected |
|---|---|---|
| 2.1 | Background colour of `<body>` | `#000000` |
| 2.2 | Header `h1` colour | `#00ff88` |
| 2.3 | `.lec-card` top border | `2px solid #00ff88` |
| 2.4 | `.lec-link--notes` text colour | `#00ff88` |
| 2.5 | Table `td` text colour | `#00ff88` |
| 2.6 | `.formula-box` background | `#000000` |
| 2.7 | `body` font family | Inter, sans-serif |
| 2.8 | `.lec-card__badge` font | JetBrains Mono |
| 2.9 | `tr:hover` background | `#0f0f0f` |
| 2.10 | Card reveal animation still works on scroll | `.visible` class added via IntersectionObserver |

---

## Section 3 — Manuscript Theme Visual Check

| # | Check | Expected |
|---|---|---|
| 3.1 | `<body>` background | Warm parchment `#f5f0e8` |
| 3.2 | Header `h1` colour | Deep red `#8b1a1a` |
| 3.3 | `.lec-card` top border | `2px solid #8b1a1a` |
| 3.4 | `.lec-link--notes` background | Semi-transparent red tint |
| 3.5 | Body font switches to serif | Georgia or Times |
| 3.6 | Monospace elements (badge, lec-link) | Courier New |
| 3.7 | MathJax formulas render correctly on parchment bg | No invisible text |
| 3.8 | `tr:hover` background | `#ede8dc` (warm, not black) |
| 3.9 | `.formula-box` left border | Uses `--accent` red |
| 3.10 | `.section` borders | `#d4c9b0` (not `#1a1a1a`) |

---

## Section 4 — Toggle Button

| # | Check | Pass? |
|---|---|---|
| 4.1 | Button visible in header on page load | ✅ |
| 4.2 | Clicking toggles between `📜 Manuscript` and `💻 Terminal` labels | ✅ |
| 4.3 | `data-theme="manuscript"` present on `<html>` after switching to Manuscript | Check DevTools Elements |
| 4.4 | Attribute removed when switching back to Terminal | ✅ |
| 4.5 | `localStorage['calc2-theme']` updates on each click | DevTools → Application → Local Storage |

---

## Section 5 — Persistence Across Navigation

| # | Check | Pass? |
|---|---|---|
| 5.1 | Set Manuscript, close tab, reopen — stays Manuscript | ✅ |
| 5.2 | Set Terminal, navigate to a lecture page (Iter 2 only) — stays Terminal | ✅ |
| 5.3 | Toggle on lecture page persists when returning to main page | ✅ (shared localStorage key) |

---

## Section 6 — Print Output

| # | Check | Expected |
|---|---|---|
| 6.1 | `Ctrl+P` in Terminal mode — background is white, text is black | ✅ `@media print` override |
| 6.2 | `Ctrl+P` in Manuscript mode — same white/black output | ✅ `@media print` overrides theme vars |
| 6.3 | Theme toggle button absent from print preview | ✅ `.no-print` class applied |
| 6.4 | MathJax formulas appear correctly in print | ✅ |

---

## Section 7 — Mobile (≤600px)

| # | Check | Pass? |
|---|---|---|
| 7.1 | Toggle button wraps correctly at mobile width | `.print-btn` already has mobile override |
| 7.2 | `lec-grid` is single column in both themes | `grid-template-columns: 1fr` |
| 7.3 | Tables have `overflow-x: auto` in both themes | ✅ |
| 7.4 | Formula boxes have `overflow-x: auto` in both themes | ✅ |

---

## Section 8 — MathJax Compatibility

| # | Check | Pass? |
|---|---|---|
| 8.1 | MathJax loads in `<head>` (not moved to external JS) | Must not be deferred |
| 8.2 | Formulas render on initial load (Terminal) | ✅ |
| 8.3 | Formulas render after toggling to Manuscript | ✅ — no re-typeset needed since DOM is same |
| 8.4 | Formulas have visible colour contrast on parchment | Check: `#1a1a1a` text on `#f5f0e8` bg ≥ 4.5:1 contrast ratio |

---

## Section 9 — Iteration 2 Specific: Asset Paths

> Only run this section after starting Iteration 2.

| # | Check | Pass? |
|---|---|---|
| 9.1 | `assets/css/math-style.css` exists at repo root | ✅ |
| 9.2 | `assets/js/math-scripts.js` exists at repo root | ✅ |
| 9.3 | Each lecture file's `<link href="assets/css/...">` resolves correctly (all files are at root level — same depth) | Check: no 404 in DevTools Network |
| 9.4 | `year1sem2calc2lec6.html` is empty/stub — skip or stub-fill before linking | ⚠️ File was 0 bytes |
| 9.5 | JS-injected toggle button appears in all lecture pages | Inspect DOM on each page |
| 9.6 | `if (element)` guards prevent JS errors on pages missing `.lec-card`, `#progress-bar`, etc. | Check Console: zero errors |
| 9.7 | No duplicate `<style>` block remaining in any migrated file | Search for `<style>` in each file post-migration |

---

## Section 10 — Common Mistakes to Watch

| Mistake | Symptom | Fix |
|---|---|---|
| Missed `rgba()` green override | Green tint visible in Manuscript | Add `[data-theme="manuscript"]` override for that rgba rule |
| `var(--accent)` used in rgba context | `rgba(var(--accent), 0.1)` — **invalid CSS** | Use separate override rules, not rgba with vars |
| Anti-flash script placed at bottom of `<body>` | Flash of Terminal on Manuscript load | Move to top of `<body>` |
| `localStorage` key typo | Toggle doesn't persist | Must be exactly `'calc2-theme'` everywhere |
| `data-theme` on `<body>` instead of `<html>` | CSS `[data-theme]` selector misses | Must be `document.documentElement` |
| External JS file cached after changes | Old behaviour persists | Hard refresh (`Ctrl+Shift+R`) |
| Print block broken by `var()` | Print shows coloured bg | Ensure `@media print` explicitly sets `background: white !important` |
