import sympy as sp
sp.init_printing()  # Agar output lebih rapi di terminal/Jupyter

x = sp.symbols('x')
persamaan = [
    x - 2,
    x**2 - 3*x - 4,
    x**2 - 6*x + 9,
    x**2 - x - 1,
    x**3 - 6*x**2 + 11*x - 6,
    x**3 - 7*x**2 + 15*x - 9,
    x**5 + 7*x**4 - 9*x**2 + 15*x + 2,
    x**5 + 9*x**2 + 2
]

for i, eq in enumerate(persamaan, 1):
    print(f"Soal {i}: {sp.solve(eq, x)}")