import numpy as np

# We want to solve:
# x + y + z = 4
# A x + B y + C z = D
# E x + F y + G z = H
#
# From OCR:
# Eq 1: x + y + z = 4 (very likely)
# Eq 2: 2x+4y+3z=8 or 2x+4y+2z=8 or 2x+4y+3z=9 or 2x+4y+3z=10
# Eq 3: x+6y+2z=6 or x+5y+2z=6 or x+6y+z=6
#
# Let's search for combination with small integer solution (x, y, z) and small integer coefficients.

eq1 = [1, 1, 1, 4]

candidates_eq2 = [
    [2, 4, 3, 8],
    [2, 4, 3, 9],
    [2, 4, 3, 10],
    [2, 4, 2, 8],
    [1, 4, 3, 8],
    [1, 4, 3, 9],
    [2, 3, 4, 8],
    [2, 3, 4, 9]
]

candidates_eq3 = [
    [1, 6, 2, 6],
    [1, 6, 2, 8],
    [1, 5, 2, 6],
    [1, 6, 3, 6],
    [1, 2, 6, 6]
]

for c2 in candidates_eq2:
    for c3 in candidates_eq3:
        M = np.array([
            [1, 1, 1],
            [c2[0], c2[1], c2[2]],
            [c3[0], c3[1], c3[2]]
        ])
        B = np.array([4, c2[3], c3[3]])
        try:
            sol = np.linalg.solve(M, B)
            if np.all(np.abs(sol - np.round(sol)) < 1e-9):
                # Integer solution found! Let's filter for reasonable range (e.g. x,y,z between -5 and 5)
                if np.all(np.abs(sol) <= 5) and np.all(np.abs(sol) >= -5):
                    print(f"Match: Eq 1: x+y+z=4 | Eq 2: {c2[0]}x+{c2[1]}y+{c2[2]}z={c2[3]} | Eq 3: {c3[0]}x+{c3[1]}y+{c3[2]}z={c3[3]} => Sol: {sol}")
        except np.linalg.LinAlgError:
            pass
