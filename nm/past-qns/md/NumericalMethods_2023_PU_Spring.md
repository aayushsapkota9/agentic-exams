# Pokhara University
### Level: Bachelor | Semester: Spring | Year: 2023
**Programme:** B.E.  
**Course:** Numerical Methods  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) Explain in brief the errors in numerical calculations. **[8]**

b) Find a root of $3x + \sin x - e^x = 0$ using: **[7]**
   i. One of the bracketing methods (Bisection or False Position).
   ii. One of the non-bracketing methods (Secant or Newton-Raphson).

---

#### 2.
a) From the data given below, find the number of students whose weight is between 60 to 70 lbs. **[8]**
| Weight in lbs | 0-40 | 40-60 | 60-80 | 80-100 | 100-120 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **No. of students** | 250 | 120 | 100 | 70 | 50 |

b) Using the method of least squares, fit the curve $y = a x^2 + b$ to the following data. **[7]**
| x | 1 | 2 | 3 | 4 |
| :--- | :---: | :---: | :---: | :---: |
| **y** | -1.52 | 0.96 | 8.88 | 7.66 |

---

#### 3.
a) Use Romberg's method to compute: **[8]**
   $$I = \int_0^2 \frac{e^x + \sin x}{2} \, dx$$
   correct up to two decimal places.

b) Estimate the approximate derivative of $f(x) = x^2$ at $x=1$ for $h = 0.1, 0.2, 0.05, 0.01$. Use the first-order difference method and find the respective errors. **[7]**

---

#### 4.
a) Apply the factorization method to solve the equation: **[8]**
   $$3x + 2y + 7z = 4$$
   $$2x + 3y + z = 5$$
   $$3x + 4y + z = 7$$

b) Using SOR method, solve the following system of equations: **[7]**
   $$4x + y + 2z = 4$$
   $$3x + 5y + z = 7$$
   $$x + y + 3z = 3$$

---

#### 5.
a) Find the largest eigen value and the corresponding eigen vector of the matrix using power method: **[8]**
   $$A = \begin{bmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{bmatrix}$$

b) Using the R-K 1st order method (Euler's method), find an approximate value of $y$ corresponding to $x = 1$, given that: **[7]**
   $$\frac{dy}{dx} = x + y \quad \text{and} \quad y = 1 \text{ when } x = 0 \quad (\text{take } h = 0.2)$$

---

#### 6.
a) Using the R-K method of fourth order, solve for $y$ at $x = 1.2, 1.4$, from: **[8]**
   $$\frac{dy}{dx} = \frac{2xy + e^x}{x^2 + x e^x}$$
   given $x_0 = 1, y_0 = 0$.

b) Solve the elliptic equation $u_{xx} + u_{yy} = 0$ over a square mesh of side four units satisfying the following boundary conditions: **[7]**
   - $u(0,y) = 0$ for $0 < y < 4$
   - $u(4,y) = 12 + y$ for $0 < y < 4$
   - $u(x,0) = 3x$ for $0 < x < 4$
   - $u(x,4) = x^2$ for $0 < x < 4$

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Shooting Method  
b) Algorithm of Gauss Jordan method  
c) Algorithm of fixed point iteration method  
