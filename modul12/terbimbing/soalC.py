import sympy as sp

x, t, w, y, s = sp.symbols('x t w y s')
hasil = [
    sp.integrate(x**3, (x, 0, 2)),
    sp.integrate(x**4, (x, -1, 2)),
    sp.integrate(3*x**2 - 2*x + 3, (x, 0, 2)),
    sp.integrate(4*x**3 + 7, (x, 1, 2)),
    sp.integrate(1/w**2, (w, 1, 4)),
    sp.integrate(2/t**3, (t, 1, 3)),
    sp.integrate(sp.sqrt(t), (t, 0, 2)),
    sp.integrate(w**(sp.Rational(1,3)), (w, 1, 8)),
    sp.integrate(y**2 + 1/y**3, (y, 0, 1)),
    sp.integrate((s**4 - 8)/s**2, (s, 1, 4)),
    sp.integrate(sp.cos(x), (x, 0, sp.pi/2)),
    sp.integrate(2*sp.sin(t), (t, sp.pi/6, sp.pi/2)),
    sp.integrate(2*x**4 - 3*x**2 + 5, (x, 0, 1)),
    sp.integrate(x**(sp.Rational(4,3)) - 2*x**(sp.Rational(1,3)), (x, 0, sp.pi/2))
]

for i, h in enumerate(hasil, 1):
    print(f"No. {i}: {h}")