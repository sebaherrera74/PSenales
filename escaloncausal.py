# Graficas de funciones singulares
import numpy as np
import matplotlib.pyplot as plt

# INGRESO
u = lambda t: np.piecewise(t,t>=0,[1,0])

a = -10
b = 10
dt = 0.1

# PROCEDIMIENTO
t = np.arange(a, b, dt)
u0 = u(t-0)
#u0 = u(t-2)  

# señal a causal
x = np.exp(-t)*u0

# SALIDA - GRAFICA
plt.figure(2)
plt.plot(t,x)

plt.xlabel('t')
plt.ylabel('x(t)u(t)')
plt.margins(dt)
plt.grid()
plt.show()