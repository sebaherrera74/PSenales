import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Definir los nodos y sus valores (corrigiendo la longitud)
x_nodes = np.array([-0.5, 0.0, 0.25, 1.0, 1.718])  # 5 nodos
y_nodes = np.array([0.732, 1.0, 1.268, 1.718, 1.718])  # 5 valores correspondientes

# Crear la spline cúbica natural
cs = CubicSpline(x_nodes, y_nodes, bc_type='natural')

# Definir el rango para la curva "real"
x_real = np.linspace(-0.5, 1.718, 400)  # Valores de x desde -0.5 hasta 1.718
y_real = np.exp(x_real) - x_real**3    # La función real f(x) = e^x - x^3

# Graficar la spline y la función real
plt.figure(figsize=(12, 6))
plt.plot(x_real, y_real, label='Curva Real: $f(x) = e^x - x^3$', color='blue')
plt.plot(x_nodes, y_nodes, 'o', label='Nodos', color='red')  # Puntos de nodos
plt.plot(x_real, cs(x_real), label='Spline Cúbica Natural', color='orange')  # Spline cúbica
plt.title('Interpolación con Spline Cúbica Natural')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.axhline(0, color='black', lw=0.5, ls='--')  # Línea horizontal en y=0
plt.axvline(0, color='black', lw=0.5, ls='--')  # Línea vertical en x=0
plt.show()
