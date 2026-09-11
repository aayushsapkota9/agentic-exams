# Chapter 6: Numerical Solution of Partial Differential Equations
**Pokhara University - Past Exam Questions Repository**

---

### Quick Navigation
[Question 5(b)](#question-5b) | [Question 6(a)](#question-6a) | [Question 6(b)](#question-6b) | [Question 7(b)](#question-7b) | [Question 7(c)](#question-7c)

---

## Question 5(b)

### 2023
* **Fall (Old):** Solve the Laplace equation $u_{xx} + u_{yy} = 0$ for the square mesh with boundary values as shown in the figure:
  - Top boundary: 200, 300, 200 (corners 0)
  - Bottom boundary: 200, 300, 200 (corners 0)
  - Left boundary: 400, 500, 400
  - Right boundary: 400, 500, 400
  - Grid interior nodes:
    - Row 1: $u_1, u_2, u_3$
    - Row 2: $u_4, u_5, u_6$
    - Row 3: $u_7, u_8, u_9$

---

## Question 6(a)

### 2025
* **Fall (New):** Solve the elliptic equation $u_{xx} + u_{yy} = 0$ for the following square mesh with boundary values as shown in figure:
  - Top boundary: 0, 500, 1000, 500, 0
  - Bottom boundary: 0, 500, 1000, 500, 0
  - Left boundary: 0, 1000, 2000, 1000, 0
  - Right boundary: 0, 1000, 2000, 1000, 0
  - Grid interior nodes:
    - Row 1: $u_1, u_2, u_3$
    - Row 2: $u_4, u_5, u_6$
    - Row 3: $u_7, u_8, u_9$
* **Spring (New):** Solve the Poisson equation $\nabla^2 f = 2x^2 y^2$ over the square domain $0 \le x \le 3, 0 \le y \le 3$, with $f = 0$ on the boundary and $h = 1$.

### 2024
* **Fall (New):** Solve the equation $u_{xx} + u_{yy} = 0$ for the square mesh with the boundary values as shown in the figure:
  - Top boundary: 60, 60, 60, 60
  - Bottom boundary: 0, 10, 20, 30
  - Left boundary: 0, 20, 40, 60
  - Right boundary: 30, 40, 50, 60
* **Spring (New):** For square bar of size $15\text{ cm} \times 15\text{ cm}$, calculate the steady state temperature at interior points for the grid size of $5\text{ cm} \times 5\text{ cm}$:
  - Top boundary: $0^\circ\text{C}, 0^\circ\text{C}$
  - Bottom boundary: $100^\circ\text{C}, 100^\circ\text{C}$
  - Left boundary: $100^\circ\text{C}, 100^\circ\text{C}$
  - Right boundary: $0^\circ\text{C}, 0^\circ\text{C}$
  - Interior Nodes: $T_1, T_2; T_3, T_4$
* **Spring:** Torsion on a square bar of size $15\text{ cm} \times 15\text{ cm}$. If two of the sides are held at $100^\circ\text{C}$ and the other two sides are held at $0^\circ\text{C}$, calculate the steady state temperature at interior points. Assume a grid size of $5\text{ cm} \times 5\text{ cm}$.

### 2022
* **Fall:** Torsion on a square bar of size $15\text{ cm} \times 15\text{ cm}$. If two of the sides are held at $100^\circ\text{C}$ and the other two sides are held at $0^\circ\text{C}$, calculate the steady state temperature at interior points. Assume a grid size of $5\text{ cm} \times 5\text{ cm}$.

### 2021
* **Fall:** In a square bar with dimension of $3\text{ inch} \times 3\text{ inch}$, torsion function, $\phi$, can be obtained from the following P.D.E:
  $$\frac{\partial^2 \phi}{\partial x^2} + \frac{\partial^2 \phi}{\partial y^2} = -2$$
  where $\phi = 0$ on the outer boundary of the bar's cross-section. Subdivide the region into nine equal squares to form a mesh and find the values of $\phi$ in the interior nodes.
* **Spring:** Determine the steady-state heat distribution in a thin square metal plate with dimensions $0.5\text{ m} \times 0.5\text{ m}$ using $n = m = 4$. Two adjacent boundaries are held at $0^\circ\text{C}$, and the heat on the other boundaries increases linearly from $0^\circ\text{C}$ at one corner to $100^\circ\text{C}$ where the sides meet.

---

## Question 6(b)

### 2025
* **Fall (New):** Solve Poisson's equation $u_{xx} + u_{yy} = 2 + x^2 y$ over a square domain of $0 \le x \le 3$ and $0 \le y \le 3$ with $u = 0$ on the boundary and mesh length $h = 1$.
* **Fall:** Solve the Poisson equation $\nabla^2 f = 2x^2 + y$ over the square domain $1 \le x \le 4, 1 \le y \le 4$, with $f = 0$ on the boundary. Take step size in $x$ and $y$, $h = k = 1$.
* **Spring (New):** Solve the elliptic equation $u_{xx} + u_{yy} = 0$ over a square mesh of side four units satisfying the following boundary conditions:
  - $u(0,y) = 0$ for $0 \le y \le 4$
  - $u(4,y) = 12 + y$ for $0 \le y \le 4$
  - $u(x,0) = 3x$ for $0 \le x \le 4$
  - $u(x,4) = x^2$ for $0 \le x \le 4$
* **Spring:** Solve the Poisson equation $\nabla^2 f = 2x^2 + y$ over the square domain $1 \le x \le 4, 1 \le y \le 4$, with $f = 0$ on the boundary. Take step size in $x$ and $y$, $h = k = 1$.

### 2024
* **Fall (New):** Solve the equation $\nabla^2 f = x^2 y + 2$ over the square domain $0 \le x \le 3, 0 \le y \le 3$, with $f = 0$ on the boundary and $h = 1$.
* **Fall:** Solve Poisson's equation $u_{xx} + u_{yy} = 243(x^2 + y^2)$ over a square domain $0 \le x \le 1, 0 \le y \le 1$ with step size $h = 1/3$ with $u = 100$ on the boundary.
* **Spring (New):** Solve the Poisson equation $\nabla^2 f = 2x^2 + y$ over the square domain $1 \le x \le 4, 1 \le y \le 4$, with $f = 0$ on the boundary. Take step size in $x$ and $y$, $h = k = 1$.
* **Spring:** Solve the Poisson equation $\nabla^2 f = 2x^2 + y$ over the square domain $1 \le x \le 4, 1 \le y \le 4$, with $f = 0$ on the boundary. Take step size in $x$ and $y$, $h = k = 1$.

### 2023
* **Fall (New):** Solve the Poisson equation $\nabla^2 f = -10(x^2 + y^2 + 10)$ over the square with $0 \le x \le 3$, $0 \le y \le 3$ and $f = 0$ on the boundary. Use $h = 1$.
* **Spring:** Solve the elliptic equation $u_{xx} + u_{yy} = 0$ over a square mesh of side four units satisfying the following boundary conditions:
  - $u(0,y) = 0$ for $0 \le y \le 4$
  - $u(4,y) = 12 + y$ for $0 \le y \le 4$
  - $u(x,0) = 3x$ for $0 \le x \le 4$
  - $u(x,4) = x^2$ for $0 \le x \le 4$

### 2022
* **Fall:** Solve the Poisson equation $\nabla^2 f = 2x^2 + y$ over the square domain $1 \le x \le 4, 1 \le y \le 4$, with $f = 0$ on the boundary. Take step size in $x$ and $y$, $h = k = 1$.

---

## Question 7(b)
*(Short Notes / Theory)*

### 2024
* **Fall:** Overview of PDEs

### 2023
* **Fall (Old):** Partial differential equation and their examples

### 2021
* **Spring:** Laplacian equation

---

## Question 7(c)
*(Short Notes / Theory)*

### 2025
* **Fall:** Classification of Second Order Partial Differential Equation
* **Spring:** Overview of PDEs

### 2023
* **Fall (New):** Schmidt method for one dimensional heat equation

### 2021
* **Fall:** Classify the partial differential equation $u_{xx} + 2u_{xy} + u_{yy} = 0$
* **Spring:** Classification of Second Order Partial Differential Equation