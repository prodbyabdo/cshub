# CS Hub — prodbyabdo

A static, GitHub Pages–hosted study hub for students of the **Faculty of Computer Science & Information Technology** at National University. Built with plain HTML, CSS, and vanilla JavaScript — no build step, no frameworks, no dependencies.

Live at → **[prodbyabdo.github.io/cshub](https://prodbyabdo.github.io/cshub)**

---

## What's Inside

| Section | Description |
|---|---|
| **Year 1–4** | Curriculum pages organised by year → semester → subject |
| **Subject Pages** | Per-subject pages with summaries, exam practice, worked examples, and curated video tutorials |
| **Resources** | Central library of YouTube playlists and references, grouped by subject area |
| **CS Wiki** | Topic stubs covering core CS disciplines (Algorithms, Databases, Networks, AI, etc.) |
| **Calculus** | Dedicated pages for Calculus I laws and worked solutions with MathJax rendering |

---

## Site Structure

```
/
├── index.html                    # Home — year selector
├── year1.html                    # Year 1 semester/subject browser
├── year2.html / year3.html / year4.html
│
├── year1sem1compapp.html         # Computer Applications (COM-111)
├── year1sem1calclaws.html        # Calculus I — Laws & Theorems
├── year1sem1calcsolutions.html   # Calculus I — Worked Solutions
├── year1sem1introcs.html         # Intro to Computer Science (COM115)
│
├── year1sem2introdbms.html       # Introduction to Databases (COM122)
├── year1sem2introprog.html       # Principles of Programming / Java (COM126)
├── year1sem2programmingjava.html # Java deep-dive content
├── year1sem2english.html         # English for Specific Purpose II
├── year1sem2filemgmt.html        # File Management (COM121)
├── year1sem2compmain.html        # Computer Maintenance (INF124)
│
├── resources.html                # Resource library (videos, references)
├── cs-wiki.html                  # CS Wiki index
├── wiki/                         # Wiki topic pages
│   ├── programming/
│   ├── databases/
│   ├── algorithms/
│   ├── data-structures/
│   ├── networks/
│   ├── operating-systems/
│   ├── computer-architecture/
│   ├── discrete-mathematics/
│   ├── software-engineering/
│   ├── ai/
│   ├── cybersecurity/
│   └── web-development/
│
├── calculus_laws.html            # Calculus law reference
├── calculus_solutions.html       # Calculus solution reference
└── unit_circle_trig.html         # Unit circle / trig reference
```

---

## Design System

- **Palette**: near-black background (`#0a0a0a`) with `#00ff88` green accent
- **Typography**: [Inter](https://fonts.google.com/specimen/Inter) for body, [JetBrains Mono](https://fonts.google.com/specimen/JetBrains+Mono) for code and labels
- **Math rendering**: [MathJax 3](https://www.mathjax.org/) on calculus pages
- **Code execution**: [OneCompiler](https://onecompiler.com/) embedded via `<iframe>` for Java examples
- No build process — all pages are static HTML with self-contained `<style>` blocks

---

## Running Locally

Just open any `.html` file in a browser, or serve the root with any static file server:

```bash
# Python
python -m http.server 8080

# Node (npx)
npx serve .
```

Then visit `http://localhost:8080`.

---

## Deployment

The site is deployed automatically via **GitHub Pages** from the `main` branch root. A `.nojekyll` file is included so GitHub Pages serves the files as-is without Jekyll processing.

---

## Contributing

This is a personal study resource. If you spot an error in content or a broken link, open an issue or submit a pull request.

---

*Made by [@prodbyabdo](https://linktr.ee/prodbyabdo)*
