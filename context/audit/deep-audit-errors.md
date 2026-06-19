# Deep Audit Findings

## Findings

### A1-001
- Severity: P1 Major
- Category: Links
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1.html:503`
- Evidence: `year1.html` links Calculus II Solutions to `year1sem2calc2sol.html`, but that file does not exist.
- Impact: Users hit a dead internal route from a primary Year 1 subject card.
- Recommendation: Point the button to the correct existing file, or remove/disable it until the target exists.
- Verification: Re-run local link validation and `Test-Path year1sem2calc2sol.html`.
- Status: open

### A1-002
- Severity: P1 Major
- Category: Routing
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2calc2lec6.html`
- Evidence: `year1sem2calc2lec6.html` is a 0-byte public page.
- Impact: Direct requests return a blank page, and any future links to it will appear broken.
- Recommendation: Remove it from public routing until content exists, or add a real lecture/stub page with explicit unavailable state.
- Verification: Confirm the file has meaningful HTML or no public links route to it.
- Status: open

### A1-003
- Severity: P2 Minor
- Category: Routing
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\index.html:217`, `index.html:226`, `index.html:235`, `year2.html:47`, `year3.html:47`, `year4.html:47`
- Evidence: Home links Year 2, Year 3, and Year 4 as normal cards, but each destination renders `Coming Soon`.
- Impact: Primary navigation makes unfinished sections look complete.
- Recommendation: Mark cards as unavailable, remove them from primary nav, or replace destinations with fuller landing pages.
- Verification: Check home cards and Year 2-4 pages after update.
- Status: open

### A1-004
- Severity: P2 Minor
- Category: Links / Accessibility
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1.html:367`, `year1.html:377`, `year1.html:420`, `year1.html:472`, `year1.html:492`
- Evidence: Five subject cards use `href="#"` for disabled-looking “Resources” actions.
- Impact: Fake navigation still behaves like links, causing jump-to-top behavior and confusing keyboard/screen-reader users.
- Recommendation: Replace fake anchors with non-link UI or point them to explicit unavailable pages.
- Verification: Search `year1.html` for `href="#"`.
- Status: open

### A1-005
- Severity: P1 Major
- Category: Links
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\resources.html:737`, `resources.html:881`, `resources.html:900`, `resources.html:919`, `resources.html:938`
- Evidence: `resources.html` contains 29 anchors with `href="" target="_blank"`.
- Impact: Visible resource CTAs open empty/self targets instead of intended external destinations.
- Recommendation: Fill missing URLs or remove links with no destination.
- Verification: Re-run search for `href="" target="_blank"`.
- Status: open

### A1-006
- Severity: P2 Minor
- Category: Links / Security
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\index.html:200`, `index.html:267`, `resources.html:655`, `resources.html:676`, `resources.html:794`
- Evidence: `index.html` has 2 external `_blank` links missing `rel`; `resources.html` has 328 `_blank` anchors missing `rel="noopener noreferrer"`.
- Impact: External tabs are opened without standard opener protection.
- Recommendation: Add `rel="noopener noreferrer"` to every external `target="_blank"` anchor.
- Verification: Re-run `_blank` anchor scan.
- Status: open

### A1-007
- Severity: P2 Minor
- Category: Routing
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2calc2lec1.html:565`, `year1sem2calc2lec2.html:565`, `year1sem2calc2lec3.html:243`, `year1sem2calc2lec4.html:244`, `year1sem2calc2lec5.html:317`, `year1sem2calc2lec7.html:285`, `year1sem2calc2lec8.html:285`
- Evidence: Public Calc II lecture pages embed/link PDFs from `context/calc2/...`.
- Impact: Public pages depend on an internal/excluded directory, risking deployment inconsistency.
- Recommendation: Move publishable PDFs to a public assets/content directory and update links.
- Verification: Search public HTML for `context/calc2/`.
- Status: open

### A1-008
- Severity: P2 Minor
- Category: Routing / Content
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\cs-wiki.html:327`, `cs-wiki.html:332`, `cs-wiki.html:340`, `wiki\programming.html:17`, `wiki\programming.html:30`, `wiki\algorithms.html:17`, `wiki\algorithms.html:29`
- Evidence: `cs-wiki.html` links category pages as real destinations, but 12 wiki category pages are placeholder shells.
- Impact: Wiki navigation lands on thin placeholder pages instead of substantive category content.
- Recommendation: Flesh out category pages or label them clearly as index/stub pages before navigation.
- Verification: Search `wiki/` for placeholder strings and check `cs-wiki.html` links.
- Status: open

### A2-001
- Severity: P1 Major
- Category: Accessibility
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1.html:328`, `year1.html:332`, `resources.html:612`, `resources.html:629`
- Evidence: Semester selection and resource topic navigation use clickable `<div onclick=...>` with no native semantics, `tabindex`, or keyboard handling.
- Impact: Keyboard users cannot reliably reach or activate primary navigation controls.
- WCAG/Standard: WCAG 2.1.1, 4.1.2, 1.3.1.
- Recommendation: Replace with semantic `<button>` or `<a>` controls and expose correct state.
- Verification: Static markup review and keyboard pass.
- Status: open

### A2-002
- Severity: P1 Major
- Category: Accessibility
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\resources.html:585`, `resources.html:591`, `resources.html:601`, `resources.html:4565`
- Evidence: Mobile drawer overlay is a clickable `div`; icon-only menu button has no accessible name; close button exposes only `&times;`; `toggleMobileMenu()` does not update ARIA or manage focus.
- Impact: Screen-reader and keyboard users cannot identify or safely operate drawer state.
- WCAG/Standard: WCAG 4.1.2, 2.4.3, 2.1.1.
- Recommendation: Add accessible names, `aria-expanded`, `aria-controls`, dialog semantics, focus placement, and focus return.
- Verification: Static ARIA check plus keyboard drawer test.
- Status: open

### A2-003
- Severity: P1 Major
- Category: Accessibility
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\resources.html:647`, `resources.html:786`, `resources.html:4156`
- Evidence: `resources.html` has 224 `<img>` elements and none include `alt`.
- Impact: Resource thumbnails have no text alternative or decorative-empty declaration.
- WCAG/Standard: WCAG 1.1.1.
- Recommendation: Add descriptive `alt` text or `alt=""` when adjacent text fully names the card.
- Verification: Re-count `<img>` elements without `alt=`.
- Status: open

### A2-004
- Severity: P1 Major
- Category: Accessibility
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1.html:188`, `year1.html:345`
- Evidence: Subject search input relies on placeholder text and `.search-input:focus` removes the default outline.
- Impact: Screen-reader users lack a persistent label and keyboard users lose a visible focus ring.
- WCAG/Standard: WCAG 3.3.2, 2.4.7, 1.3.1.
- Recommendation: Add a programmatic label and restore a visible focus style.
- Verification: Inspect label association and focus state.
- Status: open

### A2-005
- Severity: P2 Minor
- Category: Accessibility
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1.html:215`, `year1.html:294`, `year1.html:367`, `year1.html:377`, `year1.html:420`, `year1.html:472`, `year1.html:492`
- Evidence: Disabled resource actions are focusable anchors with `href="#"`, `.btn-disabled`, and stretched-link overlays.
- Impact: Users encounter unavailable-looking controls that remain interactive.
- WCAG/Standard: WCAG 3.2.4, 4.1.2.
- Recommendation: Use real disabled buttons or plain unavailable text until content exists.
- Verification: Keyboard tab through Year 1 subject cards.
- Status: open

### A2-006
- Severity: P2 Minor
- Category: Accessibility
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\resources.html:593`, `resources.html:612`, `resources.html:4581`
- Evidence: Resource topic switcher hides/shows `.content-section` panels with classes only; no tablist/tab roles, `aria-selected`, `aria-controls`, or keyboard roving focus.
- Impact: Assistive tech users are not told which topic is selected or what panel changed.
- WCAG/Standard: WCAG 4.1.2, 2.1.1, WAI-ARIA Tabs.
- Recommendation: Implement a real tabs or navigation pattern with state and keyboard behavior.
- Verification: Inspect ARIA attributes and keyboard navigation.
- Status: open

### A2-007
- Severity: P2 Minor
- Category: Accessibility
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\cs-wiki.html:252`, `wiki\programming.html:13`, `wiki\programming.html:19`
- Evidence: `cs-wiki.html` and all 102 wiki HTML files lack a page-level `<main>` landmark.
- Impact: Screen-reader users lose a standard skip target for primary content.
- WCAG/Standard: WCAG 1.3.1, 2.4.1.
- Recommendation: Wrap primary article content in one `<main>` landmark per page/template.
- Verification: Search wiki pages for `<main>`.
- Status: open

### A3-301
- Severity: P1 Major
- Category: Assets
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\calc2_mock_exam2.html:13`, `calc2_mock_exam2.html:1269`
- Evidence: Page references missing `assets/css/math-style.css` and `assets/js/math-scripts.js`.
- Impact: Public page produces guaranteed 404s and may lose shared styling/behavior.
- Recommendation: Restore missing shared files or inline the critical dependencies.
- Verification: Check `assets/css/math-style.css` and `assets/js/math-scripts.js` exist and load.
- Status: open

### A3-302
- Severity: P2 Minor
- Category: Assets
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2compmain.html:9`, `year1sem2introdbms.html:9`
- Evidence: Both pages link missing `assets/css/global.css`.
- Impact: Missing base styles can cause inconsistent rendering and avoidable 404s.
- Recommendation: Restore `assets/css/global.css` or remove the dead reference and consolidate required base rules.
- Verification: Check `assets/css/global.css` exists and page network has no 404.
- Status: open

### A3-303
- Severity: P2 Minor
- Category: Performance
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\resources.html:644`
- Evidence: `resources.html` is 317,142 bytes and contains 224 mostly remote YouTube thumbnail images.
- Impact: Large HTML parse cost, oversized DOM, and remote image pressure hurt mobile performance.
- Recommendation: Split catalog into smaller pages/sections or load card data incrementally.
- Verification: Measure file size, DOM count, and resource waterfall after refactor.
- Status: open

### A3-304
- Severity: P2 Minor
- Category: Performance
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\resources.html:676`
- Evidence: `resources.html` has 134 `onmouseover`/`onmouseout` hover-handler occurrences.
- Impact: Inline CSS/JS bloats HTML and prevents shared behavior caching.
- Recommendation: Replace inline handlers with shared classes and CSS `:hover`.
- Verification: Search for `onmouseover` and `onmouseout`.
- Status: open

### A3-305
- Severity: P2 Minor
- Category: Performance
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2calc2lec1.html:563`, `year1sem2calc2lec3.html:242`
- Evidence: Calc II lecture pages eagerly embed full PDFs in `iframe` viewers with fixed `height: 600px`.
- Impact: PDFs are fetched/rendered before the user asks, costing bandwidth and memory.
- Recommendation: Use preview cards and explicit “Load viewer” actions, or lazy-load iframes.
- Verification: Inspect network waterfall and iframe loading behavior.
- Status: open

### A3-306
- Severity: P2 Minor
- Category: Performance
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2calc2.html:8`, `year1sem2calc2lec1.html:8`, `year1sem2calc2lec2.html:8`, `year1sem2calc2lec3.html:7`, `year1sem2calc2lec4.html:7`, `year1sem2calc2lec7.html:7`, `year1sem2calc2lec8.html:7`, `calculus_laws.html:7`, `year1sem1calclaws.html:9`
- Evidence: Several math pages load MathJax in `<head>` without `async`/`defer`, while others use a different async CDN pattern.
- Impact: Render-blocking risk and unpredictable math loading across pages.
- Recommendation: Standardize one non-blocking MathJax strategy and shared config.
- Verification: Search MathJax script tags and confirm consistent loading.
- Status: open

### A3-307
- Severity: P2 Minor
- Category: Responsive
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2programmingjava.html:39`, `year1sem2programmingjava.html:371`
- Evidence: `.page` keeps `padding: 48px 52px`; `.toc` has `min-width: 300px` with no mobile fallback.
- Impact: Narrow phones can overflow horizontally instead of reflowing.
- Recommendation: Add mobile breakpoints reducing padding and setting `.toc { width: 100%; min-width: 0; }`.
- Verification: Test at narrow viewport widths.
- Status: open

### A3-308
- Severity: P2 Minor
- Category: Responsive
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\calculus_laws.html:23`, `calculus_laws.html:81`, `calculus_laws.html:99`, `calculus_laws.html:525`, `year1sem1calclaws.html:26`, `year1sem1calclaws.html:84`, `year1sem1calclaws.html:102`, `year1sem1calclaws.html:1836`
- Evidence: Law pages set main containers to `overflow: hidden` and place dense formula/table content without local horizontal scrolling.
- Impact: Long equations/tables can clip or force page overflow on small screens.
- Recommendation: Remove container clipping and wrap math/table blocks in `overflow-x: auto` containers.
- Verification: Mobile viewport review of math/table sections.
- Status: open

### A3-309
- Severity: P2 Minor
- Category: Performance
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2calc2lec1sol.html:10`, `year1sem2calc2lec2sol.html:10`
- Evidence: At least seven Calc II solution pages duplicate the same large inline CSS block and MathJax boilerplate.
- Impact: Inflates page weight and blocks stylesheet caching.
- Recommendation: Move shared solution-page shell into reusable stylesheet/script assets.
- Verification: Compare `*sol.html` pages for reduced duplicate CSS/JS.
- Status: open

### A4-001
- Severity: P1 Major
- Category: Theming
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2introdbms.html:9`, `year1sem2compmain.html:9`
- Evidence: Both pages load `assets/css/global.css`, but the repo has no `assets\css\global.css` or `assets\css\` directory.
- Impact: Intended shared token/source-of-truth layer is broken.
- Recommendation: Restore the shared stylesheet or remove the dead dependency and consolidate tokens into a real shared asset.
- Verification: Confirm `assets/css/global.css` exists and is used consistently.
- Status: duplicate-of A3-302

### A4-002
- Severity: P2 Minor
- Category: Theming
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2introprog.html:839`, `year1sem2introdbms.html:524`, `year1sem2english.html:75`, `year1sem2calc2.html:26`, `year1sem2calc2.html:491`
- Evidence: Intro Programming, DBMS, and English share a dark tabbed course shell; Calculus II uses a separate dual-theme system and control model.
- Impact: Year 1 subject pages read as separate products rather than one product family.
- Recommendation: Keep Calculus-specific personality only if anchored to shared shell primitives and token names.
- Verification: Compare subject-page header, tab, action, and token structures.
- Status: open

### A4-003
- Severity: P2 Minor
- Category: Theming
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\resources.html:20`, `index.html:20`, `wiki\wiki.css:7`, `resources.html:4165`, `resources.html:4180`
- Evidence: `resources.html` uses `#00c288`; `index.html` and `wiki/wiki.css` use `#00ff88`.
- Impact: Accent drift weakens the site’s main visual identity.
- Recommendation: Promote one site-level accent token and consume it everywhere.
- Verification: Search accent hex values.
- Status: open

### A4-004
- Severity: P2 Minor
- Category: Anti-Pattern
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\resources.html:677`, `resources.html:794`, `resources.html:4165`, `year1sem2introprog.html:2797`, `year1sem2introdbms.html:629`, `year1sem2english.html:408`
- Evidence: `resources.html` contains 151 `style=` attributes; DBMS 30; Intro Programming 12; English 8.
- Impact: Styling changes require page-by-page edits and accelerate visual drift.
- Recommendation: Pull repeated link/button/card patterns into shared classes.
- Verification: Re-count `style=` attributes after cleanup.
- Status: open

### A4-005
- Severity: P2 Minor
- Category: Theming
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\wiki\wiki.css:1`, `wiki\ai\artificial-intelligence.html:31`, `wiki\databases\sql.html:36`, `wiki\data-structures\linked-list.html:26`
- Evidence: Wiki pages use dark tokens, but repeated source footers use hard-coded light colors `#e2e8f0` and `#64748b`.
- Impact: Footer styling bypasses the wiki theme contract.
- Recommendation: Replace repeated inline source footer with a shared `.source-note` class in `wiki/wiki.css`.
- Verification: Search wiki pages for those hard-coded footer colors.
- Status: open

### A4-006
- Severity: P1 Major
- Category: Content
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\wiki\cybersecurity.html:17`, `wiki\data-structures\trees.html:15`, `wiki\ai\artificial-intelligence.html:17`, `wiki\software-engineering\software-development-process.html:17`
- Evidence: Public wiki pages expose placeholder shells, blank stubs, and imported article shells with cleanup markers.
- Impact: Users can navigate deep into pages that look production-ready but are incomplete.
- Recommendation: Hide/de-emphasize unfinished topics or label them consistently before click-through.
- Verification: Search for placeholder and cleanup-marker text across `wiki/**`.
- Status: overlaps-with A1-008

### C-001
- Severity: P1 Major
- Category: Routing
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2calc2.html:590`, `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2calc2lec6.html`
- Evidence: `year1sem2calc2.html` links Lecture 6 Notes to `year1sem2calc2lec6.html`, and that target is a 0-byte file.
- Impact: This is not only a dormant blank page; it is reachable from the public Calc II lecture list and renders as a blank route.
- Recommendation: Remove/disable the Lecture 6 Notes link until the page is populated, or populate `year1sem2calc2lec6.html` with a real notes page.
- Verification: Open the Lecture 6 Notes link from `year1sem2calc2.html` and confirm it no longer lands on a blank page.
- Status: expands A1-002

### C-002
- Severity: P1 Major
- Category: Security / Performance
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\calculus_solutions.html:8`, `unit_circle_trig.html:8`, `year1sem1calcsolutions.html:9`, `year1sem2calc2lec1sol.html:8`, `year1sem2calc2lec2sol.html:8`, `year1sem2calc2lec3sol.html:7`, `year1sem2calc2lec4sol.html:8`, `year1sem2calc2lec5sol.html:8`, `year1sem2calc2lec6sol.html:8`, `year1sem2calc2lec7sol.html:8`, `year1sem2calc2lec8sol.html:8`
- Evidence: These pages load `https://polyfill.io/v3/polyfill.min.js?features=es6`. Cloudflare documented on June 26, 2024 that Polyfill.io was used to inject malicious code and recommended removing Polyfill.io or replacing it with a secure alternative: https://blog.cloudflare.com/automatically-replacing-polyfill-io-links-with-cloudflares-mirror-for-a-safer-internet/
- Impact: Public pages depend on a third-party script source with known supply-chain risk, and modern browsers likely do not need this ES6 polyfill.
- Recommendation: Remove the Polyfill.io script entirely if supported browsers no longer need it; otherwise replace it with a trusted, pinned alternative.
- Verification: Search for `polyfill.io` and confirm zero public references remain.
- Status: open

### C-003
- Severity: P2 Minor
- Category: Links / Security
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\calculus_laws.html:172`, `calculus_solutions.html:2167`, `year1sem2calc2.html:507`, `year1sem2calc2lec1.html:544`, `year1sem2english.html:225`, `year1sem2introprog.html:2812`
- Evidence: A broader root-page scan found `_blank` anchors without `rel="noopener noreferrer"` across math and subject pages, not only `index.html` and `resources.html`.
- Impact: The external-tab opener hardening gap is systemic across public course pages.
- Recommendation: Add `rel="noopener noreferrer"` to every `target="_blank"` anchor, including PDF/resource links in subject pages.
- Verification: Re-run a repo-wide scan for `<a ... target="_blank">` without `rel` containing `noopener`.
- Status: expands A1-006

### C-004
- Severity: P2 Minor
- Category: Accessibility / Security
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2introprog.html:2858`, `year1sem2introprog_preview.html:1430`
- Evidence: The embedded OneCompiler Java iframe has no `title`, no `sandbox`, and no `referrerpolicy`.
- Impact: Screen-reader users get an unnamed frame, and the third-party compiler embed receives broad default iframe permissions.
- WCAG/Standard: WCAG 4.1.2 Name, Role, Value.
- Recommendation: Add a descriptive `title`, restrict capabilities with `sandbox` to the minimum needed, and set an explicit `referrerpolicy`.
- Verification: Inspect iframe markup and test that the compiler still works with reduced permissions.
- Status: open

### C-005
- Severity: P2 Minor
- Category: Accessibility
- Location: `C:\Users\ben.arthur\Desktop\cshub-main\year1sem2compmain.html:196`, `year1sem2english.html:76`, `year1sem2introdbms.html:525`, `year1sem2introprog.html:840`, `year1sem1compapp.html:229`, `year1sem1introcs.html:99`
- Evidence: Multiple subject pages implement tab-like UIs with `.tab-btn`, `.tab-content`, and `openTab(...)`, but the tab groups do not expose `role="tablist"`, `role="tab"`, `role="tabpanel"`, `aria-selected`, `aria-controls`, or arrow-key behavior.
- Impact: The selected tab and controlled panel relationship are not programmatically exposed, and keyboard behavior does not match the expected tab pattern.
- WCAG/Standard: WCAG 4.1.2, WCAG 2.1.1, WAI-ARIA Tabs.
- Recommendation: Standardize subject-page tabs with one shared accessible tab component or downgrade them to plain navigation links if full tab semantics are not needed.
- Verification: Inspect all `.tab-btn` groups for ARIA state and keyboard behavior after implementation.
- Status: open

## Duplicate / Merged Findings

- `A4-001` duplicates `A3-302`; both identify missing `assets/css/global.css`.
- `A1-004` and `A2-005` cover the same fake disabled `href="#"` Year 1 controls from link and accessibility angles.
- `A1-008` and `A4-006` overlap on public wiki placeholders; keep both until fixing because one is routing-focused and one is content-quality focused.
- `C-001` expands `A1-002` by confirming the blank Lecture 6 page is directly linked from the public Calc II index.
- `C-003` expands `A1-006` by showing the `_blank` hardening issue also affects math and subject pages outside `index.html` and `resources.html`.

## Needs Confirmation

- `A3-305`: exact PDF iframe runtime impact should be confirmed in browser/network tools.
- `A3-307`: exact mobile overflow should be confirmed in browser at narrow widths.
- `A3-308`: exact clipped formulas/tables should be confirmed in browser at narrow widths.

## Final Severity Counts

| Severity | Count |
|---|---:|
| P0 Blocking | 0 |
| P1 Major | 12 |
| P2 Minor | 23 |
| P3 Polish | 0 |
