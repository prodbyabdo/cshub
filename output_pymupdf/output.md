Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)

### **Lecture Two** **1 Limit of the Function**


**1.1** **Introduction**



Given the function _f_ ( _x_ ) = _[x]_ [3] _[ −]_ [1]

_x −_ 1 [, clearly it is not defined at] _[ x]_ [ = 1, and we want to study the behaviour of this]

function when _x_ approaches to 1.


_y_











_x_



The following table shows:



|x|0.75|0.9|T<br>0.99|0.999|
|---|---|---|---|---|
|_f_(_x_)|2.313|2.710|2.970|2.997|


**From the left**

|x|D<br>1.001|1.01|1.1|1.25|
|---|---|---|---|---|
|_f_(_x_)|3.003|3.030|3.310|3.813|



**From the right**



We can move arbitrarily close to 1 and as a result _f_ ( _x_ ) moves arbitrarily close to 3, and here we can say the



limit of the function _f_ ( _x_ ) = _[x]_ [3] _[ −]_ [1]



_x −_ 1 [is 3 when] _[ x]_ [ goes to 1. This limit is written as:]



_x_ [3] _−_ 1
lim
_x→_ 1 _x −_ 1 [= 3]



**In general** : If _f_ ( _x_ ) becomes arbitrarily close to a single number _L_ as _x_ approaches _c_ from either sides, the
limit of _f_ ( _x_ ) as _x_ approaches _c_ is _L_,and we can write it as:


lim
_x→c_ _[f]_ [(] _[x]_ [) =] _[ L]_


**1.2** **Definition of limit**


Let _f_ be a function defined on an open interval containing _c_ (except possibly at _c_ ) and let _L_ be a real number.
The statement lim
_x→c_ _[f]_ [(] _[x]_ [) =] _[ L]_ [ means that for each] _[ ϵ >]_ [ 0 there exist] _[ δ >]_ [ 0 such that if][ 0] _[ <][ |][x][ −]_ _[c][|][ < δ]_ [, then]

_|f_ ( _x_ ) _−_ _L| < ϵ_ .


**Example 1.2.1** _Prove that_ lim
_x→_ 3 [(2] _[x]_ [ + 3) = 9] _[.]_


_Proof_


_We must show that for each ϵ >_ 0 _, there exists a δ >_ 0 _such that |_ (2 _x_ +3) _−_ 9 _| < ϵ whenever_ 0 _< |x−_ 3 _| < δ, because_
_our choice of δ depends on ϵ. Now we need to establish a connection between the absolute value |_ (2 _x_ + 3) _−_ 9 _|_
_and |x −_ 3 _|._
_|_ (2 _x_ + 3) _−_ 9 _|_ = _|_ 2 _x −_ 6 _|_ = 2 _|x −_ 3 _|_


1 LIMIT OF THE FUNCTION (pg 1)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)



_So for a given ϵ >_ 0 _, we can choose δ_ = _[ϵ]_

2 _[. This choice works because]_



0 _< |x −_ 3 _| < δ_ = _[ϵ]_

2



_implies that_

                        - _ϵ_
_|_ (2 _x_ + 3) _−_ 9 _|_ = 2 _|x −_ 3 _| <_ 2

2


**1.3** **One Sided Limit**




= _ϵ._



1. **Left Hand Limit** : We mean by L-H-L, limit of the function when _x_ increasing to _c,_ ( _x ̸_ = _c_ ), i.e. ( _x < c_ )
and _x →_ _c_ and we denote it by

lim
_x→c_ _[−]_ _[f]_ [(] _[x]_ [)]


To evaluate the left limit, we substitute _x_ = _c −_ _ϵ_ on _f_ ( _x_ ), then we take limit when _ϵ →_ 0. ( _ϵ >_ 0)


lim
_x→c_ _[−]_ _[f]_ [(] _[x]_ [) = lim] _ϵ→_ 0 _[f]_ [(] _[c][ −]_ _[ϵ]_ [)]


2. **Right Hand Limit** : We mean by R-H-L, limit of the function when _x_ decreasing to _c,_ ( _x ̸_ = _c_ ), i.e.
( _x > c_ ) and _x →_ _c_ and we denote it by

lim
_x→c_ [+] _[ f]_ [(] _[x]_ [)]


To evaluate the left limit, we substitute _x_ = _c_ + _ϵ_ on _f_ ( _x_ ), then we take limit when _ϵ →_ 0. ( _ϵ >_ 0)


lim
_x→c_ [+] _[ f]_ [(] _[x]_ [) = lim] _ϵ→_ 0 _[f]_ [(] _[c]_ [ +] _[ ϵ]_ [)]


And the limit of the function **will be exists** if and only if:


lim
_x→c_ [+] _[ f]_ [(] _[x]_ [) = lim] _x→c_ _[−]_ _[f]_ [(] _[x]_ [)]



_|x|_
**Example 1.3.2** _Find the limit_ lim
_x→_ 0 _x_ _[using L-H-L and R-H-L]_


_Sol_


_1. L-H-L:_



_|x|_
lim
_x→_ 0 [+] _x_



_x|_ _|_ 0 _−_ _ϵ|_

_x_ [= lim] _ϵ→_ 0 0 _−_ _ϵ_



_|_ 0 _−_ _ϵ|_ _[| −]_ _[ϵ][|]_ = lim _ϵ_

[= lim] _ϵ→_ 0 0 _−_ _ϵ_ [=] _−ϵ_ _ϵ→_ 0 _−ϵ_


= lim
_ϵ→_ 0 _[−]_ [1 =] _[ −]_ [1] _[.]_



0 _−_ _ϵ|_ _[| −]_ _[ϵ][|]_

0 _−_ _ϵ_ [=] _−ϵ_



_2. R-H-L:_



_|x|_
lim
_x→_ 0 [+] _x_



_x|_ _|_ 0 + _ϵ|_

_x_ [= lim] _ϵ→_ 0 0 + _ϵ_



_|_ 0 + _ϵ|_ _[|][ϵ][|]_ _ϵ_

[= lim] _ϵ→_ 0 0 + _ϵ_ [=] _ϵ_ [= lim] _ϵ→_ 0 _ϵ_


= lim
_ϵ→_ 0 [1 = 1] _[.]_



0 + _ϵ|_ _[|][ϵ][|]_

0 + _ϵ_ [=] _ϵ_



_Since_ lim
_x→_ 0 [+] _[ f]_ [(] _[x]_ [)] _[ ̸]_ [= lim] _x→_ 0 _[−]_ _[f]_ [(] _[x]_ [)] _[, therefore the limit does not exist.]_



_x_ [2] + _x −_ 2
**Example 1.3.3** _Find the limit_ lim _using L-H-L and R-H-L_
_x→_ 1 _x −_ 1


_Sol_



_x_ [2] + _x −_ 2
_1. L-H-L_ lim
_x→_ 1 _[−]_ _x −_ 1



_x_ [2] + _x −_ 2
lim
_x→_ 1 _[−]_ _x −_ 1



+ _x −_ 2 (1 _−_ _ϵ_ ) [2] + (1 _−_ _ϵ_ ) _−_ 2

= lim
_x −_ 1 _ϵ→_ 0 (1 _−_ _ϵ_ ) _−_ 1



_ϵ→_ 0 (1 _−_ _ϵ_ ) _−_ 1 _ϵ→_ 0 _−ϵ_ _ϵ→_ 0 _−ϵ_


= lim
_ϵ→_ 0 [(3] _[ −]_ _[ϵ]_ [) = 3] _[ −]_ [0 = 3]



) [2] + (1 _−_ _ϵ_ ) _−_ 2 1 _−_ 2 _ϵ_ + _ϵ_ [2] + 1 _−_ _ϵ −_ 2

= lim
(1 _−_ _ϵ_ ) _−_ 1 _ϵ→_ 0 _−ϵ_



+ 1 _−_ _ϵ −_ 2 _ϵ_ ( _ϵ −_ 3)

= lim
_−ϵ_ _ϵ→_ 0 _−ϵ_



(pg 2) 1 LIMIT OF THE FUNCTION


Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)



_x_ [2] + _x −_ 2
_2. R-H-L:_ lim
_x→_ 1 [+] _x −_ 1



_x_ [2] + _x −_ 2
lim
_x→_ 1 [+] _x −_ 1



_ϵ→_ 0 (1 + _ϵ_ ) _−_ 1 _ϵ→_ 0 _ϵ_ _ϵ→_ 0 _ϵ_


= lim
_ϵ→_ 0 [(] _[ϵ]_ [ + 3) = 0 + 3 = 3]



) [2] + (1 + _ϵ_ ) _−_ 2 1 + 2 _ϵ_ + _ϵ_ [2] + 1 + _ϵ −_ 2

= lim
(1 + _ϵ_ ) _−_ 1 _ϵ→_ 0 _ϵ_



+ _x −_ 2 (1 + _ϵ_ ) [2] + (1 + _ϵ_ ) _−_ 2

= lim
_x −_ 1 _ϵ→_ 0 (1 + _ϵ_ ) _−_ 1



+ 1 + _ϵ −_ 2 _ϵ_ ( _ϵ_ + 3)

= lim
_ϵ_ _ϵ→_ 0 _ϵ_



_Since R-H-L = L-H-L, the limit exists and equal to 3._


**1.4** **Properties of Limits**


**Theorem 1.4.1** _Let b and c be real numbers and let n be a positive integer._


_1._

lim
_x→c_ _[b]_ [ =] _[ b]_


_2._

lim
_x→c_ _[x]_ [ =] _[ c]_



_3._


**Example 1.4.4** _Evaluate the limits_


_1._


_2._


_3._



lim
_x→_ 2 _[x]_ [2][ = (2)][2][ = 4]



lim
_x→c_ _[x][n]_ [ =] _[ c][n]_



lim
_x→_ 2 [3 = 3]


lim
_x→−_ 4 _[x]_ [ =] _[ −]_ [4]



**Theorem 1.4.2** _Let b and c be real numbers and let n be a positive integer, and let f and g be functions with_
_the following limits._
lim _,_ lim
_x→c_ _[f]_ [(] _[x]_ [) =] _[ L]_ _x→c_ _[g]_ [(] _[x]_ [) =] _[ K]_


_then_


_1. Scalar multiple_
lim
_x→c_ [[] _[bf]_ [(] _[x]_ [)] =] _[ b]_ [ lim] _x→c_ _[f]_ [(] _[x]_ [) =] _[ bL]_


_2. Sum or Difference_
lim
_x→c_ [[] _[f]_ [(] _[x]_ [)] _[ ±][ g]_ [(] _[x]_ [)] = lim] _x→c_ _[f]_ [(] _[x]_ [)] _[ ±]_ [ lim] _x→c_ _[g]_ [(] _[x]_ [) =] _[ L][ ±][ K]_


_3. Product_
lim
_x→c_ [[] _[f]_ [(] _[x]_ [)] _[.g]_ [(] _[x]_ [)] = lim] _x→c_ _[f]_ [(] _[x]_ [)] _[.]_ [ lim] _x→c_ _[g]_ [(] _[x]_ [) =] _[ L.K]_


_4. Quotient_



_f_ ( _x_ )
lim
_x→c_ _g_ ( _x_ ) [= ][lim] lim _[x]_ _x_ _[→]_ _→_ _[c]_ _c_ _[ f]_ _g_ ( [(] _x_ _[x]_ ) [)]




[lim] _[x][→][c][ f]_ [(] _[x]_ [)] _[L]_

lim _x→c g_ ( _x_ ) [=] _K_



_, K ̸_ = 0
_K_



_5. Power_

                          -                           - _n_
lim lim = _L_ _[n]_ _._
_x→c_ [[] _[f]_ [(] _[x]_ [)]] _[n]_ [ =] _x→c_ _[f]_ [(] _[x]_ [)]


**Example 1.4.5** _By using theorems of limits evaluate the following limits._


_1._ lim
_x→_ 2 [(4] _[x]_ [2][ + 3)]


_Sol_


1 LIMIT OF THE FUNCTION (pg 3)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)


lim
_x→_ 2 [(4] _[x]_ [2][ + 3) = lim] _x→_ 2 [4] _[x]_ [2][ + lim] _x→_ 2 [3 = 4 lim] _x→_ 2 _[x]_ [2][ + lim] _x→_ 2 [3]

                  - �2
= 4 lim + lim
_x→_ 2 _[x]_ _x→_ 2 [3 = 4(2)][2][ + 3 = 19] _[.]_



_2._ lim
_x→_ 3


_3._ lim
_x→_ 4




- _x −_ 2 

_x_ + 2



_Sol_




[lim] _[x][→]_ [3] _[ x][ −]_ [lim] _[x][→]_ [3][ 2] [3] _[ −]_ [2]

lim _x→_ 3 _x_ + lim _x→_ 3 2 [=] 3 + 2




[3] _[ −]_ [2]

3 + 2 [= ][1] 5



5




- = [lim] _[x][→]_ [3][(] _[x][ −]_ [2)]




[lim] _[x][→]_ [3][(] _[x][ −]_ [2)]

lim _x→_ 3( _x_ + 2) [= ][lim] lim _[x]_ _x_ _[→]_ _→_ [3] 3 _[ x]_ _x_ _[ −]_ + lim [lim] _[x]_ _x_ _[→]_ _→_ [3] 3 [ 2]



lim
_x→_ 3




- _x −_ 2


_x_ + 2







25 _−_ _x_ [2]



_Sol_



2 [1] = - lim - lim �2 [�] 2 [1]
_x→_ 4 [25] _[ −]_ _x→_ 4 _[x]_



1         - 2
lim 2 = lim
_x→_ 4 [(25] _[ −]_ _[x]_ [2][)] _x→_ 4 [25] _[ −]_ _x_ [lim] _→_ 4 _[x]_ [2][�] [1]



2
= �25 _−_ (4) [2][�] [1] 2



2
= 3



_4._ lim
_x→_ 1 [(3] _[x]_ [2] _[ −]_ [1)(9] _[x]_ [ + 2)]


**Example 1.4.6** _Evaluate the following limits:_


_1._ lim
_x→_ 1 [(] _[x]_ [ + 4] _[ −]_ _[x]_ [2][)]



3 _x_ + 1
_2._ lim
_x→_ 3 _x_ + 2


_3._ lim
_x→_ 1 [(] _[x]_ [ + 4)(] _[x][ −]_ [1)]


_x_ + 2
_4._ lim
_x→_ 2 _x −_ 2



_Sol_


_Sol_


_Sol_


_Sol_



(pg 4) 1 LIMIT OF THE FUNCTION


Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)



_5._ lim
_x→∞_



3 + [1]

_x_
2 + _x_



4 _x_ + 1
_6._ lim
_x→∞_ _x_ + 9



_Sol_


_Sol_



_x_ [2] _−_ 1
_7._ lim
_x→−_ 1 _x_ + 1



_x_ [2] + 3 _x_ + 2
_8._ lim
_x→−_ 1 _x_ + 1



_Sol_


_Sol_



_x_ [5] _−_ 32
_9._ lim
_x→_ 2 _x_ [2] _−_ 4



_x_ + sin _x_
_10._ lim
_x→_ 0 tan _x_ + _x_



_Sol_


_Sol_


1 LIMIT OF THE FUNCTION (pg 5)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)


**1.5** **Strategies for Finding Limits**


Previously, we studied several types of functions whose limits can be evaluated by **direct substitution**, this
knowledge together with the following theorem can be used to develop a strategy for finding limits.


**Theorem 1.5.3** _Let c be a real number and let f_ ( _x_ ) = _g_ ( _x_ ) _for all x ̸_ = _c in an open interval containing c. If_
_the limit of g_ ( _x_ ) _as x approaches c exists, then the limit of f_ ( _x_ ) _also exists and:_


lim
_x→c_ _[f]_ [(] _[x]_ [) = lim] _x→c_ _[g]_ [(] _[x]_ [)]


**Example 1.5.7** _Evaluate the following limits:_



_x_ [2] _−_ _x −_ 2
_1._ lim
_x→_ 2 _x_ [2] _−_ 4


_By direct substitution, we get:_



_Sol_



(2) [2] _−_ 2 _−_ 2




[2] _[ −]_ [2] = [0]

4 _−_ 4 0




[2] _−_ 2 _−_ 2 = [4] _[ −]_ [2] _[ −]_ [2]

(2) [2] _−_ 4 4 _−_ 4



( _undetermined value_ )
0



_Now we try to find a function g that agrees with f for all x other than x_ = 2 _. By factoring and dividing_
_out like factors, we can rewrite the given function as:_



_f_ ( _x_ ) = _[x]_ [2] _[ −]_ _[x][ −]_ [2]



( _x −_ 2)( _x_ + 1) _[x]_ [ + 1]

( _x −_ 2)( _x_ + 2) [=] _x_ + 2




_[x][ −]_ [2] ( _x −_ 2)( _x_ + 1)

=
_x_ [2] _−_ 4 ( _x −_ 2)( _x_ + 2)



_x_ + 2 [=] _[ g]_ [(] _[x]_ [)] _[.]_



_So for all x−values other than x_ = 2 _the functions f and g agree, since_ lim
_x→_ 2 _[g]_ [(] _[x]_ [)] _[ exists, we can apply]_

_theorem 1.5.3 to conclude that f and g have the same limit at x_ = 2 _._



_x_ [2] _−_ _x −_ 2
lim
_x→_ 2 _x_ [2] _−_ 4




[2 + 1]

2 + 2 [= ][3] 4




_−_ _x −_ 2 ( _x −_ 2)( _x_ + 1) _x_ + 1

= lim
_x_ [2] _−_ 4 _x→_ 2 ( _x −_ 2)( _x_ + 2) [= lim] _x→_ 2 _x_ + 2 [= ][2 + 1] 2 + 2



4



_x_ [3] _−_ 1
_2._ lim
_x→_ 1 _x −_ 1



_Sol_



_By direct substitution we get_ [(1)][3] _[ −]_ [1]



0 _[. Then we try to find a function][ g][ that agrees with][ f][ for all][ x]_



_other than x_ = 1 _._




[1]

= [0]
1 _−_ 1 0





_x_ [3] _−_ 1





_f_ ( _x_ ) = _[x]_ [3] _[ −]_ [1]



= ( _x_ [2] + _x_ + 1) = _g_ ( _x_ )
( _x −_ 1)




[3] _[ −]_ [1]

_x −_ 1 [= ][(] _[x][ −]_ [1)(] ( _x_ _[x]_ _−_ [2][ +] 1) _[ x]_ [ + 1)]



_Thus_ lim
_x→_ 1 _[f]_ [(] _[x]_ [) = lim] _x→_ 1 _[g]_ [(] _[x]_ [) = lim] _x→_ 1 [(] _[x]_ [2][ +] _[ x]_ [ + 1) = 1][2][ + 1 + 1 = 3] _[.]_



_**Note that:**_ _the graph of the function g_ ( _x_ ) = _x_ [2] + _x_ + 1 _is same as f_ ( _x_ ) = _[x]_ [3] _[ −]_ [1]



_x −_ 1



(pg 6) 1 LIMIT OF THE FUNCTION


Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)


_y_













_x_ + 1
_3._ lim
_x→−_ 1 _x_ [2] + 4 _x_ + 3



_Sol_


_x_ + 1 _x_ + 1 1 1
lim
_x→−_ 1 _x_ [2] + 4 _x_ + 3 [= lim] _x→−_ 1 ( _x_ + 1)( _x_ + 3) [= lim] _x→−_ 1 ( _x_ + 3) [=] _−_ 1 + 3 [= ][1] 2



_x −_ 5
_4._ lim ~~_√_~~ ~~_√_~~
_x→_ 5 _x −_ 3 _−_ 2



_Sol_



_√_ _√_
_x −_ 3 +

~~_√_~~ ~~_√_~~

2 _[.]_ _x −_ 3 +



_√_ _√_

2 ( _x −_ 5) - _x −_ 3 +

2 [= lim] _x→_ 5 ( _x −_ 5)




 - _√_
2 =



_√_
2 +



_√_
2 = 2



2 _._



_√_
_x −_ 3 +



_x −_ 5
lim ~~_√_~~ ~~_√_~~
_x→_ 5 _x −_ 3 _−_



_x −_ 3 + 2

~~_√_~~ ~~_√_~~
_x −_ 3 + 2



2 ~~�~~



= lim
( _x −_ 5) _x→_ 5




- _√_



(1 + _x_ ) [2] _−_ 1
_5._ lim
_x→_ 0 _x_


_x_ [6] _−_ 1
_6._ lim
_x→_ 1 _x_ [2] _−_ 1



_Sol_


_Sol_


1 LIMIT OF THE FUNCTION (pg 7)



_7._ lim
_x→_ 3



1
_x_ _[−]_ [1] 3

_x_ [2] _−_ 9


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)


_Sol_



_8._ lim
_x→_ 4



_√_
~~_x_~~ _−_ 2

_x −_ 4



**Example 1.5.8** _Evaluate the following limits._



_Sol_


_Sol_



9 _x_ [2]
_1._ lim
_x→∞_ 2 _x_ [2] + 4


_By direct substitution, we get:_



9 _x_ [2] 9( _∞_ ) [2]

2 _x_ [2] + 4 [=] 2( _∞_ ) [2]



_,_ ( _undetermined value_ )
_∞_



9 _x_ [2]
lim
_x→∞_ 2 _x_ [2]



9( _∞_ ) [2] _[∞]_

2( _∞_ ) [2] + 4 [=] _∞_











9
=

4
2 +
_∞_ [2]



9 _x_ [2]
lim
_x→∞_ 2 _x_ [2] + 4

   - ~~��~~   _f_ ( _x_ )




~~�~~ ~~�~~ - ~~�~~
_g_ ( _x_ )



9
=
2 + 0 [= ][9] 2



= lim
_x→∞_



 _x_ [2] [9]
 ~~�~~
 [2]




~~�~~
_x_ [2] 2 + [4]












~~�~~








 [= lim] _x→∞_


_Sol_



9





2 + [4]



_x_ [2]



_x_ [2]



_x_ [3] _−_ _x_ [2] + 2
_2._ lim
_x→∞_ 2 _x_ [2] + _x_ + 1


_x_ [3] _−_ _x_ [2] + 2
lim
_x→∞_ 2 _x_ [2] + _x_ + 1

      - ~~��~~      _f_ ( _x_ )




 _x_ [3] 1 _−_ [1]



_x_ [3]



_x_ [3]




1 _−_ [1]















= lim
_x→∞_




~~�~~ 2
_x_ [3]



2 [1]

_x_ [+] _x_




[1] [2]

_x_ [+] _x_ [3]




~~�~~ 2



2 [1]

_x_ [+] _x_




[1] [2]

_x_ [+] _x_ [3]




~~�~~ 2 1 1

_∞_ [+] _∞_ [2] [+] _∞_ [3]




- 2
1 _−_ [1]

_∞_ [+] _∞_ [3]




[1] [1]

_x_ [2] [+] _x_ [3]




[1] [1]

_x_ [2] [+] _x_ [3]



=



= _∞_

~~�~~



_x_ [3]



= lim

~~�~~ _x→∞_



_x_ [3]




~~�~~




~~�~~ ~~��~~ ~~�~~
_g_ ( _x_ )



_x_ ( _x_ + 1)
_3._ lim
_x→∞_ _x_ [3] + 1



_Sol_


(pg 8) 1 LIMIT OF THE FUNCTION


Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)



6 _x_ + 1
_4._ lim ~~_√_~~
_x→∞_ 4 _x_ [2] + 3



_Sol_



( _x −_ 3)(2 _x_ + 1)
_5._ lim
_x→∞_ 2 _x_ [2] _−_ _x_ + 1


(3 _x_ + 4)( _x −_ 2)
_6._ lim
_x→∞_ _x_ (2 _x_ + 1)( _x_ + 2)



_Sol_


_Sol_



_7._ lim
_x→∞_



_√_

9 _x_ [2] + 5


_x_ + 3



**1.6** **Cauchy’s Theorem**


**Theorem 1.6.4** _**Cauchy’s Theorem:**_



_Sol_


_x_ _[n]_ _−_ _a_ _[n]_
lim = _na_ _[n][−]_ [1]
_x→a_ _x −_ _a_



_proof_


1 LIMIT OF THE FUNCTION (pg 9)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)


_By using_ _**long division**_ _, we get:_



_x_ _[n]_ _−_ _a_ _[n]_

= _x_ _[n][−]_ [1] + _ax_ _[n][−]_ [2] + _a_ [2] _x_ _[n][−]_ [3] + _· · ·_ + _a_ _[n][−]_ [1]
_x −_ _a_



_Therefore:_


**Lemma 1.6.1**



_x_ _[n]_ _−_ _a_ _[n]_
lim
_x→a_ _x_ _[m]_ _−_ _a_



_x_ _[n]_ _−_ _a_ _[n]_
lim
_x→a_ _x −_ _a_



= lim    - _x_ _[n][−]_ [1] + _ax_ _[n][−]_ [2] + _a_ [2] _x_ _[n][−]_ [3] + _· · ·_ + _a_ _[n][−]_ [1][�]
_x −_ _a_ _x→a_



= _a_ _[n][−]_ [1] + _a × a_ _[n][−]_ [2] + _a_ [2] _× a_ _[n][−]_ [3] + _· · ·_ + _a_ _[n][−]_ [1]

= _a_ _[n][−]_ [1] + _a_ _[n][−]_ [1] + _a_ _[n][−]_ [1] + _· · ·_ + _a_ _[n][−]_ [1] = _na_ _[n][−]_ [1]

~~�~~ ~~�~~  - ~~�~~
_n times_



_m_ _[a][n][−][m]_



_x_ _−_ _a_ _[n]_

_x_ _[m]_ _−_ _a_ _[m]_ [=] _m_



_proof_



_We can write f_ ( _x_ ) = _[x][n][ −]_ _[a][n]_




_[x][n][ −]_ _[a][n]_ _[x][n][ −]_ _[a][n]_

_x_ _[m]_ _−_ _a_ _[m]_ [=] _x −_ _a_




_[n][ −]_ _[a][n]_

_÷_ _[x][m][ −]_ _[a][m]_
_x −_ _a_ _x −_ _a_



_. Then the limit will be:_
_x −_ _a_



_x_ _[n]_ _−_ _a_ _[n]_
lim
_x→a_ _x_ _[m]_ _−_ _a_



_x_ _[n]_ _−_ _a_ _[n]_ _x_ _[n]_ _−_ _a_ _[n]_

_x_ _[m]_ _−_ _a_ _[m]_ [= lim] _x→a_ _x −_ _a_




_[n]_ _−_ _a_ _[n]_ _x_ _[m]_ _−_ _a_ _[m]_

_÷_ lim
_x −_ _a_ _x→a_ _x −_ _a_




_−_ _a_ _[m]_

= _[na][n][−]_ [1]
_x −_ _a_ _ma_ _[m][−]_




_[na]_ _[n]_

_ma_ _[m][−]_ [1] [=] _m_



_m_ _[a][n][−][m][.]_



**Lemma 1.6.2**


_Proof left for you._



_x −_ _a_
lim [1]
_x→a_ _x_ _[m]_ _−_ _a_ _[m]_ [=] _m_ _[a]_ [1] _[−][m]_



**Example 1.6.9** _Evaluate the following limits._



_x_ [5] _−_ 32
_1._ lim
_x→_ 2 _x_ [3] _−_ 8


_x_ [2] _−_ 16
_2._ lim
_x→_ 4 _x_ ~~_[√]_~~ ~~_x_~~ _−_ 8



_Sol_




[5] _−_ 32 _x_ [5] _−_ (2) [5]

_x_ [3] _−_ 8 [= lim] _x→_ 2 _x_ [3] _−_ (2) [3]




[5] [5]

3 [(2)][5] _[−]_ [3][ =] 3



_x_ [5] _−_ 32
lim
_x→_ 2 _x_ [3] _−_ 8



_xx_ [3] _−−_ (2)(2) [3] [= ][5] 3



3 _[.]_




[5]

3 [(2)][2][ = ][20] 3



_Sol_



_x_ [2] _−_ 16 _x_ [2] _−_ (4) [2]
_x_ lim _→_ 4 _x_ ~~_[√]_~~ ~~_x_~~ _−_ 8 [= lim] _x→_ 4 _x_ 32 _−_ (4) 32



3 (4) [2] _[−]_ 2 [3]
2



_x_ 3 _−_ (4) 3 [2] 3

_x_ 2 _−_ (4) 2 [=]



2 [3] = [4]



3




[4]

3 [(2) = ][8] 3



_√_



_x_ + ∆ _x −_ _[√]_ ~~_x_~~


∆ _x_


_√_


lim
∆ _x→_ 0



1 1

_x −_ ~~_x_~~ ( _x_ + ∆ _x_ ) 2 _−_ _x_ 2

= lim = [1]
∆ _x_ _x_ +∆ _x→x_ ( _x_ + ∆ _x_ ) _−_ _x_ 2



_3._ lim
∆ _x→_ 0



_Sol_



_x_ + ∆ _x −_ _[√]_ ~~_x_~~



1

[1] 2 _[−]_ [1] = [1]

2 _[x]_ 2



2

2 _[x][−]_ [1]




[1] 2 = 1

2 ~~_[√]_~~ ~~_x_~~



_x −_ 3
_4._ lim
_x→_ 3 _x_ [3] _−_ 27



_Sol_



_x −_ 3 _x −_ 3
lim
_x→_ 3 _x_ [3] _−_ 27 [= lim] _x→_ 3 _x_ [3] _−_ (3) [3] [= ][1] 3




[1]

3 _[.]_ [1]




[1] [1]

3 [(3)][1] _[−]_ [3][ =] 3




[1] [1]

9 [=] 27



27 _[.]_



_x_ [3] + 1
_5._ lim
_x→−_ 1 _x_ + 1



_Sol_




[3] + 1 _x_ [3] _−_ ( _−_ 1) [3]

_x_ + 1 [= lim] _x→−_ 1 _x −_ ( _−_ 1)



_x_ [3] + 1
lim
_x→−_ 1 _x_ + 1



= 3( _−_ 1) [3] _[−]_ [1] = 3( _−_ 1) [2] = 3 _._
_x −_ ( _−_ 1)



(pg 10) 1 LIMIT OF THE FUNCTION


Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)


**1.7** **The squeeze Theorem**


**Theorem 1.7.5** _Assume the functions f, g and h satisfy f_ ( _x_ ) _≤_ _g_ ( _x_ ) _≤_ _h_ ( _x_ ) _for all values of x near a, except_
_possibly at a._

_If_ lim
_x→a_ _[f]_ [(] _[x]_ [) = lim] _x→a_ _[h]_ [(] _[x]_ [) =] _[ L, then]_ [ lim] _x→a_ _[g]_ [(] _[x]_ [) =] _[ L]_


**1.8** **Limit of Trigonometric Functions**


We have some important limits:


1. lim
_x→_ 0 [sin] _[ x]_ [ = 0]


2. lim
_x→_ 0 [cos] _[ x]_ [ = 1]



sin _x_
3. lim = 1
_x→_ 0 _x_



sin _ax_
4. lim = 1
_ax→_ 0 _ax_



tan _x_
5. lim = 1
_x→_ 0 _x_



tan _ax_
6. lim = 1
_ax→_ 0 _ax_



tan _x_
**Example 1.8.10** _1. Prove that_ lim = 1
_x→_ 0 _x_



_Sol_



_x_ sin _x_ sin _x_

= lim
_x_ _x→_ 0 _x_ cos _x_ [= lim] _x→_ 0 _x_



tan _x_
lim
_x→_ 0 _x_



_x_ 1 1

_._ lim
_x_ _x→_ 0 cos _x_ [= 1] _[ ×]_ cos 0 [= 1] _[ ×]_ [ 1 = 1]



sin 2 _x_
_2._ lim
_x→_ 0 _x_



_Sol_



sin 2 _x_
lim
_x→_ 0 _x_



_x_ 2 sin 2 _x_

= lim
_x_ 2 _x→_ 0 2 _x_



_x_ sin 2 _x_

= 2 lim
2 _x_ 2 _x→_ 0 2 _x_



= 2 _×_ 1 = 2
2 _x_



tan 3 _x_
_3._ lim
_x→_ 0 2 _x_



_Sol_



tan 3 _x_
lim
_x→_ 0 2 _x_



_x_ = [1]

2 _x_




[1] tan 3 _x_

2 _x_ [lim] _→_ 0 _x_



_x_ = [1]

_x_




[1] 3 tan 3 _x_

2 3 [lim] _x→_ 0 3 _x_



_x_ = [3]

3 _x_




[3] tan 3 _x_

2 3 [lim] _x→_ 0 3 _x_



_x_ = [3]

3 _x_ 2




[3]

2 _[×]_ [ 1 = ][3] 2



2 _[.]_



1 LIMIT OF THE FUNCTION (pg 11)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)



tan _x_ + sin 3 _x_
_4._ lim
_x→_ 0 _x_



_Sol_



tan _x_ + sin 3 _x_
lim
_x→_ 0 _x_



+ sin 3 _x_ tan _x_

= lim
_x_ _x→_ 0 _x_



_x_ sin 3 _x_

+ lim
_x_ _x→_ 0 _x_



_x_ tan _x_

= lim
_x_ _x→_ 0 _x_



_x_ sin 3 _x_

+ 3 lim
_x_ 3 _x→_ 0 3 _x_



= 1 + 3 _×_ 1 = 4 _._
3 _x_



2 _x_ + sin _x_
_5._ lim
_x→_ 0 4 _x_ + tan 5 _x_


2 _x_ + sin _x_
lim
_x→_ 0 4 _x_ + tan 5 _x_ [= lim] _x→_ 0



_Sol_







2 _x_ + sin _x_







_x_



_x_
4 _x_ + tan 5 _x_



_x_ 4 _x_ + tan 5 _x_

_÷_ lim
_x_ _x→_ 0 _x_








2 _x_ + sin _x_
 = lim
 _x→_ 0 _x_



_x_




 - sin _x_
= lim
_x→_ 0 [2 + lim] _x→_ 0 _x_

 - sin _x_
= lim
_x→_ 0 [2 + lim] _x→_ 0 _x_



5 _x_







_x_




- - tan 5 _x_
_÷_ lim
_x→_ 0 [4 + lim] _x→_ 0 _x_



_x_







_x_




- - tan 5 _x_
_÷_ lim
_x→_ 0 [4 + 5 lim] 5 _x→_ 0 5 _x_



= [2 + 1]




[2 + 1]

4 + 5 [= ][3]




[3]

9 [= ][1] 3



3 _[.]_




    - 3
_6._ lim
_x→∞_ _[x]_ [ sin] _x_







_x_



_Sol_



_Let u_ = [3]




[3] [3]

_x_ _[⇒]_ _[x]_ [ =] _u_



_u_ _[and][ u][ →]_ [0] _[ as][ x][ →∞][. Thus]_




   - 3
lim
_x→∞_ _[x]_ [ sin] _x_




- 3 sin _u_
= lim = 3 _×_ 1 = 3 _._
_u→_ 0 _u_ [sin] _[ u]_ [ = 3 lim] _u→_ 0 _u_


_Sol_



1 _−_ cos _x_
_7._ lim
_x→_ 0 _x_ [2]



1 _−_ cos _x_
lim
_x→_ 0 _x_ [2]




[1 + cos] _[ x]_ 1 _−_ cos [2] _x_ sin [2] _x_ sin [2] _x_

1 + cos _x_ [= lim] _x→_ 0 _x_ [2] (1 + cos _x_ ) [= lim] _x→_ 0 _x_ [2] (1 + cos _x_ ) [= lim] _x→_ 0 _x_ [2]



cos _x_

_×_ [1 + cos] _[ x]_
_x_ [2] 1 + cos _x_



_x_ 1

_×_ lim
_x_ [2] _x→_ 0 (1 + cos _x_ )




 - sin _x_
= lim
_x→_ 0 _x_



2



_x_



�2 1 1
_×_ lim
_x→_ 0 (1 + cos _x_ ) [= 1] _[ ×]_ (1 + cos 0) [= ][1] 2



**1.9** **The Number e**


We define the number _e_ by the limit




1 + [1]




- _x_



_e_ = lim
_x→∞_



_x_



Proof

- - _x_ - _x_ - - _x_ 1 + [1] = 1 + _._ [1] _._ [1]

[+]




_._ [1]




[1] - _x_

_x_ [+] 2




_._ [1]




[1]  - _x_

_x_ [2] [+] 3




[1]  - _x_

_x_ [3] [+] _[ · · ·]_ [ +] _n_




_._ [1]

_x_ _[n]_



_x_




- _x_ - _x_
= 1 +
1




_._ [1]




- _._ 1 _−_ [3]







_x_



=



_x_



_n_ =0



1

_n_ !




1 _−_ [1]




- _._ 1 _−_ [2]



_x_



_x_




- _. . ._ 1 _−_ _[n][ −]_ [1]



_x_



Therefore the limit will be:



_x_



_n_ =0




- 1
lim
_x→∞_ _n_ !




1 _−_ [1]




1 + [1]



_x_




- _._ 1 _−_ [2]




- _. . ._ 1 _−_ _[n][ −]_ [1]

_x_



��



lim
_x→∞_



_x_




- _x_
=



_x_




- _._ 1 _−_ [3]

_x_



3! [+] _[ . . .]_



= =



_x_



_n_ =0



1 [1]
_n_ ! [= 1 + 1 +]




[1] [1]

2! [+]



The number _e_ satisfied the inequality 2 _< e <_ 3, and its value ≊ 2 _._ 71828, and we can write the limit as:




~~�~~
1 + [1]



_e_ = lim
_n→∞_



_n_




~~�~~ _n_ 1
= lim _n_
_n→_ 0 [(1 +] _[ n]_ [)]



(pg 12) 1 LIMIT OF THE FUNCTION


Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)


**1.10** **The Exponential Theorem**



**Theorem 1.10.6**


_We know that e_ = lim
_n→∞_




1 + [1]

_n_



_e_ _[x]_ = 1 + _x_ + _[x]_ [2]




_[x]_ [2] _[x]_ [3]

2 [+] 3



3 [+] _[ · · ·]_ [ =]



_∞_




_n_ =0



_x_ _[n]_


_n_ !



_Proof_



_n_




- _n_ - _x_
= lim
_n→∞_




- _n_
_._


    _⇒_ _e_ _[x]_ = lim
_n→∞_



_n_




1 + [1]




- _nx_




1 + [1]



_put m_ = _nx ⇒_ _e_ _[x]_ = lim
_m→∞_




1 + _[x]_



_m_




- _m_
_, therefore the limit will be:_




[1)(] _[m][ −]_ [2)] _x_ [3]


3! _m_




_[ −]_ [1)] _x_ [2]

2! _m_ [2]



_x_ [2] _[m]_ [(] _[m][ −]_ [1)(] _[m][ −]_ [2)]

_m_ [2] [+] 3!



_x_ [3] 
_m_ [3] [+] _[ . . .]_



_⇒_ lim
_m→∞_


= lim
_m→∞_




1 + _[mx]_






1 + _x_ +




_[mx]_ _[m]_ [(] _[m][ −]_ [1)]

_m_ [+] 2!



+
2!











��
1 _−_ [2]








1 _−_ [1]



_m_








1 _−_ [1]

_m_


_Sol_



+ _. . ._
3!



_m_




[2] _[x]_ [3]

2! [+] 3!



= 1 + _x_ + _[x]_ [2]



3! [+] _[ . . .]_



1
**Example 1.10.11** _1._ lim _x_
_x→_ 0 [(1 +] _[ x]_ [)]




[1] [1]

_x_ _[⇒]_ _[x]_ [ =] _u_



_put u_ = [1]



_u_ _[and][ u][ →∞]_ _[as][ x][ →]_ [0]




- _u_
= _e._




1 + [1]



_u_



1
lim _x_ = lim
_x→_ 0 [(1 +] _[ x]_ [)] _u→∞_


_Sol_




- _x_
_α ̸_ = 0



_2._ lim
_x→∞_




1 + _[α]_

_x_



_(i) If α >_ 0 _, let x_ = _αu_


lim
_x→∞_



_x_




- _x_
= lim
_u→∞_



_u_




- _u_ - _α_
= _e_ _[α]_ _._



_αu_




1 + _[α]_




- _αu_ = lim
_u→∞_




1 + _[α]_




1 + [1]



_(ii) If α <_ 0 _⇒_ _let x_ = _−αu_




 = lim
_u→∞_



_u_




- _−u_ [�] _[α]_




- _u_
_u −_ 1




- _u_ - _α_





lim
_u→∞_




1 _−_ [1]



_αu_




- _−αu_
=



lim
_x→∞_




1 + _[α]_



_x_




- _x_
= lim
_u→∞_




1 _−_ _[α]_




  = lim
_u→∞_




- 1 - _u_ - _α_
1 +
_u −_ 1



_Now let u −_ 1 = _y ⇒_ _u_ = 1 + _y_ ( _y →∞_ _as u →∞._




1 + [1]

_y_





lim
_y→∞_




- _u_ - _α_
=




- _y_ +1 [�] _[α]_




1 + _[α]_



lim
_x→∞_



_x_




 - _x_ = lim
_u→∞_




- 1
1 +
_u −_ 1



_y_




  = lim
_y→∞_




1 + [1]



_y_




- _y_
_×_ lim
_y→∞_




1 + [1]



�� _α_
= ( _e ×_ 1) _[α]_ = _e_ _[α]_ _._



1 LIMIT OF THE FUNCTION (pg 13)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)




- _x_




- _x_ + 3



_3._ lim
_x→∞_



_x −_ 2



_Sol_


_Let u_ = _x −_ 2 _⇒_ _x_ = _u_ + 2 _⇒_ ( _u →∞_ ) _as_ ( _x →∞_ )




- _u_ + 2 + 3


_u_




1 + [5]

_u_




1 + [5]

_u_




1 + [5]

_u_




- _x_
= lim
_u→∞_




- _u_ +2
= lim
_u→∞_




- _u_ +2
= lim
_u→∞_




- _u_
_._ lim
_u→∞_



�2
= _e_ [5]



_⇒_ lim
_x→∞_




- _x_ + 3

_x −_ 2



**Exercise 1.10.1** _Evaluate the following limits._



_x_ [2] _−_ 2 _x −_ 3
_1._ lim
_x→_ 3 _x −_ 3



_Sol_



_x_ [2] _−_ 16
_2._ lim
_x→_ 4 4 _−_ _x_



( _x −_ _b_ ) [50] _−_ _x_ + _b_
_3._ lim
_x→b_ _x −_ _b_



_Sol_


_Sol_


_Sol_



_4._ lim
_h→_ 0



1
5 + _h_ _[−]_ [1] 5

_h_




  - 1 1

_5._ lim
_w→_ 1 _w_ [2] _−_ _w_ _[−]_ _w −_ 1







_Sol_


(pg 14) 1 LIMIT OF THE FUNCTION


Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)


_x_ [2] + 2 _x_ + 9
_6._ lim
_x→∞_ 3 _x_ [3] + _x_ + 1


_Sol_



_√_



_7._ lim
_x→_ 1


_8._ lim
_n→∞_




- 1 + 2 + 3 + _· · ·_ + _n_

_n_ [2]



9 _x_ [2] + 7

3 _x_ + 1



_Sol_







_x_ [3] + _x_ [2] + 5 _x −_ 5
_9._ lim
_x→_ 1 _x −_ 1



_Sol_


_Sol_



1 1
_x −_ 1 [+] _x_ + 1
_x_











_10._ lim
_x→_ 0











_x_ [3] ( _x −_ 1) [6] _−_ 8
_11._ lim
_x→_ 2 _x −_ 2



_Sol_


_Sol_


1 LIMIT OF THE FUNCTION (pg 15)



_12._ lim
_x→_ 2



_√_

_x_ [2] + 12 _−_ 4

_x −_ 2


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)


_Sol_



_x_ _[−]_ [1] _−_ 1
_13._ lim
_x→_ 1 _x −_ 1



_Sol_



4 _x_ [2] _−_ _x_ [2]
_14._ lim
_x→_ 4 2 _−_ ~~_[√]_~~ ~~_x_~~



4 _−_ _x_
_15._ lim ~~_√_~~
_x→_ 4 _x_ [2] + 9 _−_ 5



_Sol_


_Sol_


_Sol_


_Sol_



_16._ lim
_y→_ 8




_[√]_ 3
~~_y_~~ _−_ 2
_y_ ~~_[√]_~~ [3] ~~_y_~~ _−_ 16



_y_ [4] _−_ 81
_17._ lim
_y→_ 3 _y_ [2] _−_ 9



( _x_ + ∆ _x_ ) [3] _−_ _x_ [3]
_18._ lim
∆ _x→_ 0 ∆ _x_



_Sol_


(pg 16) 1 LIMIT OF THE FUNCTION


Semester 1 - Calculus I(lec2) Faculty of Computer Science (CS+IT)



_x_ [5] + 32
_19._ lim
_x→−_ 2 _x_ [3] + 8



4 _x_ + sin 3 _x_
_20._ lim
_x→_ 0 _x_


sin 3 _x_
_21._ lim
_x→_ 0 sin 9 _x_


sin 2 _x_
_22._ lim
_x→_ 0 _x_ [2] + 3 _x_



_Sol_


_Sol_



_Sol_


_Sol_



sin( _x −_ 2)
_23._ lim
_x→_ 2 _x_ [2] _−_ 4



1 _−_ cos 4 _x_
_24._ lim
_x→_ 0 _x_ [2]


tan 2 _x_ + 4 _x_
_25._ lim
_x→_ 0 _x_ + sin _x_ + tan _x_



_Sol_


_Sol_


_Sol_


1 LIMIT OF THE FUNCTION (pg 17)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec2)



cos 4 _x −_ cos 2 _x_
_26._ lim
_x→_ 0 _x_ [2]



_Sol_



_27._ lim [6]
_x→∞_ _[x]_ [ sin] _x_



_Sol_


(pg 18) 1 LIMIT OF THE FUNCTION


Semester 1 - Calculus I(lec3) Faculty of Computer Science (CS+IT)

### **Lecture Three** **1 The Continuity**


**1.1** **Continuity at a point on an open interval**



**Informally**, we might say that a function is continuous on an open interval if its graph can be drawn with a
pencil without lifting the pencil from the paper. i.e. A function _f_ is continuous at _x_ = _c_ means there is no
interruption in the graph of _f_ at _c_ . That is, its graph is unbroken at _c_ and there are no holes, jumps, or gaps.
The following figure identifies three values of _x_ at which the graph of _f_ is not continuous. At all other points
in the interval ( _a, b_ ) the graph of _f_ is uninterrupted and **continuous** .


Figure 1: Three cases for the discontinuity



**1.2** **Concept of Continuity**


**Definition 1.2.1** _**Continuity at a point**_ _:_
_A function f is continuous at c if the following three conditions are met._


_1. f_ ( _c_ ) _is defined_


_2._ lim
_x→c_ _[f]_ [(] _[x]_ [)] _[ exists.]_


_3. f_ ( _c_ ) = lim
_x→c_ _[f]_ [(] _[x]_ [)]


_**Continuity on an open interval**_ _:_
_A function is_ _**continuous on an open interval**_ ( _a, b_ ) _if it is continuous at each point in the interval._


**Definition 1.2.2** _Let f_ ( _x_ ) _be a_ _**defined function**_ _at x_ = _c, we say that f_ ( _x_ ) _is continuous at x_ = _c if the_
_following condition satisfied._

lim
_h→_ 0 [[] _[f]_ [(] _[c]_ [ +] _[ h]_ [)] _[ −]_ _[f]_ [(] _[c]_ [)] = 0]


**Example 1.2.1** _Given f_ ( _x_ ) = _x_ [2] _, prove that it is continuous on_ R _._


_Proof_


_To prove the function is continuous on_ R _, choose an arbitrary point x_ = _c, s.t c ∈_ R _._


lim          - _f_ ( _c_ + _h_ ) [2] _−_ _c_ [2][�] = lim          - _c_ [2] + 2 _ch_ + _h_ [2] _−_ _c_ [2][�]
_h→_ 0 [[] _[f]_ [(] _[c]_ [ +] _[ h]_ [)] _[ −]_ _[f]_ [(] _[c]_ [)] = lim] _h→_ 0 _h→_ 0


= lim
_h→_ 0 [[] _[h]_ [(2] _[c]_ [ +] _[ h]_ [)] = 0] _[ ×]_ [ (2] _[c]_ [ + 0) = 0] _[.]_


_⇒_ _f_ ( _x_ ) = _x_ [2] _is continuous at c ⇒_ _continuous at_ R _._


**Example 1.2.2** _Prove that the function f_ ( _x_ ) = cos _ax, continuous on_ R _._


_Proof_


1 THE CONTINUITY (pg 1)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec3)


_To prove the function is continuous on_ R _, choose an arbitrary point x_ = _c, s.t c ∈_ R _._




- - _ac_ + _ah_ + _ac_
sin



2



��



lim
_h→_ 0 [[] _[f]_ [(] _[c]_ [ +] _[ h]_ [)] _[ −]_ _[f]_ [(] _[c]_ [)] = lim] _h→_ 0 [[cos(] _[ac]_ [ +] _[ ah]_ [)] _[ −]_ [cos(] _[ac]_ [)] =] _[ −]_ [2 lim] _h→_ 0



2




- - _ac_ + _ah −_ _ac_
sin



2



��
= _−_ 2 _×_ sin _ac ×_ 0 = 0 _._



= _−_ 2 lim
_h→_ 0




- sin _ac_ + _[ah]_



2




- - _ah_
sin



_⇒_ _f_ ( _x_ ) = cos _ax is continuous at c ⇒_ _continuous at_ R _._


**Example 1.2.3** _Prove that the function f_ ( _x_ ) = _a_ _[x]_ _, a >_ 0 _is continuous on_ R _._


_Proof_


_To prove the function is continuous on_ R _, choose an arbitrary point x_ = _c, s.t c ∈_ R _._



lim - _a_ _[c]_ [+] _[h]_ _−_ _a_ _[c]_ [�] = lim - _a_ _[c]_ [ �] _a_ _[h]_ _−_ 1��
_h→_ 0 [[] _[f]_ [(] _[c]_ [ +] _[ h]_ [)] _[ −]_ _[f]_ [(] _[c]_ [)] = lim] _h→_ 0 _h→_ 0

= _a_ _[c]_ (1 _−_ 1) = _a_ _[c]_ _×_ 0 = 0



_⇒_ _f_ ( _x_ ) = _a_ _[x]_ _is continuous on_ R


**Example 1.2.4** _Prove that the function f_ ( _x_ ) = log _a x, a >_ 0 _is continuous on_ R [+] _._


_Proof_


_To prove the function is continuous on_ R _, choose an arbitrary point x_ = _c, s.t c >_ 0 _, c ∈_ R _._




- _c_ + _h_ ��


_c_



lim
_h→_ 0 [[] _[f]_ [(] _[c]_ [ +] _[ h]_ [)] _[ −]_ _[f]_ [(] _[c]_ [)] = lim] _h→_ 0 [[log] _[a]_ [(] _[c]_ [ +] _[ h]_ [)] _[ −]_ [log] _[a][ c]_ [] = lim] _h→_ 0




log _a_




1 + _[h]_

_c_



��
= log _a_




lim
_h→_ 0




1 + _[h]_

_c_



��
= log _a_ (1) = 0



= lim
_h→_ 0




log _a_



**Example 1.2.5** _Discuss the continuity of the function_



_f_ ( _x_ ) =




3 _x −_ 1 _, x <_ 1
2 _x_ [2] _, x ≥_ 1


_Sol_



_at x_ = 1 _._



_Here we will study the three conditions on definition 1.2.1._


_1. f_ (1) = 2(1) [2] = 2


_2. For finding the limit:_


lim
_x→_ 1 [+] _[ f]_ [(] _[x]_ [) = lim] _ϵ→_ 0 _[f]_ [(] _[a]_ [ +] _[ ϵ]_ [) = lim] _ϵ→_ 0 [2(1 +] _[ ϵ]_ [)][2][ = 2(1 + 0)][2][ = 2(1)][2][ = 2] _[.]_


lim
_x→_ 1 _[−]_ _[f]_ [(] _[x]_ [) = lim] _ϵ→_ 0 _[f]_ [(] _[a][ −]_ _[ϵ]_ [) = lim] _ϵ→_ 0 [3(1] _[ −]_ _[ϵ]_ [)] _[ −]_ [1 = 3(1)] _[ −]_ [1 = 3] _[ −]_ [1 = 2] _[.]_


_Since_ lim
_x→_ 1 [+] _[ f]_ [(] _[x]_ [) = lim] _x→_ 1 _[−]_ _[f]_ [(] _[x]_ [)] _[ ⇒]_ _x_ [lim] _→_ 1 _[f]_ [(] _[x]_ [)] _[ exists and]_ [ = 2]


_3. Clearly f_ (1) = lim
_x→_ 1 _[f]_ [(] _[x]_ [)] _[, therefore the given function is continuous at][ x]_ [ = 1] _[.]_


**Example 1.2.6** _Determine whether the following function is continuous at x_ = 0 _._






_f_ ( _x_ ) =





sin _πx_

_, x <_ 0
_x_
sin _πx_

_, x ≥_ 0
_x_ + 1


_Sol_



_1. f_ (1) = [sin(0] _[π]_ [)]




_[π]_ [)] = [0]

0 + 1



1 [= 0]



(pg 2) 1 THE CONTINUITY


Semester 1 - Calculus I(lec3) Faculty of Computer Science (CS+IT)


_2._



sin ( _π_ (0 + _ϵ_ ))
lim
_x→_ 0 [+] _[ f]_ [(] _[x]_ [) = lim] _ϵ→_ 0 _[f]_ [(] _[a]_ [ +] _[ ϵ]_ [) = lim] _ϵ→_ 0 0 + _ϵ_ + 1

sin ( _π_ (0 _−_ _ϵ_ ))
lim
_x→_ 0 _[−]_ _[f]_ [(] _[x]_ [) = lim] _ϵ→_ 0 _[f]_ [(] _[a][ −]_ _[ϵ]_ [) = lim] _ϵ→_ 0 0 _−_ _ϵ_



_π_ (0 + _ϵ_ )) sin _πϵ_

= lim
0 + _ϵ_ + 1 _ϵ→_ 0 _ϵ_ + 1



sin _πϵ_ [sin 0]

_ϵ_ + 1 [=] 0 + 1



= _π_
_ϵ_




[sin 0]

0 + 1 [= ][0]



1 [= 0]



_π_ (0 _−_ _ϵ_ )) sin _πϵ_

= lim
0 _−_ _ϵ_ _ϵ→_ 0 _ϵ_



_⇒_ lim
_x→_ 0 _[f]_ [(] _[x]_ [)] _[ not exist because]_ [ lim] _x→_ 0 [+] _[ f]_ [(] _[x]_ [)] _[ ̸]_ [= lim] _x→_ 0 _[−]_ _[f]_ [(] _[x]_ [)]


**Example 1.2.7** _Find the constant such that the function is continuous on the entire real line._



_1._


_2._


_3._


**1.3** **Properties of Continuity**



_f_ ( _x_ ) =


_f_ ( _x_ ) =




3 _x_ [2] _, x ≥_ 1

_ax −_ 4 _, x <_ 1








_, x <_ 0
_x_



4 sin _x_



 _a −_ 2 _x_ _, x ≥_ 0



_f_ ( _x_ ) =




1 _−_ 4 _x_ _, x <_ 2
_ax_ [2] _−_ 3 _x_ + 2 _, x ≥_ 2



**Theorem 1.3.1** _If b is a real number and f and g are continuous at x_ = _c, then the following functions are_
_also continuous at c_


_1. Scalar multiple: bf_


_2. Sum or Difference: f ± g_



_3. Product: fg_


_4. Quotient:_ _[f]_

_g_ _[, if][ g]_ [(] _[c]_ [)] _[ ̸]_ [= 0] _[.]_



**Note:** The following types of functions are continuous at every point in their domains.


(i) Polynomials


1 THE CONTINUITY (pg 3)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec3)



(ii) Rational _r_ ( _x_ ) = _[p]_ [(] _[x]_ [)] _, q_ ( _x_ ) _̸_ = 0

_q_ ( _x_ )




_[√]_ _n_
(iii) Radical: _f_ ( _x_ ) = ~~_x_~~


(iv) Trigonometric: sin _x,_ cos _x,_ tan _x,_ cot _x,_ sec _x,_ csc _x_


**Exercise 1.3.1** _Find the following:_


_1. Prove that f_ ( _x_ ) = sin( _ax_ ) _,_ ( _a ̸_ = 0) _is continuous on_ R _._


_2. Prove that f_ ( _x_ ) = _x_ [3] _−_ _x is continuous on_ R _._



_3. Discuss the continuity of the function f_ ( _x_ ) = ln( _x_ [2] + 1)


_4. Determine whether the following functions are continuous at the given points._



_(a) f_ ( _x_ ) =


_(b) f_ ( _x_ ) =




_x_ _[x]_ _−_ 1 _, x ̸_ = 0
1 _, x_ = 0 _[at][ x]_ [ = 0]



1 _−_ _x_ _at x_ = 1

_πx_ [2] _, x ≥_ 1








_, x <_ 1
1 _−_ _x_



_sin_ ( _πx_ )







(pg 4) 1 THE CONTINUITY


Semester 1 - Calculus I(lec3) Faculty of Computer Science (CS+IT)

### **2 The Differentiation**


**2.1** **The Change and Rate of Change**


Let _y_ = _f_ ( _x_ ) is a continuous function on an open interval _I_, ( _x ∈_ _I_ ).


1. The change on _x ≡_ ∆ _x_ = _x_ 2 _−_ _x_ 1 = _h_


2. The change on _y ≡_ ∆ _y_ = _f_ ( _x_ + _h_ ) _−_ _f_ ( _x_ )



3. The rate of change is [∆] _[y]_

∆ _x_



**Example 2.1.8** _If y_ = _x_ [3] _, find_ [∆] _[y]_

_h_



∆ _y_ _[f]_ [(] _[x]_ [ +] _[ h]_ [)] _[ −]_ _[f]_ [(] _[x]_ [)]
∆ _x_ [=] _h_


_Sol_



_y_

_h_ [= ][(] _[x]_ [ +] _[ h]_ _h_ [)][3] _[ −]_ _[x]_ [3]



∆ _y_




[)][3] _[ −]_ _[x]_ [3] �( _x_ + _h_ ) [2] + _x_ ( _x_ + _h_ ) + _x_ [2][�]

= _[h]_
_h_ _h_



_h_ _h_

= ( _x_ + _h_ ) [2] + _x_ ( _x_ + _h_ ) + _x_ [2] = 3 _x_ [2] + 3 _hx_ + _h_ [2]



_Therefore_ [∆] _[y]_ [+ 3] _[hx]_ [ +] _[ h]_ [2]

_h_ [=][ 3] _[x]_ [2]


**2.2** **Rate of Changes or Derivatives**


**Definition 2.2.3** _The derivative of f is the function:_



_′_ _dy_
_f_ ( _x_ ) =



_dy_ ∆ _y_

_dx_ [= lim] _h→_ 0 _h_



_y_ _f_ ( _x_ + _h_ ) _−_ _f_ ( _x_ )

_h_ [= lim] _h→_ 0 _h_



(2.2.1)
_h_



_′_
_provided the limit exists and x is in the domain of f_ _. If f_ ( _x_ ) _exists, we say that f is_ _**differentiable**_ _at x._


**Note:** If _f_ is differentiable at every point of an open interval _I_, we say that _f_ is differentiable on _I_ .



**Example 2.2.9** _Given y_ = _x_ [3] _, evaluate the rate of change_ _[dy]_

_dx_ _[.]_


_Sol_


_Since y_ = _x_ [3] _is a polynomial ⇒_ _continuous on_ R _. By using 2.2.1_



_dy_ _f_ ( _x_ + _h_ ) _−_ _f_ ( _x_ )
_dx_ [= lim] _h→_ 0 _h_



2 THE DIFFERENTIATION (pg 5)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec3)



_from example 2.1.8, we saw that_ _[f]_ [(] _[x]_ [ +] _[ h]_ [)] _[ −]_ _[f]_ [(] _[x]_ [)] = 3 _x_ [2] + 3 _hx_ + _h_ [2]

_h_


_L.S.L_ = lim
_h→_ 0 [+][(3] _[x]_ [2][ + 3] _[hx]_ [ +] _[ h]_ [2][) = lim] _h→_ 0 [(3] _[x]_ [2][ + 3] _[hx]_ [ +] _[ h]_ [2][) = 3] _[x]_ [2] _[.]_


_R.S.L_ = lim
_h→_ 0 _[−]_ [(3] _[x]_ [2][ + 3] _[hx]_ [ +] _[ h]_ [2][) = lim] _h→_ 0 [(3] _[x]_ [2][ + 3] _[hx]_ [ +] _[ h]_ [2][) = 3] _[x]_ [2]


_dy_
_Therefore_
_dx_ [= 3] _[x]_ [2]



**Example 2.2.10** _For the function y_ = _|x|, find_ _[dy]_

_dx_ _[at][ x]_ [ = 0] _[.]_


_Sol_


_We know that, the given function is continuous on_ R _._



_dy_ _f_ (0 + _h_ ) _−_ _f_ (0)
_dx_ [= lim] _h→_ 0 _h_



) _−_ _f_ (0) _f_ ( _h_ ) _−_ 0

= lim
_h_ _h→_ 0 _h_



) _−_ 0 _f_ ( _h_ )

= lim
_h_ _h→_ 0 _h_



_h_



_Now, we will study the existence of the limit by calculating the left and right limits._



_|h|_ _h_
_(i) L.S.L_ = lim
_h→_ 0 _[−]_ _h_ [= lim] _h→_ 0 _−h_ [=] _[ −]_ [1]



_|h|_ _h_
_(ii) L.S.L_ = lim
_h→_ 0 [+] _h_ [= lim] _h→_ 0 _h_ [= 1]



_Thus the limit does not exist at x_ = 0 _and here we say the function is not differentiable at x_ = 0 _._


**Theorem 2.2.2** _**Differentiable implies continuous**_


_Proof_


_Because f is differentiable at a point c, we know that:_


_′_ _f_ ( _x_ ) _−_ _f_ ( _c_ )
_f_ ( _c_ ) = lim
_x→c_ _x −_ _c_


_exists. To show that f is continuous at c, we mush show that_ lim
_x→c_ _[f]_ [(] _[x]_ [) =] _[ f]_ [(] _[c]_ [)] _[.]_

_We can write f_ ( _x_ ) _as:_



_f_ ( _x_ ) = _[f]_ [(] _[x]_ [)] _[ −]_ _[f]_ [(] _[c]_ [)] ( _x −_ _c_ ) + _f_ ( _c_ ) _, x ̸_ = _c_ (2.2.2)

_x −_ _c_



_By taking the limit as x approaches c on both sides of equation 2.2.2 and simplifying, we get:_



lim
_x→c_ _[f]_ [(] _[x]_ [) = lim] _x→c_




- _f_ ( _x_ ) _−_ _f_ ( _c_ ) 
( _x −_ _c_ ) + _f_ ( _c_ )
_x −_ _c_



_f_ ( _x_ ) _−_ _f_ ( _c_ )
= lim
_x→c_ _x −_ _c_



+ lim
_x→c_ _[f]_ [(] _[c]_ [)]

~~�~~ ~~�~~  - ~~�~~
_f_ ( _c_ )



_′_
= _f_ ( _c_ ) _×_ 0 + _f_ ( _c_ ) = _f_ ( _c_ )



_x→c_ _x −_ _c_

~~�~~ ~~��~~ 


_×_ lim
_x→c_ [(] _[x][ −]_ _[c]_ [)]

 - ~~��~~ ~~�~~
0



_f_ _[′]_ ( _c_ )



_Therefore_ lim
_x→c_ _[f]_ [(] _[x]_ [) =] _[ f]_ [(] _[c]_ [)] _[ which means that][ f][ is continuous at][ x][.]_


**Theorem 2.2.3** _**Not continuous implies not differentiable**_ _._
_If f is not continuous at x_ = _c, then f is not differentiable at x_ = _c_


**2.3** **Rules of Differentiation**


1. **The Constant function** _y_ = _c_ .



_dy_ _f_ ( _x_ + _h_ ) _−_ _f_ ( _x_ )
_dx_ [= lim] _h→_ 0 _h_



) _−_ _f_ ( _x_ ) _c −_ _c_

= lim
_h_ _h→_ 0 _h_



_c_ 0

= lim
_h_ _h→_ 0 _h_ [= 0]



∴ _[d]_

_dx_ [[] _[c]_ [] = 0]



(pg 6) 2 THE DIFFERENTIATION


Semester 1 - Calculus I(lec3) Faculty of Computer Science (CS+IT)


2. **Power Rule**
_d_
_dx_ [[] _[x][n]_ [] =] _[ nx][n][−]_ [1]


Proof



_dy_ ( _x_ + _h_ ) _[n]_ _−_ _x_ _[n]_
_dx_ [= lim] _h→_ 0 _h_




 - _x_ _[n]_ + _nx_ _[n][−]_ [1] _h_ + - _n_ 2� _n_ _[n][−]_ [2] _h_ [2] + _· · ·_ + _h_ _[n]_ [�] _−_ _x_ _[n]_



= lim
_h_ _h→_ 0



_h_



= lim _h_ - _nx_ _[n][−]_ [1] + - _n_ 2� _n_ _[n][−]_ [1] _h_ + _· · ·_ + _h_ _[n][−]_ [1][�]
_h→_ 0 _h_



= lim
_h→_ 0




- - _n_ - _nx_ _[n][−]_ [1] + _n_ _[n][−]_ [1] _h_ + _· · ·_ + _h_ _[n][−]_ [1] = _nx_ _[n][−]_ [1] _._
2



3. **The Sine function** _y_ = sin _x_




- - _h_
sin

2







_dy_ sin( _x_ + _h_ ) _−_ sin _x_

= lim

_dx_ [= lim] _h→_ 0 _h_ _h→_ 0




  2 cos _x_ + _[h]_

2


_h_





��




 - _h_
sin












 -  = lim _x_ + _[h]_
_h→_ 0 [cos] 2



 = cos _x ×_ 1 = cos _x._



2


~~�~~



2



lim
_h_
 2 _[→]_ [0]




~~�~~ _h_



2


∴ _[d]_

_dx_ [[sin] _[ x]_ [] = cos] _[ x]_



4. **The Cosine function** _y_ = cos _x_
_d_
_dx_ [[cos] _[ x]_ [] =] _[ −]_ [sin] _[ x]_


Proof, left for you.


5. **The Tangent Function** _y_ = tan _x_



_dy_ tan( _x_ + _h_ ) _−_ tan _x_

= lim

_dx_ [= lim] _h→_ 0 _h_ _h→_ 0



_dy_ tan( _x_ + _h_ ) _−_ tan _x_
_dx_ [= lim] _h→_ 0 _h_



tan _x_ + tan _h_
1 _−_ tan _x_ tan _h_ _[−]_ [tan] _[ x]_

_h_



tan _x_ + tan _h −_ tan _x_ (1 _−_ tan _x_ tan _h_ )
= lim
_h→_ 0 _h_ (1 _−_ tan _x_ tan _h_ )

tan _x_ + tan _h −_ tan _x_ + tan [2] _x_ tan _h_
= lim
_h→_ 0 _h_ (1 _−_ tan _x_ tan _h_ )



_×_ lim
_h→_ 0 [(1 + tan][2] _[ x]_ [)]

~~�~~ ~~�~~  -  sec [2] _x_




- tan _h_







_×_ lim
_h→_ 0







= 1 _×_ 1 _×_ sec [2] _x_ = sec [2] _x_




- 1
1 _−_ tan _x_ tan _h_



= lim
_h→_ 0



_h_




~~�~~ �� ~~�~~
(1)




~~�~~ ~~��~~ ~~�~~
(1)



6. **The Exponential function** _y_ = _a_ _[x]_ _, a >_ 0 ( _a ̸_ = 1).



_dy_ _a_ _[x]_ [+] _[h]_ _−_ _a_ _[x]_
_dx_ [= lim] _h→_ 0 _h_




_−_ _a_ _[x]_ _a_ _[h]_ _−_ 1

= _a_ _[x]_ lim
_h_ _h→_ 0 _h_



_h_



1

Now, let [1]

_u_ [=] _[ a][h][ −]_ [1] _[ ⇒]_ _[u]_ [ =] _a_ _[h]_ _−_ 1 [, thus] _[ u][ →∞]_ [when] _[ h][ →]_ [0 and] _[ h]_ [ = log] _[a]_




1 + [1]

_u_



_⇒_ _[dy]_




_[dy]_ 1

_dx_ [=] _[ a][x][ ×]_ [ lim] _u→∞_ ~~�~~ ~~�~~




~~�~~
_u_ log _a_




~~�~~
1 + [1]



1
= _a_ _[x]_ _×_ lim
~~��~~ _u→∞_ ~~�~~



_u_






~~�~~ ~~_u_~~




~~�~~
1 + [1]



_u_



log _a_



1
= _a_ _[x]_ _×_



1
~~��~~ ~~_u_~~ = _a_ _[x]_ _×_ log _a e_ [=] _[ a][x][ ×]_ [ ln(] _[a]_ [)]



_u_



log _a_




~~�~~
lim
_u→∞_




~~�~~
1 + [1]



∴ _[d]_

_dx_ [[] _[a][x]_ [] =] _[ a][x][ ×]_ [ ln] _[ a]_



2 THE DIFFERENTIATION (pg 7)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec3)


7. **The Logarithmic function** _y_ = log _a x_








1 + _[h]_



_x_ 1

= lim
_h_ _h→_ 0 _h_ [log] _[a]_



_x_



_dy_ log _a_ ( _x_ + _h_ ) _−_ log _a x_

= lim

_dx_ [= lim] _h→_ 0 _h_ _h→_ 0



log _a_



_x_








1 + _[h]_



Let _u_ = _[x]_




_[x]_ _[x]_

_h_ _[⇒]_ _[u][ →∞]_ [when] _[ h][ →]_ [0 and] _[ h]_ [ =] _u_



_u_ [.]




1 + [1]



_u_




= [1]




1 + [1]




- _u_



_⇒_ _[dy]_




1 + _[h]_




_[dy]_ 1

_dx_ [= lim] _h→_ 0 _h_ [log] _[a]_



_x_




- _u_
= lim
_u→∞_ _x_ [log] _[a]_



_u_



_x_ _u_ [lim] _→∞_ [log] _[a]_



_u_



= [1]

_x_ [log] _[a]_




lim
_u→∞_




1 + [1]




- _u_ - 1
= [1]

_x_ [log] _[a]_ [(] _[e]_ [) =] _x_ ln _a_



And we conclude that _[d]_




_[d]_ [1]

_dx_ [[ln] _[ x]_ [] =] _x_



_x_



**Example 2.3.11** _Find the derivative of the function y_ = _ax_ + _b from the first principles._


_Sol_



_dy_ _f_ ( _x_ + _h_ ) _−_ _f_ ( _x_ )
_dx_ [= lim] _h→_ 0 _h_



) _−_ _f_ ( _x_ ) _a_ ( _x_ + _h_ ) + _b −_ ( _ax_ + _b_ )

= lim
_h_ _h→_ 0 _h_



_b −_ ( _ax_ + _b_ ) - _ax_ [�] + _ah_ + � _b −_ �� _ax −_ - _b_

= lim
_h_ _h→_ 0 _h_



_ah_
= lim
_h→_ 0 _h_ [= lim] _h→_ 0 _[a]_ [ =] _[ a.]_



**Example 2.3.12** _Find the derivative of the function y_ = 4 _−_ 3 _x from the first principles._


**Example 2.3.13** _Find the derivative of the function y_ = _x_ [2] + 2 _x −_ 5 _from the first principles._


_Sol_



) _−_ _f_ ( _x_ ) ( _x_ + _h_ ) [2] + 2( _x_ + _h_ ) _−_ 5 _−_ ( _x_ [2] + 2 _x −_ 5)

= lim
_h_ _h→_ 0 _h_



_dy_ _f_ ( _x_ + _h_ ) _−_ _f_ ( _x_ )
_dx_ [= lim] _h→_ 0 _h_



_h_




- ( _x_ + _h_ ) [2] _−_ _x_ [2]
= lim
_h→_ 0 _h_



+ lim
_h_ _h→_ 0 [2]



= lim
_h→_ 0




- ( _x_ + _h_ )2 _−_ _x_ 2



) _x_ + [2] _[h]_

_h_ _h_



_h_



_h_ (2 _x_ + _h_ )
= lim + lim
_h→_ 0 _h_ _h→_ 0 [2 = lim] _h→_ 0 [(2] _[x]_ [ +] _[ h]_ [) + lim] _h→_ 0 [2 = (2] _[x]_ [ + 0) + 2 = 2] _[x]_ [ + 2] _[.]_



1
**Example 2.3.14** _Find the derivative of the function y_ = ~~_√_~~
~~_x_~~ _from the first principles._


_Sol_



~~_x_~~ _−_ _x_ + _h_

~~_√_~~ ~~_√_~~
_h_ ~~�~~ ~~_x_~~ _x_ + _h_



_√_ _√_

_x_ + _h_ ~~_x_~~ +

_×_ ~~_√_~~ ~~_√_~~
_x_ + _h_ ~~�~~ ~~_x_~~ +



_x_ + _h_



_y_ _[f]_ [(] _[x]_ [ +] _[ h]_ [)] _[ −]_ _[f]_ [(] _[x]_ [)]

_h_ [=] _h_



1
~~_√_~~



∆ _y_



=
_h_



~~_x_~~ + _x_ + _h_

~~_√_~~ ~~_√_~~
~~_x_~~ + _x_ + _h_



1

~~_√_~~ _√_ _√_
_x_ + _h_ _[−]_ [1] ~~_x_~~ ~~_x_~~ _−_
= ~~_√_~~ ~~_√_~~
_h_ _h_ ~~�~~ ~~_x_~~



_x −_ ( _x_ + _h_ )
= ~~_√_~~ ~~_√_~~ ~~_√_~~
_h_ ~~�~~ ~~_x_~~ _x_ + _h_ ~~��~~ ~~_x_~~ +




_−_ 1
= ~~_√_~~ ~~_√_~~ ~~_√_~~
_x_ + _h_ ~~�~~ ~~�~~ ~~_x_~~ _x_ + _h_ ~~��~~



_x_ + _h_ ~~�~~



~~_√_~~ ~~_√_~~
_x_ + _h_ ~~��~~ ~~_x_~~ +



~~_√_~~ ~~_√_~~
_x_ + _h_ ~~��~~ ~~_x_~~ +




_−_ 1

_[dy]_ ~~_√_~~ ~~_√_~~ ~~_√_~~

_dx_ [= lim] _h→_ 0 ~~�~~ ~~_x_~~ _x_ + _h_ ~~��~~




_−_ 1 _−_ 1
_x_ + _h_ ~~�~~ = ( ~~_[√]_~~ ~~_x_~~ ~~_[√]_~~ ~~_x_~~ ) ( ~~_[√]_~~ ~~_x_~~ + ~~_[√]_~~ ~~_x_~~ ) [=] _x_ (2 ~~_[√]_~~ ~~_x_~~ ) [=] 2 _[−]_ _x_ [1] 32



_⇒_ _[dy]_



~~_√_~~ ~~_√_~~
_x_ + _h_ ~~��~~ ~~_x_~~ +



3
2 _x_ 2



**2.4** **Properties of Derivatives**


1. **Constant multiple rule:** If _f_ is differentiable at _x_ and _c_ is a constant, then


_d_ _′_
( _x_ )
_dx_ [[] _[cf]_ [(] _[x]_ [)] =] _[ cf]_


(pg 8) 2 THE DIFFERENTIATION


Semester 1 - Calculus I(lec3) Faculty of Computer Science (CS+IT)


2. **Sum Rule:** If _f_ and _g_ are differentiable at _x_, then


_d_ _′_ _′_
( _x_ ) + _g_ ( _x_ )
_dx_ [[] _[f]_ [(] _[x]_ [) +] _[ g]_ [(] _[x]_ [)] =] _[ f]_


Proof


Let _F_ = _f_ + _g_, where _f_ and _g_ are differentiable at _x_, so:



_′_ _F_ ( _x_ + _h_ ) _−_ _F_ ( _x_ )
_F_ ( _x_ ) = lim
_h→_ 0 _h_



) _−_ _F_ ( _x_ ) [ _f_ ( _x_ + _h_ ) + _g_ ( _x_ + _h_ )] _−_ [ _f_ ( _x_ ) + _g_ ( _x_ )]

= lim
_h_ _h→_ 0 _h_



_h_



_f_ ( _x_ + _h_ ) + _g_ ( _x_ + _h_ ) _−_ _f_ ( _x_ ) _−_ _g_ ( _x_ )
= lim
_h→_ 0 _h_



) _−_ _f_ ( _x_ ) _g_ ( _x_ + _h_ ) _−_ _g_ ( _x_ )

+ lim
_h_ _h→_ 0 _h_



_h_ ) _−_ _f_ ( _x_ ) _−_ _g_ ( _x_ ) _f_ ( _x_ + _h_ ) _−_ _f_ ( _x_ )

= lim
_h_ _h→_ 0 _h_



_h→_ 0 _h_ _h→_ 0 _h_ _h→_ 0 _h_

_′_ _′_
= _f_ ( _x_ ) + _g_ ( _x_ ) _._



**Note:**


(a) The sum rule can be extended to three or more differentiable functions _f_ 1 _, f_ 2 _, . . ., fn_ to obtain the
generalized sum rule.


_d_ _′_ _′_ _′_
1 [(] _[x]_ [) +] _[ f]_ 2 [(] _[x]_ [) +] _[ · · ·]_ [ +] _[ f]_ _n_ [(] _[x]_ [)]
_dx_ [[] _[f]_ [1][(] _[x]_ [) +] _[ f]_ [2][(] _[x]_ [) +] _[ · · ·]_ [ +] _[ f][n]_ [(] _[x]_ [)] =] _[ f]_


(b) The difference of two functions _f −_ _g_ can be rewritten as the sum _f_ + ( _−g_ ). By combining the sum
rule with the constant multiple, the difference rule established.


_d_ _′_ _′_
( _x_ ) _−_ _g_ ( _x_ )
_dx_ [[] _[f]_ [(] _[x]_ [)] _[ −]_ _[g]_ [(] _[x]_ [)] =] _[ f]_


The proof (exercise)


3. **Product Rule:** If _f_ and _g_ are differentiable at _x_, then


_d_ _′_ _′_
( _x_ ) + _f_ ( _x_ ) _g_ ( _x_ )
_dx_ [[] _[f]_ [(] _[x]_ [)] _[g]_ [(] _[x]_ [)] =] _[ f]_ [(] _[x]_ [)] _[g]_


Proof


Let _F_ ( _x_ ) = _f_ ( _x_ ) _.g_ ( _x_ ), then



_dF_ _F_ ( _x_ + _h_ ) _−_ _F_ ( _x_ )

_dx_ [= lim] _h→_ 0 _h_



_h_



_dF_



) _−_ _F_ ( _x_ ) _f_ ( _x_ + _h_ ) _g_ ( _x_ + _h_ ) _−_ _f_ ( _x_ ) _g_ ( _x_ )

= lim
_h_ _h→_ 0 _h_



_f_ ( _x_ + _h_ ) _g_ ( _x_ + _h_ ) _−_ _f_ ( _x_ ) _g_ ( _x_ + _h_ ) + _f_ ( _x_ ) _g_ ( _x_ + _h_ ) _−_ _f_ ( _x_ ) _g_ ( _x_ )
= lim
_h→_ 0 _h_



_f_ ( _x_ + _h_ ) _g_ ( _x_ + _h_ ) _−_ _f_ ( _x_ ) _g_ ( _x_ + _h_ )
= lim
_h→_ 0 _h_



) _−_ _f_ ( _x_ ) _g_ ( _x_ + _h_ ) _f_ ( _x_ ) _g_ ( _x_ + _h_ ) _−_ _f_ ( _x_ ) _g_ ( _x_ )

+ lim
_h_ _h→_ 0 _h_



_h_















_. g_ ( _x_ + _h_ )

~~�~~ ~~�~~  - ~~�~~
_g_ ( _x_ ) _,as h→_ 0



_._ _[g]_ [(] _[x]_ [ +] _[ h]_ [)] _[ −]_ _[g]_ [(] _[x]_ [)]



_h_

~~�~~ ~~�~~ - ~~�~~



_g_ _[′]_ ( _x_ ) _, as h→_ 0



= lim
_h→_ 0



_f_ ( _x_ + _h_ ) _−_ _f_ ( _x_ )


_h_





_h_

~~�~~ ~~�~~ - ~~�~~



_f_ ( _x_ )
 ����
_f_ ( _x_ ) _, as h→_ 0



+ lim
_h→_ 0










_f_ _[′]_ ( _x_ ) _,as h→_ 0



_′_ _′_
= _f_ ( _x_ ) _g_ ( _x_ ) + _f_ ( _x_ ) _g_ ( _x_ )


4. **Quotient Rule** Consider the quotient _q_ ( _x_ ) = _[f]_ [(] _[x]_ [)]

_g_ ( _x_ ) [and note that] _[ f]_ [(] _[x]_ [) =] _[ g]_ [(] _[x]_ [)] _[.q]_ [(] _[x]_ [). By the product rule,]

we have:
_′_ _′_ _′_
_f_ ( _x_ ) = _g_ ( _x_ ) _q_ ( _x_ ) + _g_ ( _x_ ) _q_ ( _x_ )


_′_
Solving for _q_ ( _x_ ), we find that

_′_ _′_
_′_ _f_ ( _x_ ) _−_ _g_ ( _x_ ) _q_ ( _x_ )
_q_ ( _x_ ) =
_g_ ( _x_ )



Then substituting _q_ ( _x_ ) with _[f]_ [(] _[x]_ [)]

_g_ ( _x_ ) [we get:]



_′_ _′_ _f_ ( _x_ )
_f_ ( _x_ ) _−_ _g_ ( _x_ ) _._ _′_ _′_
_′_ _g_ ( _x_ ) ( _x_ ) _−_ _g_ ( _x_ ) _f_ ( _x_ )
_q_ ( _x_ ) = = _[g]_ [(] _[x]_ [)] _[f]_

_g_ ( _x_ ) ( _g_ ( _x_ )) [2]


2 THE DIFFERENTIATION (pg 9)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec3)


**Theorem 2.4.4** _**Quotient Rule**_



_If f and g are differentiable at x, g_ ( _x_ ) _̸_ = 0 _, then the derivative of_ _[f]_

_g_ _[at][ x][ exists and]_




- _′_ ( _x_ ) _−_ _g′_ ( _x_ ) _f_ ( _x_ )
= _[g]_ [(] _[x]_ [)] _[f]_
( _g_ ( _x_ )) [2]


_Proof_



_d_

_dx_




- _f_ ( _x_ )


_g_ ( _x_ )




= lim
_h→_ 0



_f_ ( _x_ + _h_ )
_g_ ( _x_ + _h_ ) _[−]_ _[f]_ _g_ ( [(] _x_ _[x]_ ) [)]



) _g_ ( _x_ ) _g_ ( _x_ ) _f_ ( _x_ + _h_ ) _−_ _f_ ( _x_ ) _g_ ( _x_ + _h_ )

= lim
_h_ _h→_ 0 _h_ ( _g_ ( _x_ ) _g_ ( _x_ + _h_ ))



_h_ ( _g_ ( _x_ ) _g_ ( _x_ + _h_ ))



_d_

_dx_




- _f_ ( _x_ )


_g_ ( _x_ )



_g_ ( _x_ ) _f_ ( _x_ + _h_ ) _−_ _f_ ( _x_ ) _g_ ( _x_ + _h_ ) _−_ _f_ ( _x_ ) _g_ ( _x_ ) + _f_ ( _x_ ) _g_ ( _x_ ) _−_ _f_ ( _x_ ) _g_ ( _x_ + _h_ )
= lim
_h→_ 0 _h_ ( _g_ ( _x_ ) _g_ ( _x_ + _h_ ))



_g_ ( _x_ )[ _f_ ( _x_ + _h_ ) _−_ _f_ ( _x_ )]
lim
_h→_ 0 _h_
=



_h_ ) _−_ _f_ ( _x_ )] _f_ ( _x_ )[ _g_ ( _x_ + _h_ ) _−_ _g_ ( _x_ )]

_−_ lim
_h_ _h→_ 0 _h_



_h→_ 0 _h_

lim
_h→_ 0 [(] _[g]_ [(] _[x]_ [)] _[g]_ [(] _[x]_ [ +] _[ h]_ [))]




[ _f_ ( _x_ + _h_ ) _−_ _f_ ( _x_ )]
_g_ ( _x_ ) lim
_h→_ 0 _h_
=



) _−_ _f_ ( _x_ )] [ _g_ ( _x_ + _h_ ) _−_ _g_ ( _x_ )]

_−_ _f_ ( _x_ ) lim
_h_ _h→_ 0 _h_



_h→_ 0 _h_

lim
_h→_ 0 [(] _[g]_ [(] _[x]_ [)] _[g]_ [(] _[x]_ [ +] _[ h]_ [))]



_′_ _′_
( _x_ ) _−_ _g_ ( _x_ ) _f_ ( _x_ )
= _[g]_ [(] _[x]_ [)] _[f]_
( _g_ ( _x_ )) [2]


**Note:** lim
_h→_ 0 _[g]_ [(] _[x]_ [ +] _[ h]_ [) =] _[ g]_ [(] _[x]_ [) because] _[ g]_ [ is given differentiable and therefore is continuous.]


5. **The Chain Rule**



**Theorem 2.4.5** _If y_ = _f_ ( _u_ ) _is a differentiable function of u, and u_ = _g_ ( _x_ ) _is a differentiable function of_
_x, then y_ = _f_ ( _g_ ( _x_ )) _is a differentiable function of x and_


_d_ _′_ _′_
( _g_ ( _x_ )) _.g_ ( _x_ )
_dx_ [[] _[f]_ [(] _[g]_ [(] _[x]_ [))] =] _[ f]_


**Example 2.4.15** _Evaluate_ _[dy]_

_dx_ _[for the following functions.]_



_1. y_ = 4 _x_ [3] + [3]

_x_ [+ 2] _[√][x][ −]_ [7]



_2. y_ = 3 cos _x −_ [1]

2 [sin] _[ x]_



_Sol_


_Sol_



_√_

_3. y_ = _x_ [7] + [1] ~~_√_~~

3 _[x][−]_ [2] _[ −]_ [1] ~~_x_~~ +



_x_ [3]



_Sol_


(pg 10) 2 THE DIFFERENTIATION


Semester 1 - Calculus I(lec3) Faculty of Computer Science (CS+IT)


_4. y_ = _x_ sin _x_


_Sol_


_5. y_ = _x_ [3] cos _x_ + _x_ [2] _−_ 5


_Sol_


_6. y_ = ( _x_ + 4)( _x_ [2] _−_ _x_ + 5)



_7. y_ = [3] _[x]_ [2][ + 1]

6 _x_ + 5



_Sol_


_Sol_



_8. y_ = [1 + cos] _[ x]_

1 _−_ sin _x_


_9. y_ = 2 _[−][x]_ + 3 _[x]_ [+1]



_Sol_


_Sol_


2 THE DIFFERENTIATION (pg 11)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec3)


_10. y_ = log4( _x_ ) _−_ 2 ln _x_


_Sol_


_11. y_ = _x_ sin(3 _x_ + 4)



_12. y_ = [sin] _[ x]_ [ + cos] _[ x]_

sin _x −_ cos _x_



_Sol_


_Sol_




     -     -     _13. y_ = log3 _x_ + _x_ [2] + 1



_Sol_


**Exercise 2.4.2** _1. From the first principles, evaluate the first derivative for the following function._


_(i) y_ = _x_ [3]


_x_
_(ii) y_ =
_x_ [2] _−_ 5


(pg 12) 2 THE DIFFERENTIATION


Semester 1 - Calculus I(lec3) Faculty of Computer Science (CS+IT)


_(iii) y_ = sin 2 _x_


_(iv) y_ = _xe_ _[−][x]_



_2. Find_ _[dy]_

_dx_ _[for the following:]_


_(a) y_ = sin( _x_ cos 2 _x_ )



_(b) y_ = _[x]_ [2][ +] _[ ax]_ [ +] _[ b]_

_x_ [2] _−_ _ax_ + _b_




~~�~~ ~~_√_~~
_(c) y_ = 1 +



2 _[x]_ _−_ 1




    - 2 _x_
_(d) y_ = sin [2]







_x_ + 1



_(e) y_ = [1 + 2 tan][2] _[ x]_

1 _−_ tan [2] _x_



2 THE DIFFERENTIATION (pg 13)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec3)


_(f) y_ = ln(sec _x_ + tan _x_ )



1
_(g) y_ =

~~�~~ 1 + ~~_[√]_~~ ~~_x_~~



_x_ [2]
_(h) y_ = ~~_√_~~

_a_ [2] _−_ _x_ [2]



_(i) y_ = _xe_ _[−][x]_ [2]


_(j) y_ = _x_ cos(sin 2 _x_ )


(pg 14) 2 THE DIFFERENTIATION


Semester 1 - Calculus I(lec4) Faculty of Computer Science (CS+IT)

## **Lecture Four** **1 Trigonometric Functions**

### **1.1 Sine Function**


**Properties of** _y_ = sin( _x_ ) **:**


                         - _∀x ∈_ R _,_ sin( _−x_ ) = _−_ sin( _x_ )


                         - _∀x ∈_ R _,_ sin( _x_ + 2 _π_ ) = sin( _x_ )


                         - _∀k ∈_ Z _,_ sin( _x_ + 2 _kπ_ ) = sin( _x_ )




- sin� _π_



_π_ - = cos( _x_ )

2 _[−]_ _[x]_


_π_ - = cos( _x_ )

2 [+] _[ x]_




- sin� _π_


### **1.2 Cosine Function**



_y_ = cos _x_ is the cosine function, and we know the domain _D_ = R and the range _R_ = [ _−_ 1 _,_ 1]
and it is an even function.


**Properties of** _y_ = cos( _x_ ) **:**


                          - _∀x ∈_ R _,_ cos( _−x_ ) = cos _x_


                          - _∀x ∈_ R _,_ cos ( _x_ + 2 _π_ ) = cos _x_


                          - _∀k ∈_ _I,_ cos ( _x_ + 2 _kπ_ ) = cos _x_




      - _π_      
- _∀x ∈_ R _,_ cos = sin _x_

2 _[−]_ _[x]_




      - _π_      
- _∀x ∈_ R _,_ cos = _−_ sin _x_

2 [+] _[ x]_


### **1.3 Tangent Function**




[sin] _[ x]_ - (2 _k −_ 1) _π_

cos _x_ [is the tangent function, we know the domain] _[ D]_ [ =][ R] _[ −]_ 2



_y_ = tan _x_ = [sin] _[ x]_



1) _π_  
_, k ∈_ _I_
2



and the range _R_ = R and it is an odd function.

**Properties of** _y_ = tan( _x_ ) **:**


                      - _∀x ∈_ _D,_ tan( _−x_ ) = _−_ tan _x_


                      - _∀x ∈_ _D,_ tan ( _x_ + 2 _π_ ) = tan _x_


                      - _∀k ∈_ _I, x ∈_ _D,_ tan ( _x_ + 2 _kπ_ ) =
tan _x_




      - _π_      
- _∀x ∈_ _D,_ tan = cot _x_

2 _[−]_ _[x]_




      - _π_      
- _∀x ∈_ _D,_ cos = _−_ cot _x_

2 [+] _[ x]_



1 TRIGONOMETRIC FUNCTIONS (pg 1)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec4)

### **1.4 Cotangent Function**



_y_ = cot _x_ = [cos] _[ x]_

sin _x_ [is the cotangent function, and we know the domain] _[ D]_ [ =][ R] _[ −{][kπ, k][ ∈]_ _[I][}]_
and the range _R_ = R and it is an odd function.


**Properties of** _y_ = cot( _x_ ) **:**


                      - _∀x ∈_ _D,_ cot( _−x_ ) = _−_ cot _x_


                      - _∀x ∈_ _D,_ cot ( _x_ + 2 _π_ ) = cot _x_


                      - _∀k ∈_ _I, x ∈_ _D,_ cot ( _x_ + 2 _kπ_ ) = cot _x_




      - _π_      
- _∀x ∈_ _D,_ cot = tan _x_

2 _[−]_ _[x]_




      - _π_      
- _∀x ∈_ _D,_ cot = _−_ tan _x_

2 [+] _[ x]_


### **1.5 Secant Function**



1       - (2 _k −_ 1) _π_       _y_ = sec _x_ = _, k ∈_ _I_
cos _x_ [is the secant function, and we know the domain] _[ D]_ [ =][ R] _[−]_ 2

and the range _R_ = R _−_ ( _−_ 1 _,_ 1) and it is an even function.

**Properties of** _y_ = sec( _x_ ) **:**


                      - _∀x ∈_ _D,_ sec( _−x_ ) = sec _x_


                      - _∀x ∈_ _D,_ sec ( _x_ + 2 _π_ ) = sec _x_


                      - _∀k ∈_ _I, x ∈_ _D,_ sec ( _x_ + 2 _kπ_ ) = sec _x_




      - _π_      
- _∀x ∈_ _D,_ sec = csc _x_

2 _[−]_ _[x]_




      - _π_      
- _∀x ∈_ _D,_ sec = _−_ csc _x_

2 [+] _[ x]_


### **1.6 Cosecant Function**



1       - (2 _k −_ 1) _π_       _y_ = csc _x_ = _, k ∈_ _I_
sin _x_ [is the cosecant function, we know the domain] _[ D]_ [ =][ R] _[ −]_ 2

and the range _R_ = R _−_ ( _−_ 1 _,_ 1) and it is an odd function.


**Properties of** _y_ = csc( _x_ ) **:**


                      - _∀x ∈_ _D,_ csc( _−x_ ) = _−_ csc _x_


                      - _∀x ∈_ _D,_ csc ( _x_ + 2 _π_ ) = csc _x_


                      - _∀k ∈_ _I, x ∈_ _D,_ sec ( _x_ + 2 _kπ_ ) = csc _x_




      - _π_

- _∀x ∈_ _D,_ csc




  = sec _x_
2 _[−]_ _[x]_


_π_ 
= sec _x_
2 [+] _[ x]_




      - _π_

- _∀x ∈_ _D,_ csc



(pg 2) 1 TRIGONOMETRIC FUNCTIONS


Semester 1 - Calculus I(lec4) Faculty of Computer Science (CS+IT)

## **2 Differentiation of Trigonometric Functions**

### **2.1 The Rules**


_d_
1.
_dx_ [[sin] _[ x]_ [] = cos] _[ x]_


_d_
2.
_dx_ [[cos] _[ x]_ [] =] _[ −]_ [sin] _[ x]_


_d_
3.
_dx_ [[tan] _[ x]_ [] = sec][2] _[ x]_


Proof



_d_ _[d]_
_dx_ [[tan] _[ x]_ [] =] _dx_




- sin _x_



_dx_



cos _x_




- = [cos] _[ x][ ×]_ [ cos] _[ x][ −]_ [sin] _[ x][ × −]_ [sin] _[ x]_

cos [2] _x_



_d_
4.
_dx_ [[cot] _[ x]_ [] =] _[ −]_ [csc][2] _[ x]_



= [cos][2] _[ x]_ [ + sin][2] _[ x]_ = 1

cos [2] _x_ cos [2] _x_ [= sec][2] _[ x]_


Proof



sin [2] _x_



_d_ _[d]_
_dx_ [[cot] _[ x]_ [] =] _dx_




- cos _x_


sin _x_




- = [sin] _[ x][ × −]_ [sin] _[ x][ −]_ [cos] _[ x][ ×]_ [ cos] _[ x]_




_[ x][ −]_ [cos] _[ x][ ×]_ [ cos] _[ x]_

= _−_ [sin][2] _[ x]_ [ + cos][2] _[ x]_
sin [2] _x_ sin [2] _x_



_d_
5.
_dx_ [[sec] _[ x]_ [] = sec] _[ x.]_ [ tan] _[ x]_



1
= _−_
sin [2] _x_ [=] _[ −]_ [csc][2] _[ x]_


Proof




- = [cos] _[ x][ ×]_ [ 0] _[ −]_ [1] _[ × −]_ [sin] _[ x]_




_[ −]_ [1] _[ × −]_ [sin] _[ x]_

= [sin] _[ x]_
cos [2] _x_ cos [2]



cos [2] _x_



_d_ _[d]_
_dx_ [[sec] _[ x]_ [] =] _dx_




- 1

cos _x_



_dx_



_d_
6.
_dx_ [[csc] _[ x]_ [] =] _[ −]_ [csc] _[ x.]_ [ cot] _[ x]_



1
= [sin] _[ x]_
cos _x_ _[.]_ cos _x_ [= sec] _[ x.]_ [ tan] _[ x]_


Proof




= [sin] _[ x][ ×]_ [ 0] _[ −]_ [1] _[ ×]_ [ cos] _[ x]_




_[ −]_ [1] _[ ×]_ [ cos] _[ x]_

= _−_ [cos] _[ x]_
sin [2] _x_ sin [2] _x_



sin [2] _x_



_d_ _[d]_
_dx_ [[csc] _[ x]_ [] =] _dx_




- 1

sin _x_



1
= _−_
sin _x_ _[.]_ [cos] sin _x_ _[ x]_ [=] _[ −]_ [csc] _[ x.]_ [ cot] _[ x]_



**In general:**



2 DIFFERENTIATION OF TRIGONOMETRIC FUNCTIONS (pg 3)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec4)

### **2.2 Examples**


|No.|The Trig. Function|Derivative|
|---|---|---|
|(1)|_d_<br>_dx_[sin_ u_(_x_)]|_u_<br>_′_(_x_) cos_ u_(_x_)|
|(2)|_d_<br>_dx_[cos_ u_(_x_)]|_−u_<br>_′_(_x_)_._ sin_ u_(_x_)|
|(3)|_d_<br>_dx_[tan_ u_(_x_)]|_u_<br>_′_(_x_) sec2_ u_(_x_)|
|(4)|_d_<br>_dx_[cot_ u_(_x_)]|_−u_<br>_′_(_x_) csc2_ u_(_x_)|
|(5)|_d_<br>_dx_[sec_ u_(_x_)]|_u_<br>_′_(_x_) sec_ u_(_x_) tan_ u_(_x_)|
|(6)|_d_<br>_dx_[csc_ u_(_x_)]|_−u_<br>_′_(_x_) csc_ u_(_x_) cot_ u_(_x_)|



**Example 2.2.1** _Find_ _[dy]_

_dx_ _[for the following functions:]_


_1. y_ = 3 sin (2 _x_ [2] + 5) _−_ cos [3] _x_



_Sol_


_dy_
_dx_ [= 3] _[ ×]_ [ 4] _[x][ ×]_ [ cos (2] _[x]_ [2][ + 5)] _[ −]_ [3] _[ ×]_ [ cos][2] _[ x]_ [(] _[−]_ [sin] _[ x]_ [) = 12] _[x]_ [ cos (2] _[x]_ [2][ + 5) + 3 sin] _[ x]_ [ cos][2] _[ x]_



_2. y_ = 4 sec (cos _x_ [2] + 1)



_Sol_


_dy_

    - _−_ 2 _x_ sin _x_ [2][�] sec (cos _x_ [2] + 1) tan (cos _x_ [2] + 1)
_dx_ [= 4]

= _−_ 8 _x_ sin _x_ [2] sec (cos _x_ [2] + 1) tan (cos _x_ [2] + 1)



_3. y_ = ~~�~~ tan ( _x_ sec _x_ )



_Sol_

_Let w_ = tan ( _x_ sec _x_ ) _⇒_ _y_ = _[√]_ ~~_w_~~ _i.e. y_ = _f_ ( _w_ ) _. And let u_ = _x_ sec _x_
_i.e. u_ = _h_ ( _x_ ) _⇒_ _w_ = tan _u i.e. w_ = _g_ ( _u_ ) _. Hence_



_dy_ _[dy]_
_dx_ [=] _dw_




_[dy]_

_dw_ _[.][dw]_ _du_




_[dw]_

_du_ _[.][du]_ _dx_



_dx_



_Now:_ _[dy]_




_[dy]_ 1 _,_ _[dw]_

_dw_ [=] 2 ~~_[√]_~~ ~~_w_~~ _du_




_[dw]_ _,_ _[du]_

_du_ [= sec][2] _[ u]_ _dx_



_dx_ [=] _[ x]_ [ sec] _[ x]_ [ tan] _[ x]_ [ + sec] _[ x][. Therefore:]_



_dy_ 1 sec [2] ( _x_ sec _x_ )
_dx_ [=] 2 ~~_[√]_~~ ~~_w_~~ _[×]_ [ sec][2] _[ u][ ×]_ [ (] _[x]_ [ sec] _[ x]_ [ tan] _[ x]_ [ + sec] _[ x]_ [) =] 2 ~~�~~ tan ( _x_ sec



_._ ( _x_ sec _x_ tan _x_ + sec _x_ )
tan ( _x_ sec _x_ )



2 ~~�~~




  - sin _x_
_4. y_ =
cot _x_ + tan _x_







(pg 4) 2 DIFFERENTIATION OF TRIGONOMETRIC FUNCTIONS


Semester 1 - Calculus I(lec4) Faculty of Computer Science (CS+IT)


_Sol_


sin _x_
_We can write_
cot _x_ + tan _x_ _[as:]_



sin _x_ sin _x_
cot _x_ + tan _x_ [=] cos _x_



cos _x_ [sin] _[ x]_

sin _x_ [+] cos _x_



= sin [2] _x_ cos _x_



cos _x_



sin _x_
=
cos [2] _x_ + sin [2] _x_


sin _x_ cos _x_



_Now y_ = csc (sin [2] _x_ cos _x_ ) _, let u_ = sin [2] _x_ cos _x ⇒_ _y_ = csc _u and_ _[dy]_




_[dy]_ _[dy]_

_dx_ [=] _du_




_[dy]_

_du_ _[.][du]_ _dx_



_dx_ _[. Therefore:]_



_dy_ _,_ _[du]_
_du_ [=] _[ −]_ [csc] _[ u]_ [ cot] _[ u]_ _dx_ [=] _[ −]_ [sin][3] _[ x]_ [ + cos] _[ x]_ [(2 sin] _[ x]_ [ cos] _[ x]_ [) = sin 2] _[x]_ [ cos] _[ x][ −]_ [sin][3] _[ x]_



∴ _[dy]_



_dx_ [=] _[ −]_ [csc] _[ u]_ [ cot] _[ u][ ×]_ [ (sin 2] _[x]_ [ cos] _[ x][ −]_ [sin][3] _[ x]_ [)]



= _−_ (sin 2 _x_ cos _x −_ sin [3] _x_ ) csc (sin [2] _x_ cos _x_ ) cot (sin [2] _x_ cos _x_ )


## **3 The Inverse Trigonometric Functions**

### **3.1 The Inverse Sine Function**



Let _x_ = sin _y_, then the inverse sine
function is _y_ = arcsin ( _x_ ) = sin _[−]_ [1] _x_, the
domain of definition is _D_ = [ _−_ 1 _,_ 1], the

     -      range _R_ = _−_ _[π]_, and it is an odd

2 _[, ][π]_ 2

function, where sin _[−]_ [1] ( _−x_ ) = _−_ sin _[−]_ [1] _x_ .




_[π]_

2 _[, ][π]_ 2



2




, and it is an odd


### **The derivative of inverse sin function**



_y_ = sin _[−]_ [1] _x ⇒_ _x_ = sin _y ⇒_ 1 = cos _y_ _[dy]_




_[dy]_

_dx_ _[⇒]_ _dx_ _[dy]_




_[dy]_ 1

_dx_ [=] cos _y_




          1 _−_ sin [2] _y_ . Since _y ∈_ _−_ _[π]_



2




~~�~~
And we know that cos _y_ = _±_




_[π]_

2 _[, ][π]_ 2




_⇒_ cos _y >_ 0, hence




~~�~~
cos _y_ = 1 _−_ sin [2] _y_



Therefore

_dy_ 1
~~_√_~~
_dx_ [=] 1 _−_ _x_ [2]


3 THE INVERSE TRIGONOMETRIC FUNCTIONS (pg 5)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec4)

### **3.2 The Inverse Cosine Function**


Let _x_ = cos _y_, then the inverse cosine
function is _y_ = arccos ( _x_ ) = cos _[−]_ [1] _x_, the
domain of definition is _D_ = [ _−_ 1 _,_ 1], the
range _R_ = [0 _, π_ ], and it is an odd
function, where cos _[−]_ [1] ( _−x_ ) = cos _[−]_ [1] _x_ .

### **The derivative of inverse cos function**



_y_ = cos _[−]_ [1] _x ⇒_ _x_ = cos _y ⇒_ 1 = _−_ sin _y_ _[dy]_




_[dy]_ _[−]_ [1]

_dx_ [=] sin




_[dy]_

_dx_ _[⇒]_ _dx_ _[dy]_



sin _y_




~~�~~
And we know that sin _y_ = _±_ 1 _−_ cos [2] _y_ . Since _y ∈_ [0 _, π_ ] _⇒_ sin _y >_ 0, hence




  sin _y_ =



1 _−_ cos [2] _y_



Therefore

_dy_ _−_ 1
~~_√_~~
_dx_ [=] 1 _−_ _x_ [2]

### **3.3 The Inverse Tangent Function**



Let _x_ = tan _y_, then the inverse tangent
function is _y_ = arctan ( _x_ ) = tan _[−]_ [1] _x_, the
domain of definition is _D_ = R, the range

  -  _R_ = _−_ _[π]_, and it is an odd function,

_[, ][π]_




_[π]_

2 _[, ][π]_ 2



2




, and it is an odd function,



where tan _[−]_ [1] ( _−x_ ) = _−_ tan _[−]_ [1] _x_ .


### **The derivative of inverse tan function**



_y_ = tan _[−]_ [1] _x ⇒_ _x_ = tan _y ⇒_ 1 = sec [2] _y_ _[dy]_




_[dy]_

_dx_ _[⇒]_ _dx_ _[dy]_




_[dy]_ 1

_dx_ [=] sec [2] _y_



We know sec [2] _y_ = 1 + tan [2] _y_ = 1 + _x_ [2]



1

∴ _[dy]_

_dx_ [=] 1 + _x_ [2]



(pg 6) 3 THE INVERSE TRIGONOMETRIC FUNCTIONS


Semester 1 - Calculus I(lec4) Faculty of Computer Science (CS+IT)

### **3.4 The Inverse Cotangent Function**


Let _x_ = cot _y_, then the inverse tangent
function is _y_ = cot _[−]_ [1] _x_, the domain of
definition is _D_ = R, the range _R_ = (0 _, π_ ),
and it is an odd function, where
cot _[−]_ [1] ( _−x_ ) = _−_ cot _[−]_ [1] _x_ .

### **The derivative of inverse cot function**



_y_ = cot _[−]_ [1] _x ⇒_ _x_ = cot _y ⇒_ 1 = _−_ csc [2] _y_ _[dy]_




_[dy]_

_dx_ _[⇒]_ _dx_ _[dy]_




_[dy]_ _−_ 1

_dx_ [=] csc [2] _y_



We know csc [2] _y_ = 1 + cot [2] _y_ = 1 + _x_ [2]




_−_ 1

∴ _[dy]_

_dx_ [=] 1 + _x_ [2]


### **3.5 The Inverse Secant Function**



Let _x_ = sec _y_, then the inverse cosine
function is _y_ = sec _[−]_ [1] _x_, the domain of
definition is _D_ = R _−_ ( _−_ 1 _,_ 1), the range

  -   -   - _π_   _R_ = 0 _,_ _[π]_ _∪_, and it is an even

_[, π]_



2




- - _π_
_∪_




  , and it is an even
2 _[, π]_



function, where sec _[−]_ [1] ( _−x_ ) = sec _[−]_ [1] _x_ .


### **The derivative of inverse sec function**



_y_ = sec _[−]_ [1] _x ⇒_ _x_ = sec _y ⇒_ 1 = sec _y_ tan _y_ _[dy]_




_[dy]_

_dx_ _[⇒]_ _dx_ _[dy]_




_[dy]_ 1

_dx_ [=] sec _y_ tan _y_




           sec [2] _y −_ 1, either _y ∈_ 0 _,_ _[π]_




~~�~~
And we know tan _y_ = _±_



2




this implies that tan _y >_ 0 and we




         - _π_
sec [2] _y −_ 1 _>_ 0 or _y ∈_



sec [2] _y −_ 1 and thus sec _y_ tan _y_ = _|_ sec _y|_ ~~�~~




  ,
2 _[, π]_



take tan _y_ = ~~�~~



which is implies that tan _y_ & sec _y <_ 0 _⇒_ tan _y_ = _−_ ~~�~~ sec [2] _y −_ 1 and thus sec _y_ tan _y_ =

_|_ sec _y|_ ~~�~~ sec [2] _y −_ 1 _>_ 0. Now



which is implies that tan _y_ & sec _y <_ 0 _⇒_ tan _y_ = _−_ ~~�~~



sec [2] _y −_ 1 _>_ 0. Now



_dy_ 1
_dx_ [=] _|_ sec _y|_ ~~�~~



1

_⇒_ _[dy]_
sec [2] _y −_ 1 _dx_



1

_[dy]_ ~~_√_~~

_dx_ [=] _|x|_ _x_



_x_ [2] _−_ 1



_|_ sec _y|_ ~~�~~



3 THE INVERSE TRIGONOMETRIC FUNCTIONS (pg 7)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec4)

### **3.6 The Inverse Cosecant Function**



Let _x_ = csc _y_, then the inverse cosine
function is _y_ = csc _[−]_ [1] _x_, the domain of
definition is _D_ = R _−_ ( _−_ 1 _,_ 1), the range

  -   -   -   -   -   _R_ = _−_ _[π]_ _[,]_ [ 0] _∪_ 0 _,_ _[π]_ = _−_ _[π]_ _[, ][π]_ _−{_ 0




_[π]_ - _∪_ �0 _,_ _[π]_

2 _[,]_ [ 0] 2



2




  -   -   -   -   -   _R_ = _−_ _∪_ 0 _,_ = _−_ _−{_ 0 _}_,

2 _[,]_ [ 0] 2 2 _[, ]_ 2

and it is an odd function, where
csc _[−]_ [1] ( _−x_ ) = _−_ csc _[−]_ [1] _x_ .



2




- = _−_ _[π]_




_[π]_

2 _[, ][π]_ 2


### **The derivative of inverse csc function**



_y_ = csc _[−]_ [1] _x ⇒_ _x_ = csc _y ⇒_ 1 = _−_ csc _y_ cot _y_ _[dy]_




_[dy]_

_dx_ _[⇒]_ _dx_ _[dy]_




_[dy]_ _−_ 1

_dx_ [=] csc _y_ cot _y_




          csc [2] _y −_ 1, either _y ∈_ _−_ _[π]_




~~�~~
And we know cot _y_ = _±_




  this implies that csc _y >_ 0 and we
2 _[,]_ [ 0]



sec [2] _y −_ 1 and thus csc _y_ cot _y_ = _|_ csc _y|_ ~~�~~



take cot _y_ = _−_ ~~�~~




        csc [2] _y −_ 1 _>_ 0 or _y ∈_ 0 _,_ _[π]_




, which



is implies that csc _y >_ 0 _⇒_ cot _y_ = ~~�~~ csc [2] _y −_ 1 and thus csc _y_ cot _y_ = _|_ csc _y|_ ~~�~~ csc [2] _y −_ 1 _>_ 0.

Now
_dy_ _−_ 1 _−_ 1

_⇒_ _[dy]_ ~~_√_~~

_dx_ [=] _|_ csc _y|_ ~~�~~ csc [2] _y −_ 1 _dx_ [=] _|x|_ _x_ [2] _−_ 1



csc [2] _y −_ 1 and thus csc _y_ cot _y_ = _|_ csc _y|_ ~~�~~



2



is implies that csc _y >_ 0 _⇒_ cot _y_ = ~~�~~



1

_⇒_ _[dy]_
csc [2] _y −_ 1 _dx_



_|_ csc _y|_ ~~�~~




_−_ 1

_[dy]_ ~~_√_~~

_dx_ [=] _|x|_ _x_ [2]



_x_ [2] _−_ 1



**Example 3.6.2** _Find_ _[dy]_

_dx_ _[for the following functions:]_



_1. y_ = _[x]_

2 [sin] _[−]_ [1][ 2] _[x]_



_Sol_



_dy_ _[x]_
_dx_ [=] 2



2

_[x]_ ~~_√_~~

2 _[.]_ 1 _−_



2 [+ ][1]

1 _−_ 4 _x_ [2]



_x_

[1] ~~_√_~~

2 [sin] _[−]_ [1][ 2] _[x]_ [ =] 1 _−_



_x_ [1]

[+]
1 _−_ 4 _x_ [2]



2 [sin] _[−]_ [1][ 2] _[x]_



_2. y_ = cos _[−]_ [1] ( _x_ cos _x_ )



_Sol_



_′_

_d_ _−u_ ( _x_ )

�cos _[−]_ [1] ( _u_ ( _x_ ))� =
_dx_ ~~�~~ 1 _−_ ( _u_ (



_′_ _d_
_Let u_ = _x_ cos _x ⇒_ _u_ ( _x_ ) = cos _x −_ _x_ sin _x and we know_



1 _−_ ( _u_ ( _x_ )) [2]




_[dy]_ _[−]_ [(cos] _[ x][ −]_ _[x]_ [ sin] _[ x]_ [)]

_dx_ [=] ~~�~~ 1 _−_ ( _x_ cos ( _x_ )) [2]



1 _−_ _x_ [2] cos [2] _x_



∴ _[dy]_




[(cos] _[ x][ −]_ _[x]_ [ sin] _[ x]_ [)]

~~_√_~~ _[x]_ [ sin] _[ x][ −]_ [cos] _[ x]_

[=]
1 _−_ ( _x_ cos ( _x_ )) [2] 1 _−_ _x_ [2] cos [2] _x_



_3. y_ = [tan] _[−]_ [1] _[ x]_

_x_ [2] + 1



_Sol_


(pg 8) 3 THE INVERSE TRIGONOMETRIC FUNCTIONS


Semester 1 - Calculus I(lec4) Faculty of Computer Science (CS+IT)



 = [1] _[ −]_ [2] _[x]_ [ tan] _[−]_ [1] _[ x]_
 [2] [2]



( _x_ [2] + 1) [2]











_dy_
_dx_ [=]



 1

( _x_ [2] + 1) _×_
_x_ [2] + 1 _[−]_ [tan] _[−]_ [1] _[ x][ ×]_ [ (2] _[x]_ [)]

 [2] [2]



( _x_ [2] + 1) [2]




    - tan _x_ + 1
_4. y_ = tan _[−]_ [1]

tan _x −_ 1







_Sol_


_′_
_u_ ( _x_ )

_We know that_ _[d]_ �tan _[−]_ [1] ( _u_ ( _x_ ))� =

_dx_ 1 + ( _u_ ( _x_ )) [2]



∴ _[dy]_




_[dy]_ 1

_dx_ [=] ~~�~~ tan




~~�~~ tan _x_ + 1
1 +



_×_ [(tan] _[ x][ −]_ [1)] _[ ×]_ [ sec][2] _[ x][ −]_ [(tan] _[ x]_ [ + 1)] _[ ×]_ [ sec][2] _[ x]_

~~�~~ 2 (tan _x −_ 1) [2]



tan _x −_ 1




 - (tan _x −_ 1) [2]
=

(tan _x_ + 1) [2] + (tan _x −_ 1) [2]




_×_ [sec][2] _[ x]_ [[tan] _[ x][ −]_ [1] _[ −]_ [tan] _[ x][ −]_ [1]]

(tan _x −_ 1) [2]




_−_ 2 sec [2] _x_
= _[−]_ [2 sec][2] _[ x]_
2(tan [2] _x_ + 1) [=] 2 sec [2] _x_ [=] _[ −]_ [1]



_**Another Solution:**_ _We can write_ [tan] _[ x]_ [ + 1]

tan _x −_ 1 _[as:]_




[sin] _[ x]_ [ + cos] _[ x]_

sin _x −_ cos _x_ [= ][sin][2] _[ x]_ [ + 2] sin _[x]_ [2][ sin] _x −_ _[ x]_ [ cos] cos [2] _[ x]_ _x_ [ + cos][2] _[ x]_



sin [2] _x −_ cos [2] _x_



tan _x_ + 1
tan _x −_ 1 [=]



sin _x_
cos _x_ [+ 1]



cos _x_

= [sin] _[ x]_ [ + cos] _[ x]_
sin _x_ sin _x −_ cos _x_
cos _x_ _[−]_ [1]



�1 + sin 2 _x_
= _−_

cos 2 _x_



�1 + sin 2 _x_
= _−_




= _−_ [sec 2 _x_ + tan 2 _x_ ]




    - tan _x_ + 1
_Now,_ tan _[−]_ [1]




= _−_ tan _[−]_ [1] [sec 2 _x_ + tan 2 _x_ ]



tan _x −_ 1




   - 2 sec 2 _x_ tan 2 _x_ + 2 sec2 _x_

_[dy]_

_dx_ [=] _[ −]_ 1 + (sec 2 _x_ + tan 2 _x_ ) [2]



∴ _[dy]_



1 + (sec 2 _x_ + tan 2 _x_ ) [2]








  - 2 sec 2 _x_ tan 2 _x_ + 2 sec2 _x_
= _−_

2 sec 2 _x_ tan 2 _x_ + 2 sec [2] _x_




- - 2 sec 2 _x_ tan 2 _x_ + 2 sec [2] _x_
= _−_
1 + sec [2] _x_ + 2 sec 2 _x_ tan 2 _x_ + tan [2] _x_


= _−_ 1 _._



_**Another Solution:**_




   - tan _x_ + 1
_y_ = tan _[−]_ [1]

tan _x −_ 1




- - tan _x_ + 1
= _−_ tan _[−]_ [1]

1 _−_ tan _x_




= _−_ tan _[−]_ [1]





tan _x_ + tan _[π]_

4









4
1 _−_ tan _x ×_ tan ~~_[π]_~~










4




      = _−_ tan _[−]_ [1][ �] tan _x_ + _[π]_

4



�� = _−_ _x_ + _[π]_

4




_⇒_ _y_ = _−x −_ _[π]_




_[π]_

4 _[⇒]_ _dx_ _[dy]_



_dx_ [=] _[ −]_ [1]



**Exercise 3.6.1** _Find_ _[dy]_

_dx_ _[for the following functions.]_


_1._

_y_ = 2 sin _[−]_ [1] ( _x −_ 1)


3 THE INVERSE TRIGONOMETRIC FUNCTIONS (pg 9)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec4)


_Sol_



_2._


_3._


_4._


_5._


_6._



_√_
_y_ = _x_ cos _[−]_ [1] _x −_ 1 _−_ _x_ [2]



_y_ = tan _[−]_ [1][ �] _[x]_




+ 2 sin _[−]_ [1][ �] _[a]_







_a_



_x_



_Sol_


_y_ = [cos] _[−]_ [1] _[ x]_ [2]

_x_ + 1



_Sol_


_y_ = _e_ _[x]_ [2] sin _[−]_ [1] _x_



_Sol_


_y_ = sin _[−]_ [1] 2 _x_ + cos _[−]_ [1] 2 _x_


_Sol_



(pg 10) 3 THE INVERSE TRIGONOMETRIC FUNCTIONS


Semester 1 - Calculus I(lec4) Faculty of Computer Science (CS+IT)


_Sol_



_7._


_8._


_9._


_10._




   - _x_
_y_ = csc
_x_ + 1



4 _−_ _x_ [2] + 4 sin _[−]_ [1][ �] _[x]_

2



_y_ = [1]

2




- _√_
_x_



��



_Sol_


_y_ = cos _x._ sec _[−]_ [1] _x_


_Sol_


1
_y_ = _e_ [sin] _[−]_ [1] _[ x]_ + ~~_√_~~

1 + _x_ [2]


_Sol_




- 
_−_ sec _[−]_ [1] _x_ + [1]

_x_







_Sol_


3 THE INVERSE TRIGONOMETRIC FUNCTIONS (pg 11)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec4)



_11._


_12._


_13._


_14._



_y_ = [cot] _[−]_ [1] _[ x]_

1 + _x_ [2]



_Sol_


_y_ = ln ( _x −_ tan _x_ )


_Sol_



�1 _−_ _x_
_y_ = csc _[−]_ [1]

_x_ + 1


_Sol_











_x_ + 1
_x −_ 1 [+ tan] _[−]_ [1][ 2] _[x]_



_y_ = ln



_Sol_


(pg 12) 3 THE INVERSE TRIGONOMETRIC FUNCTIONS


Semester 1 - Calculus I(lec5) Faculty of Computer Science (CS+IT)

## **Lecture Five** **1 Exponential and Logarithmic Functions**

### **1.1 Exponential Function**


**Definition 1.1.1** _Let a >_ 0 _, a ̸_ = 1 _, then the exponential function of the base a ia y_ = _a_ _[x]_ _._


**1.1.1** **Some Properties of the exponential function**


For _y_ = _a_ _[x]_,


1. If _a >_ 1, then:


(a) _a_ _[x]_ _>_ 0 _, ∀x ∈_ R


(b) _y_ = _a_ _[x]_ is an increasing function.


(c) lim
_x→−∞_ _[a][x][ →]_ [0]


(d) lim
_x→_ + _∞_ _[a][x][ →∞]_



(e) _f_ (0) = _a_ [0] = 1 _, ∀a >_ 1, the graph of _a_ _[x]_ passes through the point (0,1) on _y−_ axis.


2. If 0 _< a <_ 1, then:



(a) _a_ _[x]_ _>_ 0 _, ∀x ∈_ R


(b) _y_ = _a_ _[x]_ will be decreasing function.



(c) lim
_x→−∞_ _[a][x][ →∞]_


(d) lim
_x→_ + _∞_ _[a][x][ →]_ [0]


(e) _f_ (0) = _a_ [0] = 1 _, ∀a <_ 1, the graph of _a_ _[x]_ passes through the point (0,1) on _y−_ axis.


**Theorem 1.1.1** _Prove that_



_e_ _[x]_ = 1 + _x_ + _[x]_ [2]




_[x]_ [2] _[x]_ [3]

2! [+] 3!




_[x]_ [3] _[x][k]_

3! [+] _[ · · ·]_ [ +] _k_ !



_k_ ! [+] _[ · · ·]_ [ =]



_∞_



_k_ =0



_x_ _[k]_


_k_ !



_Proof_




1 + _[x]_



_We know e_ _[x]_ = lim
_n→∞_



_n_




- _n_
_, now:_




- _x_ 3




- _xk_




[+] _[ . . .]_
_n_ _[k]_



_x_ - _n_

_n_ [+] 2




- _x_ 2



_x_ 2 - _n_

[+]
_n_ [2] 3



_x_ 3 - _n_

[+] _[ · · ·]_ [ +]
_n_ [3] _k_




1 + _[x]_

_n_




- _n_ - _n_
= 1 +
1




- _x_




[1)(] _[n][ −]_ [2)] _x_ [3]

3! _n_ [3]




_[n][ −]_ [2)] _[ . . .]_ _x_ _[k]_

_k_ ! _n_ _[k]_




_[x]_ _[n]_ [(] _[n][ −]_ [1)]

_n_ [+] 2!



_x_ [2] _[n]_ [(] _[n][ −]_ [1)(] _[n][ −]_ [2)]

[+]
_n_ [2] 3!



_x_ [3] _[n]_ [(] _[n][ −]_ [1)(] _[n][ −]_ [2)] _[ . . .]_

[+] _[ · · ·]_ [ +]
_n_ [3] _k_ !




[+] _[ . . .]_
_n_ _[k]_



= 1 + _n._ _[x]_




_[ −]_ [1)] _x_ [2]

2! _n_ [2]




_x_ [2] + [1]



3!




1 _−_ [1]




_x_ [3] + _· · ·_ +



=1 + _x_ + [1]

2!




1 _−_ [1]

_n_



_n_



��
1 _−_ [2]

_n_




_x_ _[k]_



1

_k_ !




1 _−_ [1]



_n_



��
1 _−_ [2]



_n_




- _. . ._ 1 _−_ _[k][ −]_ [1]

_n_



1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS (pg 1)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec5)



��
1 _−_ [2]



_n_




- _. . ._ 1 _−_ _[k][ −]_ [1]




    _Therefore_ 1 + _[x]_




- _n_
=



_∞_

- _x_ _[k]_



_n_



_k_ =0




1 _−_ [1]

_n_



_n_




_and this implies that:_



_k_ !




1 + _[x]_



_∞_




_k_ !



lim
_n→∞_



_n_




- _n_
=




- _x_ _[k]_

lim
_n→∞_ _k_ !
_k_ =0




1 _−_ [1]



_n_



��
1 _−_ [2]



_n_




- _. . ._ 1 _−_ _[k][ −]_ [1]



_n_




=



3! [+] _[ . . .]_




_[x]_ [2] _[x]_ [3]

2! [+] 3!




1 + _[x]_



_∞_



_k_ =0



_x_ _[k]_ _[x]_ [2]

_k_ ! [= 1 +] _[ x]_ [ +] 2!



_x_ _[k]_



_⇒_ _e_ _[x]_ = lim
_n→∞_



_n_




- _n_
=



**Example 1.1.1** _Evaluate the following sums using the definition of exponential function e_ _[x]_ _:_



_1._


_2._


_3._



_∞_



_k_ =1


_∞_



_k_ =2



_∞_



_k_ =2



2 _[k]_


_k_ !



( _−_ 1) _[k]_

2 _[k][−]_ [1] _k_ !



_Sol_




_−_ 1 = [2][0]

0! [+]



_∞_

 

_k_ =1


( _−_ 1) _[k]_


_k_ !







2 _[k]_

_k_ ! [=]





1 +



_∞_

- 2 _[k]_



_∞_



_k_ =1



2 _[k]_

_k_ ! _[−]_ [1 =]



_∞_



_k_ =0



2 _[k]_

_k_ ! _[−]_ [1 =] _[ e]_ [2] _[ −]_ [1] _[.]_



_k_ !



_Sol_



_∞_



_k_ =2



=
_k_ !



( _−_ 1) _[k]_

= 1 _−_ 1 +
_k_ !



_k_ =1


_∞_



_k_ =2



1) _[k]_ = [(] _[−]_ [1)][0]

_k_ ! 0!



( _−_ 1) _[k]_




[1)][0] + [(] _[−]_ [1)][1]

0! 1!



+
1!



_∞_




_k_ =2



( _−_ 1) _[k]_



_∞_



_k_ =0



( _−_ 1) _[k]_

= _e_ _[−]_ [1] _._
_k_ !



_Sol_


 - _−_ 1




- _k_








- _−_ 1




- _k_







4 _[k]_ _k_ ! [= 2] _[ ×]_



4

_−_ 1 + [1]
_k_ ! 4



_∞_



_k_ =2



( _−_ 1) _[k]_

2 _[k][−]_ [1] _k_ ! [=]



_∞_






2 _×_ [(] _[−]_ [1)] _[k]_

4 _[k]_ _k_ !

_k_ =2







_∞_




_k_ =2







4



_∞_



_k_ =2



4

= 2 _×_
_k_ !



4



4











2 _[.]_



= 2





_−_ [1]
 _e_ 4



4 _−_ [3]



 = ~~_[√]_~~ 4 [2]




[2]

~~_[√]_~~ 4
~~_e_~~ _[−]_ 2 [3]



**Example 1.1.2** _Find the following limits using e_ _[x]_ _definition._



1 _−_ _e_ [2] _[x]_ + 2 _x_
_1._ lim
_x→_ 0 _x_ [2]



_Sol_


(pg 2) 1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS


Semester 1 - Calculus I(lec5) Faculty of Computer Science (CS+IT)




_[x]_ [2] _[x]_ [3]

2! [+] 3!



_We know that e_ _[x]_ = 1 + _x_ + _[x]_ [2]



3! [+] _[ . . .]_



_This implies that e_ [2] _[x]_ = 1 + 2 _x_ + [4] _[x]_ [2]




_[x]_

3! [+] _[ · · ·]_ [ = 1 + 2] _[x]_ [ + 2] _[x]_ [2][ + ][4] 3




_[x]_ [2] [8] _[x]_ [3]

2! [+] 3!



3 _[x]_ [3][ +] _[ . . .][ . Now:]_




      1 + 2 _x −_ 1 + 2 _x_ + 2 _x_ [2] + [4]

[2] _[x]_ + 2 _x_ 3

=
_x_ [2] _x_ [2]



1 _−_ _e_ [2] _[x]_ + 2 _x_



= _−_
_x_ [2]




[4] 
3 _[x]_ [3][ +] _[ . . .]_




- 2 _x_ [2] + [4]

3 _[x]_ [3][ +] _[ . . .]_

_x_ [2]




  -  = _−_ 2 + [4]

3 _[x]_ [ +] _[ . . .]_



1 _−_ _e_ [2] _[x]_ + 2 _x_
∴ lim = _−_ lim
_x→_ 0 _x_ [2] _x→_ 0



�2 + [4] - = _−_ 2 _._

3 _[x]_ [ +] _[ . . .]_


_Sol_



_e_ _[ax]_ _−_ 1
_2._ lim _, b ̸_ = 0
_x→_ 0 sin _bx_



_We can write the numerator as follows:_




[3] _[x]_ [3] 
+ _. . ._ _−_ 1 = _ax_ + _[a]_ [2] _[x]_ [2]
3! 2!




[2] _[x]_ [2]

+ _[a]_ [3] _[x]_ [3]
2! 3!



+ _. . ._
3!




[2] _[x]_ [2]

+ _[a]_ [3] _[x]_ [3]
2! 3!



_e_ _[ax]_ _−_ 1 =



_∞_




( _ax_ ) _[k]_



_k_ =0



) _[k]_  
_−_ 1 = 1 + _ax_ + _[a]_ [2] _[x]_ [2]
_k_ ! 2!



+ _. . ._
3!



+ _. . ._
3!



_ax_ + _[a]_ [2] _[x]_ [2]



_e_ _[ax]_ _−_ 1
∴ lim
_x→_ 0 sin _bx_ [= lim] _x→_ 0


lim
_x→_ 0
=



_ax_ + _[a]_ [2] _[x]_ [2]



_x_

sin _bx_
lim
_x→_ 0 _x_




[2] _[x]_ [2]

+ _[a]_ [3] _[x]_ [3]
2! 3!




[2] _[x]_ [2]

+ _[a]_ [3] _[x]_ [3]
2! 3!



= lim
sin _bx_ _x→_ 0



_x_
sin _bx_


_x_



_ax_ + _[a]_ [2] _[x]_ [2]




[2] _[x]_ [2]

+ _[a]_ [3] _[x]_ [3]
2! 3!



+ _. . ._
3!



= _[a]_

_b_



_a_ _[x]_ _−_ _b_ _[x]_
_3._ lim
_x→_ 0 _x_



_Sol_


_For you_


**1.1.2** **Derivative of the Exponential Function**


1.



_d_

  - _a_ _[u]_ [(] _[x]_ [)][�] = _a_ _[u]_ [(] _[x]_ [)] _×_ ln _a ×_ _[du]_
_dx_ _dx_



2.



_d_ - _e_ _[u]_ [(] _[x]_ [)][�] = _e_ _[u]_ [(] _[x]_ [)] _×_ ln _e ×_ _[du]_ _′_ ( _x_ ) _eu_ ( _x_ )
_dx_ _dx_ [=] _[ u]_



And when _u_ ( _x_ ) = _x ⇒_


1.
_d_
_dx_ [[] _[a][x]_ [] =] _[ a][x]_ [ ln] _[ a]_


2.
_d_
_dx_ [[] _[e][x]_ [] =] _[ e][x]_


1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS (pg 3)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec5)

### **1.2 Logarithmic Functions**


**Definition 1.2.2** _Let a >_ 0 _, a ̸_ = 1 _. The_ _**logarithmic function**_ _of the base a is y_ = log _a x,_
_and it is the inverse of y_ = _a_ _[x]_ _. The domain of definition of it D_ = R [+] = (0 _, ∞_ ) _and R_ = R _._


**Note** that if the base is _e_, it is called the natural logarithm, and we denoted by ln _x_ (log _e x_ =
ln _x_ ) and thus ln _x_ is the inverse of _e_ _[x]_ .


**1.2.1** **Properties:**













|No.|log|ln|
|---|---|---|
|(1)|log_a_ 1 = 0|ln 1 = 0|
|(2)|log_a x_ + log_a y_ = log_a xy_|ln_ x_ + ln_ y_ = ln_ xy_|
|(3)|log_a xn_ =_ n_ log_a x_|ln_ xn_ =_ n_ ln_ x_|
|(4)|log_a_<br>1<br>_x_ =_ −_log_a x_|ln 1<br>_x_ =_ −_ln_ x_|
|(5)|<br>log_a x −_log_a y_ = log_a_<br>_x_<br>_y_|<br>ln_ x −_ln_ y_ = ln _x_<br>_y_|
|(6)|log_a b_ =<br>1<br>log_b a_|ln_ b_ =<br>1<br>log_b e_|
|(7)|AF<br> <br>log_an x_ = 1<br>_n_ log_a x_|<br>log_en x_ = 1<br>_n_ ln_ x_|
|(8)|DR<br> <br>log_an xn_ = log_a x_|<br>log_en xn_ = ln_ x_|


**1.2.2** **Derivative of Logarithmic Function**


1.



_d_ 1 _[du]_
_dx_ [[log] _[a][ u]_ [(] _[x]_ [)] =] _u_ ( _x_ ) ln _a_ _[×]_ _dx_



2.


And if _u_ ( _x_ ) = _x ⇒_


1.


2.



_d_ 1 _[du]_
_dx_ [[ln] _[ u]_ [(] _[x]_ [)] =] _u_ ( _x_ ) _[×]_ _dx_


_d_ 1
_dx_ [[log] _[a][ x]_ [] =] _x_ ln _a_



_d_ [1]
_dx_ [[ln] _[ x]_ [] =] _x_



**Derivative of** [ _f_ ( _x_ )] _[g]_ [(] _[x]_ [)] :
Let _y_ = ( _f_ ( _x_ )) _[g]_ [(] _[x]_ [)], then the derivative evaluated as follows:


_y_ = [ _f_ ( _x_ )] _[g]_ [(] _[x]_ [)] _⇒_ ln _y_ = _g_ ( _x_ ) ln _f_ ( _x_ )


(pg 4) 1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS


Semester 1 - Calculus I(lec5) Faculty of Computer Science (CS+IT)


Now, by differentiating both sides w.r.t _x_, we get:



_′_ _′_
_y_ _[f]_ ( _x_ ) _′_ ( _x_ ) ln _f_ ( _x_ )

_y_ [=] _[ g]_ [(] _[x]_ [)] _[ ×]_ _f_ ( _x_ ) [+] _[ g]_



Therefore the derivative will be:


~~�~~ _′_ ~~�~~
_′_ ( _x_ ) _′_
_y_ = _g_ ( _x_ ) _×_ _[f]_ ( _x_ ) ln _f_ ( _x_ ) _× y_
_f_ ( _x_ ) [+] _[ g]_


**Example 1.2.3** _Find the first derivative of the following function:_


_1. y_ = _e_ [sin][2][(4] _[x]_ [)]


_Sol_


_dy_
_dx_ [= 2(sin 4] _[x]_ [)] _[ ×]_ [ (4 cos 4] _[x]_ [)] _[ ×][ e]_ [sin][2][(4] _[x]_ [)][ = 8 sin 4] _[x]_ [ cos 4] _[x e]_ [sin][2][(4] _[x]_ [)] _[.]_



2 _x_ [2] +8
_2. y_ = _e_ 4 _x_ +1



_Sol_


_dy_       - (4 _x_ + 1)(4 _x_ ) _−_ (2 _x_ 2 + 8)(4)
_dx_ [=] (4 _x_ + 1) [2]


_3. y_ = _x_ [3] _e_ [2] _[x]_ [2] _[−]_ [1]


_Sol_



_x_ [2] +8

4 _x_ +1
= [4] _[x][ −]_ [8] _[x]_ [2] _[ −]_ [12]



4 _x_ +1 _._




- 2 _x_ [2] +8
_e_ 4 _x_ +1




_[ −]_ [8] _[x]_ [12] 2 _x_ [2] +8

_e_ 4 _x_ +1
(4 _x_ + 1) [2]



_dy_
4 _x × e_ [2] _[x]_ [2] _[−]_ [1][�] + _e_ [2] _[x]_ [2] _[−]_ [1] _×_ (3 _x_ [2] ) = 4 _x_ [4] _e_ [2] _[x]_ [2] _[−]_ [1] + 3 _x_ [2] _e_ [2] _[x]_ [2] _[−]_ [1]
_dx_ [=] _[ x]_ [3][ �]


_Sol_



_4. y_ = _e_



tan _x_
sin(cos _x_ )



_dy_ �sin(cos _x_ ) sec2 _x_ + tan _x_ (sin _x_ cos(cos _x_ ))
_dx_ [=] sin [2] (cos _x_ )




_e_



tan _x_
sin(cos _x_ )



**Example 1.2.4** _Find_ _[dy]_

_dx_ _[for the following functions:]_



1
_(a) y_ = 2 _[x]_ + ~~_√_~~

3 _[x]_



_Sol_




_−_ _[x]_
_y_ = 2 _[x]_ + 3 2




_−_ _[x]_

_[dy]_ 2

_dx_ [= 2] _[x]_ [ ln 2 + 3]



2



2 _⇒_ _[dy]_




   2 _×_ ln 3 _×_ _−_ [1]




= 2 _[x]_ ln 2 _−_ [ln 3] ~~_√_~~



~~_√_~~
2



3 _[x]_



_(b) y_ = [4] _[x][ −]_ [1]

4 _[x]_ + 1



_Sol_


1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS (pg 5)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec5)



_dy_
_dx_ [= ][(4] _[x]_ [ + 1)(4] _[x]_ [ ln 4)] (4 _[x][ −]_ + 1) [(4] _[x]_ [2] _[ −]_ [1)(4] _[x]_ [ ln 4)]



= [4] _[x]_ [ ln 4(4] _[x]_ [ + 1] _[ −]_ [4] _[x]_ [ + 1)]



(4 _[x]_ + 1) [2]




_[x]_ [ + 1] _[ −]_ [4] _[x]_ [ + 1)]

= [2][2] _[x]_ [+1][ ln 4]
(4 _[x]_ + 1) [2] (4 _[x]_ + 1) [2]



_(c) y_ = _x_ [sec] _[−]_ [1] _[ x]_



_Sol_


_By tanking_ ln _for both sides ⇒_ ln _y_ = sec _[−]_ [1] _x_ ln _x, now:_



1 _dy_ _[sec][−]_ [1] _[x]_
_y_ _dx_ [=] _x_



_x_ [2] _−_ 1




_[x]_ ln _x_

+ ~~_√_~~
_x_ _|x|_ _x_ [2]



_Therefore, the required derivative is:_



_dy_ - _sec−_ 1 _x_
_dx_ [=] _x_



_x_ [2] _−_ 1



_x_ ln _x_

+ ~~_√_~~
_x_ _|x|_ _x_ [2]




_x_ [sec] _[−]_ [1] _[ x]_



_(d) y_ = [(] _[x]_ [ + 1)] ~~_[√]_~~ [3][(] _[x]_ [2][ + 4)][8]




~~_[√]_~~ 4



_x_ [2] + 2



_Sol_



_Firstly we take the_ ln _for both sides:_



�( _x_ + 1)3( _x_ 2 + 4)8
ln _y_ = ln ~~_[√]_~~








~~_[√]_~~ 4



_x_ [2] + 2



= 3 ln( _x_ + 1) + 8 ln( _x_ [2] + 4) _−_ [1]

4 [ln(] _[x]_ [2][ + 2)]



_Then we differentiate both sides, we get:_



1 _dy_ 3 2 _x_ 2 _x_
_y_ _dx_ [=] _x_ + 1 [+ 8] _[ ×]_ _x_ [2] + 4 _[−]_ 4 [1] _x_ [2] + 2



_Finally, we multiply both sides by y to obtain the derivative:_



_dy_

~~_[√]_~~ 4

_dx_ [= ][(] _[x]_ [ + 1)] _x_ [3][2][(] _[x]_ + 2 [2][ + 4)][8]




- 3 16 _x_ _x_
_x_ + 1 [+] _x_ [2] + 4 _[−]_ 2( _x_ [2] + 2)








~~_[√]_~~ 4



_x_ [2] + 2



_(e) x_ [sin] _[ y]_ = [sin( _x_ + _y_ )] _[y]_



_Sol_


_By taking the_ ln _for both sides, the given function can be written as:_


sin _y_ ln _x_ = _y_ ln(sin( _x_ + _y_ ))


_Now, we differentiate both sides:_



sin _y_



_y_ _′_ cos( _x_ + _y_ )

+ _y_ cos( _y_ ) ln _x_ = _y_
_x_ sin( _x_ + _y_ )



sin( _x_ + _y_ )




- _′_ [�]
1 + _y_



_Therefore:_



_y_ cot( _x_ + _y_ ) _−_ [sin] _[ y]_
_′_ _x_
_y_ =

cos( _y_ ) ln _x −_ cot( _x_ + _y_ )



(pg 6) 1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS


Semester 1 - Calculus I(lec5) Faculty of Computer Science (CS+IT)


_(f) x_ = 2 _[y]_ _−_ 2 _[−][y]_


_Sol_


_Differentiate both sides directly:_




_[dy]_ _[dy]_

_dx_ [+ 2] _[−][y]_ [ ln 2] _dx_




_[dy]_ 1

_dx_ [=] (2 _[y]_ + 2 _[−][y]_ ) ln 2



1 = 2 _[y]_ ln 2 _[dy]_




_[dy]_

_dx_ _[⇒]_ _dx_ _[dy]_



**Exercise 1.2.1** _1. Find_ _[dy]_

_dx_ _[for the following:]_


_(i) y_ = _π_ _[x]_ _−_ _x_ _[π]_


_(ii) y_ = _e_ [sin 3] _[x]_


_(iii) y_ = ln( _x_ [2] _−_ 1)



_Sol_


_Sol_


_Sol_


_Sol_



_Sol_




    - 2 _x −_ _x_
_(iv) y_ = ln

2 _[x]_ + _x_







_(v) y_ = log3




- _x_ 2 _[x]_ _−_ _x_



_(vi) y_ = tan _[−]_ [1][ �] _e_ _[−][x]_ [2][�]



_Sol_


1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS (pg 7)


Faculty of Computer Science (CS+IT) Semester 1 - Calculus I(lec5)



_√_
_(vii) y_ = sin _e_ _[x]_ _−_ 1



_(viii) y_ = [ln(] _[x]_ [) + 1]

ln( _x_ ) _−_ 1



_Sol_


_Sol_



_(ix) y_ = [(] _[x]_ [ + 1)] ~~_[√]_~~ [3] _[√]_



_x_ [2] + 4




~~_[√]_~~ 3
_x_ + 2



_Sol_


_Sol_




     -     - _x_ + 1
_(x) y_ = ln ln

_x −_ 1



��



_(xi) y_ = [sin][4][(] _[x]_ ~~_√_~~ [) cos][3][(] _[x]_ [)]
~~_x_~~


_Sol_


_(xii) xy_ = 2 _[x][−][y]_


_Sol_


_(xiii) y_ + _x_ = _y_ _[x]_


_Sol_


(pg 8) 1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS


Semester 1 - Calculus I(lec5) Faculty of Computer Science (CS+IT)


_2. Find the following limits:_


ln _x_
_(a)_ lim
_x→_ 1 _x −_ 1


_Sol_



1 _−_ _e_ [2] _[x]_
_(b)_ lim
_x→_ 0 _x_



_Sol_



_e_ _[ax]_ _−_ _e_ _[bx]_
_(c)_ lim
_x→_ 0 _x_



_e_ _[−][x]_ _−_ _e_ [2] _[x]_
_(d)_ lim
_x→_ 0 _x_



_Sol_


_Sol_



_e_ _[−][x]_ [2] _−_ 1
_(e)_ lim
_x→_ 0 _x_



_Sol_


1 EXPONENTIAL AND LOGARITHMIC FUNCTIONS (pg 9)


