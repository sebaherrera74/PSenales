import numpy as np
import matplotlib.pyplot as plt

# INGRESO - parámetros
N=20   #Periodo
#w0=0
#w0=2*np.pi/N
#w0=22*np.pi/N
#w0=2*np.pi           #igual a w0=0
w0=2*np.pi*4.576    #Ejemplo de que una señal no es peridodica cuando f0 no es racional
#w0 = np.pi/12
#w0 = np.pi/4
#w0 = np.pi/2
#w0 = np.pi             #--Tasa de oscilacion mas alta
#w0 = 2*np.pi/12

fx = lambda n: A*np.cos(w0*n)
n0 = 0   #Valor inicial
m =8   #Valor constante
A=1    #amplitud

muestras=(m*N+1)

# PROCEDIMIENTO
# vector n discreto [n,m)
n = np.arange(n0,n0+muestras,1)

# señal
senal=fx(n)

# SALIDA

#print(n)

#print(senal)

# Gráficas
plt.stem(n,senal)
plt.xlabel('n')
plt.ylabel('señal f[n]')
plt.show()
