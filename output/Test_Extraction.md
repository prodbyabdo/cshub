# Calculus Rules Extracted

_Extracted from: CALC QUESTIONS ONLY.pdf_

---

## Page 5

### Theorem 1

> Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
> 6x+1
> 4. lim √
> x→∞ 4x2+3
> Sol
> (x−3)(2x+1)
> 5. lim
> x→∞ 2x2−x+1
> Sol
> (3x+4)(x−2)
> 6. lim
> x→∞x(2x+1)(x+2) T
> F
> ASol
> R
> D
> √
> 9x2+5
> 7. lim
> x→∞ x+3
> Sol
> 1.6 Cauchy’s Theorem
> Theorem 1.6.4 Cauchy’s Theorem:
> xn−an
> lim =nan−1
> x→a x−a
> proof
> 1 LIMIT OF THE FUNCTION (pg 9)

---

## Page 11

### Theorem 2

> Semester 1 - Calculus I(lec3) Faculty of Computer Science (CS+IT)
> 2.
> sin(π(0+ϵ)) sinπϵ sin0 0
> lim f(x)= limf(a+ϵ)= lim = lim = = =0
> x→0+ ϵ→0 ϵ→0 0+ϵ+1 ϵ→0 ϵ+1 0+1 1
> sin(π(0−ϵ)) sinπϵ
> lim f(x)= limf(a−ϵ)= lim = lim =π
> x→0− ϵ→0 ϵ→0 0−ϵ ϵ→0 ϵ
> ⇒ limf(x) not exist because lim f(x)̸= lim f(x)
> x→0 x→0+ x→0−
> Example 1.2.7 Find the constant such that the function is continuous on the entire real line.
> 1.
> (cid:40)
> 3x2 ,x≥1
> f(x)=
> ax−4 ,x<1
> 2.
> 
> 4sinx
>  ,x<0
> f(x)= x
> a−2x ,x≥0
> T
> F
> A
> R
> D
> 3.
> (cid:40)
> 1−4x ,x<2
> f(x)=
> ax2−3x+2 ,x≥2
> 1.3 Properties of Continuity
> Theorem 1.3.1 If b is a real number and f and g are continuous at x = c, then the following functions are
> also continuous at c
> 1. Scalar multiple: bf
> 2. Sum or Difference: f ±g
> 3. Product: fg
> f
> 4. Quotient: , if g(c)̸=0.
> g
> Note: The following types of functions are continuous at every point in their domains.
> (i) Polynomials
> 1 THE CONTINUITY (pg 3)

---

## Page 13

### Theorem 3

> Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec3)
> Theorem 2.4.4 Quotient Rule
> f
> If f and g are differentiable at x , g(x)̸=0, then the derivative of at x exists and
> g
> d (cid:20) f(x) (cid:21) g(x)f′(x)−g′(x)f(x)
> =
> dx g(x) (g(x))2
> Proof
> f(x+h) f(x)
> −
> (cid:20) (cid:21)
> d f(x) g(x+h) g(x) g(x)f(x+h)−f(x)g(x+h)
> = lim = lim
> dx g(x) h→0 h h→0 h(g(x)g(x+h))
> g(x)f(x+h)−f(x)g(x+h)−f(x)g(x)+f(x)g(x)−f(x)g(x+h)
> = lim
> h→0 h(g(x)g(x+h))
> g(x)[f(x+h)−f(x)] f(x)[g(x+h)−g(x)]
> lim − lim
> = h→0 h h→0 h
> lim(g(x)g(x+h))
> h→0
> [f(x+h)−f(x)] [g(x+h)−g(x)]
> g(x) lim −f(x) lim
> = h→0 h h→0 h
> lim(g(x)g(x+h))
> h→0
> g(x)f′(x)−g′(x)f(x)
> =
> (g(x))2
> Note: lim g(x+h)=g(x) because g is given differentiable and therefore is continuous.
> h→0
> 5. The Chain Rule T
> F
> Theorem 2.4.5 If y =f(u) is a differentiableAfunction of u, and u=g(x) is a differentiable function of
> x, then y =f(g(x)) is a differentiable functiRon of x and
> D
> d
> ′ ′
> [f(g(x))]=f (g(x)).g (x)
> dx
> dy
> Example 2.4.15 Evaluate for the following functions.
> dx
> 3 √
> 1. y =4x3+ +2 x−7
> x
> Sol
> 1
> 2. y =3cosx− sinx
> 2
> Sol
> 1 1 √
> 3. y =x7+ x−2− √ + x3
> 3 x
> Sol
> (pg 10) 2 THE DIFFERENTIATION

---
