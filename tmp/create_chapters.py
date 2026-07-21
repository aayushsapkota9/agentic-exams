import os

base_dir = "/Users/aayushsapkota9/repos/oxford/agentic-exams/nm"

units = {
    1: {
        "title": "Solution of Non-linear equations",
        "hours": 5,
        "content": """- **1.1. Introduction, Importance of Numerical Methods**
- **1.2. Approximation and Errors in computation**
- **1.3. Bisection Method**
- **1.4. Secant method**
- **1.5. Newton Raphson method**
- **1.6. Fixed point iterative method**"""
    },
    2: {
        "title": "Interpolation and approximation",
        "hours": 5,
        "content": """- **2.1. Lagrange interpolation**
- **2.2. Finite differences (forward, backward, and divided difference)**
- **2.3. Newton’s Interpolation (forward, backward)**
- **2.4. Least square method of fitting linear and nonlinear curve for discrete data and continuous function**
- **2.5. Cubic Spline Interpolation**"""
    },
    3: {
        "title": "Numerical Differentiation and Integration",
        "hours": 4,
        "content": """- **3.1. Numerical Differentiation formulae**
- **3.2. Trapezoidal, Simpson’s 1/3, 3/8 rule**
- **3.3. Romberg integration**
- **3.4. Gaussian integration (2- point and 3- point formula)**"""
    },
    4: {
        "title": "Solution of system of linear algebraic equations",
        "hours": 6,
        "content": """- **4.1. Gauss elimination method and concept of pivoting**
- **4.2. Ill-conditioned system of linear equations**
- **4.3. LU Factorization method (Dolittle, Crout’s, Cholesky’s)**
- **4.4. Iterative methods (Jacobi method, Gauss‐Seidel method)**
- **4.5. Eigen value and Eigen vector using Power method**"""
    },
    5: {
        "title": "Solution of ordinary differential equations",
        "hours": 6,
        "content": """- **5.1. Review of ordinary differential equations**
- **5.2. Runge-Kutta methods (first, second and fourth) for first and second order differential equations**
- **5.3. Solution of boundary value problem by shooting method**"""
    },
    6: {
        "title": "Numerical solution of Partial differential Equation",
        "hours": 4,
        "content": """- **6.1. Classification of partial differential equation (elliptic, parabolic and hyperbolic)**
- **6.2. Solution of Laplace equation (standard 5-point formula with iterative methods)**
- **6.3. Solution of Poisson equation (finite difference approximation method)**
- **6.4. Solution of one-dimensional Heat equation by Schmidt method**"""
    }
}

for ch_num, info in units.items():
    ch_dir = os.path.join(base_dir, f"chap{ch_num}")
    os.makedirs(ch_dir, exist_ok=True)
    
    syllabus_content = f"""# Unit {ch_num}: {info['title']}
**Total Hours: {info['hours']}**

{info['content']}
"""
    file_path = os.path.join(ch_dir, f"chap{ch_num}-syllabus.md")
    with open(file_path, "w") as f:
        f.write(syllabus_content)
    print(f"Created {file_path}")
