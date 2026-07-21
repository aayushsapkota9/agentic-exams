import os

base_dir = "/Users/aayushsapkota9/repos/oxford/agentic-exams/nm"

questions_data = {
    1: {
        "title": "Solution of Non-linear equations",
        "qns": {
            "1(a)": [
                {
                    "year": "2025 Spring",
                    "text": "a) Solve $x \\log_{10} x = 1.2$ by Newton-Raphson method correct to four decimal places. **[8]**"
                },
                {
                    "year": "2024 Spring",
                    "text": "a) Find the root of the equation $\\cos x + e^x + x^2 = 3$ correct to three decimal places by using Newton Raphson method. **[8]**"
                },
                {
                    "year": "2023 Spring",
                    "text": "a) Explain in brief the errors in numerical calculations. **[8]**"
                }
            ],
            "1(b)": [
                {
                    "year": "2025 Spring",
                    "text": "b) Using Secant Method, find the roots of function $2x - \\log_{10} x - 7 = 0$ correct up to three decimal places. **[7]**\n\n**OR**\n\nFind the root of the equation $f(x) = x^3 - 4x - 10$ correct to three decimal places by using False Position method. **[7]**"
                },
                {
                    "year": "2024 Spring",
                    "text": "b) Find the root of the equation $f(x) = x^3 - 4x - 10$ correct to three decimal places by using False Position method. **[7]**"
                },
                {
                    "year": "2023 Spring",
                    "text": "b) Find a root of $3x + \\sin x - e^x = 0$ using:\n   i. One of the bracketing methods (Bisection or False Position).\n   ii. One of the non-bracketing methods (Secant or Newton-Raphson). **[7]**"
                }
            ],
            "7(a)": [
                {
                    "year": "2024 Spring",
                    "text": "a) Applications of Numerical Methods in Engineering **[5]**"
                }
            ],
            "7(b)": [
                {
                    "year": "2025 Spring",
                    "text": "a) Errors in Numerical Method **[5]**"
                },
                {
                    "year": "2024 Spring",
                    "text": "b) Error in Numerical Method **[5]**"
                }
            ],
            "7(c)": [
                {
                    "year": "2023 Spring",
                    "text": "c) Algorithm of fixed point iteration method **[5]**"
                }
            ]
        }
    },
    2: {
        "title": "Interpolation and approximation",
        "qns": {
            "2(a)": [
                {
                    "year": "2025 Spring",
                    "text": "a) From the following data given in the table below, evaluate $f(2.5)$ by using Lagrange method. **[8]**\n\n| x | 1 | 2 | 4 | 5 | 7 |\n| :--- | :---: | :---: | :---: | :---: | :---: |\n| **f(x)** | 1 | 1.414 | 1.732 | 2.00 | 2.6 |"
                },
                {
                    "year": "2024 Spring",
                    "text": "a) The following table gives the displacement, $x$ (in cms) of an object at various time, $t$ (in seconds). Find the displacement of this object at $t = 1.3$ seconds and $t = 1.5$ seconds, using any suitable interpolation formula. **[8]**\n\n| t | 1.0 | 1.2 | 1.4 | 1.7 |\n| :--- | :---: | :---: | :---: | :---: |\n| **x** | 9.0 | 9.5 | 10.2 | 11.0 |"
                },
                {
                    "year": "2023 Spring",
                    "text": "a) From the data given below, find the number of students whose weight is between 60 to 70 lbs. **[8]**\n\n| Weight in lbs | 0-40 | 40-60 | 60-80 | 80-100 | 100-120 |\n| :--- | :---: | :---: | :---: | :---: | :---: |\n| **No. of students** | 250 | 120 | 100 | 70 | 50 |"
                }
            ],
            "2(b)": [
                {
                    "year": "2025 Spring",
                    "text": "b) From the following table, estimate the number of students who obtained marks between 50 and 55. **[7]**\n\n| Marks | 30-40 | 40-50 | 50-60 | 60-70 | 70-80 |\n| :--- | :---: | :---: | :---: | :---: | :---: |\n| **No. of Students** | 31 | 42 | 51 | 35 | 31 |"
                },
                {
                    "year": "2024 Spring",
                    "text": "b) The growth of bacteria ($N$) in a culture after $t$ hours is given by the following table:\n\n| Time t (hr) | 0 | 1 | 2 | 3 | 4 |\n| :--- | :---: | :---: | :---: | :---: | :---: |\n| **Bacteria N** | 32 | 47 | 65 | 92 | 132 |\n\nIf the relationship between bacteria $N$ and time $t$ is of the form $N = a b^t$. Using least square approximation, estimate the $N$ at $t = 5$ hr. **[7]**"
                },
                {
                    "year": "2023 Spring",
                    "text": "b) Using the method of least squares, fit the curve $y = a x^2 + b$ to the following data. **[7]**\n\n| x | 1 | 2 | 3 | 4 |\n| :--- | :---: | :---: | :---: | :---: |\n| **y** | -1.52 | 0.96 | 8.88 | 7.66 |"
                }
            ]
        }
    },
    3: {
        "title": "Numerical Differentiation and Integration",
        "qns": {
            "3(a)": [
                {
                    "year": "2025 Spring",
                    "text": "a) Compute the Simpson's 1/3 and Simpson's 3/8 rule for $I = \\int_0^1 e^{-x^2} \\, dx$ using a regular partition with subinterval $n=6$. **[8]**"
                },
                {
                    "year": "2024 Spring",
                    "text": "a) Find $I = \\int_{0.2}^{1.4} \\left( \\sin x - \\ln x + e^x \\right) \\, dx$ by using: **[8]**\n   i. Trapezoidal rule\n   ii. Simpson's 1/3 rule\n   iii. Simpson's 3/8 rule"
                },
                {
                    "year": "2023 Spring",
                    "text": "a) Use Romberg's method to compute:\n   $$I = \\int_0^2 \\frac{e^x + \\sin x}{2} \\, dx$$\n   correct up to two decimal places. **[8]**"
                }
            ],
            "3(b)": [
                {
                    "year": "2025 Spring",
                    "text": "b) Use the Romberg integration to find the solution of $I = \\int_0^1 \\frac{1}{1 + x^2} \\, dx$ correct up to three decimal places. **[7]**"
                },
                {
                    "year": "2024 Spring",
                    "text": "b) Use the Romberg integration to find the solution of $I = \\int_0^1 \\frac{dx}{1 + x^2}$ correct up to three decimal places. **[7]**"
                },
                {
                    "year": "2023 Spring",
                    "text": "b) Estimate the approximate derivative of $f(x) = x^2$ at $x=1$ for $h = 0.1, 0.2, 0.05, 0.01$. Use the first-order difference method and find the respective errors. **[7]**"
                }
            ]
        }
    },
    4: {
        "title": "Solution of system of linear algebraic equations",
        "qns": {
            "4(a)": [
                {
                    "year": "2025 Spring",
                    "text": "a) Solve the following system of equations by Gauss elimination method: **[8]**\n   $$3x + 2y + z = 10$$\n   $$2x + 3y + 2z = 14$$\n   $$x + 2y + 3z = 14$$"
                },
                {
                    "year": "2024 Spring",
                    "text": "a) Find the inverse of the square matrix $A$ using Gauss-Jordan elimination method. **[8]**\n   $$A = \\begin{bmatrix} 1 & -2 & 2 \\\\ 2 & 3 & -1 \\\\ 1 & 1 & 2 \\end{bmatrix}$$"
                },
                {
                    "year": "2023 Spring",
                    "text": "a) Apply the factorization method to solve the equation: **[8]**\n   $$3x + 2y + 7z = 4$$\n   $$2x + 3y + z = 5$$\n   $$3x + 4y + z = 7$$"
                }
            ],
            "4(b)": [
                {
                    "year": "2025 Spring",
                    "text": "b) Solve the following system of equations using Crout method: **[7]**\n   $$x + y + z = 4$$\n   $$2x + 4y + 3z = 9$$\n   $$x + 6y + 2z = 8$$\n\n**OR**\n\nFind the largest eigen value and corresponding eigen vector of the matrix:\n   $$A = \\begin{bmatrix} 3 & -1 & 0 \\\\ -2 & 4 & -3 \\\\ 0 & -1 & 1 \\end{bmatrix} **[7]**$$"
                },
                {
                    "year": "2024 Spring",
                    "text": "b) Find the solution of the given simultaneous linear equation using Gauss Seidel method. **[7]**\n   $$6x - 2y + z = 11$$\n   $$-2x + 7y + 2z = 5$$\n   $$x + 2y - 5z = -1$$"
                },
                {
                    "year": "2023 Spring",
                    "text": "b) Using SOR method, solve the following system of equations: **[7]**\n   $$4x + y + 2z = 4$$\n   $$3x + 5y + z = 7$$\n   $$x + y + 3z = 3$$"
                }
            ],
            "5(a)": [
                {
                    "year": "2023 Spring",
                    "text": "a) Find the largest eigen value and the corresponding eigen vector of the matrix using power method: **[8]**\n   $$A = \\begin{bmatrix} 2 & -1 & 0 \\\\ -1 & 2 & -1 \\\\ 0 & -1 & 2 \\end{bmatrix}$$"
                }
            ],
            "7(b)": [
                {
                    "year": "2025 Spring",
                    "text": "b) Ill-conditioned systems **[5]**"
                },
                {
                    "year": "2023 Spring",
                    "text": "b) Algorithm of Gauss Jordan method **[5]**"
                }
            ],
            "7(c)": [
                {
                    "year": "2024 Spring",
                    "text": "c) Ill condition and well-conditioned system **[5]**"
                }
            ]
        }
    },
    5: {
        "title": "Solution of ordinary differential equations",
        "qns": {
            "5(a)": [
                {
                    "year": "2025 Spring",
                    "text": "a) Solve the following differential equation within $0 \\le x \\le 0.3$ using RK 4th order method: **[8]**\n   $$10 \\frac{dy}{dx} = x^2 + y^2, \\quad y(0) = 1 \\quad (\\text{take } h = 0.1)$$"
                },
                {
                    "year": "2024 Spring",
                    "text": "a) Solve the following differential equation within $0 \\le x \\le 0.5$ using RK 4th order method: **[8]**\n   $$10 \\frac{d^2y}{dx^2} + 2 \\frac{dy}{dx} - 3y = 5, \\quad y(0) = 0, \\ y'(0) = 0$$"
                }
            ],
            "5(b)": [
                {
                    "year": "2025 Spring",
                    "text": "b) Apply Euler's method to approximate the value of $y(0.3)$ for the differential equation: **[7]**\n   $$\\frac{dy}{dx} = y + x, \\quad y(0) = 1 \\quad (\\text{take } h = 0.1)$$"
                },
                {
                    "year": "2024 Spring",
                    "text": "b) Using Euler's method (R-K 1st order method), find an approximate value of $y$ corresponding to $x = 1$, given that: **[7]**\n   $$\\frac{dy}{dx} = x + y \\quad \\text{and} \\quad y = 1 \\text{ when } x = 0 \\quad (\\text{take } h = 0.1)$$"
                },
                {
                    "year": "2023 Spring",
                    "text": "b) Using the R-K 1st order method (Euler's method), find an approximate value of $y$ corresponding to $x = 1$, given that: **[7]**\n   $$\\frac{dy}{dx} = x + y \\quad \\text{and} \\quad y = 1 \\text{ when } x = 0 \\quad (\\text{take } h = 0.2)$$"
                }
            ],
            "6(a)": [
                {
                    "year": "2023 Spring",
                    "text": "a) Using the R-K method of fourth order, solve for $y$ at $x = 1.2, 1.4$, from: **[8]**\n   $$\\frac{dy}{dx} = \\frac{2xy + e^x}{x^2 + x e^x}$$\n   given $x_0 = 1, y_0 = 0$."
                }
            ],
            "7(a)": [
                {
                    "year": "2023 Spring",
                    "text": "a) Shooting Method **[5]**"
                }
            ],
            "7(c)": [
                {
                    "year": "2025 Spring",
                    "text": "c) Boundary value problem **[5]**"
                }
            ]
        }
    },
    6: {
        "title": "Numerical solution of Partial differential Equation",
        "qns": {
            "6(a)": [
                {
                    "year": "2025 Spring",
                    "text": "a) For a square bar of size $15\\text{cm} \\times 15\\text{cm}$, calculate the steady state temperature at interior points for the grid size of $5\\text{cm} \\times 5\\text{cm}$, if two adjacent boundaries are held at $100^\\circ\\text{C}$ and the other two at $0^\\circ\\text{C}$. **[8]**"
                },
                {
                    "year": "2024 Spring",
                    "text": "a) Torsion on a square bar of size $15\\text{cm} \\times 15\\text{cm}$. If two of the sides are held at $100^\\circ\\text{C}$ and the other two sides are held at $0^\\circ\\text{C}$. Calculate the steady state temperature at interior points. Assume a grid size of $5\\text{cm} \\times 5\\text{cm}$. **[8]**"
                }
            ],
            "6(b)": [
                {
                    "year": "2025 Spring",
                    "text": "b) Solve the Poisson equation $\\nabla^2 f = 2x^2 + y$ over the square domain $1 \\le x \\le 4, 1 \\le y \\le 4$, with $f = 0$ on the boundary. Take step size in $x$ and $y$ as $h = k = 1$. **[7]**"
                },
                {
                    "year": "2024 Spring",
                    "text": "b) Solve the Poisson equation $\\nabla^2 f = 2x^2 + y$ over the square domain $1 \\le x \\le 4, 1 \\le y \\le 4$, with $f = 0$ on the boundary. Take step size in $x$ and $y$ as $h = k = 1$. **[7]**"
                },
                {
                    "year": "2023 Spring",
                    "text": "b) Solve the elliptic equation $u_{xx} + u_{yy} = 0$ over a square mesh of side four units satisfying the following boundary conditions: **[7]**\n   - $u(0,y) = 0$ for $0 < y < 4$\n   - $u(4,y) = 12 + y$ for $0 < y < 4$\n   - $u(x,0) = 3x$ for $0 < x < 4$\n   - $u(x,4) = x^2$ for $0 < x < 4$"
                }
            ]
        }
    }
}

for ch_num, info in questions_data.items():
    file_path = os.path.join(base_dir, f"chap{ch_num}", f"chap{ch_num}-qns.md")
    
    # Generate navigation menu
    labels = sorted(list(info["qns"].keys()))
    nav_links = [f"[{lbl}](#{lbl.replace('(', '').replace(')', '')})" for lbl in labels]
    nav_menu = " | ".join(nav_links)
    
    md_content = f"# Chapter {ch_num}: {info['title']} - Past Questions\n"
    md_content += "### Quick Navigation\n"
    md_content += nav_menu + "\n\n---\n\n"
    
    for label in labels:
        md_content += f"## {label}\n\n"
        
        for qn in info["qns"][label]:
            md_content += f"##### {qn['year']} - Pokhara University\n"
            md_content += qn["text"] + "\n\n"
            md_content += "```markdown\n"
            md_content += qn["text"] + "\n"
            md_content += "```\n\n"
            md_content += "---\n\n"
            
    # Remove the trailing "---"
    if md_content.endswith("---\n\n"):
        md_content = md_content[:-7]
        
    with open(file_path, "w") as f:
        f.write(md_content)
    print(f"Created {file_path}")
