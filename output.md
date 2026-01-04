## Page 1

Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
Lecture Two
1 Limit of the Function
1.1 Introduction
x3−1
Giventhefunctionf(x)= , clearlyitisnotdefinedatx=1, andwewanttostudythebehaviourofthis
x−1
function when x approaches to 1.
y
5
4 x3−1
y =
3 x−1
2
1
x
-4 -3 -2 -1 1 2 3 4
-1
-2
The following table shows:
T
x 0.75 0.F9 0.99 0.999
f(x) 2.313 A2.710 2.970 2.997
FrRom the left
D
x 1.001 1.01 1.1 1.25
f(x) 3.003 3.030 3.310 3.813
From the right
We can move arbitrarily close to 1 and as a result f(x) moves arbitrarily close to 3, and here we can say the
x3−1
limit of the function f(x)= is 3 when x goes to 1. This limit is written as:
x−1
x3−1
lim =3
x→1 x−1
In general: If f(x) becomes arbitrarily close to a single number L as x approaches c from either sides, the
limit of f(x) as x approaches c is L,and we can write it as:
limf(x)=L
x→c
1.2 Definition of limit
Let f be a function defined on an open interval containing c (except possibly at c) and let L be a real number.
The statement limf(x) = L means that for each ϵ > 0 there exist δ > 0 such that if 0 < |x−c| < δ, then
x→c
|f(x)−L|<ϵ.
Example 1.2.1 Prove that lim(2x+3)=9.
x→3
Proof
Wemustshowthatforeachϵ>0,thereexistsaδ >0suchthat|(2x+3)−9|<ϵwhenever0<|x−3|<δ,because
our choice of δ depends on ϵ. Now we need to establish a connection between the absolute value |(2x+3)−9|
and |x−3|.
|(2x+3)−9|=|2x−6|=2|x−3|
1 LIMIT OF THE FUNCTION (pg 1)


## Page 2

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)
ϵ
So for a given ϵ>0, we can choose δ = . This choice works because
2
ϵ
0<|x−3|<δ =
2
implies that
(cid:16)ϵ(cid:17)
|(2x+3)−9|=2|x−3|<2 =ϵ.
2
1.3 One Sided Limit
1. Left Hand Limit: We mean by L-H-L, limit of the function when x increasing to c,(x̸=c), i.e. (x<c)
and x→c and we denote it by
lim f(x)
x→c−
To evaluate the left limit, we substitute x=c−ϵ on f(x), then we take limit when ϵ→0. (ϵ>0)
lim f(x)= limf(c−ϵ)
x→c− ϵ→0
2. Right Hand Limit: We mean by R-H-L, limit of the function when x decreasing to c,(x ̸= c), i.e.
(x>c) and x→c and we denote it by
lim f(x)
x→c+
To evaluate the left limit, we substitute x=c+ϵ on f(x), then we take limit when ϵ→0. (ϵ>0)
lim f(x)= limf(c+ϵ)
x→c+ ϵ→0
T
And the limit of the function will be exists if and only if:
F
lim f(xA)= lim f(x)
x→c+Rx→c−
D
|x|
Example 1.3.2 Find the limit lim using L-H-L and R-H-L
x→0 x
Sol
1. L-H-L:
|x| |0−ϵ| |−ϵ| ϵ
lim =lim = = lim
x→0+ x ϵ→0 0−ϵ −ϵ ϵ→0−ϵ
=lim−1=−1.
ϵ→0
2. R-H-L:
|x| |0+ϵ| |ϵ| ϵ
lim =lim = = lim
x→0+ x ϵ→0 0+ϵ ϵ ϵ→0ϵ
=lim1=1.
ϵ→0
Since lim f(x)̸= lim f(x), therefore the limit does not exist.
x→0+ x→0−
x2+x−2
Example 1.3.3 Find the limit lim using L-H-L and R-H-L
x→1 x−1
Sol
x2+x−2
1. L-H-L lim
x→1− x−1
x2+x−2 (1−ϵ)2+(1−ϵ)−2 1−2ϵ+ϵ2+1−ϵ−2 ϵ(ϵ−3)
lim = lim = lim = lim
x→1− x−1 ϵ→0 (1−ϵ)−1 ϵ→0 −ϵ ϵ→0 −ϵ
=lim(3−ϵ)=3−0=3
ϵ→0
(pg 2) 1 LIMIT OF THE FUNCTION


## Page 3

Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
x2+x−2
2. R-H-L: lim
x→1+ x−1
x2+x−2 (1+ϵ)2+(1+ϵ)−2 1+2ϵ+ϵ2+1+ϵ−2 ϵ(ϵ+3)
lim = lim = lim = lim
x→1+ x−1 ϵ→0 (1+ϵ)−1 ϵ→0 ϵ ϵ→0 ϵ
=lim(ϵ+3)=0+3=3
ϵ→0
Since R-H-L = L-H-L, the limit exists and equal to 3.
1.4 Properties of Limits
Theorem 1.4.1 Let b and c be real numbers and let n be a positive integer.
1.
limb=b
x→c
2.
limx=c
x→c
3.
limxn =cn
x→c
Example 1.4.4 Evaluate the limits
1.
lim3=3
x→2
T
2.
F
lim x=−4
A
x→−4
R
3.
D
limx2 =(2)2 =4
x→2
Theorem 1.4.2 Let b and c be real numbers and let n be a positive integer, and let f and g be functions with
the following limits.
limf(x)=L , limg(x)=K
x→c x→c
then
1. Scalar multiple
lim[bf(x)]=blimf(x)=bL
x→c x→c
2. Sum or Difference
lim[f(x)±g(x)]= limf(x)± limg(x)=L±K
x→c x→c x→c
3. Product
lim[f(x).g(x)]= limf(x).limg(x)=L.K
x→c x→c x→c
4. Quotient
f(x) lim f(x) L
lim = x→c = ,K ̸=0
x→c g(x) lim x→c g(x) K
5. Power
(cid:104) (cid:105)n
lim[f(x)]n = limf(x) =Ln.
x→c x→c
Example 1.4.5 By using theorems of limits evaluate the following limits.
1. lim(4x2+3)
x→2
Sol
1 LIMIT OF THE FUNCTION (pg 3)


## Page 4

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)
lim(4x2+3)= lim4x2+ lim3=4limx2+ lim3
x→2 x→2 x→2 x→2 x→2
(cid:16) (cid:17)2
= 4 limx + lim3=4(2)2+3=19.
x→2 x→2
(cid:20) (cid:21)
x−2
2. lim
x→3 x+2
Sol
(cid:20) (cid:21)
x−2 lim (x−2) lim x−lim 2 3−2 1
lim = x→3 = x→3 x→3 = =
x→3 x+2 lim x→3 (x+2) lim x→3 x+lim x→3 2 3+2 5
(cid:112)
3. lim 25−x2
x→4
Sol
lim(25−x2)1 2 = (cid:16) lim25− limx2 (cid:17)1 2 = (cid:18) lim25− (cid:16) limx (cid:17)2 (cid:19)1 2 = (cid:0) 25−(4)2(cid:1)1 2 =3
x→4 x→4 x→4 x→4 x→4
4. lim(3x2−1)(9x+2)
x→1
Example 1.4.6 Evaluate the following limits: T
F
1. lim(x+4−x2)
A
x→1
R
D Sol
3x+1
2. lim
x→3 x+2
Sol
3. lim(x+4)(x−1)
x→1
Sol
x+2
4. lim
x→2x−2
Sol
(pg 4) 1 LIMIT OF THE FUNCTION


## Page 5

Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
1
3+
x
5. lim
x→∞ 2+x
Sol
4x+1
6. lim
x→∞ x+9
Sol
x2−1
7. lim
x→−1 x+1
Sol
T
F
A
R
x2+3x+2 D
8. lim
x→−1 x+1
Sol
x5−32
9. lim
x→2 x2−4
Sol
x+sinx
10. lim
x→0tanx+x
Sol
1 LIMIT OF THE FUNCTION (pg 5)


## Page 6

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)
1.5 Strategies for Finding Limits
Previously, we studied several types of functions whose limits can be evaluated by direct substitution, this
knowledge together with the following theorem can be used to develop a strategy for finding limits.
Theorem 1.5.3 Let c be a real number and let f(x) = g(x) for all x ̸= c in an open interval containing c. If
the limit of g(x) as x approaches c exists, then the limit of f(x) also exists and:
limf(x)= limg(x)
x→c x→c
Example 1.5.7 Evaluate the following limits:
x2−x−2
1. lim
x→2 x2−4
Sol
By direct substitution, we get:
(2)2−2−2 4−2−2 0
= = (undetermined value)
(2)2−4 4−4 0
Now we try to find a function g that agrees with f for all x other than x = 2. By factoring and dividing
out like factors, we can rewrite the given function as:
x2−x−2 (cid:24)(x(cid:24)−
(cid:24)(cid:24)
2)(x+1) x+1
f(x)=
x2−4
=
(cid:24)(x(cid:24)−
T (cid:24)(cid:24)
2)(x+2)
=
x+2
=g(x).
F
A
So for all x−values other than x = 2 the functions f and g agree, since limg(x) exists, we can apply
R
x→2
theorem 1.5.3 to conclude that f and g hDave the same limit at x=2.
x2−x−2 (x−2)(x+1) x+1 2+1 3
lim = lim = lim = =
x→2 x2−4 x→2(x−2)(x+2) x→2x+2 2+2 4
x3−1
2. lim
x→1 x−1
Sol
(1)3−1 0
By direct substitution we get = . Then we try to find a function g that agrees with f for all x
1−1 0
other than x=1.
(x2+x+1)≡g(x)
x3−1
(x−1)
x3−1 (x−1)(x2+x+1)
f(x)= = =(x2+x+1)=g(x)
x−1 (x−1)
Thus limf(x)= limg(x)= lim(x2+x+1)=12+1+1=3.
x→1 x→1 x→1
x3−1
Note that: the graph of the function g(x)=x2+x+1 is same as f(x)=
x−1
(pg 6) 1 LIMIT OF THE FUNCTION


## Page 7

Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
y
5
4
y =x2+x+1
3
2
1
x
-4 -3 -2 -1 1 2 3 4
-1
-2
x+1
3. lim
x→−1x2+4x+3
Sol
x+1 x+1 1 1 1
lim = lim = lim = =
x→−1x2+4x+3 x→−1(x+1)(x+3) x→−1(x+3) −1+3 2
x−5
4. lim √ √
x→5 x−3− 2
STol
F
√ √ √ √
x−5 x−3+ 2 (x−5)A (cid:0) x−3+ 2 (cid:1) (cid:16)√ √ (cid:17) √ √ √
lim √ √ .√ √ = lim = lim x−3+ 2 = 2+ 2=2 2.
x→5 x−3− 2 x−3+ 2 x→5
R(x−5)
x→5
D
(1+x)2−1
5. lim
x→0 x
Sol
x6−1
6. lim
x→1x2−1
Sol
1 1
−
x 3
7. lim
x→3 x2−9
1 LIMIT OF THE FUNCTION (pg 7)


## Page 8

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)
Sol
√
x−2
8. lim
x→4 x−4
Sol
Example 1.5.8 Evaluate the following limits.
9x2
1. lim
x→∞2x2+4
Sol
By direct substitution, we get: T
F
9x2 9(∞)2 A∞
lim = = ,(undetermined value)
x→∞2x2+4 2(∞)2R+4 ∞
D
   
x l → im ∞ (cid:124) 2x 9 2 (cid:123) x (cid:122) + 2 4 (cid:125) = x l → im ∞    (cid:26)x (cid:26)2 (cid:20) (cid:26)x (cid:26) 2 2 + [9] x 4 2 (cid:21)    = x l → im ∞   2+ 9 x 4 2   = 2+ 9 ∞ 4 2 = 2+ 9 0 = 9 2
f(x) (cid:124) (cid:123)(cid:122) (cid:125)
g(x)
x3−x2+2
2. lim
x→∞2x2+x+1
Sol
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
1 2 1 2 1 2
(cid:26)x (cid:26)3 1− + 1− + 1− +
x3−x2+2 x x3 x x3 ∞ ∞3
lim = lim = lim = =∞
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
x→∞ (cid:124) 2x2+ (cid:123)(cid:122) x+1 (cid:125) x→∞ (cid:26)x (cid:26)3 2 + 1 + 1 x→∞ 2 + 1 + 1 2 + 1 + 1
x x2 x3 x x2 x3 ∞ ∞2 ∞3
f(x)
(cid:124) (cid:123)(cid:122) (cid:125)
g(x)
x(x+1)
3. lim
x→∞ x3+1
Sol
(pg 8) 1 LIMIT OF THE FUNCTION


## Page 9

Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
6x+1
4. lim √
x→∞ 4x2+3
Sol
(x−3)(2x+1)
5. lim
x→∞ 2x2−x+1
Sol
(3x+4)(x−2)
6. lim
x→∞x(2x+1)(x+2) T
F
ASol
R
D
√
9x2+5
7. lim
x→∞ x+3
Sol
1.6 Cauchy’s Theorem
Theorem 1.6.4 Cauchy’s Theorem:
xn−an
lim =nan−1
x→a x−a
proof
1 LIMIT OF THE FUNCTION (pg 9)


## Page 10

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)
By using long division, we get:
xn−an
=xn−1+axn−2+a2xn−3+···+an−1
x−a
Therefore:
lim
xn−an
= lim
(cid:0) xn−1+axn−2+a2xn−3+···+an−1(cid:1)
x→a x−a x→a
= an−1+a×an−2+a2×an−3+···+an−1
= an−1+an−1+an−1+···+an−1 =nan−1
(cid:124) (cid:123)(cid:122) (cid:125)
n times
Lemma 1.6.1
xn−an n
lim = an−m
x→axm−am m
proof
xn−an xn−an xm−am
We can write f(x)= = ÷ . Then the limit will be:
xm−am x−a x−a
xn−an xn−an xm−am nan−1 n
lim = lim ÷ lim = = an−m.
x→axm−am x→a x−a x→a x−a mam−1 m
Lemma 1.6.2
x−a 1
lim = a1−m
x→axm−am m
Proof left for you.
Example 1.6.9 Evaluate the following limits.
T
x5−32
1. lim F
x→2 x3−8
A
RSol
D
x5−32 x5−(2)5 5 5 20
lim = lim = (2)5−3 = (2)2 = .
x→2 x3−8 x→2x3−(2)3 3 3 3
x2−16
2. lim √
x→4x x−8
Sol
x2−16 x2−(4)2 2 4 8
lim √ = lim = (4)2−3 2 = (2)=
x→4x x−8 x→4x3
2
−(4)3
2
3
2
3 3
√ √
x+∆x− x
3. lim
∆x→0 ∆x
Sol
√ √
lim x+∆x− x = lim (x+∆x)1 2 −x1 2 = 1 x1 2 −1 = 1 x− 2 1 = √ 1
∆x→0 ∆x x+∆x→x (x+∆x)−x 2 2 2 x
x−3
4. lim
x→3x3−27
Sol
x−3 x−3 1 1 1 1
lim = lim = (3)1−3 = . = .
x→3x3−27 x→3x3−(3)3 3 3 9 27
x3+1
5. lim
x→−1 x+1
Sol
x3+1 x3−(−1)3
lim = lim =3(−1)3−1 =3(−1)2 =3.
x→−1 x+1 x→−1 x−(−1)
(pg 10) 1 LIMIT OF THE FUNCTION


## Page 11

Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
1.7 The squeeze Theorem
Theorem 1.7.5 Assume the functions f,g and h satisfy f(x)≤g(x)≤h(x) for all values of x near a, except
possibly at a.
If lim f(x)= lim h(x)=L, then lim g(x)=L
x→a x→a x→a
1.8 Limit of Trigonometric Functions
We have some important limits:
1. limsinx=0
x→0
2. limcosx=1
x→0
T
sinx F
3. lim =1 A
x→0 x
R
sinax D
4. lim =1
ax→0 ax
tanx
5. lim =1
x→0 x
tanax
6. lim =1
ax→0 ax
tanx
Example 1.8.10 1. Prove that lim =1
x→0 x
Sol
tanx sinx sinx 1 1
lim = lim = lim .lim =1× =1×1=1
x→0 x x→0xcosx x→0 x x→0cosx cos0
sin2x
2. lim
x→0 x
Sol
sin2x 2sin2x sin2x
lim = lim =2 lim =2×1=2
x→0 x 2x→0 2x 2x→0 2x
tan3x
3. lim
x→0 2x
Sol
tan3x 1 tan3x 1 3tan3x 3 tan3x 3 3
lim = lim = lim = lim = ×1= .
x→0 2x 2x→0 x 23x→0 3x 23x→0 3x 2 2
1 LIMIT OF THE FUNCTION (pg 11)


## Page 12

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)
tanx+sin3x
4. lim
x→0 x
Sol
tanx+sin3x tanx sin3x tanx sin3x
lim = lim + lim = lim +3 lim =1+3×1=4.
x→0 x x→0 x x→0 x x→0 x 3x→0 3x
2x+sinx
5. lim
x→04x+tan5x
Sol
 2x+sinx 
lim 2x+sinx = lim x = lim 2x+sinx ÷ lim 4x+tan5x
x→04x+tan5x x→0 4x+tan5x x→0 x x→0 x
x
(cid:18) (cid:19) (cid:18) (cid:19)
sinx tan5x
= lim2+ lim ÷ lim4+ lim
x→0 x→0 x x→0 x→0 x
(cid:18) (cid:19) (cid:18) (cid:19)
sinx tan5x
= lim2+ lim ÷ lim4+5 lim
x→0 x→0 x x→0 5x→0 5x
2+1 3 1
= = = .
4+5 9 3
(cid:18) (cid:19)
3
6. lim xsin
x→∞ x
Sol
3 3
Let u= ⇒x= and u→0 as x→∞. Thus
x u
(cid:18) (cid:19)
3 3 T sinu
lim xsin = lim sinu=3 lim =3×1=3.
x→∞ x u→0u F u→0 u
A
1−cosx
7. lim R
x→0 x2 D
Sol
1−cosx 1+cosx 1−cos2x sin2x sin2x 1
lim × = lim = lim = lim × lim
x→0 x2 1+cosx x→0x2(1+cosx) x→0x2(1+cosx) x→0 x2 x→0(1+cosx)
(cid:18)
sinx
(cid:19)2
1 1 1
= lim × lim =1× =
x→0 x x→0(1+cosx) (1+cos0) 2
1.9 The Number e
We define the number e by the limit
(cid:18)
1
(cid:19)x
e= lim 1+
x→∞ x
Proof
(cid:18)
1
(cid:19)x (cid:18)
x
(cid:19)
1
(cid:18)
x
(cid:19)
1
(cid:18)
x
(cid:19)
1
(cid:18)
x
(cid:19)
1
1+ = 1+ . + . + . +···+ .
x 1 x 2 x2 3 x3 n xn
x (cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
(cid:88) 1 1 2 3 n−1
= 1− . 1− . 1− ... 1−
n! x x x x
n=0
Therefore the limit will be:
(cid:18)
1
(cid:19)x
(cid:88)
x (cid:18)
1
(cid:18)
1
(cid:19) (cid:18)
2
(cid:19) (cid:18)
3
(cid:19) (cid:18)
n−1
(cid:19)(cid:19)
lim 1+ = lim 1− . 1− . 1− ... 1−
x→∞ x x→∞n! x x x x
n=0
x
(cid:88) 1 1 1
= = =1+1+ + +...
n! 2! 3!
n=0
The number e satisfied the inequality 2<e<3, and its value ≊2.71828, and we can write the limit as:
(cid:18)
1
(cid:19)n
e= lim 1+ = lim(1+n)n 1
n→∞ n n→0
(pg 12) 1 LIMIT OF THE FUNCTION


## Page 13

Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
1.10 The Exponential Theorem
Theorem 1.10.6
x2 x3 (cid:88) ∞ xn
ex =1+x+ + +···=
2 3 n!
n=0
Proof
(cid:18)
1
(cid:19)n
We know that e= lim 1+ .
n→∞ n
(cid:20) (cid:18)
1
(cid:19)n(cid:21)x (cid:18)
1
(cid:19)nx
⇒ex = lim 1+ = lim 1+
n→∞ n n→∞ n
(cid:16) x(cid:17)m
put m=nx⇒ex = lim 1+ , therefore the limit will be:
m→∞ m
(cid:20) mx m(m−1) x2 m(m−1)(m−2) x3 (cid:21)
⇒ lim 1+ + + +...
m→∞ m 2! m2 3! m3
 (cid:18) 1 (cid:19) (cid:18) 1 (cid:19)(cid:18) 2 (cid:19) 
1− 1− 1−
 m m m 
= lim 1+x+ + +...
m→∞ 2! 3! 
x2 x3
= 1+x+ + +...
2! 3!
1
Example 1.10.11 1. lim(1+x)x
x→0 T
F
ASol
R
1 1
put u= ⇒x= and u→∞ as x→D0
x u
1
(cid:18)
1
(cid:19)u
lim(1+x)x = lim 1+ =e.
x→0 u→∞ u
(cid:16) α(cid:17)x
2. lim 1+ α̸=0
x→∞ x
Sol
(i) If α>0, let x=αu
(cid:16) α(cid:17)x (cid:16) α (cid:17)αu (cid:18) (cid:18) 1 (cid:19)u(cid:19)α
lim 1+ = lim 1+ = lim 1+ =eα.
x→∞ x u→∞ αu u→∞ u
(ii) If α<0⇒ let x=−αu
(cid:16) α(cid:17)x (cid:16) α (cid:17)−αu (cid:32) (cid:18) 1 (cid:19)−u (cid:33)α (cid:18) (cid:18) u (cid:19)u(cid:19)α
lim 1+ = lim 1− = lim 1− = lim
x→∞ x u→∞ αu u→∞ u u→∞ u−1
(cid:20) (cid:18)
1
(cid:19)u(cid:21)α
= lim 1+
u→∞ u−1
Now let u−1=y ⇒u=1+y (y →∞ as u→∞.
(cid:16) α(cid:17)x (cid:20) (cid:18) 1 (cid:19)u(cid:21)α (cid:34) (cid:18) 1 (cid:19)y+1 (cid:35)α
lim 1+ = lim 1+ = lim 1+
x→∞ x u→∞ u−1 y→∞ y
(cid:20) (cid:18)
1
(cid:19)y (cid:18)
1
(cid:19)(cid:21)α
= lim 1+ × lim 1+ =(e×1)α =eα.
y→∞ y y→∞ y
1 LIMIT OF THE FUNCTION (pg 13)


## Page 14

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)
(cid:18)
x+3
(cid:19)x
3. lim
x→∞ x−2
Sol
Let u=x−2⇒x=u+2⇒(u→∞) as (x→∞)
(cid:18)
x+3
(cid:19)x (cid:18)
u+2+3
(cid:19)u+2 (cid:18)
5
(cid:19)u+2 (cid:18)
5
(cid:19)u (cid:18)
5
(cid:19)2
⇒ lim = lim = lim 1+ = lim 1+ . lim 1+ =e5
x→∞ x−2 u→∞ u u→∞ u u→∞ u u→∞ u
Exercise 1.10.1 Evaluate the following limits.
x2−2x−3
1. lim
x→3 x−3
Sol
x2−16
2. lim
x→4 4−x
Sol
T
F
A
R
(x−b)50−x+b D
3. lim
x→b x−b
Sol
1 1
−
5+h 5
4. lim
h→0 h
Sol
(cid:18) (cid:19)
1 1
5. lim −
w→1 w2−w w−1
Sol
(pg 14) 1 LIMIT OF THE FUNCTION


## Page 15

Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
x2+2x+9
6. lim
x→∞3x3+x+1
Sol
√
9x2+7
7. lim
x→1 3x+1
Sol
(cid:18) (cid:19)
1+2+3+···+n
8. lim
n→∞ n2
Sol
T
F
x3+x2+5x−5
A
9. lim
x→1 x−1 R
D
Sol
 1 1 
+
x−1 x+1
10. lim 
x→0  x 
Sol
x3(x−1)6−8
11. lim
x→2 x−2
Sol
√
x2+12−4
12. lim
x→2 x−2
1 LIMIT OF THE FUNCTION (pg 15)


## Page 16

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)
Sol
x−1−1
13. lim
x→1 x−1
Sol
4x2−x2
14. lim √
x→4 2− x
Sol
4−x T
15. lim √
x→4 x2+9−5 F
A
RSol
D
√
3y−2
16. lim √
y→8y 3y−16
Sol
y4−81
17. lim
y→3 y2−9
Sol
(x+∆x)3−x3
18. lim
∆x→0 ∆x
Sol
(pg 16) 1 LIMIT OF THE FUNCTION


## Page 17

Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)
x5+32
19. lim
x→−2 x3+8
Sol
4x+sin3x
20. lim
x→0 x
Sol
sin3x
21. lim
x→0sin9x
Sol
T
F
sin2x
22. lim A
x→0x2+3x
R
D
Sol
sin(x−2)
23. lim
x→2 x2−4
Sol
1−cos4x
24. lim
x→0 x2
Sol
tan2x+4x
25. lim
x→0x+sinx+tanx
Sol
1 LIMIT OF THE FUNCTION (pg 17)


## Page 18

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)
cos4x−cos2x
26. lim
x→0 x2
Sol
6
27. lim xsin
x→∞ x
Sol
T
F
A
R
D
(pg 18) 1 LIMIT OF THE FUNCTION


## Page 19

Semester 1 - Calculus I(lec3) Faculty of Computer Science (CS+IT)
Lecture Three
1 The Continuity
1.1 Continuity at a point on an open interval
Informally, we might say that a function is continuous on an open interval if its graph can be drawn with a
pencil without lifting the pencil from the paper. i.e. A function f is continuous at x = c means there is no
interruption in the graph of f at c. That is, its graph is unbroken at c and there are no holes, jumps, or gaps.
The following figure identifies three values of x at which the graph of f is not continuous. At all other points
in the interval (a,b) the graph of f is uninterrupted and continuous.
Figure 1: Three cases for the discontinuity
T
F
A
1.2 Concept of Continuity R
D
Definition 1.2.1 Continuity at a point:
A function f is continuous at c if the following three conditions are met.
1. f(c) is defined
2. limf(x) exists.
x→c
3. f(c)= limf(x)
x→c
Continuity on an open interval:
A function is continuous on an open interval (a,b) if it is continuous at each point in the interval.
Definition 1.2.2 Let f(x) be a defined function at x = c, we say that f(x) is continuous at x = c if the
following condition satisfied.
lim [f(c+h)−f(c)]=0
h→0
Example 1.2.1 Given f(x)=x2, prove that it is continuous on R.
Proof
To prove the function is continuous on R, choose an arbitrary point x=c, s.t c∈R.
lim [f(c+h)−f(c)]= lim
(cid:2) f(c+h)2−c2(cid:3)
= lim
(cid:2) c2+2ch+h2−c2(cid:3)
h→0 h→0 h→0
= lim [h(2c+h)]=0×(2c+0)=0.
h→0
⇒f(x)=x2 is continuous at c⇒ continuous at R.
Example 1.2.2 Prove that the function f(x)=cosax, continuous on R.
Proof
1 THE CONTINUITY (pg 1)


## Page 20

yacultFof Comuterp Science (CS+IT) Semester 1 - Calculus I(lec3)
oTovepr the unctionf is ontinuousc on R, osecho an aryarbitrointp x=c, s.t c2R.
(cid:20) (cid:18) (cid:19) (cid:18) (cid:19)(cid:21)
ac+ah+ac ac+ah(cid:0)ac
lim [f(c+h)(cid:0)f(c)]= lim [cos(ac+ah)(cid:0)cos(ac)]=(cid:0)2 lim sin sin
h!0 h!0 h!0 2 2
(cid:20) (cid:18) (cid:19) (cid:18) (cid:19)(cid:21)
ah ah
= (cid:0)2 lim sin ac+ sin =(cid:0)2(cid:2)sinac(cid:2)0=0:
h!0 2 2
)f(x)=cosax is ontinuousc at c) ontinuousc at R.
Example 1.2.3 ovePr that the function f(x)=a x ;a>0 is ontinuousc on R.
ofoPr
oTovepr the unctionf is ontinuousc on R, osecho an aryarbitrointp x=c, s.t c2R.
(cid:2) (cid:3) (cid:2) (cid:0) (cid:1)(cid:3)
lim [f(c+h)(cid:0)f(c)]= lim a c+h (cid:0)a c = lim a c a h (cid:0)1
h!0 h!0 h!0
= a c (1(cid:0)1)=a c (cid:2)0=0
)f(x)=a x is ontinuousc on R
Example 1.2.4 ovePr that the function f(x)=log x ;a>0 is ontinuousc on R + .
a
ofoPr
oTovepr the unctionf is ontinuousc on R, osecho an aryarbitrointp x=c, s.t c>0;c2R.
(cid:20) (cid:18) (cid:19)(cid:21)
c+h
lim [f(c+h)(cid:0)f(c)]= lim [log (c+h)(cid:0)log c]= lim log
h!0 h!0 a a h!0 a c
(cid:20) (cid:18) (cid:19)(cid:21) (cid:18) (cid:20) (cid:21)(cid:19)
h h
= lim log 1+ =log lim 1+ =log (1)=0
h!0 a c a h!0 c a
Example 1.2.5 Discuss the ontinuityc of the function
(
3x(cid:0)1 ;x<1
DRAFT
f(x)=
2x 2 ;x(cid:21)1
at x=1.
Sol
eHer we wlil study theeethronditionsc on de(cid:12)nition 1.2.1.
1. f(1)=2(1) 2 =2
2. orF(cid:12)nding the limit:
lim f(x)= lim f(a+(cid:15))= lim 2(1+(cid:15)) 2 =2(1+0) 2 =2(1) 2 =2:
x!1 + (cid:15)!0 (cid:15)!0
lim f(x)= lim f(a(cid:0)(cid:15))= lim 3(1(cid:0)(cid:15))(cid:0)1=3(1)(cid:0)1=3(cid:0)1=2:
x!1 (cid:0) (cid:15)!0 (cid:15)!0
eSinc lim f(x)= lim f(x)) lim f(x) exists and =2
x!1 + x!1 (cid:0) x!1
3. arlyCle f(1)= lim f(x),eefortherthe given function is ontinuousc at x=1.
x!1
Example 1.2.6 Determine whether the following function is ontinuousc at x=0.
8
>< sin(cid:25)x
;x<0
f(x)= x
>: sin(cid:25)x
;x(cid:21)0
x+1
Sol
sin(0(cid:25)) 0
1. f(1)= = =0
0+1 1
(pg 2) 1 THE CONTINUITY


## Page 21

Semester 1 - Calculus Ile(c3) yacultFof teCompur Science (CS+IT)
2.
sin((cid:25)(0+(cid:15))) sin(cid:25)(cid:15) sin0 0
lim f(x)= lim f(a+(cid:15))= lim = lim = = =0
x!0 + (cid:15)!0 (cid:15)!0 0+(cid:15)+1 (cid:15)!0 (cid:15)+1 0+1 1
sin((cid:25)(0(cid:0)(cid:15))) sin(cid:25)(cid:15)
lim f(x)= lim f(a(cid:0)(cid:15))= lim = lim =(cid:25)
x!0 (cid:0) (cid:15)!0 (cid:15)!0 0(cid:0)(cid:15) (cid:15)!0 (cid:15)
) lim f(x) not existauseceb mli f(x)6= lim f(x)
x!0 x!0 + x!0 (cid:0)
Example 1.2.7 Find the onstantc such that the function is sontinuouc on the eentiralerline.
1. (
3x 2 ;x(cid:21)1
f(x)=
ax(cid:0)4 ;x<1
2. 8
< 4sinx
;x<0
f(x)= x
:
a(cid:0)2x ;x(cid:21)0
DRAFT
3. (
1(cid:0)4x ;x<2
f(x)=
ax 2 (cid:0)3x+2 ;x(cid:21)2
1.3 Properties of yuittinCon
Theorem 1.3.1 If b is aalerernumb and f and g earontinuousc at x = c, then the following functions ear
also ontinuousc at c
1. alarSc tple:muli bf
2. Sum ore:encDi(cid:11)er f (cid:6)g
3. duct:oPr fg
f
4. Quotient: , if g(c)6=0.
g
Note: Teh wingfollopytes of functions areuoustinconat eryev ptoin in their domains.
(i) olynomialsP
1 THE CONTINUITY (pg 3)


## Page 22

yacultFof Comuterp Science (CS+IT) Semester 1 - Calculus I(lec3)
p(x)
(ii) Rational r(x)= ;q(x)6=0
q(x)
p
(iii) Radical: f(x)= n x
(iv) rigonometric:T sinx;cosx;tanx;cotx;secx;cscx
Exercise 1.3.1 Find the following:
1. ovePr that f(x)=sin(ax) ;(a6=0) is ontinuousc on R.
2. ovePr that f(x)=x 3 (cid:0)x is ontinuousc on R.
3. Discuss the ontinuityc of the function f(x)=(xln 2 +1)
4. Determine whether the following functions earontinuousc at the given oints.p
(
x x (cid:0)1 ;x6=0
(a) f(x)= at x=0
1 ;x=0
DRAFT
8
< sin((cid:25)x)
;x<1
(b) f(x)= 1(cid:0)x at x=1
:
(cid:25)x 2 ;x(cid:21)1
(pg 4) 1 THE CONTINUITY


## Page 23

Semester 1 - Calculus Ile(c3) yacultFof teCompur Science (CS+IT)
2 The tiationDi(cid:11)eren
2.1 The Change and Rate of Change
Let y =f(x) is auoustinconfunction on an openaltervinI, (x2I).
1. The hangec on x(cid:17)(cid:1)x=x (cid:0)x =h
2 1
2. The hangec on y (cid:17)(cid:1)y =f(x+h)(cid:0)f(x)
(cid:1)y
3. The rate of hangec is
(cid:1)x
(cid:1)y f(x+h)(cid:0)f(x)
=
(cid:1)x h
(cid:1)y
Example 2.1.8 If y =x 3 , (cid:12)nd DRAFT
h
Sol
(cid:2) (cid:3)
(cid:1)y (x+h) 3 (cid:0)x 3 h (x+h) 2 +x(x+h)+x 2
= =
h h h
= (x+h) 2 +x(x+h)+x 2 =3x 2 +3hx+h 2
(cid:1)y
eeforTher = 3x 2 +3hx+h 2
h
2.2 Rate of Changes or esativDeriv
De(cid:12)nition 2.2.3 heT derivative of f is the function:
dy (cid:1)y f(x+h)(cid:0)f(x)
f 0 (x)= = lim = lim (2.2.1)
dx h!0 h h!0 h
dovideprthe limit exists and x is in the domain of f. If f 0 (x) exists, we say that f isentiabledi(cid:11)erat x.
Note: If f is tiabledi(cid:11)eren at eryev tpoin of an openaltervinI, ewysa that f is tiabledi(cid:11)eren on I.
dy
Example 2.2.9 Given y =x 3 , evaluate the ater of change .
dx
Sol
eSinc y =x 3 is a olynomialp ) oosntinuuc on R. By using 2.2.1
dy f(x+h)(cid:0)f(x)
= lim
dx h!0 h
2 THETIONDIFFERENTIA (pg 5)


## Page 24

yacultFof Comuterp Science (CS+IT) Semester 1 - Calculus I(lec3)
f(x+h)(cid:0)f(x)
omfr example 2.1.8, we saw that =3x 2 +3hx+h 2
h
L:S:L= lim (3x 2 +3hx+h 2 )= lim (3x 2 +3hx+h 2 )=3x 2 :
h!0 + h!0
R:S:L= lim (3x 2 +3hx+h 2 )= lim (3x 2 +3hx+h 2 )=3x 2
h!0 (cid:0) h!0
dy
eeforTher =3x 2
dx
dy
Example 2.2.10 orFthe function y =jxj, (cid:12)nd at x=0.
dx
Sol
We know that, the given function is ontinuousc on R.
dy f(0+h)(cid:0)f(0) f(h)(cid:0)0 f(h)
= lim = lim = lim
dx h!0 h h!0 h h!0 h
Now, we will study the eexistenc of the limit by alculatingc the left and right limits.
jhj h
(i) L:S:L= lim = lim =(cid:0)1
h!0 (cid:0) h h!0 (cid:0)h
jhj h
(ii) L:S:L= lim = lim =1
h!0 + h h!0 h
Thus the limit esdo not exist at x=0 and eher we say the function is not entiabledi(cid:11)er at x=0.
Theorem 2.2.2 entiableDi(cid:11)er implies ontinuousc
ofoPr
ausecBef is entableidi(cid:11)er at a ointp c, we know that:
f 0 (c) DRAFT = lim f(x)(cid:0)f(c)
x!c x(cid:0)c
exists. oTshow that f is ontinuousc at c, we mush show that lim f(x)=f(c).
x!c
We anc write f(x) as:
f(x)(cid:0)f(c)
f(x)= (x(cid:0)c)+f(c) ;x6=c (2.2.2)
x(cid:0)c
By taking the limit as xachesoapprc on othb sides of quatione 2.2.2 and simplifying, we get:
(cid:20) (cid:21)
f(x)(cid:0)f(c)
lim f(x)= lim (x(cid:0)c)+f(c)
x!c x!c x(cid:0)c
f(x)(cid:0)f(c)
= lim (cid:2)lim (x(cid:0)c) +lim f(c) =f 0 (c)(cid:2)0+f(c)=f(c)
x!c| {z x(cid:0)c } x!c| {z } x!c| {z }
f 0 (c) 0 f(c)
eeforTher lim f(x)=f(c) which ansme that f is ontinuousc at x.
x!c
Theorem 2.2.3 Not ontinuousc implies not entiable.di(cid:11)er
If f is not ontinuousc at x=c, then f is not entiabledi(cid:11)er at x=c
2.3 Rules of tiationDi(cid:11)eren
1. The tConstan function y =c.
dy f(x+h)(cid:0)f(x) c(cid:0)c 0
= lim = lim = lim =0
dx h!0 h h!0 h h!0 h
d
) [c]=0
dx
(pg 6) 2 THETIONDIFFERENTIA


## Page 25

Semester 1 - Calculus Ile(c3) yacultFof teCompur Science (CS+IT)
2. erwoPRule
d
[x n ]=nx n(cid:0)1
dx
Proof
(cid:2) (cid:0) (cid:1) (cid:3)
dy (x+h) n (cid:0)x n x n +nx n(cid:0)1 h+ n n n(cid:0)2 h 2 +(cid:1)(cid:1)(cid:1)+h n (cid:0)x n
= iml = lim 2
dx h!0 (cid:2) h (cid:0) (cid:1) h!0 (cid:3) h
h nx n(cid:0)1 + n n n(cid:0)1 h+(cid:1)(cid:1)(cid:1)+h n(cid:0)1
= iml 2
h!0 (cid:20) (cid:18) (cid:19) h (cid:21)
n
= iml nx n(cid:0)1 + n n(cid:0)1 h+(cid:1)(cid:1)(cid:1)+h n(cid:0)1 =nx n(cid:0)1 :
h!0 2
3. The Sine function y =sinx
(cid:18) (cid:19) (cid:18) (cid:19)
h h
2cos x+ sin
dy sin(x+h)(cid:0)sinx 2 2
= mli = lim
dx h!0 h 2 h!0 (cid:18) (cid:19) 3 h
h
(cid:20) (cid:18) (cid:19)(cid:21) sin
h 6 2 7
= lim cos x+ 6 lim (cid:18) (cid:19) 7 =cosx(cid:2)1=cosx:
h!0 2 4 h !0 h 5
2
2
d
) [sinx]=cosx
dx
4. The Cosine function y =cosx
d
[cosx]=(cid:0)sinx
dx
Proof, left for ou.y
5. ThetanngeTunctionFy =tanx
DRAFT tanx+tanh
(cid:0)tanx
dy tan(x+h)(cid:0)tanx 1(cid:0)tanxtanh
= lim = lim
dx h!0 h h!0 h
tanx+tanh(cid:0)tanx(1(cid:0)tanxtanh)
= lim
h!0 h(1(cid:0)tanxtanh)
(cid:24)tanx+tanh(cid:24)(cid:0) (cid:24) (cid:24)tanx+tan(cid:24) (cid:24) 2 xtanh
= lim
h!0 h(1(cid:0)tanxtanh)
(cid:18) (cid:19) (cid:18) (cid:19)
tanh 1
= lim (cid:2) lim (cid:2) lim (1+tan 2 x) =1(cid:2)1(cid:2)sec 2 x=sec 2 x
h!0 | {z h } | h!0 1(cid:0)tanxtanh {z } h!0| {z }
(1) (1) sec 2 x
6. The Exptialonen function y =a x ;a>0 (a6=1).
dy a x+h (cid:0)a x a h (cid:0)1
= lim =a x lim
dx h!0 h h!0 h
(cid:18) (cid:19)
1 1 1
w,No let =a h (cid:0)1)u= , suth u!1 when h!0 and h=log 1+
u a h (cid:0)1 a u
dy 1 1
) = a x (cid:2) lim (cid:18) (cid:18) (cid:19)(cid:19) =a x (cid:2) lim (cid:18) (cid:19)
dx u!1 1 u!1 1 u
u log 1+ log 1+
a u a u
1 1
= a x (cid:2) (cid:18) (cid:18) (cid:19)(cid:19) =a x (cid:2) =a x (cid:2)ln(a)
1 u log e
log lim 1+ a
a u!1 u
d
) [a x ]=a x (cid:2)lna
dx
2 THETIONDIFFERENTIA (pg 7)


## Page 26

yacultFof Comuterp Science (CS+IT) Semester 1 - Calculus I(lec3)
7. The Logarithmic function y =log x
a
(cid:18) (cid:19)
h
log 1+ (cid:18) (cid:19)
dy log (x+h)(cid:0)log x a x 1 h
= lim a a = lim = lim log 1+
dx h!0 h h!0 h h!0 h a x
x x
Let u= )u!1 when h!0 and h= .
h u
(cid:18) (cid:19) (cid:18) (cid:19) (cid:18) (cid:19)
dy 1 h u 1 1 1 u
) = iml log 1+ = lim log 1+ = lim log 1+
dx h!0 h a x u!1 x a u x u!1 a u
(cid:20) (cid:18) (cid:19) (cid:21)
1 1 u 1 1
= log lim 1+ = log (e)=
x a u!1 u x a xlna
d 1
And ew conclude that [lnx]=
dx x
Example 2.3.11 Find the derivative of the function y =ax+b omfr the (cid:12)rst principles.
Sol
dy f(x+h)(cid:0)f(x) a(x+h)+b(cid:0)(ax+b) (cid:8)ax(cid:8)+ah+ (cid:1)b(cid:0) (cid:8)ax(cid:8)(cid:0) (cid:1)b
= lim = lim = lim
dx h!0 h h!0 h h!0 h
ah
= lim = lim a=a:
h!0 h h!0
Example 2.3.12 Find the derivative of the function y =4(cid:0)3x omfr the (cid:12)rst principles.
Example 2.3.13 Find the derivative of the function y =x DRAFT 2 +2x(cid:0)5 omfr the (cid:12)rst .principles
Sol
dy f(x+h)(cid:0)f(x) (x+h) 2 +2(x+h)(cid:0)5(cid:0)(x 2 +2x(cid:0)5)
= lim = lim
dx h!0 (cid:20) h h!0 (cid:21) h
(x+h) 2 (cid:0)x 2 2h (x+h) 2 (cid:0)x 2
= lim + = lim + lim 2
h!0 h h h!0 h h!0
h(2x+h)
= lim + lim 2= lim (2x+h)+ lim 2=2x(+0)+2=2x+2:
h!0 h h!0 h!0 h!0
1
Example 2.3.14 Find the derivative of the function y = p omfr the (cid:12)rst principles.
x
Sol
1 1
p (cid:0) p p p p p
(cid:1)y f(x+h)(cid:0)f(x) x+h x x(cid:0) x+h x+ x+h
= = = (cid:0) p p (cid:1) (cid:2) p p
h h h h x x+h x+ x+h
x(cid:0)(x+h) (cid:0)1
= (cid:0) p p (cid:1)(cid:0) p p (cid:1) = (cid:0) p p (cid:1)(cid:0) p p (cid:1)
h x x+h x+ x+h x x+h x+ x+h
dy (cid:0)1 (cid:0)1 (cid:0)1 (cid:0)1
) = lim (cid:0) p p (cid:1)(cid:0) p p (cid:1) = p p p p = p =
dx h!0 x x+h x+ x+h ( x x)( x+ x) x(2 x) 2x 3 2
2.4 Properties of esativDeriv
1. tConstan lutiplem rule: If f is tiabledi(cid:11)eren at x and c is a t,constan then
d
[cf(x)]=cf 0 (x)
dx
(pg 8) 2 THETIONDIFFERENTIA


## Page 27

Semester 1 - Calculus Ile(c3) yacultFof teCompur Science (CS+IT)
2. Sum Rule: If f and g are tiabledi(cid:11)eren at x, then
d
[f(x)+g(x)]=f 0 (x)+g 0 (x)
dx
Proof
Let F =f +g, where f and g are tiabledi(cid:11)eren at x, so:
F(x+h)(cid:0)F(x) [f(x+h)+g(x+h)](cid:0)[f(x)+g(x)]
F 0 (x)= lim = lim
h!0 h h!0 h
f(x+h)+g(x+h)(cid:0)f(x)(cid:0)g(x) f(x+h)(cid:0)f(x) g(x+h)(cid:0)g(x)
= lim = lim + lim
h!0 h h!0 h h!0 h
= f 0 (x)+g 0 (x):
Note:
(a) The sum rule can be extended to three or more tiabledi(cid:11)eren functions f ;f ;:::;f to obtain the
1 2 n
generalized sum rule.
d
[f (x)+f (x)+(cid:1)(cid:1)(cid:1)+f (x)]=f 0 (x)+f 0 (x)+(cid:1)(cid:1)(cid:1)+f 0 (x)
dx 1 2 n 1 2 n
(b) The di(cid:11)erecne ofowtfunctions f (cid:0)g can be rewritten as the sum f +((cid:0)g). By biningcom the sum
rule with the tconstanultiple,m the di(cid:11)erence rule established.
d
[f(x)(cid:0)g(x)]=f 0 (x)(cid:0)g 0 (x)
dx
The proof (exercise)
3. Product Rule: If f and g are tiabledi(cid:11)eren at x, then
d
[f(x)g(x])=f(x)g 0 (x)+f 0 (x)g(x)
dx
Proof
DRAFT
Let F(x)=f(x):g(x), ethn
dF F(x+h)(cid:0)F(x) f(x+h)g(x+h)(cid:0)f(x)g(x)
= mli = lim
dx h!0 h h!0 h
f(x+h)g(x+h)(cid:0)f(x)g(x+h)+f(x)g(x+h)(cid:0)f(x)g(x)
= mli
h!0 h
f(x+h)g(x+h)(cid:0)f(x)g(x+h) f(x)g(x+h)(cid:0)f(x)g(x)
= mli + lim
h!0 2 h 3 h!0 2 h 3
6 7 6 7
6 f(x+h)(cid:0)f(x) 7 6 g(x+h)(cid:0)g(x) 7
= mli 6 : g(x+)h 7 + lim 6 f(x) : 7
h!0 4 | {z h } | {z } 5 h!0 4 | {z } | {z h } 5
g(x);as h!0 f(x); as h!0
f 0 (x);as h!0 g 0 (x); as h!0
= f 0 (x)g(x)+f(x)g 0 (x)
f(x)
4. tQuotien RuleConsiderthetquotienq(x)= andnotethatf(x)=g(x):q(x). Bytheropductrule,
g(x)
ewe:vha
f 0 (x)=g 0 (x)q(x)+g(x)q 0 (x)
Solving for q 0 (x), ew (cid:12)nd that
f 0 (x)(cid:0)g 0 (x)q(x)
q 0 (x)=
g(x)
f(x)
Then substituting q(x) with ew get:
g(x)
f(x)
f 0 (x)(cid:0)g 0 (x):
g(x) g(x)f 0 (x)(cid:0)g 0 (x)f(x)
q 0 (x)= =
g(x) (g(x)) 2
2 THETIONDIFFERENTIA (pg 9)


## Page 28

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec3)
Theorem 2.4.4 Quotient uleR
f
If f and g earentiabledi(cid:11)er at x , g(x)̸=0, then the derivative of at x exists and
g
(cid:20) (cid:21) 0 0
d f(x) g(x)f (x)−g (x)f(x)
=
dx g(x) (g(x))2
ofoPr
f(x+h) f(x)
−
(cid:20) (cid:21)
d f(x) g(x+h) g(x) g(x)f(x+h)−f(x)g(x+h)
= lim = lim
dx g(x) h→0 h h→0 h(g(x)g(x+h))
g(x)f(x+h)−f(x)g(x+h)−f(x)g(x)+f(x)g(x)−f(x)g(x+h)
= lim
h→0 h(g(x)g(x+h))
g(x)[f(x+h)−f(x)] f(x)[g(x+h)−g(x)]
lim − lim
= h→0 h h→0 h
lim(g(x)g(x+h))
h→0
[f(x+h)−f(x)] [g(x+h)−g(x)]
g(x) lim −f(x) lim
= h→0 h h→0 h
lim(g(x)g(x+h))
h→0
0 0
g(x)f (x)−g (x)f(x)
=
(g(x))2
Note: lim g(x+h)=g(x) because g is given differentiable and therefore is continuous.
h→0
5. The Chain Rule
Theorem 2.4.5 If y =f(u) is aentiabledi(cid:11)erfunction of u, and u=g(x) is aentiabledi(cid:11)erfunction of
x, then y =f(g(x)) is a entiabledi(cid:11)er function of x and
DRAFT
d 0 0
[f(g(x))]=f (g(x)).g (x)
dx
dy
Example 2.4.15 Euateval for the folownlig functions.
dx
3 √
1. y =4x 3+ +2 x−7
x
Sol
1
2. y =3cosx− sinx
2
Sol
1 1 √
3. y =x 7+ x−2− √ + x3
3 x
Sol
(pg 10) 2 THE DIFFERENTIATION


## Page 29

Semester 1 - Calculus I(lec3) Faculty of Computer Science (CS+IT)
4. y =xsinx
Sol
5. y =x3cosx+x2−5
Sol
6. y =(x+4)(x2−x+5)
Sol
DRAFT
3x2+1
7. y =
6x+5
Sol
1+cosx
8. y =
1−sinx
Sol
9. y =2−x+3x+1
Sol
2 THE DIFFERENTIATION (pg 11)


## Page 30

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec3)
10. y =log (x)−2lnx
4
Sol
11. y =xsin(3x+4)
Sol
sinx+cosx
12. y =
sinx−cosx
Sol
T
F
A
R
D
(cid:16) (cid:112) (cid:17)
13. y =log x+ x2+1
3
Sol
Exercise 2.4.2 1. omrFthe (cid:12)rst principles, evaluate the (cid:12)rst derivative for the following function.
(i) y =x 3
x
(ii) y =
x2−5
(pg 12) 2 THE DIFFERENTIATION


## Page 31

Semester 1 - Calculus I(lec3) Faculty of Computer Science (CS+IT)
(iii) y =sin2x
(iv) y =xe−x
dy
2. Find for the following:
dx
(a) y =sin(xcos2x)
T
F
A
x2+ax+b R
(b) y =
x2−ax+b D
(cid:113) √
(c) y = 1+ 2x−1
(cid:18) (cid:19)
2x
(d) y =sin2
x+1
1+2tan2x
(e) y =
1−tan2x
2 THE DIFFERENTIATION (pg 13)


## Page 32

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec3)
(f) y =ln(secx+tanx)
1
(g) y = p √
1+ x
x2
(h) y = √
a2−x2
(i) y
=xe−x2
DRAFT
(j) y =xcos(sin2x)
(pg 14) 2 THE DIFFERENTIATION


## Page 33

Semester 1 - Calculus I(lec4) yacultFfo Computer Science (CS+IT)
Lecture Four
1 Trigonometric Functions
1.1 Sine Function
Properties of y = sin(x):
• 8x 2 R; sin(Γx) = Γsin(x)
• 8x 2 R; sin(x+2ß) = sin(x)
• 8k 2 Z; sin(x+2kß) = sin(x)
− (cid:1)
• sin π Γx = cos(x)
2
− (cid:1)
• sin π +x = cos(x)
2
1.2 Cosine Function
y = cosx is the cosine function, and ew wkno eth domain D = R dan the range R = Γ1;[ 1]
and it is an enev function.
T Properties of y = cos(x):
F
A • 8x 2 R; cos(Γx) = scox
R
D • 8x 2 R; cos(x+2ß) = oscx
• 8k 2 I; cos(x+2kß) = cosx
(cid:16) (cid:17)
ß
• 8x 2 R; cos Γx = sinx
2
(cid:16) (cid:17)
ß
• 8x 2 R; cos +x = Γsinx
2
1.3 Tangent Function
(cid:26) (cid:27)
sinx (2k Γ1)ß
y = tanx = is the ttangen function, ew wokn the domain D = RΓ ;k 2 I
cosx 2
and the range R = R and it is an odd function.
Properties of y = tan(x):
• 8x 2 D; tan(Γx) = Γtanx
• 8x 2 D; tan(x+2ß) = tanx
• 8k 2 I;x 2 D; ant(x+k2 ß) =
tanx
(cid:16) (cid:17)
ß
• 8x 2 D; tan Γx = cotx
2
(cid:16) (cid:17)
ß
• 8x 2 D; cos +x = Γcotx
2
1 TRIGONOMETRIC FUNCTIONS (pg 1)


## Page 34

yacultFof Computer Science (CS+IT) Semester 1 - Calculus I(lec4)
1.4 Cotangent Function
cosx
y = cotx = is the tangencot function, and ew wkno the domain D = R Γ fkß;k 2 Ig
sinx
and the range R = R and it is an odd function.
Properties of y = cot(x):
• 8x 2 D; cot(Γx) = Γcotx
• 8x 2 D; cot(x+2ß) = cotx
• 8k 2 I;x 2 D; otc(x+k2 ß) = cotx
(cid:16) (cid:17)
ß
• 8x 2 D; cot Γx = tanx
2
(cid:16) (cid:17)
ß
• 8x 2 D; cot +x = Γtanx
2
1.5 Secant Function
(cid:26) (cid:27)
1 (2k Γ1)ß
y = secx = is thetsecanfunction, andewwknothe aindom D = RΓ ;k 2 I
cosx 2
and the range R = RΓ(Γ1;1) and it is an enev function.
Pr T operties of y = sec(x):
F
A
• 8x 2 D; sec(Γx) = secx
R
D
• 8x 2 D; sec(x+2ß) = secx
• 8k 2 I;x 2 D; sec(x+2kß) = secx
(cid:16) (cid:17)
ß
• 8x 2 D; sec Γx = cscx
2
(cid:16) (cid:17)
ß
• 8x 2 D; sec +x = Γcscx
2
1.6 Cosecant Function
(cid:26) (cid:27)
1 (2k Γ1)ß
y = cscx = is the tcosecan function, ew wkno the domain D = RΓ ;k 2 I
sinx 2
and the range R = RΓ(Γ1;1) and it is an odd function.
Properties of y = csc(x):
• 8x 2 D; csc(Γx) = Γcscx
• 8x 2 D; csc(x+2ß) = cscx
• 8k 2 I;x 2 D; sec(x+2kß) = cscx
(cid:16) (cid:17)
ß
• 8x 2 D; csc Γx = secx
2
(cid:16) (cid:17)
ß
• 8x 2 D; csc +x = secx
2
(pg 2) 1 TRIGONOMETRIC FUNCTIONS


## Page 35

Semester 1 - Calculus I(lec4) yacultFfo Computer Science (CS+IT)
2 Differentiation of Trigonometric Functions
2.1 The Rules
d
1. [sinx] = cosx
dx
d
2. [cosx] = Γsinx
dx
d
3. [tanx] = sec 2 x
dx
Proof
(cid:20) (cid:21)
d d sinx cosxΘcosxΓsinxΘΓsinx
[tanx] = =
dx dx cosx cos 2 x
cos 2 x+sin 2 x 1
= = = sec 2 x
cos 2 x cos 2 x
d
4. [cotx] = Γcsc 2 x
dx
Proof
T
F
d d (cid:104)cosx (cid:105) sinxΘΓsinxΓcosA xΘcosx sin 2 x+cos 2 x
[cotx] = = R = Γ
dx dx sinx D sin 2 x sin 2 x
1
= Γ = Γcsc 2 x
sin 2 x
d
5. [secx] = secx:tanx
dx
Proof
(cid:20) (cid:21)
d d 1 cosxΘ0Γ1ΘΓsinx sinx
[secx] = = =
dx dx cosx cos 2 x cos 2 x
1 sinx
= : = secx:tanx
cosx cosx
d
6. [cscx] = Γcscx:cotx
dx
Proof
(cid:20) (cid:21)
d d 1 sinxΘ0Γ1Θcosx cosx
[cscx] = = = Γ
dx dx sinx sin 2 x sin 2 x
1 cosx
= Γ : = Γcscx:cotx
sinx sinx
In general:
2 TIONDIFFERENTIAOF TRIGONOMETRIC FUNCTIONS (pg 3)


## Page 36

yacultFof Computer Science (CS+IT) Semester 1 - Calculus I(lec4)
No. Therig.T unctionF etivaDeriv
d
(1) [sinu(x)] u′(x)cosu(x)
dx
d
(2) [cosu(x)] Γu ′(x):sinu(x)
dx
d
(3) [tanu(x)] u′(x)sec 2 u(x)
dx
d
(4) [cotu(x)] Γu ′(x)csc 2 u(x)
dx
d
(5) [secu(x)] u′(x)secu(x)tanu(x)
dx
d
(6) [cscu(x)] Γu ′(x)cscu(x)cotu(x)
dx
2.2 Examples
dy
Example 2.2.1 Find for the following functions:
dx
1. y = 3sin(2x 2 +5)Γosc 3 x
Sol
T
dy
= 3Θ4xΘcos(2x 2 +5)Γ3Θcos 2 F x(Γsinx) = 12xcos(2x 2 +5)+3sinxcos 2 x
dx A
R
2. y = 4sec(cosx 2 +1)
D
Sol
dy − (cid:1)
= 4 Γ2xsinx 2 sec(cosx 2 +1)tan(cosx 2 +1)
dx
= Γ8xsinx 2 sec(cosx 2 +1)tan(cosx 2 +1)
√
3. y = tan(xsecx)
Sol
p
Let w = tan(xsecx) ↽ y = w i.e. y = f(w). And let u = xsecx
i.e. u = h(x) ↽ w = tanu i.e. w = g(u). Hence
dy dy dw du
= : :
dx dw du dx
dy 1 dw du
Now: = p ; = sec 2 u ; = xsecxtanx+secx. Therefore:
dw 2 w du dx
dy 1 sec 2 (xsecx)
= p Θsec 2 uΘ(xsecxtanx+secx) = √ :(xsecxtanx+secx)
dx 2 w 2 tan(xsecx)
(cid:18) (cid:19)
sinx
4. y =
cotx+tanx
(pg 4) 2 TIONDIFFERENTIAOF TRIGONOMETRIC FUNCTIONS


## Page 37

Semester 1 - Calculus I(lec4) yacultFfo Computer Science (CS+IT)
Sol
sinx
We can write as:
cotx+tanx
sinx sinx sinx
= = = sin 2 xcosx
cotx+tanx cosx sinx cos 2 x+sin 2 x
+
sinx cosx sinxcosx
dy dy du
Now y = csc(sin 2 xcosx), let u = sin 2 xcosx ↽ y = cscu and = : . Therefore:
dx du dx
dy du
= Γcscucotu ; = Γsin 3 x+cosx(2sinxcosx) = sin2xoscxΓsin 3 x
du dx
dy
∴ = ΓcscucotuΘ(sin2xcosxΓsin 3 x)
dx
= Γ(sin2xcosxΓsin 3 x)csc(sin 2 xcosx)cot(sin 2 xcosx)
3 The Inverse Trigonometric Functions
3.1 The Inverse Sine Function T
F
A
R
D
Let x = siny, then the ersevin sine
function is y = arcsin(x) = sin −1 x, the
domain of itionde(cid:12)n is D = [Γ1;1], the
(cid:104) (cid:105)
ß ß
range R = Γ ; , and it is an odd
2 2
function, where sin −1 (Γx) = Γsin −1 x.
The derivative of inverse sin function
dy dy 1
y = sin −1 x ↽ x = siny ↽ 1 = cosy ↽ =
dx dx cosy
(cid:113) (cid:104) (cid:105)
ß ß
And ew wkno ttha cosy = Σ 1Γsin 2 y. Since y 2 Γ ; ↽ cosy ¿ 0, hence
2 2
(cid:113)
cosy = 1Γsin 2 y
Therefore
dy 1
= p
dx 1Γx 2
3 THE INVERSE TRIGONOMETRIC FUNCTIONS (pg 5)


## Page 38

yacultFof Computer Science (CS+IT) Semester 1 - Calculus I(lec4)
3.2 The Inverse Cosine Function
Let x = cosy, then the ersevin cosine
function is y = arccos(x) = cos −1 x, the
domain of itionde(cid:12)n is D = [Γ1;1], the
range R = [0;ß], and it is an odd
function, where cos −1 (Γx) = cos −1 x .
The derivative of inverse cos function
dy dy Γ1
y = cos −1 x ↽ x = cosy ↽ 1 = Γsiny ↽ =
dx dx siny
√
And ew wkno ttha siny = Σ 1Γcos 2 y. Since y 2 [0;ß] ↽ siny ¿ 0, hence
√
siny = 1Γcos 2 y
T
Therefore F
A
dy Γ1
R=
p
Ddx 1Γx 2
3.3 The Inverse Tangent Function
Let x = tany, then the ersevinttangen
function is y = arctan(x) = tan −1 x, the
domain of itionde(cid:12)n is D = R, the erang
(cid:16) (cid:17)
ß ß
R = Γ ; , and it is an odd function,
2 2
where tan −1 (Γx) = Γtan −1 x.
The derivative of inverse tan function
dy dy 1
y = tan −1 x ↽ x = tany ↽ 1 = sec 2 y ↽ =
dx dx sec 2 y
eWwkno sec 2 y = 1+tan 2 y = 1+x 2
dy 1
∴ =
dx 1+x 2
(pg 6) 3 THE INVERSE TRIGONOMETRIC FUNCTIONS


## Page 39

Semester 1 - Calculus I(lec4) yacultFfo Computer Science (CS+IT)
3.4 The Inverse Cotangent Function
Let x = coty, then the ersevinttangen
function is y = cot −1 x, the domain of
de(cid:12)nition is D = R, the range R = (0;ß),
and it is an odd function, where
cot −1 (Γx) = Γcot −1 x.
The derivative of inverse cot function
dy dy Γ1
y = cot −1 x ↽ x = coty ↽ 1 = Γcsc 2 y ↽ =
dx dx csc 2 y
eWwkno csc 2 y = 1+cot 2 y = 1+x 2
dy Γ1
∴ =
dx 1+x 2
3.5 The Inverse Secant Function T
F
A
R
D
Let x = secy, then the ersevin cosine
function is y = sec −1 x, the domain of
de(cid:12)nition is D = RΓ(Γ1;1), the range
(cid:104) (cid:17) (cid:16) (cid:105)
ß ß
R = 0; ♭ ;ß , and it is an enev
2 2
function, where sec −1 (Γx) = sec −1 x .
The derivative of inverse sec function
dy dy 1
y = sec −1 x ↽ x = secy ↽ 1 = secy tany ↽ =
dx dx secy tany
√ (cid:104) ß (cid:17)
And ew wkno tany = Σ sec 2 y Γ1, either y 2 0; this implies that tany ¿ 0 and ew
2
√ √ (cid:16) ß (cid:105)
etak tany = sec 2 y Γ1 and usth secy tany = jsecyj sec 2 y Γ1 ¿ 0 or y 2 ;ß ,
2
√
hwhic is implies that tany & secy ¡ 0 ↽ tany = Γ sec 2 y Γ1 and usth secytany =
√
jsecyj sec 2 y Γ1 ¿ 0. wNo
dy 1 dy 1
= √ ↽ = p
dx jsecyj sec 2 y Γ1 dx jxj x2 Γ1
3 THE INVERSE TRIGONOMETRIC FUNCTIONS (pg 7)


## Page 40

yacultFof Computer Science (CS+IT) Semester 1 - Calculus I(lec4)
3.6 The Inverse Cosecant Function
Let x = cscy, then the ersevin cosine
function is y = csc −1 x, the domain of
de(cid:12)nition is D = RΓ(Γ1;1), the range
(cid:104) (cid:17) (cid:16) (cid:105) (cid:104) (cid:105)
ß ß ß ß
R = Γ ;0 ♭ 0; = Γ ; Γf0g,
2 2 2 2
and it is an odd function, where
csc −1 (Γx) = Γcsc −1 x .
The derivative of inverse csc function
dy dy Γ1
y = csc −1 x ↽ x = cscy ↽ 1 = Γcscy coty ↽ =
dx dx cscy coty
√ (cid:104) ß (cid:17)
And ew wkno coty = Σ csc 2 y Γ1, either y 2 Γ ;0 this pliesim that sccy ¿ 0 and ew
2
√ √ (cid:16) ß (cid:105)
etak coty = Γ sec 2 y Γ1 and suth cscy coty = jcscyj csc 2 y Γ1 ¿ 0 ro y 2 0; , hwhic
2
√ √
T
is implies that cscy ¿ 0 ↽ coty = csc 2 y Γ1 and usth sccycoty = jcscyj csc 2 y Γ1 ¿ 0.
F
wNo
A
dy Γ1 R dy Γ1
= √ ↽ = p
dx jcscyj csc D2 y Γ1 dx jxj x2 Γ1
dy
Example 3.6.2 Find for the following functions:
dx
x
1. y = sin −1 2x
2
Sol
dy x 2 1 x 1
= :p + sin −1 2x = p + sin −1 2x
dx 2 1Γ4x 2 2 1Γ4x 2 2
2. y = cos −1 (xcosx)
Sol
d − (cid:1) Γu ′(x)
Let u = xcosx ↽ u ′(x) = cosxΓxsinx and we know cos −1 (u(x)) = √
dx 1Γ(u(x)) 2
dy Γ(cosxΓxsinx) xsinxΓcosx
∴ = √ = p
dx 1Γ(xcos(x)) 2 1Γx 2 cos 2 x
tan −1 x
3. y =
x2 +1
Sol
(pg 8) 3 THE INVERSE TRIGONOMETRIC FUNCTIONS


## Page 41

Semester 1 - Calculus I(lec4) yacultFfo Computer Science (CS+IT)
 
1
(x 2 +1)Θ Γtan −1 xΘ(2x)
dy  x2 +1  1Γ2xtan −1 x
= =
 
dx (x 2 +1) 2 (x 2 +1) 2
(cid:18) (cid:19)
tanx+1
4. y = tan −1
tanxΓ1
Sol
d × (cid:3) u′(x)
We know that tan −1 (u(x)) =
dx 1+(u(x)) 2
dy 1 (tanxΓ1)Θsec 2 xΓ(tanx+1)Θsec 2 x
∴ = (cid:18) (cid:19) Θ
dx tanx+1 2 (tanxΓ1) 2
1+
tanxΓ1
(cid:18) (cid:19)
(tanxΓ1) 2 sec 2 x[tanxΓ1ΓtanxΓ1]
= Θ
(tanx+1) 2 +(tanxΓ1) 2 (tanxΓ1) 2
Γ2sec 2 x Γ2sec 2 x
= = = Γ1
2(tan 2 x+1) 2sec 2 x
tanx+1
Another Solution: We can write as:
tanxΓ1
T
sinx
F
+1
tanx+1
=
cosx
=
sinx+cosxA
=
sin 2 x+2xsinxcosx+cos 2 x
tanxΓ1 sinx sinx R Γcosx sin 2 xΓcos 2 x
Γ1
D
cosx
(cid:20) (cid:21)
1+sin2x
= Γ = Γ[sec2x+tan2x]
cos2x
(cid:18) (cid:19)
tanx+1
Now, tan −1 = Γtan −1 [sec2x+tan2x]
tanxΓ1
(cid:18) (cid:19) (cid:18) (cid:19)
dy 2sec2xtan2x+2sec 2 x 2sec2xtan2x+2sec 2 x
∴ = Γ = Γ
dx 1+(sec2x+tan2x) 2 1+sec 2 x+2sec2xtan2x+tan 2 x
(cid:18) (cid:19)
2sec2xtan2x+2sec 2 x
= Γ = Γ1:
2sec2xtan2x+2sec 2 x
Another Solution:
 
ß
(cid:18)
tanx+1
(cid:19) (cid:18)
tanx+1
(cid:19) tanx+tan
4
y = tan −1 = Γtan −1 = Γtan −1  
tanxΓ1 1Γtanx
1ΓtanxΘtan
ß
4
(cid:16) (cid:16) (cid:17)(cid:17) (cid:16) (cid:17)
ß ß ß dy
= Γtan −1 tan x+ = Γ x+ ↽ y = ΓxΓ ↽ = Γ1
4 4 4 dx
dy
Exercise 3.6.1 Find for the following functions.
dx
1.
y = 2sin −1 (xΓ1)
3 THE INVERSE TRIGONOMETRIC FUNCTIONS (pg 9)


## Page 42

yacultFof Computer Science (CS+IT) Semester 1 - Calculus I(lec4)
Sol
2. (cid:16) (cid:17) (cid:16) (cid:17)
x a
y = tan −1 +2sin −1
a x
Sol
3.
cos −1 x2
y =
x+1
Sol
T
F
A
R
D
4.
y = ex 2sin −1 x
Sol
5.
y = sin −1 2x+cos −1 2x
Sol
6.
p
y = xcos −1 xΓ 1Γx 2
(pg 10) 3 THE INVERSE TRIGONOMETRIC FUNCTIONS


## Page 43

Semester 1 - Calculus I(lec4) yacultFfo Computer Science (CS+IT)
Sol
7.
1 (cid:104) p (cid:16) x (cid:17)(cid:105)
y = x 4Γx 2 +4sin −1
2 2
Sol
8.
y = cosx:sec −1 x
Sol
T
F
A
R
D
9.
1
y = e sin −1x + p
1+x 2
Sol
10. (cid:20) (cid:21) (cid:20) (cid:21)
x 1
y = csc Γsec −1 x+
x+1 x
Sol
3 THE INVERSE TRIGONOMETRIC FUNCTIONS (pg 11)


## Page 44

yacultFof Computer Science (CS+IT) Semester 1 - Calculus I(lec4)
11.
cot −1 x
y =
1+x 2
Sol
12.
y = ln(xΓtanx)
Sol
13. (cid:20) (cid:21)
1Γx
y = csc −T 1
x+1
F
A
RSol
D
14.
(cid:114)
x+1
y = ln +tan −1 2x
xΓ1
Sol
(pg 12) 3 THE INVERSE TRIGONOMETRIC FUNCTIONS


## Page 45

Semester 1 - Calculus I(lec5) Faculty of Computer Science (CS+IT)
Lecture Five
1 Exponential and Logarithmic Functions
1.1 Exponential Function
Definition 1.1.1 Let a > 0, a ̸= 1, then the exponential function of the base a ia y = ax.
1.1.1 Some Properties of the exponential function
For y = ax,
1. If a > 1, then:
(a) ax > 0 ,∀x ∈ R
(b) y = ax is an increasing function.
(c) lim ax → 0
x→−∞
(d) lim ax → ∞
x→+∞
(e) f(0) = a0 = 1, ∀a > 1, the graph of ax passes through the point (0,1) on y−axis.
2. If 0 < a < 1, then: T
F
(a) ax > 0 ,∀x ∈ R A
R
(b) y = ax will be decreasing funDction.
(c) lim ax → ∞
x→−∞
(d) lim ax → 0
x→+∞
(e) f(0) = a0 = 1, ∀a < 1, the graph of ax passes through the point (0,1) on y−axis.
Theorem 1.1.1 Prove that
x2 x3 xk (cid:88) ∞ xk
ex = 1+x+ + +···+ +··· =
2! 3! k! k!
k=0
Proof
(cid:16) x(cid:17)n
We know ex = lim 1+ , now:
n→∞ n
(cid:16) x(cid:17)n (cid:18) n (cid:19) x (cid:18) n (cid:19) x2 (cid:18) n (cid:19) x3 (cid:18) n (cid:19) xk
1+ = 1+ + + +···+ +...
n 1 n 2 n2 3 n3 k nk
x n(n−1)x2 n(n−1)(n−2)x3 n(n−1)(n−2)...xk
= 1+n. + + +···+ +...
n 2! n2 3! n3 k! nk
(cid:18) (cid:19) (cid:18) (cid:19)(cid:18) (cid:19)
1 1 1 1 2
=1+x+ 1− x2 + 1− 1− x3 +···+
2! n 3! n n
(cid:18) (cid:19)(cid:18) (cid:19) (cid:18) (cid:19)
1 1 2 k −1
1− 1− ... 1− xk
k! n n n
1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS (pg 1)


## Page 46

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec5)
(cid:16) x(cid:17)n (cid:88) ∞ xk (cid:18) 1 (cid:19)(cid:18) 2 (cid:19) (cid:18) k −1 (cid:19)
Therefore 1+ = 1− 1− ... 1− and this implies that:
n k! n n n
k=0
(cid:16) x(cid:17)n (cid:88) ∞ xk (cid:18) 1 (cid:19)(cid:18) 2 (cid:19) (cid:18) k −1 (cid:19)
lim 1+ = lim 1− 1− ... 1− =
n→∞ n n→∞ k! n n n
k=0
(cid:16) x(cid:17)n (cid:88) ∞ xk x2 x3
⇒ ex = lim 1+ = = 1+x+ + +...
n→∞ n k! 2! 3!
k=0
Example 1.1.1 Evaluate the following sums using the definition of exponential function ex:
(cid:88) ∞ 2k
1.
k!
k=1
Sol
(cid:32) (cid:33)
(cid:88) ∞ 2k (cid:88) ∞ 2k 20 (cid:88) ∞ 2k (cid:88) ∞ 2k
= 1+ −1 = + −1 = −1 = e2 −1.
k! k! 0! k! k!
k=1 k=1 k=1 k=0
(cid:88) ∞ (−1)k
2.
T
k!
k=2 F
A
RSol
D
(cid:88) ∞ (−1)k (cid:88) ∞ (−1)k (−1)0 (−1)1 (cid:88) ∞ (−1)k (cid:88) ∞ (−1)k
= 1−1+ = + + = = e−1.
k! k! 0! 1! k! k!
k=2 k=2 k=2 k=0
(cid:88) ∞ (−1)k
3.
2k−1k!
k=2
Sol
(cid:18)
−1
(cid:19)k  (cid:18)
−1
(cid:19)k 
(cid:88) ∞ (−1)k (cid:88) ∞ (−1)k (cid:88) ∞ 4 (cid:88) ∞ 4 1
= 2× = 2× = 2× −1+ 
2k−1k! 4kk! k!  k! 4
 
k=2 k=2 k=2 k=2
 1 
− 3 2 3
= 2e 4 −  = √ − .
4 4 e 2
Example 1.1.2 Find the following limits using ex definition.
1−e2x +2x
1. lim
x→0 x2
Sol
(pg 2) 1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS


## Page 47

Semester 1 - Calculus I(lec5) Faculty of Computer Science (CS+IT)
x2 x3
We know that ex = 1+x+ + +...
2! 3!
4x2 8x3 4
This implies that e2x = 1+2x+ + +··· = 1+2x+2x2 + x3 +.... Now:
2! 3! 3
(cid:18) (cid:19) (cid:18) (cid:19)
4 4
1+2x− 1+2x+2x2 + x3 +... 2x2 + x3 +...
1−e2x +2x 3 3
= = −
x2 x2 x2
(cid:18) (cid:19)
4
= − 2+ x+...
3
1−e2x +2x (cid:18) 4 (cid:19)
∴ lim = − lim 2+ x+... = −2.
x→0 x2 x→0 3
eax −1
2. lim ,b ̸= 0
x→0 sinbx
Sol
We can write the numerator as follows:
(cid:88) ∞ (ax)k (cid:18) a2x2 a3x3 (cid:19) a2x2 a3x3
eax −1 = −1 = 1+ax+ + +... −1 = ax+ + +...
k! 2! 3! 2! 3!
k=0
a2x2 a3x3
ax+ + +...
a2x2 a3x3
2! 3!
ax+ + +...
eax −1
∴ lim = lim 2! 3! = lim x
x→0 sinbx x→0 sinbx T x→0 sinbx
F
x
A
a2x2 a3x3
ax+ R+ +...
D2! 3!
lim
a
= x→0 x =
sinbx b
lim
x→0 x
ax −bx
3. lim
x→0 x
Sol
For you
1.1.2 Derivative of the Exponential Function
1.
d du
(cid:2) (cid:3)
au(x) = au(x) ×lna×
dx dx
2.
d du
(cid:2) eu(x) (cid:3) = eu(x) ×lne× = u′(x)eu(x)
dx dx
And when u(x) = x ⇒
1.
d
[ax] = axlna
dx
2.
d
[ex] = ex
dx
1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS (pg 3)


## Page 48

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec5)
1.2 Logarithmic Functions
Definition 1.2.2 Let a > 0, a ̸= 1. The logarithmic function of the base a is y = log x,
a
and it is the inverse of y = ax. The domain of definition of it D = R+ = (0,∞) and R = R.
Note that if the base is e, it is called the natural logarithm, and we denoted by lnx (log x =
e
lnx) and thus lnx is the inverse of ex.
1.2.1 Properties:
No. log ln
(1) log 1 = 0 ln1 = 0
a
(2) log x+log y = log xy lnx+lny = lnxy
a a a
(3) log xn = nlog x lnxn = nlnx
a a
1 1
(4) log = −log x ln = −lnx
a x a x
x x
(5) log x−log y = log lnx−lny = ln
a a a y y
1 1
(6) log b = lnb =
a log a T log e
b b
F
1 1
(7) log x = loAg x log x = lnx
an nR a en n
D
(8) log xn = log x log xn = lnx
an a en
1.2.2 Derivative of Logarithmic Function
1.
d 1 du
[log u(x)] = ×
dx a u(x)lna dx
2.
d 1 du
[lnu(x)] = ×
dx u(x) dx
And if u(x) = x ⇒
1.
d 1
[log x] =
dx a xlna
2.
d 1
[lnx] =
dx x
Derivative of [f(x)]g(x):
Let y = (f(x))g(x), then the derivative evaluated as follows:
y = [f(x)]g(x) ⇒ lny = g(x)lnf(x)
(pg 4) 1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS


## Page 49

Semester 1 - Calculus I(lec5) Faculty of Computer Science (CS+IT)
Now, by differentiating both sides w.r.t x, we get:
y′ f′(x)
= g(x)× +g′(x)lnf(x)
y f(x)
Therefore the derivative will be:
(cid:20) f′(x) (cid:21)
y′ = g(x)× +g′(x)lnf(x) ×y
f(x)
Example 1.2.3 Find the first derivative of the following function:
1. y =
esin2(4x)
Sol
dy
=
2(sin4x)×(4cos4x)×esin2(4x)
= 8sin4xcos4x
esin2(4x).
dx
2x2+8
2. y = e 4x+1
Sol
dy (cid:18) (4x+1)(4x)−(2x2 +8)(4) (cid:19) 2x2+8 4x−8x2 −12 2x2+8
= e 4x+1 = e 4x+1 .
dx (4x+1)2 (4x+1)2
T
F
3. y = x3e2x2−1 A
R
D Sol
dy (cid:16) (cid:17)
= x3 4x×e2x2−1 +e2x2−1 ×(3x2) = 4x4e2x2−1 +3x2e2x2−1
dx
tanx
4. y = esin(cosx)
Sol
dy (cid:20) sin(cosx)sec2x+tanx(sinxcos(cosx)) (cid:21)
tanx
= esin(cosx)
dx sin2(cosx)
dy
Example 1.2.4 Find for the following functions:
dx
1
(a) y = 2x + √
3x
Sol
x x
(cid:18) (cid:19)
− dy − 1 ln3
y = 2x +3 2 ⇒ = 2xln2+3 2 ×ln3× − = 2xln2− √
dx 2 2 3x
4x −1
(b) y =
4x +1
Sol
1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS (pg 5)


## Page 50

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec5)
dy (4x +1)(4xln4)−(4x −1)(4xln4)
=
dx (4x +1)2
4xln4(4x +1−4x +1) 22x+1ln4
= =
(4x +1)2 (4x +1)2
(c) y = xsec−1x
Sol
By tanking ln for both sides ⇒ lny = sec−1xlnx, now:
1dy sec−1x lnx
= + √
ydx x |x| x2 −1
Therefore, the required derivative is:
dy (cid:20) sec−1x lnx (cid:21)
= + √ xsec−1x
dx x |x| x2 −1
(x+1)3(x2 +4)8
(d) y = √
4 x2 +2
Sol
Firstly we take the ln for both sides:
T
(cid:20) (x+1)3(xF2 +4)8(cid:21)
lny = ln √
A
4 x2 +2
R
1
= 3ln(xD+1)+8ln(x2 +4)− ln(x2 +2)
4
Then we differentiate both sides, we get:
1dy 3 2x 1 2x
= +8× −
ydx x+1 x2 +4 4x2 +2
Finally, we multiply both sides by y to obtain the derivative:
dy (x+1)3(x2 +4)8 (cid:20) 3 16x x (cid:21)
= √ + −
dx 4 x2 +2 x+1 x2 +4 2(x2 +2)
(e) xsiny = [sin(x+y)]y
Sol
By taking the ln for both sides, the given function can be written as:
sinylnx = yln(sin(x+y))
Now, we differentiate both sides:
siny cos(x+y) (cid:16) (cid:17)
+y′cos(y)lnx = y 1+y′
x sin(x+y)
Therefore:
siny
ycot(x+y)−
y′ = x
cos(y)lnx−cot(x+y)
(pg 6) 1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS


## Page 51

Semester 1 - Calculus I(lec5) Faculty of Computer Science (CS+IT)
(f) x = 2y −2−y
Sol
Differentiate both sides directly:
dy dy dy 1
1 = 2yln2 +2−yln2 ⇒ =
dx dx dx (2y +2−y)ln2
dy
Exercise 1.2.1 1. Find for the following:
dx
(i) y = πx −xπ
Sol
(ii) y = esin3x
Sol
T
F
A
R
(iii) y = ln(x2 −1)
D
Sol
(cid:18) 2x −x (cid:19)
(iv) y = ln
2x +x
Sol
(cid:18) (cid:19)
x
(v) y = log
3 2x −x
Sol
(cid:16) (cid:17)
(vi) y = tan−1 e−x2
Sol
1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS (pg 7)


## Page 52

Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec5)
√
(vii) y = sin ex −1
Sol
ln(x)+1
(viii) y =
ln(x)−1
Sol
√
(x+1)3 x2 +4
(ix) y = √
3 x+2
Sol
T
F
(cid:20) (cid:18) (cid:19)(cid:21)
x+1
A
(x) y = ln ln
x−1 R
D
Sol
sin4(x)cos3(x)
(xi) y = √
x
Sol
(xii) xy = 2x−y
Sol
(xiii) y +x = yx
Sol
(pg 8) 1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS


## Page 53

Semester 1 - Calculus I(lec5) Faculty of Computer Science (CS+IT)
2. Find the following limits:
lnx
(a) lim
x→1 x−1
Sol
1−e2x
(b) lim
x→0 x
Sol
eax −ebx
(c) lim
x→0 x
Sol
T
F
A
e−x −e2x
R
(d) lim
x→0 x D
Sol
e−x2 −1
(e) lim
x→0 x
Sol
1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS (pg 9)

