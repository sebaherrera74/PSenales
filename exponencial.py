# Señales continuas

import numpy as np
import matplotlib.pyplot as plt

# INGRESO parámetros

#fx = lambda t: np.exp(abs(t))

#ejemplo de funciones exponenciales 
#funcion exponencial 
#fx = lambda t: np.exp(t)

#funcion exponencial con exponente negativo
#fx = lambda t: np.exp(-t)

#funcion exponencial negativa
fx = lambda t: -(np.exp(t))
t0 = 0
tn = 8

n = 50

# PROCEDIMIENTO
# vector de tiempo
dt = (tn-t0)/n
ti = np.arange(t0,tn,dt)

# señal
senal = fx(ti)


# SALIDA
'''
np.set_printoptions(precision = 4)
print('tiempo: ')
print(ti)
print('señal: x(t) ')
print(senal)

'''
# Gráfica
plt.plot(ti,senal)
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.xlabel('t')
plt.ylabel('señal x[(t)]')
plt.show()
