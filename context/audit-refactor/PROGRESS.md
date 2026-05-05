# Audit Refactor — Progress Tracker

**Branch**: `audit-refactor`  
**Created**: 2026-05-05  
**Baseline Score**: 10/20

---

## Architecture

```
main (production) ← DO NOT TOUCH
  └── audit-refactor (this branch)
        ├── Foundation commit (shared assets) ✅ DONE
        │   ├── assets/css/global.css
        │   ├── assets/js/deeplink.js
        │   └── assets/js/tabs.js
        │
        ├── Agent 1: Navigation pages
        ├── Agent 2: Resources library
        ├── Agent 3: Calculus pages
        └── Agent 4: Subject + Wiki pages
```

---

## Agent Status

| Agent | Scope | Files | Status | Progress |
|-------|-------|-------|--------|----------|
| **Foundation** | Shared CSS/JS | 3 new | ✅ Done | 3/3 |
| **Agent 1** | `index.html`, `year1-4.html` | 5 files | ⬜ Not started | 0/5 |
| **Agent 2** | `resources.html` | 1 file (317KB) | ⬜ Not started | 0/1 |
| **Agent 3** | Calculus pages + `math-style.css` | 20 files + 1 new | ⬜ Not started | 0/20 |
| **Agent 4** | Subject pages + Wiki | 10 + wiki/* | ⬜ Not started | 0/10 |

---

## Detailed Progress

### Foundation (✅ Complete)
- [x] `assets/css/global.css` — 400+ lines of shared design system
- [x] `assets/js/deeplink.js` — Extracted deep-linking IIFE
- [x] `assets/js/tabs.js` — Extracted openTab + print helpers
- [x] Task MDs created for all 4 agents
- [x] Initial commit on `audit-refactor` branch

### Agent 1 — Navigation Pages
> Task file: `context/audit-refactor/TASK_1_NAVIGATION.md`

- [ ] 1.1 — Link shared assets to all 5 files
- [ ] 1.2 — CSS deduplication (remove inline `:root`, body, nav-back, etc.)
- [ ] 1.3 — Accessibility (meta desc, semantic buttons, ARIA, favicon)
- [ ] 1.4 — Typography (remove gradient text, fix btn-primary/secondary)
- [ ] 1.5 — Visual verification

**Notes from agent**:
> _(agent writes status notes here)_

### Agent 2 — Resources Library
> Task file: `context/audit-refactor/TASK_2_RESOURCES.md`

- [ ] 2.1 — Link shared assets
- [ ] 2.2 — Fix accent color mismatch (#00c288 → #00ff88)
- [ ] 2.3 — CSS deduplication
- [ ] 2.4 — Replace ~100 inline styles with `.channel-link` class
- [ ] 2.5 — Accessibility (semantic nav, ARIA, alt text on ~100 images)
- [ ] 2.6 — Content fixes (misplaced chemistry video, empty href, nested badge-row)
- [ ] 2.7 — Mobile drawer ARIA toggle
- [ ] 2.8 — Visual verification

**Notes from agent**:
> _(agent writes status notes here)_

### Agent 3 — Calculus Pages
> Task file: `context/audit-refactor/TASK_3_CALCULUS.md`

- [ ] 3.1 — Create `assets/css/math-style.css`
- [ ] 3.2 — Link shared assets to all 20 files
- [ ] 3.3 — CSS deduplication across all 20 files
- [ ] 3.4 — Accessibility (ARIA, alt text, table wraps, iframe titles)
- [ ] 3.5 — Navigation consistency audit (all back-links correct)
- [ ] 3.6 — Visual verification

**Notes from agent**:
> _(agent writes status notes here)_

### Agent 4 — Subject + Wiki Pages
> Task file: `context/audit-refactor/TASK_4_SUBJECTS_WIKI.md`

- [ ] 4.1 — Link shared assets to all subject pages
- [ ] 4.2 — CSS deduplication (heaviest — introprog has 800+ lines of CSS)
- [ ] 4.3 — Accessibility (tab ARIA, iframe titles, table wraps)
- [ ] 4.4 — Wiki pages (cs-wiki.html → link global.css, fix wiki/wiki.css)
- [ ] 4.5 — Table overflow fix (introprog + introdbms)
- [ ] 4.6 — Preview files assessment
- [ ] 4.7 — Visual verification

**Notes from agent**:
> _(agent writes status notes here)_

---

## Merge Checklist (after all agents complete)

- [ ] All 4 agents report ✅ status
- [ ] `git diff --stat` shows expected file changes
- [ ] No merge conflicts between agent changes
- [ ] Full visual test on mobile (375px) — all pages
- [ ] Full visual test on desktop (1440px) — all pages
- [ ] Run re-audit to calculate new score (target: 16+/20)
- [ ] Squash/clean commits if needed
- [ ] Merge `audit-refactor` → `main`
- [ ] Push and verify GitHub Pages deployment

---

## Conflict Resolution Rules

If two agents accidentally edit the same file:
1. **First committed wins** — the second agent rebases on top
2. **`assets/**` is read-only** — no agent modifies foundation files after initial commit
3. **If a global.css change is needed** — agent notes it in their progress section, main orchestrator (you) makes the change

---

## Audit Scoring (Re-run After Merge)

| Dimension | Before | Target |
|-----------|--------|--------|
| Accessibility | 1/4 | 3/4 |
| Performance | 2/4 | 3/4 |
| Theming | 2/4 | 4/4 |
| Responsive | 3/4 | 4/4 |
| Anti-Patterns | 2/4 | 3/4 |
| **Total** | **10/20** | **17/20** |
