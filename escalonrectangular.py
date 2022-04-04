# Graficas de funciones singulares
import numpy as np
import matplotlib.pyplot as plt

# INGRESO
# Rectangular como u(t-2)-u(t-4)
# u2 = np.piecewise(t,t>=2,[1,0])
# u4 = np.piecewise(t,t>=4,[1,0])

u = lambda t: np.piecewise(t,t>=0,[1,0])

a = -10
b = 10
dt = 0.1

# PROCEDIMIENTO
t = np.arange(a, b, dt)

u2 =np.piecewise(t,t>=2,[1,0])
u4 =np.piecewise(t,t>=4,[1,0])

u2 = u(t-2) 
u4 = u(t-4) 
rectangular = u2 - u4



# SALIDA - GRAFICA
plt.figure(2)
plt.plot(t,rectangular)

plt.xlabel('t')
plt.ylabel('x(t)u(t)')
plt.margins(dt)
plt.grid()
plt.show()