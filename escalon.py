# Señales modelo varias
# propuesta: edelros@espol.edu.ec
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

# SALIDA - GRAFICA
import matplotlib.pyplot as plt
plt.figure(1)
plt.plot(t,u0)

plt.xlabel('t')
plt.ylabel('escalon u(t)')
plt.margins(dt)
plt.grid()
plt.show()