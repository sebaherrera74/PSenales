""" Funcion exponecial compleja"""




import sympy as sym
sym.init_printing()

t, sigma, omega = sym.symbols('t sigma omega', real=True)

s = sigma + 1j*omega
print(type(s))
x = sym.exp(s*t)
y = x.subs({omega: 10, sigma: -.1})
print(sym.re(y))
print(type(y))
#sym.plot(sym.re(y), (t, 0, 2*sym.pi), ylabel=r'Re{$e^{st}$}')
#sym.plot(sym.im(y), (t, 0, 2*sym.pi), ylabel=r'Im{$e^{st}$}');