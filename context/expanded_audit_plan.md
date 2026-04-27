# Expanded Directory-Wide UX/UI Audit (Revised)

Based on your feedback, I have updated the plan. I will preserve the visual aesthetic of the calculus pages as you requested, while focusing on mobile optimization, code cleanup, and performance.

## Group 1: Mathematics Pages Optimization (Preserving Current Aesthetics)
- **Current State**: The calculus and trig pages currently look great, and you prefer their minimalist black/white/SF Mono design. However, the way they load MathJax (the library that renders the math equations) could be improved.
- **Explanation of "Standardizing MathJax Imports"**: When a browser loads a webpage, if it hits a `<script>` tag for a massive library like MathJax, it will pause loading the rest of the webpage until MathJax finishes downloading. This is called "render-blocking." Standardizing the import means adding an `async` or `defer` attribute to the script tag. This tells the browser: *"Keep drawing the page so the user can see the text immediately, and load the math library in the background."*
- **Suggested Edits**:
  - Keep the existing black/white visual design exactly as it is since you like it.
  - Update the MathJax script tags across all math pages to load asynchronously to improve page load speed on mobile devices.

## Group 2: Mobile Optimization for Code and Math Blocks
- **Current State**: Across the site, `<pre>`, `<code>`, and `<div class="math-block">` elements lack proper mobile constraints. If a line of Java code or a LaTeX equation is wider than the phone screen, it forces the user to horizontally scroll the *entire* website, which is a frustrating mobile experience.
- **Suggested Edits (Approved by you)**:
  - Add robust global CSS rules (`max-width: 100%; overflow-x: auto; -webkit-overflow-scrolling: touch;`) to ensure that *only* the code/math block scrolls horizontally, keeping the main page firmly locked in place.
  - Style the internal scrollbar to be sleek and unobtrusive on mobile.

## Group 3: Extracting Duplicated JavaScript
- **Current State**: The `openTab(tabName)` JavaScript function is currently copy-pasted at the very bottom of every single subject page (e.g., `year1sem1compapp.html`, `year1sem2introprog.html`).
- **Suggested Edits**:
  - Extract the tab-switching logic into a centralized `ui.js` file.
  - Link this script globally so we don't have redundant code everywhere.

## Group 4: Hardcoded & Inconsistent "Back" Navigation
- **Current State**: The "← Back to Year X" links at the top of subject pages are hardcoded and manually styled on every page.
- **Suggested Edits**:
  - Convert these back links to use a standard `.nav-breadcrumb` class to ensure consistent spacing, hover states, and easy maintenance.

---
**Status**: Awaiting your order to execute.
