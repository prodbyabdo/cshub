# Computer Maintenance (INF-128) — Build Plan

## Context Gathered

### Subject Info (`subjectinfo.json`)
- **Course**: Computer Maintenance, INF-128
- **Dates**: 2026-05-17 → 2026-06-06, Final Exam June 6
- **Instructors**: Dr. Mazin, Dr. Alsir, Dr. Basil, Dr. Wafa
- **15 Lectures (CL1–CL15)**, **13 Practicals (P1–P13)**, **6 Tests (T1–T6)**

### 4 Lecture DOCX Files Extracted
| File | Topic | Key Sections |
|------|-------|-------------|
| Lec1.docx | Introduction to Maintenance | Definition, importance, types (Reactive/Preventive/Predictive/Corrective), department responsibilities, safety, tools, documentation, key terms (MTBF/MTTR) |
| Lec2.docx | Safety in Maintenance + Common Hazards | PPE types, LOTO procedure, fire safety, emergency procedures, hazard types (mechanical/electrical/ergonomic/fire/slip), unsafe acts vs conditions, hazard control hierarchy |
| Lec3.docx | Types of Maintenance | Corrective, Preventive, Predictive, CBM, Breakdown, RCM — with comparison table, advantages/disadvantages, selection factors |
| Lec4.docx | Corrective & Predictive Maintenance (Deep Dive) | Immediate vs Deferred corrective, PdM monitoring techniques, corrective vs predictive comparison table, modern trends (AI, IoT, Digital Twins) |

### Existing State
- `year1sem2compmain.html` — Stub page with 2 placeholder sections, old monospace style
- `year1.html` line 451 — Links to `year1sem2compmain.html` with "Tutorials" button only
- `resources.html` — Has `computer-architecture-maintenance` in the keyword mapping but NO section in the HTML yet
- Course code mismatch: `year1.html` says `INF124`, `subjectinfo.json` says `INF-128`

---

## Plan

### Step 1: Rewrite `year1sem2compmain.html`
**Pattern**: Follow `year1sem2introdbms.html` scaffold (tabs, cards, color-coded sections, Inter+JetBrains Mono fonts, dark theme with accent colors).

**Structure**:
- **Header**: "Computer Maintenance" · INF-128 · Final Exam: June 6, 2026
- **Tabs**: `Subject Summary` | `Schedule` | `Exam Prep`

**Summary Tab** — 4 lecture sections:
1. **Lec 1 · Introduction to Maintenance** — Definition card, importance list, types grid (4 cards: Reactive/Preventive/Predictive/Corrective), key terms table (MTBF, MTTR, etc.)
2. **Lec 2 · Safety & Hazards** — PPE table, LOTO steps flow, hazard types grid (6 cards), fire extinguisher table
3. **Lec 3 · Maintenance Strategies** — 6 strategy cards (Corrective/Preventive/Predictive/CBM/Breakdown/RCM), comparison table, selection factors
4. **Lec 4 · Corrective vs Predictive Deep Dive** — Side-by-side comparison table, monitoring techniques list, modern trends badges (AI, IoT, Digital Twins)

**Schedule Tab** — Generated from `subjectinfo.json`:
- 7 day blocks, each with time/title/type/instructor rows
- Color-coded by type: CL=blue, P=green, T=gold

**Exam Prep Tab** — Assessment questions from lectures + placeholder for exam content

> [!IMPORTANT]
> To avoid token limit issues, write the file in **3 batches**:
> 1. Head + CSS + Header + Tab buttons + Lec1–2 content
> 2. Lec3–4 content + Schedule tab
> 3. Exam Prep tab + Scripts + close tags

### Step 2: Update `year1.html` Navigation
- Line 445–453: Update the INF124 card to show `INF-128`
- Change button from `Tutorials` to `Summary & Exam`
- Add second button linking to `resources.html#computer-maintenance`

### Step 3: YouTube Resource Manager
- Add a `computer-maintenance` section to `resources.html` (new `<section>` block)
- Update `KEYWORD_MAPPING` in `update_resources.py` to add `computer-maintenance` keywords: `maintenance, preventive, corrective, predictive, troubleshooting, hardware repair, disassembly, assembly, PPE, LOTO`
- The existing `computer-architecture-maintenance` key already has some relevant keywords — decide whether to reuse or create new section

---

## Execution Order
1. Write `year1sem2compmain.html` (3 batches)
2. Update `year1.html` card (single edit)
3. Add section to `resources.html` (single edit)
4. Update `update_resources.py` keyword mapping (single edit)
5. User tests in browser
