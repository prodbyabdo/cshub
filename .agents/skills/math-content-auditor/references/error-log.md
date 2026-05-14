# Math Content Error Log

Living record of all math errors found and fixed across CS Hub.
Update this file after every audit. Patterns here inform future audits.

## Error #1 — Wrong derivative expansion (2026-05-13)

- **File:** `year1sem2calc2.html` lines 672-679
- **What:** d/dx(sec x tan x) listed as `sec x(2tan²x + sec²x − 1)`
- **Root cause:** Applied tan²x = sec²x − 1 incorrectly during simplification
- **Correct:** `sec x(tan²x + sec²x)` = `sec x(2sec²x − 1)`
- **Also affected:** d/dx(csc x cot x) had the same pattern error
- **Category:** WRONG_EXPANSION

## Error #2 — Copy-paste answer box (2026-05-13)

- **File:** `calc2_mock_exam.html` line 1247
- **What:** Q69 answer box displayed `C) x = 4sinθ` (from Q62) instead of `C) √(x²−a²)`
- **Root cause:** MCQ block was duplicated from Q62, answer text not updated
- **Category:** COPY_PASTE

## Error #3 — Cross-reference contradiction (2026-05-13)

- **File:** `calc2_mock_exam.html` lines 1459-1466
- **What:** T/F Q84 marked `x = a tan θ for √(a²+x²)` as simply "True" despite course substitution table using `x = a sinh θ`
- **Root cause:** Question written without checking the reference sheet
- **Resolution:** Added clarification that both methods work but course prefers hyperbolic
- **Category:** CROSS_REFERENCE
