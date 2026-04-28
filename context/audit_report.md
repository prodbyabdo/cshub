# Audit Report — `year1sem2introprog.html`

**Audited**: 2026-04-28  
**Compared against**: `year1sem2introdbms.html`, `year1sem2english.html`  
**File**: [year1sem2introprog.html](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html)

---

## Audit Health Score

| # | Dimension | Score | Key Finding |
|---|-----------|-------|-------------|
| 1 | Accessibility | 2 | Radio inputs lack IDs/labels; SVGs missing a11y attrs |
| 2 | Performance | 3 | Compiler iframe not lazy-loaded; no font preconnect |
| 3 | Theming | 3 | Consistent tokens but inline styles on Java Tutorials banner |
| 4 | Responsive Design | 3 | Good flex-wrap/grid but no explicit mobile breakpoints |
| 5 | Anti-Patterns | 2 | Inline styles, missing DOCTYPE, structural drift from siblings |
| **Total** | | **13/20** | **Acceptable — significant work needed** |

**Rating**: 10–13 Acceptable (significant work needed)

---

## Anti-Patterns Verdict

**Pass** — This does NOT look AI-generated. The design is intentional, cohesive, and consistent with the project's established dark-mode academic hub aesthetic. The use of Inter font is a project-wide design system choice, not an AI slop tell. Color usage is purposeful (glow cards, dot accents) and serves the educational content hierarchy. No gradient text, glassmorphism, hero metrics, or card grid slop detected.

**However**, there is structural drift from sibling pages that erodes consistency:
- Missing `<!DOCTYPE html>` (all sibling pages have it)
- Missing `header-actions` section with PDF/resource buttons (DBMS page has this)
- One SVG symbol (Annotation) doesn't match the reference textbook image

---

## Executive Summary

- **Audit Health Score: 13/20** (Acceptable)
- **Total issues: 15** — P0: 0 | P1: 3 | P2: 7 | P3: 5
- **Top 5 critical issues:**
  1. Missing `<!DOCTYPE html>` — triggers quirks mode in all browsers
  2. Annotation SVG doesn't match textbook reference symbol
  3. Missing `header-actions` section that sibling pages include
  4. Exam radio buttons have no unique IDs, no accessible labels
  5. Compiler iframe loads immediately even when tab is hidden
- **Recommended next steps:** Fix P1 issues first (DOCTYPE, SVG, header-actions), then batch P2 fixes

---

## Detailed Findings by Severity

### P1 Major — Fix before release

---

#### [P1] Missing `<!DOCTYPE html>` declaration
- **Location**: Line 1
- **Category**: Anti-Pattern / Standards
- **Impact**: Browser enters quirks mode, causing inconsistent rendering of CSS box model, table layouts, and font sizing across browsers. Every sibling page (`year1sem2introdbms.html` line 2, `year1sem2english.html` line 1) includes the DOCTYPE.
- **Standard**: HTML5 specification
- **Recommendation**: Add `<!DOCTYPE html>` as the very first line before `<html lang="en">`
- **Suggested command**: `$normalize`

---

#### [P1] Annotation SVG doesn't match textbook symbol
- **Location**: [Line 694–698](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html#L694-L698)
- **Category**: Content Accuracy
- **Impact**: The annotation symbol should be an open bracket shape (vertical line with horizontal bars at top and bottom, forming a ⌐ or [ shape) with a dashed line extending right. Current SVG only shows a plain vertical line + horizontal dashed line, which doesn't match the standard flowchart annotation symbol from the textbook reference.
- **Current SVG**:
```html
<svg width="60" height="30">
  <line x1="30" y1="2" x2="30" y2="28" stroke="#00ff88" stroke-width="1.5"/>
  <line x1="30" y1="15" x2="55" y2="15" stroke="#00ff88" stroke-width="1.5" stroke-dasharray="4,3"/>
</svg>
```
- **Should be** (open bracket with dashed line):
```html
<svg width="60" height="30">
  <line x1="10" y1="2" x2="10" y2="28" stroke="#00ff88" stroke-width="1.5"/>
  <line x1="10" y1="2" x2="25" y2="2" stroke="#00ff88" stroke-width="1.5"/>
  <line x1="10" y1="28" x2="25" y2="28" stroke="#00ff88" stroke-width="1.5"/>
  <line x1="25" y1="15" x2="55" y2="15" stroke="#00ff88" stroke-width="1.5" stroke-dasharray="4,3"/>
</svg>
```
- **Recommendation**: Replace the SVG to match the textbook annotation bracket shape
- **Suggested command**: Manual fix (content accuracy, not a design command)

---

#### [P1] Missing `header-actions` section
- **Location**: After [line 383](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html#L383) (inside `<header>`)
- **Category**: Anti-Pattern / Consistency
- **Impact**: The DBMS page (line 621–624) includes a `header-actions` div with PDF download and video tutorial links. The introprog page lacks this, creating inconsistency across sibling pages. This is part of the "80% similar" styling gap the user identified.
- **Recommendation**: Add `header-actions` section with a PDF link (or disabled placeholder) and a link to `resources.html#java-tutorials`, matching the DBMS page pattern.
- **CSS needed**: The `.header-actions` and `.pdf-btn` classes are NOT present in the introprog stylesheet — they need to be added from the DBMS page's CSS.
- **Suggested command**: `$normalize`

---

### P2 Minor — Fix in next pass

---

#### [P2] Inline styles on Java Tutorials banner
- **Location**: [Lines 1880–1891](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html#L1880-L1891)
- **Category**: Theming / Anti-Pattern
- **Impact**: The "Full Java Video Library" banner uses extensive inline styles instead of CSS classes. This makes it harder to maintain, breaks the page's pattern of class-based styling, and can't be themed.
- **Recommendation**: Extract inline styles into named CSS classes (e.g. `.promo-banner`, `.promo-title`, `.promo-cta`)
- **Suggested command**: `$extract`

---

#### [P2] Exam radio buttons lack unique IDs and accessible labels
- **Location**: [Lines 1826–1872](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html#L1826-L1872)
- **Category**: Accessibility
- **Impact**: Radio inputs have no `id` attributes and no programmatic `<label for="">` association. Screen readers cannot properly announce which option is selected. Each radio has a `<label>` wrapper but no `for`/`id` pairing.
- **WCAG**: 1.3.1 Info and Relationships, 4.1.2 Name, Role, Value
- **Recommendation**: Add unique `id` to each `<input>` and `for` attribute to each `<label>`
- **Suggested command**: `$harden`

---

#### [P2] Compiler iframe not lazy-loaded
- **Location**: [Lines 1941–1943](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html#L1941-L1943)
- **Category**: Performance
- **Impact**: The OneCompiler iframe loads immediately on page load even though the Compiler tab is hidden by default. This adds unnecessary network requests and delays initial page load.
- **Recommendation**: Add `loading="lazy"` to the iframe, or defer loading until the Compiler tab is first activated
- **Suggested command**: `$optimize`

---

#### [P2] SVGs in flowchart table lack accessibility attributes
- **Location**: [Lines 680–718](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html#L680-L718)
- **Category**: Accessibility
- **Impact**: All 8 flowchart SVGs lack `role="img"` and `aria-label` attributes. Screen readers cannot describe what these symbols represent.
- **WCAG**: 1.1.1 Non-text Content
- **Recommendation**: Add `role="img" aria-label="Process Symbol"` (etc.) to each SVG
- **Suggested command**: `$harden`

---

#### [P2] Tab buttons use inline `onclick` handlers
- **Location**: [Lines 386–390](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html#L386-L390)
- **Category**: Anti-Pattern
- **Impact**: Inline event handlers are harder to maintain and don't follow modern JS practices. However, this is consistent across ALL pages in the project (DBMS, English all use inline onclick), so this is a systemic pattern, not a one-off issue.
- **Recommendation**: Low priority — would require refactoring all pages simultaneously
- **Suggested command**: `$normalize` (systemic, defer)

---

#### [P2] No focus management on tab switch
- **Location**: [openTab function, lines 1948–1962](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html#L1948-L1962)
- **Category**: Accessibility
- **Impact**: When a tab is activated via keyboard, focus does not move to the tab panel content. Keyboard users must tab through all buttons before reaching the content. The `tabindex` and `aria-selected` patterns are missing.
- **WCAG**: 2.1.1 Keyboard, 4.1.2 Name/Role/Value
- **Recommendation**: Add `role="tablist"`, `role="tab"`, `role="tabpanel"`, and `aria-selected` to implement WAI-ARIA tab pattern
- **Suggested command**: `$harden`

---

#### [P2] Inline `onmouseover`/`onmouseout` on CTA button
- **Location**: [Lines 1888–1890](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html#L1888-L1890)
- **Category**: Anti-Pattern
- **Impact**: The "Go to Java Resources Tab" button uses inline JS for hover effects (`onmouseover`, `onmouseout`). This should use CSS `:hover` instead — it's simpler, more performant, and maintainable.
- **Recommendation**: Replace inline JS hover with a CSS class and `:hover` pseudo-class
- **Suggested command**: `$extract`

---

### P3 Polish — Fix if time permits

---

#### [P3] No Google Fonts `preconnect` hint
- **Location**: [Lines 7–9](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html#L7-L9)
- **Category**: Performance
- **Impact**: Missing `<link rel="preconnect" href="https://fonts.googleapis.com">` delays font loading slightly. Minor impact.
- **Recommendation**: Add preconnect links before the font stylesheet link
- **Suggested command**: `$optimize`

---

#### [P3] Google Fonts URL uses `&amp;` entity encoding
- **Location**: [Line 8](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html#L8)
- **Category**: Standards
- **Impact**: The font URL uses `&amp;` instead of `&` in the `href`. While technically valid HTML entity encoding, the DBMS and English pages use plain `&`. Minor inconsistency.
- **Recommendation**: Normalize to match sibling pages (use `&` directly)
- **Suggested command**: `$normalize`

---

#### [P3] Missing `meta description`
- **Location**: `<head>` section
- **Category**: SEO
- **Impact**: No `<meta name="description">` tag. Won't affect functionality but reduces SEO quality if the site is indexed.
- **Recommendation**: Add a descriptive meta tag
- **Suggested command**: `$polish`

---

#### [P3] Course Summary tab lacks section dividers between lectures
- **Location**: Between sections §1–§8
- **Category**: Consistency
- **Impact**: The English page uses `<hr class="section-divider">` between major sections. The Course Summary tab relies solely on `.section-title` dividers. The DBMS page also uses only `.section-title`, so this is partially consistent, but section dividers could improve readability for the dense 8-lecture content.
- **Recommendation**: Optional — consider adding dividers between lecture groups (e.g., after §4 Pseudocode before §5 Flowcharts)
- **Suggested command**: `$arrange`

---

#### [P3] Exam section has only 4 questions
- **Location**: [Lines 1822–1873](file:///c:/Users/ben.arthur/Downloads/new%20backup/cshub-main/year1sem2introprog.html#L1822-L1873)
- **Category**: Content
- **Impact**: The practice exam only covers 4 questions on theory topics. The DBMS page has comprehensive exam sections with answer keys. The English page has 35+ questions with toggleable answers.
- **Recommendation**: Expand with more questions covering all 8 lectures, add an answer key with toggle functionality
- **Suggested command**: Manual content expansion

---

## Patterns & Systemic Issues

1. **Structural drift from sibling pages**: The introprog page is missing `<!DOCTYPE html>`, `header-actions`, and uses `&amp;` in font URLs where siblings use `&`. These small differences compound to create the "80% similar" feel.

2. **Inline styles concentrated in Java Tutorials tab**: Lines 1880–1891 contain the most inline styling on the entire page. All other tabs follow the class-based pattern well.

3. **Accessibility is project-wide gap**: No page in the project implements WAI-ARIA tab patterns, keyboard focus management, or proper form labeling. This isn't unique to introprog but is worth noting.

4. **Inline onclick is a project convention**: All pages use inline `onclick` for tab switching. This is a conscious (if not ideal) pattern — don't fix in isolation.

---

## Positive Findings

- ✅ **CSS custom properties used consistently** — all colors, fonts reference `:root` variables
- ✅ **Card glow pattern is well-executed** — blue/red/green/gold/purple glow variants add visual hierarchy without being garish
- ✅ **Content is comprehensive and well-structured** — 8 full lecture sections with accurate pseudocode examples
- ✅ **Inline SVGs for flowchart symbols** — creative approach that avoids external image dependencies
- ✅ **Deep linking script works correctly** — hash-based navigation activates correct tabs
- ✅ **Tab system is functional** — works across all 5 tabs without JS framework dependencies
- ✅ **`.section-title` pattern** — consistent with DBMS page, properly creates visual breaks
- ✅ **`.def` callout pattern** — consistently used for definitions across both introprog and DBMS pages
- ✅ **Font loading** — same Inter + JetBrains Mono combination across all pages

---

## Recommended Actions

Priority order (P1 first):

1. **[P1] `$normalize`** — Add `<!DOCTYPE html>`, normalize font URL encoding, add `header-actions` section with PDF/resource buttons, add missing `.header-actions`/`.pdf-btn` CSS classes from DBMS page
2. **[P1] Manual fix** — Replace annotation SVG with correct open-bracket symbol matching textbook reference
3. **[P2] `$harden`** — Add unique IDs to exam radio inputs, add `role="img"` + `aria-label` to flowchart SVGs, add WAI-ARIA tab attributes
4. **[P2] `$extract`** — Extract Java Tutorials banner inline styles into CSS classes, replace inline JS hover with CSS `:hover`
5. **[P2] `$optimize`** — Add `loading="lazy"` to compiler iframe, add font preconnect hints
6. **[P3] `$polish`** — Add meta description, optionally add section dividers between lecture groups

> You can ask me to run these one at a time, all at once, or in any order you prefer.
>
> Re-run `$audit` after fixes to see your score improve.
