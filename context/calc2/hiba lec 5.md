
# Lecture 05 — Integration by Parts

Dr. Mohamed Ali Mohamed  
Faculty of Engineering and Architecture  
Fall 2024

---

## Definition

If \(u\) and \(v\) are differentiable functions:

\[
\frac{d}{dx}(uv)=u\frac{dv}{dx}+v\frac{du}{dx}
\]

Rearranging:

\[
u\,dv=d(uv)-v\,du
\]

Integrating both sides:

\[
\int u\,dv = uv - \int v\,du
\]

This is the formula for **Integration by Parts**.

---

# LIATE Rule

To select \(u\), use the LIATE priority:

1. Logarithmic
2. Inverse trigonometric
3. Algebraic
4. Trigonometric
5. Exponential

---

# Example 1

Evaluate:

\[
\int xe^x\,dx
\]

Choose:

\[
u=x \quad \Rightarrow \quad du=dx
\]

\[
dv=e^x dx \quad \Rightarrow \quad v=e^x
\]

Apply integration by parts:

\[
\int xe^x dx = xe^x - \int e^x dx
\]

\[
= xe^x - e^x + C
\]

\[
= e^x(x-1)+C
\]

---

# Example 2

Evaluate:

\[
\int x\sin x\,dx
\]

Choose:

\[
u=x \Rightarrow du=dx
\]

\[
dv=\sin x\,dx \Rightarrow v=-\cos x
\]

Then:

\[
\int x\sin x\,dx
=
-x\cos x+\int \cos x\,dx
\]

\[
=-x\cos x+\sin x+C
\]

---

# Example 3

Evaluate:

\[
\int x^2 \ln x\,dx
\]

Choose:

\[
u=\ln x \Rightarrow du=\frac{1}{x}dx
\]

\[
dv=x^2dx \Rightarrow v=\frac{x^3}{3}
\]

Apply integration by parts:

\[
\int x^2\ln x\,dx
=
\frac{x^3}{3}\ln x
-
\int \frac{x^3}{3}\cdot \frac{1}{x}dx
\]

\[
=
\frac{x^3}{3}\ln x
-
\frac{1}{3}\int x^2dx
\]

\[
=
\frac{x^3}{3}\ln x
-
\frac{x^3}{9}
+C
\]

---

# Example 4

Evaluate:

\[
\int \tan^{-1}x\,dx
\]

Let:

\[
u=\tan^{-1}x
\Rightarrow
du=\frac{1}{x^2+1}dx
\]

\[
dv=dx
\Rightarrow
v=x
\]

Then:

\[
\int \tan^{-1}x\,dx
=
x\tan^{-1}x
-
\int \frac{x}{x^2+1}dx
\]

\[
=
x\tan^{-1}x
-
\frac{1}{2}\ln(x^2+1)
+C
\]

---

# Example 5

Evaluate:

\[
\int \ln x\,dx
\]

Let:

\[
u=\ln x
\Rightarrow
du=\frac{1}{x}dx
\]

\[
dv=dx
\Rightarrow
v=x
\]

Then:

\[
\int \ln x\,dx
=
x\ln x
-
\int x\cdot \frac{1}{x}dx
\]

\[
=
x\ln x - x + C
\]

---

# Example 6

Evaluate:

\[
I=\int \sqrt{x^2+a^2}\,dx
\]

Let:

\[
u=\sqrt{x^2+a^2}
\]

Then:

\[
du=\frac{x}{\sqrt{x^2+a^2}}dx
\]

Also:

\[
dv=dx
\Rightarrow
v=x
\]

Apply integration by parts:

\[
I
=
x\sqrt{x^2+a^2}
-
\int \frac{x^2}{\sqrt{x^2+a^2}}dx
\]

Rewrite:

\[
x^2=(x^2+a^2)-a^2
\]

So:

\[
I
=
x\sqrt{x^2+a^2}
-
\int \sqrt{x^2+a^2}dx
+
a^2\int \frac{dx}{\sqrt{x^2+a^2}}
\]

\[
I=x\sqrt{x^2+a^2}-I+a^2\sinh^{-1}\left(\frac{x}{a}\right)
\]

\[
2I
=
x\sqrt{x^2+a^2}
+
a^2\sinh^{-1}\left(\frac{x}{a}\right)
\]

Therefore:

\[
I
=
\frac{1}{2}x\sqrt{x^2+a^2}
+
\frac{a^2}{2}\sinh^{-1}\left(\frac{x}{a}\right)
+C
\]

---

# Example 7

Evaluate:

\[
I=\int e^{3x}\cos 2x\,dx
\]

Choose:

\[
u=e^{3x}
\Rightarrow
du=3e^{3x}dx
\]

\[
dv=\cos 2x\,dx
\Rightarrow
v=\frac{1}{2}\sin 2x
\]

Then:

\[
I
=
\frac{1}{2}e^{3x}\sin 2x
-
\frac{3}{2}\int e^{3x}\sin 2x\,dx
\]

Integrate again by parts:

\[
\int e^{3x}\sin 2x\,dx
\]

Choose:

\[
u=e^{3x}
\Rightarrow
du=3e^{3x}dx
\]

\[
dv=\sin 2x\,dx
\Rightarrow
v=-\frac{1}{2}\cos 2x
\]

Then:

\[
I
=
\frac{1}{2}e^{3x}\sin 2x
+
\frac{3}{4}e^{3x}\cos 2x
-
\frac{9}{4}I
\]

So:

\[
\left(1+\frac{9}{4}\right)I
=
\frac{1}{2}e^{3x}\sin 2x
+
\frac{3}{4}e^{3x}\cos 2x
\]

\[
\frac{13}{4}I
=
\frac{1}{2}e^{3x}\sin 2x
+
\frac{3}{4}e^{3x}\cos 2x
\]

Hence:

\[
I
=
\frac{e^{3x}}{13}
\left(
2\sin 2x + 3\cos 2x
\right)
+C
\]