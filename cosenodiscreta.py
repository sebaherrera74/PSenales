import numpy as np
import matplotlib.pyplot as plt

# INGRESO - parámetros
#w0=0
w0=2*np.pi/8
#w0=2*np.pi           #igual a w0=0
#w0=2*np.pi*4.576    #Ejemplo de que una señal no es peridodica cuando f0 no es racional       
#w0 = np.pi/12
#w0 = np.pi/4
#w0 = np.pi/2
#w0 = np.pi             #--Tasa de oscilacion mas alta

#w0 = 2*np.pi/12
fx = lambda n: A*np.cos(w0*n)
n0 = 0
m =40
A=1

# PROCEDIMIENTO
# vector n discreto [n,m)
n = np.arange(n0,m+1,1)

# señal
senal = fx(n)

# SALIDA
np.set_printoptions(precision=4)
print('n: ')
print(n)
print('señal x[n]:')
print(senal)

# Gráficas
plt.stem(n, senal)
plt.xlabel('n')
plt.ylabel('señal x[n]')
plt.show()