# Señales- Operaciones


import numpy as np
import matplotlib.pyplot as plt

# INGRESO - tiempo [a,b)
fx = lambda t: np.sin(t)
a  = 0
b  = 40
dt = 0.1
k  = 1  # desplazamiento

# PROCEDIMIENTO
t = np.arange(a,b,dt)
senal=fx(t)
# Escalamiento en tiempo
factor = 5

expande  = fx(t/factor)
#comprime = fx(factor*t)

# SALIDA
plt.plot(t,senal,label='x(t)')
plt.plot(t,expande,label='expande=x(t/factor)')
#plt.plot(t,comprime,label='comprime=x(t*factor)')
plt.axvline(0, color='gray')
plt.axhline(0, color='gray')
plt.xlabel('t')
plt.legend(loc='lower left')
plt.show()
