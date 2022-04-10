# Señales de Energía y Potencia


import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

# INGRESO - Parámetros
w  = 1
fx = lambda t: np.sin(w*t)
a  = 0
b  = 2*np.pi # un periodo T
dte = 0.005

# PROCEDIMIENTO
T  = 2*np.pi/w
te = np.arange(a,b,dte)
xe = fx(te)

# energía en un periodo
cuadradoxe = xe**2
energiaxe  = integrate.simps(cuadradoxe,te)

# potencia en un periodo
potenciaxe = (1/T)*energiaxe

# SALIDA
print('la energia de xe es: ',energiaxe)
print('la potencia de xe es: ',potenciaxe)
# gráfica
plt.plot(te,xe,label='xe')
plt.fill_between(te,0,cuadradoxe,color='lightgreen')
plt.plot(te,cuadradoxe,'g--', label='xe^2')



plt.xlabel('t')
plt.legend()
plt.show()
