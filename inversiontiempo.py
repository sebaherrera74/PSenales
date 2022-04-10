
import numpy as np
import matplotlib.pyplot as plt

# INGRESO - tiempo [a,b)
fx = lambda t: np.sin(t)
a  = 0
b  = 10
dt = 0.1
k  = 1  # desplazamiento

# PROCEDIMIENTO
t = np.arange(a,b,dt)
senal=fx(t)

# inversion en tiempo
espejo = fx(-t)

# SALIDA
plt.plot(t,senal,label='x(t)')
plt.plot(t,espejo,label='espejo=x(-t)')
plt.axvline(0, color='gray')
plt.axhline(0, color='gray')
plt.xlabel('t')
plt.legend(loc='lower left')
plt.show()