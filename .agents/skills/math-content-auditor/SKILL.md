---
name: math-content-auditor
description: >
  Audits mathematical content (formulas, solutions, reference tables, exam questions)
  across CS Hub HTML pages for correctness, consistency, and copy-paste errors.
  Use this skill whenever the user asks to audit, verify, check, or review math formulas,
  derivative/integral tables, exam solutions, mock exam answers, reference sheets,
  or any MathJax-rendered content in the CS Hub calculus or math pages.
  Also triggers when the user reports a suspected math error, asks to cross-check
  formulas between sections, or wants a quality pass on newly created math content
  like lecture notes, solution sets, or exam questions.
---

# CS Hub Math Content Auditor

Systematic workflow for verifying mathematical content across CS Hub HTML pages that use MathJax rendering.

## Scope

Target files (all in project root):

| Pattern | Content |
|---------|---------|
| `year1sem2calc2.html` | Main Calc II reference sheet (D↔I tables, standard integrals, substitution tables) |
| `year1sem2calc2lec*.html` | Lecture notes with formulas and worked examples |
| `year1sem2calc2lec*sol.html` | Solution sets |
| `calc2_mock_exam.html` | Mock exam with 90 questions and expandable solutions |
| `calculus_laws.html` | Calc I derivative/limit reference |
| `calculus_solutions.html` | Calc I worked solutions |

## Audit Workflow

### Phase 1 — Scope the audit

1. Identify which file(s) and section(s) need auditing (user may specify, or audit all)
2. Grep for MathJax content: search for `\\(` and `\\[` patterns to locate all formula blocks
3. Categorize formulas by type: derivatives, integrals, identities, worked solutions, answer boxes

### Phase 2 — Verify formulas

Apply these checks **in order** — each catches a different error class:

#### A. Reverse-differentiation check (for integral tables)
- For every stated antiderivative `∫f(x)dx = F(x) + C`, verify `d/dx[F(x)] = f(x)`
- Product-rule derivatives are especially error-prone (e.g., `d/dx(sec x tan x)`)

#### B. Numerical spot-check (for all formulas)
- Substitute a concrete value (e.g., `x=1`, `x=π/4` for trig) into both sides
- A mismatch instantly reveals algebraic errors without needing full symbolic verification
- For definite integrals, verify the final numerical answer

#### C. Identity expansion check (for simplified forms)
- When a formula uses a Pythagorean identity (`tan²x = sec²x − 1`, `cosh²x − sinh²x = 1`, etc.), expand fully and verify the simplification
- **Known pitfall**: `tan²x + sec²x ≠ 2tan²x + sec²x − 1` (the latter is a common mis-expansion)

#### D. Copy-paste check (for MCQ/exam answer boxes)
- Search all `.ans` div contents and verify each matches its question context
- Grep pattern: `<div class="ans">` — extract the text and cross-check with the question's `q-label`
- Flag any answer that references a different question number's content

#### E. Cross-reference consistency check
- Compare the substitution table in Section 5 against substitution usage in Q33/Q34/Q50 and T/F questions
- Compare the D↔I table entries against how the same formulas appear in lecture notes
- Flag when different equivalent forms are used without acknowledgment (e.g., `sinh⁻¹(x/a)` vs `ln|x+√(x²+a²)|`)

### Phase 3 — Report

Produce a structured report with:

| Column | Content |
|--------|---------|
| Location | File + line range or question number |
| Item | The specific formula or answer |
| Issue | What's wrong (with proof) |
| Severity | ❌ Error / ⚠️ Inconsistency / 💡 Suggestion |
| Fix | Corrected formula or text |

### Phase 4 — Apply fixes

- Fix errors directly in the HTML files
- For each fix, verify the MathJax LaTeX syntax is preserved correctly
- Use `\(` for inline and `\[` for display math — never break these delimiters

## Common Error Patterns

These are the error classes found in past audits. Check for all of them:

```
1. WRONG EXPANSION
   ❌ sec x(2tan²x + sec²x − 1)  →  expands to sec x(3sec²x − 3) = wrong
   ✅ sec x(tan²x + sec²x)       →  expands to sec x(2sec²x − 1) = correct

2. COPY-PASTE ANSWER
   ❌ Q69 answer box shows "C) x = 4sinθ" (from Q62)
   ✅ Q69 answer box should show "C) √(x²−a²)"

3. CROSS-REFERENCE CONTRADICTION
   ❌ T/F says "x = a tanθ for √(a²+x²)" is True, but course table uses x = a sinhθ
   ✅ Either change the T/F or clarify that both methods are valid

4. EQUIVALENT FORM INCONSISTENCY
   ⚠️ Section 5 uses sinh⁻¹(x/a), Section 7 uses ln|x+√(x²+a²)| for same integral
   ✅ Add a note explaining the equivalence, or unify the presentation
```

## MathJax Search Tips

MathJax in these files uses standard LaTeX. Grep patterns that work:

```powershell
# Find all trig derivative entries
Select-String -Path "year1sem2calc2.html" -Pattern "sec|csc|cot"

# Find all answer boxes in mock exam
Select-String -Path "calc2_mock_exam.html" -Pattern 'class="ans"'

# Find all display math blocks
Select-String -Path "*.html" -Pattern '\\\[' -Include "year1sem2calc2*.html"
```

Note: Standard `grep`/`ripgrep` may not match `\sec` because the backslash is a LaTeX command inside HTML, not a file-level escape. Use `Select-String` with literal patterns or search for the text without the backslash prefix.
