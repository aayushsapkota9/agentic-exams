# Chapter 5: Solution of Ordinary Differential Equations
**Pokhara University - Past Exam Questions Repository**

---

### Quick Navigation
[Question 5(a)](#question-5a) | [Question 5(b)](#question-5b) | [Question 6(a)](#question-6a) | [Question 6(b)](#question-6b) | [Question 7(a)](#question-7a) | [Question 7(c)](#question-7c)

---

## Question 5(a)

### 2025
* **Fall (New):** Solve by using Euler's method:
  $$\frac{dy}{dx} = \frac{2x + e^x}{x^2 + x e^x}, \quad \text{given } y(1) = 0, \text{ for } y \text{ at } x = 1.04 \text{ taking } h = 0.01$$
* **Fall:** Using the R-K $1^{\text{st}}$ order method, find an approximate value of $y$ corresponding to $x = 1$, given that $\frac{dy}{dx} = \frac{y-x}{y+x}$ and $y = 1$ when $x = 0$, and $h = 0.02$.
* **Spring (New):** Find the solution of the given ordinary differential equation at $x = 0.5$ using the step size of $h = 0.25$ using RK4 method:
  $$\frac{dy}{dx} = x + y, \quad y(0) = 1$$
* **Spring:** Solve the differential equation $y' = y - \frac{2x}{y}$ using Modified Euler's method within $0 \le x \le 0.2$ with initial condition $y(0) = 1$ and step size $h = 0.2$.

### 2024
* **Fall (New):** Solve $\frac{dy}{dx} = x + y$, given $y(0) = 1$, when $x = 0.3$ taking $h = 0.1$ using modified Euler's method.
* **Spring (New):** Solve the following differential equation within $0 \le x \le 0.3$ using RK-$4^{\text{th}}$ order Method:
  $$10 \frac{dy}{dx} = x^2 + y^2, \quad y(0) = 1 \text{ with } h = 0.1$$
* **Spring:** Solve the following differential equation within $0 \le x \le 0.5$ using RK $4^{\text{th}}$ order method:
  $$10 \frac{d^2y}{dx^2} + 2 \frac{dy}{dx} - 3y = 5, \quad y(0) = 0, y'(0) = 0$$

### 2022
* **Fall:** Using Euler's (R-K $1^{\text{st}}$ order method) find an approximate value of $y$ corresponding to $x = 1$, given that $\frac{dy}{dx} = x + y$ and $y = 1$ when $x = 0$, $h = 0.1$.

### 2021
* **Spring:** Use Runge-Kutta of order four to find the solution of the given differential equation at $x = 1.5$ taking a step size of $h = 0.25$:
  $$\frac{dy}{dx} + 2y = x^2, \quad y(1) = 5$$

---

## Question 5(b)

### 2025
* **Fall (New):** Solve the differential equation by RK-4 method:
  $$y'' - xy' + y = 0 \quad \text{with initial condition } y(0) = 3, y'(0) = 0 \text{ for } y(0.2) \text{ taking } h = 0.2$$
* **Fall:** Find the solution of the given ordinary differential equation at $x = 0.5$ using the step size of $h = 0.25$ using Heun's method:
  $$\frac{dy}{dx} + 0.4y = 3e^{-x}, \quad y(0) = 5$$
* **Spring (New):** Solve the following equation for $y(0.2)$ using shooting method:
  $$\frac{d^2y}{dx^2} + 2 \frac{dy}{dx} - 3y = 6x \quad \text{Given } y(0) = 0, y'(0) = 1$$
* **Spring:** Solve $y' = x + y, y(0) = 1$ by Taylor's series method. Hence find the value of $y$ at $x = 0.1$ and $x = 0.2$.

### 2024
* **Fall (New):** Applying Runge-Kutta fourth order method, find an approximate value of $y$ when $x = 0.2$ given that $y' = x + y$ and $y(0) = 1$.
* **Fall:** Use Taylor series method to solve the ordinary differential equation:
  $$\frac{dy}{dx} = x^2 + y^2 \quad \text{for } x = 0.5 \text{ subject to the initial condition: } y(0) = 1$$
* **Spring (New):** Apply Euler's method to approximate the value of $y(0.3)$ for the differential equation: $\frac{dy}{dx} = y + x, \quad y(0) = 1$.
* **Spring:** Using the Euler's (R-K $1^{\text{st}}$ order method) find an approximate value of $y$ corresponding to $x = 1$, given that $\frac{dy}{dx} = x + y$ and $y = 1$ when $x = 0$, $h = 0.1$.

### 2023
* **Fall (New):** Solve the following differential equation for $y(0.4)$ using Heun's method:
  $$\frac{d^2y}{dx^2} + 2 \frac{dy}{dx} - 3y = 6x \quad \text{with } y(0) = 0 \text{ and } y'(0) = 1 \quad (\text{take } h = 0.2)$$
* **Spring:** Using the R-K $1^{\text{st}}$ order method, find an approximate value of $y$ corresponding to $x = 1$, given that $\frac{dy}{dx} = \frac{y-x}{y+x}$ and $y = 1$ when $x = 0$, and $h = 0.02$.

### 2022
* **Fall:** Apply Euler's method to approximate the value of $y(0.3)$ for the differential equation:
  $$\frac{dy}{dx} = y + x, \quad y(0) = 1$$

### 2021
* **Fall:** Apply R-K-4 method to solve for $y(0.2)$ for the given equation:
  $$\frac{d^2y}{dx^2} + x \frac{dy}{dx} - y = 0$$
  given that $y = 1$ and $\frac{dy}{dx} = 0$ when $x = 0$.
* **Spring:** Find the solution of the given ordinary differential equation at $x = 0.5$ using the step size of $h = 0.25$ using Heun's method:
  $$\frac{dy}{dx} + 0.4y = 3e^{-x}, \quad y(0) = 5$$

---

## Question 6(a)

### 2025
* **Fall:** Solve the given differential equation by RK-$4^{\text{th}}$ order method:
  $$y'' - x^2 y' - 2xy = 0 \quad \text{with initial condition } y(0) = 1, y'(0) = 0, \text{ for } y(0.1) \text{ taking } h = 0.1$$
* **Spring:** Solve the equation $\frac{d^2y}{dx^2} = 6xy^2 + y, y(0) = 1 \text{ and } y'(0) = 0$ to find $y(0.2)$ and $y'(0.2)$, using RK-4 method (take $h = 0.2$).

### 2024
* **Fall:** Solve $\frac{dy}{dx} = x + z$, $\frac{dz}{dx} = x - y$ for $x = 1.5$, given that $y = z = 1$ at $x = 1$ by using Euler's method (take $h = 0.1$).

### 2023
* **Fall (New):** Use Euler's method to solve the following equation for $y(1)$ using $h = 0.25$:
  $$\frac{dy}{dx} = x + y + xy, \quad y(0) = 1$$
* **Fall (Old):** Solve the following equation for $y(0.2)$ using shooting method:
  $$\frac{d^2y}{dx^2} + 2 \frac{dy}{dx} - 3y = 6x \quad \text{Given } y(0) = 0, y'(0) = 1$$
* **Spring:** Using the R-K method of fourth order, solve for $y$ at $x = 1.2, 1.4$, from:
  $$\frac{dy}{dx} = \frac{2xy + e^x}{x^2 + x e^x}, \quad \text{given } x_0 = 1, y_0 = 0$$

---

## Question 6(b)

### 2023
* **Fall (Old):** Use Picard's method to approximate the value of $y$ when $x=0.1$, $x=0.2$ and $x=0.4$, given that $y=1$ at $x=0$ and $\frac{dy}{dx} = 1 + xy$ correct to three decimal places (Use upto second approximations).

### 2021
* **Fall:** Consider the second order initial value problem:
  $$y'' - 4y' + 2y = e^t \sin(t) \quad \text{with } y(0) = 0.4 \text{ and } y'(0) = -0.6$$
  Using Heun's method, find the value of $y(0.2)$ and $y'(0.2)$.

---

## Question 7(a) 
*(Short Notes / Theory)*

### 2023
* **Fall (New):** Initial Value problems and Boundary value problems
* **Spring:** Shooting Method

### 2021
* **Fall:** Taylor's series for solving ODE

---

## Question 7(c) 
*(Short Notes / Theory)*

### 2025
* **Spring (New):** Review of ODEs

### 2024
* **Fall (New):** Shooting method
* **Fall:** Shooting method
* **Spring (New):** Boundary value problem
