# Señales No periodicas contínuas


import numpy as np
import matplotlib.pyplot as plt

# ingresar parametros
T = 2*np.pi
fx = lambda t: t**2   #Cuadrada 
#fx = lambda t: t**3   #Al cubo 
#fx = lambda t: np.exp(t) #exponencial
#fx = lambda t: 1/t               
m  = 1 #periodos para la grafica
t0 = 0
n  = 50

# PROCEDIMIENTO
# vector de tiempo
tn = T*m
dt = (tn-t0)/n
ti  = np.arange(t0,tn,dt)

# señal
senal = fx(ti)

# SALIDA
# Grafica
plt.plot(ti,senal)
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.xlabel('t')
plt.ylabel('señal x[(t)]')
plt.show()