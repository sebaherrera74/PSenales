#Ejemplos de transformadas de Fourier
#con sympy

# Importar librerias basicas
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

#sym.init_printing()

t, w = sym.symbols('t omega', real=True)

def fourier_transform(x):
    return sym.integrals.transforms._fourier_transform(x, t, w, 1, -1, 'Fourier')

#t, w = sym.symbols('t omega', real=True)""
#print(t)
#print(w)
"""
----------------Transformada de Fourier de funcion delta de dirac
X = sym.integrate(sym.DiracDelta(t)*sym.exp(-sym.I*w*t), (t, -sym.oo, sym.oo))
X = fourier_transform(sym.DiracDelta(t))
print(X)

"""


class rect(sym.Function):
    @classmethod
    def eval(cls, arg):
        return sym.Heaviside(arg + sym.S.Half) - sym.Heaviside(arg - sym.S.Half)

#print("Ancho del pulso desde cero = 0.5")


sym.plot(rect(t), (t, -4, 4), xlabel=r'$t$', ylabel=r'$x(t)$');
print('La transformada de Fourier de x(t) sera:')

XW = fourier_transform(rect(t))

sym.plot(XW, (w, -30, 30), xlabel=r'$\omega$', ylabel=r'sinc($\omega / 2$)')




