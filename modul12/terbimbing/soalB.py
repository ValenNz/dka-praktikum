import sympy as sp

x = sp.symbols('x')
fungsi = [
    x**3 + 3*x**2 + 6*x,
    x**5 + x**4,
    (3*x + 5)**3,
    (3 - 5*x)**5,
    sp.sin(7*x),
    sp.sin(x**3),
    1/(x - 1),
    3*x/(1 - x)
]

for i, f in enumerate(fungsi, 1):
    print(f"No. {i}: {sp.diff(f, x)}")