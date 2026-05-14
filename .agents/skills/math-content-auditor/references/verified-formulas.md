# Calc II — Known-Correct Reference Formulas

Use this file as ground truth when auditing CS Hub math content.
Every formula below has been manually verified.

## Standard Trig Derivatives

| f(x) | f'(x) |
|------|--------|
| sin x | cos x |
| cos x | −sin x |
| tan x | sec²x |
| cot x | −csc²x |
| sec x | sec x tan x |
| csc x | −csc x cot x |
| sec²x | 2 sec²x tan x |
| csc²x | −2 csc²x cot x |
| sec x tan x | sec x(tan²x + sec²x) = sec x(2sec²x − 1) |
| csc x cot x | −csc x(cot²x + csc²x) = −csc x(2csc²x − 1) |

### Derivation of d/dx(sec x tan x)

```
d/dx(sec x tan x) = sec x tan x · tan x + sec x · sec²x
                   = sec x tan²x + sec³x
                   = sec x(tan²x + sec²x)
Using tan²x = sec²x − 1:
                   = sec x(sec²x − 1 + sec²x)
                   = sec x(2sec²x − 1)  ✓
```

## Hyperbolic Derivatives

| f(x) | f'(x) |
|------|--------|
| sinh x | cosh x |
| cosh x | sinh x |
| tanh x | sech²x |
| coth x | −csch²x |
| sech x | −sech x tanh x |
| csch x | −csch x coth x |
| sech²x | −2 sech²x tanh x |
| csch²x | 2 csch²x coth x |

## Six Standard Integrals (Lecture 4)

| # | Integral | Result |
|---|----------|--------|
| 1 | ∫ dx/√(a²−x²) | sin⁻¹(x/a) + C |
| 2 | ∫ √(a²−x²) dx | (a²/2)sin⁻¹(x/a) + (x/2)√(a²−x²) + C |
| 3 | ∫ dx/√(a²+x²) | sinh⁻¹(x/a) + C |
| 4 | ∫ √(a²+x²) dx | (x/2)√(a²+x²) + (a²/2)sinh⁻¹(x/a) + C |
| 5 | ∫ dx/√(x²−a²) | cosh⁻¹(x/a) + C |
| 6 | ∫ √(x²−a²) dx | (x/2)√(x²−a²) − (a²/2)cosh⁻¹(x/a) + C |

## Substitution Table (Course Standard)

| Expression | Substitution | Identity |
|-----------|-------------|----------|
| √(a²−x²) | x = a sin θ | 1 − sin²θ = cos²θ |
| √(a²+x²) | x = a sinh θ | 1 + sinh²θ = cosh²θ |
| √(x²−a²) | x = a cosh θ | cosh²θ − 1 = sinh²θ |

**Note:** x = a tan θ also works for √(a²+x²) via 1 + tan²θ = sec²θ, but this course's standard table uses the hyperbolic form.

## Equivalent Forms (ln vs inverse hyperbolic)

These pairs are equivalent and differ only by a constant absorbed into C:

```
sinh⁻¹(x/a) = ln|x + √(x² + a²)| − ln a
cosh⁻¹(x/a) = ln|x + √(x² − a²)| − ln a
```

When both forms appear in the same document, add a note explaining the equivalence.

## Inverse Trig Derivatives (with parameter a)

| f(x) | f'(x) |
|------|--------|
| sin⁻¹(x/a) | 1/√(a²−x²) |
| tan⁻¹(x/a) | a/(a²+x²) |
| sec⁻¹(x/a) | a/(|x|√(x²−a²)) |

## Inverse Trig Integrals (IBP-derived)

| f(x) | ∫ f(x) dx |
|------|-----------|
| sin⁻¹(x/a) | x·sin⁻¹(x/a) + √(a²−x²) + C |
| tan⁻¹(x/a) | x·tan⁻¹(x/a) − (a/2)·ln(a²+x²) + C |
| sec⁻¹(x/a) | x·sec⁻¹(x/a) − a·ln|x + √(x²−a²)| + C |
