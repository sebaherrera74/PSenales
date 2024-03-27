"""Funcion Escalon (Headviside)"""




import sympy as sym
sym.init_printing()
t, sigma, omega = sym.symbols('t sigma omega', real=True)
step = sym.Heaviside(t)
#sym.plot(step, (t, -2, 2), ylim=[-0.2, 1.2], ylabel=r'$\epsilon(t)$');

"""ejemplo de como aplicar la funcion escalon con una cosenoidal"""

x = sym.cos(omega*t) * sym.Heaviside(t)
sym.plot(x.subs(omega, 2), (t, -2, 10), ylim=[-1.2, 1.2], ylabel=r'$x(t)$');