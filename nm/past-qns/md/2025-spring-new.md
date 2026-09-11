# Pokhara University
### Level: Bachelor | Semester: Spring | Year: 2025
**Programme:** B.E.  
**Course:** Numerical Methods (New)  
**Full Marks:** 100 | **Pass Marks:** 45 | **Time:** 3 hrs.

---

*Candidates are required to give their answers in their own words as far as practicable.*  
*The figures in the margin indicate full marks.*

---

### Attempt all the questions.

#### 1.
a) Find the root of the equation $x^3 + x^2 - 3x - 3 = 0$ correct up to three decimal places using Bisection method. **[7]**

b) What are the limitations of NR method? Using NR method, find the root of $\log x - \cos x = 0$ correct up to three decimal places. **[8]**  
**OR**  
Write an algorithm to find a real root of a non-linear equation using secant method.

---

#### 2.
a) The following table gives the population of a town during the last six censuses. Estimate the increase in the population during the period from 1976: **[8]**

| Year | 1941 | 1951 | 1961 | 1971 | 1981 | 1991 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Population (in thousand)** | 12 | 15 | 20 | 27 | 39 | 52 |

**OR**  
The velocity of a rocket is measured at three different times as follows:

| Time, t (s) | 10 | 15 | 20 |
| :--- | :---: | :---: | :---: |
| **Velocity, v(t) (m/s)** | 227.04 | 362.78 | 517.35 |

Using a quadratic Lagrange interpolating polynomial, determine time $t$ at which the rocket's velocity is $300\text{ m/s}$.

b) Fit the equation $y = \frac{1}{ax + b}$ from the given set of data: **[7]**

| x | -5 | -4 | -3 | 0 | 2 | 3 | 6 | 8 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **y** | 0.15 | 0.18 | 0.23 | 2 | -0.5 | -0.31 | -0.143 | -0.1 |

---

#### 3.
a) Evaluate the integral $I = \int_4^{5.2} \log x \, dx$ for $n = 6$ using Simpson's 1/3 rule and 3/8 rule. Compare the result in both conditions. **[7]**

b) Evaluate the integral $\int_{0.5}^{1.5} e^{x^2} \, dx$ using 3-point Gaussian quadrature. **[8]**

---

#### 4.
a) Using the LU Crout decomposition method, solve the following system of equations: **[8]**
$$4x_1 - x_2 + x_3 = 7$$
$$-2x_1 + 6x_2 + x_3 = 9$$
$$-x_1 + x_2 + 7x_3 = -6$$

b) Find the solution of the given simultaneous linear equations using Gauss Seidel method: **[7]**
$$6x_1 - 2x_2 + x_3 = 11$$
$$-2x_1 + 7x_2 + 2x_3 = 5$$
$$x_1 + 2x_2 - 5x_3 = -1$$

---

#### 5.
a) Find the solution of the given ordinary differential equation at $x = 0.5$ using the step size of $h = 0.25$ using RK4 method: **[7]**
$$\frac{dy}{dx} = x + y, \quad y(0) = 1$$

b) Solve the following equation for $y(0.2)$ using shooting method: **[8]**
$$\frac{d^2y}{dx^2} + 2 \frac{dy}{dx} - 3y = 6x \quad \text{Given } y(0) = 0, y'(0) = 1$$

---

#### 6.
a) Solve the Poisson equation $\nabla^2 f = 2x^2 y^2$ over the square domain $0 \le x \le 3, 0 \le y \le 3$, with $f = 0$ on the boundary and $h = 1$. **[7]**

b) Solve the elliptic equation $u_{xx} + u_{yy} = 0$ over a square mesh of side four units satisfying the following boundary conditions: **[8]**
- $u(0,y) = 0$ for $0 \le y \le 4$
- $u(4,y) = 12 + y$ for $0 \le y \le 4$
- $u(x,0) = 3x$ for $0 \le x \le 4$
- $u(x,4) = x^2$ for $0 \le x \le 4$

---

#### 7. Write short notes on: (Any two) **[2 x 5 = 10]**
a) Importance of Numerical methods  
b) Power Method  
c) Review of ODEs  
