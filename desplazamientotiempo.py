# Señales- Operaciones


import numpy as np
import matplotlib.pyplot as plt

# INGRESO - tiempo [a,b)
fx = lambda t: np.sin(t)
a  = 0
b  = 8
dt = 0.1
k  = 1  # desplazamiento

# PROCEDIMIENTO
t = np.arange(a,b,dt)

senal     = fx(t)
derecha   = fx(t-k)
#izquierda = fx(t+k)

# SALIDA
plt.plot(t,senal,label='x(t)')
plt.plot(t,derecha,label='derecha=x(t-k)')
#plt.plot(t,izquierda,label='izquierda=x(t+k)')
plt.axvline(0, color='gray')
plt.axhline(0, color='gray')
plt.xlabel('t')
plt.legend(loc='lower left')
plt.show()