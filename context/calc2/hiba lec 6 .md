# Lec 6 — Tabular Method

Dr Hiba Omer

---

# Example 4 — Tabular Method

The tabular method is a convenient way to organize repeated integration by parts.

Evaluate:

\[
\int x^2 e^x \, dx
\]

Let:

\[
f(x)=x^2
\]

\[
g(x)=e^x
\]

Construct the table:

| Differentiate \(f(x)\) | Integrate \(g(x)\) |
|---|---|
| \(x^2\) | \(e^x\) |
| \(2x\) | \(e^x\) |
| \(2\) | \(e^x\) |
| \(0\) | |

Apply alternating signs:

\[
\int x^2 e^x dx
=
x^2 e^x
-
2x e^x
+
2 e^x
+
C
\]

Factor:

\[
=
e^x(x^2-2x+2)+C
\]

---

# Example 5

Find:

\[
\int x^2 \cos(nx)\,dx
\]

where \(n\) is a positive integer.

Let:

\[
f(x)=x^2
\]

\[
g(x)=\cos(nx)
\]

Table:

| Differentiate | Integrate |
|---|---|
| \(x^2\) | \(\frac{1}{n}\sin(nx)\) |
| \(2x\) | \(-\frac{1}{n^2}\cos(nx)\) |
| \(2\) | \(-\frac{1}{n^3}\sin(nx)\) |
| \(0\) | |

Using alternating signs:

\[
\int x^2\cos(nx)\,dx
=
\frac{x^2}{n}\sin(nx)
+
\frac{2x}{n^2}\cos(nx)
-
\frac{2}{n^3}\sin(nx)
+
C
\]

---

# Example 6 — Recurring Integrals

Evaluate:

\[
\int e^x \sin(x)\,dx
\]

Let:

\[
I=\int e^x \sin(x)\,dx
\]

Apply integration by parts:

Choose:

\[
u=e^x
\Rightarrow
du=e^x dx
\]

\[
dv=\sin(x)\,dx
\Rightarrow
v=-\cos(x)
\]

Then:

\[
I
=
-e^x\cos(x)
+
\int e^x\cos(x)\,dx
\]

Integrate again by parts:

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
2I
=
e^x(\sin(x)-\cos(x))
\]

Therefore:

\[
I
=
\frac{e^x}{2}
(\sin(x)-\cos(x))
+
C
\]

Hence:

\[
\boxed{
\int e^x\sin(x)\,dx
=
\frac{e^x}{2}
(\sin(x)-\cos(x))
+
C
}
\]