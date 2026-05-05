# CS Hub — Full Directory Context

> **Live site**: [prodbyabdo.github.io/cshub](https://prodbyabdo.github.io/cshub)
> **Repo**: `c:\Users\ben.arthur\Desktop\cshub-main`
> **Purpose**: Self-built Moodle replacement LMS for the Faculty of CS & IT at National University. **Designed 80% phone / 20% PC.**

---

## 1. Project Identity

| Field | Value |
|---|---|
| Stack | Pure HTML + CSS + Vanilla JS. **Zero build step, zero dependencies, zero frameworks.** |
| Hosting | GitHub Pages (static), `.nojekyll` present |
| Math rendering | MathJax 3 (CDN) on calculus pages |
| Code execution | OneCompiler embedded `<iframe>` for Java examples |
| Design system | Dark theme (`#0a0a0a` bg), `#00ff88` accent, Inter + JetBrains Mono |
| CSS approach | Self-contained `<style>` blocks in each HTML file (no shared CSS except `wiki/wiki.css`) |
| Target audience | CS & IT undergrads, Years 1–4 |

---

## 2. Directory Tree (Full)

```
cshub-main/
├── .git/
├── .gitignore                    # Excludes *.md, *.py, *.json, *.ini, previews, /cshub/
├── .nojekyll                     # Tells GitHub Pages to skip Jekyll
├── README.md                     # Project overview
│
├── index.html                    # HOME — year selector (01–04 + Resources + Wiki)
├── year1.html                    # Year 1 — semester picker → subject grid + search
├── year2.html                    # Year 2 (placeholder)
├── year3.html                    # Year 3 (placeholder)
├── year4.html                    # Year 4 (placeholder)
├── year1-preview.html            # Preview build (gitignored)
│
│ ┌── YEAR 1 SEMESTER 1 ──────────────────────────────────────────
├── year1sem1compapp.html         # COM-111 Computer Applications (resources + embedded videos)
├── year1sem1introcs.html         # COM-115 Intro to Computer Science
├── year1sem1calclaws.html        # MAT-114 Calculus I — Laws & Theorems (MathJax)
├── year1sem1calcsolutions.html   # MAT-114 Calculus I — Worked Solutions (MathJax, 203 KB)
│
│ ┌── YEAR 1 SEMESTER 2 ──────────────────────────────────────────
├── year1sem2calc2.html           # MAT-128 Calculus II — Complete Reference + lecture links (53 KB)
├── year1sem2calc2lec1.html       # Calc II Lecture 1: Basic Integration
├── year1sem2calc2lec1sol.html    # Calc II Lecture 1 Solutions
├── year1sem2calc2lec2.html       # Calc II Lecture 2: Substitution & Square Complement
├── year1sem2calc2lec2sol.html    # Calc II Lecture 2 Solutions
├── year1sem2calc2lec3.html       # Calc II Lecture 3: Integration by Parts & Tabular Method
├── year1sem2calc2lec3sol.html    # ...
├── year1sem2calc2lec4.html       # Calc II Lecture 4: Trigonometric Integrals
├── year1sem2calc2lec4sol.html    # ...
├── year1sem2calc2lec5.html       # Calc II Lecture 5: Partial Fractions
├── year1sem2calc2lec5sol.html    # ...
├── year1sem2calc2lec6.html       # Calc II Lecture 6: Trig & Clever Substitution
├── year1sem2calc2lec6sol.html    # ...
├── year1sem2calc2lec7.html       # Calc II Lecture 7: Areas Between Curves
├── year1sem2calc2lec7sol.html    # ...
├── year1sem2calc2lec8.html       # Calc II Lecture 8: Multiple & Triple Integrals
├── year1sem2calc2lec8sol.html    # ...
├── year1sem2introdbms.html       # COM-122 Intro to Databases (summary + exam + answer sheet; 58 KB)
├── year1sem2introprog.html       # COM-126 Principles of Programming / Java (153 KB, largest page)
├── year1sem2introprog_preview.html # Preview version
├── year1sem2programmingjava.html # Java deep-dive content (99 KB)
├── year1sem2english.html         # HMS-123 English for Specific Purpose II (41 KB)
├── year1sem2filemgmt.html        # COM-121 File Management
├── year1sem2compmain.html        # INF-124 Computer Maintenance
│
│ ┌── REFERENCE PAGES ────────────────────────────────────────────
├── calculus_laws.html            # Calculus law reference (standalone)
├── calculus_solutions.html       # Calculus solution reference (standalone)
├── unit_circle_trig.html         # Unit circle / trig reference
│
│ ┌── RESOURCES LIBRARY ──────────────────────────────────────────
├── resources.html                # MASSIVE (317 KB, 4732 lines). Sidebar + 14 categories of video cards
│                                 # with YouTube thumbnails, play buttons, badge system
│
│ ┌── CS WIKI ────────────────────────────────────────────────────
├── cs-wiki.html                  # Wiki index — Wikipedia-style article on "Computer" with TOC + infobox
│
├── wiki/
│   ├── wiki.css                  # Shared stylesheet for all wiki topic pages
│   ├── programming.html          # Category index with link-grid to subtopics
│   ├── programming/              # Subtopic pages (auto-generated from Wikipedia)
│   │   ├── computer-programming.html
│   │   ├── object-oriented-programming.html
│   │   ├── functional-programming.html
│   │   └── control-flow.html
│   ├── databases.html            # Category index
│   ├── databases/                # sql.html, database.html, relational-database.html, nosql.html
│   ├── algorithms.html           # Category index
│   ├── algorithms/               # algorithm.html, sorting-algorithm.html, sorting.html
│   ├── data-structures.html      # Category index
│   ├── data-structures/          # data-structure.html, linked-list.html, hash-table.html, trees.html
│   ├── networks.html             # Category index
│   ├── networks/                 # computer-network.html, tcp.html, osi-model.html, tcp-ip.html
│   ├── operating-systems.html    # Category index
│   ├── operating-systems/        # operating-system.html, process.html, memory-management.html, file-system.html
│   ├── computer-architecture.html # Category index
│   ├── computer-architecture/    # cpu.html, computer-architecture.html, etc.
│   ├── discrete-mathematics.html # Category index
│   ├── discrete-mathematics/     # discrete-mathematics.html, boolean-algebra.html, set-theory.html, graph-theory.html
│   ├── software-engineering.html # Category index
│   ├── software-engineering/     # software-engineering.html, agile.html, version-control.html, etc.
│   ├── ai.html                   # Category index
│   ├── ai/                       # artificial-intelligence.html, machine-learning.html, neural-network.html, search-algorithm.html
│   ├── cybersecurity.html        # Category index
│   ├── cybersecurity/            # computer-security.html, cryptography.html, network-security.html, malware.html
│   ├── web-development.html      # Category index
│   └── web-development/          # web-development.html, html.html, css.html, javascript.html
│
├── assets/
│   ├── online.png                # Favicon
│   ├── programming.png           # Decorative image
│   └── icons/                    # 16 SVG icons for subject categories
│       ├── ai.svg, apps.svg, back.svg, database.svg, dsa.svg, external.svg,
│       ├── intro-cs.svg, java.svg, maintenance.svg, math.svg, networks.svg,
│       ├── os.svg, play.svg, programming.svg, security.svg, software-eng.svg
│
├── scripts/
│   ├── data_fetching/
│   │   ├── fetch_wiki.py         # AUTO-GENERATES wiki pages from Wikipedia API (ranks by inlinks)
│   │   ├── fetch_new.py          # Fetch newer wiki content
│   │   └── extract_hiba.py       # Extract content from instructor PDFs
│   │
│   ├── maintenance/
│   │   ├── fix_calc.py           # Fix calculus page formatting
│   │   ├── fix_deeplinks.py      # Repair deep-link anchors (8 KB)
│   │   ├── fix_mobile.py         # Mobile compatibility fixes (11 KB)
│   │   ├── repair_onclick.py     # Fix onclick handlers (multiple iterations: 1-4)
│   │   ├── repair_onclick2.py
│   │   ├── repair_onclick3.py
│   │   ├── repair_onclick4.py
│   │   ├── scratch.py            # Scratch/temp maintenance script
│   │   └── verify.py             # Verification checks
│   │
│   └── utils/
│       ├── inject_videos.py      # Injects YouTube video cards into resources.html
│       ├── inject_deeplinks.py   # Adds deep-link anchors to pages
│       ├── update_html.py        # General HTML updater
│       ├── update_viewers.py     # Update viewer components
│       ├── convert_to_pdf.py     # HTML to PDF converter
│       └── process_playlist.py   # Process YouTube playlist JSON
│
├── data/
│   ├── csv/
│   │   └── newtempcsv.csv        # Temporary CSV data
│   ├── json/
│   │   ├── java_curriculum.json  # Java course structure (9 KB)
│   │   ├── java_playlist.json    # Java playlist data (17 KB)
│   │   ├── new_videos.json       # New videos to inject (4 KB)
│   │   ├── playlist_raw.json     # Raw YouTube playlist dump (572 KB)
│   │   └── scratch_topics.json   # Topic scratch data (38 KB)
│   └── txt/
│       └── hiba_extract.txt      # Extracted text from instructor
│
├── context/                      # Development context & reference docs
│   ├── audit_report.md           # Previous audit (15 KB)
│   ├── implementation_plan.md    # Master implementation plan (43 KB!)
│   ├── expanded_audit_plan.md    # Expanded audit plan
│   ├── codex chat.md             # Dev chat history (20 KB)
│   ├── java_lecture1_reference.html # Reference HTML for Java lectures
│   ├── calc2/                    # Calculus II source materials
│   │   ├── *.pdf, *.ppt, *.pptx # 29 files — lecture slides from instructor "Hiba"
│   │   ├── lec1.json             # Structured lecture data
│   │   ├── lec1q.json            # Questions data
│   │   └── timetable.json        # Course timetable
│   ├── introtoprog/              # Intro to Programming lecture notes (8 markdown files)
│   │   ├── introproglec1.md → introproglec8.md
│   └── updatingwiki/             # Wiki population management
│       ├── PROGRESS.md           # Tracks fetch status of 240+ Wikipedia articles
│       ├── TASK_FETCH.md         # Fetch task tracker
│       └── WIKI_POPULATION_GUIDE.md # How the wiki system works
│
├── contentforwiki/               # Raw Wikipedia category pages (saved HTML, gitignored)
│   └── Category_*.html + *_files/  # 10 categories with companion asset folders
│
├── scratch/                      # Temporary scratch files
│   ├── check_missing.py          # Check for missing pages
│   └── generate_calc2sol.py      # Generate calculus 2 solution pages
│
├── cshub/                        # Appears to be an older/separate git checkout (gitignored)
│   └── .git/
│
└── *.md (root)                   # Implementation plans (gitignored except README)
    ├── implementation_plan_unify_assets.md
    ├── implementation_plannewvids.md
    └── implementationasa_plan.md
```

---

## 3. Design System

### CSS Variables (repeated in every page's `<style>` block)

```css
:root {
    --bg-color: #0a0a0a;
    --card-bg: #111111;
    --panel-bg: #0f0f0f;           /* Used on sidebar/panels */
    --text-primary: #ffffff;
    --text-secondary: #a0a0a0;
    --accent-color: #00ff88;        /* Primary green accent */
    --accent-dim: rgba(0, 255, 136, 0.1);
    --accent-hover: rgba(0, 255, 136, 0.2);
    --border-color: #333333;
    --font-main: "Inter", sans-serif;
    --font-mono: "JetBrains Mono", monospace;
}
```

### Additional color tokens (subject pages like introprog, introdbms)

```css
--blue: #3b82f6;  --blue2: #60a5fa;  --red: #ef4444;
--green: #10b981;  --gold: #f59e0b;  --purple: #a855f7;
```

> [!WARNING]
> `resources.html` uses `--accent-color: #00c288` (slightly different green) while all other pages use `#00ff88`. This is an inconsistency.

### Fonts
- **Inter** (400, 600, 800) — body text, headings
- **JetBrains Mono** (400, 700) — code, labels, monospace UI elements
- Loaded from Google Fonts CDN on every page

### Component Patterns

| Pattern | Usage |
|---|---|
| `.card` with `.blue-glow`, `.red-glow`, `.green-glow`, `.gold-glow`, `.purple-glow` | Subject pages (colored border + gradient) |
| `.nav-back` | "← Back to X" navigation link (top-left on every page) |
| `.tab-btn` / `.tab-content` | Tab switching on subject pages (Summary / Exam / Answer Sheet) |
| `.print-btn` | "Print Full PDF" button (triggers `window.print()`) |
| `.resource-card` + `.resource-thumbnail` | Video cards in resources.html with YouTube thumbnail + play overlay |
| `.semester-btn` | Large semester selection buttons (year1.html) |
| `.subject-card` with `data-sem` + `data-search` | Searchable/filterable subject cards |
| `.formula-box`, `.important`, `.theorem` | Math content containers (Calculus pages) |
| `.stub-section` + `.link-grid` + `.link-card` | Wiki category indexes |
| Deep-linking script | Copied into every page — handles hash navigation + tab auto-open |

---

## 4. Page Architecture Taxonomy

### A. Home & Navigation (`index.html`, `year*.html`)
- Card grid for year selection
- year1.html has a **2-step drill-down**: semester picker → subject grid with search
- year2–4 are placeholder shells

### B. Subject Content Pages (the core LMS content)
Pattern: **Summary tab + Exam tab + Answer Sheet tab**

| Page | Subject Code | Content |
|---|---|---|
| `year1sem2introprog.html` | COM-126 | Biggest page (153 KB). Full programming course notes with code blocks, exam practice, embedded Java compiler |
| `year1sem2introdbms.html` | COM-122 | Database theory (DBMS types, SQL, normalization, ER diagrams) |
| `year1sem2english.html` | HMS-123 | English for Specific Purpose II |
| `year1sem1compapp.html` | COM-111 | Computer Applications resources |
| `year1sem2programmingjava.html` | — | Java deep-dive (99 KB) |

### C. Calculus Pages (MathJax-powered)
- `year1sem2calc2.html` — Master reference with all integration laws + links to 8 lectures
- `year1sem2calc2lec[1-8].html` — Individual lecture pages
- `year1sem2calc2lec[1-8]sol.html` — Corresponding solution pages
- `year1sem1calclaws.html` / `year1sem1calcsolutions.html` — Calc I reference pages
- All use MathJax 3 for LaTeX rendering

### D. Resources Library (`resources.html`)
- **317 KB, 4,732 lines** — the largest file
- Layout: **top nav → sidebar (desktop) / bottom chip strip (mobile) → content sections**
- 14 categories of YouTube video cards with thumbnails
- Mobile: sidebar hidden, replaced by horizontal scrolling chip nav + slide-out drawer
- Deep-linking supported (`#intro-to-cs`, `#java-tutorials`, `#calculus`, etc.)

### E. CS Wiki (`cs-wiki.html` + `wiki/`)
- Main article is a Wikipedia-style "Computer" overview with infobox + TOC
- 12 category indexes under `wiki/*.html` (programming, databases, algorithms, etc.)
- 50+ auto-generated subtopic pages fetched from Wikipedia via `fetch_wiki.py`
- Uses shared `wiki/wiki.css` (only shared CSS file in project)
- Rank system: pages ranked 1-6 by Wikipedia inlinks, only Rank ≤3 are generated

---

## 5. Tooling Pipeline

### Wiki Population System
```
fetch_wiki.py → Wikipedia API → rank by inlinks → generate HTML → update category index
                                                                 → update PROGRESS.md
```
- **240+ articles** tracked across 12 categories
- ~50 completed (Rank 1-3), ~5 skipped (Rank 4+), ~3 errors, rest pending
- Managed via `context/updatingwiki/PROGRESS.md` and `TASK_FETCH.md`

### Video Injection Pipeline
```
YouTube data (playlist_raw.json / new_videos.json) → inject_videos.py → resources.html
```
- Maps videos to sections by YouTube video ID
- Generates resource cards with thumbnails, badges, play buttons, channel links

### Maintenance Scripts
| Script | Purpose |
|---|---|
| `fix_deeplinks.py` | Repairs anchor IDs and deep-link navigation |
| `fix_mobile.py` | Mobile-specific CSS and layout fixes |
| `repair_onclick[1-4].py` | Iterative fixes for onclick handlers |
| `fix_calc.py` | Calculus page formatting repairs |
| `verify.py` | Verification checks |

### Content Generation
| Script | Purpose |
|---|---|
| `generate_calc2sol.py` | Auto-generates calculus 2 solution page HTML |
| `extract_hiba.py` | Extracts content from instructor PDFs |
| `convert_to_pdf.py` | HTML to PDF conversion |

---

## 6. Mobile-First Design Patterns

> [!IMPORTANT]
> The site is designed **80% phone / 20% PC**. Every page has mobile breakpoints.

### Common mobile patterns:
- `@media (max-width: 768px)` — primary breakpoint
- `@media (max-width: 600px)` / `@media (max-width: 420px)` — small phone
- `resources.html`: sidebar hidden on mobile, replaced by bottom chip strip + drawer
- All pages: reduced padding, smaller fonts, 2→1 column grid
- YouTube thumbnails: smaller aspect ratio on mobile
- Channel links hidden on mobile to save space
- Print styles: white background, black text, hidden nav/buttons

### Touch-friendly patterns:
- `.semester-btn` — large touch targets (60px padding)
- `.drawer-link` — 14px padding, easy tap
- `.mobile-nav-chip` — scrollable horizontal strip
- PDF download fallback links for iframes on mobile

---

## 7. Shared JavaScript Patterns

### Deep-Linking Script (copy-pasted into every page)
```javascript
(function () {
    function handleHash() {
        // Decode hash → find element → auto-open parent tab → smooth scroll
    }
    // Fires on DOMContentLoaded and hashchange
})();
```

### Tab System (subject pages)
```javascript
function openTab(tabId, btn) {
    // Hide all .tab-content, remove .active from .tab-btn
    // Show target tab, add .active to clicked button
}
```

### Semester/Subject Filtering (year1.html)
```javascript
function openSemester(semester) { /* Hide semester picker, show subject grid, filter by data-sem */ }
function filterSubjects() { /* Filter by data-search attribute, show/hide cards */ }
```

### Mobile Drawer (resources.html)
```javascript
function toggleMobileMenu() { /* Toggle .show on drawer + overlay */ }
function showSection(sectionId, navElement) { /* Switch content sections + update active nav */ }
```

---

## 8. Content Coverage Status

### Year 1 Semester 1 (5/7 subjects have content)
| Subject | Code | Status |
|---|---|---|
| Computer Applications | COM-111 | ✅ Full resources page |
| Principles of Info Systems | INF-112 | ❌ Placeholder (disabled link) |
| English for SP I | HMS-113 | ❌ Placeholder |
| Calculus I | MAT-114 | ✅ Laws + Solutions pages |
| Intro to Computer Science | COM-115 | ✅ Resources page |
| Discrete Mathematics | MAT-116 | ⚠️ Links to resources.html only |
| Principles of Economic | HMS-117 | ❌ Placeholder |

### Year 1 Semester 2 (7/8 subjects have content)
| Subject | Code | Status |
|---|---|---|
| File Management | COM-121 | ✅ Page exists |
| Intro to Databases | COM-122 | ✅ Full summary + exam + answers |
| Computer Maintenance | INF-124 | ✅ Page exists |
| English for SP II | HMS-123 | ✅ Full content (41 KB) |
| Principles of Accounting | HMS-125 | ❌ Placeholder |
| Principles of Programming | COM-126 | ✅ Massive (153 KB) with Java compiler |
| Algebra and Geometry | MAT-127 | ❌ Placeholder |
| Calculus II | MAT-128 | ✅ Full reference + 8 lectures + solutions |

### Years 2–4
❌ All placeholder pages (~3.4 KB each, same layout with "coming soon" content)

---

## 9. Key Technical Observations

> [!NOTE]
> **No shared CSS file** (except `wiki/wiki.css`). Every page has its own `<style>` block with the full design system copy-pasted. This means:
> - CSS variables are duplicated ~30+ times
> - Any design system change requires editing every file
> - The `assets/css/math-style.css` unification plan exists but hasn't been executed yet

> [!WARNING]
> **File sizes are large.** `resources.html` is 317 KB (4,732 lines), `year1sem2introprog.html` is 153 KB (2,952 lines). All content is inline — no lazy loading of sections, no code splitting.

> [!TIP]
> **Deep-linking script is duplicated** in every page (~45 lines each). Could be extracted to a shared JS file.

### Gitignore quirks
- `*.md` is gitignored (except README.md which is force-tracked)
- `*.py`, `*.json` are gitignored — scripts and data only exist locally
- `contentforwiki/` and `cshub/` are gitignored

---

## 10. File Size Summary

| File | Size | Lines |
|---|---|---|
| `resources.html` | 317 KB | 4,732 |
| `year1sem1calcsolutions.html` | 203 KB | — |
| `year1sem2introprog.html` | 153 KB | 2,952 |
| `year1sem2programmingjava.html` | 99 KB | — |
| `year1sem2introprog_preview.html` | 62 KB | — |
| `year1sem2introdbms.html` | 58 KB | 1,128 |
| `year1sem1calclaws.html` | 56 KB | — |
| `year1sem2calc2.html` | 53 KB | 1,167 |
| `year1sem2english.html` | 41 KB | — |
| `year1sem2calc2lec1.html` | 40 KB | — |
| All other pages | 3–25 KB | — |
