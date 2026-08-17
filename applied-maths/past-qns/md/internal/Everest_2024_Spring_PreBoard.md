# Everest Engineering College
*(Affiliated to Pokhara University)*  

### Pre-Board Exam
**Level:** Bachelor | **Semester:** IV Spring | **Year:** 2024  
**Programme:** B.E. Computer / IT  
**Subject:** Applied Mathematics  
**Full Marks:** 50 (scaled or full) | **Pass Marks:** 23 | **Time:** 1.5 hrs. (or 3 hrs. for full paper)

---

*Attempt all the questions.*

---

#### 1.
a) Define analyticity of a complex-valued function $f(z)$. Does differentiability always imply analyticity? Justify with a suitable example. State and prove the necessary conditions (Cauchy-Riemann equations) for a complex-valued function $f(z) = u + i v$ to be analytic in a domain $D$. **[8]**

b) Define a harmonic function. Is $u = \sin x \cosh y$ harmonic? If yes, find a corresponding harmonic conjugate and the corresponding analytic function $f(z)$. **[7]**

---

#### 2.
a) State and prove Cauchy's Integral Theorem. Is it possible to apply Cauchy's Integral Theorem to evaluate the integral:
$$\oint_C \frac{e^z}{z^2 + 4} \, dz$$
where $C$ is the ellipse $x^2 + 4y^2 = 4$, counter-clockwise? Justify. **[8]**

b) Expand $f(z) = \frac{7z-2}{(z+1)(z-3)}$ in a Laurent series valid for:
1. $0 < |z+1| < 1$
2. $1 < |z+1| < 3$
3. $|z+1| > 3$
**[7]**

---

#### 3.
a) State Cauchy's Residue Theorem. Use it to evaluate the following integral:
$$\oint_C \frac{e^z}{z^2 + 4} \, dz$$
where $C: |z| = 3$ counter-clockwise. **[8]**

b) Define Z-transform. State and prove the First Shifting Theorem of Z-transform. Also, prove that:
$$Z(n^2) = \frac{z(z+1)}{(z-1)^3}$$
and then use it to find $Z(n^2 e^{-an})$. **[7]**

**OR**

Define the convolution of two discrete-time functions $f(n)$ and $g(n)$. State and prove the Convolution Theorem of Z-transform. **[7]**

---

#### 4.
a) Solve the difference equation by using Z-transform:
$$y_{n+2} - 4y_{n+1} + 4y_n = 2^n$$
with $y_0 = 0$, $y_1 = 1$. **[7]**

b) Derive the one-dimensional wave equation with necessary assumptions. **[8]**

**OR**

Find the deflection $u(x, t)$ of a vibrating string of length $L$ with $c = 1$, if the initial deflection is zero and the initial velocity is:
$$g(x) = \begin{cases} 
x, & 0 \le x < \frac{L}{2} \\ 
L - x, & \frac{L}{2} \le x < L 
\end{cases}$$
**[8]**

---

#### 5.
a) Find the temperature function $u(x, t)$ in a laterally insulated thin copper bar of length $L$ with constant cross-section, whose endpoints at $x = 0$ and $x = L$ are kept at $0^\circ\text{C}$ and whose initial temperature is $f(x) = \sin^3\left(\frac{\pi x}{L}\right)$. Use $c^2 = 0.175\text{ cm}^2/\text{sec}$. **[7]**

b) Express the Laplacian $\nabla^2 u = u_{xx} + u_{yy}$ in polar coordinates. **[8]**

---

#### 6.
a) Find the Fourier integral representation of the function:
$$f(x) = \begin{cases} 
e^{-x}, & x > 0 \\ 
0, & x < 0 
\end{cases}$$
and show that at $x = 0$ it converges to $\frac{1}{2}$. **[7]**

b) Find the Fourier sine transform of $e^{-x}$ and by using Parseval's Identity, show that:
$$\int_0^\infty \frac{x^2}{(1 + x^2)^2} \, dx = \frac{\pi}{4}$$
**[8]**

---

#### 7. Answer the following questions: **[4 x 2.5 = 10]**
a) Find the bilinear transformation $w = f(z)$ which maps $z_1 = \infty, z_2 = 1, z_3 = 0$ onto the points $w_1 = 0, w_2 = i, w_3 = \infty$. Also, find its fixed points.
b) Find $Z(3n^2 - 2n + 1)$.
c) State and prove the Initial Value Theorem of Z-transform.
d) Let $f(x)$ be continuous on $\mathbb{R}$, $f(t) \to 0$ as $t \to \infty$, and $f'(x)$ be absolutely integrable on $\mathbb{R}$. Show that:
$$\mathcal{F}_c\{f'(x)\} = \omega \mathcal{F}_s\{f(x)\} - \sqrt{\frac{2}{\pi}} f(0)$$
