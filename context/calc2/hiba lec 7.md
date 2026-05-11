# Lecture 07

Dr. Mohamed Ali Mohamed  
Faculty of Engineering and Architecture  
Fall 2024

---

# Standard Integrals

1.

\[
\int \frac{dx}{\sqrt{a^2-x^2}}
\]

2.

\[
\int \sqrt{a^2-x^2}\,dx
\]

3.

\[
\int \frac{dx}{\sqrt{a^2+x^2}}
\]

4.

\[
\int \sqrt{a^2+x^2}\,dx
\]

5.

\[
\int \frac{dx}{\sqrt{x^2-a^2}}
\]

6.

\[
\int \sqrt{x^2-a^2}\,dx
\]

---

# 1.

Evaluate:

\[
\int \frac{dx}{\sqrt{a^2-x^2}}
\]

Put:

\[
x=a\sin\theta
\]

Then:

\[
dx=a\cos\theta\,d\theta
\]

Substitute:

\[
\int \frac{dx}{\sqrt{a^2-x^2}}
=
\int
\frac{a\cos\theta\,d\theta}
{\sqrt{a^2-a^2\sin^2\theta}}
\]

\[
=
\int
\frac{a\cos\theta\,d\theta}
{a\cos\theta}
\]

\[
=
\int d\theta
=
\theta+C
\]

Since:

\[
\theta=\sin^{-1}\left(\frac{x}{a}\right)
\]

Therefore:

\[
\int \frac{dx}{\sqrt{a^2-x^2}}
=
\sin^{-1}\left(\frac{x}{a}\right)+C
\]

---

# 2.

Evaluate:

\[
\int \sqrt{a^2-x^2}\,dx
\]

Put:

\[
x=a\sin\theta
\]

Then:

\[
dx=a\cos\theta\,d\theta
\]

Substitute:

\[
\sqrt{a^2-a^2\sin^2\theta}
=
a\cos\theta
\]

Thus:

\[
\int \sqrt{a^2-x^2}\,dx
=
a^2\int \cos^2\theta\,d\theta
\]

Use identity:

\[
\cos^2\theta
=
\frac{1+\cos 2\theta}{2}
\]

Then:

\[
=
\frac{a^2}{2}
\int (1+\cos2\theta)\,d\theta
\]

\[
=
\frac{a^2}{2}
\left(
\theta+\frac{1}{2}\sin2\theta
\right)+C
\]

Using:

\[
\sin2\theta=2\sin\theta\cos\theta
\]

\[
=
\frac{a^2}{2}\theta
+
\frac{a^2}{2}\sin\theta\cos\theta
+C
\]

Convert back:

\[
\sin\theta=\frac{x}{a}
\]

\[
\cos\theta=\frac{\sqrt{a^2-x^2}}{a}
\]

Hence:

\[
\int \sqrt{a^2-x^2}\,dx
=
\frac{a^2}{2}\sin^{-1}\left(\frac{x}{a}\right)
+
\frac{x}{2}\sqrt{a^2-x^2}
+C
\]

---

# 3.

Evaluate:

\[
\int \frac{dx}{\sqrt{a^2+x^2}}
\]

Put:

\[
x=a\sinh\theta
\]

Then:

\[
dx=a\cosh\theta\,d\theta
\]

Substitute:

\[
\sqrt{a^2+a^2\sinh^2\theta}
=
a\cosh\theta
\]

Thus:

\[
\int \frac{dx}{\sqrt{a^2+x^2}}
=
\int d\theta
=
\theta+C
\]

Since:

\[
\theta=\sinh^{-1}\left(\frac{x}{a}\right)
\]

Therefore:

\[
\int \frac{dx}{\sqrt{a^2+x^2}}
=
\sinh^{-1}\left(\frac{x}{a}\right)+C
\]

---

# 4.

Evaluate:

\[
\int \sqrt{a^2+x^2}\,dx
\]

Put:

\[
x=a\sinh\theta
\]

Then:

\[
dx=a\cosh\theta\,d\theta
\]

Using:

\[
\cosh^2\theta-\sinh^2\theta=1
\]

Substitute:

\[
\int \sqrt{a^2+x^2}\,dx
=
a^2\int \cosh^2\theta\,d\theta
\]

Use identity:

\[
\cosh^2\theta
=
\frac{\cosh2\theta+1}{2}
\]

Then:

\[
=
\frac{a^2}{2}
\int (\cosh2\theta+1)\,d\theta
\]

\[
=
\frac{a^2}{2}
\left(
\frac{\sinh2\theta}{2}
+
\theta
\right)
+C
\]

Since:

\[
\sinh2\theta=2\sinh\theta\cosh\theta
\]

\[
=
\frac{a^2}{2}
\sinh\theta\cosh\theta
+
\frac{a^2}{2}\theta
+C
\]

Back substitute:

\[
\sinh\theta=\frac{x}{a}
\]

\[
\cosh\theta=\sqrt{1+\frac{x^2}{a^2}}
\]

Therefore:

\[
\int \sqrt{a^2+x^2}\,dx
=
\frac{x}{2}\sqrt{a^2+x^2}
+
\frac{a^2}{2}
\sinh^{-1}\left(\frac{x}{a}\right)
+C
\]

---

# 5.

Evaluate:

\[
\int \frac{dx}{\sqrt{x^2-a^2}}
\]

Put:

\[
x=a\cosh\theta
\]

Then:

\[
dx=a\sinh\theta\,d\theta
\]

Substitute:

\[
\sqrt{a^2\cosh^2\theta-a^2}
=
a\sinh\theta
\]

Thus:

\[
\int \frac{dx}{\sqrt{x^2-a^2}}
=
\int d\theta
=
\theta+C
\]

Since:

\[
\theta=\cosh^{-1}\left(\frac{x}{a}\right)
\]

Therefore:

\[
\int \frac{dx}{\sqrt{x^2-a^2}}
=
\cosh^{-1}\left(\frac{x}{a}\right)+C
\]

---

# 6.

Evaluate:

\[
\int \sqrt{x^2-a^2}\,dx
\]

