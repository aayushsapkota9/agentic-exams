# Pokhara University
### Level: Bachelor | Semester: Fall | Year: 2025
**Programme:** B.E.  
**Course:** Numerical Methods (New)  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) Using bisection method, find where the graph $y = x - 6$ and $y = \ln(x)$ intersects. Write your answer correct to three decimal places. **[7]**  
**OR**  
Find the real root of $x^5 - 3x^3 - 1 = 0$ correct to four decimal places using secant method.

b) Find the square root of 7 using Newton Raphson method correct to 4 decimal places. **[8]**

---

#### 2.
a) Estimate the value of $\sin\theta$ at $\theta = 45$ using Newton's backward interpolation: **[7]**

| $\theta$ | 10 | 20 | 30 | 40 | 50 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **$\sin\theta$** | 0.1736 | 0.3420 | 0.5 | 0.6428 | 0.7660 |

**OR**  
Fit a second order polynomial to the following data:

| x | 1 | 2 | 3 | 4 |
| :--- | :---: | :---: | :---: | :---: |
| **y** | 6 | 11 | 18 | 27 |

b) Find a cubic polynomial $f(x)$ from the following table using Lagrange interpolation method. Also, use the polynomial to find $f(1.5)$: **[8]**

| x | 0 | 1 | 2 | 3 |
| :--- | :---: | :---: | :---: | :---: |
| **f(x)** | 1 | 2 | 1 | 10 |

---

#### 3.
a) The distance covered by a particle at any time is given in the table below: **[7]**

| Time (t, sec) | 5 | 6 | 7 | 8 |
| :--- | :---: | :---: | :---: | :---: |
| **Distance (d, m)** | 10.0 | 18.6 | 23.5 | 33.4 |

Calculate the velocity of the particle at $t = 6\text{ sec}$.

b) Evaluate the integral $I = \int_0^{0.6} e^{x^2} \, dx$ for $n = 6$, by using: **[8]**  
   i. Trapezoidal rule.  
   ii. Simpson's 1/3rd rule.  
   iii. Simpson's 3/8th rule.  

---

#### 4.
a) Solve the following system of equations using Doolittle's method: **[7]**
$$2x + 3y + z = 9$$
$$x + 2y + 3z = 6$$
$$3x + y + 2z = 8$$

b) Find the largest Eigen value and corresponding Eigen vector from the following matrix: **[8]**
$$\begin{bmatrix} 2 & 4 & 1 \\ 0 & 2 & 3 \\ 1 & 0 & 3 \end{bmatrix}$$
using power method.

---

#### 5.
a) Solve by using Euler's method: **[7]**
$$\frac{dy}{dx} = \frac{2x + e^x}{x^2 + x e^x}, \quad \text{given } y(1) = 0, \text{ for } y \text{ at } x = 1.04 \text{ taking } h = 0.01$$

b) Solve the differential equation by RK-4 method: **[8]**
$$y'' - xy' + y = 0 \quad \text{with initial condition } y(0) = 3, y'(0) = 0 \text{ for } y(0.2) \text{ taking } h = 0.2$$

---

#### 6.
a) Solve the elliptic equation $u_{xx} + u_{yy} = 0$ for the following square mesh with boundary values as shown in figure: **[7]**
- Top boundary: 0, 500, 1000, 500, 0
- Bottom boundary: 0, 500, 1000, 500, 0
- Left boundary: 0, 1000, 2000, 1000, 0
- Right boundary: 0, 1000, 2000, 1000, 0
- Grid interior nodes:
  - Row 1: $u_1, u_2, u_3$
  - Row 2: $u_4, u_5, u_6$
  - Row 3: $u_7, u_8, u_9$

b) Solve Poisson's equation $u_{xx} + u_{yy} = 2 + x^2 y$ over a square domain of $0 \le x \le 3$ and $0 \le y \le 3$ with $u = 0$ on the boundary and mesh length $h = 1$. **[8]**

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Importance of numerical computation in the field of science and engineering  
b) Ill conditioned and well conditioned system  
c) Application of interpolation  
