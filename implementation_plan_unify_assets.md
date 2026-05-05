# Unify Math Page Assets

This plan outlines the process of extracting shared CSS and JavaScript from the various math-related HTML files into central asset files. This will improve maintainability, reduce file size, and ensure a consistent design across all calculus resources.

## Target Files

- `year1sem2calc2.html` (Main page)
- `year1sem2calc2lec[1-8].html`
- `year1sem2calc2lec[1-8]sol.html`
- `calculus_laws.html`
- `calculus_solutions.html`
- `year1sem1calclaws.html`
- `year1sem1calcsolutions.html`

## Proposed Assets

### 1. Central CSS (`assets/css/math-style.css`)
Contains:
- Global resets and typography (Inter, JetBrains Mono)
- Layout containers and grid logic (including desktop sidebar)
- Section and header styling
- Formula boxes (`.formula-box`, `.theorem`, `.important`)
- Step blocks and exam question styling
- Table and list formatting
- Interaction styles (`.print-btn`, `.nav-back`, `.progress-bar`)
- Print media queries

### 2. Central JS (`assets/js/math-scripts.js`)
Contains:
- Reading progress bar scroll listener
- (Optional) Any future shared math interactivity

## Refactoring Steps

1. Create the `assets/css` and `assets/js` directories.
2. Extract the `<style>` block from `year1sem2calc2lec1.html` into `assets/css/math-style.css`.
3. Extract the progress bar script into `assets/js/math-scripts.js`.
4. Iterate through all target HTML files:
   - Replace the large `<style>` block with `<link rel="stylesheet" href="assets/css/math-style.css">`.
   - Replace the inline `<script>` block with `<script src="assets/js/math-scripts.js"></script>`.
   - Ensure the `nav-back` link and `header` structure are consistent.
