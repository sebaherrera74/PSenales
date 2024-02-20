# Señales continuas

import numpy as np
import matplotlib.pyplot as plt

# INGRESO parámetros

#fx = lambda t: np.exp(abs(t))

#ejemplo de funciones exponenciales 
#funcion exponencial 
#fx = lambda t: np.exp(t)
A=1
w=2*np.pi*30
#funcion exponencial con exponente negativo
fx = lambda t: A*np.exp(-w*t)

#funcion exponencial negativa
#fx = lambda t: -(np.exp(t))
t0 = 0
tn =0.2

n = 10000

# PROCEDIMIENTO
# vector de tiempo
dt = (tn-t0)/n
ti = np.arange(t0,tn,dt)

# señal
senal = fx(ti)


###########Senoidal##############
# INGRESO parámetros
frecuencia=39
w  = 2*np.pi*frecuencia
fx2 = lambda t: np.sin(w*t)* 1*np.exp(-w*t)
#t0 = 0
#tn = 1
#n = 1000

# PROCEDIMIENTO
# vector de tiempo
#dt = (tn-t0)/n
#ti = np.arange(t0,tn,dt)

# señal
senal2 = fx2(ti)



# SALIDA
'''
np.set_printoptions(precision = 4)
print('tiempo: ')
print(ti)
print('señal: x(t) ')
print(senal)

'''


senalcompuesta=senal+senal2

# Gráfica
plt.plot(ti,senalcompuesta)
plt.axhline(0, color='gray')
plt.axvline(0, color='gray')
plt.xlabel('t')
plt.ylabel('señal x[(t)]')
plt.show()


