# Lec 6 - Tabular Method

Dr. Hiba Omer

---

## Example 4 - Tabular Method

The tabular method is a convenient way to organize repeated integration by parts. It is useful when one factor differentiates to zero after a finite number of steps.

Evaluate:

\[
\int x^2 e^x \, dx
\]

Let:

\[
f(x)=x^2,\qquad g(x)=e^x
\]

Construct the table:

| Differentiate \(f(x)\) | Sign | Integrate \(g(x)\) |
|---|---:|---|
| \(x^2\) | \(+\) | \(e^x\) |
| \(2x\) | \(-\) | \(e^x\) |
| \(2\) | \(+\) | \(e^x\) |
| \(0\) | | |

Multiply diagonally and use alternating signs:

\[
\int x^2 e^x\,dx
=
x^2e^x
-
2xe^x
+
2e^x
+
C
\]

Therefore:

\[
\boxed{
\int x^2 e^x\,dx
=
e^x(x^2-2x+2)+C
}
\]

---

## Example 5 - Definite Integral with Tabular Method

Find:

\[
\frac{1}{\pi}\int_0^\pi x^3\cos(nx)\,dx
\]

where \(n\) is a positive integer.

Let:

\[
f(x)=x^3,\qquad g(x)=\cos(nx)
\]

Construct the table:

| Differentiate \(f(x)\) | Sign | Integrate \(g(x)\) |
|---|---:|---|
| \(x^3\) | \(+\) | \(\frac{1}{n}\sin(nx)\) |
| \(3x^2\) | \(-\) | \(-\frac{1}{n^2}\cos(nx)\) |
| \(6x\) | \(+\) | \(-\frac{1}{n^3}\sin(nx)\) |
| \(6\) | \(-\) | \(\frac{1}{n^4}\cos(nx)\) |
| \(0\) | | |

Thus:

\[
\int x^3\cos(nx)\,dx
=
\frac{x^3}{n}\sin(nx)
+
\frac{3x^2}{n^2}\cos(nx)
-
\frac{6x}{n^3}\sin(nx)
-
\frac{6}{n^4}\cos(nx)
\]

Apply the bounds \(0\) and \(\pi\):

\[
\frac{1}{\pi}\int_0^\pi x^3\cos(nx)\,dx
=
\frac{1}{\pi}
\left[
\frac{x^3}{n}\sin(nx)
+
\frac{3x^2}{n^2}\cos(nx)
-
\frac{6x}{n^3}\sin(nx)
-
\frac{6}{n^4}\cos(nx)
\right]_0^\pi
\]

Since \(\sin(n\pi)=0\), \(\sin(0)=0\), \(\cos(n\pi)=(-1)^n\), and \(\cos(0)=1\):

\[
\frac{1}{\pi}\int_0^\pi x^3\cos(nx)\,dx
=
\frac{1}{\pi}
\left[
\frac{3\pi^2(-1)^n}{n^2}
-
\frac{6(-1)^n}{n^4}
+
\frac{6}{n^4}
\right]
\]

Therefore:

\[
\boxed{
\frac{1}{\pi}\int_0^\pi x^3\cos(nx)\,dx
=
\frac{3\pi^2 n^2(-1)^n-6(-1)^n+6}{\pi n^4}
}
\]

---

## Example 6 - Recurring Integrals

Evaluate:

\[
\int e^x\sin(x)\,dx
\]

Let:

\[
I=\int e^x\sin(x)\,dx
\]

Apply integration by parts once:

\[
u=e^x,\qquad dv=\sin(x)\,dx
\]

\[
du=e^x\,dx,\qquad v=-\cos(x)
\]

Then:

\[
I
=
-e^x\cos(x)
+
\int e^x\cos(x)\,dx
\]

Apply integration by parts again to \(\int e^x\cos(x)\,dx\):

\[
u=e^x,\qquad dv=\cos(x)\,dx
\]

\[
du=e^x\,dx,\qquad v=\sin(x)
\]

\[
\int e^x\cos(x)\,dx
=
e^x\sin(x)
-
\int e^x\sin(x)\,dx
\]

Substitute back:

\[
I
=
-e^x\cos(x)
+
e^x\sin(x)
-
I
\]

Thus:

\[
2I=e^x(\sin(x)-\cos(x))
\]

Therefore:

\[
\boxed{
\int e^x\sin(x)\,dx
=
\frac{e^x}{2}(\sin(x)-\cos(x))+C
}
\]
