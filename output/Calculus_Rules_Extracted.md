# Calculus Rules Extracted

_Extracted from: CALC MERGED.pdf_

---

## Page 1

### Definition 1

> Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
> Lecture Two
> 1 Limit of the Function
> 1.1 Introduction
> x3−1
> Giventhefunctionf(x)= , clearlyitisnotdefinedatx=1, andwewanttostudythebehaviourofthis
> x−1
> function when x approaches to 1.
> y
> 5
> 4 x3−1
> y =
> 3 x−1
> 2
> 1
> x
> -4 -3 -2 -1 1 2 3 4
> -1
> -2
> The following table shows:
> T
> x 0.75 0.F9 0.99 0.999
> f(x) 2.313 A2.710 2.970 2.997
> FrRom the left
> D
> x 1.001 1.01 1.1 1.25
> f(x) 3.003 3.030 3.310 3.813
> From the right
> We can move arbitrarily close to 1 and as a result f(x) moves arbitrarily close to 3, and here we can say the
> x3−1
> limit of the function f(x)= is 3 when x goes to 1. This limit is written as:
> x−1
> x3−1
> lim =3
> x→1 x−1
> In general: If f(x) becomes arbitrarily close to a single number L as x approaches c from either sides, the
> limit of f(x) as x approaches c is L,and we can write it as:
> limf(x)=L
> x→c
> 1.2 Definition of limit
> Let f be a function defined on an open interval containing c (except possibly at c) and let L be a real number.
> The statement limf(x) = L means that for each ϵ > 0 there exist δ > 0 such that if 0 < |x−c| < δ, then
> x→c
> |f(x)−L|<ϵ.
> Example 1.2.1 Prove that lim(2x+3)=9.
> x→3
> Proof
> Wemustshowthatforeachϵ>0,thereexistsaδ >0suchthat|(2x+3)−9|<ϵwhenever0<|x−3|<δ,because
> our choice of δ depends on ϵ. Now we need to establish a connection between the absolute value |(2x+3)−9|
> and |x−3|.
> |(2x+3)−9|=|2x−6|=2|x−3|
> 1 LIMIT OF THE FUNCTION (pg 1)

---

## Page 3

### Theorem 2

> Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
> x2+x−2
> 2. R-H-L: lim
> x→1+ x−1
> x2+x−2 (1+ϵ)2+(1+ϵ)−2 1+2ϵ+ϵ2+1+ϵ−2 ϵ(ϵ+3)
> lim = lim = lim = lim
> x→1+ x−1 ϵ→0 (1+ϵ)−1 ϵ→0 ϵ ϵ→0 ϵ
> =lim(ϵ+3)=0+3=3
> ϵ→0
> Since R-H-L = L-H-L, the limit exists and equal to 3.
> 1.4 Properties of Limits
> Theorem 1.4.1 Let b and c be real numbers and let n be a positive integer.
> 1.
> limb=b
> x→c
> 2.
> limx=c
> x→c
> 3.
> limxn =cn
> x→c
> Example 1.4.4 Evaluate the limits
> 1.
> lim3=3
> x→2
> T
> 2.
> F
> lim x=−4
> A
> x→−4
> R
> 3.
> D
> limx2 =(2)2 =4
> x→2
> Theorem 1.4.2 Let b and c be real numbers and let n be a positive integer, and let f and g be functions with
> the following limits.
> limf(x)=L , limg(x)=K
> x→c x→c
> then
> 1. Scalar multiple
> lim[bf(x)]=blimf(x)=bL
> x→c x→c
> 2. Sum or Difference
> lim[f(x)±g(x)]= limf(x)± limg(x)=L±K
> x→c x→c x→c
> 3. Product
> lim[f(x).g(x)]= limf(x).limg(x)=L.K
> x→c x→c x→c
> 4. Quotient
> f(x) lim f(x) L
> lim = x→c = ,K ̸=0
> x→c g(x) lim x→c g(x) K
> 5. Power
> (cid:104) (cid:105)n
> lim[f(x)]n = limf(x) =Ln.
> x→c x→c
> Example 1.4.5 By using theorems of limits evaluate the following limits.
> 1. lim(4x2+3)
> x→2
> Sol
> 1 LIMIT OF THE FUNCTION (pg 3)

---

## Page 6

### Theorem 3

> Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)
> 1.5 Strategies for Finding Limits
> Previously, we studied several types of functions whose limits can be evaluated by direct substitution, this
> knowledge together with the following theorem can be used to develop a strategy for finding limits.
> Theorem 1.5.3 Let c be a real number and let f(x) = g(x) for all x ̸= c in an open interval containing c. If
> the limit of g(x) as x approaches c exists, then the limit of f(x) also exists and:
> limf(x)= limg(x)
> x→c x→c
> Example 1.5.7 Evaluate the following limits:
> x2−x−2
> 1. lim
> x→2 x2−4
> Sol
> By direct substitution, we get:
> (2)2−2−2 4−2−2 0
> = = (undetermined value)
> (2)2−4 4−4 0
> Now we try to find a function g that agrees with f for all x other than x = 2. By factoring and dividing
> out like factors, we can rewrite the given function as:
> x2−x−2 (cid:24)(x(cid:24)−
> (cid:24)(cid:24)
> 2)(x+1) x+1
> f(x)=
> x2−4
> =
> (cid:24)(x(cid:24)−
> T (cid:24)(cid:24)
> 2)(x+2)
> =
> x+2
> =g(x).
> F
> A
> So for all x−values other than x = 2 the functions f and g agree, since limg(x) exists, we can apply
> R
> x→2
> theorem 1.5.3 to conclude that f and g hDave the same limit at x=2.
> x2−x−2 (x−2)(x+1) x+1 2+1 3
> lim = lim = lim = =
> x→2 x2−4 x→2(x−2)(x+2) x→2x+2 2+2 4
> x3−1
> 2. lim
> x→1 x−1
> Sol
> (1)3−1 0
> By direct substitution we get = . Then we try to find a function g that agrees with f for all x
> 1−1 0
> other than x=1.
> (x2+x+1)≡g(x)
> x3−1
> (x−1)
> x3−1 (x−1)(x2+x+1)
> f(x)= = =(x2+x+1)=g(x)
> x−1 (x−1)
> Thus limf(x)= limg(x)= lim(x2+x+1)=12+1+1=3.
> x→1 x→1 x→1
> x3−1
> Note that: the graph of the function g(x)=x2+x+1 is same as f(x)=
> x−1
> (pg 6) 1 LIMIT OF THE FUNCTION

---

## Page 9

### Theorem 4

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

## Page 10

### Lemma 5

> Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)
> By using long division, we get:
> xn−an
> =xn−1+axn−2+a2xn−3+···+an−1
> x−a
> Therefore:
> lim
> xn−an
> = lim
> (cid:0) xn−1+axn−2+a2xn−3+···+an−1(cid:1)
> x→a x−a x→a
> = an−1+a×an−2+a2×an−3+···+an−1
> = an−1+an−1+an−1+···+an−1 =nan−1
> (cid:124) (cid:123)(cid:122) (cid:125)
> n times
> Lemma 1.6.1
> xn−an n
> lim = an−m
> x→axm−am m
> proof
> xn−an xn−an xm−am
> We can write f(x)= = ÷ . Then the limit will be:
> xm−am x−a x−a
> xn−an xn−an xm−am nan−1 n
> lim = lim ÷ lim = = an−m.
> x→axm−am x→a x−a x→a x−a mam−1 m
> Lemma 1.6.2
> x−a 1
> lim = a1−m
> x→axm−am m
> Proof left for you.
> Example 1.6.9 Evaluate the following limits.
> T
> x5−32
> 1. lim F
> x→2 x3−8
> A
> RSol
> D
> x5−32 x5−(2)5 5 5 20
> lim = lim = (2)5−3 = (2)2 = .
> x→2 x3−8 x→2x3−(2)3 3 3 3
> x2−16
> 2. lim √
> x→4x x−8
> Sol
> x2−16 x2−(4)2 2 4 8
> lim √ = lim = (4)2−3 2 = (2)=
> x→4x x−8 x→4x3
> 2
> −(4)3
> 2
> 3
> 2
> 3 3
> √ √
> x+∆x− x
> 3. lim
> ∆x→0 ∆x
> Sol
> √ √
> lim x+∆x− x = lim (x+∆x)1 2 −x1 2 = 1 x1 2 −1 = 1 x− 2 1 = √ 1
> ∆x→0 ∆x x+∆x→x (x+∆x)−x 2 2 2 x
> x−3
> 4. lim
> x→3x3−27
> Sol
> x−3 x−3 1 1 1 1
> lim = lim = (3)1−3 = . = .
> x→3x3−27 x→3x3−(3)3 3 3 9 27
> x3+1
> 5. lim
> x→−1 x+1
> Sol
> x3+1 x3−(−1)3
> lim = lim =3(−1)3−1 =3(−1)2 =3.
> x→−1 x+1 x→−1 x−(−1)
> (pg 10) 1 LIMIT OF THE FUNCTION

---

## Page 11

### Theorem 6

> Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
> 1.7 The squeeze Theorem
> Theorem 1.7.5 Assume the functions f,g and h satisfy f(x)≤g(x)≤h(x) for all values of x near a, except
> possibly at a.
> If lim f(x)= lim h(x)=L, then lim g(x)=L
> x→a x→a x→a
> 1.8 Limit of Trigonometric Functions
> We have some important limits:
> 1. limsinx=0
> x→0
> 2. limcosx=1
> x→0
> T
> sinx F
> 3. lim =1 A
> x→0 x
> R
> sinax D
> 4. lim =1
> ax→0 ax
> tanx
> 5. lim =1
> x→0 x
> tanax
> 6. lim =1
> ax→0 ax
> tanx
> Example 1.8.10 1. Prove that lim =1
> x→0 x
> Sol
> tanx sinx sinx 1 1
> lim = lim = lim .lim =1× =1×1=1
> x→0 x x→0xcosx x→0 x x→0cosx cos0
> sin2x
> 2. lim
> x→0 x
> Sol
> sin2x 2sin2x sin2x
> lim = lim =2 lim =2×1=2
> x→0 x 2x→0 2x 2x→0 2x
> tan3x
> 3. lim
> x→0 2x
> Sol
> tan3x 1 tan3x 1 3tan3x 3 tan3x 3 3
> lim = lim = lim = lim = ×1= .
> x→0 2x 2x→0 x 23x→0 3x 23x→0 3x 2 2
> 1 LIMIT OF THE FUNCTION (pg 11)

---

## Page 13

### Theorem 7

> Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
> 1.10 The Exponential Theorem
> Theorem 1.10.6
> x2 x3 (cid:88) ∞ xn
> ex =1+x+ + +···=
> 2 3 n!
> n=0
> Proof
> (cid:18)
> 1
> (cid:19)n
> We know that e= lim 1+ .
> n→∞ n
> (cid:20) (cid:18)
> 1
> (cid:19)n(cid:21)x (cid:18)
> 1
> (cid:19)nx
> ⇒ex = lim 1+ = lim 1+
> n→∞ n n→∞ n
> (cid:16) x(cid:17)m
> put m=nx⇒ex = lim 1+ , therefore the limit will be:
> m→∞ m
> (cid:20) mx m(m−1) x2 m(m−1)(m−2) x3 (cid:21)
> ⇒ lim 1+ + + +...
> m→∞ m 2! m2 3! m3
>  (cid:18) 1 (cid:19) (cid:18) 1 (cid:19)(cid:18) 2 (cid:19) 
> 1− 1− 1−
>  m m m 
> = lim 1+x+ + +...
> m→∞ 2! 3! 
> x2 x3
> = 1+x+ + +...
> 2! 3!
> 1
> Example 1.10.11 1. lim(1+x)x
> x→0 T
> F
> ASol
> R
> 1 1
> put u= ⇒x= and u→∞ as x→D0
> x u
> 1
> (cid:18)
> 1
> (cid:19)u
> lim(1+x)x = lim 1+ =e.
> x→0 u→∞ u
> (cid:16) α(cid:17)x
> 2. lim 1+ α̸=0
> x→∞ x
> Sol
> (i) If α>0, let x=αu
> (cid:16) α(cid:17)x (cid:16) α (cid:17)αu (cid:18) (cid:18) 1 (cid:19)u(cid:19)α
> lim 1+ = lim 1+ = lim 1+ =eα.
> x→∞ x u→∞ αu u→∞ u
> (ii) If α<0⇒ let x=−αu
> (cid:16) α(cid:17)x (cid:16) α (cid:17)−αu (cid:32) (cid:18) 1 (cid:19)−u (cid:33)α (cid:18) (cid:18) u (cid:19)u(cid:19)α
> lim 1+ = lim 1− = lim 1− = lim
> x→∞ x u→∞ αu u→∞ u u→∞ u−1
> (cid:20) (cid:18)
> 1
> (cid:19)u(cid:21)α
> = lim 1+
> u→∞ u−1
> Now let u−1=y ⇒u=1+y (y →∞ as u→∞.
> (cid:16) α(cid:17)x (cid:20) (cid:18) 1 (cid:19)u(cid:21)α (cid:34) (cid:18) 1 (cid:19)y+1 (cid:35)α
> lim 1+ = lim 1+ = lim 1+
> x→∞ x u→∞ u−1 y→∞ y
> (cid:20) (cid:18)
> 1
> (cid:19)y (cid:18)
> 1
> (cid:19)(cid:21)α
> = lim 1+ × lim 1+ =(e×1)α =eα.
> y→∞ y y→∞ y
> 1 LIMIT OF THE FUNCTION (pg 13)

---

## Page 19

### Definition 8

> Semester 1 - Calculus I(lec3) Faculty of Computer Science (CS+IT)
> Lecture Three
> 1 The Continuity
> 1.1 Continuity at a point on an open interval
> Informally, we might say that a function is continuous on an open interval if its graph can be drawn with a
> pencil without lifting the pencil from the paper. i.e. A function f is continuous at x = c means there is no
> interruption in the graph of f at c. That is, its graph is unbroken at c and there are no holes, jumps, or gaps.
> The following figure identifies three values of x at which the graph of f is not continuous. At all other points
> in the interval (a,b) the graph of f is uninterrupted and continuous.
> Figure 1: Three cases for the discontinuity
> T
> F
> A
> 1.2 Concept of Continuity R
> D
> Definition 1.2.1 Continuity at a point:
> A function f is continuous at c if the following three conditions are met.
> 1. f(c) is defined
> 2. limf(x) exists.
> x→c
> 3. f(c)= limf(x)
> x→c
> Continuity on an open interval:
> A function is continuous on an open interval (a,b) if it is continuous at each point in the interval.
> Definition 1.2.2 Let f(x) be a defined function at x = c, we say that f(x) is continuous at x = c if the
> following condition satisfied.
> lim [f(c+h)−f(c)]=0
> h→0
> Example 1.2.1 Given f(x)=x2, prove that it is continuous on R.
> Proof
> To prove the function is continuous on R, choose an arbitrary point x=c, s.t c∈R.
> lim [f(c+h)−f(c)]= lim
> (cid:2) f(c+h)2−c2(cid:3)
> = lim
> (cid:2) c2+2ch+h2−c2(cid:3)
> h→0 h→0 h→0
> = lim [h(2c+h)]=0×(2c+0)=0.
> h→0
> ⇒f(x)=x2 is continuous at c⇒ continuous at R.
> Example 1.2.2 Prove that the function f(x)=cosax, continuous on R.
> Proof
> 1 THE CONTINUITY (pg 1)

---

## Page 21

### Theorem 9

> Semester 1 - Calculus Ile(c3) yacultFof teCompur Science (CS+IT)
> 2.
> sin((cid:25)(0+(cid:15))) sin(cid:25)(cid:15) sin0 0
> lim f(x)= lim f(a+(cid:15))= lim = lim = = =0
> x!0 + (cid:15)!0 (cid:15)!0 0+(cid:15)+1 (cid:15)!0 (cid:15)+1 0+1 1
> sin((cid:25)(0(cid:0)(cid:15))) sin(cid:25)(cid:15)
> lim f(x)= lim f(a(cid:0)(cid:15))= lim = lim =(cid:25)
> x!0 (cid:0) (cid:15)!0 (cid:15)!0 0(cid:0)(cid:15) (cid:15)!0 (cid:15)
> ) lim f(x) not existauseceb mli f(x)6= lim f(x)
> x!0 x!0 + x!0 (cid:0)
> Example 1.2.7 Find the onstantc such that the function is sontinuouc on the eentiralerline.
> 1. (
> 3x 2 ;x(cid:21)1
> f(x)=
> ax(cid:0)4 ;x<1
> 2. 8
> < 4sinx
> ;x<0
> f(x)= x
> :
> a(cid:0)2x ;x(cid:21)0
> DRAFT
> 3. (
> 1(cid:0)4x ;x<2
> f(x)=
> ax 2 (cid:0)3x+2 ;x(cid:21)2
> 1.3 Properties of yuittinCon
> Theorem 1.3.1 If b is aalerernumb and f and g earontinuousc at x = c, then the following functions ear
> also ontinuousc at c
> 1. alarSc tple:muli bf
> 2. Sum ore:encDi(cid:11)er f (cid:6)g
> 3. duct:oPr fg
> f
> 4. Quotient: , if g(c)6=0.
> g
> Note: Teh wingfollopytes of functions areuoustinconat eryev ptoin in their domains.
> (i) olynomialsP
> 1 THE CONTINUITY (pg 3)

---

## Page 24

### Theorem 10

> yacultFof Comuterp Science (CS+IT) Semester 1 - Calculus I(lec3)
> f(x+h)(cid:0)f(x)
> omfr example 2.1.8, we saw that =3x 2 +3hx+h 2
> h
> L:S:L= lim (3x 2 +3hx+h 2 )= lim (3x 2 +3hx+h 2 )=3x 2 :
> h!0 + h!0
> R:S:L= lim (3x 2 +3hx+h 2 )= lim (3x 2 +3hx+h 2 )=3x 2
> h!0 (cid:0) h!0
> dy
> eeforTher =3x 2
> dx
> dy
> Example 2.2.10 orFthe function y =jxj, (cid:12)nd at x=0.
> dx
> Sol
> We know that, the given function is ontinuousc on R.
> dy f(0+h)(cid:0)f(0) f(h)(cid:0)0 f(h)
> = lim = lim = lim
> dx h!0 h h!0 h h!0 h
> Now, we will study the eexistenc of the limit by alculatingc the left and right limits.
> jhj h
> (i) L:S:L= lim = lim =(cid:0)1
> h!0 (cid:0) h h!0 (cid:0)h
> jhj h
> (ii) L:S:L= lim = lim =1
> h!0 + h h!0 h
> Thus the limit esdo not exist at x=0 and eher we say the function is not entiabledi(cid:11)er at x=0.
> Theorem 2.2.2 entiableDi(cid:11)er implies ontinuousc
> ofoPr
> ausecBef is entableidi(cid:11)er at a ointp c, we know that:
> f 0 (c) DRAFT = lim f(x)(cid:0)f(c)
> x!c x(cid:0)c
> exists. oTshow that f is ontinuousc at c, we mush show that lim f(x)=f(c).
> x!c
> We anc write f(x) as:
> f(x)(cid:0)f(c)
> f(x)= (x(cid:0)c)+f(c) ;x6=c (2.2.2)
> x(cid:0)c
> By taking the limit as xachesoapprc on othb sides of quatione 2.2.2 and simplifying, we get:
> (cid:20) (cid:21)
> f(x)(cid:0)f(c)
> lim f(x)= lim (x(cid:0)c)+f(c)
> x!c x!c x(cid:0)c
> f(x)(cid:0)f(c)
> = lim (cid:2)lim (x(cid:0)c) +lim f(c) =f 0 (c)(cid:2)0+f(c)=f(c)
> x!c| {z x(cid:0)c } x!c| {z } x!c| {z }
> f 0 (c) 0 f(c)
> eeforTher lim f(x)=f(c) which ansme that f is ontinuousc at x.
> x!c
> Theorem 2.2.3 Not ontinuousc implies not entiable.di(cid:11)er
> If f is not ontinuousc at x=c, then f is not entiabledi(cid:11)er at x=c
> 2.3 Rules of tiationDi(cid:11)eren
> 1. The tConstan function y =c.
> dy f(x+h)(cid:0)f(x) c(cid:0)c 0
> = lim = lim = lim =0
> dx h!0 h h!0 h h!0 h
> d
> ) [c]=0
> dx
> (pg 6) 2 THETIONDIFFERENTIA

---

## Page 26

### Rule 11

> yacultFof Comuterp Science (CS+IT) Semester 1 - Calculus I(lec3)
> 7. The Logarithmic function y =log x
> a
> (cid:18) (cid:19)
> h
> log 1+ (cid:18) (cid:19)
> dy log (x+h)(cid:0)log x a x 1 h
> = lim a a = lim = lim log 1+
> dx h!0 h h!0 h h!0 h a x
> x x
> Let u= )u!1 when h!0 and h= .
> h u
> (cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
> dy 1 h u 1 1 1 u
> ) = iml log 1+ = lim log 1+ = lim log 1+
> dx h!0 h a x u!1 x a u x u!1 a u
> (cid:20) (cid:18) (cid:19) (cid:21)
> 1 1 u 1 1
> = log lim 1+ = log (e)=
> x a u!1 u x a xlna
> d 1
> And ew conclude that [lnx]=
> dx x
> Example 2.3.11 Find the derivative of the function y =ax+b omfr the (cid:12)rst principles.
> Sol
> dy f(x+h)(cid:0)f(x) a(x+h)+b(cid:0)(ax+b) (cid:8)ax(cid:8)+ah+ (cid:1)b(cid:0) (cid:8)ax(cid:8)(cid:0) (cid:1)b
> = lim = lim = lim
> dx h!0 h h!0 h h!0 h
> ah
> = lim = lim a=a:
> h!0 h h!0
> Example 2.3.12 Find the derivative of the function y =4(cid:0)3x omfr the (cid:12)rst principles.
> Example 2.3.13 Find the derivative of the function y =x DRAFT 2 +2x(cid:0)5 omfr the (cid:12)rst .principles
> Sol
> dy f(x+h)(cid:0)f(x) (x+h) 2 +2(x+h)(cid:0)5(cid:0)(x 2 +2x(cid:0)5)
> = lim = lim
> dx h!0 (cid:20) h h!0 (cid:21) h
> (x+h) 2 (cid:0)x 2 2h (x+h) 2 (cid:0)x 2
> = lim + = lim + lim 2
> h!0 h h h!0 h h!0
> h(2x+h)
> = lim + lim 2= lim (2x+h)+ lim 2=2x(+0)+2=2x+2:
> h!0 h h!0 h!0 h!0
> 1
> Example 2.3.14 Find the derivative of the function y = p omfr the (cid:12)rst principles.
> x
> Sol
> 1 1
> p (cid:0) p p p p p
> (cid:1)y f(x+h)(cid:0)f(x) x+h x x(cid:0) x+h x+ x+h
> = = = (cid:0) p p (cid:1) (cid:2) p p
> h h h h x x+h x+ x+h
> x(cid:0)(x+h) (cid:0)1
> = (cid:0) p p (cid:1)(cid:0) p p (cid:1) = (cid:0) p p (cid:1)(cid:0) p p (cid:1)
> h x x+h x+ x+h x x+h x+ x+h
> dy (cid:0)1 (cid:0)1 (cid:0)1 (cid:0)1
> ) = lim (cid:0) p p (cid:1)(cid:0) p p (cid:1) = p p p p = p =
> dx h!0 x x+h x+ x+h ( x x)( x+ x) x(2 x) 2x 3 2
> 2.4 Properties of esativDeriv
> 1. tConstan lutiplem rule: If f is tiabledi(cid:11)eren at x and c is a t,constan then
> d
> [cf(x)]=cf 0 (x)
> dx
> (pg 8) 2 THETIONDIFFERENTIA

---

## Page 27

### Rule 12

> Semester 1 - Calculus Ile(c3) yacultFof teCompur Science (CS+IT)
> 2. Sum Rule: If f and g are tiabledi(cid:11)eren at x, then
> d
> [f(x)+g(x)]=f 0 (x)+g 0 (x)
> dx
> Proof
> Let F =f +g, where f and g are tiabledi(cid:11)eren at x, so:
> F(x+h)(cid:0)F(x) [f(x+h)+g(x+h)](cid:0)[f(x)+g(x)]
> F 0 (x)= lim = lim
> h!0 h h!0 h
> f(x+h)+g(x+h)(cid:0)f(x)(cid:0)g(x) f(x+h)(cid:0)f(x) g(x+h)(cid:0)g(x)
> = lim = lim + lim
> h!0 h h!0 h h!0 h
> = f 0 (x)+g 0 (x):
> Note:
> (a) The sum rule can be extended to three or more tiabledi(cid:11)eren functions f ;f ;:::;f to obtain the
> 1 2 n
> generalized sum rule.
> d
> [f (x)+f (x)+(cid:1)(cid:1)(cid:1)+f (x)]=f 0 (x)+f 0 (x)+(cid:1)(cid:1)(cid:1)+f 0 (x)
> dx 1 2 n 1 2 n
> (b) The di(cid:11)erecne ofowtfunctions f (cid:0)g can be rewritten as the sum f +((cid:0)g). By biningcom the sum
> rule with the tconstanultiple,m the di(cid:11)erence rule established.
> d
> [f(x)(cid:0)g(x)]=f 0 (x)(cid:0)g 0 (x)
> dx
> The proof (exercise)
> 3. Product Rule: If f and g are tiabledi(cid:11)eren at x, then
> d
> [f(x)g(x])=f(x)g 0 (x)+f 0 (x)g(x)
> dx
> Proof
> DRAFT
> Let F(x)=f(x):g(x), ethn
> dF F(x+h)(cid:0)F(x) f(x+h)g(x+h)(cid:0)f(x)g(x)
> = mli = lim
> dx h!0 h h!0 h
> f(x+h)g(x+h)(cid:0)f(x)g(x+h)+f(x)g(x+h)(cid:0)f(x)g(x)
> = mli
> h!0 h
> f(x+h)g(x+h)(cid:0)f(x)g(x+h) f(x)g(x+h)(cid:0)f(x)g(x)
> = mli + lim
> h!0 2 h 3 h!0 2 h 3
> 6 7 6 7
> 6 f(x+h)(cid:0)f(x) 7 6 g(x+h)(cid:0)g(x) 7
> = mli 6 : g(x+)h 7 + lim 6 f(x) : 7
> h!0 4 | {z h } | {z } 5 h!0 4 | {z } | {z h } 5
> g(x);as h!0 f(x); as h!0
> f 0 (x);as h!0 g 0 (x); as h!0
> = f 0 (x)g(x)+f(x)g 0 (x)
> f(x)
> 4. tQuotien RuleConsiderthetquotienq(x)= andnotethatf(x)=g(x):q(x). Bytheropductrule,
> g(x)
> ewe:vha
> f 0 (x)=g 0 (x)q(x)+g(x)q 0 (x)
> Solving for q 0 (x), ew (cid:12)nd that
> f 0 (x)(cid:0)g 0 (x)q(x)
> q 0 (x)=
> g(x)
> f(x)
> Then substituting q(x) with ew get:
> g(x)
> f(x)
> f 0 (x)(cid:0)g 0 (x):
> g(x) g(x)f 0 (x)(cid:0)g 0 (x)f(x)
> q 0 (x)= =
> g(x) (g(x)) 2
> 2 THETIONDIFFERENTIA (pg 9)

---

## Page 28

### Theorem 13

> Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec3)
> Theorem 2.4.4 Quotient uleR
> f
> If f and g earentiabledi(cid:11)er at x , g(x)̸=0, then the derivative of at x exists and
> g
> (cid:20) (cid:21) 0 0
> d f(x) g(x)f (x)−g (x)f(x)
> =
> dx g(x) (g(x))2
> ofoPr
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
> 0 0
> g(x)f (x)−g (x)f(x)
> =
> (g(x))2
> Note: lim g(x+h)=g(x) because g is given differentiable and therefore is continuous.
> h→0
> 5. The Chain Rule
> Theorem 2.4.5 If y =f(u) is aentiabledi(cid:11)erfunction of u, and u=g(x) is aentiabledi(cid:11)erfunction of
> x, then y =f(g(x)) is a entiabledi(cid:11)er function of x and
> DRAFT
> d 0 0
> [f(g(x))]=f (g(x)).g (x)
> dx
> dy
> Example 2.4.15 Euateval for the folownlig functions.
> dx
> 3 √
> 1. y =4x 3+ +2 x−7
> x
> Sol
> 1
> 2. y =3cosx− sinx
> 2
> Sol
> 1 1 √
> 3. y =x 7+ x−2− √ + x3
> 3 x
> Sol
> (pg 10) 2 THE DIFFERENTIATION

---

## Page 45

### Definition 14

> Semester 1 - Calculus I(lec5) Faculty of Computer Science (CS+IT)
> Lecture Five
> 1 Exponential and Logarithmic Functions
> 1.1 Exponential Function
> Definition 1.1.1 Let a > 0, a ̸= 1, then the exponential function of the base a ia y = ax.
> 1.1.1 Some Properties of the exponential function
> For y = ax,
> 1. If a > 1, then:
> (a) ax > 0 ,∀x ∈ R
> (b) y = ax is an increasing function.
> (c) lim ax → 0
> x→−∞
> (d) lim ax → ∞
> x→+∞
> (e) f(0) = a0 = 1, ∀a > 1, the graph of ax passes through the point (0,1) on y−axis.
> 2. If 0 < a < 1, then: T
> F
> (a) ax > 0 ,∀x ∈ R A
> R
> (b) y = ax will be decreasing funDction.
> (c) lim ax → ∞
> x→−∞
> (d) lim ax → 0
> x→+∞
> (e) f(0) = a0 = 1, ∀a < 1, the graph of ax passes through the point (0,1) on y−axis.
> Theorem 1.1.1 Prove that
> x2 x3 xk (cid:88) ∞ xk
> ex = 1+x+ + +···+ +··· =
> 2! 3! k! k!
> k=0
> Proof
> (cid:16) x(cid:17)n
> We know ex = lim 1+ , now:
> n→∞ n
> (cid:16) x(cid:17)n (cid:18) n (cid:19) x (cid:18) n (cid:19) x2 (cid:18) n (cid:19) x3 (cid:18) n (cid:19) xk
> 1+ = 1+ + + +···+ +...
> n 1 n 2 n2 3 n3 k nk
> x n(n−1)x2 n(n−1)(n−2)x3 n(n−1)(n−2)...xk
> = 1+n. + + +···+ +...
> n 2! n2 3! n3 k! nk
> (cid:18) (cid:19) (cid:18) (cid:19)(cid:18) (cid:19)
> 1 1 1 1 2
> =1+x+ 1− x2 + 1− 1− x3 +···+
> 2! n 3! n n
> (cid:18) (cid:19)(cid:18) (cid:19) (cid:18) (cid:19)
> 1 1 2 k −1
> 1− 1− ... 1− xk
> k! n n n
> 1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS (pg 1)

---

## Page 46

### Box 15

>  1 
> − 3 2 3
> = 2e 4 −  = √ − .
> 4 4 e 2

---

### Definition 16

> Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec5)
> (cid:16) x(cid:17)n (cid:88) ∞ xk (cid:18) 1 (cid:19)(cid:18) 2 (cid:19) (cid:18) k −1 (cid:19)
> Therefore 1+ = 1− 1− ... 1− and this implies that:
> n k! n n n
> k=0
> (cid:16) x(cid:17)n (cid:88) ∞ xk (cid:18) 1 (cid:19)(cid:18) 2 (cid:19) (cid:18) k −1 (cid:19)
> lim 1+ = lim 1− 1− ... 1− =
> n→∞ n n→∞ k! n n n
> k=0
> (cid:16) x(cid:17)n (cid:88) ∞ xk x2 x3
> ⇒ ex = lim 1+ = = 1+x+ + +...
> n→∞ n k! 2! 3!
> k=0
> Example 1.1.1 Evaluate the following sums using the definition of exponential function ex:
> (cid:88) ∞ 2k
> 1.
> k!
> k=1
> Sol
> (cid:32) (cid:33)
> (cid:88) ∞ 2k (cid:88) ∞ 2k 20 (cid:88) ∞ 2k (cid:88) ∞ 2k
> = 1+ −1 = + −1 = −1 = e2 −1.
> k! k! 0! k! k!
> k=1 k=1 k=1 k=0
> (cid:88) ∞ (−1)k
> 2.
> T
> k!
> k=2 F
> A
> RSol
> D
> (cid:88) ∞ (−1)k (cid:88) ∞ (−1)k (−1)0 (−1)1 (cid:88) ∞ (−1)k (cid:88) ∞ (−1)k
> = 1−1+ = + + = = e−1.
> k! k! 0! 1! k! k!
> k=2 k=2 k=2 k=0
> (cid:88) ∞ (−1)k
> 3.
> 2k−1k!
> k=2
> Sol
> (cid:18)
> −1
> (cid:19)k  (cid:18)
> −1
> (cid:19)k 
> (cid:88) ∞ (−1)k (cid:88) ∞ (−1)k (cid:88) ∞ 4 (cid:88) ∞ 4 1
> = 2× = 2× = 2× −1+ 
> 2k−1k! 4kk! k!  k! 4
>  
> k=2 k=2 k=2 k=2
>  1 
> − 3 2 3
> = 2e 4 −  = √ − .
> 4 4 e 2
> Example 1.1.2 Find the following limits using ex definition.
> 1−e2x +2x
> 1. lim
> x→0 x2
> Sol
> (pg 2) 1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS

---

## Page 47

### Box 17

> (cid:18) (cid:19)
> 4
> − 2+ x+...

---

## Page 48

### Definition 18

> Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec5)
> 1.2 Logarithmic Functions
> Definition 1.2.2 Let a > 0, a ̸= 1. The logarithmic function of the base a is y = log x,
> a
> and it is the inverse of y = ax. The domain of definition of it D = R+ = (0,∞) and R = R.
> Note that if the base is e, it is called the natural logarithm, and we denoted by lnx (log x =
> e
> lnx) and thus lnx is the inverse of ex.
> 1.2.1 Properties:
> No. log ln
> (1) log 1 = 0 ln1 = 0
> a
> (2) log x+log y = log xy lnx+lny = lnxy
> a a a
> (3) log xn = nlog x lnxn = nlnx
> a a
> 1 1
> (4) log = −log x ln = −lnx
> a x a x
> x x
> (5) log x−log y = log lnx−lny = ln
> a a a y y
> 1 1
> (6) log b = lnb =
> a log a T log e
> b b
> F
> 1 1
> (7) log x = loAg x log x = lnx
> an nR a en n
> D
> (8) log xn = log x log xn = lnx
> an a en
> 1.2.2 Derivative of Logarithmic Function
> 1.
> d 1 du
> [log u(x)] = ×
> dx a u(x)lna dx
> 2.
> d 1 du
> [lnu(x)] = ×
> dx u(x) dx
> And if u(x) = x ⇒
> 1.
> d 1
> [log x] =
> dx a xlna
> 2.
> d 1
> [lnx] =
> dx x
> Derivative of [f(x)]g(x):
> Let y = (f(x))g(x), then the derivative evaluated as follows:
> y = [f(x)]g(x) ⇒ lny = g(x)lnf(x)
> (pg 4) 1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS

---

### Box 19

> 1 1
> = −log x ln = −
> a x a x

---

### Box 20

> og y = log xy lnx+ln
> a a

---
